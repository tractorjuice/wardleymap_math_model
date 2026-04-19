#!/usr/bin/env python3
"""Compare our skill's AI TRUST output to Wardley's reference map.

- Extract (name, visibility, evolution) from both maps
- Fuzzy-match component names
- Compute placement deltas for matches
- Report: anchor overlap, coverage, placement correlation, unique components
"""
import re, sys
from pathlib import Path
from difflib import SequenceMatcher

REFERENCE = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10/eval-ai-trust/wardley-reference.owm")
OURS = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10/eval-ai-trust/with_skill/run-1/outputs/output.md")


def parse_owm(text: str):
    anchors = {}
    components = {}
    # strip fences if present
    m = re.search(r"```owm\s*\n(.*?)\n```", text, re.DOTALL)
    if m:
        text = m.group(1)
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        m = re.match(r"(anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\]", line)
        if m:
            kind, name, v, e = m.groups()
            target = anchors if kind == "anchor" else components
            target[name.strip()] = (float(v), float(e))
    return anchors, components


def fuzzy_match(name, candidates, threshold=0.55):
    """Find the closest name in candidates. Returns (matched_name, score) or (None, 0)."""
    best = (None, 0.0)
    nlow = name.lower()
    for c in candidates:
        clow = c.lower()
        # exact/substring
        if nlow == clow:
            return c, 1.0
        if nlow in clow or clow in nlow:
            return c, 0.9
        score = SequenceMatcher(None, nlow, clow).ratio()
        # word-overlap boost
        nwords = set(re.findall(r"\w+", nlow))
        cwords = set(re.findall(r"\w+", clow))
        if nwords & cwords:
            overlap = len(nwords & cwords) / max(len(nwords), len(cwords))
            score = max(score, overlap)
        if score > best[1]:
            best = (c, score)
    if best[1] >= threshold:
        return best
    return (None, 0.0)


def main():
    ref_text = REFERENCE.read_text()
    ours_text = OURS.read_text()
    ref_anchors, ref_comps = parse_owm(ref_text)
    ours_anchors, ours_comps = parse_owm(ours_text)

    print(f"REFERENCE (Wardley): {len(ref_anchors)} anchors, {len(ref_comps)} components")
    print(f"OURS:                {len(ours_anchors)} anchors, {len(ours_comps)} components")
    print()

    # Anchor comparison
    print("=" * 60)
    print("ANCHORS")
    print("=" * 60)
    print(f"Wardley:  {sorted(ref_anchors.keys())}")
    print(f"Ours:     {sorted(ours_anchors.keys())}")
    for name, (v, e) in ref_anchors.items():
        match, score = fuzzy_match(name, ours_anchors.keys())
        if match:
            ov, oe = ours_anchors[match]
            print(f"  '{name}' (ν={v}, ε={e})  <->  '{match}' (ν={ov}, ε={oe})  [sim={score:.2f}]")
        else:
            print(f"  '{name}' (ν={v}, ε={e})  <->  (no match)")
    print()

    # Component matching
    print("=" * 60)
    print("COMPONENT OVERLAP")
    print("=" * 60)
    matched = []
    ref_unmatched = []
    ours_matched_names = set()
    for rname, (rv, re_) in ref_comps.items():
        match, score = fuzzy_match(rname, ours_comps.keys())
        if match:
            ov, oe = ours_comps[match]
            matched.append((rname, rv, re_, match, ov, oe, score))
            ours_matched_names.add(match)
        else:
            ref_unmatched.append((rname, rv, re_))
    ours_unmatched = [(n, v, e) for n, (v, e) in ours_comps.items() if n not in ours_matched_names]

    print(f"\n{len(matched)}/{len(ref_comps)} of Wardley's components matched to ours ({100*len(matched)/len(ref_comps):.0f}% coverage)")
    print(f"{len(ours_unmatched)} components in our map not in Wardley's")
    print()

    print("MATCHES (sorted by |Δε|):")
    print(f"  {'Wardley':<36} {'Ours':<36} {'ν-W':>4} {'ν-O':>4} {'ε-W':>4} {'ε-O':>4} {'Δε':>5}")
    for row in sorted(matched, key=lambda r: abs(r[5] - r[2]), reverse=True):
        rname, rv, re_, oname, ov, oe, _ = row
        de = oe - re_
        print(f"  {rname:<36.36} {oname:<36.36} {rv:>4.2f} {ov:>4.2f} {re_:>4.2f} {oe:>4.2f} {de:>+5.2f}")

    # Placement delta stats
    if matched:
        deltas_eps = [r[5] - r[2] for r in matched]
        deltas_vis = [r[4] - r[1] for r in matched]
        mean_abs_eps = sum(abs(d) for d in deltas_eps) / len(deltas_eps)
        mean_abs_vis = sum(abs(d) for d in deltas_vis) / len(deltas_vis)
        bias_eps = sum(deltas_eps) / len(deltas_eps)
        bias_vis = sum(deltas_vis) / len(deltas_vis)
        print()
        print(f"ε: mean |Δ| = {mean_abs_eps:.3f}, signed bias = {bias_eps:+.3f}")
        print(f"ν: mean |Δ| = {mean_abs_vis:.3f}, signed bias = {bias_vis:+.3f}")
        # Count % within stage band (0.25 wide)
        same_stage = sum(1 for d in deltas_eps if abs(d) < 0.25)
        print(f"Same-stage placement: {same_stage}/{len(matched)} ({100*same_stage/len(matched):.0f}%)")

    print()
    print("=" * 60)
    print("WARDLEY'S COMPONENTS NOT IN OUR MAP")
    print("=" * 60)
    for name, v, e in ref_unmatched:
        print(f"  '{name}' (ν={v}, ε={e})")

    print()
    print("=" * 60)
    print("OUR COMPONENTS NOT IN WARDLEY'S MAP")
    print("=" * 60)
    for name, v, e in ours_unmatched:
        print(f"  '{name}' (ν={v}, ε={e})")


if __name__ == "__main__":
    main()
