# CROSSROADS — Task List

*Current status: Stage 3 (table-tested, iterating), in the collection **on notice**. Last playtest: 02 (v1.1, 2P→off-spec 3P, flips barely used). Verdict: iterate, with a flagged structural concern (pass-to-win).*

*See [CROSSROADS_playtest_02.md](CROSSROADS_playtest_02.md) for the findings this plan responds to.*

---

## The reframing this plan is built on

Playtest 02 plus the designer's follow-up observations point at one root cause:

- The 2P **perfect-information** premise ("your rival's hand is exactly the rest, so everything is computable") is **the unfun, unused part** — players are at capacity tracking their *own* 14 cards and the invisible road-vs-contract split, and never reason about the opponent's hand at all.
- The deck-necessity does **not** depend on that premise. It comes from **pair-exhaustion** ("keeping a card deletes that road from the world"), which exists at *every* player count. So the player-count question is open, not fixed at 2P.
- **Hand size is the dominant comfort lever.** 2P = 14 (overwhelming); 3P = 9 + a 1-card board seed (group preferred it); **4P = exactly 7 each (28 = 4×7, no leftover).**
- The issues are **coupled**: more builders → more connectivity → **pass-to-win (Bug 1) gets worse**. So multiplayer is *blocked on* first fixing pass-to-win.
- **Deal-split** (some cards dealt as fixed contracts, some as roads) is a **dual-purpose fix**: it kills pass-to-win *and* removes the invisible road/contract mental split.

Bug references below are from [playtest 02](CROSSROADS_playtest_02.md): **Bug 1** pass-to-win (CRITICAL), **Bug 2** end trigger (HIGH), **Bug 3** 14-card overwhelm (HIGH), **Bug 4** first-turn paralysis (MEDIUM).

---

## Phase 0 — Decide the design question *(needs the designer)* — ✅ DECIDED

**Decision (June 2026):** pursue **both 2P and 3P** (4P falls out for free), and judge one-ruleset-vs-variants from the sim. Phase 1 answered it: **one ruleset with a player-count callout** — rules identical across counts; only the deal differs (14 / 9+seed / 7). 2P plays as perfect-information; 3P+ as partial-information; same rules, different feel.

- [x] Player count: 2P + 3P official (4P supported, same rules).
- [x] One ruleset, not separate variants (sim-confirmed, §6 design analysis).
- [x] Distinctness check: at 3–4P the "perfect information" claim weakens (TWELVE TRIALS, THE ORRERY cover open-info), but CROSSROADS stays the only **route/connection/contract** game — distinct from GLEAN/BLIGHT/TRIGON/TURNCOAT.
- [ ] Update [COLLECTION_OVERVIEW.md](../COLLECTION_OVERVIEW.md) player-count + coverage rows (Phase 6).

---

## Phase 1 — Fix pass-to-win *(the gate; sim work, no partner needed)* — ✅ DONE

*Tied to Bug 1. Findings written up in [CROSSROADS_design_analysis.md](CROSSROADS_design_analysis.md) §6. Sim: [crossroads_sim.py](crossroads_sim.py).*

**Outcome (June 2026):**
- [x] Simulator extended to N players (2/3/4; 3P uses a one-card neutral seed). 2P base regression reproduces the §3 numbers.
- [x] `PassBot` reproduces the bug — but the root cause is **denial-awareness, not player count**. The passer wins **~75% at every count (2P/3P/4P)** against *naive* builders (no denial — the playtest table), and **0–8%** against *greedy* builders that deny via flips. 2P is just as vulnerable as 3P. (Binding lesson 6(a): the obvious line hides the real skill.)
- [x] **Toll Roads is the fix.** Promotes to the base game. Kills pass-to-win unconditionally (passer wins **0% / 0% / 1.7%** vs naive; 0–0.3% vs greedy) and **preserves the skill gap** (~2×/3×/4× fair).
- [x] **Deal-split rejected.** It also suppresses the bug but guts the skill gap (4P → 1.36× fair, dull-game floor) and removes the keep-vs-build agency. Its handling benefit isn't worth the depth loss.
- [x] All counts terminate crisply under Signal Fires (0% turn-cap hits).

**Answer to the Phase 0 question — one ruleset, not two variants:** rules are identical across 2/3/4P; the only deal-time deltas are hand size (14/9/7) and the 3P seed card. The perfect-info (2P) vs partial-info (3P+) difference is emergent flavour, not a rule change. → **Ship as one ruleset with a player-count callout box.**

**Remaining for later phases / the table:**
- [ ] Confirm Toll's end-game scoring (trace route, count your roads) isn't a fiddly handling burden (Phase 4).
- [ ] Add a rulebook strategy note teaching **denial via flips** as the counter to hoarding (Phase 6) — the real onboarding lever per lesson 6(a).

---

## Phase 2 — Hand size & onboarding *(Bugs 3, 4)* — ✅ DONE (sim); table-pending

*Tied to playtest 02 Bug 3 (14-card overwhelm, the major 2P issue) and the designer's ruling that perfect information must not be a fixed property. Findings in [CROSSROADS_design_analysis.md](CROSSROADS_design_analysis.md) §7.*

**Decision — unify 2P and 3P into ONE variation: deal 9 roads each, set the remainder aside (out of play).**
- [x] Confirmed in sim: a fixed hand with the rest set aside **preserves the skill gap** (2.0×/3.0× fair at every H from 8–14) — unlike deal-split, which gutted it. The keep-vs-build decision is untouched.
- [x] Confirmed: the full 14-card deal connects **91%** of city-pairs (contracts nearly free — the pass-to-win soil); **H=9 drops this to 66% (2P) / 81% (3P)** — contracts become contested, fixing overwhelm *and* deepening the game.
- [x] Pass-to-win stays dead with Toll at H=9 (≤9% 2P, ≤4% 3P vs naive); all cells terminate.
- [x] **Individual vs unified → unified.** Both counts' main issues (2P overwhelm, 3P pass-to-win) are solved by the *same* two changes (deal-9 + Toll), so no separate rulesets. Only the aside-pile size differs (10 vs 1), invisible to play.
- [ ] **Table question (fun/feel, sim can't answer):** does 2P at H=9 feel satisfying or thin (66% connectivity, ~2.8 fulfilled/player)? **Fallback if thin: H=10** (74% conn, 3.8 fulfilled, skill gap unchanged).
- [x] Bug 4 (first-turn paralysis): Toll gives the opening a purpose (build infrastructure you score on); smaller hands shrink the opening choice space. Reassess at the table rather than adding an opening rule now.

**Identity shift flagged:** this retires the "perfect-information chess" framing → partial-information route/contract game. `COLLECTION_OVERVIEW.md` tags must change (Phase 6).

---

## Phase 3 — End-of-game trigger *(Bug 2, twice-flagged HIGH)*

- [ ] In the N-player sim, test the **eighth-dim end trigger** (game ends when all eight cities are dimmed / all shared flips spent) — confirm it terminates crisply at 2/3/4P (the 2P sim already shows ~20-turn clean ends).
- [ ] Check the trigger removes the **asymmetric-readiness** unfairness (no player trapped watching others build).
- [ ] If the eighth-dim clock alone doesn't resolve it, test the secondary condition floated in playtest 02: *a player may declare a stop only if their entire hand is completed contracts.*
- [ ] Document the chosen trigger; retire the old "double-pass" wording.

---

## Phase 4 — Table tests *(needs partners; counts per Phase 0)*

*Write a playtest plan per [playtesting.md](../.kiro/steering/playtesting.md) before each session, starting from these questions.*

- [ ] **Multiplayer session (3P and/or 4P)** if Phase 0 chose A or C:
  - [ ] Does the chosen pass-to-win fix hold at the table (try the pass line deliberately)?
  - [ ] Do smaller hands (7/9) cure the cold-start overwhelm?
  - [ ] Does partial information (can't compute who holds what) feel better than 2P's "compute everything"?
- [ ] **2P session** (still owes the long-standing recorded questions):
  - [ ] Does **eight flips ache**? Does **dimming read at a glance**? (H1/H2 — untested across two sessions running.)
  - [ ] Does pass-to-win survive proper 2P + Signal Fires play?
- [ ] Write playtest report 03. Verdict per count: iterate / park / cut.

---

## Phase 5 — Layout *(solo prototyping; needed before any flip-heavy table test)*

*Tied to playtest 01: the organic layout (card touches source city, shows destination face) emerged but felt ugly. More builders (3–4P) means more built roads on the table, so layout matters more, not less.*

- [ ] Prototype **Dual-rail** and **Harbour columns** solo (most structured; encode direction by position). Candidates:

  | Layout | Core idea | Direction encoding |
  |---|---|---|
  | **Dual-rail** | Each city has an inbound + outbound zone; a road lives in its destination's inbound zone | Position (filed under destination) |
  | **Harbour columns** | 8 cities in a row, a column below each; roads go in the destination city's column | Position + visible face |
  | **Compact ring + fan** | Larger ring with gaps; roads lean toward destination | Physical angle/lean |
  | **Graph drawing** | Freeform; cities drift apart as roads bridge them | Bridging + orientation |

- Solo assessment checklist:
  - [ ] Scan whole network state in < 5 s?
  - [ ] Trace A→B without picking anything up?
  - [ ] Flipping a road feels clean?
  - [ ] Still readable at 10–14 built roads (worse at 4P)?
  - [ ] Lit/dim city state reads alongside roads?
  - [ ] Fits a normal table?
- [ ] Pick a winner; write it to teach in < 30 s; update the rulebook.

---

## Phase 6 — Documentation *(after the above settle)*

- [ ] Rewrite the rulebook around the Phase 0 decision (player counts, deal-split if adopted, Toll-into-base if adopted, new end trigger, layout convention). Update the version and the design footnote.
- [ ] Reinforce **equal-deal** procedure and note **7-symbol is cut** (plays at 8 or 9 symbols only) — carried from playtest 01 Bug 3.
- [ ] Sync [COLLECTION_OVERVIEW.md](../COLLECTION_OVERVIEW.md): player count, coverage tables, status, outstanding questions.

---

## Parked / blocked

- **Draw-model variant (deal ~6 + draw replacements)** — *evaluated and rejected*, [design analysis §8](CROSSROADS_design_analysis.md). Fixes small-hand sparsity but dilutes the 2P skill gap to 1.47–1.60× (random refill = luck), introduces the no-card-back draw-pile handling hazard, and weakens pair-exhaustion. **Open-draft** version (choose from a face-up row) kept warm as a future "dynamic CROSSROADS" exploration — turns the handling problem into a feature, but a larger redesign.
- **Caravans variant balance** — direction-blind; design analysis says it probably doesn't need the flip pool. Park until the base game settles.
- **The Long Haul** (play twice, swap first player) — 2P-only; revisit only if 2P stays an official mode.

## Completed

- [x] Playtest 01 — no-flip, 7-sym + 9-sym. Core connection mechanic confirmed at 9 symbols; 7-sym refuted; layout convention emerged; asymmetric end + first-turn paralysis flagged.
- [x] Playtest 02 — v1.1 (2P → off-spec 3P, flips barely used). Surfaced pass-to-win (CRITICAL), re-confirmed end-trigger + hand-size bugs; found 3P/smaller hands more comfortable.
- [x] Simulation (design analysis v1.0→v1.1) — ko insufficiency proven, Signal Fires pool designed, pie rule adopted.
