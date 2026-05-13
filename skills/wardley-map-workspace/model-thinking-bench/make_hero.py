#!/usr/bin/env python3
"""Hero PNG — which Claude to use, indexed by the kind of map you're drawing.

Layout uses two stacked rows (top: decision cards, bottom: per-zone evidence)
with hand-tuned spacing so titles never overflow card boundaries. Card sizes
are picked so the widest title at the chosen fontsize still has margin.
"""
from __future__ import annotations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

ROOT = Path(__file__).parent
OUT = ROOT / "hero.png"

# Zone palette — purple to green, no red.
GENESIS_C   = "#8e44ad"
CUSTOM_C    = "#e67e22"
PRODUCT_C   = "#2980b9"
COMMODITY_C = "#16a085"

INK = "#111"
SUBINK = "#555"
DARK_ON_TINT = "#1a1a1a"

# Three top-row decision rules. Titles kept short so they fit comfortably
# inside the card width; the explanatory line lives in `subkind`.
RULES = [
    {
        "tag":      "WORKING ON SOMETHING",
        "kind":     "NEW & NOVEL",
        "subkind":  "emerging tech, new market, fresh regulation",
        "verdict":  "Opus 4.7  +  thinking",
        "color":    GENESIS_C,
        "support": [
            "Thinking lifts Opus +15pp on Genesis",
            "(41% → 56%) — the zone the model",
            "hasn't memorised. Reasoning earns",
            "its keep here.",
        ],
    },
    {
        "tag":      "WORKING ON A",
        "kind":     "WELL-KNOWN MAP",
        "subkind":  "mature industry, familiar stack, standard arch.",
        "verdict":  "Opus 4.7  —  no thinking",
        "color":    PRODUCT_C,
        "support": [
            "47% overall, 225s, validator-clean.",
            "Dominates Commodity +25pp.",
            "Thinking HURTS Commodity here",
            "(67% → 42%) — don't pay for it.",
        ],
    },
    {
        "tag":      "OR IF YOU'RE",
        "kind":     "COST-SENSITIVE",
        "subkind":  "many maps, batch use, prototyping",
        "verdict":  "Haiku 4.5  +  thinking",
        "color":    COMMODITY_C,
        "support": [
            "38% overall, ~18× cheaper per call.",
            "Within 12pp of Opus-on on Genesis.",
            "Drops a tier overall; eats almost",
            "no quality on Product.",
        ],
    },
]

ZONES = [
    ("Genesis",      13, "Opus 4.7",   "thinking ON",  56, GENESIS_C),
    ("Custom Built",  9, "Sonnet 4.6", "thinking ON",  48, CUSTOM_C),
    ("Product",       8, "Sonnet 4.6", "no thinking",  56, PRODUCT_C),
    ("Commodity",     4, "Opus 4.7",   "no thinking",  67, COMMODITY_C),
]


def draw_rule_card(ax, x, y, w, h, rule):
    color = rule["color"]

    # Card body
    body = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.005,rounding_size=0.015",
        linewidth=1.6, edgecolor=color, facecolor=color, alpha=0.08,
    )
    ax.add_patch(body)

    # Top colour band
    band_h = 0.060
    band = Rectangle((x, y + h - band_h), w, band_h, facecolor=color, alpha=0.92)
    ax.add_patch(band)

    cx = x + w / 2
    # Tag inside band
    ax.text(cx, y + h - band_h / 2, rule["tag"],
            fontsize=12, fontweight="bold", color="white",
            ha="center", va="center", alpha=0.95)

    # Kind name — the headline phrase, sized to fit the card
    ax.text(cx, y + h - band_h - 0.040, rule["kind"],
            fontsize=20, fontweight="bold", color=color,
            ha="center", va="center")

    # Subkind line
    ax.text(cx, y + h - band_h - 0.080, rule["subkind"],
            fontsize=11.5, color=SUBINK, ha="center", va="center", style="italic")

    # "USE" label
    ax.text(cx, y + h - band_h - 0.140, "USE",
            fontsize=12, fontweight="bold", color="#888",
            ha="center", va="center")

    # Verdict — model + thinking
    ax.text(cx, y + h - band_h - 0.190, rule["verdict"],
            fontsize=20, fontweight="bold", color=DARK_ON_TINT,
            ha="center", va="center")

    # Divider before support text
    ax.plot([x + 0.02, x + w - 0.02],
            [y + h - band_h - 0.235, y + h - band_h - 0.235],
            color="#ddd", lw=0.6)

    # Support text — pre-wrapped to 4 short lines per card
    line_height = 0.030
    support_top = y + h - band_h - 0.275
    for i, line in enumerate(rule["support"]):
        ax.text(cx, support_top - i * line_height, line,
                fontsize=12, color=INK, ha="center", va="top")


def draw_zone_pill(ax, x, y, w, h, zone, n, model, state, cov, color):
    body = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.012",
        linewidth=1.0, edgecolor=color, facecolor=color, alpha=0.10,
    )
    ax.add_patch(body)

    # Top band — zone name on one line, n=N on a second so neither overflows
    band_h = 0.080
    band = Rectangle((x, y + h - band_h), w, band_h, facecolor=color, alpha=0.92)
    ax.add_patch(band)
    cx = x + w / 2
    ax.text(cx, y + h - 0.028, zone.upper(),
            fontsize=20, fontweight="bold", color="white", ha="center", va="center")
    ax.text(cx, y + h - 0.061, f"n = {n} components",
            fontsize=11, color="white", alpha=0.9, ha="center", va="center")

    # Model name + state
    ax.text(cx, y + h - band_h - 0.040, model,
            fontsize=22, fontweight="bold", color=DARK_ON_TINT,
            ha="center", va="center")
    ax.text(cx, y + h - band_h - 0.080, state,
            fontsize=15, color=DARK_ON_TINT, ha="center", va="center", style="italic")

    # Coverage number
    ax.text(cx, y + 0.045, f"{cov}%",
            fontsize=46, fontweight="bold", color=color,
            ha="center", va="center")


def main():
    # Figure sized to give cards real breathing room
    fig = plt.figure(figsize=(17.0, 11.5), dpi=150)
    fig.patch.set_facecolor("white")

    # The main axes occupy most of the figure; title sits above.
    ax = fig.add_axes([0.03, 0.02, 0.94, 0.85])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Title + subtitle
    fig.text(0.03, 0.965,
             "Which Claude should you use? Pick by the kind of Wardley map you're drawing.",
             fontsize=24, fontweight="bold", color=INK)
    fig.text(0.03, 0.925,
             "ai-trust pilot — recommendations above, per-zone evidence below. "
             "Colour = evolution stage; no red.",
             fontsize=14, color=SUBINK)

    # ===== STEP 1: decision rule cards =====
    ax.text(0.005, 0.985,
            "STEP 1 — What kind of map is this?",
            fontsize=13, fontweight="bold", color="#888",
            ha="left", va="top", transform=ax.transAxes)

    n_cards = len(RULES)
    card_w = 0.305
    gap = (1.0 - n_cards * card_w) / (n_cards + 1)
    card_h = 0.52
    card_y = 0.42
    for i, rule in enumerate(RULES):
        x = gap + i * (card_w + gap)
        draw_rule_card(ax, x, card_y, card_w, card_h, rule)

    # Divider between sections
    div_y = 0.38
    ax.plot([0.005, 0.995], [div_y, div_y], color="#ddd", lw=1.0)

    # ===== STEP 2: per-zone evidence strip =====
    ax.text(0.005, div_y - 0.015,
            "STEP 2 — Or dial it in per zone of the output map",
            fontsize=13, fontweight="bold", color="#888", ha="left", va="top")

    nz = len(ZONES)
    z_w = 0.225
    z_gap = (1.0 - nz * z_w) / (nz + 1)
    z_y = 0.05
    z_h = 0.30
    for i, (zone, count, model, state, cov, color) in enumerate(ZONES):
        x = z_gap + i * (z_w + z_gap)
        draw_zone_pill(ax, x, z_y, z_w, z_h, zone, count, model, state, cov, color)

    # Evolution arrow
    arrow_y = 0.018
    ax.annotate("", xy=(0.995, arrow_y), xytext=(0.005, arrow_y),
                arrowprops=dict(arrowstyle="-|>", color="#aaa",
                                lw=1.2, mutation_scale=14))
    ax.text(0.0, arrow_y + 0.012, "less evolved", fontsize=11,
            color="#888", ha="left", va="bottom", style="italic")
    ax.text(1.0, arrow_y + 0.012, "more evolved", fontsize=11,
            color="#888", ha="right", va="bottom", style="italic")

    plt.savefig(OUT, bbox_inches="tight", facecolor="white")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
