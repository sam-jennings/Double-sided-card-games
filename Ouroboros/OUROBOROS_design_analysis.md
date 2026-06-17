# OUROBOROS — Design Analysis

*How the solitaire was tuned, v0 → v1.0. Companion to the rulebook; sibling to the SYZYGY/TURNCOAT analyses.*

> ## ⚠️ Playtest verdict (June 2026): demoted from the main collection
>
> Live testing of the short game (21 cards) found it **boring and too luck-based**, and the physical handling **awkward — the head's open symbol is the hidden face of the last card**, so the player must repeatedly check under the end of the serpent to know what's playable. The sim's warnings (§4) pointed the same way: the greedy/random gap was thin, meaning most of a session's variance is the shuffle, not the player.
>
> Lessons carried forward to the rest of the collection: **(1)** solo games on this deck should run on *open information or deduction, not hidden-face memory*; **(2)** any state a player must constantly know (an "open symbol") must be *visible*, never the down-face; **(3)** thin bot skill-gaps predicted the live experience accurately — treat them as a red flag before tabling.
>
> The design is retained below as a record and as a possible box-page *curiosity* (the Eulerian guarantee and the impossible-single-scar theorem remain lovely), but it is not a main game.

## 1. The mathematical spine

The game is an Eulerian-trail construction in disguise: cards are edges of K₉ (or K₇), the serpent is a walk, and flipping decides which endpoint of each edge faces which neighbour. Three theorems do real design work:

1. **A perfect serpent always exists.** K₇ and K₉ have all-even degrees (6 and 8), so an Eulerian *circuit* — a closed walk using every card — exists for any deck contents. The puzzle is purely about draw order and limited hand foresight, never about an unwinnable deal. (This is also why 6- and 8-symbol decks can't host the game: odd degrees make closure impossible.)
2. **Full placement forces closure.** A trail with two *distinct* endpoints requires exactly those two vertices to have odd degree. All degrees are even, so any scarless serpent containing all cards *must* bite its own tail — the bite is a theorem, not a rule.
3. **Exactly one scar is impossible.** Model each scar join as an extra edge between the two mismatched symbols. The finished loop is a closed walk, so every symbol needs even total degree; real degrees are already even, so the scar-edges alone must form an even-degree multigraph — which a single edge between distinct symbols never does. The simulation confirmed it: across ~50,000 finished serpents, not one ended with exactly 1 scar. The rulebook sells this as flavour ("scars come in constellations"); it's also a free tension mechanic — one scar means you're guaranteed at least two.

## 2. v0 failed: the no-scar game is dead on arrival

The first ruleset had no scars — get stuck, lose, count your cards. Simulated win rates (1,500 games/config, seed 42):

| n | Hand | Random win | Greedy win | Avg cards placed |
|---|---|---|---|---|
| 9 | 3 | 0.0% | 0.0% | 4.3 |
| 9 | 4 | 0.3% | 0.5% | 6.7 |
| 9 | 5 | 2.2% | 6.2% | 11.4 |
| 9 | 8 | 30.7% | 43.8% | 26.7 |

The structural problem: a hand accumulates **adversely selected** dead cards — everything playable gets played, everything dead stays — so the hand poisons itself and most games died inside seven cards. Reaching playable win rates needed an 8-card hand, which is unholdable and unfun. Hard-fail solitaires need failure to arrive *slowly*; this one face-planted in the first minute.

## 3. v1.0: scars — always finish, count the damage

Replacing lose-on-stuck with the forced scar tie converts the game from pass/fail into golf: every game completes, the score is the scar count, and the perfect game stays mathematically real. Three bot tiers establish the skill ladder (2,000 games/config, seed 42, closing scar included):

| n | Hand | Policy | Avg scars | 0 scars | ≤2 | ≤4 | ≤6 |
|---|---|---|---|---|---|---|---|
| 9 | 4 | random | 7.90 | 0.3% | 1.7% | 9.0% | 28.8% |
| 9 | 4 | greedy (deck-counting) | 7.00 | 0.6% | 3.2% | 16.6% | 42.9% |
| 9 | 4 | **smart (hand-health)** | **4.74** | 2.9% | 15.3% | 45.2% | 80.7% |
| 7 | 3 | random | 4.29 | 7.2% | 21.6% | 52.8% | 84.8% |
| 7 | 3 | greedy | 3.65 | 9.3% | 28.9% | 67.8% | 92.8% |
| 7 | 3 | **smart** | **2.60** | 17.9% | 51.1% | 88.2% | 99.5% |

Robustness: alternate seed 1234 reproduced the n=9 smart line (4.75 avg, 3.7% perfect).

**The skill signal is the headline.** The *greedy* policy (maximise remaining copies of the symbol you expose) — the move every beginner reasons toward — barely beats random (7.00 vs 7.90). The *smart* policy changes one thing: it values each play by **how many hand cards stay connected to either open end afterwards**, and scars nearly halve (4.74). The game's skill is hand stewardship, not symbol chasing — a real, learnable insight, which the rulebook teaches openly in the strategy notes (the project's SYZYGY precedent: surface the skill rather than hide it).

**Hand size selection.** Hand 4 at n=9 puts the three tiers at 7.9 / 7.0 / 4.7 — wide spread, perfect games rare but real (≈3% for a one-ply bot; humans who plan should exceed it). Hand 5 collapsed the top (28.5% perfect for smart): too easy to be a chase. Hand 3 at n=7 gives the short game a friendlier curve (18% perfect under smart play) — correct for the teaching version. Hand 5 survives as the "Hatchling" easy variant.

**Scoring ladder** read directly off the smart column: full game par (Bronze) at 5–6 (smart ≤6 = 81%), Silver 3–4, Gold 2 (smart ≤2 = 15%), perfect 0. Short game shifts one tier (par 3–4 ≈ smart ≤4 = 88%, Gold ≤2 = 51% — generous, it's the intro game).

## 4. Honest limitations

- **One-ply bots undersell humans.** The smart policy never plans multiple draws ahead, never deliberately routes the serpent toward its hand, and scars greedily-locally. Treat 4.74 as a *weak-skilled* anchor; strong human par may be a scar or two lower. If live play beats Gold routinely, tighten the ladder, not the rules.
- **Scar placement was simmed head-only** with the best-for-hand face choice; the rulebook's strategy hinges hold regardless, but live tuning may reveal tail-scar value.
- **Voluntary scars are untested.** Allowing a scar *by choice* (dumping a dead card early) might add depth or might trivialise par — flagged for live testing, not shipped.
- **Feel is unmeasured.** The numbers say golf; only the table says satisfying. First live questions: does saying the chain aloud ("Sun flows to Comet") carry the theme; does the impossible-single-scar fact land as delightful or as a gotcha; is hand-of-4 physically comfortable with double-faced cards (no card backs — hold them fanned low).

## 5. Change log

| Version | Change | Reason (data) |
|---|---|---|
| v0 | Lose-on-stuck, win = full loop | Win rates 0–6% at holdable hand sizes; games died at ~7 cards |
| v1.0 | Forced scar ties; score = scar count; closing mismatch = scar | 100% completion, three-tier skill ladder 7.9/7.0/4.7 |
| v1.0 | Hand fixed at 4 (full) / 3 (short) | Hand 5 made perfects too common (28.5%); hand 3 at n=9 too bleak |
| v1.0 | Ladder: 0/2/3–4/5–6 | Read off smart-policy distribution; "exactly 1" provably impossible |

*All numbers: ~36,000 simulated games for the shipped ruleset (plus ~12,000 on the rejected v0), seeds 42/1234, `ouroboros_sim.py`.*
