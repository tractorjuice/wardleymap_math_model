#!/usr/bin/env python3
"""Mirror of skills/wardley-map/scripts/validate_owm.mjs for this sandbox run.

Validates an OWM file against the same three rules as the Node validator.
"""
import re
import sys

def parse_owm(text):
    coords = {}
    edges = []
    node_re = re.compile(r'^(?:anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\](?:\s+.*)?$')
    edge_re = re.compile(r'^(.+?)->(.+)$')
    for raw in text.split('\n'):
        line = raw.strip()
        if not line or line.startswith('//') or line.startswith('#'):
            continue
        m = node_re.match(line)
        if m:
            name = m.group(1).strip()
            v = float(m.group(2))
            e = float(m.group(3))
            coords[name] = (v, e)
            continue
        if '->' in line and not line.startswith('evolve'):
            em = edge_re.match(line)
            if em:
                edges.append((em.group(1).strip(), em.group(2).strip()))
    return coords, edges

def validate(coords, edges):
    violations = []
    for name, (v, e) in coords.items():
        if not (0.0 <= v <= 1.0):
            violations.append(f"COORD OUT OF RANGE: '{name}' visibility={v}")
        if not (0.0 <= e <= 1.0):
            violations.append(f"COORD OUT OF RANGE: '{name}' evolution={e}")
    for src, tgt in edges:
        if src not in coords:
            violations.append(f"UNKNOWN SOURCE: '{src}->{tgt}' — '{src}' not declared")
        if tgt not in coords:
            violations.append(f"UNKNOWN TARGET: '{src}->{tgt}' — '{tgt}' not declared")
    for src, tgt in edges:
        if src in coords and tgt in coords:
            vs = coords[src][0]
            vt = coords[tgt][0]
            if vs < vt:
                violations.append(f"VISIBILITY VIOLATION: {src}(nu={vs}) -> {tgt}(nu={vt}) — source must be >= target")
    return violations

def main():
    path = sys.argv[1]
    with open(path) as f:
        text = f.read()
    fence = re.search(r'```owm\s*\n([\s\S]*?)\n```', text)
    if fence:
        text = fence.group(1)
    coords, edges = parse_owm(text)
    violations = validate(coords, edges)
    if not violations:
        print(f"OK: {len(coords)} components/anchors, {len(edges)} edges -- no violations.")
        sys.exit(0)
    print(f"FAIL: {len(violations)} violation(s) in map with {len(coords)} components/anchors and {len(edges)} edges.")
    print()
    for v in violations:
        print(f"  - {v}")
    sys.exit(1)

if __name__ == '__main__':
    main()
