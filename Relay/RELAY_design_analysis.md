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
