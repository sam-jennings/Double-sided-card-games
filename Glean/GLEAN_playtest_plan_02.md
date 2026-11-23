# GLEAN — Playtest Plan 02

*Pairs with the forthcoming `GLEAN_playtest_02.md`. Written per [playtesting.md](../.kiro/steering/playtesting.md). Hypotheses come from "What to test next" and the changes considered in [GLEAN_playtest_01.md](GLEAN_playtest_01.md), the caveats in [GLEAN_design_analysis.md](GLEAN_design_analysis.md) §5, and the `COLLECTION_OVERVIEW.md` outstanding questions. Numbered 02 to pair with the second session's report.*

## Open before the session

The changes playtest 01 adopted are in the rulebook. One proposal was deliberately not adopted, and there are two small text issues. Nothing blocks the session.

- **Applied:** Plunder is now proto-majority (1 point per claimed sign, max 9; the pip-sum version is retired with a note). The **"Sign is rank"** callout is in Components (B2 / F4). The **Closed Harvest** memory variant is documented.
- **Not applied, by decision:** playtest 01 named "face-up but not inspectable" harvests (option 2) as the sweet spot to test. The rulebook kept the **open, examinable harvest** as canonical, on the grounds that the dislike formed under Plunder, where the registry had no purpose. This session plays the canonical rule and asks the question afterwards (H6). Don't switch mid-match.
- **No counterweight for 9-dominance (B4).** By design: the report said to test majorities before treating it as a bug. H4 is that test.
- **No counting procedure for nine majorities.** The rulebook says "for each of the 9 signs, count…" but not how. **Session convention:** go sign by sign from Moon to Crown, each player calls their count aloud, and the scorer writes the claimant (or "deadlocked"). Time it.
- **Text issues (non-blocking, don't fix now):** the design footnote still says "untested at the table". Setup gives a 5-player deal, but the game record's `players` is `[3, 4, 6]`. Flag both for the catalogue owner.
- **Prototype:** playtest 01 used a letters A–I prototype, which caused the rank confusion. Use the **Nine Signs** print with pips 1–9.

## Setup

- **Game:** GLEAN
- **Version:** v1.0, **full majority scoring** (pip value to whoever gathers the most of each sign; ties deadlock). Open harvest.
- **Players:** 3. 12 cards each, 12 tricks a round. The design analysis recommends 3P: steepest skill gap, clearest contest/duck decisions.
- **Symbol subset:** all 9 signs / 36 cards.
- **Session shape:** **one full match**, three rounds. The first lead rotates clockwise, and scores are summed. About 10–12 minutes a round plus scoring, so ~40 minutes.
  - If a player is **new to GLEAN**, play one short **Plunder** round first as a teach, and don't count it. Returning players start straight on the match.
- **Why this session:** `next_step` is "test the intended majority scoring over a full match". Playtest 01 never reached majorities, so the real game, its main handling question (counting nine majorities) and the match structure that answers its deal-sensitivity are all untested.

## Hypotheses to test

Sim reference: [design analysis](GLEAN_design_analysis.md) §3, 4,000 rounds, seed 42. 3P all-skilled: **average score 12.4 of 45**, average round margin **22.6**, tie rate **2.5%**, first leader wins **28%** vs ~36% for the other seats. Skill edge **1.74×**; the strongest hand wins **51.9%** under all-random play (1.56×). Extra probe run for this plan (`glean_sim.py` bots, 3P all-skilled, 4,000 rounds, seed 42): **7.44 of 9 signs claimed** and **1.56 deadlocked** per round. Crown claimed in **81.5%** of rounds. The player who wins the most tricks wins the round outright **75.8%** of the time.

- **H1 — Nine majorities count quickly.** Design analysis §5 calls this the biggest open question. *Prediction:* each round's sign-by-sign count takes **≤ 2 minutes**, with no recount of any sign. *Falsified if* it takes over 3 minutes (playtest plan 01's red-flag line), or players flip through harvests repeatedly to settle signs. That would push the table towards Plunder and change the game's identity.
- **H2 — Majorities steer play during the round.** Overview: "does majority scoring play well?" *Prediction:* each round someone says a live majority aloud ("I need one more Crown", "Leaf's gone"). In the match, at least one sign is **deliberately deadlocked** to deny a rival. Expect ~1–2 deadlocks a round (sim 1.56). *Falsified if* nobody mentions a majority until scoring, i.e. the payoff is too deferred to steer play.
- **H3 — Scores land in the sim's shape.** *Prediction:* winning round scores are mostly **20–30**, losing scores well below, and **no round tie** (sim 2.5%). *Falsified if* scores bunch within a few points every round (majorities flatten the contest), or one player claims most signs every round (runaway).
- **H4 — Majorities dilute 9-dominance without killing trick-winning.** Playtest 01 B4. *Prediction:* the most-tricks player wins most rounds (sim 75.8%), but at least once a player **ducks a trick on purpose** and says why, and **sloughing** is used to place a card. *Falsified if* players call it "just win tricks" and never duck. Then the Plunder problem has survived into the real game and B4 needs a counterweight.
- **H5 — The match washes out the deal.** Design analysis §3.2 caveat. *Prediction:* after three rounds no player says the result was "decided at the deal". The match winner is not determined by round 1 alone; at least one round goes to a different player. *Falsified if* one player wins every round on visibly stronger hands, or a player feels shut out from round 1. Then The Passing should become the recommended default (a designer decision).
- **H6 — The open harvest earns its place under majorities.** Playtest 01 B3. *Prediction:* each round, players pick up or scan a rival's harvest at least once to count a sign, and afterwards nobody calls the public harvest "wrong". *Falsified if* the playtest-01 complaint ("removes the remembering skill") returns even with majorities live. Then test option 2 or Closed Harvest next.
- **H7 — Rank teaching sticks.** F4 / B2. *Prediction:* no player misunderstands which sign is high. *Falsified if* any play reveals the belief that two signs share a rank.

## What to watch

Handling first:

- **The 12-card hand.** Two faces, no natural sort, realigning every trick: the cross-game F1 problem BLIGHT hit at the same count. Note fumbles, dropped cards, and hands laid on the table to read.
- **Flip-to-follow.** Does the card a player flips to follow stay showing the led sign when placed? Is the hidden face ever exposed before the reveal?
- **The reveal.** Flipping every card in the trick at once: does anyone lose track of which cards followed and which sloughed? (Sloughs can't win.)
- **Harvest spread.** Do harvests stay readable as they grow to ~12 cards? Are examined cards returned as found?
- **Scoring physicality.** For each sign, players count cards carrying it on *either* face, so every harvested card has to be checked on both sides. Watch whether players flip each card, or read the hidden faces from memory (and get it wrong).

Then:

- **Leading.** Does the leader lead what they're long in, and does the table read it as information?
- **First-leader penalty.** Who leads round 1, and how do they do (sim 28% vs ~36%)?
- **Star/Crown card.** Who takes it, and does it decide two majorities at once?

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | Count ≤ 2 min per round, no recounts | > 3 min; repeated flipping through harvests |
| H2 | Live majorities said aloud; a deliberate deadlock | Majorities ignored until scoring |
| H3 | Winners ~20–30; no round tie | Bunched scores, or a runaway every round |
| H4 | A reasoned duck and a deliberate slough | "Just win tricks"; never duck |
| H5 | No "decided at the deal"; round wins spread | One player sweeps on stronger hands |
| H6 | Harvests consulted; no "feels wrong" | The playtest-01 complaint returns |
| H7 | Rank structure understood | Shared-rank misconception |
| Handling | 12-card hand handled; reveal clean | Hands laid down; follow/slough confusion |

## Teaching plan (retest: what to re-teach)

- Start with **Sign is rank**, read aloud from the Components callout: Crown is always 9, Moon is always 1, and every card carries two different strengths.
- Re-teach the **trick**: the shown face follows, the hidden face wins, and ties are impossible.
- Teach **majority scoring** with the playtest-plan-01 worked example. Put 3–4 cards on the table and show one card counting towards two signs. Then: ties deadlock, and the round maximum is 45.
- State the **match**: three rounds, the lead passes clockwise, scores summed.
- **Don't** read the strategy notes (ducking, counting the eights, deadlocking) before round 1. H2 and H4 test whether they're found. Reading them between rounds 1 and 2 is allowed; note it if you do.

## Record sheet

| | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| First leader | | | |
| Tricks won (A / B / C) | | | |
| Signs claimed (A / B / C) | | | |
| Signs deadlocked (which) | | | |
| Score (A / B / C) | | | |
| Most-tricks player won the round? (Y/N) | | | |
| Reasoned ducks / deliberate sloughs (count) | | | |
| Majorities said aloud during play (count) | | | |
| Rival harvests consulted (count) | | | |
| Counting time | | | |
| Round time | | | |

- Match total (A / B / C): ____ Winner: ____
- Did anyone say the deal decided it? Which round? ____
- Open harvest: right, or would a closed / no-inspect harvest be better? ____
- Majority scoring vs Plunder: which would you play again? ____
- Strategy notes read between rounds? (Y/N) ____
- Surprises / quotes:

## Out of scope

- 4P and 6P (and the off-record 5P deal).
- The Passing, Partners and Closed Harvest variants. Switching harvest rules is the next session's call, based on H6.
- Any 9-dominance counterweight until H4 has a result.
