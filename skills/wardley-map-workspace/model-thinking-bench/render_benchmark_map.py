#!/usr/bin/env python3
"""Render benchmark.owm as a static PNG Wardley map.

GitHub's mermaid wardley-beta rendering is good for the live README, but a
static PNG is useful for the article (and for places where wardley-beta is
unavailable). Highlights the three model nodes in distinct colours and
annotates each with its headline performance number from matrix_summary.json.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

ROOT = Path(__file__).parent
OWM = ROOT / "benchmark.owm"
SUMMARY = ROOT / "matrix_summary.json"
OUT = ROOT / "benchmark-map.png"

ANCHOR_RE = re.compile(r"^anchor\s+([^\[]+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\]")
COMP_RE = re.compile(r"^component\s+([^\[]+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\]")
EDGE_RE = re.compile(r"^([^\-]+?)\s*->\s*(.+?)\s*$")


def parse_owm(text: str):
    anchors, components, edges = {}, {}, []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        if m := ANCHOR_RE.match(line):
            anchors[m.group(1).strip()] = (float(m.group(2)), float(m.group(3)))
            continue
        if m := COMP_RE.match(line):
            components[m.group(1).strip()] = (float(m.group(2)), float(m.group(3)))
            continue
        if m := EDGE_RE.match(line):
            edges.append((m.group(1).strip(), m.group(2).strip()))
    return anchors, components, edges


def main():
    anchors, components, edges = parse_owm(OWM.read_text())
    summary = {(r["model"], r["thinking"]): r for r in json.loads(SUMMARY.read_text())}

    # Per-zone routing finding from zone_analysis.json — what each model is best at.
    # Opus appears for both Genesis-on and Commodity-off; the model_strength
    # caption captures the headline cell.
    perf_lines = {
        "Opus 4.7": _perf("claude-opus-4-7", summary),
        "Sonnet 4.6": _perf("claude-sonnet-4-6", summary),
        "Haiku 4.5": _perf("claude-haiku-4-5-20251001", summary),
    }
    model_strength = {
        "Opus 4.7":   ("best: Commodity 67% (off)  ·  Genesis 56% (on)", "#d62728"),
        "Sonnet 4.6": ("best: Custom 48% (on)", "#ff7f0e"),
        "Haiku 4.5":  ("competitive Genesis 44% (on), 10x cheaper than Opus", "#2ca02c"),
    }
    model_colors = {name: color for name, (_, color) in model_strength.items()}

    fig, ax = plt.subplots(figsize=(15.0, 11.5), dpi=140)
    plt.subplots_adjust(bottom=0.22)  # reserve space for the routing panel

    # Evolution zone backgrounds
    zones = [
        (0.00, 0.25, "#fafafa", "Genesis"),
        (0.25, 0.50, "#f0f0f0", "Custom Built"),
        (0.50, 0.75, "#e6e6e6", "Product (+rental)"),
        (0.75, 1.00, "#dcdcdc", "Commodity (+utility)"),
    ]
    for x0, x1, color, label in zones:
        ax.axvspan(x0, x1, color=color, zorder=0)
        ax.text((x0 + x1) / 2, 1.02, label, ha="center", va="bottom",
                fontsize=11, color="#555")

    # Edges (drawn first so dots sit on top)
    all_nodes = {**anchors, **components}
    for src, tgt in edges:
        if src not in all_nodes or tgt not in all_nodes:
            continue
        sv, se = all_nodes[src]
        tv, te = all_nodes[tgt]
        ax.add_patch(FancyArrowPatch(
            (se, sv), (te, tv),
            arrowstyle="-",
            color="#999", linewidth=0.8, alpha=0.55, zorder=1,
        ))

    # Anchor (user need): big square
    for name, (v, e) in anchors.items():
        ax.scatter([e], [v], s=260, color="#000", marker="s", zorder=4)
        ax.annotate(name, (e, v), xytext=(8, 6), textcoords="offset points",
                    fontsize=11, fontweight="bold", color="#000", zorder=5)

    # Regular components
    for name, (v, e) in components.items():
        if name in model_colors:
            continue  # render models below with special styling
        ax.scatter([e], [v], s=110, color="#fff", edgecolor="#222",
                   linewidth=1.4, zorder=3)
        ax.annotate(name, (e, v), xytext=(8, 4), textcoords="offset points",
                    fontsize=9.5, color="#222", zorder=4)

    # Highlighted: the three models, each with a zone-strength badge.
    for name, color in model_colors.items():
        if name not in components:
            continue
        v, e = components[name]
        ax.scatter([e], [v], s=320, color=color, edgecolor="#111",
                   linewidth=1.8, zorder=5)
        ax.annotate(
            name,
            (e, v),
            xytext=(0, -28),
            textcoords="offset points",
            ha="center", va="top",
            fontsize=11.5, fontweight="bold", color=color, zorder=6,
        )
        if perf_lines.get(name):
            ax.annotate(
                perf_lines[name],
                (e, v),
                xytext=(0, -44),
                textcoords="offset points",
                ha="center", va="top",
                fontsize=9, color="#333", zorder=6,
            )
        strength_text, _ = model_strength.get(name, ("", ""))
        if strength_text:
            ax.annotate(
                strength_text,
                (e, v),
                xytext=(0, -60),
                textcoords="offset points",
                ha="center", va="top",
                fontsize=8.5, color=color, fontstyle="italic", zorder=6,
            )

    # Per-zone routing policy panel (top-right)
    routing_lines = [
        ("Per-zone routing policy", "#111", True),
        ("(empirical from zone_analysis.json — N=3, single map)", "#777", False),
        ("", "#000", False),
        ("Genesis   →  Haiku 4.5 + thinking   (44%, ~10x cheaper than Opus)", "#2ca02c", False),
        ("Custom    →  Sonnet 4.6 + thinking  (48%, judgement zone)", "#ff7f0e", False),
        ("Product   →  Haiku 4.5  (flat across models, pick cheapest)", "#2ca02c", False),
        ("Commodity →  Opus 4.7 (off)  (67%, +25pp over next best)", "#d62728", False),
    ]
    # Routing panel rendered in figure coordinates below the axes — keeps
    # the value-chain area unobstructed.
    panel_top_y = 0.18   # in figure coordinates
    panel_left_x = 0.07
    line_step = 0.022
    for i, (text, color, bold) in enumerate(routing_lines):
        fig.text(
            panel_left_x, panel_top_y - i * line_step, text,
            fontsize=10.5 if bold else 9.5,
            fontweight="bold" if bold else "normal",
            color=color, family="monospace",
            ha="left", va="top",
        )

    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.06)
    ax.set_xlabel("Evolution  →", fontsize=11)
    ax.set_ylabel("Visibility (closer to user →)", fontsize=11)
    ax.set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticks([0.0, 0.25, 0.5, 0.75, 1.0])
    ax.grid(False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    fig.suptitle(
        "Where the three Claude models sit on the benchmark's value chain",
        fontsize=14, fontweight="bold", y=0.99, x=0.07, ha="left", color="#111",
    )
    fig.text(
        0.07, 0.94,
        "Models drawn at the same visibility (every cell calls one) but staggered by evolution: "
        "Opus 4.7 still Custom Built, Haiku 4.5 nearly commoditised.",
        fontsize=10, color="#444", ha="left",
    )

    plt.savefig(OUT, bbox_inches="tight", facecolor="white")
    print(f"wrote {OUT}")


def _perf(model_id, summary):
    row = summary.get((model_id, "off"))
    if not row:
        return ""
    return (
        f"coverage {100 * row['coverage_mean']:.0f}%   "
        f"|Δε| {row['abs_de_median_mean']:.2f}   "
        f"{row['duration_sec_mean']:.0f}s"
    )


if __name__ == "__main__":
    main()
