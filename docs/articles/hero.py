"""Render a hero PNG for the Wardley Map skill article.

A stylised Wardley-map visual on dark background, with the band boundaries,
a handful of components and edges to evoke the map shape, and the
benchmark headline numbers along the bottom.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

W, H = 1600, 900
# Claude-inspired palette — cream background, clay/peach accent, near-black text.
# Approximates the colours used on anthropic.com / Claude product surfaces.
BG = (240, 238, 230)             # warm cream  #F0EEE6
GRID = (229, 226, 216)           # faint grid on cream
AXIS = (124, 117, 104)           # warm gray axis
AXIS_LABEL = (58, 58, 58)        # dark charcoal
BAND = (212, 207, 191)           # band divider (warmer, slightly darker than grid)
TITLE = (25, 25, 25)             # near-black  #191919
SUBTITLE = (86, 86, 86)          # medium warm gray
STAT = (217, 119, 87)            # Claude clay/peach  #D97757
ANCHOR = (25, 25, 25)            # anchor as near-black dot
NODE = (217, 119, 87)            # components in clay
NODE_DIM = (191, 104, 73)        # darker clay
EDGE = (207, 201, 190)           # warm gray-beige
LABEL = (58, 58, 58)             # readable dark charcoal

IMG_PATH = "/workspaces/wardleymap_math_model/docs/articles/hero.png"


def load_font(size, bold=False):
    candidates = [
        # common DejaVu paths on Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
            else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf" if bold
            else "/usr/share/fonts/TTF/DejaVuSans.ttf",
    ]
    for c in candidates:
        try:
            return ImageFont.truetype(c, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Define the map canvas: left-side large, right-side reserved for headline
    map_left = 80
    map_top = 120
    map_right = 1020
    map_bottom = 720
    mw = map_right - map_left
    mh = map_bottom - map_top

    # Subtle background grid (every 0.1)
    for i in range(1, 10):
        x = map_left + mw * i / 10
        d.line([(x, map_top), (x, map_bottom)], fill=GRID, width=1)
    for i in range(1, 10):
        y = map_top + mh * i / 10
        d.line([(map_left, y), (map_right, y)], fill=GRID, width=1)

    # Band dividers at ε = 0.25, 0.5, 0.75
    for frac in (0.25, 0.5, 0.75):
        x = map_left + mw * frac
        d.line([(x, map_top), (x, map_bottom)], fill=BAND, width=2)

    # Axis frame
    d.line([(map_left, map_top), (map_left, map_bottom)], fill=AXIS, width=2)
    d.line([(map_left, map_bottom), (map_right, map_bottom)], fill=AXIS, width=2)

    # Axis labels
    small = load_font(22)
    band_font = load_font(20, bold=True)
    # Y-axis (vertical) label "VISIBILITY" rotated
    vis_img = Image.new("RGBA", (300, 36), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vis_img)
    vd.text((0, 0), "VISIBILITY", font=load_font(24, bold=True), fill=AXIS_LABEL)
    vis_img = vis_img.rotate(90, expand=True)
    img.paste(vis_img, (28, map_top + 80), vis_img)

    # X-axis stage labels (two lines each, to fit within band width)
    stage_names = [
        ("GENESIS", ""),
        ("CUSTOM", "BUILT"),
        ("PRODUCT", "(+rental)"),
        ("COMMODITY", "(+utility)"),
    ]
    for i, (line1, line2) in enumerate(stage_names):
        cx = map_left + mw * (i + 0.5) / 4
        d.text((cx, map_bottom + 10), line1, font=band_font, fill=AXIS_LABEL, anchor="mt")
        if line2:
            d.text((cx, map_bottom + 34), line2, font=band_font, fill=AXIS_LABEL, anchor="mt")

    d.text((map_left + mw / 2, map_bottom + 78), "EVOLUTION",
           font=load_font(22, bold=True), fill=AXIS_LABEL, anchor="mt")

    # Plot components. (ν, ε, label, is_anchor)
    # Positions picked to look like a legit Wardley map, not a precision statement.
    nodes = [
        (0.95, 0.40, "User Need", True),
        (0.80, 0.45, "Product", False),
        (0.70, 0.58, "Recommendation", False),
        (0.68, 0.28, "Onboarding Flow", False),
        (0.55, 0.67, "Search", False),
        (0.50, 0.35, "Fraud Detection", False),
        (0.42, 0.55, "Identity", False),
        (0.35, 0.72, "Payments", False),
        (0.28, 0.80, "Data Pipeline", False),
        (0.20, 0.88, "Cloud Compute", False),
        (0.12, 0.93, "Networking", False),
    ]

    def to_px(v, e):
        # v: 0 at bottom, 1 at top
        x = map_left + mw * e
        y = map_bottom - mh * v
        return x, y

    # Edges (src → dst by index)
    edges = [
        (0, 1), (0, 3),
        (1, 2), (1, 4), (1, 5),
        (2, 6), (2, 8),
        (3, 5), (3, 6),
        (4, 6), (4, 8),
        (5, 6), (5, 8),
        (6, 7), (6, 9),
        (7, 9), (7, 8),
        (8, 9), (8, 10),
        (9, 10),
    ]
    for a, b in edges:
        x1, y1 = to_px(nodes[a][0], nodes[a][1])
        x2, y2 = to_px(nodes[b][0], nodes[b][1])
        d.line([(x1, y1), (x2, y2)], fill=EDGE, width=2)

    # Draw nodes
    node_font = load_font(18)
    for v, e, lbl, is_anchor in nodes:
        x, y = to_px(v, e)
        r = 10 if is_anchor else 7
        colour = ANCHOR if is_anchor else NODE
        d.ellipse([(x - r, y - r), (x + r, y + r)], fill=colour, outline=BG, width=2)
        # Label placement: offset right by default
        lx, ly = x + r + 8, y - 10
        # keep labels inside map where possible
        if lx + 200 > map_right:
            lx = x - r - 8 - 180
        d.text((lx, ly), lbl, font=node_font, fill=LABEL)

    # Right panel: headline, subtitle, benchmark stats
    panel_left = map_right + 60
    title_font = load_font(48, bold=True)
    subtitle_font = load_font(22)
    kicker_font = load_font(18, bold=True)
    stat_num_font = load_font(54, bold=True)
    stat_lbl_font = load_font(18)

    d.text((panel_left, map_top - 8), "BENCHMARK REPORT",
           font=kicker_font, fill=STAT)
    d.text((panel_left, map_top + 22), "A Wardley-Map",
           font=title_font, fill=TITLE)
    d.text((panel_left, map_top + 80), "skill,",
           font=title_font, fill=TITLE)
    d.text((panel_left, map_top + 138), "benchmarked.",
           font=title_font, fill=TITLE)

    d.text((panel_left, map_top + 215),
           "Blind test, 25 of Wardley's\nown maps, 18 domains.",
           font=subtitle_font, fill=SUBTITLE)

    # Stats block
    stats = [
        ("61%", "within strategic tolerance"),
        ("92%", "in Wardley's band or adjacent"),
        ("37%", "strict same-band match"),
        ("25/25", "validator-clean on ship"),
    ]
    sy = map_top + 310
    for num, lbl in stats:
        d.text((panel_left, sy), num, font=stat_num_font, fill=STAT)
        bbox = d.textbbox((panel_left, sy), num, font=stat_num_font)
        d.text((bbox[2] + 18, sy + 18), lbl, font=stat_lbl_font, fill=SUBTITLE)
        sy += 68

    # Footer strip: attribution
    foot_font = load_font(18)
    d.text((80, H - 42),
           "tractorjuice/wardleymap_math_model · skills/wardley-map · BENCHMARK-REPORT.md",
           font=foot_font, fill=(140, 134, 122))

    Path(IMG_PATH).parent.mkdir(parents=True, exist_ok=True)
    img.save(IMG_PATH, "PNG", optimize=True)
    print(f"wrote {IMG_PATH}")


if __name__ == "__main__":
    main()
