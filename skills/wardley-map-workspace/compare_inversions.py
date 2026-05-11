#!/usr/bin/env python3
"""B2: Inter-iteration inversion smoke test.

For each map that has run-1 outputs in multiple iterations, compute the
benchmark metrics at each iteration using the same matcher/parser, and flag
inversions where a later iteration scored *worse* than an earlier one.

Per `audit.md` §1: inverted items are usually revealing a task or grader bug,
or run-to-run noise — they make a good starting point for where to look
closely.

Thresholds for flagging (chosen to exceed A3 noise floor):
  - coverage drop > 5pp
  - |Δε| increase > 0.04
"""
import sys, json
from pathlib import Path
sys.path.insert(0, "/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10")
from compare import parse_owm, fuzzy_match

ROOT = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace")


def stage_of(eps):
    if eps < 0.25: return 0
    if eps < 0.5:  return 1
    if eps < 0.75: return 2
    return 3


def stats(ref_path, ours_path):
    ra, rc = parse_owm(ref_path.read_text())
    oa, oc = parse_owm(ours_path.read_text())
    ref_all = {**ra, **rc}
    ours_all = {**oa, **oc}
    matched = []
    for rname, (rv, re_) in ref_all.items():
        m, s = fuzzy_match(rname, ours_all.keys())
        if m:
            ov, oe = ours_all[m]
            matched.append((rname, rv, re_, m, ov, oe))
    de = [r[5] - r[2] for r in matched]
    n = max(len(matched), 1)
    return {
        "ref": len(ref_all),
        "ours": len(ours_all),
        "match": len(matched),
        "coverage": len(matched) / max(len(ref_all), 1),
        "abs_eps": sum(abs(d) for d in de) / n,
        "same_band": sum(1 for r in matched if stage_of(r[2]) == stage_of(r[5])) / n,
    }


def find_output(eval_dir):
    for p in [eval_dir / "with_skill/run-1/outputs/output.md",
              eval_dir / "with_skill/run-1/output.md"]:
        if p.exists():
            return p
    return None


# Discover maps and the iterations they have outputs in.
ITS = ["iteration-10", "iteration-11", "iteration-12", "iteration-13",
       "iteration-14", "iteration-15", "iteration-16"]

map_runs = {}  # map_name -> [(iteration, ref_path, out_path), ...]
for it in ITS:
    it_dir = ROOT / it
    if not it_dir.exists():
        continue
    for eval_dir in sorted(it_dir.glob("eval-*")):
        ref = eval_dir / "wardley-reference.owm"
        out = find_output(eval_dir)
        if ref.exists() and out:
            name = eval_dir.name.replace("eval-", "")
            map_runs.setdefault(name, []).append((it, ref, out))

# Only look at maps with 2+ iterations.
multi = {n: runs for n, runs in map_runs.items() if len(runs) >= 2}
print(f"{len(multi)} maps have outputs in 2+ iterations.\n")

# Per-map: stats per iteration, plus inversion flags.
inversions = []  # (map, earlier_it, later_it, metric, earlier_val, later_val, delta)
print(f"{'Map':<26} {'It':<14} {'Cov':>5} {'|Δε|':>6} {'Same':>5}")
print("-" * 60)
for name in sorted(multi):
    runs = multi[name]
    per_it = []
    for it, ref, out in runs:
        s = stats(ref, out)
        per_it.append((it, s))
        print(f"{name if it == runs[0][0] else '':<26} {it:<14} "
              f"{s['coverage']*100:>4.0f}% {s['abs_eps']:>6.3f} {s['same_band']*100:>4.0f}%")
    # Check pairwise: any later iteration with materially worse metrics?
    for i in range(len(per_it) - 1):
        for j in range(i + 1, len(per_it)):
            earlier_it, e_s = per_it[i]
            later_it, l_s = per_it[j]
            cov_drop = e_s["coverage"] - l_s["coverage"]
            eps_rise = l_s["abs_eps"] - e_s["abs_eps"]
            if cov_drop > 0.05:
                inversions.append((name, earlier_it, later_it, "coverage",
                                   e_s["coverage"], l_s["coverage"], -cov_drop))
            if eps_rise > 0.04:
                inversions.append((name, earlier_it, later_it, "|Δε|",
                                   e_s["abs_eps"], l_s["abs_eps"], eps_rise))
    print()

print("\n" + "=" * 70)
print(f"INVERSIONS FOUND: {len(inversions)}")
print("=" * 70)
print(f"{'Map':<26} {'Earlier':<14} {'Later':<14} {'Metric':<8} {'Earlier':>8} {'Later':>8} {'Δ':>8}")
print("-" * 90)
for inv in inversions:
    name, e, l, m, ev, lv, d = inv
    print(f"{name:<26} {e:<14} {l:<14} {m:<8} "
          f"{ev:>8.3f} {lv:>8.3f} {d:>+8.3f}")

(ROOT / "inversions-summary.json").write_text(json.dumps({
    "n_multi_iteration_maps": len(multi),
    "n_inversions": len(inversions),
    "thresholds": {"coverage_drop_pp": 5, "abs_eps_rise": 0.04},
    "inversions": [{"map": i[0], "earlier": i[1], "later": i[2],
                    "metric": i[3], "earlier_val": i[4], "later_val": i[5],
                    "delta": i[6]} for i in inversions],
}, indent=2))
print(f"\nSaved inversions-summary.json")
