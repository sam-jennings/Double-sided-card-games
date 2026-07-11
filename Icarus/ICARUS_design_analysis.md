# ICARUS — Design Analysis (v0.1)

*Push-your-luck flights on the all-pairs flip deck. Sim-certified floor; untested at the table. Companion to `ICARUS_rulebook.md` and `icarus_sim.py`.*

---

## 1. The questions the sim was built to answer

1. Does the game terminate, conserve cards, and avoid degenerate strategies?
2. Is a stop-cost needed — is "bank after every card" dominant without the toll?
3. Does skilled play beat random by the house health bar (~1.5×)?
4. How much is the counting layer (D4) worth on its own?
5. What flight-length / fall-rate curve does good play produce, and is there a seat advantage?

## 2. Method

Full v0.1 ruleset modelled, including shuffle face-randomisation, tower splits (18/12/9), the toll, soar doubling, and the public-registry information model (counting bots see only fully-public cards — Fallen, banked, rows — and treat the hidden face as uniform over the unaccounted partners of the visible sign; they do not condition on other towers' visible tops).

Bots: `RandomBot` (50/50 press), `BankOneBot` (degeneracy probe), `EVBot(naive)` (myopic soar-aware EV on naive 8-partner odds), `EVBot(counting)` (same policy on registry-exact odds). Development also swept threshold policies (press iff p < θ) and a Monte-Carlo full-tower rollout planner. ~3,000 games per configuration, ~50,000 total; 600-turn guard; card conservation asserted after every flight. Stall rate: **0** everywhere.

**What the sim can't model:** table feel, downtime, watching-the-counter social pressure, and non-myopic human lines (deliberately steering toward a countable 4-card soar; toll-timing to burn dangerous tops).

## 3. Results

### Degeneracy — why the toll exists

| Config | bank-every-card vs counting | Verdict |
|---|---|---|
| No toll, no soar | **80% win, 1.27× score** for bank1 | broken — grazing dominates |
| No toll, soar on | 40% win, 0.90× | soar alone almost rescues it |
| **Toll on (shipped)** | **10% / 3% win (2P/3P), ~0.5×** | dead |

Both rules jointly guard the push incentive: the toll makes landing cost a card; the soar makes deep flights worth reaching for.

### Headline skill gap (shipped config: toll + soar ×2 at 4+)

| Players | counting vs random | score ratio |
|---|---|---|
| 2P | 80.6% win | **1.61×** |
| 3P | 66.1% win (33% baseline) | **1.55×** |
| 4P | 57.4% win (25% baseline) | **1.58×** |

Without the soar rule the ratio drops to 1.24× — the soar is what pulls correct play into high-stakes, count-sensitive territory. Meets the collection's ~1.5× health bar.

### The counting layer in isolation

Counting vs naive odds at the same policy: **1.06–1.08× score, 55.5% h2h at 2P** (36.3% at 3P vs 33% baseline). Modest at myopic depth. Two readings, per the OUROBOROS lesson: (a) myopic bots are a **floor** — human counting compounds across reach-for-the-soar planning and toll timing, which no bot here models; (b) a full-tower rollout planner beat the best simple bot by only ~1% score in a route-visible variant, so the *mechanical* ceiling above "count + be cautious" is genuinely modest. The honest claim: the game is a healthy push-your-luck whose *edge* comes from counting; it is not a deep engine. That is the right weight for a ~10-minute filler.

### Shape of good play

Mirror counting games: fall rate ~27–30%, mean flight ~3 cards, **bimodal flight lengths — land at 2 (~30%) or reach the soar at 4 (~40%)**, ~3.3 soars per game. Exactly the intended arc: a safe wage or a doubled fortune, rarely the mushy middle. Score levels ~90/60/45 per player at 2/3/4P. Estimated real time: ~11–13 flights of 30–60s → 10–15 min.

### Seat fairness

Mirror seat spreads: 2P 89.8/91.0; 3P 58.2/59.8/61.4; 4P 44.8/44.3/45.7/47.4. Later seats trend ~2–5% ahead (they fly with a richer registry). Within tolerance for a light game, but **check at the table**; if real, rotate first player or give seat 1 the first-toll choice.

## 4. Design decisions and their reasons

- **Personal towers, not a shared deck.** 36's even divisibility gives identical card budgets (18/12/9) — no unequal-final-round problem, and your risk never eats an opponent's deck. Cross-tower counting still works because every departed card is fully public.
- **Poison = revealed faces only.** The poison set is literally the face-up signs of your row — glanceable, zero memory (D2). Both-faces poison was rejected: base odds jump 25/50/75% and flights die at 2.
- **The toll (burn your next top on landing).** The stop-cost that kills grazing. Also feeds the registry — every landing is information for everyone.
- **Soar ×2 at 4+.** Lifts skilled-vs-random from 1.24× to ~1.6×; creates the bimodal push arc; makes the k=3 decision (naive 3/8) the game's signature moment, where the registry most often contradicts the naive odds.
- **Squared towers, not visible cascades.** A route-visible variant was tested with a rollout planner: +1% score. Not worth the table space or the analysis-paralysis risk. Parked.
- **Rank-sum scoring.** Keeps C7's rank canon doing work: a revealed Crown is 9 points *and* one more poison — sweet-poison tension for free.

## 5. Rubric self-scores (D5/D6 deliberately out of scope for this pass)

| Dim | Score | Justification |
|---|---|---|
| D1 Deck-necessity | 9/10 | The core gamble — *half of the next card is public* — is physically impossible with backed cards: an ordinary deck offers all-or-nothing information about its top. Towers use 36's even divisibility (18/12/9); per-sign scarcity (8 cards) bounds every count. Not 10: the all-pairs property is exploited through odds, not structure. |
| D2 Physical handling | 9/10 | No hidden state anywhere except tower interiors (which *are* the randomness). Row, Fallen field, and banked clutches are open spreads under the C6 sentence; live/dead and sideways-soar marks follow C3/C4; ~50k sims asserted conservation and termination. Open risk: table space for 2P banked clutches. |
| D3 Flipping load-bearing | 9/10 | The flip **is** the push — every flip is the game's central decision, and *declining* to flip is the other half. Removing flipping removes the game. |
| D4 Pair-uniqueness | 8/10 | Every-pair-once makes bust odds exactly computable and *verifiable* from the public record ("Flame–Moon already fell — Moon can't hurt me"). Held from 9: the sim's myopic counting edge is ~1.07×; the deeper human counting game is plausible but unproven at the table. |
| D7 Teachability | 9/10 | One-breath core: "flip — if it matches your row, you fall." Toll and soar are one sentence each; Fledgling variant strips the toll for first games; needs the C7 rank callout. |

## 6. Changes adopted during development

- v0.0 → shared deck, no toll, linear scoring: **rejected** (grazing degenerate; unfair final round).
- +towers, +toll: floor fixed, but skilled-vs-random only 1.24× (thin-gap red flag).
- +soar ×2 at 4+: **1.55–1.61×** — adopted as v0.1.
- Route-visible towers, zenith +5 flat bonus: tested, negligible — rejected/parked.

## 7. Caveats for the first table test (what only humans can answer)

1. Does the counting feel *delicious* or homework? (The design bets on delicious: it's optional, public, and verifiable.)
2. Is the k=3 "reach for the soar" moment as tense as the sim's bimodal distribution implies?
3. Downtime: do waiting players actually read the Fallen field, or switch off?
4. Table space and handling of banked clutches + sideways soar marking at 2P (18 cards each).
5. Is the toll intuitively acceptable, or does burning a card feel bad in a way that needs reframing?
6. Seat advantage: does the later-seat registry edge show up in human play?
7. Kestrel (memory) variant: is the symmetric memory load fun for the memory-game audience it targets?

First-table plan: 3P base game × 2 plays (teach time, flight tension, downtime), then one Fledgling teach with a new player, then Kestrel with willing victims. Use `Templates/Playtest Plan.md`.
