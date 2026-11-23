# THE ORRERY — Playtest Plan 02

*Pairs with the forthcoming `ORRERY_playtest_02.md`. Written per `.kiro/steering/playtesting.md`. Hypotheses come from the revised first-table questions in [ORRERY_playtest_01.md](ORRERY_playtest_01.md), the open questions at the end of [ORRERY_rulebook.md](ORRERY_rulebook.md), and tasks 2–3 in [ORRERY_tasks.md](ORRERY_tasks.md). Numbered 02 to pair with the second session's report.*

## Open before the session

No rule gap blocks a session. Three things to settle first:

- **No flip tracker.** The rules say to count flips ("paper helps") and have no physical marker. TWELVE TRIALS dropped its flip count mid-solve for the same reason (its playtest 01, bug 3). **For this session:** keep a pencil tally and tick it the moment a card is turned.
- **Replaying a deal needs its starting faces.** The rulebook suggests replaying the same deal to cut two flips, but nothing records how the deal started. **Photograph the sky before the first move** of every deal.
- **The tiers are not calibrated.** There is no design analysis, simulation or solver for THE ORRERY. Sky debt is only a lower bound, and the rulebook says so. Treat the tier you reach as a data point, not a verdict.

## Setup

- **Game:** THE ORRERY
- **Version:** v0.2 (terminology revised after playtest 01: split cycles allowed, Clockmaker a separate prestige challenge).
- **Players:** 1 (solo).
- **Session shape:**
  1. **Deals 1–2 — Apprentice, random.** 7 signs / 21 cards / three orbits of 7, target 3 per sign. Shuffle with random faces. **No pre-balancing**: playtest 01's pre-balanced deal is what left sky debt and flips untested.
  2. **Deal 3 — full game, if time allows.** 9 signs / 36 cards / four orbits of 9, target 4.
  3. **Clockmaker:** out of scope (see below).
- **Why this session:** `next_step` is "test a random full deal with the revised terminology". This is the first session where sky debt and flips actually count.

**Expected sky debt** (computed for this plan: 20,000 random-face deals): **7-symbol mean 3.3** (most deals 2–4); **9-symbol mean 4.9** (most deals 4–6). A deal far outside those ranges is worth noting.

## Hypotheses to test

- **H1 — Sky debt is quick and feels fair.** Rulebook question 2. *Prediction:* counting the sky and working out the debt takes **under 3 minutes**, and the final flip count lands close enough to it (within +4) that the debt feels like a real benchmark. *Falsified if* setup arithmetic drags or is skipped, or the final count is so far above the debt (+7 or more) that the bound feels meaningless.
- **H2 — Split cycles now feel valid.** Playtest 01's high-severity bug was "orbit" implying one loop. *Prediction:* when a finished orbit contains two or more cycles, you accept it without any sense of failure. *Falsified if* you rearrange a valid split orbit "to make it a proper loop", or feel the solve is second-rate. (Naming watch item from `naming.md`: if "orbit" misleads again, record it.)
- **H3 — The standard 7-symbol game holds up across random deals.** Revised question 1. *Prediction:* both Apprentice deals are challenging and satisfying, not one interesting deal and one rote one. *Falsified if* deal 2 feels solved by routine.
- **H4 — Flipping is the interesting cost, not bookkeeping.** Task 2. *Prediction:* at least once per deal you deliberately *swap* cards between orbits instead of flipping (the strategy note "swap before flipping"). *Falsified if* flips are made mechanically, or the tally is abandoned.
- **H5 — The full 9-symbol game is manageable after 7.** Revised question 2. *Prediction:* deal 3 is completed in ~25 minutes without feeling it needs a solver. *Falsified if* it's abandoned or feels like computation.
- **H6 — It feels distinct from TWELVE TRIALS.** Revised question 7; left open in playtest 01. *Prediction:* you can name what feels different (balancing global counts and swapping between groups, against hunting closed triangles). *Falsified if* it reads as the same puzzle with different labels.

## What to watch

Handling first:

- **Examine-and-return.** Every check of a hidden face is a lift. Watch for any card put back the wrong way up: that is an unrecorded flip, and it breaks the tally.
- **Visible-only false completes.** The FAQ warns that a row can look perfect on top with a mess underneath. Count how often a "done" orbit fails the hidden-face check.
- **Footprint.** At 9 symbols: four rows of nine plus a pool. TWELVE TRIALS sprawled badly at the same card count, so measure the area.
- **Tally drift.** Does the pencil tally keep up with your hands?

Then:

- **Emergency almanac.** Rulebook question 4. Note whether you are tempted to look, and whether you do.
- **Split-cycle frequency.** Revised question 3. Trace the arrows in each finished orbit and record how many cycles it has.

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | Debt worked out in < 3 min; final within +4 | Arithmetic skipped or tedious; +7 or more |
| H2 | Split orbits accepted as done | Rearranged into one loop "properly" |
| H3 | Both Apprentice deals engaging | Second deal rote |
| H4 | Deliberate swaps instead of flips | Mechanical flipping; tally dropped |
| H5 | 9-symbol deal finished, manageable | Abandoned, or "needs a solver" |
| H6 | A named difference from TWELVE TRIALS | "Same puzzle, different labels" |
| Handling | No unrecorded flips (photo check) | Faces silently changed |

## Teaching plan (retest — what to re-read)

- Re-read **Core idea** and the FAQ entry **"Can a valid orbit contain split cycles?"** with its 7-symbol example. These are the v0.2 changes, and H2 depends on them having landed.
- Re-read the sky-debt example in Setup step 4 (`6, 5, 5, 4, 4, 4, 3, 3, 2` → debt 4), and remember the target is **3** at 7 symbols.
- Don't re-read the strategy notes before deal 1. H4 tests whether swapping is found, not taught.

## Record sheet

| | Deal 1 (7-sym) | Deal 2 (7-sym) | Deal 3 (9-sym) |
|---|---|---|---|
| Photographed? (Y/N) | | | |
| Visible counts at setup | | | |
| Sky debt | | | |
| Time to compute debt | | | |
| Flips at finish | | | |
| Flips − debt (tier) | | | |
| Orbits with split cycles / total | | | |
| "Done" orbits that failed the hidden check | | | |
| Deliberate swaps (instead of flips) | | | |
| Emergency almanac consulted? (Y/N) | | | |
| Footprint (approx. cm × cm) | | | |
| Time to solve | | | |

- Distinct from TWELVE TRIALS? In one sentence: ____
- Did "orbit" mislead again? ____
- Surprises / quotes:

## Out of scope

- **Clockmaker.** Task 4 makes it conditional on a completed 9-symbol standard solve. Attempt it only if deal 3 finishes with time and energy left.
- **Co-op, Silent Observatory, Pocket Orrery.** Later.
- **Tier recalibration.** Needs a solver (none exists) or several recorded deals. Collect numbers now.
