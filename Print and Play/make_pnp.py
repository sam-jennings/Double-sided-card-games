"""Print-and-play generator for the 36-card flip-deck master prototype.

Set D 'Glyphs' skin (SYMBOL_SETS.md): shape IS rank — Dot, Bar, Triangle,
Square, Pentagon, Hexagon, Heptagram, Octagon, Nonagram. Pips 1-9 in two
corners of BOTH faces, identical placement, no asymmetric marks
(standing project rule: nothing on a card may reveal which face you see).

Output: A4, page 1 = legend/instructions (print single-sided),
pages 2-9 = four duplex sheets (long-edge flip), 3x3 poker cards each.
"""

import itertools
import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfgen import canvas as rl_canvas

PAGE_W, PAGE_H = A4
CARD_W, CARD_H = 63 * mm, 88 * mm
COLS = ROWS = 3
MARGIN_X = (PAGE_W - COLS * CARD_W) / 2
MARGIN_Y = (PAGE_H - ROWS * CARD_H) / 2

SYMBOLS = list(range(1, 10))
PAIRS = [tuple(p) for p in itertools.combinations(SYMBOLS, 2)]  # 36

NAMES = {1: "Dot", 2: "Bar", 3: "Triangle", 4: "Square", 5: "Pentagon",
         6: "Hexagon", 7: "Heptagram", 8: "Octagon", 9: "Nonagram"}

COLORS = {
    1: HexColor("#D62828"),  # red
    2: HexColor("#F77F00"),  # orange
    3: HexColor("#C9A227"),  # gold
    4: HexColor("#2E933C"),  # green
    5: HexColor("#2A9D8F"),  # teal
    6: HexColor("#1D6FB8"),  # blue
    7: HexColor("#5E548E"),  # violet
    8: HexColor("#B5179E"),  # magenta
    9: HexColor("#2B2D42"),  # near-black
}

PAPER = HexColor("#FCFAF4")
INK = HexColor("#222222")


def polygon_pts(cx, cy, r, n, rot=-90):
    return [(cx + r * math.cos(math.radians(rot + 360 * i / n)),
             cy + r * math.sin(math.radians(rot + 360 * i / n)))
            for i in range(n)]


def star_pts(cx, cy, r_out, r_in, n, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + 180 * i / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def draw_path(c, pts, fill_color):
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    p.close()
    c.setFillColor(fill_color)
    c.setStrokeColor(fill_color)
    c.drawPath(p, fill=1, stroke=0)


def draw_glyph(c, sym, cx, cy, R):
    col = COLORS[sym]
    if sym == 1:
        c.setFillColor(col)
        c.circle(cx, cy, R * 0.62, stroke=0, fill=1)
    elif sym == 2:
        c.setFillColor(col)
        w, h = R * 1.8, R * 0.7
        c.roundRect(cx - w / 2, cy - h / 2, w, h, h / 2, stroke=0, fill=1)
    elif sym in (3, 4, 5, 6, 8):
        rot = -90 if sym != 4 else -45  # square sits flat
        if sym == 3:
            rot = 90  # triangle points up
        draw_path(c, polygon_pts(cx, cy, R, sym, rot), col)
    elif sym == 7:
        draw_path(c, star_pts(cx, cy, R * 1.06, R * 0.52, 7, 90), col)
    else:  # 9
        draw_path(c, star_pts(cx, cy, R * 1.06, R * 0.52, 9, 90), col)
    # white pip numeral in the glyph's heart
    c.setFillColor(Color(1, 1, 1))
    size = R * (0.85 if sym in (1, 3, 7, 9) else 1.0)
    if sym == 2:
        size = R * 0.55
    if sym == 3:
        cy -= R * 0.18  # optical centre of a triangle is lower
    c.setFont("Helvetica-Bold", size)
    c.drawCentredString(cx, cy - size * 0.36, str(sym))


def draw_corner_index(c, sym, x, y, rotated):
    c.saveState()
    c.translate(x, y)
    if rotated:
        c.rotate(180)
    c.setFillColor(COLORS[sym])
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(0, 0, str(sym))
    c.restoreState()


def draw_face(c, sym, ox, oy):
    """One card face at lower-left (ox, oy). Identical template both faces."""
    c.setFillColor(PAPER)
    c.rect(ox, oy, CARD_W, CARD_H, stroke=0, fill=1)
    # inner frame, inset enough to forgive duplex drift
    c.setStrokeColor(COLORS[sym])
    c.setLineWidth(1.1)
    c.roundRect(ox + 4 * mm, oy + 4 * mm, CARD_W - 8 * mm, CARD_H - 8 * mm,
                3 * mm, stroke=1, fill=0)
    cx, cy = ox + CARD_W / 2, oy + CARD_H / 2
    draw_glyph(c, sym, cx, cy, 18.5 * mm)
    # corner indices: top-left upright, bottom-right rotated (reads both ways)
    draw_corner_index(c, sym, ox + 9.5 * mm, oy + CARD_H - 12.5 * mm, False)
    draw_corner_index(c, sym, ox + CARD_W - 9.5 * mm, oy + 12.5 * mm, True)


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
        c.line(x, PAGE_H - MARGIN_Y, x, MARGIN_Y)
    for row in range(ROWS + 1):
        y = PAGE_H - MARGIN_Y - row * CARD_H
        c.line(MARGIN_X - 4 * mm, y, MARGIN_X, y)
        c.line(PAGE_W - MARGIN_X, y, PAGE_W - MARGIN_X + 4 * mm, y)
        c.line(MARGIN_X, y, PAGE_W - MARGIN_X, y)
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
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 28 * mm, "THE FLIP DECK")
    c.setFont("Helvetica", 11)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 35 * mm,
                        "36-card master prototype · 9 symbols · every pair "
                        "exactly once · Set D “Glyphs” skin")
    # glyph legend
    top = PAGE_H - 52 * mm
    for i, sym in enumerate(SYMBOLS):
        gx = PAGE_W / 2 + (i - 4) * 20 * mm
        draw_glyph(c, sym, gx, top, 6.5 * mm)
        c.setFillColor(INK)
        c.setFont("Helvetica", 8)
        c.drawCentredString(gx, top - 12.5 * mm, NAMES[sym])
    # instructions
    lines = [
        ("PRINTING", [
            "Print at 100% scale (no “fit to page”) on A4 cardstock.",
            "Page 1 (this page): print single-sided, or skip it.",
            "Pages 2–9: print DOUBLE-SIDED, flip on LONG edge.",
            "Check duplex alignment by holding a sheet up to the light;",
            "the 4 mm frame inset forgives a couple of millimetres of drift.",
            "Cut along the dashed guides: 9 cards per sheet, 36 total.",
            "Standard 63.5 × 88 mm sleeves fit. Opaque sleeves are wasted",
            "here — there is no card back. Both sides are faces.",
        ]),
        ("THE DECK", [
            "Each card carries one glyph on each side; every possible pair",
            "of the nine glyphs appears on exactly one card (36 = 9×8÷2).",
            "Shape is rank: count the sides. Pips 1–9 sit in two corners of",
            "every face, identically placed — no mark on any card reveals",
            "which of its two faces you are looking at.",
            "Games for fewer symbols use a subset: glyphs 1–6 (15 cards),",
            "1–7 (21) or 1–8 (28) form exact smaller all-pairs decks.",
        ]),
        ("SORTING AFTER PLAY", [
            "To verify the deck: lay cards in rows by their lower glyph —",
            "row 1 holds 1+2 … 1+9 (eight cards), row 2 holds 2+3 … 2+9",
            "(seven), and so on. A missing card names itself.",
        ]),
    ]
    y = top - 28 * mm
    for head, body in lines:
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(INK)
        c.drawString(30 * mm, y, head)
        y -= 6.5 * mm
        c.setFont("Helvetica", 9.5)
        for ln in body:
            c.drawString(30 * mm, y, ln)
            y -= 5 * mm
        y -= 4 * mm
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(PAGE_W / 2, 18 * mm,
                        "Flip-deck project · prototype skin · June 2026 "
                        "· collection: 9 games, one deck")
    c.showPage()


def main(path):
    c = rl_canvas.Canvas(path, pagesize=A4)
    c.setTitle("Flip Deck - 36-card print-and-play prototype")
    draw_legend(c)
    for s in range(4):
        chunk = PAIRS[s * 9:(s + 1) * 9]
        draw_sheet(c, chunk, 0, mirrored=False)  # fronts: lower glyph
        draw_sheet(c, chunk, 1, mirrored=True)   # backs: higher glyph
    c.save()
    print("wrote", path)


if __name__ == "__main__":
    main("FLIP_DECK_print_and_play.pdf")