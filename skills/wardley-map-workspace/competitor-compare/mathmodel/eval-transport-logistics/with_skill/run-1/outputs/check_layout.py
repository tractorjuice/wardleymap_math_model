#!/usr/bin/env python3
"""Mirror of skills/wardley-map/scripts/check_layout.mjs for this sandbox run."""
import re
import sys

NEAR_DUP_THRESHOLD = 0.02
BOUNDARY_TOLERANCE = 0.01
BAND_BOUNDARIES = [0.25, 0.50, 0.75]
ANCHOR_EDGE_HIGH = 0.98
ANCHOR_EDGE_LOW = 0.02
COMP_EDGE_HIGH = 0.99
COMP_EDGE_LOW = 0.01
STAGE_SHARE_LIMIT = 0.60

NODE_RE = re.compile(r'^(anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\]')


def parse_owm(text):
    nodes = []
    for raw in text.split('\n'):
        line = raw.strip()
        if not line or line.startswith('//') or line.startswith('#'):
            continue
        m = NODE_RE.match(line)
        if m:
            nodes.append({'kind': m.group(1), 'name': m.group(2).strip(), 'v': float(m.group(3)), 'e': float(m.group(4))})
    return nodes


def stage_of(e):
    if e < 0.25:
        return 'Genesis'
    if e < 0.50:
        return 'Custom'
    if e < 0.75:
        return 'Product'
    return 'Commodity'


def check_near_duplicates(nodes):
    out = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dv = abs(nodes[i]['v'] - nodes[j]['v'])
            de = abs(nodes[i]['e'] - nodes[j]['e'])
            if dv < NEAR_DUP_THRESHOLD and de < NEAR_DUP_THRESHOLD:
                out.append(
                    f"NEAR-DUPLICATE: '{nodes[i]['name']}' [{nodes[i]['v']}, {nodes[i]['e']}] "
                    f"and '{nodes[j]['name']}' [{nodes[j]['v']}, {nodes[j]['e']}] "
                    f"(|dnu|={dv:.3f}, |deps|={de:.3f})."
                )
    return out


def check_boundary(nodes):
    out = []
    for n in nodes:
        if n['kind'] != 'component':
            continue
        for b in BAND_BOUNDARIES:
            if abs(n['e'] - b) <= BOUNDARY_TOLERANCE:
                out.append(
                    f"BOUNDARY STRADDLE: '{n['name']}' at eps={n['e']} within +/-{BOUNDARY_TOLERANCE} of boundary {b}. "
                    f"Nudge to {b - 0.03:.2f} or {b + 0.03:.2f}."
                )
    return out


def check_canvas(nodes):
    out = []
    for n in nodes:
        is_anchor = n['kind'] == 'anchor'
        v_high = ANCHOR_EDGE_HIGH if is_anchor else COMP_EDGE_HIGH
        v_low = ANCHOR_EDGE_LOW if is_anchor else COMP_EDGE_LOW
        if n['v'] > v_high:
            out.append(f"CANVAS CLIP: {n['kind']} '{n['name']}' at nu={n['v']} may clip. Pull back to {v_high - 0.02:.2f}.")
        if n['v'] < v_low:
            out.append(f"CANVAS CLIP: {n['kind']} '{n['name']}' at nu={n['v']} may clip. Push up to {v_low + 0.02:.2f}.")
        if n['e'] > COMP_EDGE_HIGH:
            out.append(f"CANVAS CLIP: {n['kind']} '{n['name']}' at eps={n['e']} may clip right. Pull back to {COMP_EDGE_HIGH - 0.02:.2f}.")
        if n['e'] < COMP_EDGE_LOW:
            out.append(f"CANVAS CLIP: {n['kind']} '{n['name']}' at eps={n['e']} may clip left. Push right to {COMP_EDGE_LOW + 0.02:.2f}.")
    return out


def check_stage_distribution(nodes):
    comps = [n for n in nodes if n['kind'] == 'component']
    if len(comps) < 5:
        return []
    counts = {'Genesis': 0, 'Custom': 0, 'Product': 0, 'Commodity': 0}
    for n in comps:
        counts[stage_of(n['e'])] += 1
    out = []
    total = len(comps)
    for stage, n in counts.items():
        share = n / total
        if share > STAGE_SHARE_LIMIT:
            out.append(f"STAGE IMBALANCE: {n}/{total} ({share*100:.0f}%) in {stage}.")
    for stage, n in counts.items():
        if n == 0:
            out.append(f"STAGE EMPTY: no components in {stage}.")
    return out


def main():
    strict = '--strict' in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith('--')]
    with open(files[0]) as f:
        text = f.read()
    fence = re.search(r'```owm\s*\n([\s\S]*?)\n```', text)
    if fence:
        text = fence.group(1)
    nodes = parse_owm(text)
    warnings = (
        check_near_duplicates(nodes)
        + check_boundary(nodes)
        + check_canvas(nodes)
        + check_stage_distribution(nodes)
    )
    anchors = sum(1 for n in nodes if n['kind'] == 'anchor')
    components = sum(1 for n in nodes if n['kind'] == 'component')
    if not warnings:
        print(f"LAYOUT OK: {anchors} anchors, {components} components -- no warnings.")
        sys.exit(0)
    print(f"LAYOUT WARNINGS: {len(warnings)} issue(s) ({anchors} anchors, {components} components).")
    print()
    for w in warnings:
        print(f"  - {w}")
    sys.exit(1 if strict else 0)


if __name__ == '__main__':
    main()
