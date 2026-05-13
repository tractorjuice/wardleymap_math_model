#!/usr/bin/env python3
"""Per-zone routing chart — sibling to benchmark-map.png.

Four rows, one per output-map evolution zone. Each row shows the recommended
model + thinking state, the empirical coverage number, and the reasoning.
This is the *deployment* recommendation — distinct from where each model
sits on the benchmark value chain (that's benchmark-map.png).
"""
from __future__ import annotations
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).parent
data = json.loads((ROOT / "zone_analysis.json").read_text())

OPUS = "#d62728"
SONNET = "#ff7f0e"
HAIKU = "#2ca02c"

# Per-zone recommendation. Each entry: zone label, n, model name, model color,
# coverage %, headline rationale.
ROWS = [
    ("Genesis",   13, "Haiku 4.5  + thinking",   HAIKU,  44,
     "Within 12pp of Opus-on at ~10x lower cost. Thinking lifts Haiku +13pp here."),
    ("Custom Built", 9, "Sonnet 4.6 + thinking", SONNET, 48,
     "Judgement zone — mid-tier model that thinks beats both bigger and smaller."),
    ("Product",     8, "Haiku 4.5  (off or on)", HAIKU,  50,
     "Flat across models (42-56%). Standard middle-zone furniture; pick cheapest."),
    ("Commodity",   4, "Opus 4.7   (no thinking)", OPUS, 67,
     "+25pp over next best. Big-model RECALL pays here; thinking actively hurts (67% -> 42%)."),
]

fig, ax = plt.subplots(figsize=(13.5, 7.2), dpi=160)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Header
ax.text(0.02, 0.96, "Per-zone routing policy", fontsize=17, fontweight="bold", color="#111")
ax.text(
    0.02, 0.91,
    "Which model to use for which evolution band of the output map. Empirical, ai-trust pilot, N=3.",
    fontsize=10.5, color="#555",
)

# Column headers
y_header = 0.83
ax.text(0.02, y_header, "Output zone", fontsize=10, fontweight="bold", color="#555")
ax.text(0.22, y_header, "Recommended model", fontsize=10, fontweight="bold", color="#555")
ax.text(0.52, y_header, "Coverage", fontsize=10, fontweight="bold", color="#555")
ax.text(0.64, y_header, "Why", fontsize=10, fontweight="bold", color="#555")
ax.plot([0.02, 0.98], [y_header - 0.02, y_header - 0.02], color="#ccc", lw=0.8)

ROW_H = 0.16
y0 = 0.74

for i, (zone, n, model, color, coverage, rationale) in enumerate(ROWS):
    y = y0 - i * ROW_H

    # Zone block (left)
    ax.text(0.02, y, zone, fontsize=13, fontweight="bold", color="#111")
    ax.text(0.02, y - 0.035, f"n = {n} components", fontsize=9, color="#777")

    # Arrow
    ax.annotate(
        "", xy=(0.21, y), xytext=(0.16, y),
        arrowprops=dict(arrowstyle="->", color="#999", lw=1.4),
    )

    # Model badge
    badge = FancyBboxPatch(
        (0.215, y - 0.04), 0.27, 0.08,
        boxstyle="round,pad=0.005",
        linewidth=1.2, edgecolor=color, facecolor=color, alpha=0.12,
    )
    ax.add_patch(badge)
    ax.text(0.35, y, model, fontsize=11.5, fontweight="bold", color=color, ha="center", va="center")

    # Coverage
    ax.text(0.52, y, f"{coverage}%", fontsize=18, fontweight="bold", color=color, va="center")

    # Rationale (wrap-friendly)
    ax.text(0.64, y + 0.012, rationale, fontsize=10, color="#222", va="center", wrap=True)

# Footer caveat
ax.text(
    0.02, 0.04,
    "Caveat: Commodity column has only 4 reference components, so its 25pp lead is noisy. "
    "Replicate on a low-leakage map (agriculture-regen, culture-gender) before relying on this policy.",
    fontsize=9, color="#888", style="italic",
)

plt.tight_layout()
plt.savefig(ROOT / "routing-chart.png", bbox_inches="tight", facecolor="white")
print(f"wrote {ROOT / 'routing-chart.png'}")
