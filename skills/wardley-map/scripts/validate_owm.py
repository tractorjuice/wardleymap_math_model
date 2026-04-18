#!/usr/bin/env python3
"""Validate an OWM (Online Wardley Maps) block against structural rules.

Usage:
    python validate_owm.py < map.owm
    python validate_owm.py map.owm

Exit codes:
    0 — no violations
    1 — violations found (printed to stdout)

Extract your OWM block from the draft (everything between ```owm and ```) and
pipe it to this script. If it exits non-zero, fix the reported violations and
re-run until clean.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path


def parse_owm(text: str) -> tuple[dict[str, tuple[float, float]], list[tuple[str, str]]]:
    """Return ({component_name: (visibility, evolution)}, [(source, target), ...])."""
    coords: dict[str, tuple[float, float]] = {}
    edges: list[tuple[str, str]] = []

    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("//") or line.startswith("#"):
            continue
        # anchor or component line
        m = re.match(
            r"(?:anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\](?:\s+.*)?$",
            line,
        )
        if m:
            name = m.group(1).strip()
            try:
                coords[name] = (float(m.group(2)), float(m.group(3)))
            except ValueError:
                pass
            continue
        # dependency edge: "A->B"
        if "->" in line and not line.startswith("evolve"):
            m = re.match(r"(.+?)->(.+)$", line)
            if m:
                edges.append((m.group(1).strip(), m.group(2).strip()))
    return coords, edges


def validate(coords: dict[str, tuple[float, float]], edges: list[tuple[str, str]]) -> list[str]:
    violations: list[str] = []

    # 1. Coords in [0, 1]
    for name, (v, e) in coords.items():
        if not (0.0 <= v <= 1.0):
            violations.append(f"COORD OUT OF RANGE: '{name}' visibility={v} (must be in [0,1])")
        if not (0.0 <= e <= 1.0):
            violations.append(f"COORD OUT OF RANGE: '{name}' evolution={e} (must be in [0,1])")

    # 2. Every edge endpoint should exist as a component/anchor
    for src, tgt in edges:
        if src not in coords:
            violations.append(f"UNKNOWN SOURCE: edge '{src}->{tgt}' — '{src}' not declared")
        if tgt not in coords:
            violations.append(f"UNKNOWN TARGET: edge '{src}->{tgt}' — '{tgt}' not declared")

    # 3. Visibility constraint: for every edge a->b, ν(a) >= ν(b)
    for src, tgt in edges:
        if src in coords and tgt in coords:
            v_src = coords[src][0]
            v_tgt = coords[tgt][0]
            if v_src < v_tgt:
                violations.append(
                    f"VISIBILITY VIOLATION: {src}(ν={v_src}) -> {tgt}(ν={v_tgt}) "
                    f"— source must be at or above target"
                )

    return violations


def main() -> int:
    if len(sys.argv) > 1:
        text = Path(sys.argv[1]).read_text()
    else:
        text = sys.stdin.read()

    # Strip ```owm fences if the caller pasted them
    m = re.search(r"```owm\s*\n(.*?)\n```", text, re.DOTALL)
    if m:
        text = m.group(1)

    coords, edges = parse_owm(text)
    violations = validate(coords, edges)

    if not violations:
        print(f"OK: {len(coords)} components/anchors, {len(edges)} edges — no violations.")
        return 0

    print(f"FAIL: {len(violations)} violation(s) found in map with "
          f"{len(coords)} components/anchors and {len(edges)} edges.")
    print()
    for v in violations:
        print(f"  - {v}")
    print()
    print("Fix each violation and re-run. For visibility violations, either:")
    print("  (a) raise the source's visibility to be >= target's, or")
    print("  (b) lower the target's visibility to be <= source's.")
    print("After fixing, re-run this script because adjustments can cascade.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
