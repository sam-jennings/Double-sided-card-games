# SLEEPER — fix options, simulated (November 2026)

*Evidence for the two designer decisions in the [design analysis Verdict](SLEEPER_design_analysis.md#verdict). This note measures the candidates; it does not choose one, and the rulebook (v0.1a) is unchanged.*

## Method

- **Sim:** [sleeper_sim.py](sleeper_sim.py), new opt-in sweep `python sleeper_sim.py --fixes --games 2000 --seed 1`. The default run (`python sleeper_sim.py --games 2000 --seed 1`) is untouched: its output was diffed byte-for-byte against the pre-change output and is identical.
- **Volume:** 2,000 games per table × 3 tables (random / skilled / mixed) × 3 player counts × 9 option rows = 162,000 games. Same bots as the analysis (greedy SkilledBot that ignores others' loyalties; RandomBot; mixed = one skilled seat among random ones). Talk, Unmask and the Wager are still not modelled. Sampling error is about ±1.1 points on a 50% rate.
- **Columns** (all from the skilled table unless noted):
  - *Last-mover win* — win rate of the seat that takes the final Court card. For (a) and (b), where the last round has no real "last" seat, this is the seat last in deal order. *Others mean* — average win rate of the other seats.
  - *Seat spread* — highest minus lowest win rate by seat position from the first player.
  - *Skill ×* — mixed-table win rate of the skilled seat ÷ mean per-seat win rate on the all-random table (same option).
  - *Pinned* — share of Masters that the public registry narrows to one sign at the end of play, before the reckoning (same measure as the analysis).
  - *Turns* — Court cards played per game. *No win / shared* — games with zero / several winners. *Stalls* — games over the 600-turn guard, across all three tables.

## Options as modelled (and how each is done at a table)

| Option | Sim reading | At the table |
|---|---|---|
| **(a) Simultaneous final round** | The last P Court cards form one final round, one card per player. All are revealed. Everyone chooses against the same pre-round row and all act at once. Flips toggle the pre-round row, so two flips on one card cancel. | When the Court deck holds P cards, the Steward deals one to each player. Each shows both faces, then holds the card between palms. On "three", everyone at once either lays their card in the row with the chosen face up, or drops it on the spent pile and puts a fingertip on the Court card they turn. Then flip the touched cards; a card touched twice stays as it is. |
| **(b) Sealed final round** (the "hidden commit") | The last P cards go one to each player, **unseen by the others**. In turn order, each player lays theirs in the row as a *sealed decree*, with the sign it backs pressed **down**. No coat-turns this round. Sealed decrees flip up at the reckoning. SkilledBot reads its own sealed decree, plus any other whose pressed sign the registry pins to one candidate. | When the Court deck holds P cards, the Steward shuffles them under the table, flipping as they go, and deals one between palms to each player. On your final turn, look at it privately and lay it in the row **rotated sideways**, chosen sign down. At the reckoning, turn every sideways card over. |
| **(c) Rotating end seat** | After the opening row, burn *d* cards = (showing pip of the 3rd opening card) mod P. Burned cards are revealed and spent in public, so the registry is unchanged. This moves which seat takes the final turn from game to game. | Read the third opening card's pip and divide by the number of players. Reveal that many cards (the remainder) off the Court deck and put them on the spent pile. |
| **Set aside k unseen** (k = 2, 3, 4) | After the opening row, k Court cards are removed unseen. The unseen pool becomes P + k cards instead of P. The clock shortens by k turns. | After opening the Court, the Steward takes k cards off the Court deck by Blind Cut, under the table edge and without looking, squares them, and puts them under the Steward token (the *Vault*). Nobody looks at them until the reckoning. They can be shown then to confirm nothing was peeked. |
| **(a)/(b) + set aside 3** | Each combined with k = 3. | As above. |

The literal "hidden-commit final *turn*" (one player only) changes nothing. The final mover already acts with no reply possible, so hiding the move removes no information from anyone who could have responded. A hidden commit only helps if it covers a whole round, which is why (b) is a round. A hidden commit also can't be a face-down card (there are no card backs), and a palmed card can be re-oriented until it's revealed. So the only *enforceable* sequential hidden commit is a card laid on the table with the chosen sign pressed down. That restricts (b) to decrees: you can't secretly commit to a coat-turn target.

## Results (2,000 games per table, seed 1)

| Option | P | Last-mover win | Others mean | Seat spread | Skill × | Pinned | Turns | No win | Shared | Stalls |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline | 4 | **59.8%** | 26.7% | 39.8% | 7.6 | 62% | 29.0 | 5.7% | 40.2% | 0 |
| baseline | 5 | **55.8%** | 24.6% | 37.2% | 6.6 | 49% | 28.0 | 6.0% | 48.4% | 0 |
| baseline | 6 | **55.3%** | 22.4% | 37.0% | 5.1 | 37% | 27.0 | 5.0% | 56.5% | 0 |
| (a) simultaneous final round | 4 | 32.8% | 28.5% | 4.6% | 6.8 | 62% | 29.0 | 11.1% | 24.5% | 0 |
| (a) simultaneous final round | 5 | 27.8% | 25.0% | 3.7% | 5.4 | 49% | 28.0 | 10.2% | 29.9% | 0 |
| (a) simultaneous final round | 6 | 24.1% | 22.1% | 3.2% | 4.2 | 38% | 27.0 | 9.3% | 33.1% | 0 |
| (b) sealed final round | 4 | 43.6% | 25.8% | 22.2% | 6.6 | 23% | 29.0 | 19.6% | 35.5% | 0 |
| (b) sealed final round | 5 | 32.2% | 20.4% | 14.7% | 5.3 | 12% | 28.0 | 25.9% | 32.9% | 0 |
| (b) sealed final round | 6 | 28.9% | 17.5% | 14.6% | 4.2 | 6% | 27.0 | 27.6% | 33.6% | 0 |
| (c) rotating end seat | 4 | 60.2% | 25.9% | 4.6% | 7.8 | 62% | 27.6 | 7.3% | 40.3% | 0 |
| (c) rotating end seat | 5 | 56.5% | 24.3% | 5.2% | 5.7 | 48% | 25.8 | 6.5% | 47.8% | 0 |
| (c) rotating end seat | 6 | 54.8% | 21.9% | 5.9% | 5.3 | 37% | 24.7 | 5.7% | 53.9% | 0 |
| set aside 2 unseen | 4 | 61.9% | 26.5% | 41.6% | 7.4 | 38% | 27.0 | 6.0% | 42.0% | 0 |
| set aside 2 unseen | 5 | 56.2% | 24.3% | 36.0% | 5.7 | 29% | 26.0 | 6.5% | 48.1% | 0 |
| set aside 2 unseen | 6 | 54.9% | 22.0% | 38.5% | 5.0 | 22% | 25.0 | 5.9% | 54.1% | 0 |
| set aside 3 unseen | 4 | 57.5% | 26.7% | 38.5% | 7.4 | 29% | 26.0 | 8.3% | 40.9% | 0 |
| set aside 3 unseen | 5 | 53.9% | 24.3% | 34.6% | 6.0 | 22% | 25.0 | 7.6% | 48.3% | 0 |
| set aside 3 unseen | 6 | 54.2% | 22.1% | 35.8% | 4.9 | 16% | 24.0 | 6.9% | 54.2% | 0 |
| set aside 4 unseen | 4 | 61.8% | 25.4% | 41.0% | 6.8 | 22% | 25.0 | 6.8% | 39.4% | 0 |
| set aside 4 unseen | 5 | 56.0% | 23.3% | 36.8% | 5.6 | 16% | 24.0 | 7.4% | 46.7% | 0 |
| set aside 4 unseen | 6 | 52.5% | 21.5% | 35.6% | 5.0 | 12% | 23.0 | 7.3% | 52.2% | 0 |
| (a) + set aside 3 | 4 | 28.8% | 29.0% | 3.3% | 6.4 | 27% | 26.0 | 12.2% | 22.6% | 0 |
| (a) + set aside 3 | 5 | 26.2% | 24.4% | 5.2% | 4.5 | 22% | 25.0 | 12.0% | 27.8% | 0 |
| (a) + set aside 3 | 6 | 23.2% | 22.2% | 2.3% | 3.9 | 16% | 24.0 | 10.2% | 34.4% | 0 |
| (b) + set aside 3 | 4 | 39.5% | 24.1% | 19.8% | 6.3 | 9% | 26.0 | 23.4% | 31.0% | 0 |
| (b) + set aside 3 | 5 | 32.6% | 19.0% | 15.1% | 4.9 | 5% | 25.0 | 28.2% | 29.7% | 0 |
| (b) + set aside 3 | 6 | 27.0% | 17.3% | 12.3% | 3.7 | 2% | 24.0 | 29.0% | 33.0% | 0 |

The per-seat skilled win rates by position from the first player are in the raw sweep output. For example, (a) at 6P gives 23 · 23 · 24 · 21 · 21 · 22%, against the baseline's 25 · 30 · **55** · 18 · 18 · 20%. In the baseline and set-aside rows, the 55–62% seat moves with the deck length, because removing k cards changes which seat moves last.

No option produced a stall. Every option still ends when the Court deck empties.

## Handling check per candidate

- **(a) Simultaneous final round.**
  - *What's visible:* everything. All P final cards are shown on both faces.
  - *What's hidden:* only the choice, and only until the count of three. This is THE COUNCIL's palms-commit / simultaneous reveal, so it's a known-good technique.
  - *Verification:* the result is all on the table after the reveal.
  - *Costs:* up to six hands go into one row at once, and a fingertip-on-target gesture is easy to fumble or dispute ("I touched that one"). Players must notice "P cards left", which means counting the deck near the end; that's easy, because it's small. One player hesitating to watch the others is the classic simultaneous-reveal cheat, and the count has to be enforced socially.
  - *No buried state.* This option also replaces the impossible "finish the go-around" sentence.
- **(b) Sealed final round.**
  - *What's hidden:* a sealed decree is a flat card with one pressed face, exactly the loyalty card's own concealment. It's sound by construction, and it's enforceable: the card is on the table and can't be re-oriented without being seen.
  - *Verification:* at the reckoning, by flipping.
  - *What can be deduced:* the pressed sign *is* deducible from the public face plus the registry. Sometimes that pins it, so the hidden information is partial on purpose.
  - *Costs:*
    - A second "sideways" meaning: sideways in the row means sealed, while the sideways pile means spent. They're in different places, but it's one more thing to teach.
    - Decree-only: you can't secretly commit to a coat-turn target.
    - The Court deck's top face is always public, so one of the P dealt cards had a known face. The under-table shuffle hides who got it; the sim doesn't model that leak.
- **(c) Rotating end seat.** Fully public and trivial to handle: a remainder, then a short public burn. Everyone can still count the deck, so the last mover is known in advance. The end can't be made secret, because the deck can't be hidden.
- **Set aside k unseen.**
  - *Handling:* one more Blind Cut and a pile nobody may look at. This is the same discipline as the loyalty deal, so it's not a new skill.
  - *Where it goes:* it needs a place that can't be confused with the spent pile; under the Steward token works.
  - *Verification:* it can be revealed at the reckoning.
  - *Costs:* it doesn't touch the clock-as-public-history idea, but it does shorten the game by k turns, and it changes which seat moves last.

## Reading

**Decision 1 — last mover.**

- **(a) is the only candidate that meets the Verdict target** (last seat within ~10 points of the others) on its own. The gap is +4.3 / +2.8 / +2.0 points at 4/5/6P, against the baseline's +33 / +31 / +33, and the seat spread drops from ~37–40 points to 3–5. Its costs:
  - Coordination gets harder. Shared wins fall from 40–57% to 25–33%, and no-winner games roughly double, from 5–6% to 9–11%.
  - The skill multiple drops, but stays healthy: 6.8 / 5.4 / 4.2× against 7.6 / 6.6 / 5.1×.
  - The table cost is a mass simultaneous gesture.
- **(b) halves the edge but doesn't clear it.** The gap is +18 / +12 / +11 points. The last sealer still reads the sealed decrees the registry pins, so information still flows to the last seat, most at 4P. Its other effects:
  - No-winner games jump to 20–28%, because nobody can see the final push.
  - **It also blunts the registry heavily**, as a side effect: pinned drops to 23 / 12 / 6%. The P sealed cards stay unseen until the reckoning.
  - So it is really an answer to *both* decisions at once, at the price of a lot of zero-winner games.
- **(c) fixes seat fairness by position only, not last-mover power.** The spread is 4.6–5.9 points, but whoever moves last still wins 55–60%. It shares the advantage out across games; it doesn't remove it within a game, and it does nothing for kingmaking at the reckoning.

**Decision 2 — the registry.**

- **Setting cards aside works in a straight line and leaves the last-mover problem exactly as it was.** Pinned at 4/5/6P:

  | Cards set aside | 4P | 5P | 6P |
  |---|---:|---:|---:|
  | none (baseline) | 62% | 49% | 37% |
  | 2 | 38% | 29% | 22% |
  | 3 | 29% | 22% | 16% |
  | 4 | 22% | 16% | 12% |

- The skill multiple barely moves: 6.8–7.4× at 4P. The cost is k fewer turns (29 → 25 at 4P with k = 4).
- The 4P/6P gap closes but persists, because the unseen pool is P + k, so 4P stays the most counting-exposed count. A per-count k (for example k = 4 at 4P and k = 2 at 6P) would equalise pinning at about 22%.
- **Embracing counting** isn't measured here. The bots don't use counting to read Masters, so this sim can't say whether counting is fun; it can only say how often it would settle the question.

**Combined:** **(a) + set aside 3** meets the last-mover target at every count (gap −0.2 / +1.8 / +1.0 points; spread 2–5 points). It holds pinned at 27 / 22 / 16%, and the skill multiple stays at 3.9× or more. It also has the lowest shared-win rate (23–34%) and 10–12% no-winner games. **(b) + set aside 3** nearly kills counting (9 / 5 / 2% pinned), but leaves a 10–15-point last-seat edge and 23–29% no-winner games.

**What the sim can't say:**

- The bots are greedy and one-ply. They don't anticipate a simultaneous round, don't steer toward known allies, and don't kingmake on purpose, so human kingmaking risk is under-measured in every row.
- No-winner and shared-win rates will move with talk.
- Whether a six-hand simultaneous reveal is fun or a scramble, and whether sealed decrees feel tense or arbitrary, are table questions.
