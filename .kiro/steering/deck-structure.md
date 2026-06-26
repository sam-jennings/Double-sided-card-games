# Deck Structure & Mathematical Constraints

The deck is the fixed foundation of everything. Internalise these facts before proposing or editing any game.

## The master deck

- **9 symbols, 36 cards.** Each card is double-faced, one symbol per face.
- **Every unordered pair of distinct symbols appears on exactly one card.** The deck *is* the complete graph **K₉**: symbols are vertices, cards are edges.
- **Each symbol appears on exactly 8 cards** (its degree in K₉).
- Card count for n symbols is `C(n,2) = n(n−1)/2`:

  | symbols | cards | cards/symbol |
  |---:|---:|---:|
  | 6 | 15 | 5 |
  | 7 | 21 | 6 |
  | 8 | 28 | 7 |
  | **9** | **36** | **8** |

## The subset property (load-bearing)

Remove every card showing symbol 8 or 9 (on either face) and the remaining 21 cards are *exactly* the complete 7-symbol deck. The same holds for any 6/7/8-symbol subset. Consequences:

- A game declares its **symbol range** (e.g. "use symbols 1–7") instead of needing a separate deck.
- Subset selection must be fast at the table. There is a **canonical symbol order 1–9** with an **index pip 1–9 printed on both faces** of every card, so a subset is a quick sort ("remove all cards showing 8 or 9").
- Choosing 9 was not choosing against smaller sizes — it is the only size that *contains* them. This is settled (`DECK_SIZE_DECISION.md`); don't relitigate it without new evidence.

## Structural properties games exploit

| Property | Exists at | Used by |
|---|---|---|
| Every pair exactly once (deduction registry) | all sizes | JANUS, FORKED TONGUE, UNPLAYED PAIR, CROSSROADS, FACE VALUE |
| Even divisibility (2,3,4,6 players) | 36 only | TRIGON, TURNCOAT, WILDFIRE, COUNCIL |
| 6×6 exact grid | 36 | TWELVE TRIALS |
| Eulerian circuit (whole deck chains into one loop) | odd symbol counts (7, 9) | OUROBOROS (revived) |
| Steiner triple / triangle partition | 7 (Fano) and 9 only | TWELVE TRIALS |
| 12 triangles → 4 "seasons" of 3, each covering all 9 symbols once | 9 | TWELVE TRIALS |

### The 12-triangle / 4-season almanac (reference)

| Season I | Season II | Season III | Season IV |
|---|---|---|---|
| 1-2-3 | 1-4-7 | 1-5-9 | 1-6-8 |
| 4-5-6 | 2-5-8 | 2-6-7 | 2-4-9 |
| 7-8-9 | 3-6-9 | 3-4-8 | 3-5-7 |

Each row is a symbol-triangle; each column uses all nine symbols exactly once.

## Special role of symbol 9

Symbol 9 is removed first for subsets, and its 8 cards physically become the board in CROSSROADS (placed 9-face-down — symbol 9 is never *seen* during that game; the cities show symbols 1–8). Wanting 9 to *feel* above the others is a soft flavour preference (the subset-removal story reads best when you "set aside the greatest"), not a legibility requirement. In the Nine Signs set (see below), symbol 9 is **Crown**.

## Symbol identity — The Nine Signs (working title, primary)

The shipping symbol set uses **nine archetypal signs** — broad, family-neutral symbols that each game reinterprets locally. This is a settled decision. The canonical quick reference is [`SYMBOL_SET.md`](../../SYMBOL_SET.md) (pip · name · glyph · colour · role · per-game meaning · sub-deck behaviour); see `SYMBOL_SETS.md` §7 for the full study and rationale.

| Pip | Sign |
|---:|---|
| 1 | Moon |
| 2 | Leaf |
| 3 | Wave |
| 4 | Flame |
| 5 | Eye |
| 6 | Mask |
| 7 | Key |
| 8 | Star |
| 9 | Crown |

### The two-layer production rule

1. **Permanent deck identity (printed once, forever):** pip 1–9 on both faces, sign icon + name, colour/pattern, and a both-faces-identical orientation marker. No ability text, no pair-specific decoration.
2. **Per-game interpretation (in each rulebook):** what the signs *mean* in that game. The Crown is a capital city in CROSSROADS, the top issue in THE COUNCIL, the apex faction in TURNCOAT. The Eye is deduction/reveal in one game, surveillance in another.

### Role symbols (mechanically relevant)

- **Star (8):** the wild / special-exception sign (TRIGON's "Star is wild" is preserved verbatim).
- **Crown (9):** the apex / highest rank / capital.
- **Moon (1):** the outsider / catch-up / lowest rank.

### Hard rules

- **No one-sided asymmetric marks of any kind** — including the orientation marker, which must be identical on both faces. They would leak hidden-face information (`physical-handling.md`).
- **Render as bold, filled, high-contrast icons** — legibility at arm's length, rotated, by colour-blind players. Shape carries identity; colour is secondary.
- **Prototype with Set D Glyphs** (geometric shapes) for legibility testing — the accessibility benchmark the shipping art must not regress against.

### Alternatives (documented, not recommended)

- **The Ninefold Menagerie** (Set E: Mouse·Hare·Fox·Owl·Serpent·Stag·Wolf·Bear·Dragon) — the "one-world" alternative if the product pivots to a single coherent setting rather than a multi-game toolkit. Stronger rank intuition (food chain) at the cost of forcing animal framing onto CROSSROADS and THE COUNCIL.
- **Celestial Sky** (Set A) — most conservative; keeps TRIGON native, re-skins only TURNCOAT. Radiant-disc confusability cluster (Sun/Star/Nova/Meteor) needs deliberate art resolution.
- **Set D Glyphs** — permanent prototyping/accessibility companion, never the shipping identity (no ability mnemonics).

Full study, fit matrix, and re-skin mappings: `SYMBOL_SETS.md`.

## When proposing any rule or game

Verify against the maths:
- Does it actually need the all-pairs structure, or would generic symbols do? (If generic, reconsider — see `design-principles.md`.)
- Does the chosen symbol count make the structure it relies on *exist*? (Loops need odd counts; triangle partitions need 7 or 9; even deals need 36.)
- Does it respect divisibility for its target player counts?
- If you assert a combinatorial fact, it must be **verifiable** — prefer computing it (see `simulation-standards.md`).
