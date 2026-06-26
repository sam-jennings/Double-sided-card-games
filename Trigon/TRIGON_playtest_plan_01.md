# TRIGON — Playtest Plan 01

*Pairs with the forthcoming `TRIGON_playtest_01.md`. Written per `.kiro/steering/playtesting.md`.*

## Setup

- **Game:** TRIGON
- **Version:** v1.2 (balanced over ~23k simulated games; never tabled).
- **Players:** 2 (the testable count per `focus-priority.md` rung 2 — 18 turns each, full deck).
- **Symbol subset:** all 9 signs / 36 cards.
- **Why this session:** TRIGON is the collection's flagship and is extensively sim-tuned but has had **zero plays**. `playtesting.md` is explicit: a first table test outranks more simulation. This is the first human contact. Numbers are not the question here — feel, drama, and teachability are.

## Hypotheses to test

The recorded first-table questions live in the game's design analysis §7 (reproduced in `COLLECTION_AUDIT.md`, as the Overview treats TRIGON as a finished benchmark). Framed as falsifiable predictions:

- **H1 — Capture cadence feels good, not exhausting.** Sim shows roughly a capture every ~5 turns / ~19 cards captured per game. *Prediction:* players experience captures as periodic payoffs, not a relentless grind, across an 18-turn-each game.
- **H2 — No ability is dead weight.** *Recorded question: "does anyone use Aurora?"* — note: **"Aurora" is a legacy sign name not present in v1.2's nine signs** (Moon/Leaf/Wave/Flame/Eye/Mask/Key/Star/Crown); this is a stale-terminology artifact worth flagging back into the docs. The live, testable form: *Prediction:* every one of the nine abilities gets activated at least once across a couple of games; no sign is so situational that a thoughtful player never fires it.
- **H3 — "Active player captures everything" is dramatic, not theft.** *Prediction:* when a player completes a line that an opponent's placements mostly set up, the table reads it as a satisfying swing, not as a feel-bad rules-gotcha.
- **H4 — Charging vs re-charging teaches itself within one game.** *Prediction:* by mid-first-game, players correctly judge which cards are charged (just placed / flipped / moved / requirement newly met) without re-reading the rule each turn.

## What to watch

- **Declining activations.** Sim found ~3/4 of skilled activations are *declined* — "the board you leave matters more than the action you take." Watch whether humans discover this or over-activate and feed the opponent.
- **The deck-top-is-public rule.** Does the table actually use the known top card to plan, or ignore it?
- **Chain resolution flow.** Long chains are legal and self-limiting, but watch for *handling* friction: losing track of which cards are charged mid-chain, or disputes over resolution order. This is the most likely handling bug.
- **Hidden-side memory.** Eye formalises peeking, but the strategy notes say "attention is free." Watch whether players strain to remember placed-card hidden faces — a flagged risk for this deck (`physical-handling.md`).
- **Grid-full discard** comprehension once the 3×3 fills.

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | Captures land as periodic highlights; no "are we done yet" at turn 12 | Captures feel constant/mechanical, or droughts make turns feel pointless |
| H2 | All nine abilities fire across the session | One or more signs never worth activating |
| H3 | Audible "oh no / nice" on a stolen line | "That's not fair" — feels like theft, not tactics |
| H4 | Charge state judged unaided by mid-game | Players re-read charging rule every turn; disputes persist |
| Handling | Chains resolved without losing the board state | Mid-chain confusion over charge/order; needs a referee |

## Teaching plan

- Open with the **sign reference table** visible to both — it's billed as the only mid-game reference.
- Teach the turn loop (draw → place a face → resolve) before any ability detail; let the first capture happen, then introduce activations.
- **Use the Calm Signs variant for the first game** (Star is *not* wild) — the rulebook stages it for first teaches; it slows captures and lets charging/chaining be learned before the wild accelerant is added. Switch to full v1.2 (Star wild) for game two.
- **Watch during teaching:** the moment the "active player always captures" rule is stated — does it land as a warning ("be careful what you leave") or get forgotten until it bites someone (H3 signal).

## Out of scope

- 3–4P play (needs more players; this session is the 2P first contact).
- Re-tuning balance — sim has covered the numbers; do not re-sim to avoid the table (`playtesting.md`).
- Deep Signs / Shared Glory variants unless a clean game finishes with time to spare.
