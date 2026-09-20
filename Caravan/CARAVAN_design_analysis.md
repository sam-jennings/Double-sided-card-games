# CARAVAN — Design Analysis & Floor Simulation

*September 2026 · simulator: [`caravan_sim.py`](caravan_sim.py) · rulebook: [`CARAVAN_rulebook.md`](CARAVAN_rulebook.md) (v0.1) · brief: [DOWRY_future_directions.md](../Dowry/DOWRY_future_directions.md)*

Reported in the post-[SKILL_GAP_METHOD](../Project/SKILL_GAP_METHOD.md) format: **decision density first**, every bot's information set stated, skilled-vs-random labelled as a floor and not as a headline.

## 1. Design intent

**Naming options (8 September 2026):** **Fair Share / Trade Winds** or **Velvet Cut / Velvet Road**, with DOWRY taking the first name and CARAVAN the second in each pair. Neither pair is adopted. See the [paired naming notes](../Dowry/DOWRY_future_directions.md#paired-names-for-dowry-and-caravan) for rationale and straplines.

CARAVAN keeps everything the sibling brief said to inherit — small dressed offers, a consequential receiver choice, public ownership, two useful faces, inspectable revealed pairs, a short route from decision to reveal — and changes one thing: **the offer is no longer bilateral and no longer a turn.** Every player packs one offer and receives one offer, simultaneously, along a road whose direction is fixed by the round.

The new question is meant to be **"how much can I afford to hand *this particular person*?"** — the same question the brief set for OPEN SECRET.

### Why not OPEN SECRET

The brief recommended OPEN SECRET first. This design deliberately answers the same question with a different structure, because OPEN SECRET's own risk list is largely structural rather than incidental:

| OPEN SECRET risk (from the brief) | Cause | CARAVAN |
|---|---|---|
| Written commitment for buyers *and* for sellers choosing between buyers | Buyers collide, so simultaneity must be **enforced** | Every player reads a *different* offer, so takes cannot collide. Simultaneity needs no enforcement and no paper. **Deck only.** |
| Seller veto becoming personal or kingmaking | A popular seller chooses whom to strengthen | Nobody chooses a counterparty. The road does. |
| Failed purchases feeling like lost turns | Several buyers, one sale | Every offer is packed and taken, every round, by everybody. |
| Three rounds at 4P being too brief | 36 cards ÷ 3 per offer ÷ 4 sellers | Identical constraint — CARAVAN is also 3 rounds at 4P, and the rulebook says to play two deals. This one is not solved, it is inherited. |

CARAVAN also has no downtime at any count, which a 4-player DOWRY variant cannot claim: in DOWRY's own 3–4P variant one player cuts while everyone else waits.

The cost is real and should be stated: **CARAVAN removes targeting.** OPEN SECRET lets you choose whom to court; CARAVAN only lets you choose what to show. If the table wants targeting back, *The trailing road* variant is the cheapest way to buy it without kingmaking.

## 2. Card flow — the structural result

36 cards ÷ 3 per offer = **12 offers, at every player count**, and the same deal works everywhere:

| Players | Deal | Stock | Rounds × offers | Stock empties | Hands after |
|---|---:|---:|---|---|---|
| 2 | 6 each | 24 | 6 × 2 = 12 | after round 4 | 6 → 3 → 0 |
| 3 | 6 each | 18 | 4 × 3 = 12 | after round 2 | 6 → 3 → 0 |
| 4 | 6 each | 12 | 3 × 4 = 12 | after round 1 | 6 → 3 → 0 |

Deal 6, refill to 6, and hands and stock empty together at 2, 3 and 4 players with no partial refills and no short offers. Termination is structural, not a rule. The road schedules are derangements and rotationally symmetric, so **all seats are identical by construction** — asserted in the simulator, not assumed.

## 3. Method

Full ruleset modelled at 2/3/4P including the physical information flow: face randomisation on shuffle, public self-deal glimpses, public stock-top faces at every refill, offered faces public, simultaneous placement revealing both faces (the open registry).

**Bot information set — identical for every non-random bot:** own hand (both faces) + the public registry + deduction from pair uniqueness. **No bot ever reads another player's hand.** This is the §2 requirement of SKILL_GAP_METHOD; the figures below are not void.

| Bot | Line |
|---|---|
| **RandomBot** | Uniform legal pack / take / placement. Mechanics floor only. |
| **NaiveBot** | Naive but sensible: values a card by its better pip, offers its three worst, splits so the lots look even, dresses honestly, takes the bigger visible pips, places on the bigger pip. No majority reasoning; no thought about who receives. **This is the headline baseline.** |
| **ThoughtfulBot** | Same information. Majority-threshold valuation, predicts the taker's read *from the taker's knowledge*, dresses to protect the lot it means to keep. |
| — *ring-blind* ablation | Identical, except it optimises its own keep and ignores who receives the rest. **Tests whether the road is load-bearing.** |
| — *honest-dress* ablation | Identical, except it must show the better pip face. **Tests whether the dressing is load-bearing.** |

Volume: ~4,200 games in the headline runs (7 arms × 200 games × 3 player counts), plus ~2,500 in the offer-shape selection of §5 and a matched probe of DOWRY's own simulator.

## 4. Decision density (reported first)

Thoughtful mirror, 2,400 take-decisions per player count. **DOWRY's column was produced by instrumenting `dowry_sim.py` itself with the same measures**, so these are comparable rather than free-floating.

| Measure | 2P | 3P | 4P | DOWRY (2P) |
|---|---:|---:|---:|---:|
| Legal packs per offer (mean) | 404 | 366 | 328 | 1,428 |
| Take-decisions with ≥2 options | 100% | 100% | 100% | 100% |
| **Risk-free / dominant takes** *(one lot's worst case ≥ the other's best)* | 32.7% | 40.1% | 43.4% | 37.8% |
| Near-indifferent takes *(within 10%)* | 26.9% | 21.2% | 20.6% | 30.0% |
| **LIVE takes** *(neither obvious nor a wash)* | **40.4%** | **38.6%** | **36.0%** | **32.2%** |
| Takes that move a sign's current leader | 91.9% | 92.2% | 92.2% | 92.1% |
| Took the bigger lot | 60.7% | 58.4% | 62.0% | 51.4% |

Legal-pack counts are the full legal space, computed rather than sampled, in both games; DOWRY's is larger only because its hand is 9 rather than 6.

CARAVAN's take-decision is live *slightly more often than DOWRY's* at every count, and more than nine takes in ten visibly change who leads a sign — the perceivability check that WILDFIRE failed. The pack decision is never obvious: a few hundred legal packs, and the best one depends on a specific opponent's spread.

The mild drift with player count (dominant takes 32.7% → 43.4%) is the expected direction: the more opponents there are, the less a packer internalises the cost of the gift, so offers get a little lazier. It is a drift, not a cliff.

## 5. Two methodological findings that changed the design

### 5a. The value model can manufacture false obviousness

The first floor run used a smooth positional value proxy (each sign's pip weighted by how close the player is to leading it) and reported **74% risk-free takes** at 3P — a CLAMOUR-grade kill. Re-run against DOWRY's own `place_value` — a step function, where a card that changes no majority is worth almost nothing — the same ruleset reports **40%**.

The smooth model was wrong, not the game. Under a smooth proxy almost every card has positive value, so two cards beat one nearly always and the 2/1 take looks pre-decided. Under a step model most cards are worth nothing right now, so a pair of dead cards genuinely can be worth less than one live card — which is how a person at the table reads a lot.

| Config A at 3P | sharp (DOWRY's model) | smooth |
|---|---:|---:|
| Risk-free / dominant takes | 40.1% | 68.1% |
| LIVE takes | 38.6% | 18.5% |

**Proposed addition to SKILL_GAP_METHOD:** obviousness figures are meaningless without the value model stated beside them, and a smooth positional proxy systematically over-reports obviousness in any game with unequal lot sizes. Two of the collection's existing games would be worth re-checking on this basis.

### 5b. DOWRY's published "dressing edge ≈ 1.6–1.7×" is mostly not the dressing

Before changing CARAVAN's offer shape in response to the false alarm above, `dowry_sim.py` was probed directly. DOWRY's `HonestCutBot` differs from `SkilledBot` on **two** axes at once — it cuts for the most even *true* split **and** dresses informatively — so the published figure attributes the split objective to the dressing.

| DOWRY arm (120–150 games/arm) | Score ratio |
|---|---:|
| Published-style: deceptive vs honest-*cut* | **1.86×** (reproduces the published 1.6–1.7×) |
| Matched ablation: deceptive vs honest-*dress only* | **1.11×** |

The dressing layer in DOWRY is worth roughly a tenth, not two thirds. This does not weaken DOWRY — it is Proven at the table on player evidence, not on this number — but the claim *"the dressing layer is load-bearing, not decorative"* in [DOWRY_design_analysis.md](../Dowry/DOWRY_design_analysis.md) §3 is not supported by the arm that was run. **Recommended: annotate that file rather than re-run it**, per SKILL_GAP_METHOD §7's own triage.

It also reframes CARAVAN's flat dressing ablation below: CARAVAN is not worse than DOWRY here. They are the same, and the family's bluff may simply be worth less to a perfect-memory bot than it is to a person.

## 6. Results

All arms 200 games per player count. "A" is one thoughtful player seated among naive/random/ablated opponents, seat rotating.

| Arm | 2P | 3P | 4P |
|---|---|---|---|
| Flow failures (all arms) | **0** | **0** | **0** |
| Seats, thoughtful mirror | 92 / 107 | 67 / 65 / 67 | 44 / 47 / 59 / 47 |
| **THOUGHTFUL vs naive** *(headline)* | **1.22×** | **1.25×** | **1.29×** |
| thoughtful vs random *(floor, labelled)* | 3.59× | 2.51× | 2.71× |
| ring-AWARE vs ring-blind | 0.90× | 1.01× | 0.98× |
| DRESSING vs honest-dress | 1.12× | 0.96× | 1.03× |

- **Termination and card flow: certified.** Zero flow failures in every arm at every count. Every game is exactly 12 offers, every one of the 36 cards reaches a spread, hands and stock empty together.
- **Seats: fair.** 3P is 67/65/67. The 4P spread (59 high) is about +2σ on 200 games and is consistent with the construction being symmetric. **At 2P, 92/107 — CARAVAN does not reproduce DOWRY's 55.8/44.2 second-cutter edge**, which is the expected consequence of both players cutting at once. A 2P CARAVAN match needs no alternating-seat protocol.
- **Thought beats naive-but-sensible by 1.22–1.29×** on matched information with no cheating. Modest, and it is the honest number; the 1.5× bar it would have failed no longer exists ([SKILL_GAP_METHOD §6](../Project/SKILL_GAP_METHOD.md)).
- **The road ablation is flat (0.90–1.01×).** A bot that ignores who receives the lot does as well as one that reasons about it. This is the design's central premise and the simulation does not support it. See §7.
- **The dressing ablation is flat (0.96–1.12×)** — and so is DOWRY's, once matched (1.11×).

## 7. The one real flag: the road may be decoration

The design's pitch is that the road changes the packing decision. The bots say it does not.

Two reasons that may be a limitation of the bots rather than of the game, neither of which excuses the result:

1. **The ablation is one-ply.** The aware bot values the gift against the taker's *current* spread; it never reasons "this player is running away with it and I pack for them next round." Multi-round leader-management is the specific human skill the road is supposed to create, and it is not modelled.
2. **Bot tables rarely produce a runaway leader**, which is the situation where "whom can I afford to help" has an answer. Human tables produce them constantly, and produce grudges besides.

Neither point is evidence. **The correct response is to put it first in the rulebook's playtest questions and to carry a specific repair**: *The trailing road*, in which the weakest player names the direction each round. That converts the road from a timetable into a contested decision, without letting a strong player pick whom to strengthen. It should not be adopted before the base game has been played once.

If the base road reads flat at the table *and* the trailing road does not fix it, the honest conclusion is that this design is DOWRY-without-waiting rather than a different game — still useful, since 3–4 player DOWRY has no tested procedure, but not the sibling the brief asked for.

## 8. Rubric evaluation

1. **Exploits all-pairs deck?** Yes. The hidden face of an offered card is deducible only because every pair exists exactly once, and the registry closes as the game runs.
2. **Physically works with double-faced cards?** Yes — no card backs are needed anywhere. The offer is flat on the table showing one face; the private zone is the hand; commitment needs no component because no two players read the same offer.
3. **Information visible or deducible?** Yes. Six cards per player are private; everything else is public or on the table.
4. **Flipping matters?** Twice per card: the packer chooses what is advertised, the receiver chooses what is scored, and those are different people with different interests.
5. **Pair uniqueness matters?** Yes, as the deduction engine — and, unlike DOWRY, four to six offered cards per round accelerate the registry's closure.
6. **Distinct experience?** Partly proven, partly open. Simultaneity, no downtime and no counterparty choice are structurally distinct from DOWRY. Whether that *feels* distinct is question 1 and is not yet answered.
7. **Fills a player count / time / complexity gap?** The collection's Proven-and-loved game is 2P-only in practice. CARAVAN is a native 3–4P offer game at ~15 minutes with deck-only components.
8. **Explainable cleanly?** Yes — "pack three cards as a two and a one for the player the road points to, everyone takes at once, you keep what they leave" is one sentence, and there is no turn order to teach.
9. **Testable with current prototype?** Yes, immediately, with the existing deck and nothing else.
10. **Fastest way to falsify fun?** One 3-player deal, logging for each round who you packed for and whether their spread changed what you packed. If the answer is consistently "no", the road is decoration.

## 9. What the simulation cannot certify

1. **Whether simultaneous play feels social or parallel.** This is the top risk and it is the exact opposite of OPEN SECRET's risk, which was downtime and confrontation. Nobody waits — but nobody may be watching, either.
2. **Whether inability to retaliate is interesting or annoying.** The player squeezing you is never the player you pack for until the road turns.
3. **Human memory ≠ perfect memory.** The bots never forget a glimpse. With four offers a round the registry closes faster than in DOWRY, which may either help humans keep up or bury them.
4. **Table reading load at 4P.** Twelve offered cards plus four spreads per round; you only need to read your own offer, but players will want to read all of them.
5. **Whether three rounds at 4P is a game.** The rulebook recommends two deals; that is a guess.

**Next step:** one 3-player deal against the rulebook's five playtest questions, question 1 first.
