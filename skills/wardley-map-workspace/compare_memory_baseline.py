#!/usr/bin/env python3
"""Memory baseline comparison: how much of skill coverage is recallable from training?

Compares `no_skill/run-1/outputs/output.md` against `wardley-reference.owm` using the
same parser and fuzzy matcher as compare_all_25.py. The headline finding is
(skill coverage) − (memory baseline coverage) per map — the skill's marginal lift.
"""
import sys, json
from pathlib import Path
sys.path.insert(0, "/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10")
from compare import parse_owm, fuzzy_match

ROOT = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace")

# (name, ref_path, no_skill_path, skill_coverage_pct, profile)
# profile = rough estimate of how publicly discussed Wardley's specific map is.
PAIRS = [
    ("ai-trust",
     "iteration-10/eval-ai-trust/wardley-reference.owm",
     "iteration-10/eval-ai-trust/no_skill/run-1/outputs/output.md",
     62, "high"),
    ("healthcare-clinical",
     "iteration-10/eval-healthcare-clinical/wardley-reference.owm",
     "iteration-10/eval-healthcare-clinical/no_skill/run-1/outputs/output.md",
     60, "med-high"),
    ("finance-risk",
     "iteration-10/eval-finance-risk/wardley-reference.owm",
     "iteration-10/eval-finance-risk/no_skill/run-1/outputs/output.md",
     55, "med-high"),
    ("cybersecurity",
     "iteration-13/eval-cybersecurity-risk/wardley-reference.owm",
     "iteration-13/eval-cybersecurity-risk/no_skill/run-1/outputs/output.md",
     58, "med"),
    ("construction-supply",
     "iteration-14/eval-construction-supply/wardley-reference.owm",
     "iteration-14/eval-construction-supply/no_skill/run-1/outputs/output.md",
     35, "low"),
    ("telecoms-sovereignty",
     "iteration-14/eval-telecoms-sovereignty/wardley-reference.owm",
     "iteration-14/eval-telecoms-sovereignty/no_skill/run-1/outputs/output.md",
     24, "low"),
    ("culture-gender",
     "iteration-14/eval-culture-gender/wardley-reference.owm",
     "iteration-14/eval-culture-gender/no_skill/run-1/outputs/output.md",
     19, "low"),
]


def compare(ref_path, ours_path):
    ref_a, ref_c = parse_owm(ref_path.read_text())
    ours_a, ours_c = parse_owm(ours_path.read_text())
    ref_all = {**ref_a, **ref_c}
    ours_all = {**ours_a, **ours_c}
    matched = []
    for rname, (rv, re_) in ref_all.items():
        m, s = fuzzy_match(rname, ours_all.keys())
        if m:
            ov, oe = ours_all[m]
            matched.append((rname, rv, re_, m, ov, oe, s))
    n = max(len(matched), 1)
    de = [r[5] - r[2] for r in matched]
    return {
        "ref_n": len(ref_all),
        "ours_n": len(ours_all),
        "match_n": len(matched),
        "coverage": len(matched) / max(len(ref_all), 1),
        "abs_eps": sum(abs(d) for d in de) / n,
        "bias_eps": sum(de) / n,
        "matches": [(r[0], r[3], round(r[6], 2)) for r in matched],
    }


print(f"{'Map':<22} {'Profile':<10} {'Skill cov':>10} {'Memory cov':>11} {'Lift':>7} {'|Δε|':>6}")
print("-" * 70)
out = []
for name, ref, ours, skill_cov, profile in PAIRS:
    r = compare(ROOT / ref, ROOT / ours)
    lift = skill_cov - r["coverage"] * 100
    print(f"{name:<22} {profile:<10} {skill_cov:>9}% {r['coverage']*100:>10.0f}% {lift:>+5.0f}pp "
          f"{r['abs_eps']:>6.3f}")
    out.append({"name": name, "profile": profile, "skill_coverage": skill_cov / 100,
                "skill_lift_pp": lift, **r})

# Cluster summary by profile
print(f"\nBy profile:")
for p in ["high", "med-high", "med", "low"]:
    rows = [o for o in out if o["profile"] == p]
    if rows:
        mc = sum(r["coverage"] for r in rows) / len(rows) * 100
        sl = sum(r["skill_lift_pp"] for r in rows) / len(rows)
        print(f"  {p:<10} n={len(rows)}  mean memory cov = {mc:>4.0f}%  mean skill lift = {sl:>+5.1f}pp")

(ROOT / "memory-baseline-summary.json").write_text(json.dumps(out, indent=2))
print(f"\nSaved to memory-baseline-summary.json")
