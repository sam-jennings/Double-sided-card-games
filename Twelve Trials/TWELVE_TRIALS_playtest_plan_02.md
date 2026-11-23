# TWELVE TRIALS — Playtest Plan 02

*Pairs with the forthcoming `TWELVE_TRIALS_playtest_02.md`. Written per `.kiro/steering/playtesting.md`. Hypotheses come from the open questions in [TWELVE_TRIALS_playtest_01.md](TWELVE_TRIALS_playtest_01.md), the active tasks in [TWELVE_TRIALS_tasks.md](TWELVE_TRIALS_tasks.md) and the `COLLECTION_OVERVIEW.md` entry. Numbered 02 to pair with the second session's report.*

## Open before the session

One gap blocks the session's main purpose; two are small.

- **The rulebook still uses the tracking method that failed.** v1.1 marks a flip by turning the card sideways, which is exactly what playtest 01 found does not survive constant regrouping (bug 2). No replacement has been chosen; `next_step` and task 1 both ask for one to be trialled. **For this session, trial the penny/token method first** (one coin on each flipped card, coin travels with the card). It is the only task-list candidate that survives movement *and* keeps the Duel/replay restore. If tokens slip off during regrouping, switch to the **tally sheet** for the second solve. This is a test condition, not a rules change; the rulebook stays as it is until the report.
- **Workspace convention.** Not in the rules. Lay out three zones before dealing (task 3): **pool** (centre), **staging** (candidate trios, one side), **almanac row** (set-aside trios, far edge). Mark them with paper strips if it helps.
- **Player-count mismatch (non-blocking).** The game record says `players: [1, 2, 3]`; the rulebook banner says "1–2 players (plus a table co-op mode)" and Round the Table says 2–5. Irrelevant to a solo session; flag for the catalogue owner.

## Setup

- **Game:** TWELVE TRIALS
- **Version:** v1.1 rules, with tokens (then tally) substituted for sideways marking as the session's test condition.
- **Players:** 1 (solo).
- **Symbol subset:** all 9 signs / 36 cards; 12 trios.
- **Session shape:** two solves, ~15–25 minutes each.
  1. **Solve A — scored.** Fresh deal, tokens, zones, flips counted from first card to declaration.
  2. **Solve B — completion mode.** Fresh deal, no scoring at all (task 4). Keep tokens on anyway, silently, so the flip count is still known afterwards.
- **Before each solve: photograph the deal** from above. It is the audit trail for the token count and lets the deal's true optimum be computed afterwards (transcribe each card's starting face and pass it to `optimal()` in [twelve_trials_sim.py](twelve_trials_sim.py)).
- **Why this session:** `next_step` is "retest the tracking method and workspace convention". Playtest 01 also left H1 open because flip-counting was abandoned mid-solve, so a full counted solve is the other priority.

## Hypotheses to test

- **H1 — A thoughtful solve lands near 7 flips.** Solver average over 2,000 deals is **5.29**; picking any almanac without optimising averages **8.97** ([design analysis](TWELVE_TRIALS_design_analysis.md) §3). *Prediction:* Solve A ends at **6–8 flips** (Silver or a high Bronze). *Falsified if* it ends at 9+ (no better than not optimising: the search isn't reaching players) or at ≤5 without effort (tiers too loose; compress them). Compare against the photographed deal's exact optimum, which can sit ±2 from 5.3.
- **H2 — Tokens survive regrouping.** *Prediction:* at declaration, the number of tokens equals the flips actually made (checked against the photo), and no token was knocked off or left behind. *Falsified if* any token is lost or misattributed, or if keeping them on slows regrouping enough that you want to stop using them.
- **H3 — Zones cut the sprawl.** Playtest 01 bug 1 (high): cards were in near-constant motion across many ad-hoc groups. *Prediction:* the whole solve fits inside a ~60 × 90 cm area, and cards move pool → staging → almanac row more than they move sideways between ad-hoc piles. *Falsified if* the zones are abandoned within ten minutes or you rebuild your own groupings anyway.
- **H4 — Flip-counting is kept up to the end.** Playtest 01 bug 3: counting was dropped to focus on completion. *Prediction:* with tokens doing the counting, Solve A is counted to the end without effort. *Falsified if* the urge to stop counting returns: then scoring itself, not the tracker, is the overhead.
- **H5 — Unpicking an early lock happens and pays.** The design's skill is choosing among 840 almanacs. *Prediction:* at least once in Solve A you pull apart a set-aside trio to rescue the last few, and it lowers the final count. *Falsified if* trios are never unpicked (the depth stays invisible) or unpicking feels like punishment.
- **H6 — Completion mode still has teeth.** *Prediction:* Solve B is still challenging without scoring, and you would recommend it as a first-play mode. *Falsified if* it feels trivial (scoring is the game) or it feels identical to Solve A (the mode adds nothing).

## What to watch

Handling first:

- **Token behaviour during regrouping.** Does a token ride on the card when you slide it, or fall off? Do you lift tokens to examine a card and put them back on the wrong card?
- **Examine-and-return.** The rule is "return exactly as found". With tokens instead of rotation, rotation no longer carries state, so a card returned crooked is harmless. Note whether this frees up handling.
- **Footprint.** Note the real area used and whether the almanac row grows to unreadable length (12 trios × 3 cards).
- **Verification.** Checking a trio means looking at three hidden faces. Note whether it's still quick once trios are stacked in the almanac row.

Then:

- **Seasons.** Playtest 01's discovery was that trios assemble into four seasons of three. Does that happen again, and does it speed the solve?
- **Time.** Rulebook says ~15 minutes. Time both solves.

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | 6–8 flips, near the deal's optimum + 2 | 9+ flips, or ≤5 with no struggle |
| H2 | Token count matches the photo audit | Lost, moved or misattributed tokens |
| H3 | Zones kept; footprint fits ~60 × 90 cm | Zones abandoned; sprawl returns |
| H4 | Counting kept to the end without effort | Counting dropped again |
| H5 | An early lock unpicked and it helps | No unpicking, or it feels punitive |
| H6 | Completion mode is a fair first-play mode | Trivial, or no different from scored |
| Handling | No tracking state lost | Any flip miscounted |

If H2 fails with tokens **and** with the tally, the tracking problem is structural: record it and leave the design question to the designer (candidates in the tasks list: a flip-queue zone, or dropping scoring as default).

## Teaching plan (retest — what to re-read)

- Re-read only **What you're building** and the **one-flip law** ("any trio is perfect as dealt or fixable by flipping exactly one card").
- Ignore the sideways-marking sentences; tokens replace them for this session.
- Don't re-read the strategy notes before Solve A. H5 tests whether unpicking is found, not taught.

## Record sheet

| | Solve A (scored) | Solve B (completion) |
|---|---|---|
| Tracking method | tokens / tally | tokens / tally |
| Deal photographed? (Y/N) | | |
| Flips at declaration | | (silent count) |
| Exact optimum for this deal (computed later) | | |
| Tier | | n/a |
| Trios set aside, then unpicked (count) | | |
| Tokens lost / misplaced | | |
| Zones kept to the end? (Y/N) | | |
| Footprint (approx. cm × cm) | | |
| Time to declare | | |
| Seasons noticed? When? | | |

- Did you want to stop counting at any point? When and why: ____
- Would you teach completion mode first? ____
- Surprises / quotes:

## Out of scope

- Duel and Round the Table (co-op) modes. Retest them once tracking is settled.
- Changing tier thresholds: only after H1 has a counted result.
- New simulation. The solver is exact; the questions are physical.
