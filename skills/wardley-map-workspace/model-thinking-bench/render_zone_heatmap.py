#!/usr/bin/env python3
"""Render per-zone coverage as a heatmap.

Rows: model × thinking. Columns: Wardley's evolution zones (Genesis / Custom /
Product / Commodity). Values: % of reference components in that zone the cell
recovered (mean over 3 reps). Annotated with the per-cell percentage.
"""
from __future__ import annotations
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).parent
OUT = ROOT / "zone-heatmap.png"

data = json.loads((ROOT / "zone_analysis.json").read_text())

# Row ordering: smallest-cheapest → biggest-most-expensive
ROW_ORDER = [
    ("claude-haiku-4-5-20251001", "off", "Haiku 4.5 · off"),
    ("claude-haiku-4-5-20251001", "on",  "Haiku 4.5 · on"),
    ("claude-sonnet-4-6",         "off", "Sonnet 4.6 · off"),
    ("claude-sonnet-4-6",         "on",  "Sonnet 4.6 · on"),
    ("claude-opus-4-7",           "off", "Opus 4.7 · off"),
    ("claude-opus-4-7",           "on",  "Opus 4.7 · on"),
]
ZONES = ["Genesis", "Custom", "Product", "Commodity"]
N_BY_ZONE = {z: len(data["reference_by_zone"][z]) for z in ZONES}
CELL = {(r["model"], r["thinking"]): r["coverage_by_zone"] for r in data["matrix"]}

matrix = np.array(
    [[100 * (CELL[(m, t)][z] or 0) for z in ZONES] for m, t, _ in ROW_ORDER]
)

fig, ax = plt.subplots(figsize=(10.2, 5.8), dpi=160)

im = ax.imshow(matrix, cmap="YlGnBu", vmin=0, vmax=70, aspect="auto")

# Cell text
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        v = matrix[i, j]
        ax.text(
            j, i, f"{v:.0f}%",
            ha="center", va="center",
            color="white" if v > 40 else "#222",
            fontsize=12, fontweight="bold",
        )

ax.set_xticks(range(len(ZONES)))
ax.set_xticklabels([f"{z}\n(n={N_BY_ZONE[z]})" for z in ZONES], fontsize=10.5)
ax.set_yticks(range(len(ROW_ORDER)))
ax.set_yticklabels([label for _, _, label in ROW_ORDER], fontsize=10.5)

# Move column labels to the top so the heatmap reads like a table
ax.xaxis.set_label_position("top")
ax.xaxis.tick_top()

# Highlight the per-zone best
best_per_zone = matrix.argmax(axis=0)
for j, i in enumerate(best_per_zone):
    ax.add_patch(plt.Rectangle((j - 0.48, i - 0.48), 0.96, 0.96,
                               fill=False, edgecolor="#c0392b", linewidth=2.2))

cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02)
cbar.set_label("Coverage (%)", fontsize=10)

fig.suptitle(
    "Per-zone coverage — does the model gap hold across evolution stages?",
    fontsize=13.5, fontweight="bold", y=1.01, x=0.02, ha="left", color="#111",
)
fig.text(
    0.02, 0.955,
    "Red-outlined cell = best in column. Opus-on wins Genesis; Opus-off wins Commodity; "
    "Sonnet-on wins Custom; Product is flat.",
    fontsize=10, color="#444", ha="left",
)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.savefig(OUT, bbox_inches="tight", facecolor="white")
print(f"wrote {OUT}")
