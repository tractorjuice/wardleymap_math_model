#!/usr/bin/env python3
"""Compare arc-kit skill outputs against Wardley references.

Uses the same parse_owm + fuzzy_match primitives as compare_all_25.py so
results are apples-to-apples with the 25-map benchmark.
"""
import json, sys
from pathlib import Path

sys.path.insert(0, "/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10")
from compare import parse_owm, fuzzy_match  # noqa: E402

ROOT = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/arc-kit-compare")
OUR_SUMMARY = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/benchmark-25-summary.json")

BENCHMARKS = [
    ("ai-trust",             "eval-ai-trust",             "ai-trust"),
    ("manufacturing",        "eval-manufacturing",        "manufacturing"),
    ("culture-gender",       "eval-culture-gender",       "culture-gender"),
    ("telecoms-sovereignty", "eval-telecoms-sovereignty", "telecoms-sovereignty"),
    ("politics-labour",      "eval-politics-labour",      "politics-labour"),
    ("agriculture-regen",    "eval-agriculture-regen",    "agriculture"),
    ("cybersecurity",        "eval-cybersecurity-risk",   "cybersecurity"),
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
    same = sum(1 for d in de if stage_of(d + 0) == 0)  # placeholder, recompute below
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
        close_010=sum(1 for x in de if abs(x) <= 0.10) / n,
        close_020=sum(1 for x in de if abs(x) <= 0.20) / n,
        close_025=sum(1 for x in de if abs(x) <= 0.25) / n,
    )


def main():
    # Load our 25-map summary for side-by-side
    ours_by_name = {row["name"]: row for row in json.loads(OUR_SUMMARY.read_text())["per_map"]}

    print(f"{'benchmark':<18} {'skill':<10} {'ref':>4} {'ours':>5} {'match':>5} "
          f"{'cov':>5} {'|Δε|':>6} {'|Δν|':>6} {'εbias':>7} {'νbias':>7} "
          f"{'same':>5} {'±1':>5} {'≤.20':>5}")
    print("-" * 110)

    for name, subdir, our_key in BENCHMARKS:
        arc_out = ROOT / subdir / "with_skill/run-1/outputs/output.md"
        ref = ROOT / subdir / "wardley-reference.owm"
        if not arc_out.exists():
            print(f"{name:<18} arc-kit    (no output yet)")
            continue
        s = stats(ref, arc_out)
        print(f"{name:<18} arc-kit    {s['ref']:>4} {s['ours']:>5} {s['match']:>5} "
              f"{s['coverage']:>5.1%} {s['abs_eps']:>6.3f} {s['abs_vis']:>6.3f} "
              f"{s['bias_eps']:>+7.3f} {s['bias_vis']:>+7.3f} "
              f"{s['same_stage']:>5.1%} {s['within_one_stage']:>5.1%} {s['close_020']:>5.1%}")
        o = ours_by_name.get(our_key)
        if o:
            print(f"{name:<18} ours       {o['ref']:>4} {o['ours']:>5} {o['match']:>5} "
                  f"{o['coverage']:>5.1%} {o['abs_eps']:>6.3f} {o['abs_vis']:>6.3f} "
                  f"{o['bias_eps']:>+7.3f} {o['bias_vis']:>+7.3f} "
                  f"{o['same_stage']:>5.1%} {o['within_one_stage']:>5.1%} "
                  f"{o['close_020']:>5.1%}")
        print()


if __name__ == "__main__":
    main()
