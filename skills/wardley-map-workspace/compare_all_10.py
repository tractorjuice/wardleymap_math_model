#!/usr/bin/env python3
"""Run comparison across all 10 benchmark maps."""
import sys
from pathlib import Path
sys.path.insert(0, "/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10")
from compare import parse_owm, fuzzy_match

ROOT = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace")

BENCHMARKS = [
    # (name, reference_path, ours_path, domain)
    ("ai-trust", "iteration-10/eval-ai-trust/wardley-reference.owm",
     "iteration-10/eval-ai-trust/with_skill/run-1/outputs/output.md", "AI"),
    ("retail-journey", "iteration-10/eval-retail-journey/wardley-reference.owm",
     "iteration-10/eval-retail-journey/with_skill/run-1/outputs/output.md", "Retail"),
    ("healthcare-clinical", "iteration-10/eval-healthcare-clinical/wardley-reference.owm",
     "iteration-10/eval-healthcare-clinical/with_skill/run-1/outputs/output.md", "Healthcare"),
    ("finance-risk", "iteration-10/eval-finance-risk/wardley-reference.owm",
     "iteration-10/eval-finance-risk/with_skill/run-1/outputs/output.md", "Finance"),
    ("retail-journey-v2", "iteration-11/eval-retail-journey/wardley-reference.owm",
     "iteration-11/eval-retail-journey/with_skill/run-1/outputs/output.md", "Retail (exp-seed)"),
    ("manufacturing", "iteration-12/eval-manufacturing-supply/wardley-reference.owm",
     "iteration-12/eval-manufacturing-supply/with_skill/run-1/outputs/output.md", "Manufacturing"),
    ("cybersecurity", "iteration-12/eval-cybersecurity-risk/wardley-reference.owm",
     "iteration-12/eval-cybersecurity-risk/with_skill/run-1/outputs/output.md", "Cybersecurity"),
    ("agriculture", "iteration-12/eval-agriculture-regen/wardley-reference.owm",
     "iteration-12/eval-agriculture-regen/with_skill/run-1/outputs/output.md", "Agriculture"),
    ("education", "iteration-12/eval-education-lifelong/wardley-reference.owm",
     "iteration-12/eval-education-lifelong/with_skill/run-1/outputs/output.md", "Education"),
    ("gaming", "iteration-12/eval-gaming-economies/wardley-reference.owm",
     "iteration-12/eval-gaming-economies/with_skill/run-1/outputs/output.md", "Gaming"),
    ("sustainability", "iteration-12/eval-sustainability-supply/wardley-reference.owm",
     "iteration-12/eval-sustainability-supply/with_skill/run-1/outputs/output.md", "Sustainability"),
]

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
    n_ref = len(ref_all); n_match = len(matched)
    coverage = n_match / n_ref if n_ref else 0
    de = [r[5]-r[2] for r in matched]
    dv = [r[4]-r[1] for r in matched]
    return {
        "ref": n_ref, "ours": len(ours_all), "match": n_match,
        "coverage": coverage,
        "abs_eps": sum(abs(d) for d in de)/max(len(de),1),
        "abs_vis": sum(abs(d) for d in dv)/max(len(dv),1),
        "bias_eps": sum(de)/max(len(de),1),
        "bias_vis": sum(dv)/max(len(dv),1),
        "same_stage": sum(1 for d in de if abs(d)<0.25)/max(len(de),1),
    }

results = []
for name, ref, ours, domain in BENCHMARKS:
    ref_p = ROOT / ref
    ours_p = ROOT / ours
    if not ref_p.exists() or not ours_p.exists():
        print(f"SKIP {name}")
        continue
    r = stats(ref_p, ours_p)
    r["name"] = name
    r["domain"] = domain
    results.append(r)

print(f"{'Benchmark':<22} {'Domain':<20} {'Ref':>4} {'Ours':>5} {'Match':>6} {'Cov':>5}  {'|Δε|':>5} {'|Δν|':>5} {'ε-bias':>7} {'ν-bias':>7} {'stage%':>7}")
print("-" * 110)
for r in results:
    print(f"{r['name']:<22} {r['domain']:<20} {r['ref']:>4} {r['ours']:>5} {r['match']:>6} "
          f"{r['coverage']*100:>4.0f}%  {r['abs_eps']:>5.3f} {r['abs_vis']:>5.3f} "
          f"{r['bias_eps']:>+7.3f} {r['bias_vis']:>+7.3f} {r['same_stage']*100:>6.0f}%")

# Aggregates: exclude iter-10 retail (superseded by iter-11)
for group_name, group in [("All 10 benchmarks (latest run per scenario)",
                            [r for r in results if r["name"] != "retail-journey"])]:
    print()
    print(group_name, f"— N={len(group)}")
    for k in ["coverage", "abs_eps", "abs_vis", "bias_eps", "bias_vis", "same_stage"]:
        avg = sum(r[k] for r in group) / len(group)
        print(f"  {k}: {avg:.3f}" + (f" ({avg*100:.0f}%)" if "coverage" in k or "same_stage" in k else ""))
