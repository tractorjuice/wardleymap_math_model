#!/usr/bin/env python3
"""Generate the hero PNG for the model x thinking pilot article.

Two-panel grouped bar chart:
  Left  — coverage % (with stdev error bars)
  Right — wall-clock duration (s)
Both grouped by model with thinking-off / thinking-on side by side.
"""
import json
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

ROOT = Path(__file__).parent
data = json.loads((ROOT / "matrix_summary.json").read_text())

MODELS = [
    ("claude-haiku-4-5-20251001", "Haiku 4.5"),
    ("claude-sonnet-4-6", "Sonnet 4.6"),
    ("claude-opus-4-7", "Opus 4.7"),
]

def row(model_id, thinking):
    for r in data:
        if r["model"] == model_id and r["thinking"] == thinking:
            return r
    raise KeyError(f"{model_id} / {thinking}")

OFF_COLOR = "#9ecae1"
ON_COLOR = "#08519c"
ANNOT_KW = dict(ha="center", va="bottom", fontsize=9, color="#222")

fig, (ax_cov, ax_dur) = plt.subplots(
    1, 2, figsize=(11.5, 5.0), dpi=160, gridspec_kw=dict(wspace=0.28)
)

# ---------- Coverage panel ----------
x = list(range(len(MODELS)))
w = 0.36
cov_off = [100 * row(m[0], "off")["coverage_mean"] for m in MODELS]
cov_on  = [100 * row(m[0], "on")["coverage_mean"]  for m in MODELS]
err_off = [100 * row(m[0], "off")["coverage_stdev"] for m in MODELS]
err_on  = [100 * row(m[0], "on")["coverage_stdev"]  for m in MODELS]

b1 = ax_cov.bar([xi - w/2 for xi in x], cov_off, w, yerr=err_off,
                color=OFF_COLOR, label="thinking off",
                error_kw=dict(ecolor="#444", capsize=4, elinewidth=1))
b2 = ax_cov.bar([xi + w/2 for xi in x], cov_on,  w, yerr=err_on,
                color=ON_COLOR,  label="thinking on",
                error_kw=dict(ecolor="#444", capsize=4, elinewidth=1))

for xi, v in zip(x, cov_off):
    ax_cov.text(xi - w/2, v + 1.2, f"{v:.1f}%", **ANNOT_KW)
for xi, v in zip(x, cov_on):
    ax_cov.text(xi + w/2, v + 1.2, f"{v:.1f}%", **ANNOT_KW, fontweight="bold")

ax_cov.set_xticks(x)
ax_cov.set_xticklabels([m[1] for m in MODELS], fontsize=11)
ax_cov.set_ylabel("Coverage of Wardley's components (%)", fontsize=10)
ax_cov.set_ylim(0, 60)
ax_cov.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
ax_cov.set_title("Coverage", fontsize=12, pad=10, loc="left", color="#222")
ax_cov.legend(frameon=False, loc="upper left", fontsize=9)
ax_cov.grid(axis="y", linestyle="--", alpha=0.4)
ax_cov.spines[["top", "right"]].set_visible(False)

# ---------- Duration panel ----------
dur_off = [row(m[0], "off")["duration_sec_mean"] for m in MODELS]
dur_on  = [row(m[0], "on")["duration_sec_mean"]  for m in MODELS]

ax_dur.bar([xi - w/2 for xi in x], dur_off, w, color=OFF_COLOR, label="thinking off")
ax_dur.bar([xi + w/2 for xi in x], dur_on,  w, color=ON_COLOR,  label="thinking on")

for xi, v in zip(x, dur_off):
    ax_dur.text(xi - w/2, v + 10, f"{v:.0f}s", **ANNOT_KW)
for xi, v in zip(x, dur_on):
    ax_dur.text(xi + w/2, v + 10, f"{v:.0f}s", **ANNOT_KW, fontweight="bold")

ax_dur.set_xticks(x)
ax_dur.set_xticklabels([m[1] for m in MODELS], fontsize=11)
ax_dur.set_ylabel("Wall-clock per map (s)", fontsize=10)
ax_dur.set_ylim(0, max(dur_on) * 1.18)
ax_dur.set_title("Latency", fontsize=12, pad=10, loc="left", color="#222")
ax_dur.grid(axis="y", linestyle="--", alpha=0.4)
ax_dur.spines[["top", "right"]].set_visible(False)

# ---------- Top-line title ----------
fig.suptitle(
    "Bigger model > more thinking — and the gap widens on coverage",
    fontsize=14, fontweight="bold", y=1.02, x=0.07, ha="left", color="#111"
)
fig.text(
    0.07, 0.965,
    "ai-trust pilot — 3 models × 2 thinking states × 3 replicates. "
    "Opus 4.7 leads coverage regardless of thinking; "
    "thinking lifts Haiku +5pp but Opus only +1pp.",
    fontsize=9.5, color="#444", ha="left",
)

out = ROOT / "hero.png"
plt.savefig(out, bbox_inches="tight", facecolor="white")
print(f"wrote {out}")
