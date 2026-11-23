# CONCORD — Playtest Plan 01

*Pairs with the forthcoming `CONCORD_playtest_01.md`. Written per `.kiro/steering/playtesting.md`. Hypotheses come from the first playtest plan in [CONCORD_design_proposal.md](CONCORD_design_proposal.md) §7, which this file expands rather than replaces.*

## Open before the session

No rule gap blocks a first session. Three small things to settle before sitting down:

- **Counters.** The game needs 4 generic counters (2 Amendments each); they are not part of the deck. Bring coins or tokens.
- **Rules handout.** There is no separate rulebook; the playable rules are §4 of the design proposal. Print or open that section only, so players don't read the candidate-concept discussion.
- **Dealing the six.** "Deal the next 6 cards face-up, preserving the faces dealt" can be read as "slide each card off showing its deck-top face" or "turn it over as you deal". Either is random; agree on **slide, don't turn** so the dealt face is the one everyone just saw.

## Setup

- **Game:** CONCORD
- **Version:** working prototype v0.1 (score scale sanity-checked on random holdings; not simulated with strategic play; never tabled).
- **Players:** 2 (the only count).
- **Symbol subset:** all 9 signs / 36 cards. Six rounds of 6 cards; each player Divides 3 times and Chooses 3 times and ends with 18 cards.
- **Configuration:** 2 Amendment counters each, 3/2 scoring, one ratification per player per round — exactly the base rules. No variants in game 1.
- **Why this session:** `next_step` is "run the first physical prototype and test cognitive legibility". The proposal names legibility, not balance, as the main risk: the game only works if players can scan their loose bonds and judge a six-card cut without turning every round into a graph search. Use the plainest glyph set available (Set D Glyphs).

## Hypotheses to test

The proposal's seven questions (§7), framed as falsifiable predictions:

- **H1 — Cutting is the main skill.** *Prediction:* the Divider builds two genuinely competing lots most rounds, not "three good, three bad". *Falsified if* the Chooser's pick is obvious in 4+ of the 6 rounds — this is a **fast falsification gate** (see below).
- **H2 — The compulsory flip shapes the cut.** *Prediction:* players can name a purpose for most flips (bait, repair, or sabotage). *Falsified if* flips are mostly made at random or "on whatever doesn't matter".
- **H3 — Triangles can be recognised without full re-sorting.** *Prediction:* after round 2, players find their candidate triangles in well under a minute without spreading and regrouping the whole Workshop. *Falsified if* evaluating a cut needs an exhaustive, slow triangle search every round — the second **fast falsification gate**.
- **H4 — One ratification per round creates useful commitment.** *Prediction:* at least once per game a player deliberately leaves a ratifiable triangle loose to keep its cards for a better one. *Watch for the failure:* frustration when two or more Concords are ready late and only one window remains.
- **H5 — Two Amendments are scarce.** *Prediction:* counters are spent deliberately, not automatically on the first two repairable triangles; at least one player ends with an Amendment unspent or spends one after round 4.
- **H6 — The score reflects decisions, not offer luck.** *Prediction:* each player can name one cut or choice they regret and say how it changed the result.
- **H7 — Footprint stays readable.** *Prediction:* each Workshop plus ratified Concords fits a normal half-table and stays legible to the opponent at all times.

**Score expectation (rough, not a hypothesis gate).** The proposal's random-holding check gives ~3.3 visible Concords per 18 cards with 2 Amendments under optimal end-grouping. If roughly half are natural, that is ~8 points. Sequential locking should pull scores below that; strategic drafting may push them either way. Record the actual numbers.

## What to watch

Handling first:

- **Accidental flips in the Workshop.** Orientation is scoring state, and loose cards may be picked up and inspected "then returned as found". With 18 loose cards and a lot of inspection, watch for cards returned the wrong way up — and whether anyone notices. If it happens, it is a handling bug, not a player error.
- **Offer inspection.** Both players may inspect both faces of the six offered cards. Watch whether that slows the cut (picking up every card) and whether cards are reliably returned as found.
- **Ratified vs loose.** Locked Concords must stay visibly separate from the Workshop. Watch for a ratified card drifting back into the loose area.
- **The Amendment flip.** Confirm players find the single repair card without trial-and-error. (Verified for this plan: of the 8 orientations of a triangle, 2 are valid and each of the other 6 has exactly one repairing flip.)

Then:

- **Analysis paralysis.** Time the Divide step every round. Rising times with a growing Workshop is the H3 failure in slow motion.
- **Denial play.** Does anyone take or split a lot to deny the other player a unique bond they need? That is the pair-uniqueness interaction the design claims.
- **Tiebreak.** Note whether the breadth tiebreak is ever needed.

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | Chooser hesitates; picks are split between lots | Pick obvious in 4+ rounds (**gate: redesign**) |
| H2 | Flips have a stated purpose | Flips feel random or token |
| H3 | Triangles found by scanning; Divide step stays under ~2 min | Exhaustive re-sorting every round (**gate: redesign**) |
| H4 | A ready triangle is deliberately held at least once | Late frustration with stacked-up ratifications |
| H5 | Counters spent late or kept | Both spent on the first two triangles |
| H6 | Each player names a decisive regret | "It came down to the deal" |
| H7 | Both Workshops readable at a glance | Players lose track of their own loose cards |
| Handling | No mis-returned faces | Any card's orientation silently changed |

Per the proposal: if either gate fails, **cut or structurally redesign**. If triangle recognition works but timing is awkward, the flip matters but two counters feel wrong, or ties are frequent, **iterate**.

## Teaching plan

- Use the proposal's teaching script verbatim, then **lay out one real triangle and one non-triangle** before round 1.
- Demonstrate an Amendment on that triangle: show it wrong, flip the one card, show it right.
- Teach the Divider's flip as part of the offer — "your cut includes one turned card".
- **Watch during teaching:** whether "AB, AC, BC" lands from the example or needs a second demonstration. Needing a second demo is an H3 warning, recorded as such.
- No variants in game 1. If the base loop works and there's time, a second game may try **Open Ratification** (tests whether the one-per-round limit adds value). Leave One Amendment, Four-card Cut and Silent Cut for later.

## Record sheet

| Round | Divider | Divide time | Lot taken (A/B) | Was the pick obvious? (Y/N) | Flip purpose (bait / repair / sabotage / none) | Ratified this round (P1 / P2, natural or amended) |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |

| | Player 1 | Player 2 |
|---|---|---|
| First Divider? (Y/N) | | |
| Natural Concords (×3) | | |
| Amended Concords (×2) | | |
| Final score | | |
| Different signs in Concords (tiebreak) | | |
| Amendments spent (round) | | |
| Loose cards at end | | |
| One regretted cut or choice | | |

- Teach time: ____ Total play time: ____ (target 25–35 min)
- Mis-returned or accidental flips: ____
- Surprises / quotes:

## Out of scope

- All variants except possibly Open Ratification in a second game.
- Point-value or counter-count tuning — collect observations this session; tune later.
- Strategic simulation — the proposal's maths is a sanity check only, and the table is the priority.
