# The Nine Signs — Canonical Symbol Reference

> The single source of truth for *what the symbols are*. This is the **reference**;
> [`SYMBOL_SETS.md`](SYMBOL_SETS.md) is the **rationale** (why this set won, the
> alternatives, the matrices), and `Designs/Brand Kit/` holds the **assets** (glyphs,
> colours, CSS). When those disagree with this file on the fixed set, this file wins.

The shipping deck carries **nine archetypal signs** — broad, family-neutral symbols
that each game reinterprets locally. The set is **settled**. Pip order is fixed and
printed on both faces of every card.

## The set

| Pip | Sign      | Glyph | Hue       | Archetype (verb)                  | Role                                                 |
| --: | --------- | :---: | --------- | --------------------------------- | ---------------------------------------------------- |
|   1 | **Moon**  |  🌙   | `#2E2C5F` | wane / reflect / catch-up         | **Outsider** — lowest rank, the catch-up valve       |
|   2 | **Leaf**  |  🍃   | `#3E7A3E` | grow / connect / turn toward      | —                                                    |
|   3 | **Wave**  |  🌊   | `#1577B5` | move / carry / flow               | —                                                    |
|   4 | **Flame** |  🔥   | `#D83A22` | burn / destroy / remove           | —                                                    |
|   5 | **Eye**   |  👁   | `#169488` | see / peek / reveal               | —                                                    |
|   6 | **Mask**  |  🎭   | `#A6328C` | swap / disguise / flip identity   | —                                                    |
|   7 | **Key**   |  🗝   | `#B98A2A` | unlock / extract / access         | —                                                    |
|   8 | **Star**  |   ⭐   | `#E0A91F` | the anomaly / draw the unexpected | **Wild** — the special-exception sign                |
|   9 | **Crown** |  👑   | `#5E3A9E` | rule / decree / self-determine    | **Apex** — highest rank, removed first for sub-decks |

The **pip is the authoritative rank and value** (1 lowest … 9 highest). The sign's
*name and picture* never override the number; a game's rank, tie-break, or issue
value always reads the pip.

## The two-layer rule

1. **Permanent deck identity (printed once, forever):** pip 1–9 on both faces, the
   sign icon + name, a colour, and a both-faces-identical orientation marker.
   **No ability text, no pair-specific decoration.**
2. **Per-game interpretation (in each rulebook):** what the signs *mean* in that
   game. The same nine signs carry different truths per game — that is the
   collection's premise, not a compromise.

> **Hard rule:** nothing on a card may differ between its two faces or correlate
> with the hidden face — including the orientation marker. A one-sided mark would
> leak hidden-face information (`.kiro/steering/physical-handling.md`).

## How each game reads a sign (selected)

The three role signs show the range; the rest are read through their archetype verb.

| Sign | TRIGON | TURNCOAT | CROSSROADS | THE COUNCIL | rank games* |
|---|---|---|---|---|---|
| **Moon** (1) | catch-up draw when isolated | erase the leader's banked card | a city (pip 1) | the cheapest issue (1) | rank 1 (lowest) |
| **Star** (8) | **wild** + corner draw | draw-and-play | a city (pip 8) | issue worth 8 | rank 8 |
| **Crown** (9) | flip a full line (decree) | extracts *itself* (apex) | the **capital** — its 8 cards become the board, Crown-face-down | the richest issue (9) | rank 9 (highest) |

\*rank games = FACE VALUE, THE UNPLAYED PAIR, GLEAN, BLIGHT (and THE COUNCIL's issue values). They use the pip directly.

Note: **"Star is wild" is a TRIGON rule, not a deck-wide property.** In every rank
game Star is simply worth 8. Wild, apex, and outsider are *roles a game may invoke*,
not marks printed on the card.

## Values check & sub-deck behaviour

Several games declare a **sub-deck**. The canonical way to build one is to **remove
the highest pips** — "remove every card showing an 8 or a 9" leaves the complete
7-sign deck (pips 1–7); the same trims to 6 or 8 signs. Sub-decks therefore always
**keep the low end and trim from the top.** Confirmed users: JANUS (1–7), CAIRN
(1–7 standard, all 9 on the Long Trail), FACE VALUE Quick Draw (1–7), CROSSROADS
(removes the 8 Crown cards to build the board, cities = pips 1–8).

This makes the pip→sign assignment **correct and sub-deck-safe**, for three reasons:

1. **The catch-up role is universal.** Moon (1) sits at the bottom, so it survives
   in *every* deck size — full, 8, 7, and 6. A game's catch-up/outsider valve is
   never lost to subsetting.
2. **Rank truncates cleanly from the top.** Because only the highest pips are
   removed, relative order is preserved and a sub-deck rank game simply has a lower
   ceiling (Key = 7 becomes the effective top in a 1–7 game). No middle gaps, no
   re-ranking.
3. **The apex disappears first, on purpose.** Crown (9) is the "set aside the
   greatest" sign, removed first for subsets and laid face-down as the board in
   CROSSROADS — exactly where the apex should sit.

### One constraint worth recording

The **wild (Star, 8)** and **apex (Crown, 9)** exist only in the full deck (Star also
survives an 8-sign subset). **A 6- or 7-sign sub-deck has no printed wild or apex.**
No current game breaks this — TRIGON (the only "wild" game) and the apex-using games
run on the full 36, and rank games on subsets simply use the pip generically. But a
*future* sub-deck game wanting a wild or apex must either avoid those roles or
**declare a substitute** (legal, since wild/apex are per-game rules, not printed
marks — e.g. "in this 7-sign game, Key is wild").

### One inconsistency to note

[THE ORRERY](The%20Orrery/THE_ORRERY_rulebook.md) builds its short game from "any
7-symbol sub-deck" (remove any two signs), not the canonical top-two. That is
mathematically valid — any 7 of the 9 signs form a complete all-pairs deck — and
harmless because ORRERY is rank-agnostic. Treat **top-removal as the canonical
default**; ORRERY's "any two" is the rank-agnostic exception.

## See also

- [`SYMBOL_SETS.md`](SYMBOL_SETS.md) — the full study: why the Nine Signs, the rejected
  alternatives (Sky / Court / Bestiary / Glyphs / Menagerie), and the June 2026
  revision (Void→Moon, Root→Leaf; Flame/Mask redrawn).
- [`.kiro/steering/deck-structure.md`](.kiro/steering/deck-structure.md) — the deck
  maths, the subset property, and the special role of symbol 9.
- `Designs/Brand Kit/` — `glyphs.svg`, `double-sided.css`, and `starter.html` carry
  the production glyphs and hues. Draft glyphs are also in
  [`Designs/symbol_recognisability_test.html`](Designs/symbol_recognisability_test.html).
