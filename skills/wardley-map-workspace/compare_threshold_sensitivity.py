#!/usr/bin/env python3
"""Fuzzy-match threshold sensitivity sweep (BENCHMARK-AUDIT.md B3).

Reruns the 25-map benchmark at multiple thresholds for the fuzzy name matcher.
Reports how the headline aggregates move; if they barely move, the 0.55 default
is robust. If they jump, the report's coverage / |Δε| numbers need a
confidence interval.

Uses run-1 outputs only — the threshold question is orthogonal to multi-trial
variance (A3), so a single-trial sweep is sufficient.
"""
import sys, json, re
from pathlib import Path
from difflib import SequenceMatcher
from statistics import median

sys.path.insert(0, "/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10")
from compare import parse_owm  # parser is threshold-independent

# Import the 25-map list directly from compare_all_25 by re-execing only the
# BENCHMARKS literal. Simpler than maintaining a duplicate.
exec(open("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/compare_all_25.py").read().split("def stage_of")[0])

ROOT = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace")


def fuzzy_match(name, candidates, threshold):
    """Same scoring as iteration-10/compare.py, but threshold is required."""
    best = (None, 0.0)
    nlow = name.lower()
    for c in candidates:
        clow = c.lower()
        if nlow == clow:
            return c, 1.0
        if nlow in clow or clow in nlow:
            return c, 0.9
        score = SequenceMatcher(None, nlow, clow).ratio()
        nwords = set(re.findall(r"\w+", nlow))
        cwords = set(re.findall(r"\w+", clow))
        if nwords & cwords:
            overlap = len(nwords & cwords) / max(len(nwords), len(cwords))
            score = max(score, overlap)
        if score > best[1]:
            best = (c, score)
    return best if best[1] >= threshold else (None, 0.0)


def stage_of(eps):
    if eps < 0.25: return 0
    if eps < 0.5:  return 1
    if eps < 0.75: return 2
    return 3


def aggregate_at_threshold(threshold):
    """Run all 25 benchmarks at this threshold; return aggregate metrics."""
    n_matches_total = 0
    n_ref_total = 0
    abs_eps_total = 0.0
    abs_vis_total = 0.0
    bias_eps_total = 0.0
    same_band_total = 0
    within_one_total = 0
    all_de = []
    n_maps_used = 0
    for name, ref, ours, domain in BENCHMARKS:
        ref_p = ROOT / ref
        ours_p = ROOT / ours
        if not ref_p.exists() or not ours_p.exists():
            continue
        ra, rc = parse_owm(ref_p.read_text())
        oa, oc = parse_owm(ours_p.read_text())
        ref_all = {**ra, **rc}
        ours_all = {**oa, **oc}
        n_maps_used += 1
        n_ref_total += len(ref_all)
        for rname, (rv, re_) in ref_all.items():
            m, s = fuzzy_match(rname, ours_all.keys(), threshold)
            if m:
                ov, oe = ours_all[m]
                de = oe - re_
                dv = ov - rv
                n_matches_total += 1
                abs_eps_total += abs(de)
                abs_vis_total += abs(dv)
                bias_eps_total += de
                all_de.append(de)
                if stage_of(re_) == stage_of(oe):
                    same_band_total += 1
                if abs(stage_of(re_) - stage_of(oe)) <= 1:
                    within_one_total += 1
    n = max(n_matches_total, 1)
    return {
        "threshold": threshold,
        "n_maps": n_maps_used,
        "n_ref": n_ref_total,
        "n_matches": n_matches_total,
        "coverage": n_matches_total / max(n_ref_total, 1),
        "abs_eps": abs_eps_total / n,
        "abs_vis": abs_vis_total / n,
        "bias_eps": bias_eps_total / n,
        "same_band": same_band_total / n,
        "within_one": within_one_total / n,
        "close_010": sum(1 for d in all_de if abs(d) <= 0.10) / n,
        "close_020": sum(1 for d in all_de if abs(d) <= 0.20) / n,
    }


THRESHOLDS = [0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70]
rows = [aggregate_at_threshold(t) for t in THRESHOLDS]

print(f"{'τ':>5} {'matches':>8} {'cov':>5} {'|Δε|':>6} {'|Δν|':>6} {'ε-bias':>7} {'same':>5} {'±1st':>5} {'≤.10':>5} {'≤.20':>5}")
print("-" * 70)
for r in rows:
    marker = "  <-- default" if r["threshold"] == 0.55 else ""
    print(f"{r['threshold']:>5.2f} {r['n_matches']:>8d} {r['coverage']*100:>4.0f}% "
          f"{r['abs_eps']:>6.3f} {r['abs_vis']:>6.3f} {r['bias_eps']:>+7.3f} "
          f"{r['same_band']*100:>4.0f}% {r['within_one']*100:>4.0f}% "
          f"{r['close_010']*100:>4.0f}% {r['close_020']*100:>4.0f}%{marker}")

# Quick sensitivity summary: max delta on key metrics across {0.45, 0.55, 0.65}
core = [r for r in rows if r["threshold"] in (0.45, 0.55, 0.65)]
print(f"\nCore-range sensitivity (τ ∈ {{0.45, 0.55, 0.65}}):")
for k, label in [("coverage", "Coverage"), ("abs_eps", "|Δε|"),
                 ("same_band", "Same band"), ("close_020", "≤0.20")]:
    vals = [r[k] for r in core]
    spread = max(vals) - min(vals)
    unit = "pp" if k in ("coverage", "same_band", "close_020") else ""
    fmt = f"{spread*100:.1f}{unit}" if unit == "pp" else f"{spread:.3f}{unit}"
    print(f"  {label:<12}  max−min = {fmt}")

Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/threshold-sensitivity.json").write_text(
    json.dumps(rows, indent=2)
)
print("\nSaved threshold-sensitivity.json")
