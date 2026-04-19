#!/usr/bin/env python3
"""Comparison across all 25 benchmarks."""
import sys, json
from pathlib import Path
sys.path.insert(0, "/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10")
from compare import parse_owm, fuzzy_match

ROOT = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace")

BENCHMARKS = [
    # original 4 (iter-10)
    ("ai-trust", "iteration-10/eval-ai-trust/wardley-reference.owm",
     "iteration-10/eval-ai-trust/with_skill/run-1/outputs/output.md", "AI"),
    ("healthcare-clinical", "iteration-10/eval-healthcare-clinical/wardley-reference.owm",
     "iteration-10/eval-healthcare-clinical/with_skill/run-1/outputs/output.md", "Healthcare"),
    ("finance-risk", "iteration-10/eval-finance-risk/wardley-reference.owm",
     "iteration-10/eval-finance-risk/with_skill/run-1/outputs/output.md", "Finance"),
    # retail (use iter-11 with exponential seed)
    ("retail-journey", "iteration-11/eval-retail-journey/wardley-reference.owm",
     "iteration-11/eval-retail-journey/with_skill/run-1/outputs/output.md", "Retail"),
    # iter-12 (6 maps)
    ("manufacturing", "iteration-12/eval-manufacturing-supply/wardley-reference.owm",
     "iteration-12/eval-manufacturing-supply/with_skill/run-1/outputs/output.md", "Manufacturing"),
    ("agriculture", "iteration-12/eval-agriculture-regen/wardley-reference.owm",
     "iteration-12/eval-agriculture-regen/with_skill/run-1/outputs/output.md", "Agriculture"),
    ("education", "iteration-12/eval-education-lifelong/wardley-reference.owm",
     "iteration-12/eval-education-lifelong/with_skill/run-1/outputs/output.md", "Education"),
    ("gaming", "iteration-12/eval-gaming-economies/wardley-reference.owm",
     "iteration-12/eval-gaming-economies/with_skill/run-1/outputs/output.md", "Gaming"),
    ("sustainability", "iteration-12/eval-sustainability-supply/wardley-reference.owm",
     "iteration-12/eval-sustainability-supply/with_skill/run-1/outputs/output.md", "Sustainability"),
    # cybersecurity (use iter-13 with density guidance)
    ("cybersecurity", "iteration-13/eval-cybersecurity-risk/wardley-reference.owm",
     "iteration-13/eval-cybersecurity-risk/with_skill/run-1/outputs/output.md", "Cybersecurity"),
    # iter-14 (15 new maps)
    ("construction-supply", "iteration-14/eval-construction-supply/wardley-reference.owm",
     "iteration-14/eval-construction-supply/with_skill/run-1/outputs/output.md", "Construction"),
    ("culture-gender", "iteration-14/eval-culture-gender/wardley-reference.owm",
     "iteration-14/eval-culture-gender/with_skill/run-1/outputs/output.md", "Culture"),
    ("defence-intelligence", "iteration-14/eval-defence-intelligence/wardley-reference.owm",
     "iteration-14/eval-defence-intelligence/with_skill/run-1/outputs/output.md", "Defence"),
    ("defence-grey-zone", "iteration-14/eval-defence-grey-zone/wardley-reference.owm",
     "iteration-14/eval-defence-grey-zone/with_skill/run-1/outputs/output.md", "Defence"),
    ("energy-disruption", "iteration-14/eval-energy-disruption/wardley-reference.owm",
     "iteration-14/eval-energy-disruption/with_skill/run-1/outputs/output.md", "Energy"),
    ("energy-storage", "iteration-14/eval-energy-storage/wardley-reference.owm",
     "iteration-14/eval-energy-storage/with_skill/run-1/outputs/output.md", "Energy"),
    ("government-digital-id", "iteration-14/eval-government-digital-id/wardley-reference.owm",
     "iteration-14/eval-government-digital-id/with_skill/run-1/outputs/output.md", "Government"),
    ("government-sovereignty", "iteration-14/eval-government-sovereignty/wardley-reference.owm",
     "iteration-14/eval-government-sovereignty/with_skill/run-1/outputs/output.md", "Government"),
    ("personal-fin-inclusion", "iteration-14/eval-personal-fin-inclusion/wardley-reference.owm",
     "iteration-14/eval-personal-fin-inclusion/with_skill/run-1/outputs/output.md", "Personal"),
    ("personal-conversational", "iteration-14/eval-personal-conversational/wardley-reference.owm",
     "iteration-14/eval-personal-conversational/with_skill/run-1/outputs/output.md", "Personal"),
    ("politics-labour", "iteration-14/eval-politics-labour/wardley-reference.owm",
     "iteration-14/eval-politics-labour/with_skill/run-1/outputs/output.md", "Politics"),
    ("telecoms-sovereignty", "iteration-14/eval-telecoms-sovereignty/wardley-reference.owm",
     "iteration-14/eval-telecoms-sovereignty/with_skill/run-1/outputs/output.md", "Telecoms"),
    ("telecoms-space", "iteration-14/eval-telecoms-space/wardley-reference.owm",
     "iteration-14/eval-telecoms-space/with_skill/run-1/outputs/output.md", "Telecoms"),
    ("transport-logistics", "iteration-14/eval-transport-logistics/wardley-reference.owm",
     "iteration-14/eval-transport-logistics/with_skill/run-1/outputs/output.md", "Transportation"),
    ("transport-demand", "iteration-14/eval-transport-demand/wardley-reference.owm",
     "iteration-14/eval-transport-demand/with_skill/run-1/outputs/output.md", "Transportation"),
]


def stage_of(eps):
    """Return band index 0..3 for ε in [0,1]. Boundaries at 0.25, 0.5, 0.75."""
    if eps < 0.25: return 0        # Genesis
    if eps < 0.5:  return 1        # Custom Built
    if eps < 0.75: return 2        # Product (+rental)
    return 3                        # Commodity (+utility)


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
    de = [r[5]-r[2] for r in matched]
    dv = [r[4]-r[1] for r in matched]
    n = max(len(matched), 1)
    # Proper band-membership metric (was |Δε|<0.25 which allowed cross-boundary pairs)
    same_band = sum(1 for r in matched if stage_of(r[2]) == stage_of(r[5]))
    within_one = sum(1 for r in matched if abs(stage_of(r[2]) - stage_of(r[5])) <= 1)
    # |Δε| cumulative distribution — how close are placements regardless of band?
    # Also tag: band-match status for each pair
    close_buckets = {t: sum(1 for d in de if abs(d) <= t) / n for t in [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]}
    # "Close across boundary": near misses that happen to cross a band line
    near_boundary_miss = sum(
        1 for r in matched
        if stage_of(r[2]) != stage_of(r[5]) and abs(r[5] - r[2]) <= 0.10
    )
    return {
        "ref": len(ref_all), "ours": len(ours_all), "match": len(matched),
        "coverage": len(matched)/max(len(ref_all),1),
        "abs_eps": sum(abs(d) for d in de)/n,
        "abs_vis": sum(abs(d) for d in dv)/n,
        "bias_eps": sum(de)/n,
        "bias_vis": sum(dv)/n,
        "same_stage": same_band/n,
        "within_one_stage": within_one/n,
        "close_005": close_buckets[0.05],
        "close_010": close_buckets[0.10],
        "close_015": close_buckets[0.15],
        "close_020": close_buckets[0.20],
        "close_025": close_buckets[0.25],
        "close_030": close_buckets[0.30],
        "near_boundary_miss": near_boundary_miss / n,
        "all_de": de,
    }


results = []
for name, ref, ours, domain in BENCHMARKS:
    ref_p = ROOT / ref
    ours_p = ROOT / ours
    if not ref_p.exists() or not ours_p.exists():
        print(f"SKIP {name}: missing file(s)")
        continue
    r = stats(ref_p, ours_p)
    r["name"] = name
    r["domain"] = domain
    results.append(r)

print(f"{'Benchmark':<26} {'Domain':<16} {'Ref':>4} {'Ours':>5} {'Match':>6} {'Cov':>5}  {'|Δε|':>5} {'|Δν|':>5} {'ε-bias':>7} {'ν-bias':>7} {'same':>5} {'±1st':>5}")
print("-" * 116)
for r in results:
    print(f"{r['name']:<26} {r['domain']:<16} {r['ref']:>4} {r['ours']:>5} {r['match']:>6} "
          f"{r['coverage']*100:>4.0f}%  {r['abs_eps']:>5.3f} {r['abs_vis']:>5.3f} "
          f"{r['bias_eps']:>+7.3f} {r['bias_vis']:>+7.3f} "
          f"{r['same_stage']*100:>4.0f}% {r['within_one_stage']*100:>4.0f}%")

print()
print(f"Aggregates across {len(results)} benchmarks:")
for k, label in [("coverage","Coverage"), ("abs_eps","|Δε|"), ("abs_vis","|Δν|"),
                   ("bias_eps","ε-bias"), ("bias_vis","ν-bias"),
                   ("same_stage","Same band (strict)"),
                   ("within_one_stage","Within 1 band (soft)")]:
    avg = sum(r[k] for r in results) / len(results)
    fmt = f"{avg*100:.0f}%" if k in ("coverage","same_stage","within_one_stage") else (f"{avg:+.3f}" if "bias" in k else f"{avg:.3f}")
    print(f"  {label}: {fmt}")

# Pooled |Δε| distribution across all matches
all_de = [d for r in results for d in r["all_de"]]
print(f"\n|Δε| cumulative distribution across all {len(all_de)} matched pairs:")
for t in [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]:
    frac = sum(1 for d in all_de if abs(d) <= t) / len(all_de)
    print(f"  |Δε| ≤ {t:.2f}: {frac*100:.0f}%")

# Cross-boundary near-misses: |Δε| small but bands differ
near_misses = [r for r in results for _ in range(int(r["near_boundary_miss"]*r["match"]))]
total_near = sum(int(r["near_boundary_miss"]*r["match"]) for r in results)
total_matched = sum(r["match"] for r in results)
print(f"\nNear-boundary misses (|Δε| ≤ 0.10 but different bands): "
      f"{total_near}/{total_matched} = {total_near/total_matched*100:.0f}% of all matches")
# Of strict-miss cases, how many are near-boundary?
total_strict_miss = sum(r["match"] - int(r["same_stage"]*r["match"]) for r in results)
print(f"Near-boundary misses as fraction of strict-band misses: "
      f"{total_near}/{total_strict_miss} = {total_near/max(total_strict_miss,1)*100:.0f}%")

# Save aggregate json
out = {"n": len(results), "per_map": results,
       "averages": {k: sum(r[k] for r in results) / len(results) for k in
                    ["coverage","abs_eps","abs_vis","bias_eps","bias_vis","same_stage"]}}
(ROOT / "benchmark-25-summary.json").write_text(json.dumps(out, indent=2))
print(f"\nSaved summary to benchmark-25-summary.json")
