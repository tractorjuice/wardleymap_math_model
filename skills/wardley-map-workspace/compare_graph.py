#!/usr/bin/env python3
"""A7 part 1: dependency-graph grader.

The benchmark's current metrics score component placement but ignore the
*structure* the skill produces. This script parses the directed edge set
from both reference and skill output, fuzzy-aligns nodes (using the same
matcher as compare_all_25.py), and reports edge precision / recall / F1
per map.

Two maps that score identically on coverage and |Δε| can have entirely
different dependency graphs — this grader surfaces that.
"""
import sys, re, json
from pathlib import Path
sys.path.insert(0, "/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-10")
from compare import parse_owm, fuzzy_match

ROOT = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace")

# Reuse the 25-map list from compare_all_25.py.
exec(open(ROOT / "compare_all_25.py").read().split("def stage_of")[0])

# Lines that start with these keywords are declarations, not edges.
DECL = re.compile(r"^(anchor|component|pipeline|title|style|note|evolution|evolve|inertia|annotation|market)\b", re.I)


def parse_edges(text):
    """Return a set of (src, dst) edges from the OWM block."""
    edges = set()
    m = re.search(r"```owm\s*\n(.*?)\n```", text, re.DOTALL)
    if m:
        text = m.group(1)
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("//") or line.startswith("#"):
            continue
        if DECL.match(line):
            continue
        if "->" not in line:
            continue
        # Strip any trailing comment.
        if "//" in line:
            line = line.split("//", 1)[0].strip()
        parts = line.split("->")
        if len(parts) != 2:
            continue
        src, dst = parts[0].strip(), parts[1].strip()
        if src and dst:
            edges.add((src, dst))
    return edges


def grade(ref_nodes, ref_edges, ours_nodes, ours_edges):
    """Compute edge precision/recall/F1 after fuzzy-aligning nodes."""
    # Map each ref node to its best-match in ours, and vice versa.
    ref_to_ours = {}
    for r in ref_nodes:
        m, _ = fuzzy_match(r, list(ours_nodes))
        if m:
            ref_to_ours[r] = m
    ours_to_ref = {}
    for o in ours_nodes:
        m, _ = fuzzy_match(o, list(ref_nodes))
        if m:
            ours_to_ref[o] = m
    # Recall: how many ref edges exist (under translation) in ours?
    matched_ref = 0
    for src, dst in ref_edges:
        ms, md = ref_to_ours.get(src), ref_to_ours.get(dst)
        if ms and md and (ms, md) in ours_edges:
            matched_ref += 1
    # Precision: how many ours edges exist (under translation) in ref?
    matched_ours = 0
    for src, dst in ours_edges:
        ms, md = ours_to_ref.get(src), ours_to_ref.get(dst)
        if ms and md and (ms, md) in ref_edges:
            matched_ours += 1
    recall = matched_ref / max(len(ref_edges), 1)
    precision = matched_ours / max(len(ours_edges), 1)
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return {
        "ref_edges": len(ref_edges),
        "ours_edges": len(ours_edges),
        "ref_nodes_matched": len(ref_to_ours),
        "ours_nodes_matched": len(ours_to_ref),
        "matched_ref_edges": matched_ref,
        "matched_ours_edges": matched_ours,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


results = []
for name, ref, ours, domain in BENCHMARKS:
    ref_p, ours_p = ROOT / ref, ROOT / ours
    if not ref_p.exists() or not ours_p.exists():
        continue
    ref_text, ours_text = ref_p.read_text(), ours_p.read_text()
    ra, rc = parse_owm(ref_text)
    oa, oc = parse_owm(ours_text)
    ref_nodes = {**ra, **rc}.keys()
    ours_nodes = {**oa, **oc}.keys()
    ref_edges = parse_edges(ref_text)
    ours_edges = parse_edges(ours_text)
    g = grade(ref_nodes, ref_edges, ours_nodes, ours_edges)
    g["name"] = name
    g["domain"] = domain
    results.append(g)

print(f"{'Map':<26} {'Domain':<16} {'RefE':>4} {'OurE':>4} {'OurN':>4}/{'RefN':<4} {'Prec':>6} {'Recall':>7} {'F1':>5}")
print("-" * 92)
for r in results:
    print(f"{r['name']:<26} {r['domain']:<16} {r['ref_edges']:>4} {r['ours_edges']:>4} "
          f"{r['ours_nodes_matched']:>4}/{r['ref_nodes_matched']:<4} "
          f"{r['precision']*100:>5.0f}% {r['recall']*100:>6.0f}% {r['f1']*100:>4.0f}%")

n = len(results)
print(f"\nAggregate across {n} maps:")
for k in ["precision", "recall", "f1"]:
    avg = sum(r[k] for r in results) / max(n, 1)
    print(f"  {k:<10} mean = {avg*100:>4.0f}%")
print(f"  ref_edges  total = {sum(r['ref_edges'] for r in results)}, mean per map = {sum(r['ref_edges'] for r in results)/n:.0f}")
print(f"  ours_edges total = {sum(r['ours_edges'] for r in results)}, mean per map = {sum(r['ours_edges'] for r in results)/n:.0f}")

# F1 distribution.
f1s = sorted(r["f1"] for r in results)
print(f"\nF1 distribution: min={f1s[0]*100:.0f}%  p25={f1s[n//4]*100:.0f}%  median={f1s[n//2]*100:.0f}%  p75={f1s[3*n//4]*100:.0f}%  max={f1s[-1]*100:.0f}%")

# How often is edge F1 close to coverage? (i.e. is the graph grader telling
# us something different from the coverage metric?)
import json as _json
summary = _json.load(open(ROOT / "benchmark-25-summary.json"))
cov_by_name = {r["name"]: r["coverage"] for r in summary["per_map"]}
print(f"\n{'Map':<26} {'Coverage':>9} {'Edge F1':>8} {'Δ':>6}")
print("-" * 50)
deltas = []
for r in sorted(results, key=lambda r: r["f1"] - cov_by_name.get(r["name"], 0)):
    cov = cov_by_name.get(r["name"], 0)
    d = r["f1"] - cov
    deltas.append(d)
    print(f"{r['name']:<26} {cov*100:>8.0f}% {r['f1']*100:>7.0f}% {d*100:>+5.0f}pp")

(ROOT / "graph-grader-summary.json").write_text(json.dumps({
    "n_maps": n,
    "aggregates": {k: sum(r[k] for r in results) / max(n, 1) for k in ["precision", "recall", "f1"]},
    "per_map": results,
}, indent=2))
print(f"\nSaved graph-grader-summary.json")
