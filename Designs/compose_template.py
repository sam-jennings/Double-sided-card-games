"""Composite the 9 symbol cutouts into a CONSISTENT card template.

Layout per CARD_LAYOUT.md (identical on every card):
  - Orientation marker: fixed neutral top-edge bar (identical both faces, H3-safe)
  - Index pip 1-9: top-centre, in the symbol's colour
  - Symbol icon: centred in a FIXED icon box, scaled by its content bounding box
                 so every symbol appears the same visual size
  - Coloured border frame + light background (colour reflects the VISIBLE symbol)
  - NO sign name text (per request)

Output: 64x89mm @ 300 DPI (756x1051 px).
"""

import os
from PIL import Image, ImageDraw, ImageFont

# --- Dimensions ---
DPI = 300
CARD_W_MM, CARD_H_MM = 64, 89
MM_TO_PX = DPI / 25.4
CARD_W = round(CARD_W_MM * MM_TO_PX)   # 756
CARD_H = round(CARD_H_MM * MM_TO_PX)   # 1051


def mm(v):
    return round(v * MM_TO_PX)


SIGNS = {1: "Void", 2: "Root", 3: "Wave", 4: "Flame", 5: "Eye",
         6: "Mask", 7: "Key", 8: "Star", 9: "Crown"}

# Distinct, thematically relevant colour per symbol (shape is primary identity;
# colour is a secondary cue, spaced around the wheel for max distinctness).
COLORS = {
    1: (63, 71, 165),    # Void  - indigo
    2: (78, 120, 56),    # Root  - earthy green
    3: (0, 140, 190),    # Wave  - ocean blue
    4: (208, 55, 38),    # Flame - red
    5: (0, 142, 128),    # Eye   - teal
    6: (130, 47, 165),   # Mask  - purple
    7: (184, 134, 28),   # Key   - amber/bronze
    8: (235, 184, 30),   # Star  - bright gold-yellow
    9: (151, 36, 122),   # Crown - royal magenta-purple
}

# Light background tint per symbol (very pale wash of its colour)
def bg_tint(color):
    return tuple(round(c * 0.10 + 245 * 0.90) for c in color)

# Fixed neutral colour for the orientation marker — same on EVERY card/face (H3)
ORIENT_COLOR = (43, 45, 66)   # dark slate
PAPER = (250, 248, 242)

# Fixed icon box (same on every card) — content is fitted into this region
ICON_BOX_TOP = mm(22)
ICON_BOX_BOTTOM = CARD_H - mm(14)
ICON_BOX_LEFT = mm(9)
ICON_BOX_RIGHT = CARD_W - mm(9)


def get_font(size, bold=True):
    candidates = (
        ["C:/Windows/Fonts/georgiab.ttf", "C:/Windows/Fonts/arialbd.ttf"]
        if bold else
        ["C:/Windows/Fonts/georgia.ttf", "C:/Windows/Fonts/arial.ttf"]
    )
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def content_bbox(img):
    """Bounding box of non-transparent content in an RGBA image."""
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    alpha = img.split()[3]
    bbox = alpha.getbbox()
    return bbox or (0, 0, img.width, img.height)


def compose(sym, cutout_path):
    color = COLORS[sym]
    card = Image.new("RGB", (CARD_W, CARD_H), PAPER)
    draw = ImageDraw.Draw(card)

    frame_inset = mm(3.5)
    corner_r = mm(3.5)

    # Background tint
    draw.rounded_rectangle(
        [frame_inset, frame_inset, CARD_W - frame_inset, CARD_H - frame_inset],
        radius=corner_r, fill=bg_tint(color))

    # Outer coloured border (reflects visible symbol)
    draw.rounded_rectangle(
        [frame_inset, frame_inset, CARD_W - frame_inset, CARD_H - frame_inset],
        radius=corner_r, outline=color, width=mm(1.3))

    # Inner thin border (lighter)
    lighter = tuple(min(255, c + 90) for c in color)
    inner = frame_inset + mm(2.2)
    draw.rounded_rectangle(
        [inner, inner, CARD_W - inner, CARD_H - inner],
        radius=max(corner_r - mm(1.5), 4), outline=lighter, width=max(mm(0.4), 1))

    # Orientation marker — fixed neutral bar at top edge, centred, with a notch.
    # Identical on every card and every face (H3).
    bar_w = mm(20)
    bar_h = mm(2.4)
    bar_top = frame_inset + mm(2.6)
    bar_x0 = (CARD_W - bar_w) // 2
    draw.rounded_rectangle(
        [bar_x0, bar_top, bar_x0 + bar_w, bar_top + bar_h],
        radius=mm(1.2), fill=ORIENT_COLOR)
    # Centre notch/arrow pointing up, marking "this edge is the top"
    notch_w = mm(3.5)
    notch_h = mm(2.2)
    ncx = CARD_W // 2
    draw.polygon(
        [(ncx - notch_w / 2, bar_top - mm(0.6)),
         (ncx + notch_w / 2, bar_top - mm(0.6)),
         (ncx, bar_top - mm(0.6) - notch_h)],
        fill=ORIENT_COLOR)

    # Index pip — top-centre, in symbol colour, inside a subtle circle
    pip_font = get_font(mm(8), bold=True)
    pip_text = str(sym)
    pip_cy = bar_top + bar_h + mm(7)
    # subtle disc behind the pip
    disc_r = mm(6)
    draw.ellipse([CARD_W // 2 - disc_r, pip_cy - disc_r,
                  CARD_W // 2 + disc_r, pip_cy + disc_r],
                 fill=PAPER, outline=color, width=max(mm(0.5), 1))
    bbox = draw.textbbox((0, 0), pip_text, font=pip_font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((CARD_W // 2 - tw / 2 - bbox[0], pip_cy - th / 2 - bbox[1]),
              pip_text, fill=color, font=pip_font)

    # Symbol icon — fit cutout's content bbox into the fixed icon box, centred.
    icon = Image.open(cutout_path).convert("RGBA")
    bx0, by0, bx1, by1 = content_bbox(icon)
    cropped = icon.crop((bx0, by0, bx1, by1))
    cw, ch = cropped.size

    box_w = ICON_BOX_RIGHT - ICON_BOX_LEFT
    box_h = ICON_BOX_BOTTOM - ICON_BOX_TOP
    scale = min(box_w / cw, box_h / ch) * 0.92
    new_w, new_h = max(1, round(cw * scale)), max(1, round(ch * scale))
    cropped = cropped.resize((new_w, new_h), Image.LANCZOS)

    icon_x = ICON_BOX_LEFT + (box_w - new_w) // 2
    icon_y = ICON_BOX_TOP + (box_h - new_h) // 2
    card.paste(cropped, (icon_x, icon_y), cropped)

    return card


def main():
    d = os.path.dirname(os.path.abspath(__file__))
    print(f"Composing 9 cards into consistent template ({CARD_W}x{CARD_H} px, "
          f"{CARD_W_MM}x{CARD_H_MM}mm @ {DPI} DPI)\n")
    for sym, name in SIGNS.items():
        cutout = os.path.join(d, f"cutout_{sym:02d}_{name.lower()}.png")
        if not os.path.exists(cutout):
            print(f"  [{sym}] MISSING {cutout}")
            continue
        card = compose(sym, cutout)
        out = os.path.join(d, f"card_{sym:02d}_{name.lower()}.png")
        card.save(out, dpi=(DPI, DPI))
        print(f"  [{sym}] {name} -> card_{sym:02d}_{name.lower()}.png")
    print(f"\nDone. 9 consistent card faces saved to {d}")


if __name__ == "__main__":
    main()
