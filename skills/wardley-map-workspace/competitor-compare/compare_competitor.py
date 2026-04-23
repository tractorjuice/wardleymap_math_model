#!/usr/bin/env python3
"""Shared comparator for any competitor Wardley-map skill.

Usage:
    python3 compare_competitor.py <competitor-dir> [--output-subdir NAME]

Reads reference/output pairs from competitor-compare/<competitor-dir>/eval-*/
and emits metrics identical to compare_all_25.py so numbers are apples-to-apples
with the mathmodel skill's BENCHMARK-REPORT.md. `mathmodel` is the label used
throughout for the in-tree skill at skills/wardley-map/ — the one built on the
formal tuple M = (V, E, U, nu, epsilon, t). The original in-tree summary in
benchmark-25-summary.json is from an earlier run on different scenarios and is
referenced here as the "ours" row for historical continuity.

The --output-subdir flag selects the per-eval subdirectory that holds the
skill's output. Defaults to `with_skill`, matching arc-kit-compare convention.
For prompt-baseline the subdir is `with_prompt-<variant>` (e.g.
`with_prompt-mathmodel` for runs using prompts/wardley_map_generator.md).

Examples:
    python3 compare_competitor.py mathmodel
    python3 compare_competitor.py haberlah
    python3 compare_competitor.py prompt-baseline --output-subdir with_prompt-mathmodel
"""
import argparse
import json
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE / "iteration-10"))
from compare import parse_owm, fuzzy_match  # noqa: E402

OUR_SUMMARY = WORKSPACE / "benchmark-25-summary.json"

# Canonical 25-map manifest. Mirrors compare_all_25.py so the reference for
# each benchmark is the exact file the in-tree skill was scored against.
# (benchmark-key, reference-path-under-workspace, in-tree-benchmark-name)
BENCHMARKS_25 = [
    ("ai-trust",                "iteration-10/eval-ai-trust/wardley-reference.owm",                "ai-trust"),
    ("healthcare-clinical",     "iteration-10/eval-healthcare-clinical/wardley-reference.owm",     "healthcare-clinical"),
    ("finance-risk",            "iteration-10/eval-finance-risk/wardley-reference.owm",            "finance-risk"),
    ("retail-journey",          "iteration-11/eval-retail-journey/wardley-reference.owm",          "retail-journey"),
    ("manufacturing",           "iteration-12/eval-manufacturing-supply/wardley-reference.owm",    "manufacturing"),
    ("agriculture-regen",       "iteration-12/eval-agriculture-regen/wardley-reference.owm",       "agriculture"),
    ("education-lifelong",      "iteration-12/eval-education-lifelong/wardley-reference.owm",      "education"),
    ("gaming-economies",        "iteration-12/eval-gaming-economies/wardley-reference.owm",        "gaming"),
    ("sustainability-supply",   "iteration-12/eval-sustainability-supply/wardley-reference.owm",   "sustainability"),
    ("cybersecurity-risk",      "iteration-13/eval-cybersecurity-risk/wardley-reference.owm",      "cybersecurity"),
    ("construction-supply",     "iteration-14/eval-construction-supply/wardley-reference.owm",     "construction-supply"),
    ("culture-gender",          "iteration-14/eval-culture-gender/wardley-reference.owm",          "culture-gender"),
    ("defence-intelligence",    "iteration-14/eval-defence-intelligence/wardley-reference.owm",    "defence-intelligence"),
    ("defence-grey-zone",       "iteration-14/eval-defence-grey-zone/wardley-reference.owm",       "defence-grey-zone"),
    ("energy-disruption",       "iteration-14/eval-energy-disruption/wardley-reference.owm",       "energy-disruption"),
    ("energy-storage",          "iteration-14/eval-energy-storage/wardley-reference.owm",          "energy-storage"),
    ("government-digital-id",   "iteration-14/eval-government-digital-id/wardley-reference.owm",   "government-digital-id"),
    ("government-sovereignty",  "iteration-14/eval-government-sovereignty/wardley-reference.owm",  "government-sovereignty"),
    ("personal-fin-inclusion",  "iteration-14/eval-personal-fin-inclusion/wardley-reference.owm",  "personal-fin-inclusion"),
    ("personal-conversational", "iteration-14/eval-personal-conversational/wardley-reference.owm", "personal-conversational"),
    ("politics-labour",         "iteration-14/eval-politics-labour/wardley-reference.owm",         "politics-labour"),
    ("telecoms-sovereignty",    "iteration-14/eval-telecoms-sovereignty/wardley-reference.owm",    "telecoms-sovereignty"),
    ("telecoms-space",          "iteration-14/eval-telecoms-space/wardley-reference.owm",          "telecoms-space"),
    ("transport-logistics",     "iteration-14/eval-transport-logistics/wardley-reference.owm",     "transport-logistics"),
    ("transport-demand",        "iteration-14/eval-transport-demand/wardley-reference.owm",        "transport-demand"),
]


def stage_of(eps):
    if eps < 0.25: return 0
    if eps < 0.5:  return 1
    if eps < 0.75: return 2
    return 3


def stats(ref_path: Path, out_path: Path):
    ref_a, ref_c = parse_owm(ref_path.read_text())
    ous_a, ous_c = parse_owm(out_path.read_text())
    ref_all = {**ref_a, **ref_c}
    ous_all = {**ous_a, **ous_c}
    matched = []
    for rname, (rv, re_) in ref_all.items():
        m, s = fuzzy_match(rname, ous_all.keys())
        if m:
            ov, oe = ous_all[m]
            matched.append((rname, rv, re_, m, ov, oe))
    de = [r[5] - r[2] for r in matched]
    dv = [r[4] - r[1] for r in matched]
    n = max(len(matched), 1)
    same = sum(1 for r in matched if stage_of(r[2]) == stage_of(r[5]))
    within1 = sum(1 for r in matched if abs(stage_of(r[2]) - stage_of(r[5])) <= 1)
    close = lambda t: sum(1 for x in de if abs(x) <= t) / n
    return dict(
        ref=len(ref_all), ours=len(ous_all), match=len(matched),
        coverage=len(matched) / max(len(ref_all), 1),
        abs_eps=sum(abs(x) for x in de) / n,
        abs_vis=sum(abs(x) for x in dv) / n,
        bias_eps=sum(de) / n,
        bias_vis=sum(dv) / n,
        same_stage=same / n,
        within_one_stage=within1 / n,
        close_010=close(0.10),
        close_015=close(0.15),
        close_020=close(0.20),
        close_025=close(0.25),
        deltas=de,
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("competitor", help="competitor directory under competitor-compare/")
    ap.add_argument("--output-subdir", default="with_skill",
                    help="per-eval subdir holding outputs (default: with_skill)")
    args = ap.parse_args()

    comp_root = WORKSPACE / "competitor-compare" / args.competitor
    if not comp_root.is_dir():
        sys.exit(f"error: {comp_root} not found")

    ours_by_name = {row["name"]: row
                    for row in json.loads(OUR_SUMMARY.read_text())["per_map"]}

    print(f"competitor : {args.competitor}")
    print(f"subdir     : {args.output_subdir}")
    print(f"workspace  : {WORKSPACE}")
    print()

    hdr = (f"{'benchmark':<24} {'skill':<12} {'ref':>4} {'out':>4} {'match':>5} "
           f"{'cov':>5} {'|Δε|':>6} {'|Δν|':>6} {'εbias':>7} {'νbias':>7} "
           f"{'same':>5} {'±1':>5} {'≤.20':>5}")
    print(hdr)
    print("-" * len(hdr))

    rows_out = []
    pooled_deltas = []
    n_with_output = 0
    for key, ref_rel, ours_key in BENCHMARKS_25:
        ref_path = WORKSPACE / ref_rel
        eval_dir = comp_root / f"eval-{key}"
        out_md   = eval_dir / args.output_subdir / "run-1" / "outputs" / "output.md"
        draft    = eval_dir / args.output_subdir / "run-1" / "outputs" / "draft.owm"
        # Prefer draft.owm when it parses something. Some competitors (e.g. haberlah)
        # embed the OWM block only in draft.owm and put a markdown table in output.md,
        # which parse_owm can't read.
        chosen = None
        for candidate in (draft, out_md):
            if candidate.exists():
                a, c = parse_owm(candidate.read_text())
                if a or c:
                    chosen = candidate
                    break
        if chosen is None:
            print(f"{key:<24} {args.competitor:<12} (no parseable output)")
            continue
        out_path = chosen
        s = stats(ref_path, out_path)
        n_with_output += 1
        pooled_deltas.extend(s["deltas"])
        row = dict(name=key, **{k: v for k, v in s.items() if k != "deltas"})
        rows_out.append(row)
        print(f"{key:<24} {args.competitor:<12} {s['ref']:>4} {s['ours']:>4} "
              f"{s['match']:>5} {s['coverage']:>5.1%} {s['abs_eps']:>6.3f} "
              f"{s['abs_vis']:>6.3f} {s['bias_eps']:>+7.3f} {s['bias_vis']:>+7.3f} "
              f"{s['same_stage']:>5.1%} {s['within_one_stage']:>5.1%} "
              f"{s['close_020']:>5.1%}")
        o = ours_by_name.get(ours_key)
        if o:
            print(f"{key:<24} {'ours':<12} {o['ref']:>4} {o['ours']:>4} "
                  f"{o['match']:>5} {o['coverage']:>5.1%} {o['abs_eps']:>6.3f} "
                  f"{o['abs_vis']:>6.3f} {o['bias_eps']:>+7.3f} {o['bias_vis']:>+7.3f} "
                  f"{o['same_stage']:>5.1%} {o['within_one_stage']:>5.1%} "
                  f"{o['close_020']:>5.1%}")
        print()

    # Aggregate (only over maps we actually ran)
    if n_with_output == 0:
        print("no competitor outputs found; nothing to aggregate")
        return
    aggregated = {
        "competitor": args.competitor,
        "output_subdir": args.output_subdir,
        "n_maps": n_with_output,
        "mean_coverage":    sum(r["coverage"]    for r in rows_out) / n_with_output,
        "mean_same_stage":  sum(r["same_stage"]  for r in rows_out) / n_with_output,
        "mean_within_1":    sum(r["within_one_stage"] for r in rows_out) / n_with_output,
        "mean_abs_eps":     sum(r["abs_eps"]     for r in rows_out) / n_with_output,
        "mean_abs_vis":     sum(r["abs_vis"]     for r in rows_out) / n_with_output,
        "mean_bias_eps":    sum(r["bias_eps"]    for r in rows_out) / n_with_output,
        "mean_bias_vis":    sum(r["bias_vis"]    for r in rows_out) / n_with_output,
        "pooled_deltas_n":  len(pooled_deltas),
        "pooled_close_010": sum(1 for x in pooled_deltas if abs(x) <= 0.10) / max(len(pooled_deltas), 1),
        "pooled_close_015": sum(1 for x in pooled_deltas if abs(x) <= 0.15) / max(len(pooled_deltas), 1),
        "pooled_close_020": sum(1 for x in pooled_deltas if abs(x) <= 0.20) / max(len(pooled_deltas), 1),
        "pooled_close_025": sum(1 for x in pooled_deltas if abs(x) <= 0.25) / max(len(pooled_deltas), 1),
        "per_map": rows_out,
    }

    print("-" * len(hdr))
    print(f"{args.competitor} aggregate over {n_with_output} map(s):")
    print(f"  mean coverage         : {aggregated['mean_coverage']:>5.1%}")
    print(f"  mean same-band        : {aggregated['mean_same_stage']:>5.1%}")
    print(f"  mean within-1-band    : {aggregated['mean_within_1']:>5.1%}")
    print(f"  mean |Δε|             : {aggregated['mean_abs_eps']:>6.3f}")
    print(f"  mean |Δν|             : {aggregated['mean_abs_vis']:>6.3f}")
    print(f"  mean signed ε-bias    : {aggregated['mean_bias_eps']:>+6.3f}")
    print(f"  mean signed ν-bias    : {aggregated['mean_bias_vis']:>+6.3f}")
    print(f"  pooled |Δε|≤0.10      : {aggregated['pooled_close_010']:>5.1%}")
    print(f"  pooled |Δε|≤0.15      : {aggregated['pooled_close_015']:>5.1%}")
    print(f"  pooled |Δε|≤0.20      : {aggregated['pooled_close_020']:>5.1%}")
    print(f"  pooled |Δε|≤0.25      : {aggregated['pooled_close_025']:>5.1%}")

    out_json = comp_root / f"competitor-summary-{args.competitor}.json"
    out_json.write_text(json.dumps(aggregated, indent=2))
    print(f"\nwrote {out_json}")


if __name__ == "__main__":
    main()
