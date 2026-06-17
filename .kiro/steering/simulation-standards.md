---
inclusion: fileMatch
fileMatchPattern: '*sim*.py'
---

# Simulation & Analysis Standards

How to build and use simulators and solvers. The benchmarks are `Turnover/turnover_sim.py` + `TURNOVER_design_analysis.md` and the TRIGON/TURNCOAT analyses.

## Philosophy: what simulation is for

Simulation answers **specific, bounded questions** that humans can't cheaply check — balance numbers, termination, seat fairness, parameter tuning, solver baselines. It does **not** decide whether a game is fun. Fun, pacing, table feel, social dynamics, and teachability are decided at the table (see `playtesting.md`).

Use simulation to *certify the floor* (the game ends, isn't broken, defaults are sound) so that human testing can spend its scarce time on feel.

## When to simulate vs. when to playtest

- **Simulate** for: does the game terminate? are seats fair? what's the right value for a tunable parameter? does skilled play beat random? what's the score distribution / game length? solver-optimal baselines for puzzles.
- **Playtest** for: is it fun? is it teachable? does a rule confuse people? does the handling feel good? downtime, kingmaking-in-practice, the social layer.
- A game can be "simulation validated" and still fail at the table — that is exactly why tier-2 games' priority is the **first table test**, not more sim.

## How to build a simulator

- **Model the real ruleset**, including physical handling (face randomisation on shuffle, which face is public, deal sizes per player count). Note explicitly in the analysis anything the sim *cannot* model (e.g. an announce/policing rule, bluff reads, table talk).
- **Two bots minimum**: a `RandomBot` (uniform legal play) as the mechanics floor, and a `SkilledBot` that plays the public-information strategy the rulebook's strategy notes describe (counting, scarcity, denial, etc.).
- **The skill gap is a headline metric.** Report skilled-vs-random win rate / score ratio. A thin gap (~1.0–1.2×) is a red flag for a dull game; the collection treats ~1.5×+ as healthy (the OUROBOROS lesson).
- **Volume**: enough games for stable numbers — the collection runs ~1,000+ games per configuration, tens of thousands total across a parameter sweep.
- **Termination guard**: cap turns (e.g. 600) and **report stall rate** for any game that could fail to end. A non-zero stall rate at the shipped config is a bug.
- **Sweep parameters**: test the grid of tunable values (chain limits, costs, budgets) across all supported player counts, with seat-randomised arms to measure seat advantage.
- **Solvers**: for open-information puzzles, compute the optimal/exact baseline (e.g. TWELVE TRIALS' 5.3-flip solver average) to set score tiers honestly.

## What to report (in the design analysis)

Follow the established analysis shape:

1. **The questions** the sim was built to answer (ideally the open questions from the rulebook's design footnote).
2. **Method** — ruleset modelled, bots, games per config, total volume, turn cap.
3. **Results** — tables per parameter: stall rate, avg turns/player, skill edge, seat spread.
4. **Health checks** — stalls, seat fairness, skill gap, estimated real-time length.
5. **Changes adopted** — what the data changed, with version bump (v1.0 → v1.1).
6. **Caveats for the first table test** — what the sim can't certify; what humans must check.

## Verifying combinatorial claims

Any structural/maths claim made in a design doc should be **computed, not asserted** (use `itertools`/`math.comb`, construct explicit witnesses like an Eulerian circuit or triangle partition). Record the verification method in an appendix, as `DECK_SIZE_DECISION.md` does.

## Code conventions

- Keep simulators self-contained and runnable; name them `<game>_sim.py` in the game's folder.
- Make the ruleset and bot strategies readable — they are documentation of the design as much as code.
- Seed/record enough that headline numbers are reproducible.
- Prefer `--run`-style single execution; never leave a long sweep as a blocking watch process. Property-based / large stochastic sweeps should be run deliberately and flagged as long-running.
