# SYZYGY — Design Analysis

*How the rules were tested and tuned, v1.0 → v1.2. Companion to the rulebook.*

---

## 1. Method

The full ruleset was implemented as a Python simulator (`syzygy_sim.py`, included) with a rules engine that mirrors the rulebook exactly: charging on place/flip/move/requirement-transition, once-per-turn activation caps, continuous alignment checking mid-chain, full-grid discards, and per-variant rule switches so each candidate change could be tested in isolation.

Two bot tiers establish a floor and ceiling for play quality. **RandomBot** places randomly and fires every available ability — it shows what the mechanics *permit*. **GreedyBot** does a one-ply lookahead over placements and ability choices, scoring positions by capture differential minus a penalty for threats left on the board (a pair plus an empty third cell, or a flip-completable line), declining any activation that doesn't improve its position. It shows what *adversarial* play converges to. The gap between them brackets where human play will land.

Every claim below comes from batches of 600–1,500 games per configuration, fixed seeds for comparability, with one alternate-seed robustness check on the final design. Total: roughly **23,000 simulated games**. Card conservation (grid + scores + removed + deck = 36) and termination were asserted on every game.

Health targets set before tuning: captures ≥ 8 cards/game (2P), zero-capture games < 5%, ties < 8%, no dead symbols, seat win rates within 52/48, and a skilled bot beating a random one > 70% of the time.

---

## 2. What v1.0 got wrong

The first complete ruleset (no wild Star, Sun requires the exact centre cell, Meteor requires exactly one neighbour, Void grabs a deck card whenever isolated, ties shared) was playable and skill-rewarding — greedy beat random 82% — but the data exposed five problems.

**The chain fantasy was dead under skilled play.** Greedy bots activated abilities on only 0.12 of turns; 89% of turns used no ability at all. The cause is structural: because the *active player* captures any completed line, building toward an alignment across turns is self-defeating — you're assembling a gift for the next player. Skilled play collapsed into "place safely, complete only what you can finish this instant." The signature mechanic barely fired.

**Eclipse dominated a self-fulfilling meta.** Placed face-up 18% of the time (uniform would be 11%), requirement met 94% of placements, 1.74 activations/game, captured-as 2.69 cards/game — and winners activated it +0.77 more than losers, the largest skill signal of any symbol. Because everyone showed Eclipse, Eclipse lines were the easiest to complete, which made showing Eclipse even better.

**Sun and Meteor were dead.** The grid saturates by turn ~9 and stays full (19.8 forced discards/game), so the centre cell is almost never empty when you draw a Sun (0.08 activations/game) and "exactly one neighbour" almost never holds for Meteor (0.04).

**Void was free luck.** ~1.2 points/game from early isolated placements, uncorrelated with skill.

**Ties were common.** 12.5% in 2P, 24.3% in 4P — too many anticlimaxes for a game this short.

### v1.0 baseline (greedy mirror, 2P, 1,000 games)

| Metric | v1.0 |
|---|---|
| Captured cards/game | 7.7 |
| Zero-capture games | 2.3% |
| Ties | 12.5% |
| Activations/turn (skilled) | 0.12 |
| Turns with no activation | 89.2% |
| Full-grid discards/game | 19.8 |
| Greedy vs random win rate | 82.2% |

---

## 3. Five candidate fixes, tested in isolation

Each change was run alone against the baseline (greedy mirror 2P, 800 games, same seed) so effects wouldn't be confounded.

| Variant | Captures/game | Ties | Act/turn | Key symbol effect | Verdict |
|---|---|---|---|---|---|
| v1.0 baseline | 7.7 | 12.5% | 0.12 | Eclipse +0.77 outlier | — |
| **Star is wild** | **19.4** | **3.5%** | 0.27 | every symbol's capture rate up 3–5× | **adopt** |
| **Sun: middle row/col** | 8.2 | 10.1% | 0.13 | Sun req-met 26→76%, act ×3.5 | **adopt** |
| **Meteor: 1–2 nbrs** | 7.7 | 10.2% | 0.12 | Meteor req-met 16→63% | **adopt** |
| **Void: catch-up only** | 7.0 | 23.9% | 0.09 | luck points 1.21→0.12 | **adopt** (tie spike fixed by star-wild) |
| Eclipse: self-swap only | 5.6 | 14.8% | 0.10 | Eclipse act −39%, but captures −27% | **reject** as core; keep as variant |

**Star-wild is the keystone.** Making the Star face count as any symbol in alignments multiplies the number of completable lines, which changes the incentive structure around abilities: a flip or swap now *frequently* completes a capture on the same turn, so activations stop being pure setup-for-the-opponent and start being conversion tools. Captures jumped from 7.7 to 19.4 cards/game, zero-capture games vanished, ties collapsed, and — crucially — every other symbol came alive because lines through wilds involve everyone's faces. It also half-solved the grid-saturation problem on its own: forced discards fell from ~20 to ~9 per game because captures keep emptying cells.

**The Eclipse nerf was rejected for the core game.** Self-swap-only did flatten Eclipse (+0.60 vs +0.77 win-correlation) but cost 27% of all captures and raised ties — it removed the game's best conflict tool to fix a dominance that star-wild dilutes anyway (under wilds, Eclipse's +0.63 is statistically indistinguishable from Star's own +0.62; it's no longer an outlier, just one strong card among nine). It survives as the harsher two-player "Deep Space" variant.

---

## 4. v1.1 → v1.2: the tiebreaker problem

Combining the four adopted fixes (v1.1) hit every capture/liveliness target, but exposed a final issue: with shared ties, 2P still tied 6.9% and 3–4P tied 17–18% of games. Three tiebreak rules were tested across all player counts:

| Tiebreak rule | 2P seats | 3P seats | 4P seats | Residual ties |
|---|---|---|---|---|
| Shared ties (v1.1) | 47/53 | 33/32/35 | 23/25/27/25 | 7–18% |
| Earliest seat wins | 51/49 | **40**/32/29 | 28/28/25/**19** | 0% |
| First capturer wins, then seat | 48/52 ↔ 51/49* | 32/34/33 | 24/27/25/24 | 0% |

*\*two seeds, 1,500 + 800 games — the 2P seat difference flips sign across seeds, i.e. it is noise around 50/50.*

"Earliest seat wins" fixed 2P but broke multiplayer: dumping 17% of games into seat 1 produced a 40% first-player win rate in 3P. "Whoever made the **first alignment capture** of the game" is seat-neutral by construction (any seat can capture first), resolves nearly all ties on a memorable, thematic event ("first blood"), and falls through to turn order for the rare remainder. That chain — most cards → most distinct symbols → first capturer → earliest seat — is v1.2's scoring rule and produces flat seats at every player count.

---

## 5. Final state of the design (v1.2)

Greedy mirrors: 1,500 games (2P), 800 (3P), 800 (4P), seed 42; robustness re-run at seed 1234.

| Metric | 2P | 3P | 4P | Target |
|---|---|---|---|---|
| Captured cards/game | 19.2 | 19.3 | 19.6 | ≥ 8 ✓ |
| Zero-capture games | 0.0% | 0.0% | 0.0% | < 5% ✓ |
| Ties | 0.0% | 0.0% | 0.0% | < 8% ✓ |
| Avg winning margin (cards) | 5.6 | 3.6 | 3.0 | — |
| Seat win rates | 48/52 (51/49 alt seed) | 32/34/33 | 24/27/25/24 | within 52/48 ✓ |
| Skilled activations/turn | 0.24 | 0.24 | 0.25 | see §6 |
| Forced grid discards/game | 9.3 | 9.1 | 8.9 | (was 19.8) |

Skill check: greedy beats random **96.3%** of the time in v1.2 (was 82.2% in v1.0) with an average margin of 12 cards — the rule changes made the game *more* skill-rewarding, not less, because abilities now matter and using them well is a real differentiator.

Per-symbol health (2P, 1,500 games): every symbol's requirement now fires regularly and every symbol gets captured at a meaningful rate. The capture-rate spread compressed from 15× (Eclipse 2.69 vs Meteor 0.18 in v1.0) to 3.3× excluding the structurally capture-prone wild Star.

| Symbol | Placed face-up | Req met when placed | Activations/game | Captured-as/game | Winner−loser act diff |
|---|---|---|---|---|---|
| Sun | 12.7% | 76.9% | 0.75 | 1.98 | +0.16 |
| Moon | 8.6% | 53.9% | 0.26 | 1.10 | +0.06 |
| Star | 14.1% | 75.8% | 2.06 | 5.38 | +0.60 |
| Comet | 13.5% | 77.2% | 1.23 | 2.29 | +0.24 |
| Eclipse | 14.9% | 86.6% | 2.01 | 2.95 | +0.64 |
| Aurora | 8.6% | 58.1% | 0.31 | 1.13 | +0.07 |
| Meteor | 9.3% | 74.0% | 0.14 | 1.02 | +0.01 |
| Nova | 10.1% | 80.4% | 0.57 | 1.87 | +0.13 |
| Void | 8.1% | 29.9% | 0.63 | 0.90 | −0.30 |

Void's negative skill-correlation is by design — it's the catch-up valve, so *losing* players activate it. Star and Eclipse remain the strongest faces but within a healthy band, and both carry real risk (a shown Star is a wild for your opponents too; a shown Eclipse is a popular alignment target).

---

## 6. Hypothesis verdicts

**H1 — skill matters (greedy ≥ 75% vs random):** Pass, 96.3%.

**H2 — captures are frequent (≥ 2 capture events/game):** Pass; ~19 captured cards ≈ 6+ alignment events per game, one every 5–6 turns.

**H3 — no dead symbols:** Pass in v1.2. v1.0 failed (Sun 0.08 and Meteor 0.04 activations/game); both now fire and get captured at ≥ 1 card/game.

**H4 — no seat dominates (≤ 57% for any seat):** Pass at all player counts; worst observed seat is 27% in 4P (uniform 25%).

**H5 — chains are lively but bounded:** *Partial.* The mechanics support rich chains — random bots, which fire everything, average 0.74 activations/turn with 18% of turns chaining 2+ abilities, and the once-per-turn cap kept every one of ~23,000 games terminating. But optimal play is more restrained than hoped: greedy bots activate on only 1 in 5 turns, because declining is genuinely often correct (the rulebook now frames this as strategy rather than hiding it). Human play should land between the 0.24 floor and 0.74 ceiling — a mixed greedy-vs-random table averaged 0.49. Whether that *feels* lively enough is exactly what live playtesting must answer.

**H6 — most games have action (zero-capture < 10%):** Pass, 0.0%.

---

## 7. Honest limitations — what simulation cannot tell us

**Aurora is undervalued by construction.** The bots have perfect information, so an ability whose entire point is *revealing hidden information* (peek at a card's hidden face) evaluates as a mere conditional flip. Its true table-value — memory, bluff-calling, safe flips — is invisible here. Aurora's numbers (0.31 act/game) should be read as a floor. If live players still ignore it, it's the first candidate for a buff.

**Hidden-face memory and bluffing aren't modelled at all.** Choosing which face to show is a rich information decision for humans (the deck-top is public; hidden sides are deducible if you watched placements). The bots simply know everything, so the game's deduction layer is untested.

**One-ply lookahead is not deep play.** A stronger searcher might find multi-turn ability lines the greedy bot declines, raising the skilled activation rate — or might confirm that restraint is optimal. Either way the termination and balance guarantees hold; only the "feel" estimate would shift.

**Fun is not a simulation output.** The numbers say the game is balanced, skill-rewarding, decisive, and active. They cannot say it's *fun*. Recommended first live tests: (1) does a capture every ~5 turns feel exciting or exhausting at 19 cards/game; (2) does anyone use Aurora; (3) is the "active player captures everything" rule legible and dramatic, or does it feel like theft; (4) do new players grasp charging vs. re-charging within one game.

**Suggested first table protocol:** one 2P game with the Calm Skies variant (no wild) to learn the symbols, then standard rules; watch for the moment players start *declining* activations — that's the skill curve announcing itself.

---

## 8. Change log

| Version | Change | Reason (data) |
|---|---|---|
| v1.0 | Initial complete ruleset | — |
| v1.1 | Star wild in alignments | Captures 7.7→19.4, all symbols alive, ties 12.5→3.5% |
| v1.1 | Sun req: centre → middle row/col | Sun activations 0.08→0.28 in isolation |
| v1.1 | Meteor req: =1 → 1–2 neighbours, choose target | Meteor req-met 16→63% |
| v1.1 | Void: only when strictly behind | Luck points 1.21→0.12/game; becomes catch-up valve |
| v1.2 | Tiebreak: distinct symbols → first capturer → seat | Ties 7–18% → 0% with flat seats at all counts |
| — | Eclipse self-swap rejected as core | Cost 27% of captures; kept as "Deep Space" variant |

*All numbers: greedy-mirror simulations, 600–1,500 games per configuration, seeds 42/1234, ~23,000 games total.*
