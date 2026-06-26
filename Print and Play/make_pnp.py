"""Print-and-play generator for the 36-card flip-deck master prototype.

THE NINE SIGNS (SYMBOL_SET.md): 1 Moon, 2 Leaf, 3 Wave, 4 Flame, 5 Eye,
6 Mask, 7 Key, 8 Star, 9 Crown. Glyphs from Designs/Brand Kit/glyphs.svg,
hues from SYMBOL_SET.md.

Card layout per Designs/CARD_LAYOUT.md (June 2026):
  - large centred sign glyph (primary identity)
  - single top-left corner pip (authoritative rank 1-9)
  - sign name, small, bottom-centre
  - top-edge orientation marker (neutral chevron), IDENTICAL on every face

H3 (physical-handling.md): the only structural elements (frame, orientation
marker) are neutral and identical on every face, so nothing differs between a
card's two faces or correlates with the hidden face. The pip/glyph/name describe
only the face they sit on.

Output: A4, page 1 = legend/instructions (print single-sided),
pages 2-9 = four duplex sheet pairs (long-edge flip), 3x3 poker cards each.
"""

import itertools
import os
import tempfile
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg

PAGE_W, PAGE_H = A4
CARD_W, CARD_H = 63.5 * mm, 88 * mm
COLS = ROWS = 3
MARGIN_X = (PAGE_W - COLS * CARD_W) / 2
MARGIN_Y = (PAGE_H - ROWS * CARD_H) / 2

SIGNS = list(range(1, 10))
PAIRS = [tuple(p) for p in itertools.combinations(SIGNS, 2)]  # 36

NAMES = {1: "Moon", 2: "Leaf", 3: "Wave", 4: "Flame", 5: "Eye",
         6: "Mask", 7: "Key", 8: "Star", 9: "Crown"}

COLORS = {
    1: "#2E2C5F",  # Moon  - indigo
    2: "#3E7A3E",  # Leaf  - green
    3: "#1577B5",  # Wave  - blue
    4: "#D83A22",  # Flame - red
    5: "#169488",  # Eye   - teal
    6: "#A6328C",  # Mask  - magenta
    7: "#B98A2A",  # Key   - gold
    8: "#E0A91F",  # Star  - amber
    9: "#5E3A9E",  # Crown - violet
}

# Glyph path bodies (viewBox 0 0 100 100), ported from Brand Kit/glyphs.svg.
GLYPHS = {
    1: '<path fill-rule="evenodd" d="M50 50 m-36 0 a36 36 0 1 0 72 0 a36 36 0 1 0 -72 0 Z M58 50 m-28 0 a28 28 0 1 0 56 0 a28 28 0 1 0 -56 0 Z" fill="{c}"/>',
    2: '<path d="M50 12 C70 30 70 56 50 80 C30 56 30 30 50 12 Z" fill="{c}"/><rect x="48" y="76" width="4" height="12" rx="2" fill="{c}"/>',
    3: '<path d="M14 56 Q32 32 50 56 T86 56" fill="none" stroke="{c}" stroke-width="11" stroke-linecap="round"/>',
    4: '<path fill-rule="evenodd" d="M54 6 C48 30 30 36 30 60 C30 78 42 94 54 94 C69 94 77 78 71 60 C67 48 56 50 59 35 C61 26 58 16 54 6 Z M53 52 C51 61 45 65 45 73 C45 81 49 85 54 85 C60 85 63 79 61 72 C59 64 55 63 53 52 Z" fill="{c}"/>',
    5: '<path d="M12 50 Q50 18 88 50 Q50 82 12 50 Z" fill="none" stroke="{c}" stroke-width="9"/><circle cx="50" cy="50" r="12" fill="{c}"/>',
    6: '<path fill-rule="evenodd" d="M14 40 C24 30 40 30 50 37 C60 30 76 30 86 40 C88 53 79 63 65 64 C57 65 52 59 50 53 C48 59 43 65 35 64 C21 63 12 53 14 40 Z M33 47 m-9 0 a9 6 0 1 0 18 0 a9 6 0 1 0 -18 0 Z M67 47 m-9 0 a9 6 0 1 0 18 0 a9 6 0 1 0 -18 0 Z" fill="{c}"/>',
    7: '<circle cx="50" cy="30" r="16" fill="none" stroke="{c}" stroke-width="10"/><rect x="45" y="44" width="10" height="42" fill="{c}"/><rect x="55" y="66" width="15" height="9" fill="{c}"/>',
    8: '<path d="M50 14 L61 39 L88 42 L67 60 L74 87 L50 72 L26 87 L33 60 L12 42 L39 39 Z" fill="{c}"/>',
    9: '<path d="M18 74 L18 38 L35 53 L50 30 L65 53 L82 38 L82 74 Z" fill="{c}"/>',
}

PAPER = HexColor("#FCFAF4")
INK = HexColor("#222222")
FRAME = HexColor("#D8D2C4")     # neutral hairline frame (cut/drift guide)
MARKER = HexColor("#9A9486")    # neutral orientation marker

_GLYPH_CACHE = {}
_TMPDIR = tempfile.mkdtemp(prefix="glyphs_")


def glyph_drawing(sign):
    """Return a cached reportlab Drawing for a sign glyph, coloured by hue."""
    if sign in _GLYPH_CACHE:
        return _GLYPH_CACHE[sign]
    body = GLYPHS[sign].format(c=COLORS[sign])
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" '
           f'viewBox="0 0 100 100" width="100" height="100">{body}</svg>')
    path = os.path.join(_TMPDIR, f"sign{sign}.svg")
    with open(path, "w") as f:
        f.write(svg)
    d = svg2rlg(path)
    _GLYPH_CACHE[sign] = d
    return d


_MASSX_CACHE = {}


def mass_centroid_x(sign):
    """Horizontal centre of the glyph's actual ink (drawing units).

    Differs from the bounding-box centre for mass-asymmetric glyphs (e.g. the
    Moon crescent leans left of its box). Centring on this makes such signs
    look optically centred. Symmetric glyphs are unaffected (mass == box).
    """
    if sign in _MASSX_CACHE:
        return _MASSX_CACHE[sign]
    import numpy as np
    d = glyph_drawing(sign)
    dpi = 288
    img = renderPM.drawToPIL(d, dpi=dpi, bg=0xffffff).convert("L")
    a = np.asarray(img).astype(int)
    xs = np.where(a < 200)[1]
    mcx = (xs.mean() * 72.0 / dpi) if len(xs) else 37.5
    _MASSX_CACHE[sign] = mcx
    return mcx


def draw_glyph(c, sign, cx, cy, target):
    """Draw the sign glyph centred at (cx, cy) fitted to a target box (pts).

    Horizontal: centred on the glyph's visual mass (optical centring), so a
    crescent Moon or off-balance sign reads centred. Vertical: centred on the
    content bounding box. Sized to fit the target box by its larger dimension.
    """
    d = glyph_drawing(sign)
    x0, y0, x1, y1 = d.getBounds()
    cw, ch = x1 - x0, y1 - y0
    s = target / max(cw, ch)
    # Horizontal and vertical: centre on the content bounding box (the implied
    # full shape), so e.g. the Moon's disc sits dead-centre on the card.
    hcx = (x0 + x1) / 2.0
    ccy = (y0 + y1) / 2.0
    c.saveState()
    c.translate(cx - s * hcx, cy - s * ccy)
    c.scale(s, s)
    renderPDF.draw(d, c, 0, 0)
    c.restoreState()


def draw_orientation_marker(c, ox, oy):
    """Neutral up-chevron, top-edge centre. Identical on every face (H3)."""
    cx = ox + CARD_W / 2
    top = oy + CARD_H - 6.5 * mm
    w = 5 * mm
    c.setStrokeColor(MARKER)
    c.setLineWidth(1.4)
    c.setLineCap(1)
    p = c.beginPath()
    p.moveTo(cx - w / 2, top - 1.6 * mm)
    p.lineTo(cx, top + 1.0 * mm)
    p.lineTo(cx + w / 2, top - 1.6 * mm)
    c.drawPath(p, stroke=1, fill=0)


def draw_face(c, sign, ox, oy):
    """One card face at lower-left (ox, oy). Identical template both faces."""
    col = HexColor(COLORS[sign])
    c.setFillColor(PAPER)
    c.rect(ox, oy, CARD_W, CARD_H, stroke=0, fill=1)
    # neutral inner frame, inset to forgive duplex drift
    c.setStrokeColor(FRAME)
    c.setLineWidth(1.0)
    c.roundRect(ox + 4 * mm, oy + 4 * mm, CARD_W - 8 * mm, CARD_H - 8 * mm,
                3 * mm, stroke=1, fill=0)
    draw_orientation_marker(c, ox, oy)
    # large centred glyph
    draw_glyph(c, sign, ox + CARD_W / 2, oy + CARD_H / 2 + 3 * mm, 34 * mm)
    # single top-left corner pip
    c.setFillColor(col)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(ox + 8.5 * mm, oy + CARD_H - 16 * mm, str(sign))
    # sign name, bottom-centre
    c.setFillColor(col)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(ox + CARD_W / 2, oy + 9 * mm, NAMES[sign].upper())


def cell_origin(row, col):
    """row 0 = top row. Returns lower-left of the cell."""
    x = MARGIN_X + col * CARD_W
    y = PAGE_H - MARGIN_Y - (row + 1) * CARD_H
    return x, y


def draw_cut_guides(c):
    c.setStrokeColor(HexColor("#BBBBBB"))
    c.setLineWidth(0.3)
    c.setDash(2, 3)
    for col in range(COLS + 1):
        x = MARGIN_X + col * CARD_W
        c.line(x, PAGE_H - MARGIN_Y + 4 * mm, x, PAGE_H - MARGIN_Y)
        c.line(x, MARGIN_Y, x, MARGIN_Y - 4 * mm)
    for row in range(ROWS + 1):
        y = PAGE_H - MARGIN_Y - row * CARD_H
        c.line(MARGIN_X - 4 * mm, y, MARGIN_X, y)
        c.line(PAGE_W - MARGIN_X, y, PAGE_W - MARGIN_X + 4 * mm, y)
    c.setDash()


def draw_sheet(c, cards, face_idx, mirrored):
    """cards: list of up to 9 pairs. face_idx 0/1. mirrored for backs."""
    draw_cut_guides(c)
    for i, pair in enumerate(cards):
        row, col = divmod(i, COLS)
        if mirrored:
            col = COLS - 1 - col
        ox, oy = cell_origin(row, col)
        draw_face(c, pair[face_idx], ox, oy)
    c.showPage()


def draw_legend(c):
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 26 * mm, "THE FLIP DECK")
    c.setFont("Helvetica", 11)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 33 * mm,
                        "36-card master prototype  ·  the Nine Signs  ·  "
                        "every pair exactly once")
    # glyph legend row
    top = PAGE_H - 56 * mm
    for i, sign in enumerate(SIGNS):
        gx = PAGE_W / 2 + (i - 4) * 19 * mm
        draw_glyph(c, sign, gx, top, 13 * mm)
        c.setFillColor(HexColor(COLORS[sign]))
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(gx, top - 11 * mm, f"{sign} {NAMES[sign]}")
    lines = [
        ("PRINTING", [
            "Print at 100% scale (no “fit to page”) on A4 cardstock.",
            "Page 1 (this page): print single-sided, or skip it.",
            "Pages 2–9: print DOUBLE-SIDED, flip on the LONG edge.",
            "Check duplex alignment against the light; the 4 mm frame",
            "inset forgives a couple of millimetres of drift.",
            "Cut along the dashed guides: 9 cards per sheet, 36 total.",
            "Standard 63.5 × 88 mm sleeves fit. There is no card back —",
            "both sides are faces, so opaque sleeves are wasted here.",
        ]),
        ("THE DECK", [
            "Each card shows one sign on each side; every possible pair of",
            "the nine signs appears on exactly one card (36 = 9×8÷2).",
            "The pip (1–9) is the authoritative rank: Moon 1 (lowest) …",
            "Crown 9 (highest). The sign’s name and picture never override",
            "the number. The top-edge chevron marks “up” and is identical",
            "on every face — nothing reveals a card’s hidden side.",
            "Sub-decks remove from the top: signs 1–6 (15 cards), 1–7",
            "(21) or 1–8 (28) each form an exact smaller all-pairs deck.",
        ]),
        ("SORTING AFTER PLAY", [
            "To verify the deck: lay cards in rows by their lower sign -",
            "row 1 holds 1+2 ... 1+9 (eight cards), row 2 holds 2+3 ... 2+9",
            "(seven), and so on. A missing card names itself.",
        ]),
    ]
    y = top - 26 * mm
    for head, body in lines:
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(INK)
        c.drawString(28 * mm, y, head)
        y -= 6.5 * mm
        c.setFont("Helvetica", 9.5)
        for ln in body:
            c.drawString(28 * mm, y, ln)
            y -= 5 * mm
        y -= 4 * mm
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(PAGE_W / 2, 15 * mm,
                        "Flip-deck project  -  the Nine Signs  -  June 2026  "
                        "-  one deck, eleven games")
    c.showPage()


def main(path):
    c = rl_canvas.Canvas(path, pagesize=A4)
    c.setTitle("Flip Deck - 36-card print-and-play (the Nine Signs)")
    draw_legend(c)
    for s in range(4):
        chunk = PAIRS[s * 9:(s + 1) * 9]
        draw_sheet(c, chunk, 0, mirrored=False)
        draw_sheet(c, chunk, 1, mirrored=True)
    c.save()
    print("wrote", path, "-", len(PAIRS), "cards")


if __name__ == "__main__":
    main("FLIP_DECK_print_and_play.pdf")
