# OUROBOROS — Design Analysis

*How the solitaire was tuned, v0 → v1.0, then revived as v1.1. Companion to the rulebook; sibling to the SYZYGY/TURNCOAT analyses.*

> ## ↩️ Revival (June 2026): back in the pipeline as v1.1
>
> OUROBOROS has been **revived from the cut pile into the pipeline** (Stage 2, validated — awaiting a re-test of the fix). The June 2026 cut verdict below stands as a historical record, but two of its three pillars were re-examined and found weaker than they first looked. See **§6** for the full revival case. In short:
>
> - **The handling bug is fixed (v1.1).** The head's open symbol no longer lives on a buried face. Cards are now laid showing their *onward* symbol, so both open ends stay face-up (orientation-as-state, per CROSSROADS) — you never lift the serpent. One-line convention change; the maths is untouched.
> - **The "luck-dominant / thin skill gap" verdict leaned on one-ply floor numbers.** A Monte-Carlo planning bot (the deeper bot the analysis itself said was missing) reaches **~1.74× over random at n=9 and ~1.84× at n=7** — above the collection's ~1.5× healthy bar. The real defect was always that the *obvious* (greedy) line is near-random (~1.13×); that is a **teaching** problem (surface hand-stewardship), which the strategy notes already address.
> - **Remaining gate:** a first table test of v1.1 — does the fixed handling read cleanly, and is the hand-stewardship skill *learnable* at the table rather than only in the sim? Promotion to the collection still requires that test.

> ## ⚠️ Playtest verdict (June 2026): demoted from the main collection *(superseded by §6 — retained as record)*
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

## 6. Revival (June 2026): v1.1, and re-examining the cut

OUROBOROS was cut on three recorded reasons (see the verdict box and `COLLECTION_AUDIT.md` §4): **(a)** luck-driven play, **(b)** the open symbol buried under the serpent's head, **(c)** a thin skill gap. A re-reading found the cut over-weighted (a) and (c) and rested (c) on numbers the analysis itself had flagged as a floor. Each is revisited below.

### 6.1 (b) The buried open symbol — fixed in v1.1

This was the one *handling* defect, and it has a clean fix. v1.0 laid each card showing its **matched** face, so the head's open symbol — the thing you must read to know what's playable — sat on the hidden bottom face, forcing you to lift the serpent's head. v1.1 inverts the convention: **lay each card showing its *onward* (open) symbol**, pressing the matched symbol into the seam. Both open ends are then permanently face-up; nothing you need is ever hidden. This is the orientation-as-state technique CROSSROADS and TWELVE TRIALS use. The maths, scoring, and theorems are untouched — it is purely a layout convention. Cut reason (b) is resolved.

### 6.2 (c) The skill gap — a deeper bot clears the bar

The cut cited the *greedy*-vs-random gap (~1.13× at n=9) as evidence of a dull game. But greedy is the beginner-obvious line, not skilled play, and §4 explicitly warned the one-ply bots "undersell humans… strong human par may be a scar or two lower." A **Monte-Carlo planning bot** was added to `ouroboros_sim.py` to test that warning: for each choice it reshuffles the *remaining* deck (the honest information set — the player knows which cards remain, not their order) and rolls the game out under `smart`, picking the lowest expected scars.

Results (avg scars, lower is better; baselines 1,000 games, mc 60 games × 12 rollouts, seed 42):

| n | H | random | greedy | smart | **mc (planner)** | mc × over random |
|---|---|---|---|---|---|---|
| 9 | 4 | 7.88 | 6.95 | 4.78 | **4.52** | **~1.74×** |
| 7 | 3 | 4.29 | 3.60 | 2.63 | **2.33** | **~1.84×** |

Two findings:

1. **The ceiling clears the bar.** The planner beats random by ~1.74×/~1.84×, above the collection's ~1.5× healthy threshold (`design-principles.md` lesson 6). The skill is real; the one-ply numbers were a floor, exactly as the analysis suspected.
2. **`smart` is already near that ceiling.** The planner only edges out the one-ply `smart` heuristic (4.52 vs 4.78; 2.33 vs 2.63), so most of the achievable skill is captured by the *hand-stewardship* idea the strategy notes already teach. The gap between *obvious* play (greedy) and *good* play (smart/mc) is the whole story: a learnable, counter-intuitive insight, not luck.

*(mc counts are small and so noisier than the baselines; the direction is stable across the n=9 and n=7 rows and is enough to retire the "thin skill gap" claim. A larger mc run is cheap if a firmer number is wanted.)*

### 6.3 (a) Luck — reframed, not dismissed

A single-pass, limited-foresight puzzle does carry shuffle variance — that is honest and unchanged. But "most variance is the shuffle" is in tension with a skilled line that nearly halves random's scars. The accurate statement: **the *obvious* strategy is near-random, so a first-time player correctly feels luck-buffeted**, while the real skill (keeping hand cards connected to an open end) is invisible until taught. That is a teaching/onboarding problem layered on the (now-fixed) handling tedium — both addressable — not proof of an intrinsic luck ceiling. The skilled experience exists; the v1.1 job is to make players *find* it.

### 6.4 Status and the remaining gate

OUROBOROS returns to the **pipeline at Stage 2 (validated)**, not straight into the collection. Promotion still requires a **first table test of v1.1**, answering:

- Does the open-symbol-shown layout read cleanly — genuinely no lifting, no buried state? (Confirms 6.1.)
- Is hand-stewardship *learnable at the table*? Does a player who reads the strategy notes climb out of the greedy near-random band within a session or two? (Confirms 6.2.)
- With handling and teaching fixed, does the shuffle variance now read as *tension* rather than *luck-blame*? (Confirms 6.3.)

If the table refutes these, the honest call is to re-cut — but on evidence about v1.1, not the v1.0 floor numbers. The impossible-single-scar theorem (§1) and the Eulerian guarantee remain intact and are now attached to a game that is legible to handle.

### 6.5 Change log (revival)

| Version | Change | Reason |
|---|---|---|
| v1.1 | Lay each card showing its **onward** symbol; both open ends stay face-up | Fixes cut reason (b) — buried head symbol; orientation-as-state |
| v1.1 | Added Monte-Carlo planner to the sim; ceiling ~1.74×/~1.84× over random | Tests cut reason (c) — one-ply bots were a floor; ceiling clears the bar |
| v1.1 | Revived to pipeline Stage 2, pending a first v1.1 table test | Two of three cut reasons weakened; the third (handling) fixed |
