#!/usr/bin/env python3
"""Convert an OWM (Online Wardley Maps) file to a Mermaid wardley-beta block.

Python port of tractorjuice/arc-kit's tests/mermaid-wardley/convert.mjs.

Strategy: always emit double-quoted names. Mermaid's wardley-beta grammar
accepts `STRING | ID | NAME_WITH_SPACES` everywhere a name is expected;
using STRING (double-quoted) avoids every keyword-collision and hyphen
issue. Internal double quotes inside a name are replaced with single quotes.

Preserves: title, evolution, anchor, component (+ build/buy/outsource
decorator + inertia flag + label offset), links, evolve, note, annotation(s),
and pipelines (detected via OWM's `pipeline X [min, max]` + component
proximity, then emitted as mermaid's nested `pipeline "X" { component ... }`
block form).

Drops: `style wardley`, standalone `build/buy/outsource <name>` lines
(used as decorators during component emission), `market <name> [v, e]`
(takes care not to swallow edges starting with "Market"), `x-axis`/`y-axis`,
`ecosystem`, `submap`, `url`, `pioneer`, `settler`, `townplanner`.

Usage:
    python3 scripts/owm_to_mermaid.py <input.owm>
"""
import re
import sys
from pathlib import Path


def quote_name(name: str) -> str:
    """Always-quote — STRING terminal in mermaid wardley-beta grammar."""
    if not name:
        return name
    name = name.strip()
    if name.startswith('"') and name.endswith('"'):
        return name
    return '"' + name.replace('"', "'") + '"'


def convert(owm: str, filename: str = "") -> str:
    lines = owm.split("\n")
    out = ["wardley-beta"]
    has_title = False

    # ── Pass 1: collect sourcing directives, component coords, pipeline ranges
    sourcing = {}               # name(lower) → 'build'|'buy'|'outsource'
    comp_coords = {}            # name(original-case) → {vis, evo}
    pipeline_ranges = {}        # name(original-case) → {min, max}

    SRC_RE = re.compile(r"^(build|buy|outsource)\s+(.+)$", re.I)
    COMP_RE = re.compile(r"^component\s+(.+?)\s*\[\s*([\d.]+)\s*,\s*([\d.]+)\s*\]")
    PIPE_RE = re.compile(r"^pipeline\s+(.+?)\s*\[\s*([\d.]+)\s*,\s*([\d.]+)\s*\]\s*$")

    for raw in lines:
        s = raw.strip()
        if s.startswith("//"):
            continue
        m = SRC_RE.match(s)
        if m:
            sourcing[m.group(2).strip().lower()] = m.group(1).lower()
            continue
        m = COMP_RE.match(s)
        if m:
            comp_coords[m.group(1).strip()] = {
                "vis": float(m.group(2)),
                "evo": float(m.group(3)),
            }
        m = PIPE_RE.match(s)
        if m:
            pipeline_ranges[m.group(1).strip()] = {
                "min": float(m.group(2)),
                "max": float(m.group(3)),
            }

    # ── Pass 1b: detect pipeline children (same visibility ±0.05, evo in range)
    pipeline_children = {}      # parent-name → [{name, evo}, ...]
    is_pipeline_child = set()

    for pipe_name, rng in pipeline_ranges.items():
        parent = comp_coords.get(pipe_name)
        if not parent:
            continue
        children = []
        for c_name, c_coord in comp_coords.items():
            if c_name == pipe_name:
                continue
            if c_name in is_pipeline_child:
                continue
            if (abs(c_coord["vis"] - parent["vis"]) <= 0.05
                    and rng["min"] - 0.01 <= c_coord["evo"] <= rng["max"] + 0.01):
                children.append({"name": c_name, "evo": c_coord["evo"]})
        if children:
            children.sort(key=lambda x: x["evo"])
            pipeline_children[pipe_name] = children
            for c in children:
                is_pipeline_child.add(c["name"])

    # ── Pass 2: emit lines
    in_pipeline_block = False
    pending_pipeline_name = None

    DROP_SINGLE_RE = re.compile(
        r"^(ecosystem|submap|url|pioneer|settler|townplanner)\s+", re.I)
    MARKET_DROP_RE = re.compile(
        r"^market\s+[^\[\]]+\[\s*[\d.]+\s*,", re.I)
    AXIS_DROP_RE = re.compile(r"^[xy]-axis\s+", re.I)

    def inline_comment_strip(s: str) -> str:
        # remove trailing // comment unless part of a URL (://)
        m = re.match(r"^(.+?)\s+//(?!/)(.*)$", s)
        if m and "://" not in m.group(1):
            return m.group(1).strip()
        return s

    for raw in lines:
        s = raw.strip()
        if not s:
            out.append("")
            continue
        if s.startswith("//"):
            continue
        s = inline_comment_strip(s)
        if not s:
            continue

        # Directives to drop entirely
        if re.match(r"^style\s+wardley\s*$", s, re.I):
            continue
        if re.match(r"^(build|buy|outsource)\s+", s, re.I):
            continue
        if AXIS_DROP_RE.match(s):
            continue
        if MARKET_DROP_RE.match(s):
            continue
        if DROP_SINGLE_RE.match(s):
            continue

        # title
        if re.match(r"^title\s+", s, re.I):
            out.append(s)
            out.append("size [1100, 800]")
            has_title = True
            continue

        # evolution
        if re.match(r"^evolution\s+", s, re.I):
            out.append(s)
            continue

        # anchor
        m = re.match(r"^anchor\s+(.+?)\s*(\[[\d.,\s]+\])", s, re.I)
        if m:
            out.append(f"anchor {quote_name(m.group(1).strip())} {m.group(2)}")
            continue

        # pipeline X [min, max]  — drop; children are emitted inside the block
        if re.match(r"^pipeline\s+.+\[\s*[\d.]+\s*,\s*[\d.]+\s*\]\s*$", s, re.I):
            continue

        # pipeline X { ... }  or  pipeline X   (followed later by `{`)
        m = re.match(r"^pipeline\s+(.+?)(?:\s*\{)?\s*$", s, re.I)
        if m and re.match(r"^pipeline\s+", s, re.I) and not re.search(r"\[[\d]", s):
            pname = quote_name(m.group(1).strip())
            if "{" in s:
                out.append(f"pipeline {pname} {{")
                in_pipeline_block = True
            else:
                pending_pipeline_name = pname
            continue
        if pending_pipeline_name and s == "{":
            out.append(f"pipeline {pending_pipeline_name} {{")
            in_pipeline_block = True
            pending_pipeline_name = None
            continue
        if (in_pipeline_block or pending_pipeline_name) and s == "}":
            if pending_pipeline_name:
                pending_pipeline_name = None
            else:
                out.append("}")
                in_pipeline_block = False
            continue

        # component
        m = re.match(r"^component\s+(.+?)\s*(\[[\d.,\s]+\])", s, re.I)
        if m:
            cname = m.group(1).strip()
            coords = m.group(2)
            has_inertia = bool(re.search(r"\binertia\s*$", s, re.I))

            if cname in is_pipeline_child:
                continue

            qname = quote_name(cname)

            if in_pipeline_block:
                inner = coords.strip("[] ").strip()
                out.append(f'  component {qname} [{inner}]')
            else:
                line = f"component {qname} {coords}"
                decorators = []
                if cname.lower() in sourcing:
                    decorators.append(f"({sourcing[cname.lower()]})")
                if has_inertia:
                    decorators.append("(inertia)")
                if decorators:
                    line += " " + " ".join(decorators)
                out.append(line)

                # Emit pipeline block if this component is a pipeline parent
                children = pipeline_children.get(cname)
                if children:
                    out.append(f"pipeline {qname} {{")
                    for ch in children:
                        out.append(f'  component {quote_name(ch["name"])} [{ch["evo"]}]')
                    out.append("}")
            continue

        # evolve
        m = re.match(r"^evolve\s+(.+?)\s+([\d.]+)", s, re.I)
        if m:
            out.append(f"evolve {quote_name(m.group(1).strip())} {m.group(2)}")
            continue

        # note "text" [v, e]  — text may or may not already be quoted
        m = re.match(r"^note\s+(.+?)\s+(\[[\d.,\s]+\])\s*$", s, re.I)
        if m:
            note_text = m.group(1).strip()
            coord = m.group(2)
            # strip trailing OWM label offset inside the text if any
            lbl_idx = note_text.rfind("] label ")
            if lbl_idx > 0:
                note_text = note_text[:lbl_idx + 1]
            note_text = note_text.strip('"')
            out.append(f'note "{note_text.replace(chr(34), chr(39))}" {coord}')
            continue

        # annotations [x, y]
        if re.match(r"^annotations\s+\[", s, re.I):
            out.append(s)
            continue

        # annotation N, [x, y] text
        m = re.match(r"^annotation\s+(\d+)\s*,?\s*(\[[\d.,\s]+\])\s*(.*)$", s, re.I)
        if m:
            num = m.group(1)
            coords = m.group(2)
            text = m.group(3).strip()
            if text and not text.startswith('"'):
                text = '"' + text.replace('"', "'") + '"'
            if text:
                out.append(f"annotation {num},{coords} {text}")
            else:
                out.append(f"annotation {num},{coords}")
            continue

        # link (edge)
        if "->" in s and not re.match(
                r"^(evolve|component|pipeline|anchor|note)\s", s, re.I):
            link = s
            annotation = ""
            semi = link.find(";")
            if semi > 0:
                annotation = link[semi:]
                link = link[:semi].strip()
            arrow = link.find("->")
            if arrow > 0:
                left = quote_name(link[:arrow].strip())
                right = quote_name(link[arrow + 2:].strip())
                link = f"{left} -> {right}"
            out.append(link + annotation)
            continue

        # unknown — silently skip

    # If no title was found, synthesise one from the filename.
    if not has_title and filename:
        base = Path(filename).stem.replace("-", " ").replace("_", " ")
        out.insert(1, f"title {base}")
        out.insert(2, "size [1100, 800]")

    # Collapse consecutive blank lines
    cleaned = []
    last_empty = False
    for ln in out:
        if ln == "":
            if not last_empty:
                cleaned.append(ln)
            last_empty = True
        else:
            cleaned.append(ln)
            last_empty = False
    return "\n".join(cleaned)


def main():
    if len(sys.argv) < 2:
        print("usage: owm_to_mermaid.py <file.owm>", file=sys.stderr)
        sys.exit(2)
    src = Path(sys.argv[1])
    mermaid = convert(src.read_text(), str(src))
    sys.stderr.write(f"{src.name}: {mermaid.count(chr(10)) + 1} lines emitted\n")
    print(mermaid)


if __name__ == "__main__":
    main()
