#!/usr/bin/env python3
"""Two side-by-side routing charts.

  routing-empirical.png  — best cell per zone from zone_analysis.json,
                            with no cost reasoning. Honest to the numbers.
  routing-cost-aware.png — cost/quality tradeoff. Picks the cheapest model
                            whose coverage is competitive with the empirical
                            best; each row notes the gap and why.
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


# ---------- Empirical winners (no cost reasoning) ----------
# Pulled directly from zone_analysis.json: argmax(coverage) per zone.
EMPIRICAL = [
    ("Genesis",      13, "Opus 4.7   + thinking",   OPUS,   56,
     "Opus-on tops Genesis by 12pp over Haiku-on (44%)."),
    ("Custom Built",  9, "Sonnet 4.6 + thinking",   SONNET, 48,
     "Mid-tier model that thinks beats both bigger and smaller."),
    ("Product",       8, "Sonnet 4.6 (no thinking)", SONNET, 56,
     "Edges out Opus-off and Haiku-off (both 50-54%)."),
    ("Commodity",     4, "Opus 4.7   (no thinking)", OPUS,   67,
     "+25pp over next best. Thinking hurts here (67% -> 42%)."),
]

# ---------- Cost-aware policy ----------
# Pick the cheapest model whose coverage isn't far from the empirical best.
# Per-call cost ratio (with prompt caching, ai-trust pilot):
#   Haiku  ~$0.32  ·  Sonnet  ~$1.15  ·  Opus  ~$5.93
COST_AWARE = [
    ("Genesis",      13, "Haiku 4.5  + thinking",    HAIKU,  44,
     "12pp behind Opus-on (56%), ~18x cheaper. Take the trade if running at volume."),
    ("Custom Built",  9, "Sonnet 4.6 + thinking",    SONNET, 48,
     "Matches the empirical best. No cheaper option is competitive."),
    ("Product",       8, "Haiku 4.5  (no thinking)", HAIKU,  50,
     "6pp behind Sonnet-off (56%), ~4x cheaper. Zone is flat enough to drop tier."),
    ("Commodity",     4, "Opus 4.7   (no thinking)", OPUS,   67,
     "+25pp over next best. No cheaper model gets close; pay for Opus here."),
]


def render(rows, title, subtitle, out_path):
    fig, ax = plt.subplots(figsize=(13.5, 7.2), dpi=160)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.02, 0.96, title, fontsize=17, fontweight="bold", color="#111")
    ax.text(0.02, 0.91, subtitle, fontsize=10.5, color="#555")

    y_header = 0.83
    ax.text(0.02, y_header, "Output zone", fontsize=10, fontweight="bold", color="#555")
    ax.text(0.22, y_header, "Model", fontsize=10, fontweight="bold", color="#555")
    ax.text(0.52, y_header, "Coverage", fontsize=10, fontweight="bold", color="#555")
    ax.text(0.64, y_header, "Note", fontsize=10, fontweight="bold", color="#555")
    ax.plot([0.02, 0.98], [y_header - 0.02, y_header - 0.02], color="#ccc", lw=0.8)

    ROW_H = 0.16
    y0 = 0.74
    for i, (zone, n, model, color, coverage, note) in enumerate(rows):
        y = y0 - i * ROW_H

        ax.text(0.02, y, zone, fontsize=13, fontweight="bold", color="#111")
        ax.text(0.02, y - 0.035, f"n = {n} components", fontsize=9, color="#777")

        ax.annotate(
            "", xy=(0.21, y), xytext=(0.16, y),
            arrowprops=dict(arrowstyle="->", color="#999", lw=1.4),
        )

        badge = FancyBboxPatch(
            (0.215, y - 0.04), 0.27, 0.08,
            boxstyle="round,pad=0.005",
            linewidth=1.2, edgecolor=color, facecolor=color, alpha=0.12,
        )
        ax.add_patch(badge)
        ax.text(0.35, y, model, fontsize=11.5, fontweight="bold",
                color=color, ha="center", va="center")

        ax.text(0.52, y, f"{coverage}%", fontsize=18, fontweight="bold",
                color=color, va="center")

        ax.text(0.64, y + 0.012, note, fontsize=10, color="#222", va="center", wrap=True)

    ax.text(
        0.02, 0.04,
        "Caveat: Commodity column has only 4 reference components, so its 25pp lead is noisy. "
        "Replicate on a low-leakage map (agriculture-regen, culture-gender) before relying on this.",
        fontsize=9, color="#888", style="italic",
    )

    plt.tight_layout()
    plt.savefig(out_path, bbox_inches="tight", facecolor="white")
    print(f"wrote {out_path}")


def main():
    render(
        EMPIRICAL,
        "Per-zone empirical best",
        "Highest coverage per zone, no cost weighting. ai-trust pilot, N=3.",
        ROOT / "routing-empirical.png",
    )
    render(
        COST_AWARE,
        "Per-zone cost-aware routing",
        "Cheapest competitive model per zone (cost gap vs empirical best in notes column).",
        ROOT / "routing-cost-aware.png",
    )

    # Remove the older single-chart artefact so the article isn't ambiguous
    old = ROOT / "routing-chart.png"
    if old.exists():
        old.unlink()
        print(f"removed stale {old}")


if __name__ == "__main__":
    main()
