"""Compose final card face designs at 64×89mm (300 DPI).

Takes the Bria-generated symbol icons and places them into proper card layouts
following CARD_LAYOUT.md:
  - Orientation marker (top-edge bar)
  - Index pip (top-left corner)
  - Large centred symbol icon (Bria-generated)
  - Sign name (bottom-centre)
  - Coloured border frame with background tint
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# --- Dimensions ---
DPI = 300
CARD_W_MM, CARD_H_MM = 64, 89
MM_TO_PX = DPI / 25.4
CARD_W = round(CARD_W_MM * MM_TO_PX)   # 756 px
CARD_H = round(CARD_H_MM * MM_TO_PX)   # 1051 px


def mm(val):
    return round(val * MM_TO_PX)


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

# Rich colour palette per symbol
COLORS = {
    1: (30, 30, 60),       # deep indigo (Void)
    2: (90, 60, 30),       # dark wood brown (Root)
    3: (0, 100, 170),      # deep ocean blue (Wave)
    4: (190, 30, 30),      # rich red (Flame)
    5: (0, 130, 120),      # deep teal (Eye)
    6: (85, 60, 130),      # rich violet (Mask)
    7: (170, 140, 30),     # antique gold (Key)
    8: (160, 20, 140),     # deep magenta (Star)
    9: (180, 150, 30),     # royal gold (Crown)
}

# Light background tints
BG_TINTS = {
    1: (230, 230, 245),
    2: (242, 235, 225),
    3: (225, 238, 250),
    4: (250, 230, 230),
    5: (225, 245, 242),
    6: (238, 230, 248),
    7: (250, 245, 225),
    8: (248, 228, 244),
    9: (250, 246, 225),
}

PAPER = (252, 250, 244)


def get_font(size, bold=False):
    """Load a font, trying several options."""
    if bold:
        candidates = [
            "C:/Windows/Fonts/georgiab.ttf",
            "C:/Windows/Fonts/arialbd.ttf",
            "C:/Windows/Fonts/calibrib.ttf",
        ]
    else:
        candidates = [
            "C:/Windows/Fonts/georgia.ttf",
            "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/calibri.ttf",
        ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def compose_card(sym, icon_path):
    """Create a complete card face with the Bria icon centred."""
    color = COLORS[sym]
    bg_tint = BG_TINTS[sym]
    name = SIGNS[sym]

    # Create card canvas
    card = Image.new("RGB", (CARD_W, CARD_H), PAPER)
    draw = ImageDraw.Draw(card)

    frame_inset = mm(3.5)
    corner_r = mm(3)

    # Background tint fill
    draw.rounded_rectangle(
        [frame_inset, frame_inset, CARD_W - frame_inset, CARD_H - frame_inset],
        radius=corner_r,
        fill=bg_tint,
    )

    # Border frame
    frame_lw = mm(1.2)
    draw.rounded_rectangle(
        [frame_inset, frame_inset, CARD_W - frame_inset, CARD_H - frame_inset],
        radius=corner_r,
        outline=color,
        width=round(frame_lw),
    )

    # Inner decorative line (thinner, slightly inset)
    inner_inset = frame_inset + mm(2)
    draw.rounded_rectangle(
        [inner_inset, inner_inset, CARD_W - inner_inset, CARD_H - inner_inset],
        radius=corner_r - 2,
        outline=color + (80,),  # won't work on RGB, use lighter
        width=max(mm(0.4), 1),
    )
    # Redraw with a lighter version of the colour
    lighter = tuple(min(255, c + 100) for c in color)
    draw.rounded_rectangle(
        [inner_inset, inner_inset, CARD_W - inner_inset, CARD_H - inner_inset],
        radius=corner_r - 2,
        outline=lighter,
        width=max(mm(0.4), 1),
    )

    # Orientation marker — top bar
    bar_h = mm(2.2)
    bar_margin_x = mm(8)
    bar_y = frame_inset + mm(2.5)
    draw.rounded_rectangle(
        [bar_margin_x, bar_y, CARD_W - bar_margin_x, bar_y + bar_h],
        radius=mm(1),
        fill=color,
    )

    # Index pip — top-left corner, large and bold (single, non-mirrored; F2)
    pip_font = get_font(mm(7), bold=True)
    pip_text = str(sym)
    bbox = draw.textbbox((0, 0), pip_text, font=pip_font)
    pip_tw = bbox[2] - bbox[0]
    pip_th = bbox[3] - bbox[1]
    pip_x = frame_inset + mm(3)
    pip_y = bar_y + bar_h + mm(2)
    draw.text((pip_x, pip_y), pip_text, fill=color, font=pip_font)

    # Load and place the Bria icon
    icon = Image.open(icon_path).convert("RGBA")

    # Calculate icon placement area (between pip and name)
    icon_area_top = pip_y + pip_th + mm(4)
    icon_area_bottom = CARD_H - frame_inset - mm(14)
    icon_area_height = icon_area_bottom - icon_area_top
    icon_area_width = CARD_W - 2 * (frame_inset + mm(5))

    # Resize icon to fit, maintaining aspect ratio
    icon_w, icon_h = icon.size
    scale = min(icon_area_width / icon_w, icon_area_height / icon_h) * 0.88
    new_w = round(icon_w * scale)
    new_h = round(icon_h * scale)
    icon_resized = icon.resize((new_w, new_h), Image.LANCZOS)

    # Centre the icon in the available area
    icon_x = (CARD_W - new_w) // 2
    icon_y = icon_area_top + (icon_area_height - new_h) // 2

    # Paste with alpha compositing
    card.paste(icon_resized, (icon_x, icon_y), icon_resized)

    # Sign name — bottom-centre
    name_font = get_font(mm(3.8), bold=False)
    bbox = draw.textbbox((0, 0), name.upper(), font=name_font)
    name_tw = bbox[2] - bbox[0]
    name_y = CARD_H - frame_inset - mm(9)
    # Redraw on the pasted image
    draw = ImageDraw.Draw(card)
    draw.text(
        ((CARD_W - name_tw) // 2, name_y),
        name.upper(),
        fill=color,
        font=name_font,
    )

    # Small decorative dots flanking the name
    dot_r = mm(0.8)
    dot_y_c = name_y + (bbox[3] - bbox[1]) // 2
    draw.ellipse(
        [(CARD_W - name_tw) // 2 - mm(4) - dot_r, dot_y_c - dot_r,
         (CARD_W - name_tw) // 2 - mm(4) + dot_r, dot_y_c + dot_r],
        fill=color,
    )
    draw.ellipse(
        [(CARD_W + name_tw) // 2 + mm(4) - dot_r, dot_y_c - dot_r,
         (CARD_W + name_tw) // 2 + mm(4) + dot_r, dot_y_c + dot_r],
        fill=color,
    )

    return card


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Composing 9 card faces at {CARD_W}×{CARD_H} px ({CARD_W_MM}×{CARD_H_MM} mm @ {DPI} DPI)\n")

    for sym in range(1, 10):
        name = SIGNS[sym]
        icon_file = f"bria_{sym:02d}_{name.lower()}.png"
        icon_path = os.path.join(script_dir, icon_file)

        if not os.path.exists(icon_path):
            print(f"  [{sym}] ✗ Missing icon: {icon_file}")
            continue

        card = compose_card(sym, icon_path)
        out_file = f"card_{sym:02d}_{name.lower()}_final.png"
        out_path = os.path.join(script_dir, out_file)
        card.save(out_path, dpi=(DPI, DPI))
        print(f"  [{sym}] ✓ {out_file}")

    print(f"\nDone — 9 final card designs saved to {script_dir}")


if __name__ == "__main__":
    main()
