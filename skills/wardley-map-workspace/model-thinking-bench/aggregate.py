#!/usr/bin/env python3
"""Aggregate model x thinking benchmark results for ai-trust.

Per cell:
  - components, coverage, same-band %, |Δε| median, |Δν| median,
    ν-bias, ε-bias, density, validator pass

Per (model, thinking) — mean and stdev across replicates.

Outputs:
  - cell_metrics.json  (per-cell)
  - matrix_summary.json (per-condition aggregate)
  - matrix_summary.md (table for humans)
"""
from __future__ import annotations
import json
import re
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent
REPO = ROOT.parents[2]
sys.path.insert(0, str(REPO / "skills/wardley-map-workspace/iteration-10"))
from compare import parse_owm, fuzzy_match  # noqa: E402

REFERENCE_PATH = REPO / "skills/wardley-map-workspace/iteration-10/eval-ai-trust/wardley-reference.owm"
VALIDATOR = REPO / "skills/wardley-map/scripts/validate_owm.mjs"
OUTPUTS = ROOT / "outputs"


def stage_of(eps: float) -> int:
    if eps < 0.25:
        return 0
    if eps < 0.5:
        return 1
    if eps < 0.75:
        return 2
    return 3


def extract_owm_block(md_text: str) -> str | None:
    m = re.search(r"```owm\s*\n(.*?)\n```", md_text, re.DOTALL)
    return m.group(1) if m else None


def run_validator(owm_text: str) -> tuple[bool, str]:
    with tempfile.NamedTemporaryFile("w", suffix=".owm", delete=False) as f:
        f.write(owm_text)
        path = f.name
    try:
        res = subprocess.run(
            ["node", str(VALIDATOR), path],
            capture_output=True,
            text=True,
            timeout=30,
        )
        return res.returncode == 0, (res.stdout + res.stderr)[:2000]
    except Exception as exc:
        return False, f"validator error: {exc!r}"
    finally:
        Path(path).unlink(missing_ok=True)


def metrics_for_cell(md_text: str, ref_anchors: dict, ref_comps: dict) -> dict:
    owm = extract_owm_block(md_text)
    if not owm:
        return {
            "status": "no_owm_block",
            "components": 0,
            "anchors": 0,
            "validator_pass": False,
            "coverage": None,
            "same_band_pct": None,
            "abs_de_median": None,
            "abs_dv_median": None,
            "nu_bias": None,
            "eps_bias": None,
        }
    ours_anchors, ours_comps = parse_owm(owm)
    matched = []
    for rname, (rv, re_) in ref_comps.items():
        match, score = fuzzy_match(rname, ours_comps.keys())
        if match:
            ov, oe = ours_comps[match]
            matched.append((rname, rv, re_, match, ov, oe, score))
    coverage = len(matched) / len(ref_comps) if ref_comps else None
    if matched:
        same_band = sum(1 for _, rv, re_, _, ov, oe, _ in matched if stage_of(re_) == stage_of(oe))
        same_band_pct = same_band / len(matched)
        abs_de = [abs(re_ - oe) for _, rv, re_, _, ov, oe, _ in matched]
        abs_dv = [abs(rv - ov) for _, rv, re_, _, ov, oe, _ in matched]
        nu_bias = statistics.mean(ov - rv for _, rv, _, _, ov, _, _ in matched)
        eps_bias = statistics.mean(oe - re_ for _, _, re_, _, _, oe, _ in matched)
        abs_de_med = statistics.median(abs_de)
        abs_dv_med = statistics.median(abs_dv)
    else:
        same_band_pct = abs_de_med = abs_dv_med = nu_bias = eps_bias = None
    valid_ok, valid_msg = run_validator(owm)
    return {
        "status": "ok",
        "components": len(ours_comps),
        "anchors": len(ours_anchors),
        "matched": len(matched),
        "ref_components": len(ref_comps),
        "validator_pass": valid_ok,
        "validator_msg_snippet": valid_msg.splitlines()[-1] if valid_msg else "",
        "coverage": coverage,
        "same_band_pct": same_band_pct,
        "abs_de_median": abs_de_med,
        "abs_dv_median": abs_dv_med,
        "nu_bias": nu_bias,
        "eps_bias": eps_bias,
    }


def collect_cells():
    ref_text = REFERENCE_PATH.read_text()
    ref_anchors, ref_comps = parse_owm(ref_text)
    print(f"reference: {len(ref_anchors)} anchors, {len(ref_comps)} components")

    cells = []
    for cell_md in sorted(OUTPUTS.glob("eval-ai-trust/*/thinking-*/run-*/outputs/output.md")):
        rel = cell_md.relative_to(OUTPUTS)
        # eval-ai-trust/<model>/thinking-<state>/run-<n>/outputs/output.md
        parts = rel.parts
        model = parts[1]
        thinking = parts[2].replace("thinking-", "")
        rep = int(parts[3].replace("run-", ""))
        timing = json.loads((cell_md.parent.parent / "timing.json").read_text())
        text = cell_md.read_text()
        m = metrics_for_cell(text, ref_anchors, ref_comps)
        cells.append(
            {
                "model": model,
                "thinking": thinking,
                "rep": rep,
                "duration_sec": timing.get("duration_sec"),
                "usage": timing.get("usage_totals"),
                "last_stop": timing.get("last_stop"),
                "agent_turns": timing.get("agent_turns"),
                **m,
            }
        )
    return cells, ref_comps


def safe(values, fn):
    vals = [v for v in values if v is not None]
    if not vals:
        return None
    return fn(vals)


def aggregate(cells):
    groups: dict[tuple, list] = {}
    for c in cells:
        groups.setdefault((c["model"], c["thinking"]), []).append(c)
    rows = []
    for (model, thinking), reps in sorted(groups.items()):
        n = len(reps)
        row = {
            "model": model,
            "thinking": thinking,
            "n_reps": n,
            "validator_pass_rate": sum(1 for r in reps if r["validator_pass"]) / n,
            "components_mean": safe([r["components"] for r in reps], statistics.mean),
            "coverage_mean": safe([r["coverage"] for r in reps], statistics.mean),
            "coverage_stdev": safe([r["coverage"] for r in reps], lambda v: statistics.stdev(v) if len(v) > 1 else 0.0),
            "same_band_pct_mean": safe([r["same_band_pct"] for r in reps], statistics.mean),
            "abs_de_median_mean": safe([r["abs_de_median"] for r in reps], statistics.mean),
            "abs_dv_median_mean": safe([r["abs_dv_median"] for r in reps], statistics.mean),
            "nu_bias_mean": safe([r["nu_bias"] for r in reps], statistics.mean),
            "eps_bias_mean": safe([r["eps_bias"] for r in reps], statistics.mean),
            "duration_sec_mean": safe([r["duration_sec"] for r in reps], statistics.mean),
            "agent_turns_mean": safe([r["agent_turns"] for r in reps], statistics.mean),
        }
        rows.append(row)
    return rows


def fmt(v, pct=False, places=3):
    if v is None:
        return "—"
    if pct:
        return f"{100*v:.1f}%"
    return f"{v:.{places}f}"


def write_markdown(rows, path: Path):
    headers = [
        "model",
        "thinking",
        "n",
        "valid%",
        "comps",
        "coverage",
        "same-band",
        "|Δε|",
        "|Δν|",
        "ν-bias",
        "ε-bias",
        "dur(s)",
        "turns",
    ]
    lines = [
        "# Model × thinking benchmark — ai-trust",
        "",
        f"Reference: `{REFERENCE_PATH.relative_to(REPO)}`",
        f"Cells: 3 models × 2 thinking states × 3 replicates = 18.",
        "",
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    for r in rows:
        cells = [
            r["model"].replace("claude-", "").replace("-20251001", ""),
            r["thinking"],
            str(r["n_reps"]),
            fmt(r["validator_pass_rate"], pct=True),
            fmt(r["components_mean"], places=1),
            fmt(r["coverage_mean"], pct=True),
            fmt(r["same_band_pct_mean"], pct=True),
            fmt(r["abs_de_median_mean"]),
            fmt(r["abs_dv_median_mean"]),
            fmt(r["nu_bias_mean"]),
            fmt(r["eps_bias_mean"]),
            fmt(r["duration_sec_mean"], places=1),
            fmt(r["agent_turns_mean"], places=1),
        ]
        lines.append("| " + " | ".join(cells) + " |")
    path.write_text("\n".join(lines) + "\n")


def main():
    cells, _ = collect_cells()
    if not cells:
        print("No cells found.")
        return
    (ROOT / "cell_metrics.json").write_text(json.dumps(cells, indent=2))
    rows = aggregate(cells)
    (ROOT / "matrix_summary.json").write_text(json.dumps(rows, indent=2))
    write_markdown(rows, ROOT / "matrix_summary.md")
    print(f"Aggregated {len(cells)} cells into {len(rows)} (model, thinking) groups")
    print(f"  cell_metrics.json")
    print(f"  matrix_summary.json")
    print(f"  matrix_summary.md")


if __name__ == "__main__":
    main()
