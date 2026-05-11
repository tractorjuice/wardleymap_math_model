#!/usr/bin/env python3
"""Comparison across all 25 benchmarks."""
import sys, json
from pathlib import Path
from statistics import median, stdev
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


# Statuses richer than these (infra_error, validator_unconverged) need runtime
# instrumentation we don't currently capture — they'd require recording the
# subagent's exit reason and validator iteration count into timing.json at run time.
STATUSES = {"ok", "no_output", "parse_failed", "no_timing"}


def load_timing(ours_path):
    """Return (tokens, duration_s) from the run dir's timing.json, or (None, None)."""
    # ours_path is .../with_skill/run-1/outputs/output.md; timing.json is in run-1/.
    t = ours_path.parent.parent / "timing.json"
    if not t.exists():
        return None, None
    try:
        d = json.loads(t.read_text())
    except json.JSONDecodeError:
        return None, None
    tokens = d.get("total_tokens")
    secs = d.get("total_duration_seconds")
    if secs is None and "duration_ms" in d:
        secs = d["duration_ms"] / 1000.0
    return tokens, secs


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
    tokens, duration_s = load_timing(ours_path)
    if len(ours_all) == 0:
        status = "parse_failed"
    elif tokens is None:
        status = "no_timing"
    else:
        status = "ok"
    return {
        "status": status,
        "tokens": tokens,
        "duration_s": duration_s,
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


METRIC_KEYS = [
    "coverage", "abs_eps", "abs_vis", "bias_eps", "bias_vis",
    "same_stage", "within_one_stage",
    "close_005", "close_010", "close_015", "close_020", "close_025", "close_030",
    "near_boundary_miss",
]


def aggregate_trials(name, domain, ref_path, trial_paths):
    """Run stats() on each trial path; aggregate mean+stdev across trials.

    Backward-compat: with one trial, stdev is 0.0 and the numeric metrics equal
    the single-trial value, so single-trial behaviour is preserved.
    """
    trials = [stats(ref_path, p) for p in trial_paths]
    agg = {"name": name, "domain": domain, "n_trials": len(trials)}
    # Worst status across trials (no_output > parse_failed > no_timing > ok).
    rank = {"no_output": 0, "parse_failed": 1, "no_timing": 2, "ok": 3}
    agg["status"] = min(
        (t["status"] for t in trials),
        key=lambda s: rank.get(s, -1),
    )
    # Placement metrics: mean and stdev across trials.
    for k in METRIC_KEYS:
        vals = [t[k] for t in trials]
        agg[k] = sum(vals) / len(vals)
        agg[f"{k}_stdev"] = stdev(vals) if len(vals) > 1 else 0.0
    # Timing: aggregate only over trials that have it.
    tok = [t["tokens"] for t in trials if t["tokens"] is not None]
    dur = [t["duration_s"] for t in trials if t["duration_s"] is not None]
    agg["tokens"] = (sum(tok) / len(tok)) if tok else None
    agg["tokens_stdev"] = stdev(tok) if len(tok) > 1 else 0.0
    agg["duration_s"] = (sum(dur) / len(dur)) if dur else None
    agg["duration_s_stdev"] = stdev(dur) if len(dur) > 1 else 0.0
    # Per-pair |Δε| pooled across trials, for the cumulative distribution.
    agg["all_de"] = [d for t in trials for d in t["all_de"]]
    # Carry through the first trial's counts; these are stable in practice.
    agg["ref"] = trials[0]["ref"]
    agg["ours"] = sum(t["ours"] for t in trials) / len(trials)
    agg["match"] = sum(t["match"] for t in trials) / len(trials)
    # Keep per-trial detail in the JSON for downstream inspection.
    agg["per_trial"] = trials
    return agg


def empty_record(name, domain):
    r = {"name": name, "domain": domain, "n_trials": 0, "status": "no_output",
         "tokens": None, "duration_s": None, "tokens_stdev": 0.0, "duration_s_stdev": 0.0,
         "ref": 0, "ours": 0, "match": 0, "all_de": [], "per_trial": []}
    for k in METRIC_KEYS:
        r[k] = 0.0
        r[f"{k}_stdev"] = 0.0
    return r


results = []
for name, ref, ours, domain in BENCHMARKS:
    ref_p = ROOT / ref
    ours_run1 = ROOT / ours
    # Discover all run-N trial outputs for this benchmark.
    with_skill_dir = ours_run1.parents[2]  # .../with_skill/
    trial_paths = sorted(with_skill_dir.glob("run-*/outputs/output.md"))
    if not ref_p.exists() or not trial_paths:
        results.append(empty_record(name, domain))
        continue
    results.append(aggregate_trials(name, domain, ref_p, trial_paths))

ok_results = [r for r in results if r["status"] in ("ok", "no_timing")]

def fmt_tok(t):
    return f"{t/1000:>4.0f}K" if t else "    -"
def fmt_dur(s):
    return f"{s:>4.0f}s" if s else "    -"

print(f"{'Benchmark':<26} {'Domain':<16} {'St':<4} {'N':>2} {'Ref':>4} {'Ours':>5} {'Match':>6} {'Cov':>5}  {'|Δε|':>5} {'±σ':>5} {'|Δν|':>5} {'ε-bias':>7} {'ν-bias':>7} {'same':>5} {'±1st':>5} {'Tok':>5} {'Dur':>5}")
print("-" * 142)
status_short = {"ok": "ok", "no_timing": "~tm", "parse_failed": "prs", "no_output": "no"}
for r in results:
    print(f"{r['name']:<26} {r['domain']:<16} {status_short[r['status']]:<4} {r['n_trials']:>2} {r['ref']:>4} {r['ours']:>5.0f} {r['match']:>6.1f} "
          f"{r['coverage']*100:>4.0f}%  {r['abs_eps']:>5.3f} {r['abs_eps_stdev']:>5.3f} {r['abs_vis']:>5.3f} "
          f"{r['bias_eps']:>+7.3f} {r['bias_vis']:>+7.3f} "
          f"{r['same_stage']*100:>4.0f}% {r['within_one_stage']*100:>4.0f}% "
          f"{fmt_tok(r['tokens'])} {fmt_dur(r['duration_s'])}")

print()
print(f"Status counts: " + ", ".join(
    f"{s}={sum(1 for r in results if r['status']==s)}" for s in STATUSES
))
print(f"\nPlacement aggregates across {len(ok_results)} ok+no_timing benchmarks "
      f"(excluding {len(results) - len(ok_results)} failed):")
for k, label in [("coverage","Coverage"), ("abs_eps","|Δε|"), ("abs_vis","|Δν|"),
                   ("bias_eps","ε-bias"), ("bias_vis","ν-bias"),
                   ("same_stage","Same band (strict)"),
                   ("within_one_stage","Within 1 band (soft)")]:
    avg = sum(r[k] for r in ok_results) / max(len(ok_results), 1)
    fmt = f"{avg*100:.0f}%" if k in ("coverage","same_stage","within_one_stage") else (f"{avg:+.3f}" if "bias" in k else f"{avg:.3f}")
    print(f"  {label}: {fmt}")

# Timing aggregates: only across runs that produced a timing.json
timed = [r for r in results if r["status"] == "ok"]
if timed:
    toks = [r["tokens"] for r in timed]
    durs = [r["duration_s"] for r in timed]
    print(f"\nTiming aggregates across {len(timed)} benchmarks with timing.json:")
    print(f"  tokens   p50={median(toks):>6.0f}  min={min(toks):>6.0f}  max={max(toks):>6.0f}  sum={sum(toks):>7.0f}")
    print(f"  duration p50={median(durs):>6.0f}s min={min(durs):>6.0f}s max={max(durs):>6.0f}s sum={sum(durs):>7.0f}s")

# Pooled |Δε| distribution across all matches (ok+no_timing only)
all_de = [d for r in ok_results for d in r["all_de"]]
print(f"\n|Δε| cumulative distribution across all {len(all_de)} matched pairs:")
for t in [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]:
    frac = sum(1 for d in all_de if abs(d) <= t) / max(len(all_de), 1)
    print(f"  |Δε| ≤ {t:.2f}: {frac*100:.0f}%")

# Cross-boundary near-misses: |Δε| small but bands differ
total_near = sum(int(r["near_boundary_miss"]*r["match"]) for r in ok_results)
total_matched = sum(r["match"] for r in ok_results)
print(f"\nNear-boundary misses (|Δε| ≤ 0.10 but different bands): "
      f"{total_near}/{total_matched} = {total_near/max(total_matched,1)*100:.0f}% of all matches")
total_strict_miss = sum(r["match"] - int(r["same_stage"]*r["match"]) for r in ok_results)
print(f"Near-boundary misses as fraction of strict-band misses: "
      f"{total_near}/{total_strict_miss} = {total_near/max(total_strict_miss,1)*100:.0f}%")

# Save aggregate json
summary = {
    "n": len(results),
    "status_counts": {s: sum(1 for r in results if r["status"] == s) for s in STATUSES},
    "trial_counts": {n: sum(1 for r in results if r["n_trials"] == n)
                     for n in sorted({r["n_trials"] for r in results})},
    "per_map": results,
    "averages": {k: sum(r[k] for r in ok_results) / max(len(ok_results), 1) for k in
                 ["coverage","abs_eps","abs_vis","bias_eps","bias_vis","same_stage"]},
}
if timed:
    summary["timing"] = {
        "n": len(timed),
        "tokens_p50": int(median(r["tokens"] for r in timed)),
        "duration_s_p50": median(r["duration_s"] for r in timed),
        "tokens_total": sum(r["tokens"] for r in timed),
        "duration_s_total": sum(r["duration_s"] for r in timed),
    }
(ROOT / "benchmark-25-summary.json").write_text(json.dumps(summary, indent=2))
print(f"\nSaved summary to benchmark-25-summary.json")
