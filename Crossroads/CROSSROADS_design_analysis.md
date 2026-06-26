# CROSSROADS — Design Analysis

*How the 2P abstract was stress-tested by simulation, v1.0 → v1.1. Companion to the rulebook; sibling to the SYZYGY, TURNCOAT and TURNOVER analyses.*

---

## 1. The questions

The v1.0 footnote asked three things: does the endgame drag (pass timing)? Does ko suffice against flip-loops? And how big is the first-player advantage (komi candidate noted)? The simulation answered the second question so loudly that it restructured the game.

## 2. Method

The full ruleset as a simulator ([crossroads_sim.py](crossroads_sim.py), included): cities 1–8, the 28-road deal, build-with-facing / flip-with-ko / pass, two consecutive passes ending the game, contracts scored by directed reachability in either direction, pip-sum tiebreak. Bots: RandomBot as the floor, and a one-ply GreedyBot whose evaluation scores each contract 1.0 if fulfilled, 0.45 if its cities are connected ignoring direction (one flip-war from payable), summed for both hands as a differential — enough heuristic to build purposefully, deny purposefully, and fight over facings. 150–400 games per configuration across seeds, 400-turn cap. The usual caveat is sharper here than usual and is owned in §5: a one-ply bot is myopic about tempo, and CROSSROADS is a tempo game.

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


---

## 6. Player count + pass-to-win (Phase 1 simulation, June 2026)

*Responds to [playtest 02](CROSSROADS_playtest_02.md)'s CRITICAL pass-to-win finding and the designer's request to support both 2P and 3P. The simulator ([crossroads_sim.py](crossroads_sim.py)) was extended to N players (28 roads deal 14 / 9-plus-one-seed / 7 for 2 / 3 / 4 players; the single leftover at 3P seeds the board as a neutral public road) and given a `PassBot` (builds nothing, keeps every card) plus two candidate fixes. The 2P base regression still reproduces §3 (unlimited flips: 100% turn-cap; Signal Fires shared:8: ~20 turns, first mover 38% of decisive). 300 games/cell, seed 42, with the robustness rows across seeds 7/123/2024.*

### The diagnosis: pass-to-win is a *denial-awareness* bug, not a player-count bug

The decisive result is the split between adversarial and non-adversarial opponents. `GreedyBot` evaluates *own contract potential minus the mean of others'* — so it incidentally **denies** the passer (reverses/withholds roads that would complete the passer's routes). `NaiveBot` maximises **only its own** contracts and never denies — the way the playtest table actually played (everyone builds their own routes; the network connects everything).

| Passer (builds nothing) wins | 2P | 3P | 4P |
|---|---:|---:|---:|
| vs **Greedy** (denies) | 0% | 2% | 8% |
| vs **Naive** (no denial) | **75%** | **77%** | **73%** |

The naive figures are stable across four seeds (73–77%). **The bug appears at every player count, including 2P** — it is not caused by adding a third player. It is caused by opponents who don't deny. This is binding lesson 6(a) (`design-principles.md`) in the wild: the *obvious* line (build your own routes) gifts the passer free contracts; the *non-obvious* line (spend flips to deny) defeats passing but isn't taught. Playtest 02 only saw it at 3P because that's where it was tested and because flips were declined — not because 3P is special. **2P is equally vulnerable to a naive table.**

### Fix 1 — Toll Roads into the base game: works unconditionally

Toll scores a fulfilled contract +1 per road *you* built on its (shortest) route. Because the passer builds zero roads, it collects zero toll bonus, so builders overtake it even when the passer fulfils *more* contracts:

| Passer wins, with Toll | 2P | 3P | 4P |
|---|---:|---:|---:|
| vs Greedy | 0% | 0% | 0.3% |
| vs **Naive** | **0%** | **0%** | **1.7%** |

At 2P-vs-naive the passer still fulfils **9.3** contracts to the builder's 6.8 — and loses every game on tolls. Skill gap is preserved (greedy beats random ≈1.97× / 3.0× / 4.0× fair at 2/3/4P — indistinguishable from base). Toll is the recommended fix at **all** counts.

### Fix 2 — Deal-split: fixes the bug but guts the skill

Dealing K fixed contracts + (hand−K) buildable roads caps the passer's contracts at K, so pass-to-win falls to at-or-below fair share (18–32% vs naive). But it removes the keep-vs-build decision that *is* the game's skill, and the skill gap collapses toward random:

| greedy vs random (× fair) | base | split |
|---|---:|---:|
| 2P | 2.00× | 1.54× |
| 3P | 3.00× | 1.38× |
| 4P | 3.99× | **1.36×** |

4P split sits on the dull-game floor (~1.5×, `design-principles.md` lesson 6). **Rejected**: it solves a problem Toll solves better, at the cost of the depth that makes CROSSROADS "the collection's chess." (Its incidental handling benefit — a pre-sorted hand — is real but not worth the skill loss; pursue hand-load via player count instead.)

### Player count: one ruleset, not two variants

Every configuration **terminates crisply** under Signal Fires (0% turn-cap hits at 2/3/4P). The rules are *identical* across counts — build / flip-with-ko / pass, the shared 8-flip pool, Toll scoring, contracts-as-kept-cards. The **only** deal-time differences:

- **Deal size:** 14 (2P) / 9 (3P) / 7 (4P).
- **3P seed:** the one leftover card (28 = 3×9 + 1) is built as a neutral public road; 2P and 4P divide evenly with no seed.
- **Information structure (emergent, not a rule):** at 2P your rival's hand is exactly the complement of yours (perfect information — the "chess" framing). At 3P+ you know the *union* of the others' hands but not the split (partial information / deduction). This changes the *feel*, not the rules.

So 2P and 3P (and 4P) are **one ruleset with a player-count callout**, not separately-defined variants. The rulebook should state the deal sizes and the 3P seed, and note the perfect-vs-partial-information difference as flavour.

### What this leaves for the table

- Toll into base is a **sim-backed structural fix**; the table must still confirm Toll's end-game scoring (trace your route, count your roads) isn't a fiddly handling burden.
- The naive-vs-greedy split predicts that **teaching denial** (flips as a weapon against hoarders) is the real onboarding lever — a rulebook/strategy-note fix, per lesson 6(a), not a mechanics change.
- 3P/4P deal smaller hands (9/7), directly targeting the 14-card cold-start overwhelm (playtest 02 Bug 3) — to be confirmed at the table.

### Caveats

One-ply bots, as always (§5). The naive/greedy contrast is the point here, not their absolute strength: it isolates that pass-to-win is contingent on opponent denial, which a deeper bot or a thoughtful human would supply more of than NaiveBot and less reliably than GreedyBot — the truth sits between the two rows. Toll's fix does **not** depend on that contingency, which is why it is preferred over "expect players to learn to deny."


---

## 7. The 2P hand-size problem, and the unified deal (Phase 2 simulation, June 2026)

*Phase 1 fixed pass-to-win but did **nothing** for playtest 02's other HIGH bug: 14-card hands overwhelm at 2P, with or without flips. The designer's ruling that **perfect information should not be a fixed property** (players can't use it — they can barely track their own hand) removes the constraint that forced 2P to deal all 28 roads. That unlocks a fix. Sim: `crossroads_sim.py` `unified_study()`, 250–300 games/cell, seeds 42 + 7, Toll on, Signal Fires on.*

### The candidate: a fixed hand, rest set aside

Deal each player a fixed **H** roads; the remaining `28 − n·H` are **set aside, out of play** (not built, not contracts). Information becomes **partial at every count** (you no longer know the complement of your hand) — which matches how the game is actually played.

### Two structural facts the sweep revealed

**(1) Setting cards aside preserves the skill gap** — unlike deal-split. Greedy beats random at ~2.0× (2P) / ~3.0× (3P) fair at *every* hand size from 8 to 14 (both seeds). The keep-vs-build decision — the actual skill — is untouched, because you still choose which of your H cards to build and which to keep. This is the decisive advantage over deal-split (§6), which gutted the gap to 1.36×.

**(2) The full 14-card deal is the soil pass-to-win grows in.** At H=14, the network connects **91%** of all 28 city-pairs, and **87% of kept cards auto-fulfil** (7.9 of 9.1). Contracts are nearly free. Shrinking the hand starves this at the source:

| 2P | in play | builds/p | kept/p | fulfilled/p | map-connectivity |
|---:|---:|---:|---:|---:|---:|
| H=14 | 28 | 4.9 | 9.1 | 7.9 | **91%** |
| H=12 | 24 | 4.7 | 7.3 | 5.9 | 86% |
| H=11 | 22 | 4.5 | 6.5 | 4.9 | 81% |
| H=10 | 20 | 4.3 | 5.7 | 3.8 | 74% |
| **H=9** | **18** | **4.0** | **5.0** | **2.8** | **66%** |
| H=8 | 16 | 3.7 | 4.3 | 2.1 | 60% |

| 3P | in play | builds/p | kept/p | fulfilled/p | map-connectivity |
|---:|---:|---:|---:|---:|---:|
| **H=9** | **27** | **3.0** | **6.0** | **4.4** | **81%** |
| H=8 | 24 | 2.9 | 5.1 | 3.3 | 75% |
| H=7 | 21 | 2.6 | 4.4 | 2.3 | 65% |

At H=9, 2P contracts fulfil at ~56% (2.8 of 5.0), not 87%. Connections become **contested**, not free. Smaller hands fix the overwhelm *and* deepen the contract game *and* further starve pass-to-win — one lever, three problems. (Pass-to-win stays dead with Toll across all H: 2P ≤ 9%, 3P ≤ 4% vs naive, both far under the 50% / 33% fair lines.) Every cell terminates (0% turn-cap).

### Decision: unify 2P and 3P into one variation — **deal 9, set the rest aside**

Both counts use the **same rule**: deal **9 roads each**, set the remainder aside (2P sets aside 10; 3P sets aside 1 — invisible to play), Toll scoring in the base, Signal Fires, contracts = kept cards.

Why 9, and why unify:

- **9 is the playtested-comfortable number** — the Lauren & Arran session found 9 "markedly more manageable" than 14 (playtest 02, Bug 3).
- **It is literally one rule for both counts.** The only between-count difference is the size of the unused aside pile. This is the strongest possible "single variation that works for both" — there is no reason to maintain separate 2P/3P rulesets, because the two counts' different main issues (2P overwhelm; 3P pass-to-win) are both solved by the *same* two changes (fixed 9-deal + Toll).
- **Skill preserved** (2.0× / 3.0×), **pass-to-win dead**, **partial information at both counts** (matches reality and the designer's ruling), **terminates crisply**.
- **4P**, if ever wanted, is the natural full-deck case (deal 7 = all 28); heavier and denser, documented separately, not part of the 2P/3P unified variation.

### The identity shift (flag for the designer)

This retires CROSSROADS's "perfect-information chess" identity. It becomes a **partial-information tactical route/contract duel** (2P) and small-group game (3P) on one ruleset. It remains the collection's only route/connection/contract game, so distinctness holds, but `COLLECTION_OVERVIEW.md`'s "head-to-head abstract / perfect information" tags for CROSSROADS are now wrong and must change (Phase 6).

### The one open question for the table

2P at H=9 sits at the **lower edge of density** (66% connectivity, 2.8 fulfilled/player). The sim says it's contested-not-sparse and the skill gap is intact, but whether a ~8-built-road, ~3-connection 2P duel *feels* satisfying rather than thin is a fun/feel judgment only the table can make. **If 2P plays thin, H=10 is the documented fallback** (74% connectivity, 3.8 fulfilled, skill gap unchanged) at the cost of the exact 2P=3P hand-size match.


---

## 8. Draw-model alternative — evaluated and rejected (June 2026)

*The designer asked whether a smaller deal (~6) with **drawing replacement cards** beats the static deal-9. Simmed via `crossroads_sim.py` `draw_study()` (deal 6, a build auto-refills the hand from a pile, contracts = final hand, Toll + Signal Fires on). 300 games, seed 42.*

**What it fixes:** drawing solves the sparsity that kills a *static* 6-card hand. Static H=6 connects only 46% of pairs (too sparse — the 7-symbol failure mode); drawing churns ~8.4 of 28 roads into play and reaches **73%** connectivity, ~3.9 fulfilled/player — comparable to static H=9. Games still end (~19 turns, 0% caps). Pass-to-win stays dead (0% vs naive with Toll).

**What it breaks — the measured flaw:** it dilutes the **2P** skill gap toward the dull-game floor.

| 2P model | greedy vs random |
|---|---:|
| static H=9 | 2.00× |
| static H=6 (ref) | 1.96× |
| draw H=6 cap=6 | **1.60×** |
| draw H=6 cap=8 | **1.47×** |

The static-6 reference holds at 1.96×, so the small hand is not the cause — the **random refill** is. Drawing replaces a chosen card with a luck-of-the-draw card, injecting variance that compresses skill (lesson 6: ≤1.5× is the warning zone). 3P drawing is unaffected (2.95×) because multiplayer interaction supplies skill regardless — but 2P is precisely the count under rescue, and drawing makes *2P* shallower.

**What it breaks — structural (not simmable):**

1. **Face-up draw pile.** A pile of double-faced cards has no back; the top card always shows a face, so drawing is semi-open at best (`physical-handling.md`, the project's #1 failure mode). The static closed hand sidesteps this entirely.
2. **Weakened pair-exhaustion.** A road not in your hand now sits in the pile, recoverable by a draw, so "keeping a card deletes that road forever" stops holding — eroding the deck-necessity toward a generic route-builder (`design-principles.md`).
3. **More rules** (hand cap, refill timing, pile/end-of-pile handling) for a problem deal-9 already solves.

**Verdict: rejected in favour of static deal-9.** Drawing's only gain is a momentary hand of 6 vs 9 — paid for with a diluted 2P skill gap, a handling hazard, weaker deck-tie, and extra rules. Nine is already the playtested-comfortable number, so the gap closed is small.

**Parked thread:** the one draw variant that might beat static-9 is an **open draft** (choose from a face-up row), which would turn the no-card-back handling problem into a feature and likely restore the skill gap by replacing random draw with choice. It still weakens pair-exhaustion and is a larger redesign into a different game. Kept warm as a future "dynamic CROSSROADS" exploration; not pursued now.
