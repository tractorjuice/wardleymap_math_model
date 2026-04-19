#!/usr/bin/env python3
"""3-way comparison: arc-kit vs ours-v1 vs ours-v2 against Wardley references.

ours-v1 numbers come from the 25-map benchmark summary (pre-checklist skill).
ours-v2 runs blind on the same 6/7 scenarios with the checklists added.
arc-kit runs use its own skill package (vendored into skill/).
"""
import json, sys
from pathlib import Path

sys.path.insert(0, "/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10")
from compare import parse_owm, fuzzy_match  # noqa: E402

ROOT = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/arc-kit-compare")
OUR_V1_SUMMARY = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/benchmark-25-summary.json")

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


def fmt_row(label, s):
    return (f"  {label:<10} {s['ref']:>4} {s['ours']:>5} {s['match']:>5} "
            f"{s['coverage']:>6.1%} {s['abs_eps']:>6.3f} {s['abs_vis']:>6.3f} "
            f"{s['bias_eps']:>+7.3f} {s['bias_vis']:>+7.3f} "
            f"{s['same_stage']:>5.1%} {s['within_one_stage']:>5.1%} "
            f"{s['close_020']:>5.1%}")


def main():
    v1_by_name = {row["name"]: row for row in json.loads(OUR_V1_SUMMARY.read_text())["per_map"]}

    header = (f"  {'skill':<10} {'ref':>4} {'ours':>5} {'match':>5} {'cov':>6} "
              f"{'|Δε|':>6} {'|Δν|':>6} {'εbias':>7} {'νbias':>7} "
              f"{'same':>5} {'±1':>5} {'≤.20':>5}")
    print(header)
    print("  " + "-" * (len(header) - 2))

    # Aggregates
    agg = {"arc-kit": [], "ours-v1": [], "ours-v2": []}

    for name, subdir, v1_key in BENCHMARKS:
        print(f"\n### {name}")
        ref = ROOT / subdir / "wardley-reference.owm"

        arc = ROOT / subdir / "with_skill/run-1/outputs/output.md"
        v2 = ROOT / subdir / "ours-v2/run-1/outputs/output.md"

        if arc.exists():
            s = stats(ref, arc)
            print(fmt_row("arc-kit", s))
            agg["arc-kit"].append(s)
        else:
            print("  arc-kit    (no output)")

        v1 = v1_by_name.get(v1_key)
        if v1:
            print(f"  {'ours-v1':<10} {v1['ref']:>4} {v1['ours']:>5} {v1['match']:>5} "
                  f"{v1['coverage']:>6.1%} {v1['abs_eps']:>6.3f} {v1['abs_vis']:>6.3f} "
                  f"{v1['bias_eps']:>+7.3f} {v1['bias_vis']:>+7.3f} "
                  f"{v1['same_stage']:>5.1%} {v1['within_one_stage']:>5.1%} "
                  f"{v1['close_020']:>5.1%}")
            agg["ours-v1"].append(v1)
        else:
            print("  ours-v1    (not in summary)")

        if v2.exists():
            s = stats(ref, v2)
            print(fmt_row("ours-v2", s))
            agg["ours-v2"].append(s)
        else:
            print("  ours-v2    (no output)")

    # Aggregates over maps that have all three
    print("\n### Aggregate (maps with all three skills)")
    common = set()
    for i, (name, _, _) in enumerate(BENCHMARKS):
        has_arc = (ROOT / BENCHMARKS[i][1] / "with_skill/run-1/outputs/output.md").exists()
        has_v2 = (ROOT / BENCHMARKS[i][1] / "ours-v2/run-1/outputs/output.md").exists()
        has_v1 = v1_by_name.get(BENCHMARKS[i][2]) is not None
        if has_arc and has_v2 and has_v1:
            common.add(i)
    print(f"  (n={len(common)} maps: "
          + ", ".join(BENCHMARKS[i][0] for i in sorted(common)) + ")\n")

    def mean(xs, k): return sum(x[k] for x in xs) / len(xs) if xs else 0.0

    def filt(xs, lst): return [xs[i] for i, (n, _, _) in enumerate(BENCHMARKS) if i in common and xs is lst]

    # Build filtered per-skill lists
    arc_f = [agg["arc-kit"][j] for j, (i, (n, _, _)) in enumerate(
        [(i, BENCHMARKS[i]) for i in sorted(common) if (ROOT / BENCHMARKS[i][1] / "with_skill/run-1/outputs/output.md").exists()])]
    # Simpler: rebuild from scratch
    arc_f, v1_f, v2_f = [], [], []
    for i in sorted(common):
        name, subdir, v1_key = BENCHMARKS[i]
        ref = ROOT / subdir / "wardley-reference.owm"
        arc_f.append(stats(ref, ROOT / subdir / "with_skill/run-1/outputs/output.md"))
        v2_f.append(stats(ref, ROOT / subdir / "ours-v2/run-1/outputs/output.md"))
        v1_f.append(v1_by_name[v1_key])

    for label, xs in [("arc-kit", arc_f), ("ours-v1", v1_f), ("ours-v2", v2_f)]:
        print(f"  {label:<10} "
              f"cov={mean(xs, 'coverage'):>5.1%}  "
              f"|Δε|={mean(xs, 'abs_eps'):>.3f}  "
              f"|Δν|={mean(xs, 'abs_vis'):>.3f}  "
              f"εbias={mean(xs, 'bias_eps'):>+.3f}  "
              f"νbias={mean(xs, 'bias_vis'):>+.3f}  "
              f"same={mean(xs, 'same_stage'):>5.1%}  "
              f"±1={mean(xs, 'within_one_stage'):>5.1%}  "
              f"≤.20={mean(xs, 'close_020'):>5.1%}")


if __name__ == "__main__":
    main()
