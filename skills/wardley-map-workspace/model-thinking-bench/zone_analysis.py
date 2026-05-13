#!/usr/bin/env python3
"""Per-zone coverage analysis.

Test the hypothesis: Opus's coverage lead is concentrated in commoditised
components (training-data recall), not in Genesis ones (novel reasoning).

For each cell, classify every reference component by its band on Wardley's
own placement, then ask: what fraction of Wardley's Genesis components did
each model match? Custom? Product? Commodity?
"""
from __future__ import annotations
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
REPO = ROOT.parents[2]
sys.path.insert(0, str(REPO / "skills/wardley-map-workspace/iteration-10"))
from compare import parse_owm, fuzzy_match  # noqa: E402

REFERENCE_PATH = REPO / "skills/wardley-map-workspace/iteration-10/eval-ai-trust/wardley-reference.owm"
OUTPUTS = ROOT / "outputs"

ZONES = ["Genesis", "Custom", "Product", "Commodity"]


def zone_of(eps: float) -> str:
    if eps < 0.25:
        return "Genesis"
    if eps < 0.5:
        return "Custom"
    if eps < 0.75:
        return "Product"
    return "Commodity"


def extract_owm_block(md_text: str) -> str | None:
    import re
    m = re.search(r"```owm\s*\n(.*?)\n```", md_text, re.DOTALL)
    return m.group(1) if m else None


def main():
    ref_anchors, ref_comps = parse_owm(REFERENCE_PATH.read_text())
    # Group reference components by zone
    ref_by_zone: dict[str, list[str]] = defaultdict(list)
    for name, (_v, e) in ref_comps.items():
        ref_by_zone[zone_of(e)].append(name)
    print("\nReference component distribution:")
    for z in ZONES:
        names = ref_by_zone.get(z, [])
        print(f"  {z:10s}  n={len(names):2d}  {', '.join(sorted(names)[:5])}{'...' if len(names) > 5 else ''}")
    print()

    # For each cell: which reference components did we match? Tag by zone.
    cells = []
    for cell_md in sorted(OUTPUTS.glob("eval-ai-trust/*/thinking-*/run-*/outputs/output.md")):
        parts = cell_md.relative_to(OUTPUTS).parts
        model = parts[1]
        thinking = parts[2].replace("thinking-", "")
        rep = int(parts[3].replace("run-", ""))
        owm = extract_owm_block(cell_md.read_text())
        if not owm:
            continue
        _, ours_comps = parse_owm(owm)
        matched_by_zone: dict[str, int] = defaultdict(int)
        for rname, (_v, re_) in ref_comps.items():
            match, _ = fuzzy_match(rname, ours_comps.keys())
            if match:
                matched_by_zone[zone_of(re_)] += 1
        cells.append({"model": model, "thinking": thinking, "rep": rep, "matched": dict(matched_by_zone)})

    # Aggregate per (model, thinking, zone)
    groups: dict[tuple, list] = defaultdict(list)
    for c in cells:
        groups[(c["model"], c["thinking"])].append(c)

    # Print per-zone coverage table
    print("Per-zone coverage (% of Wardley's components in each zone that the cell matched)")
    print()
    header = ["model", "thinking"] + [f"{z}\n({len(ref_by_zone.get(z, []))})" for z in ZONES]
    rows = []
    for (model, thinking), cs in sorted(groups.items()):
        row = [model.replace("claude-", "").replace("-20251001", ""), thinking]
        for z in ZONES:
            n_in_zone = len(ref_by_zone.get(z, []))
            if n_in_zone == 0:
                row.append("—")
                continue
            cov = [c["matched"].get(z, 0) / n_in_zone for c in cs]
            row.append(f"{100 * statistics.mean(cov):.0f}%")
        rows.append(row)

    # Layout
    flat_header = [
        "model", "thinking",
        f"Genesis (n={len(ref_by_zone.get('Genesis', []))})",
        f"Custom (n={len(ref_by_zone.get('Custom', []))})",
        f"Product (n={len(ref_by_zone.get('Product', []))})",
        f"Commodity (n={len(ref_by_zone.get('Commodity', []))})",
    ]
    widths = [max(len(h), max(len(r[i]) for r in rows)) for i, h in enumerate(flat_header)]
    print("  " + "  ".join(h.ljust(w) for h, w in zip(flat_header, widths)))
    print("  " + "  ".join("-" * w for w in widths))
    for r in rows:
        print("  " + "  ".join(c.ljust(w) for c, w in zip(r, widths)))

    # Save as JSON for the article
    out = {
        "reference_by_zone": {z: sorted(ref_by_zone.get(z, [])) for z in ZONES},
        "matrix": [
            {
                "model": k[0], "thinking": k[1],
                "coverage_by_zone": {
                    z: statistics.mean(c["matched"].get(z, 0) / len(ref_by_zone[z]) for c in cs)
                       if ref_by_zone.get(z) else None
                    for z in ZONES
                },
            }
            for k, cs in sorted(groups.items())
        ],
    }
    (ROOT / "zone_analysis.json").write_text(json.dumps(out, indent=2))
    print(f"\nwrote zone_analysis.json")


if __name__ == "__main__":
    main()
