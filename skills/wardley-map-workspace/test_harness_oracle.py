#!/usr/bin/env python3
"""A5: oracle and null harness checks.

Validates that the benchmark machinery (parse_owm + fuzzy_match + stats)
behaves correctly at the extremes:

  - **Oracle**: when `output = reference`, the matcher should score
    coverage=100%, |Δε|=0, |Δν|=0, same-band=100%. If not, parse_owm or
    fuzzy_match has a bug.
  - **Null (randomised placements)**: same component names as the reference,
    but coordinates uniformly randomised. Coverage should still be 100% (names
    match exactly) but |Δε| should approach 0.25 (mean abs deviation for a
    uniform random variable on [0,1] vs another uniform) and same-band should
    approach 25% (chance, four equal-width bands).

Both are run on every reference in the 25-map corpus.
"""
import sys, random, json, re
from pathlib import Path
from statistics import mean, stdev
sys.path.insert(0, "/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10")
from compare import parse_owm, fuzzy_match

ROOT = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace")

# Reuse the 25-map list from compare_all_25.py.
exec(open(ROOT / "compare_all_25.py").read().split("def stage_of")[0])


def stage_of(eps):
    if eps < 0.25: return 0
    if eps < 0.5:  return 1
    if eps < 0.75: return 2
    return 3


def stats_from_dicts(ref_all, ours_all):
    matched = []
    for rname, (rv, re_) in ref_all.items():
        m, s = fuzzy_match(rname, ours_all.keys())
        if m:
            ov, oe = ours_all[m]
            matched.append((rv, re_, ov, oe))
    n = max(len(matched), 1)
    return {
        "coverage": len(matched) / max(len(ref_all), 1),
        "abs_eps": sum(abs(r[3] - r[1]) for r in matched) / n,
        "abs_vis": sum(abs(r[2] - r[0]) for r in matched) / n,
        "same_band": sum(1 for r in matched if stage_of(r[1]) == stage_of(r[3])) / n,
    }


def synthesize_owm_text(items):
    """Re-emit a name → (v, e) dict as OWM lines (for round-trip testing)."""
    lines = []
    for name, (v, e) in items.items():
        lines.append(f"component {name} [{v}, {e}]")
    return "\n".join(lines)


# ---- Oracle: output == reference ----
print("=" * 70)
print("ORACLE TEST: output is parsed from the reference itself")
print("=" * 70)
print("Expectations: coverage=100%, |Δε|=0, |Δν|=0, same-band=100%")
print(f"\n{'Map':<26} {'Cov':>5} {'|Δε|':>6} {'|Δν|':>6} {'Same':>5}")
print("-" * 56)
oracle_results = []
for name, ref, _, _ in BENCHMARKS:
    ref_p = ROOT / ref
    if not ref_p.exists():
        continue
    ra, rc = parse_owm(ref_p.read_text())
    ref_all = {**ra, **rc}
    # Feed reference as ours by serialising-then-reparsing (round-trip).
    rt_text = synthesize_owm_text(ref_all)
    rta, rtc = parse_owm(rt_text)
    ours_all = {**rta, **rtc}
    s = stats_from_dicts(ref_all, ours_all)
    oracle_results.append((name, s, len(ref_all), len(ours_all)))
    print(f"{name:<26} {s['coverage']*100:>4.0f}% {s['abs_eps']:>6.3f} "
          f"{s['abs_vis']:>6.3f} {s['same_band']*100:>4.0f}%")

# Oracle pass criteria.
oracle_fails = [r for r in oracle_results
                if r[1]["coverage"] < 0.99
                or r[1]["abs_eps"] > 0.001
                or r[1]["abs_vis"] > 0.001
                or r[1]["same_band"] < 0.99]
print(f"\nOracle: {len(oracle_results) - len(oracle_fails)}/{len(oracle_results)} maps pass strict thresholds.")
if oracle_fails:
    print("FAILURES (parser/matcher bug suspect):")
    for name, s, ref_n, ours_n in oracle_fails:
        print(f"  {name}: cov={s['coverage']*100:.0f}% |Δε|={s['abs_eps']:.3f} "
              f"|Δν|={s['abs_vis']:.3f} same={s['same_band']*100:.0f}%  "
              f"(ref={ref_n}, parsed={ours_n})")

# ---- Null: random placements ----
print("\n" + "=" * 70)
print("NULL TEST: random placements on same component names (mean of 5 seeds)")
print("=" * 70)
print("Expectations: coverage=100% (names exact), |Δε|≈0.33, same-band≈25%")
print(f"\n{'Map':<26} {'Cov':>5} {'|Δε|':>6} {'|Δν|':>6} {'Same':>5}")
print("-" * 56)
null_per_map = []
for name, ref, _, _ in BENCHMARKS:
    ref_p = ROOT / ref
    if not ref_p.exists():
        continue
    ra, rc = parse_owm(ref_p.read_text())
    ref_all = {**ra, **rc}
    samples = []
    for seed in range(5):
        rng = random.Random(seed)
        randomised = {n: (rng.random(), rng.random()) for n in ref_all}
        s = stats_from_dicts(ref_all, randomised)
        samples.append(s)
    avg = {k: mean(s[k] for s in samples) for k in samples[0]}
    null_per_map.append((name, avg))
    print(f"{name:<26} {avg['coverage']*100:>4.0f}% {avg['abs_eps']:>6.3f} "
          f"{avg['abs_vis']:>6.3f} {avg['same_band']*100:>4.0f}%")

# Null pooled stats.
print(f"\nNull pooled across {len(null_per_map)} maps × 5 seeds:")
for k in ["coverage", "abs_eps", "abs_vis", "same_band"]:
    vals = [r[1][k] for r in null_per_map]
    expected = {"coverage": 1.00, "abs_eps": 0.333, "abs_vis": 0.333, "same_band": 0.25}[k]
    fmt = (f"{mean(vals)*100:.0f}% ± {stdev(vals)*100:.1f}pp"
           if k in ("coverage", "same_band")
           else f"{mean(vals):.3f} ± {stdev(vals):.3f}")
    exp_fmt = (f"{expected*100:.0f}%" if k in ("coverage", "same_band")
               else f"{expected:.3f}")
    print(f"  {k:<12} observed: {fmt}   expected: {exp_fmt}")

# Save artefact.
(ROOT / "harness-oracle-summary.json").write_text(json.dumps({
    "oracle": {
        "n_maps": len(oracle_results),
        "n_pass": len(oracle_results) - len(oracle_fails),
        "failures": [{"map": r[0], "stats": r[1], "ref_n": r[2], "parsed_n": r[3]}
                     for r in oracle_fails],
    },
    "null": {
        "n_maps": len(null_per_map),
        "n_seeds": 5,
        "pooled": {k: mean(r[1][k] for r in null_per_map)
                   for k in ["coverage", "abs_eps", "abs_vis", "same_band"]},
        "per_map": [{"map": r[0], **r[1]} for r in null_per_map],
    },
}, indent=2))
print(f"\nSaved harness-oracle-summary.json")
