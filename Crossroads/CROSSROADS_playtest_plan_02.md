# CROSSROADS — Playtest Plan 02

*Pairs with the forthcoming `CROSSROADS_playtest_02.md`. Written per [playtesting.md](../.kiro/steering/playtesting.md).*

## Setup

- **Game:** CROSSROADS
- **Version:** v1.1 — **full rules, Signal Fires enabled** (this is the change from playtest 01, which deliberately disabled flips).
- **Players:** 2
- **Symbol subset:** 9 symbols / 36 cards (8 symbol-9 cards become the cities; 28 roads, 14 each). Playtest 01 refuted the 7-symbol configuration as too sparse — do **not** retest it.
- **Why this session:** Playtest 01 confirmed the core connection mechanic at 9 symbols but could not touch the recorded first-table questions, because flips were off. The whole point of v1.1 — the Signal Fires flip economy — is still **untested at the table**. This session is the first table contact with flips. It is the rung-1 priority per [focus-priority.md](../.kiro/steering/focus-priority.md).

## Hypotheses to test

The two recorded first-table questions ([COLLECTION_OVERVIEW.md](../COLLECTION_OVERVIEW.md), echoed in the rulebook footnote), framed as falsifiable predictions, plus two carried-forward bugs from playtest 01.

- **H1 — "Eight flips ache."** *Prediction:* by roughly the midpoint, both players are visibly reluctant to spend a flip, and at least one flip decision is agonised over because spending it now forfeits the last-flip endgame. *(`physical-handling.md`: flips are paid by dimming cities — contested visible tempo.)*
- **H2 — "Dimming reads at a glance."** *Prediction:* players track remaining flips by glancing at the ring (lit vs sideways cities) without recounting or asking "how many flips are left?"
- **H3 — Banked-contract behaviour survives flips.** Playtest 01 found players set aside already-fulfilled contracts as a cognitive shortcut. *Prediction:* with flips live, a single reversal does **not** so destabilise both hands that the shortcut collapses and tracking becomes overwhelming. *(This is the "instability of banked contracts" concern raised but untested in playtest 01.)*
- **H4 — The double-pass end trigger is the live problem, not flips.** Playtest 01 flagged asymmetric readiness-to-end as a high-severity bug. *Prediction:* with the flip economy forcing a natural exhaustion point (all eight cities dim), the end now arrives cleanly and the double-pass unfairness is reduced or gone.

## What to watch

- **Flip hoarding vs spending.** The sim's second-mover advantage came from *myopic* bots that always spent greedily; [CROSSROADS_design_analysis.md](CROSSROADS_design_analysis.md) §5 explicitly flags that humans who hoard will shift this. Watch whether players hoard, and who owns the eighth (final) flip.
- **Last-flip destruction at the whistle.** Playtest 01's central worry: a critical road flipped on the final move collapsing contracts. Watch whether this reads as exciting conflict or feel-bad arbitrariness.
- **First-turn paralysis** (playtest 01 medium bug): does the opening still feel arbitrary, or does experience / the flip economy give it an anchor?
- **The layout convention** that emerged organically in playtest 01 (card touches source city, shows destination face) — confirm it still holds with flips reversing facings, and whether a flipped road's new facing is unambiguous.
- **Ko rule** comprehension — does "can't reflip the road they just flipped" get applied correctly without prompting?

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | At least one visibly agonised flip decision; players reference "the last flip" | Flips spent without thought; pool feels like a formality |
| H2 | Remaining flips read off the ring at a glance, no recounting | Players repeatedly recount or lose track of dim count |
| H3 | Set-aside shortcut survives; tracking stays manageable | A reversal cascades; players give up tracking, game stalls in confusion |
| H4 | Game ends cleanly near eighth dim; no one feels trapped watching the other build | Asymmetric readiness recurs; double-pass still feels unfair |
| Handling | Flipped roads read unambiguously; dimming is glanceable | Reversed facings confuse; dim/lit hard to distinguish |

## Teaching plan

- Teach the **board-from-deck** reveal first (eight symbol-9 cards → ring, 9-face down) — it's the game's signature and an easy hook.
- Teach builds and routes with flips **off** for the first 2–3 turns, then introduce Signal Fires once routes are understood. (Playtest 01 already validated that the no-flip core teaches cleanly.)
- Offer **Caravans** (direction-blind) only if a player struggles with directed routes — but note the session's value is in the *directed + flip* game, so prefer to push through.
- **Watch during teaching:** whether "keeping a card is a contract" lands, and whether directed-route scoring (reachable either direction) is grasped before the first flip.

## Out of scope

- 7-symbol play (refuted, playtest 01).
- Toll Roads / Long Haul variants — only if a clean v1.1 game completes with time to spare.
