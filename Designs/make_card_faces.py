"""Generate 9 card-face designs (one per symbol) at 64×89mm, 300 DPI.

Follows CARD_LAYOUT.md:
  - Orientation marker (top-edge bar)
  - Index pip (top-centre)
  - Large centred symbol icon
  - Sign name (bottom-centre)
  - Coloured border frame

Uses the Nine Signs set (deck-structure.md / SYMBOL_SETS.md §7):
  1 Void · 2 Root · 3 Wave · 4 Flame · 5 Eye · 6 Mask · 7 Key · 8 Star · 9 Crown

Output: individual PNG files in the Designs/ folder, one per symbol.
"""

import math
from PIL import Image, ImageDraw, ImageFont

# --- Dimensions ---
DPI = 300
CARD_W_MM, CARD_H_MM = 64, 89
MM_TO_PX = DPI / 25.4
CARD_W = round(CARD_W_MM * MM_TO_PX)  # 756 px
CARD_H = round(CARD_H_MM * MM_TO_PX)  # 1051 px

# --- Nine Signs ---
SIGNS = {
    1: "Void",
    2: "Root",
    3: "Wave",
    4: "Flame",
    5: "Eye",
    6: "Mask",
    7: "Key",
    8: "Star",
    9: "Crown",
}

# Colour palette — distinct, high-contrast, colour-blind-considered
COLORS = {
    1: (30, 30, 50),       # deep indigo-black (Void)
    2: (101, 67, 33),      # dark brown (Root)
    3: (0, 119, 182),      # ocean blue (Wave)
    4: (214, 40, 40),      # red (Flame)
    5: (42, 157, 143),     # teal (Eye)
    6: (94, 84, 142),      # violet (Mask)
    7: (196, 164, 52),     # gold (Key)
    8: (181, 23, 158),     # magenta (Star)
    9: (212, 175, 55),     # rich gold (Crown)
}

# Background tints (very light wash of the symbol colour)
BG_TINTS = {
    1: (235, 235, 245),
    2: (245, 238, 228),
    3: (228, 242, 252),
    4: (252, 235, 235),
    5: (228, 248, 245),
    6: (240, 235, 248),
    7: (252, 248, 228),
    8: (248, 228, 245),
    9: (252, 248, 232),
}

PAPER = (252, 250, 244)
WHITE = (255, 255, 255)
DARK = (34, 34, 34)


def mm(val):
    """Convert mm to pixels."""
    return round(val * MM_TO_PX)


def get_font(size, bold=False):
    """Try to load a good font, fall back to default."""
    names = (
        ["arialbd.ttf", "Arial Bold.ttf", "calibrib.ttf"] if bold
        else ["arial.ttf", "Arial.ttf", "calibri.ttf"]
    )
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except (OSError, IOError):
            continue
    # Last resort
    try:
        return ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf", size)
    except (OSError, IOError):
        return ImageFont.load_default()


# --- Icon drawing functions ---

def draw_void(draw, cx, cy, r, color):
    """Void: a ring (hollow circle) — emptiness, the outsider."""
    lw = max(r // 6, 4)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=lw)
    # Inner dot
    dot_r = r // 5
    draw.ellipse([cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r], fill=color)


def draw_root(draw, cx, cy, r, color):
    """Root: a tree/root shape — grounded, connected."""
    # Trunk
    tw = r // 4
    draw.rectangle([cx - tw // 2, cy - r // 3, cx + tw // 2, cy + r], fill=color)
    # Branches (upward V)
    pts_left = [(cx, cy - r // 3), (cx - r, cy - r)]
    pts_right = [(cx, cy - r // 3), (cx + r, cy - r)]
    lw = max(tw // 2, 3)
    draw.line(pts_left, fill=color, width=lw)
    draw.line(pts_right, fill=color, width=lw)
    # Roots (downward spread)
    draw.line([(cx, cy + r), (cx - r * 2 // 3, cy + r + r // 2)], fill=color, width=lw)
    draw.line([(cx, cy + r), (cx + r * 2 // 3, cy + r + r // 2)], fill=color, width=lw)
    draw.line([(cx, cy + r), (cx, cy + r + r // 2)], fill=color, width=lw)


def draw_wave(draw, cx, cy, r, color):
    """Wave: three stacked wave curves — flow, movement."""
    lw = max(r // 7, 4)
    for offset in [-r // 2, 0, r // 2]:
        points = []
        for i in range(50):
            x = cx - r + (2 * r * i / 49)
            y = cy + offset + math.sin(i / 49 * 2 * math.pi) * (r // 4)
            points.append((x, y))
        draw.line(points, fill=color, width=lw)


def draw_flame(draw, cx, cy, r, color):
    """Flame: a teardrop/flame shape — energy, destruction."""
    # Outer flame (teardrop polygon)
    pts = []
    for i in range(60):
        angle = 2 * math.pi * i / 60
        # Teardrop shape: r * (1 - cos(t)) modified
        if angle < math.pi:
            rx = r * 0.7 * math.sin(angle)
            ry = -r * (1 - 0.3 * math.cos(angle))
        else:
            rx = r * 0.7 * math.sin(angle)
            ry = -r * (1 - 0.3 * math.cos(angle))
        pts.append((cx + rx, cy - ry * 0.6 + r * 0.2))
    draw.polygon(pts, fill=color)
    # Inner lighter core
    inner_r = r // 3
    inner_pts = []
    for i in range(40):
        angle = 2 * math.pi * i / 40
        if angle < math.pi:
            rx = inner_r * 0.6 * math.sin(angle)
            ry = -inner_r * (1 - 0.3 * math.cos(angle))
        else:
            rx = inner_r * 0.6 * math.sin(angle)
            ry = -inner_r * (1 - 0.3 * math.cos(angle))
        inner_pts.append((cx + rx, cy - ry * 0.5))
    orange = (255, 140, 0)
    draw.polygon(inner_pts, fill=orange)


def draw_eye(draw, cx, cy, r, color):
    """Eye: an eye shape — seeing, knowledge, surveillance."""
    # Almond/eye outline
    pts_top = []
    pts_bottom = []
    for i in range(50):
        t = i / 49
        x = cx - r + 2 * r * t
        # Parabolic arcs
        y_top = cy - r * 0.5 * math.sin(math.pi * t)
        y_bot = cy + r * 0.5 * math.sin(math.pi * t)
        pts_top.append((x, y_top))
        pts_bottom.append((x, y_bot))
    # Fill eye shape
    eye_pts = pts_top + list(reversed(pts_bottom))
    draw.polygon(eye_pts, fill=color)
    # White of the eye
    white_r = r * 0.35
    draw.ellipse([cx - white_r, cy - white_r, cx + white_r, cy + white_r], fill=WHITE)
    # Pupil
    pupil_r = r * 0.18
    draw.ellipse([cx - pupil_r, cy - pupil_r, cx + pupil_r, cy + pupil_r], fill=DARK)


def draw_mask(draw, cx, cy, r, color):
    """Mask: a theatrical mask shape — disguise, deception."""
    # Mask outline (rounded rectangle-ish with pointed chin)
    mask_w = r * 0.85
    mask_h = r * 1.1
    # Top dome
    draw.ellipse([cx - mask_w, cy - mask_h, cx + mask_w, cy + mask_h * 0.3], fill=color)
    # Bottom pointed chin
    chin_pts = [(cx - mask_w * 0.6, cy + mask_h * 0.1),
                (cx, cy + mask_h),
                (cx + mask_w * 0.6, cy + mask_h * 0.1)]
    draw.polygon(chin_pts, fill=color)
    # Eye holes
    eye_w = r * 0.28
    eye_h = r * 0.18
    for dx in [-r * 0.35, r * 0.35]:
        draw.ellipse([cx + dx - eye_w, cy - r * 0.2 - eye_h,
                      cx + dx + eye_w, cy - r * 0.2 + eye_h], fill=PAPER)


def draw_key(draw, cx, cy, r, color):
    """Key: a classic key silhouette — access, unlocking, extraction."""
    # Bow (circular top)
    bow_r = r * 0.35
    bow_cy = cy - r * 0.5
    draw.ellipse([cx - bow_r, bow_cy - bow_r, cx + bow_r, bow_cy + bow_r], fill=color)
    # Inner hole in bow
    hole_r = bow_r * 0.4
    draw.ellipse([cx - hole_r, bow_cy - hole_r, cx + hole_r, bow_cy + hole_r], fill=PAPER)
    # Shaft
    shaft_w = r * 0.12
    shaft_top = bow_cy + bow_r * 0.5
    shaft_bottom = cy + r * 0.9
    draw.rectangle([cx - shaft_w, shaft_top, cx + shaft_w, shaft_bottom], fill=color)
    # Teeth (two notches on the right)
    tooth_w = r * 0.25
    tooth_h = r * 0.12
    for ty in [shaft_bottom - r * 0.3, shaft_bottom - r * 0.1]:
        draw.rectangle([cx + shaft_w, ty, cx + shaft_w + tooth_w, ty + tooth_h], fill=color)


def draw_star(draw, cx, cy, r, color):
    """Star: an 8-pointed star — the wild, the special."""
    pts = []
    for i in range(16):
        angle = math.radians(-90 + 360 * i / 16)
        rad = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rad * math.cos(angle), cy + rad * math.sin(angle)))
    draw.polygon(pts, fill=color)


def draw_crown(draw, cx, cy, r, color):
    """Crown: a crown silhouette — the apex, the greatest."""
    # Base band
    base_top = cy + r * 0.3
    base_bot = cy + r * 0.7
    draw.rectangle([cx - r * 0.8, base_top, cx + r * 0.8, base_bot], fill=color)
    # Five-point top
    crown_pts = [
        (cx - r * 0.8, base_top),
        (cx - r * 0.8, cy - r * 0.3),
        (cx - r * 0.4, cy),
        (cx - r * 0.15, cy - r * 0.8),
        (cx, cy - r * 0.2),
        (cx + r * 0.15, cy - r * 0.8),
        (cx + r * 0.4, cy),
        (cx + r * 0.8, cy - r * 0.3),
        (cx + r * 0.8, base_top),
    ]
    draw.polygon(crown_pts, fill=color)
    # Jewels (small dots on the points)
    jewel_r = r * 0.06
    for jx, jy in [(cx - r * 0.15, cy - r * 0.8), (cx, cy - r * 0.2), (cx + r * 0.15, cy - r * 0.8)]:
        draw.ellipse([jx - jewel_r, jy - jewel_r, jx + jewel_r, jy + jewel_r], fill=WHITE)


ICON_DRAWERS = {
    1: draw_void,
    2: draw_root,
    3: draw_wave,
    4: draw_flame,
    5: draw_eye,
    6: draw_mask,
    7: draw_key,
    8: draw_star,
    9: draw_crown,
}


def draw_card_face(sym):
    """Create one card face image for the given symbol (1-9)."""
    img = Image.new("RGB", (CARD_W, CARD_H), PAPER)
    draw = ImageDraw.Draw(img)

    color = COLORS[sym]
    bg_tint = BG_TINTS[sym]
    name = SIGNS[sym]

    # Background tint fill (inside the frame)
    frame_inset = mm(4)
    draw.rounded_rectangle(
        [frame_inset, frame_inset, CARD_W - frame_inset, CARD_H - frame_inset],
        radius=mm(3),
        fill=bg_tint,
    )

    # Border frame
    frame_lw = max(mm(0.8), 2)
    draw.rounded_rectangle(
        [frame_inset, frame_inset, CARD_W - frame_inset, CARD_H - frame_inset],
        radius=mm(3),
        outline=color,
        width=frame_lw,
    )

    # Orientation marker — top bar
    bar_h = mm(2.5)
    bar_margin = mm(6)
    draw.rounded_rectangle(
        [bar_margin, frame_inset + mm(1.5), CARD_W - bar_margin, frame_inset + mm(1.5) + bar_h],
        radius=mm(1),
        fill=color,
    )

    # Index pip — top-centre
    pip_font = get_font(mm(6), bold=True)
    pip_text = str(sym)
    pip_y = frame_inset + mm(5)
    bbox = draw.textbbox((0, 0), pip_text, font=pip_font)
    pip_tw = bbox[2] - bbox[0]
    pip_th = bbox[3] - bbox[1]
    draw.text(
        ((CARD_W - pip_tw) // 2, pip_y),
        pip_text,
        fill=color,
        font=pip_font,
    )

    # Symbol icon — centred, large
    icon_cx = CARD_W // 2
    icon_cy = CARD_H // 2 - mm(2)  # slightly above true centre (name below)
    icon_r = mm(18)
    ICON_DRAWERS[sym](draw, icon_cx, icon_cy, icon_r, color)

    # Sign name — bottom-centre
    name_font = get_font(mm(4), bold=False)
    bbox = draw.textbbox((0, 0), name, font=name_font)
    name_tw = bbox[2] - bbox[0]
    name_y = CARD_H - frame_inset - mm(8)
    draw.text(
        ((CARD_W - name_tw) // 2, name_y),
        name,
        fill=color,
        font=name_font,
    )

    return img


def main():
    import os
    out_dir = os.path.dirname(os.path.abspath(__file__))
    for sym in range(1, 10):
        img = draw_card_face(sym)
        filename = f"card_face_{sym:02d}_{SIGNS[sym].lower()}.png"
        path = os.path.join(out_dir, filename)
        img.save(path, dpi=(DPI, DPI))
        print(f"  ✓ {filename} ({CARD_W}×{CARD_H} px, {CARD_W_MM}×{CARD_H_MM} mm @ {DPI} DPI)")
    print(f"\nDone — 9 card faces saved to {out_dir}")


if __name__ == "__main__":
    main()
