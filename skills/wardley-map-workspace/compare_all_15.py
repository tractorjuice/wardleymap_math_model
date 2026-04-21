#!/usr/bin/env python3
"""Comparator for iteration-15 — 20-map re-run of the current (v2 + mermaid) skill.

Uses the same parse_owm + fuzzy_match primitives as compare_all_25.py so numbers
are apples-to-apples with the original 25-map benchmark (which was run against
v1 — pre-checklist skill).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, "/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10")
from compare import parse_owm, fuzzy_match  # noqa: E402

ROOT = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace")
ITER15 = ROOT / "iteration-15"
V1_SUMMARY = ROOT / "benchmark-25-summary.json"

# name → key in benchmark-25-summary.json (matches v1 runs)
BENCHMARKS = [
    ("ai-trust",             "ai-trust"),
    ("healthcare-clinical",  "healthcare-clinical"),
    ("finance-risk",         "finance-risk"),
    ("retail-journey",       "retail-journey"),
    ("manufacturing",        "manufacturing"),
    ("agriculture-regen",    "agriculture"),
    ("education-lifelong",   "education"),
    ("gaming-economies",     "gaming"),
    ("sustainability-supply","sustainability"),
    ("cybersecurity-risk",   "cybersecurity"),
    ("construction-supply",  "construction-supply"),
    ("culture-gender",       "culture-gender"),
    ("defence-intelligence", "defence-intelligence"),
    ("defence-grey-zone",    "defence-grey-zone"),
    ("energy-disruption",    "energy-disruption"),
    ("energy-storage",       "energy-storage"),
    ("government-digital-id","government-digital-id"),
    ("government-sovereignty","government-sovereignty"),
    ("telecoms-sovereignty", "telecoms-sovereignty"),
    ("telecoms-space",       "telecoms-space"),
]


def stage_of(eps):
    if eps < 0.25: return 0
    if eps < 0.5:  return 1
    if eps < 0.75: return 2
    return 3


def stats(ref_path, ours_path):
    ref_a, ref_c = parse_owm(ref_path.read_text())
    ours_a, ours_c = parse_owm(ours_path.read_text())
    ref_all = {**ref_a, **ref_c}
    ours_all = {**ours_a, **ours_c}
    matched = []
    for rname, (rv, re_) in ref_all.items():
        m, s = fuzzy_match(rname, ours_all.keys())
        if m:
            ov, oe = ours_all[m]
            matched.append((rname, rv, re_, m, ov, oe))
    de = [r[5] - r[2] for r in matched]
    dv = [r[4] - r[1] for r in matched]
    n = max(len(matched), 1)
    same = sum(1 for r in matched if stage_of(r[2]) == stage_of(r[5]))
    within1 = sum(1 for r in matched if abs(stage_of(r[2]) - stage_of(r[5])) <= 1)
    return dict(
        ref=len(ref_all), ours=len(ours_all), match=len(matched),
        coverage=len(matched) / max(len(ref_all), 1),
        abs_eps=sum(abs(x) for x in de) / n,
        abs_vis=sum(abs(x) for x in dv) / n,
        bias_eps=sum(de) / n,
        bias_vis=sum(dv) / n,
        same_stage=same / n,
        within_one_stage=within1 / n,
        close_020=sum(1 for x in de if abs(x) <= 0.20) / n,
        close_025=sum(1 for x in de if abs(x) <= 0.25) / n,
    )


def fmt(lbl, s):
    return (f"  {lbl:<8} {s['ref']:>4} {s['ours']:>5} {s['match']:>5} "
            f"{s['coverage']:>6.1%} {s['abs_eps']:>6.3f} {s['abs_vis']:>6.3f} "
            f"{s['bias_eps']:>+7.3f} {s['bias_vis']:>+7.3f} "
            f"{s['same_stage']:>5.1%} {s['within_one_stage']:>5.1%} "
            f"{s['close_020']:>5.1%}")


def main():
    v1 = {r["name"]: r for r in json.loads(V1_SUMMARY.read_text())["per_map"]}
    hdr = (f"  {'skill':<8} {'ref':>4} {'ours':>5} {'match':>5} {'cov':>6} "
           f"{'|Δε|':>6} {'|Δν|':>6} {'εbias':>7} {'νbias':>7} "
           f"{'same':>5} {'±1':>5} {'≤.20':>5}")
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))

    v1_rows, v3_rows = [], []
    per_map = []
    for name, v1key in BENCHMARKS:
        ref = ITER15 / f"eval-{name}" / "wardley-reference.owm"
        v3_out = ITER15 / f"eval-{name}" / "with_skill/run-1/outputs/output.md"
        if not v3_out.exists():
            print(f"\n### {name}\n  v3 output missing")
            continue
        v3 = stats(ref, v3_out)
        v3_rows.append(v3)
        print(f"\n### {name}")
        v1row = v1.get(v1key)
        if v1row:
            print(fmt("v1", v1row))
            v1_rows.append(v1row)
        else:
            print("  v1       (not in 25-map summary)")
        print(fmt("v3", v3))
        per_map.append({"name": name, "v3": v3, "v1": v1row})

    def mean(rows, k):
        return sum(r[k] for r in rows) / len(rows) if rows else 0

    print("\n### Aggregate (n=20)\n")
    for label, rows in [("v1 (avg)", v1_rows), ("v3 (avg)", v3_rows)]:
        print(f"  {label:<10} "
              f"cov={mean(rows, 'coverage'):>5.1%}  "
              f"|Δε|={mean(rows, 'abs_eps'):>.3f}  "
              f"|Δν|={mean(rows, 'abs_vis'):>.3f}  "
              f"εbias={mean(rows, 'bias_eps'):>+.3f}  "
              f"νbias={mean(rows, 'bias_vis'):>+.3f}  "
              f"same={mean(rows, 'same_stage'):>5.1%}  "
              f"±1={mean(rows, 'within_one_stage'):>5.1%}  "
              f"≤.20={mean(rows, 'close_020'):>5.1%}")

    # Machine-readable
    out_json = {
        "n": len(v3_rows),
        "per_map": per_map,
        "aggregate_v3": {k: mean(v3_rows, k) for k in
                         ["coverage","abs_eps","abs_vis","bias_eps","bias_vis",
                          "same_stage","within_one_stage","close_020"]},
        "aggregate_v1_same_maps": {k: mean(v1_rows, k) for k in
                         ["coverage","abs_eps","abs_vis","bias_eps","bias_vis",
                          "same_stage","within_one_stage","close_020"]},
    }
    (ROOT / "iteration-15" / "benchmark-20-v3-summary.json").write_text(json.dumps(out_json, indent=2))


if __name__ == "__main__":
    main()
