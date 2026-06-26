# CAIRN — Playtest Plan 01

*Pairs with the forthcoming `CAIRN_playtest_01.md`. Written per [playtesting.md](../.kiro/steering/playtesting.md).*

## Setup

- **Game:** CAIRN
- **Version:** v0.1 (sim-validated; never tabled). See [CAIRN_rulebook.md](CAIRN_rulebook.md) and [cairn_sim.py](cairn_sim.py).
- **Players:** 1 (solo). Always fieldable — no scheduling constraint.
- **Symbol subset:** standard game = **7 signs / 21 cards** (signs 1–7; Star and Crown set aside). Three cairns, hand of four.
- **Session shape:** one sitting of **6–8 deals**, because each is ~10 minutes and the questions are about the *repeated* feel, not a single solve:
  1. **1 deal — First Trail** (4 cairns) to learn the flow.
  2. **3–4 deals — standard** (3 cairns, hand 4): the configuration under test.
  3. **1 deal — Pathfinder** (hand 3) to feel the tightening.
  4. **1 deal — The Long Trail** (9 signs, 3 cairns, hand 5) to sanity-check the expert variant exists and isn't pure luck.
- **Why this session:** CAIRN is the collection's first *contained* solo game — the answer to "I can't sprawl TWELVE TRIALS or THE ORRERY on a train table." The sim has already cleared the structural and skill-accessibility gates (careful play approaches the clairvoyant ceiling at 7 signs). What simulation cannot answer is whether the per-turn chaining decision is **fun** or merely **arithmetic**, and whether a loss feels **earned**. First contact.

## Calibration from the sim (what "normal" looks like)

At 7 signs / 3 cairns / hand 4, [cairn_sim.py](cairn_sim.py) measured clear rates of roughly: random **~41%**, casual counting play **~74%**, careful planning **~98%**. So:

- A thoughtful human should **clear most standard deals**, losing occasionally.
- A learning player losing *most* standard deals is a red flag — teaching or hand size is wrong, not the player.
- Depth-2 lookahead matched deep search, so **planning two moves ahead should be enough** to play well. If the player feels they'd need to see the whole stock to make decisions, that's a finding.

## Hypotheses to test

Framed as falsifiable predictions, drawn from the rulebook's open questions:

- **H1 — The chaining choice is a real decision, not arithmetic.** *Prediction:* on most turns the player visibly weighs *which* cairn to feed / *which* sign to expose, and can articulate a reason ("I'll keep Flame alive", "that guarantees my next card lands"). At least a few "good move" satisfaction beats per session. *(Failure: the player plays on autopilot, reports it feels like sorting/bookkeeping, or says "there was only ever one thing to do".)*
- **H2 — Getting blocked reads as a foreseeable mistake.** *Prediction:* when a deal is lost, the player can point back to a turn where a different play would have helped ("I shouldn't have stranded that cairn on Key"). *(Failure: losses feel arbitrary — "the draws just killed me" — which would mean draw-luck dominates at the table even though the sim says skill is reachable.)*
- **H3 — A hand of four is the right size.** *Prediction:* four cards gives a genuine choice most turns without making blocking almost impossible; the standard game wins comfortably but not automatically. *(Failure: four feels either starved — constant forced plays — or trivial — never any danger. Pathfinder/First Trail comparisons calibrate this.)*
- **H4 — The free look is discovered and used.** *Prediction:* the player notices the stock's visible top and begins steering placements to match the sign they can see coming, without being told. *(Failure: the peek goes unnoticed or unused, suggesting it needs to be promoted in the rules or surfaced as an explicit step.)*
- **H5 — The footprint is genuinely tray-sized.** *Prediction:* the whole game (three growing cairns + a held fan + stock) fits a train tray / lap, including The Long Trail. *(Failure: cairns creep, the hand is awkward to hold and read, or it wants more table than a TWELVE TRIALS-weary player will accept.)*
- **H6 — The handling fix holds (the anti-OUROBOROS claim).** *Prediction:* the player never needs to consult a buried card; all decisions are made from the three visible tops and the hand. No hidden-face memory strain. *(Failure: the player finds themselves wanting to check what's under a top, i.e. buried state secretly matters.)*

## What to watch

- **Decision texture.** Are turns "play one, draw one, next" reflexes, or pauses-and-chooses? Note any turn the player audibly deliberates — and whether that deliberation feels rewarding or tedious. This is the make-or-break observation.
- **Dead-cairn recognition.** Does the player learn to avoid topping a cairn with a sign whose cards are spent? Watch whether this insight arrives on its own (good — the skill is discoverable) or never (the game may read as luck).
- **Counting behaviour.** Does the player track how many cards of a sign remain, or play purely by what's in front of them? The sim's skill comes from light counting; see whether humans reach for it.
- **The blocking moment.** When a deal dies, capture *why* immediately: a foreseeable stranding, an unlucky run, or a genuine no-win deal. Tally these — the mix is the H2 evidence.
- **Win/loss tally per difficulty.** Record stones-left for every deal. Compare the standard-deal clear rate to the sim's ~74–98% band.
- **Replay pull.** After a loss, does the player want to reshuffle and go again (good solo sign), or set it down?
- **Long Trail feel.** At 9 signs, does the bigger hand feel like it restores control, or does the 36-card crossing feel like luck regardless?

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | Player deliberates and can justify plays; "nice" moments | Autopilot; "felt like sorting"; one obvious move per turn |
| H2 | Losses traced to a specific earlier misplay | "The draws killed me"; losses feel random |
| H3 | Standard wins ~most deals, with real scares | Constant forced plays (starved) or zero danger (trivial) |
| H4 | Player spontaneously uses the stock's visible top | Peek unnoticed / unused |
| H5 | Fits a tray; hand comfortable to hold and read | Cairns creep; hand awkward; wants more table |
| H6 | Never consults a buried card | Wants to check buried state |

## Teaching plan

CAIRN is solo, so **the rulebook is the teacher** — its teachability is itself under test.

- **First, attempt a cold read:** hand over [CAIRN_rulebook.md](CAIRN_rulebook.md) and have the player set up and start *without* verbal help. Note every point where they hesitate, re-read, or ask — those are rulebook bugs.
- Only step in if they stall. If you must explain, lead with the **one-sentence hook:** "match a cairn's top sign, lay your card showing its other side, and don't box yourself in."
- Demonstrate one join concretely: "this cairn shows Flame; this card is Flame/Eye, so it goes here and now shows Eye."
- Point out the **loss condition** early ("if nothing in hand fits any top, the trail dies") so the player understands what they're avoiding.
- Do **not** pre-teach the free look or dead-cairn avoidance — whether the player discovers these unprompted is exactly what H4 and the dead-cairn watch are measuring.

## Outcome data to record

Per deal: difficulty, win/loss, stones left, rough time, and (on a loss) the cause category — *foreseeable stranding / unlucky run / no-win deal*. One line each; the table is the report's spine.

## Out of scope

- Deep tuning of scoring tiers / a "win-margin" rating — first answer whether the core loop is fun.
- Extensive Long Trail (9-sign) testing — one deal to confirm it's viable; full study is a later session if the standard game earns it.
- Re-simulation — the sim has done its job; this session is the table's turn (per [playtesting.md](../.kiro/steering/playtesting.md): a first table test outranks more simulation).
- Any co-op / multiplayer framing — CAIRN is solo by design.
