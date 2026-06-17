# Deck Size Decision

*Combinatorial analysis of the 6/7/8/9-symbol options, scored against the full game portfolio. All numbers verified programmatically (see appendix).*

## Recommendation

**Fix the deck at 9 symbols / 36 cards — and treat it as a *master deck* whose smaller decks live inside it.**

The decisive fact is the subset property: remove all cards carrying symbols 8 and 9 from the 36-card deck and the remaining 21 cards are *exactly* the complete 7-symbol deck. The same holds for any 6-, 7-, or 8-symbol subset. Choosing 9 is therefore not choosing *against* the smaller sizes — it's the only choice that contains them. A game tuned for 15 cards simply says "use these 6 symbols"; a game that wants 36 uses everything. The symbol-count question dissolves from "which size?" into "which size *per game*?", which is the right question for a collection.

## The structural maths

| Property | 6 sym / 15 | 7 sym / 21 | 8 sym / 28 | **9 sym / 36** |
|---|---|---|---|---|
| Cards per symbol | 5 | 6 | 7 | **8** |
| Deals evenly to players | 3, 5 | 3 | 2, 4 | **2, 3, 4, 6** |
| Exact rectangular grid | 3×5 | 3×7 | 4×7 | **6×6** |
| Eulerian circuit (whole deck chains into one loop) | no | **yes** | no | **yes** |
| Triangle partition (deck = disjoint symbol-triangles) | no | **yes (7 = Fano plane)** | no | **yes (12, in 4 "seasons")** |
| 1-factorisation (deck = rounds where every symbol appears once) | yes (5×3) | near (7×3) | yes (7×4) | near (9×4) |
| Triangles available | 20 | 35 | 56 | **84** |
| Hidden-side candidates per visible symbol | 5 | 6 | 7 | **8** |

Four findings matter most:

**1. Divisibility.** 36 is the only deck size that deals evenly at 2, 3, 4 *and* 6 players — the counts that matter. The 5-player remainder of exactly one card is itself a usable mechanic (THE UNPLAYED PAIR builds its deduction endgame on it). 21 cards divide only by 3; 28 only by 2 and 4.

**2. Odd symbol counts unlock the loop games.** Only at 7 and 9 symbols does every symbol sit on an even number of cards, which is what lets the entire deck chain into a single closed loop (OUROBOROS) — at 6 or 8 symbols that game is mathematically impossible.

**3. Only 7 and 9 admit triangle partitions.** The deck splitting perfectly into symbol-triangles (a Steiner triple system) exists only at 7 (the Fano plane) and 9 symbols. At 9 it's stronger still: the 12 triangles group into **4 seasons of 3 triangles, each season covering all 9 symbols exactly once** — a free campaign/round structure (TWELVE TRIALS). 6 and 8 get nothing.

**4. The subset property.** Every smaller all-pairs deck is an exact sub-deck of the 36-card deck. The converse is false: choose 28 cards and the 36-card games are gone forever, including both finished designs.

Verified 12-triangle partition (symbols numbered 1–9), for reference cards:

| Season I | Season II | Season III | Season IV |
|---|---|---|---|
| 1-2-3 | 1-4-7 | 1-5-9 | 1-6-8 |
| 4-5-6 | 2-5-8 | 2-6-7 | 2-4-9 |
| 7-8-9 | 3-6-9 | 3-4-8 | 3-5-7 |

*(Each row of three cards is a triangle; each column uses all nine symbols exactly once.)*

## Portfolio fit

Best size per game, across the whole collection:

| Game | 15 | 21 | 28 | 36 | Playable at 36 via subset? |
|---|---|---|---|---|---|
| TRIGON (tuned, ~23k sims) | – | – | – | **best** | native |
| TURNCOAT (tuned, ~22k sims) | – | – | – | **best** | native |
| JANUS (co-op) | ok | **best** | ok | ok | yes — 7-symbol subset |
| FALSE FACE (bluffing) | weak | ok | ok | **best** | native |
| OUROBOROS (solo) | impossible | **best (short)** | impossible | **best (full)** | yes — both versions |
| TWELVE TRIALS (solo/co-op) | impossible | ok | impossible | **best** | native |
| THE UNPLAYED PAIR (tricks) | weak | weak | ok | **best** | native |
| CROSSROADS (2P duel) | ok (micro) | weak | **best** | weak | yes — 8-symbol subset |
| THE COUNCIL (negotiation) | weak | weak | ok | **best** | native |
| HOT POTATO PAIRS (party) | weak | weak | weak | **best** | native |

Score it however you like — most-firsts, fewest-impossibles, or coverage of player counts — 36 wins on every column, and every game whose *ideal* size is smaller is fully served by a labelled subset. No game in the portfolio is harmed by owning the larger deck; three games (both finished designs plus TWELVE TRIALS at full strength) are impossible without it.

The 6-player counts (FALSE FACE, THE COUNCIL, HOT POTATO PAIRS) only exist at 36 — and "larger player counts" was an explicit collection goal.

## What this costs, honestly

- **Production:** 36 cards vs 15–28. Still a single small box; the all-pairs structure caps the count regardless.
- **Memory load at 9 symbols:** real, but it's a *per-game* cost, not a deck cost. The TURNCOAT/TRIGON data already showed 9 symbol-abilities is the practical ceiling; new games above either use subsets or (like most of the eight new concepts) use symbols as identities with **no per-symbol rules at all** — the structural games (OUROBOROS, TWELVE TRIALS, CROSSROADS, HOT POTATO PAIRS) carry zero ability text.
- **Shuffling/setup of subsets:** finding "all cards without symbols 8–9" must be fast. Design consequence below.

## Design consequences (do these next)

1. **Rank the symbols.** Give the 9 symbols a canonical, printed order (1–9, or a visual sequence). Subset games then say "remove all cards showing symbol 8 or 9 on either face" — a 20-second sort. Consider a small index pip (1–9) in the card corner for both faces.
2. **Keep both finished games untouched.** TRIGON and TURNCOAT are tuned at 36; the decision validates ~45k simulated games of investment rather than discarding it.
3. **Print the almanac.** The 12-triangle / 4-season table above should become a reference card — it powers TWELVE TRIALS and is a beautiful proof-of-depth for the box copy.
4. **Adopt the subset framing in the project goals.** The symbol-count question in `flip_card_project_goals.md` can be marked resolved: *n = 9, with games declaring their symbol range.*

## Appendix — verification

All table claims were computed (Python, `itertools`/`math.comb`):

- Deck sizes, per-symbol counts, triangle counts: `C(n,2)`, `n−1`, `C(n,3)` for n = 6..9.
- Divisibility: direct remainder checks, players 2–6.
- Eulerian circuits: degree parity (n−1 even ⇔ n odd); an explicit 36-edge circuit of K₉ was constructed (Hierholzer) as proof.
- Triangle partitions: STS(n) exists iff n ≡ 1, 3 (mod 6) → n = 7, 9 only. The 12-triple system above was generated from the affine plane AG(2,3), verified to cover all 36 pairs exactly once, and verified resolvable into the 4 parallel classes shown.
- Subset property: verified that the cards of the 9-symbol deck restricted to any k chosen symbols form exactly the complete k-symbol deck (k = 6, 7, 8).
