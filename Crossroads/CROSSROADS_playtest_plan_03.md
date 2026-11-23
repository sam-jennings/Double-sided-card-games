# CROSSROADS — Playtest Plan 03

*Pairs with the forthcoming `CROSSROADS_playtest_03.md`. Written per [playtesting.md](../.kiro/steering/playtesting.md). Hypotheses come from the "Next session must answer" list in [CROSSROADS_playtest_02.md](CROSSROADS_playtest_02.md), the open items in [CROSSROADS_tasks.md](CROSSROADS_tasks.md) Phases 1–5, [CROSSROADS_design_analysis.md](CROSSROADS_design_analysis.md) §6–§7, and the `COLLECTION_OVERVIEW.md` outstanding questions. Numbered 03 to pair with the third session's report.*

## Open before the session

The rulebook is **behind the settled design**, and its own banner says so. None of the changes called for since playtest 01 has been written into the rules text. The session runs on the banner's interim instructions plus the conventions below. Don't edit the rules before the report.

- **v1.2 not written.** The body still says **deal 14**, "your rival's hand is exactly the rest" (perfect information), and keeps **Toll Roads as a variant**. The banner says: deal 9, score Tolls, partial information. **Session convention:** deal **9 roads each**, set the other **10 aside** without looking, and score with **Toll in the base game**. Apply the pie rule (higher pip total chooses who goes first) to the 9-card hands.
- **End trigger undecided (Bug 2, HIGH, flagged twice).** The rulebook still ends on two consecutive passes. Tasks Phase 3 (the eighth-dim trigger sim) is not done. **Session convention:** play to the written double-pass end, but **stop and score a snapshot the moment the eighth city dims** (photo plus a written score), then play on to the double pass. This tests both triggers on one game without changing a rule.
- **Layout convention not formalised** (playtest 01 change 1, Phase 5 unpicked). **Session convention:** the playtest-01 organic layout. The road card touches its source city and shows its destination face.
- **Equal deal not reinforced** (playtest 01 change 2). Count both hands to 9 aloud before looking.
- **No denial strategy note** (Phase 1 remaining item, the real onboarding lever per lesson 6(a)). It isn't in the strategy notes. Leave it untaught for duel A (H4 tests whether denial is found unprompted).
- **Not a rules gap, but stale:** the design footnote still says "untested at the table" and "perfect information is embraced". Ignore it this session.

## Setup

- **Game:** CROSSROADS
- **Version:** v1.1 rules + the banner's v1.2 interim (deal 9, 10 aside, Toll in base) + the conventions above.
- **Players:** 2. On-spec at last: playtest 02 drifted to 3P and never used flips.
- **Symbol subset:** 9 symbols / 36 cards: the 8 symbol-9 cards form the city ring (all lit), plus 28 roads.
- **Session shape:** two duels, ~20 minutes each.
  1. **Duel A — honest duel.** Both players play to win. Signal Fires in full use.
  2. **Duel B — the pass probe.** One player (**the passer**) builds nothing and passes every turn. The other (**the builder**) plays to win and is told the passer's plan. Swap who goes first. Score it **twice**: with Toll (the session rule) and without Toll (v1.1 base). The second score tells us whether deal-9 alone would have fixed pass-to-win.
- **Why this session:** `next_step` is "run a proper 2-player Signal Fires test and probe pass-to-win". CROSSROADS has had two sessions and **neither has tested the flip economy**. Playtest 02's verdict put the game on notice until pass-to-win is tested in proper 2P play.

## Hypotheses to test

Sim reference: §7 tables, plus a probe of the exact session configuration run for this plan (`crossroads_sim.py`, 2P, H=9, `shared:8`, 300 games, seed 42).

| 2P, deal 9, Signal Fires | passer wins | passer fulfilled | builder fulfilled |
|---|---:|---:|---:|
| no Toll vs **naive** builder (never denies) | **74.3%** | 3.98 | 2.35 |
| no Toll vs **greedy** builder (denies) | 1.3% | 0.09 | 1.43 |
| **Toll** vs naive builder | **7.3%** | 4.15 | 2.35 |
| Toll vs greedy builder | 0.0% | 0.08 | 1.32 |

Greedy mirror with Toll, same probe: the pool empties in **100%** of games, which last **18.4 turns**, with **5.3 turns** played after the eighth dim. §7 density at H=9: **4.0 builds, 5.0 kept, 2.8 fulfilled** per player, **66%** of city pairs connected.

- **H1 — "Eight flips ache."** The original first-table question, never tested. *Prediction:* in duel A at least one flip decision visibly takes 30+ seconds, a player mentions "the last flip", and no flip is spent before turn 3 without a stated reason. *Falsified if* flips are spent casually or declined as "more confusion" again (playtest 02). That means the flip economy is overhead, not tension.
- **H2 — Dimming reads at a glance.** *Prediction:* nobody counts the cities aloud or asks "how many flips are left?". Remaining flips are read off the ring. *Falsified if* players recount more than once a duel or misread lit vs dim.
- **H3 — Nine cards is comfortable, not thin.** Bugs 3–4 and the §7 table question. *Prediction:* each player fulfils **2–4 contracts** in duel A (sim 2.8), the first move takes **< 1 minute**, and neither player says the network feels thin. *Falsified on the thin side if* someone fulfils ≤ 1, or players say there is nothing to do. **H=10 is the documented fallback** (3.8 fulfilled, 74% connected). *Falsified on the heavy side if* 9 still feels overwhelming. That would move the problem from hand size to the two-faced hand itself.
- **H4 — Denial is found, and pass-to-win dies at the table.** Bug 1, CRITICAL. *Prediction:* in duel B the passer **loses on Toll scoring** (sim 0–7%). The builder **spends ≥ 3 of the 8 flips** reversing roads the passer needs. The builder also beats the passer on the **no-Toll** count, which means they denied (sim 1.3%) rather than built naively (74%). *Falsified if* the passer wins the Toll count (Toll doesn't fix it at the table), or wins the no-Toll count while the builder never flips against them (the playtest-02 naive line returns and denial isn't findable).
- **H5 — The eighth dim is a natural end.** Bug 2. *Prediction:* the double pass comes **within ~5 turns** of the eighth dim (sim 5.3). Nobody feels trapped watching the other build, and the **snapshot winner equals the final winner** in both duels. *Falsified if* the post-dim tail runs 8+ turns, or one player is clearly ready to stop while the other keeps scoring, or the snapshot and final winners differ. Then post-dim building is where the asymmetry lives.
- **H6 — Toll scoring isn't fiddly.** Phase 1 table item. *Prediction:* tracing each fulfilled contract's shortest route and counting your own roads takes **≤ 2 minutes per player**, with no dispute over which route is "shortest". *Falsified if* scoring takes longer than the last five turns did, or two routes of equal length are argued over.

## What to watch

Handling first:

- **Reading a flipped road.** After a flip, does the road show its new destination unambiguously under the organic layout? Or does a road touching its *old* source now point away from where it touches? Log every misread facing.
- **Dimming.** Is a sideways city card ever mistaken for a lit one, or knocked straight?
- **Ownership for Toll.** Toll needs to know **who built each road**, and nothing on the table records it. Watch whether players remember, argue, or invent a marker (e.g. nudging roads towards the builder's side). This is the likeliest new handling bug. Record it, don't fix it.
- **The aside pile.** The 10 set-aside roads must never be looked at. Keep them squared and rotated, apart from the play area, and note any temptation to check them ("does that road exist?").
- **Hand handling.** Nine two-faced cards: is the hand read on both sides comfortably? Do players sort it into "contracts I'm keeping" and "roads to build" (the shortcut from playtest 01)?

Then:

- **Ko.** Is it applied without prompting?
- **Who owns the eighth flip**, and does the first-move choice look informed?
- **Last-flip destruction.** Does a contract broken by a late flip read as exciting or as feel-bad?

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | An agonised flip; "the last flip" said aloud | Flips casual, or declined as confusion |
| H2 | Remaining flips read off the ring | Recounting; lit/dim misread |
| H3 | 2–4 fulfilled each; first move < 1 min | ≤ 1 fulfilled ("thin") or still overwhelming |
| H4 | Passer loses the Toll count; builder flips ≥ 3 against them | Passer wins on Toll, or wins no-Toll with zero denial |
| H5 | Double pass ≤ ~5 turns after the eighth dim; same winner at snapshot and end | Long tail; trapped player; winners differ |
| H6 | Toll counted ≤ 2 min/player, no disputes | Slow, or route/builder disputes |
| Handling | Every facing read correctly after flips | Misread flipped roads; builder identity lost |

**Verdict framing:** this is the test playtest 02 put CROSSROADS on notice for. If H4 holds, pass-to-win is closed at the table and the v1.2 rewrite (deal 9 + Toll) is safe to write. Its end trigger can follow from H5. If H4 fails on the Toll count, the sim's fix doesn't survive humans, and the collection status question returns to the designer.

## Teaching plan (retest: what to re-teach)

- Re-teach the **interim deal** before anything else: 9 each, 10 aside unseen. Say that you **don't** know your rival's hand, which retires the old perfect-information pitch.
- Re-teach **contracts = kept cards** and **Toll**: each fulfilled contract scores 1, plus 1 for every road *you built* on its shortest route. Do one worked example on the table before turn 1.
- Re-teach **Signal Fires and ko** together. Every flip dims a city, eight in all, and you may not flip back the road your rival just flipped.
- Don't use the playtest-02 ramp (flips off for the first turns). The flip economy is the subject of this test.
- **Don't** mention denial before duel A (H4). Brief the duel B builder only with "your opponent will pass every turn".

## Record sheet

| | Duel A (honest) | Duel B (pass probe) |
|---|---|---|
| First player (chooser / chosen) | | |
| Turns total / turn of the eighth dim | | |
| Flips spent by each player (P1 / P2) | | |
| Builder flips spent against the passer | n/a | |
| Longest flip deliberation (approx. s) | | |
| Recounts of remaining flips | | |
| Builds / kept / fulfilled (P1) | | |
| Builds / kept / fulfilled (P2) | | |
| Toll bonus (P1 / P2) | | |
| **Snapshot score at the eighth dim** (P1 / P2, Toll) | | |
| **Final score** with Toll (P1 / P2) | | |
| Final score without Toll (P1 / P2) | | |
| Winner: snapshot / final with Toll / final without Toll | | |
| Toll scoring time | | |
| Misread flipped roads / builder-identity disputes | | |
| First-move time | | |
| Time | | |

- Did anyone say "the last flip"? Context: ____
- Nine cards: thin, right, or still too many? ____
- Did either player feel trapped at the end? ____
- Surprises / quotes:

## Out of scope

- 3P and 4P. The unified ruleset supports them, but this session owes the 2P questions.
- Choosing a Phase 5 layout (Dual-rail, Harbour columns). Log layout pain only.
- Deal-split, the draw model and the open-draft variant: rejected or parked in the design analysis.
- Caravans and The Long Haul variants.
