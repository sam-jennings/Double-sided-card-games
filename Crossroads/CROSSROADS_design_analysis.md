# CROSSROADS — Design Analysis

*How the 2P abstract was stress-tested by simulation, v1.0 → v1.1. Companion to the rulebook; sibling to the SYZYGY, TURNCOAT and TURNOVER analyses.*

---

## 1. The questions

The v1.0 footnote asked three things: does the endgame drag (pass timing)? Does ko suffice against flip-loops? And how big is the first-player advantage (komi candidate noted)? The simulation answered the second question so loudly that it restructured the game.

## 2. Method

The full ruleset as a simulator (`crossroads_sim.py`, included): cities 1–8, the 28-road deal, build-with-facing / flip-with-ko / pass, two consecutive passes ending the game, contracts scored by directed reachability in either direction, pip-sum tiebreak. Bots: RandomBot as the floor, and a one-ply GreedyBot whose evaluation scores each contract 1.0 if fulfilled, 0.45 if its cities are connected ignoring direction (one flip-war from payable), summed for both hands as a differential — enough heuristic to build purposefully, deny purposefully, and fight over facings. 150–400 games per configuration across seeds, 400-turn cap. The usual caveat is sharper here than usual and is owned in §5: a one-ply bot is myopic about tempo, and CROSSROADS is a tempo game.

## 3. Results

### Ko does not suffice — the unlimited game does not end

Greedy vs greedy under v1.0 rules: **100% of games hit the 400-turn cap**, averaging 10 builds and **389 flips**. Ko forbids re-flipping one road; the moment two or more roads are contested, both players cycle improving flips forever and no one ever passes. This is partly bot stubbornness — but only partly. The rule as written hands every contested facing to whoever is willing to outlast the other, which is exactly the "flip war won by whoever has spare moves" the v1.0 strategy notes already feared. A game between two determined players has no natural end. **Structural fix required.**

### Per-player flip budgets: terminate, but on a knife edge

Giving each player a fixed stock of flips ends every game (0 caps at budgets 4–8, games of 20–29 turns). But the mirror match exposes brutal parity sensitivity:

| Budgets (P1/P2) | 6/6 | 7/6 | 8/6 | 9/6 |
|---|---|---|---|---|
| P1 win (decisive) | 26% | 74% | 96% | 99.7% |

The last flip is close to the whole game among equal players: equal budgets give the second mover the final word (P1 26%); one extra flip overcorrects (74%); two is a forced win. A balance that swings 70 points on ±1 token cannot be tuned by tokens.

### The adopted fix: a shared pool the players fight over

Instead of owning flips, the table owns them: a **communal pool of 8 flips** — and the deck supplies its own markers, because the board already has exactly eight city cards in it. Any flip by either player **dims a city**: rotate one still-lit city card 90°. When all eight cities are dark, roads can no longer be turned. Ko stays (it still stops the cheapest exchange).

| Shared pool | 7 | **8** | 9 | 11 |
|---|---|---|---|---|
| Turn-cap hits | 0% | **0%** | 0% | 0% |
| Avg length (turns) | 19.2 | **20.0** | 21.4 | 23.3 |
| P1 win (decisive) | 38% | **35–39%** (3 seeds) | 36% | 44% |
| Contracts fulfilled (both) | 15.6 | **15.7** | 15.8 | 15.9 |

Every pool size terminates crisply; 8 is chosen because the markers are free, the count is thematic (eight cities, eight signal-fires), and the numbers are indistinguishable from its neighbours. Parity stops being an allowance and becomes *contested tempo*: spending a flip now is also spending one of the eight the endgame will be fought with — the strategy note about counting the last flip becomes literal table arithmetic on visibly dimmed cities.

### First-player advantage — inverted, and answered with the pie rule

Even with the pool, the greedy mirror shows the **second** mover winning ~61–65% of decisive games (stable across seeds): the player moving later converts the last useful action more often. The v1.0 rule "lower pip total goes first" therefore hands a measured *disadvantage* to a randomly determined player. Rather than tune a komi against bot-grade evidence, v1.1 adopts the abstract-game standard that is correct regardless of the advantage's true size or even its sign: **after examining hands, the player with the higher pip total decides who goes first.** The informed player makes the choice; whatever the seat is worth, it was chosen, not dealt. (The pip count keeps a job; nothing new to learn.)

### Health checks

With the pool: ~10 of 28 roads built, ~18 kept as contracts, ~15.7 fulfilled across both hands — scores land close, draws 1–2%, tiebreak earns its place. Skill gap: greedy beats random in ~100% of decisive games at every tested pool — the steepest gap in the collection, fitting for "the collection's chess." Twenty bot-turns of ~12 thoughtful seconds projects to roughly 10–15 human minutes, inside the box.

## 4. Changes adopted in v1.1

1. **The Signal Fires rule:** all flips draw from a shared pool of 8, marked by rotating ("dimming") one lit city per flip; all cities dark = no more flips. Replaces nothing — v1.0 simply had no limit, and provably never ended.
2. **Start rule:** higher pip total *chooses* who goes first (pie-rule style), replacing "lower pip goes first."
3. Ko retained unchanged.
4. Strategy notes updated: flip parity is now a visible, spendable resource.
5. Design footnote updated: all three open questions closed.

## 5. Caveats for the first table test

The second-mover figure comes from myopic bots that always spend the pool greedily; humans who *hoard* flips will shift it, which is exactly why v1.1 prefers the self-correcting pie rule over a numeric komi. Watch at the table: whether eight flips feels scarce enough to ache, whether dimming cities reads at a glance, and whether the Caravans variant (direction-blind routes) still wants the pool at all — analytically it shouldn't need one, since flips don't affect undirected connectivity.
