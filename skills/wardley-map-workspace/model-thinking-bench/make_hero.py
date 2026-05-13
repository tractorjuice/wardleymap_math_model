#!/usr/bin/env python3
"""Hero PNG — which Claude to use, indexed by the kind of map you're drawing.

Two stacked sections:
  - Top: three decision rules, colour-coded by the *kind of work* they apply
    to (red = new / Genesis, blue = standard / Product, green = utility / cost).
  - Bottom: the per-zone empirical evidence the rules are built from, with
    each zone shaded in its Wardley-convention colour.

Colours encode evolution stage / strategic intent — not model identity.
Model names appear in dark text within their zone's colour band so the eye
links a recommendation to the band of the output map it applies to.
"""
from __future__ import annotations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

ROOT = Path(__file__).parent
OUT = ROOT / "hero.png"

# Zone palette — rare-to-mature spectrum:
# Genesis = purple (rare/exotic/novel); Custom = orange (industrialising);
# Product = blue (stable, well-understood); Commodity = green (utility, mature).
# Red intentionally avoided — it reads as warning/error in most UIs.
GENESIS_C  = "#8e44ad"
CUSTOM_C   = "#e67e22"
PRODUCT_C  = "#2980b9"
COMMODITY_C = "#16a085"

INK = "#111"
SUBINK = "#555"
DARK_ON_TINT = "#1a1a1a"

# --- Top: three decision rules. Colour follows the zone the rule targets. ---
RULES = [
    {
        "tag": "WORKING ON SOMETHING",
        "kind": "NEW & NOVEL",
        "subkind": "(emerging tech, fresh regulation, new market)",
        "verdict": "Opus 4.7  +  thinking",
        "color": GENESIS_C,
        "support": "Thinking lifts Opus +15pp on Genesis\n(41% → 56%) — the zone the model\n"
                   "hasn't memorised. Reasoning earns\nits keep here.",
    },
    {
        "tag": "WORKING ON A",
        "kind": "STANDARD / WELL-KNOWN LANDSCAPE",
        "subkind": "(mature industry, familiar stack, standard architecture)",
        "verdict": "Opus 4.7  —  no thinking",
        "color": PRODUCT_C,
        "support": "47% overall, 225s, validator-clean.\nDominates Commodity +25pp.\n"
                   "Thinking actively HURTS Commodity\n(67% → 42%) — don't pay for it.",
    },
    {
        "tag": "OR IF YOU'RE",
        "kind": "COST-SENSITIVE AT VOLUME",
        "subkind": "(many maps, batch use, prototyping)",
        "verdict": "Haiku 4.5  +  thinking",
        "color": COMMODITY_C,
        "support": "38% overall, ~18× cheaper than Opus.\nWithin 12pp of Opus-on on Genesis.\n"
                   "Drops a tier overall; eats almost\nno quality on Product.",
    },
]

# --- Bottom: per-zone evidence. Colour = zone, not model. ----------------
ZONES = [
    ("Genesis",      13, "Opus 4.7",   "thinking ON",  56, GENESIS_C),
    ("Custom Built",  9, "Sonnet 4.6", "thinking ON",  48, CUSTOM_C),
    ("Product",       8, "Sonnet 4.6", "no thinking",  56, PRODUCT_C),
    ("Commodity",     4, "Opus 4.7",   "no thinking",  67, COMMODITY_C),
]


def draw_rule_card(ax, x, y, w, h, rule):
    color = rule["color"]
    body = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.005,rounding_size=0.015",
        linewidth=1.6, edgecolor=color, facecolor=color, alpha=0.08,
    )
    ax.add_patch(body)
    band = Rectangle((x, y + h - 0.075), w, 0.075, facecolor=color, alpha=0.92)
    ax.add_patch(band)
    cx = x + w / 2
    ax.text(cx, y + h - 0.038, rule["tag"],
            fontsize=12, fontweight="bold", color="white",
            ha="center", va="center", alpha=0.95)

    ax.text(cx, y + h - 0.125, rule["kind"],
            fontsize=19, fontweight="bold", color=color,
            ha="center", va="center")
    ax.text(cx, y + h - 0.165, rule["subkind"],
            fontsize=12, color=SUBINK, ha="center", va="center", style="italic")

    ax.text(cx, y + h - 0.235, "USE",
            fontsize=12, fontweight="bold", color="#888",
            ha="center", va="center")
    ax.text(cx, y + h - 0.295, rule["verdict"],
            fontsize=22, fontweight="bold", color=DARK_ON_TINT,
            ha="center", va="center")

    ax.text(cx, y + 0.025, rule["support"],
            fontsize=13, color=INK, ha="center", va="bottom",
            linespacing=1.4)


def draw_zone_pill(ax, x, y, w, h, zone, n, model, state, cov, color):
    body = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.012",
        linewidth=1.0, edgecolor=color, facecolor=color, alpha=0.10,
    )
    ax.add_patch(body)
    band = Rectangle((x, y + h - 0.060), w, 0.060, facecolor=color, alpha=0.92)
    ax.add_patch(band)
    cx = x + w / 2
    ax.text(cx, y + h - 0.030, f"{zone.upper()}   (n={n})",
            fontsize=19, fontweight="bold", color="white", ha="center", va="center")

    ax.text(cx, y + h - 0.115, model,
            fontsize=24, fontweight="bold", color=DARK_ON_TINT,
            ha="center", va="center")
    ax.text(cx, y + h - 0.160, state,
            fontsize=17, color=DARK_ON_TINT, ha="center", va="center", style="italic")
    ax.text(cx, y + 0.030, f"{cov}%",
            fontsize=46, fontweight="bold", color=color,
            ha="center", va="center")


def main():
    fig = plt.figure(figsize=(15.0, 10.0), dpi=160)
    fig.patch.set_facecolor("white")
    ax = fig.add_axes([0.03, 0.02, 0.94, 0.78])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.03, 0.955,
             "Which Claude should you use? Pick by the kind of Wardley map you're drawing.",
             fontsize=28, fontweight="bold", color=INK)
    fig.text(0.03, 0.905,
             "ai-trust pilot — model recommendations above, per-zone evidence below. "
             "Colour = evolution stage.",
             fontsize=17, color=SUBINK)

    # Step labels
    ax.text(0.005, 0.985,
            "STEP 1 — What kind of landscape is the map about?",
            fontsize=15, fontweight="bold", color="#888",
            ha="left", va="top", transform=ax.transAxes)

    # ----- Top: three decision rules -----
    n = len(RULES)
    card_w = 0.30
    card_h = 0.50
    gap = (1.0 - n * card_w) / (n + 1)
    y_top_card = 0.94 - card_h
    for i, rule in enumerate(RULES):
        x = gap + i * (card_w + gap)
        draw_rule_card(ax, x, y_top_card, card_w, card_h, rule)

    # ----- Divider -----
    div_y = 0.395
    ax.plot([0.005, 0.995], [div_y, div_y], color="#ddd", lw=1.0)
    ax.text(0.005, div_y - 0.02,
            "STEP 2 — Want to dial it in per zone? Here's who wins each band of the output map.",
            fontsize=15, fontweight="bold", color="#888", ha="left", va="top")

    # ----- Bottom: per-zone evidence strip -----
    nz = len(ZONES)
    z_w = 0.225
    z_gap = (1.0 - nz * z_w) / (nz + 1)
    z_y = 0.05
    z_h = 0.30
    for i, (zone, count, model, state, cov, color) in enumerate(ZONES):
        x = z_gap + i * (z_w + z_gap)
        draw_zone_pill(ax, x, z_y, z_w, z_h, zone, count, model, state, cov, color)

    # Evolution-axis cue
    arrow_y = 0.015
    ax.annotate("", xy=(0.995, arrow_y), xytext=(0.005, arrow_y),
                arrowprops=dict(arrowstyle="-|>", color="#aaa",
                                lw=1.2, mutation_scale=14))
    ax.text(0.0, arrow_y + 0.011, "less evolved", fontsize=12,
            color="#888", ha="left", va="bottom", style="italic")
    ax.text(1.0, arrow_y + 0.011, "more evolved", fontsize=12,
            color="#888", ha="right", va="bottom", style="italic")

    plt.savefig(OUT, bbox_inches="tight", facecolor="white")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
