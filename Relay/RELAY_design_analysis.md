---
record_type: game
game: "RELAY"
state: In the workshop
players: [2, 3, 4]
player_count: "2, 3, 4"
duration: "20–25 min"
genre: "Network route race"
complexity: Medium
min_players: 2
max_players: 4
min_minutes: 20
max_minutes: 25
physically_playtested: false
public_document: "Relay/RELAY_design_analysis.md"
next_step: "Decide the open points in the RELAY_rulebook.md draft (place markers at 4P; one action vs build-then-re-aim; build connectivity), then vet it and table it at 2P or 3P."
catalog_order: 20
---
# RELAY — Design Analysis (structural sim)

*Concept: [NEW_GAME_CONCEPTS.md §14](../NEW_GAME_CONCEPTS.md). Sim: [relay_sim.py](relay_sim.py). 250 games/cell, seeds 42 + 7, 1-ply bots. Player count scales by subset: 2P = 7 signs/21 cards, 3P = 8/28, 4P = 9/36. Hand 3, market 3, 3 face-up goals, shared flip pool 6/8/9.*

This run decided the open fork (goal-race vs node-majority) and, in doing so, **reversed the armchair prediction** in the concept sheet that node-majority would have the stronger flips. It does not. The sim is the reason we know.

## What was tested

Two forks on one skeleton (draft → build a directed edge → optional re-aim, bounded by a shared flip pool):
- **GOAL-RACE (deck-only):** claim public goal cards by completing a directed route to the goal's destination.
- **NODE-MAJORITY (cube kit):** own the edges you aim; control a sign by majority of votes aimed at it; score its pip.

Four questions: termination, skill gap (≥~1.5×), pass-to-win (should be dead), and **flip-relevance** (compare each fork with vs without the flip action — the fork-deciding metric).

## Headline results (seeds 42 / 7)

| | GOAL-RACE | NODE-MAJORITY |
|---|---|---|
| Terminates (caps) | **0%** (24–45 turns) | **0%** (29–52 turns) |
| Skill gap 2P / 3P / 4P (×fair) | **1.9 / 2.8 / 3.6** | 1.95 / 2.5 / 2.6 |
| Greedy win-rate at 4P | **~89–94%** | ~65–67% |
| Draw rate (2P/3P/4P) | 2–5% | 7–10% |
| Pass-to-win (passer score) | **0** (wins 0%) | **0** (wins 0%) |
| Flips: skill ON → OFF | **1.9→1.8, 2.8→2.4, 3.6→2.9** (flips *add* skill) | 1.95→1.96, 2.5→2.6, 2.9→3.0 (flips *don't*) |
| Share of scoring from flips | **~22–28% of claims come via a flip** | flips used (6–9/game) but flat/negative on skill |

## Reading

1. **Both forks terminate and kill pass-to-win.** The bounded flip pool fixes the CROSSROADS non-termination trap (an early unbounded-flip build looped 100% to the turn cap — same lesson, caught and fixed). A do-nothing player scores exactly 0 in both forks: you score only by completing routes / owning votes, so hoarding is structurally worthless. Pass-to-win cannot exist here.

2. **Goal-race has the better skill gap**, and it grows with player count (greedy wins ~89–94% at 4P vs node-majority's ~65–67%, where random catches up). Node-majority is **noisier and more tie-prone** (draws up to 10% at 4P) because sign-majorities tie often.

3. **The decisive surprise — goal-race also has the *more relevant* flips.** Removing flips drops the goal-race skill gap everywhere (e.g. 4P 3.6→2.9), and ~a quarter of all goal claims are made *by* a flip (re-aiming completes a route). In node-majority, removing flips leaves the skill gap **flat, and at 4P it rises** (2.9→3.0) — i.e. the flip pool there mostly lets weaker players disrupt the leader (a kingmaking/noise signal) rather than rewarding skill. The concept sheet bet node-majority would be the flip-centric fork; the data says the opposite.

## Decision

**Adopt the GOAL-RACE (deck-only) fork. Drop node-majority.** Goal-race wins on every axis that was supposed to favour node-majority and several that weren't: healthier and more scalable skill gap, fewer ties, *more* relevant flips, no GLEAN scoring overlap — and it needs **no cube kit**. Node-majority's only hoped-for edge (flip-centrality) did not materialise, and it carries ties, a kingmaking signal at 4P, the GLEAN overlap, and a component cost. The component-policy question that motivated the cube kit is therefore moot: the better game is the deck-only one.

## Caveats (per simulation-standards / agent-discipline)

- **1-ply bots** — a floor, not a ceiling. Node-majority's flips *might* reward deeper lookahead the greedy bot can't see; but the goal-race is judged on the *same* 1-ply bots, so the comparison is fair and goal-race wins it.
- **Draft skill is understated** — bots draft with a light heuristic and no build look-ahead, so the real skill gaps are likely higher than reported (these are floors).
- **"×fair" inflates with player count** (fair = 1/n); read the absolute greedy win-rate alongside it (goal 4P ~89–94% vs node ~66%).
- **Parameters unswept** — goal pool (5/6/7), flip pool (6/8/9), hand (3) are first guesses. All goals get claimed every game (claims/game = pool), which is fine for contention given the healthy skill gap but suggests room to make goals scarcer/harder if the table wants more tension.
- **Kingmaking and fun are table questions.** The 4P node-majority "flips help random disrupt the leader" is a sim signal, not proof; and whether goal-race *feels* like more than a connection race (and isn't too close to CROSSROADS) only the table answers.

## Next step

Goal-race clears the structural gate at 2–4P. Per [focus-priority.md](../.kiro/steering/focus-priority.md), the cheap remaining work is a short rulebook draft (deck-only goal-race), then a first 2P + 3P table test for the fun, interaction, route-tracing legibility, and CROSSROADS-distinctness questions a sim can't answer.

**Update (November 2026):** the rulebook draft now exists: [RELAY_rulebook.md](RELAY_rulebook.md) v0.1, written from the sim's GOAL mode. The draft surfaced a physical gap the sim can't see: a road's source is its pressed face, so the web is readable only if each road touches a visible marker for its source place. The removed Star cards (2P) and Crown cards (3P) supply those markers. At 4P no cards are spare (see §4P place markers below). The draft's design notes also list two places where the concept and the sim differ: build-then-re-aim vs one action, and the build-connectivity rule.

## Re-run at 1,000 games per cell (November 2026)

`python relay_sim.py --games 1000 --seed 42 --goal-only` (GOAL fork only; the NODE fork stays dropped). The table above came from 250 games per cell; these replace it as the headline numbers. They agree within ~0.2× everywhere.

| | 2P (7 signs) | 3P (8 signs) | 4P (9 signs) |
|---|---:|---:|---:|
| Length (turns) | 24.8 | 34.8 | 44.9 |
| Turn-cap hits | 0.0% | 0.0% | 0.0% |
| Draws | 2.3% | 3.0% | 4.2% |
| Greedy win vs random | 96.0% (1.92× fair) | 93.7% (2.81×) | 92.5% (3.70×) |
| Claims via a flip | 22.7% | 24.4% | 26.7% |
| Passer score (wins) | 0 (0%) | 0 (0%) | 0 (0%) |
| Skill gap, flips on → off | 1.91 → 1.74× | 2.83 → 2.37× | 3.68 → 3.08× |

All 1,000 games per cell, 1-ply bots, seed 42. The greedy seat rotates across positions; the first player is always seat 0. Seat order is measured separately below.

## Seat fairness (November 2026)

`python relay_sim.py --seats --games 2000 --seed 42` (and `--seed 7`; add `--signs4 8` for the Option B map). GOAL fork, every seat greedy, the starting seat rotated each game, results grouped by turn position. 2,000 games per player count per seed. Win share is among decided games (fair = 1/n).

| Table | Win share by position, 1st / 2nd / 3rd / 4th (seed 42) | Seed 7 | Draws (42 / 7) |
|---|---|---|---:|
| 2P, 7 signs | 50.7 / 49.3% | 49.0 / 51.0% | 2.6 / 2.2% |
| 3P, 8 signs | 33.5 / 33.2 / 33.3% | 32.7 / 35.5 / 31.7% | 4.6 / 4.0% |
| 4P, 9 signs | 25.2 / 25.3 / 26.8 / 22.7% | 25.9 / 24.5 / 25.1 / 24.5% | 4.5 / 5.0% |
| 4P, 8 signs (Option B) | 24.4 / 25.3 / 23.6 / 26.7% | 25.7 / 23.2 / 25.6 / 25.5% | 4.9 / 4.9% |

Mean score by position never differs by more than 0.8 points at any count.

**Reading:** no seat advantage. Every position stays within ~2.3 points of fair, which is about two standard errors at 4P (~1 point per position). No position leads or trails at both seeds: the 22.7% for the 4P fourth seat at seed 42 is 24.5% at seed 7. The 4P marker options don't differ on seat order either. *Caveat:* 1-ply bots. A first-player edge from seeing the opening market first could still show up with deeper play or at the table.

## 4P place markers — options for the designer (not decided here)

The problem: at 4P all 36 cards are roads or goals, so there's nothing left to mark the nine places. The 2P/3P markers come from the removed cards.

**Option A — RELAY is a 2–3 player game.** Record `players: [2, 3]`.
- *For:* no new rule or component. Markers are deck-native at both counts, and both are already simulated (1.92× / 2.81×).
- *Against:* loses the concept's "designed for 2–4" goal, and with it the subset-scaling story (adding a player adds a sign). 4P route play is left uncovered in the collection; CROSSROADS is 2P only.

**Option B — 4P plays on 8 signs (Moon–Star, 28 cards), using the Crown cards as markers exactly as at 3P.** Sim evidence (`--signs4 8`, 1,000 games, seed 42):

| 4P on 8 signs | Result |
|---|---|
| Length | 36.5 turns (~9 actions each, vs ~11 on 9 signs) |
| Turn-cap hits / draws | 0.0% / 5.2% |
| Greedy win vs random | 88.8% (3.55× fair) |
| Claims via a flip | 25.7%; skill gap 3.54× with flips vs 2.51× without |

- *For:* deck-only, no new component, the same setup as 3P, and the sim stays healthy. Flips matter *more* than on 9 signs (removing them costs 1.03× of skill gap vs 0.60×).
- *Against:* the subset no longer grows with the table (3P and 4P share a map), so the deal is tighter: 12 cards in hands and a 6-card stock. Slightly more draws. This sim kept the 9-flip pool and 7 goals, which are untuned for 8 signs.

**Option C — 4P keeps all nine signs with nine external place markers** (a ring sketched on paper, nine coins labelled with sign names, or a printed ring in the rulebook).
- *For:* plays exactly the simulated 9-sign game (3.70×), and keeps the subset-scaling story intact.
- *Against:* a component the deck can't supply. The collection's generic counter kit (C5) is unlabelled, so this needs either a new labelled-marker class or a printed sheet, which the component policy resists. A sketched ring is a free prototype method, but not a product answer.

**Recommendation (for the designer to accept or reject):** **B** is the smallest honest fix if 4P matters: it stays deck-only and has sim support. **A** is the cleanest if it doesn't. C is worth it only if a printed reference sheet becomes a collection-wide component anyway (see DECK_CONVENTIONS T2). Until you choose, RELAY stays In the workshop with `players: [2, 3, 4]` unchanged.

*Caveat:* 1,000 games per cell meets the collection standard. The bots are still 1-ply, so the gaps are floors.
