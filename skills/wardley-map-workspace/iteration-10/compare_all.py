#!/usr/bin/env python3
"""Run the comparison against all 4 benchmarks and produce a summary table."""
import sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from compare import parse_owm, fuzzy_match  # type: ignore

BENCHMARKS = [
    ("ai-trust", "eval-ai-trust/wardley-reference.owm",
     "eval-ai-trust/with_skill/run-1/outputs/output.md"),
    ("retail-journey", "eval-retail-journey/wardley-reference.owm",
     "eval-retail-journey/with_skill/run-1/outputs/output.md"),
    ("healthcare-clinical", "eval-healthcare-clinical/wardley-reference.owm",
     "eval-healthcare-clinical/with_skill/run-1/outputs/output.md"),
    ("finance-risk", "eval-finance-risk/wardley-reference.owm",
     "eval-finance-risk/with_skill/run-1/outputs/output.md"),
]

BASE = Path(__file__).parent


def compare(name: str, ref_path: Path, ours_path: Path):
    ref_a, ref_c = parse_owm(ref_path.read_text())
    ours_a, ours_c = parse_owm(ours_path.read_text())
    # Wardley sometimes uses high-ν 'component' as anchor; treat ν >= 0.85 as effective anchors
    ref_all = {**ref_a, **ref_c}
    ours_all = {**ours_a, **ours_c}

    matched = []
    for rname, (rv, re_) in ref_all.items():
        match, score = fuzzy_match(rname, ours_all.keys())
        if match:
            ov, oe = ours_all[match]
            matched.append((rname, rv, re_, match, ov, oe, score))
    n_ref = len(ref_all)
    n_match = len(matched)
    coverage = n_match / n_ref if n_ref else 0
    deltas_eps = [r[5] - r[2] for r in matched]
    deltas_vis = [r[4] - r[1] for r in matched]
    mean_abs_eps = sum(abs(d) for d in deltas_eps) / max(len(deltas_eps), 1)
    mean_abs_vis = sum(abs(d) for d in deltas_vis) / max(len(deltas_vis), 1)
    bias_eps = sum(deltas_eps) / max(len(deltas_eps), 1)
    bias_vis = sum(deltas_vis) / max(len(deltas_vis), 1)
    same_stage = sum(1 for d in deltas_eps if abs(d) < 0.25)
    same_stage_pct = same_stage / max(len(deltas_eps), 1)

    return {
        "name": name,
        "ref_total": n_ref,
        "ours_total": len(ours_all),
        "matched": n_match,
        "coverage": coverage,
        "mean_abs_eps": mean_abs_eps,
        "mean_abs_vis": mean_abs_vis,
        "bias_eps": bias_eps,
        "bias_vis": bias_vis,
        "same_stage_pct": same_stage_pct,
    }


results = []
for name, ref, ours in BENCHMARKS:
    ref_path = BASE / ref
    ours_path = BASE / ours
    if not ref_path.exists() or not ours_path.exists():
        print(f"SKIP {name}: missing file(s)")
        continue
    r = compare(name, ref_path, ours_path)
    results.append(r)

print(f"{'Benchmark':<22} {'Ref':>4} {'Ours':>5} {'Match':>6} {'Cov':>5}  {'|Δε|':>5} {'|Δν|':>5} {'ε-bias':>7} {'ν-bias':>7} {'stage%':>7}")
print("-" * 90)
for r in results:
    print(f"{r['name']:<22} {r['ref_total']:>4} {r['ours_total']:>5} {r['matched']:>6} "
          f"{r['coverage']*100:>4.0f}%  {r['mean_abs_eps']:>5.3f} {r['mean_abs_vis']:>5.3f} "
          f"{r['bias_eps']:>+7.3f} {r['bias_vis']:>+7.3f} {r['same_stage_pct']*100:>6.0f}%")

print()
# aggregates
avg_cov = sum(r['coverage'] for r in results) / len(results)
avg_eps = sum(r['mean_abs_eps'] for r in results) / len(results)
avg_vis = sum(r['mean_abs_vis'] for r in results) / len(results)
avg_stage = sum(r['same_stage_pct'] for r in results) / len(results)
avg_bias_vis = sum(r['bias_vis'] for r in results) / len(results)
print(f"Averages across {len(results)} benchmarks:")
print(f"  Coverage: {avg_cov*100:.0f}%")
print(f"  Mean |Δε|: {avg_eps:.3f}")
print(f"  Mean |Δν|: {avg_vis:.3f}")
print(f"  ν bias: {avg_bias_vis:+.3f} (positive = we place things higher than Wardley)")
print(f"  Same-stage placement: {avg_stage*100:.0f}%")
