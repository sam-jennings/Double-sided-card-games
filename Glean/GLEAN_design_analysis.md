# GLEAN — Design Analysis

*How the accumulation trick-taker was validated by simulation. Companion to the rulebook; sibling to the BLIGHT analysis. Follows the analysis shape in [simulation-standards.md](../.kiro/steering/simulation-standards.md).*

---

## 1. The questions

GLEAN inherits a shared trick engine (lead a face, follow by either face, highest hidden pip wins) and adds **area-majority scoring**: each of the 9 signs is worth its pip to whoever gathered the most cards carrying it. The open questions before any table test:

1. **Does "highest hidden pip wins" degenerate?** Is the winner simply whoever was dealt high cards (low skill), or is *which trick to contest* a real lever?
2. **Is the skill gap healthy** (≥1.5× over random, the OUROBOROS standard)?
3. **Score distribution, tie rate, seat fairness** — is the majority scoring well-behaved?
4. **How does it behave at 3 / 4 / 6 players** (the clean-deal counts on 36 cards)?

## 2. Method

`glean_sim.py` models the full ruleset:

- 36-card deck (all pairs of 9 signs); pip = sign number 1–9.
- Even deals: 3P=12, 4P=9, 6P=6. Every card is gathered over the round.
- Lead any card/face; follow by showing the led sign (flip if needed) on either face; slough if void. Among followers, highest hidden pip wins. Winner gathers all cards, leads next.
- Scoring: per sign, most cards carrying it (either face) claims its pip; ties leave the sign unclaimed.

Bots:

- **RandomBot** — uniform legal play (the mechanics floor).
- **SkilledBot** — leads the sign it holds most of (with a high-hidden card to win its own lead); when following, computes a *majority-aware trick value* (the pip-weighted sum of contested, still-winnable signs in the trick) and **wins cheaply** when that value clears a threshold, otherwise **ducks** with its lowest-hidden follower to save strong cards.

Volume: 4,000 rounds per configuration, seed 42. No turn cap needed — trick games terminate by construction (one card per player per trick).

**A third diagnostic — the degeneration check.** To isolate the *engine* from bot skill, the sim also replays deals under **all-random** play and measures how often the "strongest hand" (highest sum of per-card maximum pips — a proxy for raw winning power) wins. If that figure is high, the deal decides the game, not the decisions.

**What the sim cannot model:** whether nine simultaneous majorities are trackable at a real table; whether the harvest counting is frictionless; whether the captures *feel* rewarding; teaching.

## 3. Results

### 3.1 Skill gap — healthy at 3–4P, thin at 6P

One SkilledBot versus all-random, seat randomised:

| Players | Skilled win rate | Baseline | Edge |
|---|---|---|---|
| 3 | 57.9% | 33.3% | **1.74×** |
| 4 | 41.8% | 25.0% | **1.67×** |
| 6 | 24.9% | 16.7% | **1.49×** |

3P and 4P clear the 1.5× threshold comfortably. 6P sits just under — with 6 cards and 6 tricks there is little room for the contest/duck decision to express itself. **GLEAN is a 3–4P game first; 6P is the lighter, higher-variance option.**

### 3.2 The degeneration check — the deal matters, but skill matters more

Under **all-random** play, the strongest hand wins:

| Players | "Strongest hand" wins | Baseline | Deal-strength edge |
|---|---|---|---|
| 3 | 51.9% | 33.3% | 1.56× |
| 4 | 41.4% | 25.0% | 1.66× |
| 6 | 33.3% | 16.7% | 2.00× |

This is the headline caveat. The engine **does** reward the deal: a strong hand (lots of high hidden pips) wins majorities even with random decisions. But the **skill edge (1.74× at 3P) exceeds the deal-strength edge (1.56×)** — decisions outweigh the cards. GLEAN is not degenerate, but it is deal-sensitive, and that shapes two design choices:

- **Match play with a rotating lead** is core, not optional — one round per player, scores summed, so a strong deal is shared luck across the match.
- **The Passing variant** (pass 3 cards each round) is offered to soften deals further for groups that find the variance high.

At 6P the deal-strength edge (2.0×) actually exceeds the skill edge (1.49×) — another reason 6P is the casual option.

### 3.3 Score distribution, ties, seat fairness

All-skilled mirror, per round:

| Players | Avg player score (of 45) | Avg margin (max−min) | Tie rate | Seat note |
|---|---|---|---|---|
| 3 | 12.4 | 22.6 | 2.5% | seat 0 (first leader) low: 28% vs ~36% |
| 4 | 9.7 | 22.8 | 2.6% | seat 0 low: 20.5% vs ~26% |
| 6 | 6.7 | 23.3 | 2.8% | roughly flat |

- **Healthy spread** — winning margins are decisive, scores are not bunched.
- **Tie rate ~2.5%** — the tiebreak (most signs claimed) earns its place but rarely decides.
- **The first leader is disadvantaged** (leading commits information; later players respond). The rotating-lead match structure answers this directly.

## 4. Design decisions adopted (v1.0)

1. **Match play, one round per player, rotating the first lead** — smooths both the deal-sensitivity (§3.2) and the first-leader penalty (§3.3).
2. **Area-majority scoring with deadlock-on-tie** — the validated scoring; deadlocking a sign 4–4 denies its points to all, a real defensive lever.
3. **Harvest piles kept public and examinable both sides** — majorities count both faces, so the pile must be a re-readable registry, not a memory test (per [physical-handling.md](../.kiro/steering/physical-handling.md)). No hidden-face memory burden.
4. **The Passing and Partners variants** documented for variance control and larger counts.
5. **Plunder** retained as a teaching scaffold — explicitly *not* sim-validated. **Revised after the first table test (June 2026):** the original pip-sum Plunder (score both pips of every captured card) was dropped — totals ran to ~110 a round, the arithmetic was unpleasant, and high pips dominated winning and scoring at once. Plunder is now **proto-majority** (most cards of a sign = 1 point, max 9), which removes the large numbers and teaches the majority count directly. See [GLEAN_playtest_01.md](GLEAN_playtest_01.md).

## 5. Caveats for the first table test

The sim certifies the floor: GLEAN terminates, isn't degenerate, has a healthy 3–4P skill gap, and is roughly seat-fair under match play. It cannot tell us:

- **Is counting nine simultaneous majorities frictionless** at the table, or does flipping through harvests to settle each sign drag? This is the single biggest open question — if it drags, the table may prefer Plunder, which would change the game's identity.
- **Does the deal-sensitivity feel fair** across a match, or do strong opening hands sour the early rounds before the totals even out?
- **Do the captures feel meaningful** turn to turn, or does the majority payoff feel too deferred to the end?
- **Does leading-from-strength** read as clever, or does the first-leader disadvantage frustrate before players internalise it?

Per [playtesting.md](../.kiro/steering/playtesting.md), these are table questions, not sim questions. The recommended first session is 3P (the steepest skill gap and clearest contest/duck decisions), played as a full match, watching the harvest-counting friction above all.

---

*Analysis date: June 2026. Sim: `glean_sim.py`, ~4,000 rounds × 3 player counts × 3 measurements, seed 42.*
