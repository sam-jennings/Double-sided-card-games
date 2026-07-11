# DOWRY — Design Analysis & Floor Simulation

*July 2026 · simulator: [`dowry_sim.py`](dowry_sim.py) · rulebook: [`DOWRY_rulebook.md`](DOWRY_rulebook.md) (v0.1)*

## 1. The questions

Built to answer the rulebook's first-table question 1 and the standard floor checks before any table time is spent:

1. **Does even-splitting dominate?** If an honest, value-equalising cutter matches a deceptive one, the dressing layer — the reason this game exists — is dead.
2. Does the game **terminate** and is the card flow sound (12 offers, all 36 captured, stock exhausted at offer 6)?
3. Are the **seats fair**?
4. Does **skilled play beat random** (~1.5×+ is the collection's health bar)?

## 2. Method

Full 2P ruleset modelled, including physical information flow: face randomisation on shuffle, rung-2 deal glimpses, public stock-top faces at refill, offer faces public, placement revealing both faces (C6 registry). Turn cap 40 (game should always be 12).

Bots (perfect memory — an *upper bound* on human registry tracking):

- **RandomBot** — uniform legal cut, choice, and placement. Mechanics floor.
- **SkilledBot** — *deceptive* cutter: searches candidate cuts (sampled triples × splits × dressings), predicts the chooser's perceived lot values from *the chooser's* knowledge model (registry deduction over consistent hidden faces), and maximises true-kept minus true-given. Chooser: expected-value over registry-consistent hidden faces. Placement: majority-greedy.
- **HonestCutBot** — identical chooser/placement, but cuts for the most even *true* split and dresses fully informatively (best face shown). The pure even-split strategy.

Volume: ~4,750 games total, chunked runs with distinct seeds (results identical in shape across chunks). Value model is a pip/majority-threshold proxy — adequate for a floor, not a solver.

## 3. Results

| Arm | Games | Wins | Avg score | Notes |
|---|---:|---|---|---|
| random vs random | 2,000 | 986 / 1,003 / 11 shared | 17.7 v 18.0 | seats fair at the floor |
| skilled vs random (both seats) | 1,250 | skilled 1,238 (99%) | ~30.0 v ~8.3 | **skill edge ≈ 3.6× score** |
| skilled vs skilled | 500 | 219 / 276 / 5 | 17.2 v 19.0 | **second-cutter edge 55.8%** — see §4 |
| deceptive vs honest-cut (both seats) | 1,000 | **deceptive 830 (83%)** | ≈22.2 v ≈13.0 | **dressing edge ≈ 1.6–1.7× score** |

- **Stall rate 0** in every arm; every game is exactly 12 offers. Card-flow arithmetic (12 offers · 6 per player · stock empty at offer 6 · all 36 captured) verified by construction and assertion.
- **Q1 answered (bot scope): even-splitting loses decisively.** The deceptive cutter beats the honest even-splitter from both seats — the dressing layer is load-bearing, not decorative. The rubric's fastest-falsification test survives the floor.
- **Skill gap 3.6×** — far above the 1.5× health bar. Per the OUROBOROS lesson this is a floor claim from one-ply heuristics, but the *direction* is unambiguous.

## 4. Health checks & the one flag

- Termination ✓ · legality by construction ✓ · length: 12 offers ≈ 15–20 min real time (estimate).
- **Seat edge:** in the skilled mirror, the player who cuts second (and chooses first) wins ~56/44. Plausible cause: the last cut (offer 12) is made with the registry nearly closed, and the second cutter also gets the first choice while fog is thickest. Not fatal, but real. **Adopted mitigation:** rulebook match-play note — play an even number of games, alternating first cutter, summing scores. A rules-level fix (e.g. game-tie awarded to the first cutter) is left for the table.

## 5. Changes adopted

- Rulebook v0.1 → **v0.2**: added the match-play seat note and updated the design footnote with the sim certification. No rules changed — the floor passed as drafted.

## 6. Caveats for the first table test

The sim cannot certify what actually matters next:

1. **Human memory ≠ perfect memory.** The bots never forget a glimpse; humans will. The dressing edge could *grow* at the table (more fog) or the deduction could collapse into guessing (frustration). This is the central table question.
2. **Bluff-reading is unmodelled.** The deceptive bot exploits a fixed perceived-value model; humans adapt and read habits. The honest/deceptive equilibrium at the table may be richer (or swingier) than 83/17.
3. **Deduction fatigue** at 9-card hands (rulebook question 2) — feel, not maths.
4. The honest bot is one particular honesty; a human "mostly honest, occasionally poisonous" cutter is the strategy the sim cannot price.

**Next step:** one 2P table session against the rulebook's first-table questions (Q1 now sharpened to: *can humans execute and read the dressing game the sim says is there?*).
