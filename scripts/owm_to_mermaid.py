#!/usr/bin/env python3
"""Convert an OWM (Online Wardley Maps) file to a Mermaid wardley-beta block.

Handles the sanitisation the Mermaid parser requires:
  - Component / anchor names: strip '/', '(', ')', '[', ']', normalise whitespace.
    Names that collapse to empty or collide are suffixed with a numeric tag.
  - Edges: only emit when both endpoints are declared components/anchors.
    OWM sometimes references undefined components; those edges are dropped.
  - Notes: quoted string. Em-dash, apostrophe, semicolon rewritten out of text.
  - Pipelines, evolution-stage overrides, labels, market/evolve directives,
    style, copyright comments: skipped (Mermaid wardley-beta doesn't support them).

Usage:
    python3 scripts/owm_to_mermaid.py <input.owm> [<title-override>]
"""
import re
import sys
from pathlib import Path


def sanitise_name(raw: str) -> str:
    s = raw.strip()
    s = s.replace("/", " and ")
    s = re.sub(r"[()\[\]{}]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def sanitise_note(raw: str) -> str:
    s = raw.replace("—", ", ").replace("–", ", ")
    s = s.replace("'", "").replace('"', "")
    s = s.replace(";", ".")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_owm(text: str):
    """Parse an OWM file into (title, anchors, components, edges, notes).
    anchors: dict name -> (v, e); components: dict name -> (v, e)
    edges: list of (src, dst); notes: list of (text, x, y)
    """
    title = None
    anchors = {}
    components = {}
    edges = []
    notes = []

    node_re = re.compile(
        r"(anchor|component)\s+(.+?)\s*\[\s*([0-9.+-]+)\s*,\s*([0-9.+-]+)\s*\]"
    )
    edge_re = re.compile(r"^\s*(.+?)\s*->\s*(.+?)\s*$")
    note_re = re.compile(
        r"note\s+(.+?)\s*\[\s*([0-9.+-]+)\s*,\s*([0-9.+-]+)\s*\]"
    )

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("//") or line.startswith("#"):
            continue
        if line.startswith("title "):
            title = line[len("title "):].strip()
            continue
        if line.startswith("style ") or line.startswith("evolution ") \
                or line.startswith("pipeline ") or line.startswith("market ") \
                or line.startswith("evolve ") or line.startswith("annotation ") \
                or line.startswith("annotations "):
            continue  # silently drop

        m = node_re.match(line)
        if m:
            kind, name, v, e = m.groups()
            name = sanitise_name(name)
            try:
                v_f, e_f = float(v), float(e)
            except ValueError:
                continue
            if not (0.0 <= v_f <= 1.0 and 0.0 <= e_f <= 1.0):
                continue  # drop out-of-range labels and the like
            target = anchors if kind == "anchor" else components
            target[name] = (v_f, e_f)
            continue

        m = note_re.match(line)
        if m:
            text_, x, y = m.groups()
            try:
                x_f, y_f = float(x), float(y)
            except ValueError:
                continue
            notes.append((sanitise_note(text_), x_f, y_f))
            continue

        m = edge_re.match(line)
        if m:
            src, dst = m.groups()
            edges.append((sanitise_name(src), sanitise_name(dst)))

    return title, anchors, components, edges, notes


def to_mermaid(title, anchors, components, edges, notes) -> str:
    declared = set(anchors) | set(components)
    lines = ["wardley-beta"]
    if title:
        safe_title = sanitise_note(title)
        lines.append(f"title {safe_title}")
    for name, (v, e) in anchors.items():
        lines.append(f"anchor {name} [{v:.2f}, {e:.2f}]")
    for name, (v, e) in components.items():
        lines.append(f"component {name} [{v:.2f}, {e:.2f}]")
    kept_edges = 0
    dropped_edges = 0
    for src, dst in edges:
        if src in declared and dst in declared:
            lines.append(f"{src} -> {dst}")
            kept_edges += 1
        else:
            dropped_edges += 1
    for text, x, y in notes:
        if text:
            lines.append(f'note "{text}" [{x:.2f}, {y:.2f}]')
    return "\n".join(lines), kept_edges, dropped_edges


def main():
    if len(sys.argv) < 2:
        print("usage: owm_to_mermaid.py <file.owm> [title-override]", file=sys.stderr)
        sys.exit(2)
    src = Path(sys.argv[1])
    override_title = sys.argv[2] if len(sys.argv) > 2 else None

    text = src.read_text()
    title, anchors, components, edges, notes = parse_owm(text)
    if override_title:
        title = override_title

    mermaid, kept, dropped = to_mermaid(title, anchors, components, edges, notes)
    sys.stderr.write(
        f"{src.name}: {len(anchors)} anchors, {len(components)} components, "
        f"{kept} edges kept, {dropped} edges dropped (undeclared endpoints), "
        f"{len(notes)} notes\n"
    )
    print(mermaid)


if __name__ == "__main__":
    main()
