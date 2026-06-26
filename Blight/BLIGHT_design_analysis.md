# BLIGHT — Design Analysis

*How the avoidance trick-taker was validated by simulation. Companion to the rulebook; sibling to the GLEAN analysis. Follows the analysis shape in [simulation-standards.md](../.kiro/steering/simulation-standards.md).*

---

## 1. The questions

BLIGHT runs the **shared trick engine** (lead a face, follow by either face, highest hidden pip wins) but inverts the goal: a captured card's penalty is its **hidden-face pip**, and **lowest total penalty wins**. Open questions:

1. **Skill gap** — does ducking-and-shedding skill beat random play (≥1.5×)?
2. **Shoot-the-rot frequency** — how often does one player capture *every* trick (the shoot-the-moon equivalent)? Is the rule live or dead?
3. **Penalty distribution & seat fairness** — does anyone get crushed by seat position?
4. **Behaviour at 3 / 4 / 6 players.**

## 2. Method

`blight_sim.py` models the full ruleset (engine identical to GLEAN; scoring inverted):

- Captured card's penalty = its hidden (unshown) pip. Lowest total wins.
- **Shoot the rot:** winning every trick → shooter scores 0, all opponents score the round's total penalty.
- Note: the round's total penalty is **endogenous** — sum(shown) + sum(hidden) = 360 across the deck, so showing high faces lowers the table's total poison. Face choices matter.

Bots:

- **RandomBot** — uniform legal play.
- **SkilledBot** — avoids winning: when following, plays the **highest card that still loses** (sheds danger safely) or, if a loss can't be guaranteed, the lowest-hidden card to minimise damage; when void, sloughs its **worst poison** (shows a low face so the high pip lands on the winner); leads by showing a **high** face so its own hidden pip is low and it ducks its own lead.
- **GreedyBot** (shoot-feasibility probe) — always tries to *win* every trick (highest hidden), to test whether shooting the rot is even achievable.

Volume: 4,000 rounds per configuration, seed 42. Trick games terminate by construction.

**What the sim cannot model:** whether ducking feels agonising or passive; whether a surprise hidden 9 reads as drama or a gotcha; whether the shoot *threat* is exciting; teaching.

## 3. Results

### 3.1 Skill gap — the steepest of the siblings at 3–4P

One SkilledBot versus all-random, seat randomised:

| Players | Skilled win rate | Baseline | Edge |
|---|---|---|---|
| 3 | 67.4% | 33.3% | **2.02×** |
| 4 | 47.6% | 25.0% | **1.91×** |
| 6 | 23.4% | 16.7% | **1.41×** |

Avoidance rewards skill more sharply than accumulation (GLEAN's 1.74× / 1.67× / 1.49×): the duck-and-shed decision is high-leverage and a random player bleeds penalty fast. As with GLEAN, 6P is thin (1.41×) — **BLIGHT is a 3–4P game first.**

### 3.2 Seat fairness — excellent

All-skilled mirror, seat win shares (lowest penalty):

| Players | Seat shares |
|---|---|
| 3 | 33.4% / 33.0% / 33.6% |
| 4 | 24.4% / 24.4% / 25.3% / 25.9% |
| 6 | ~16–17% across all six |

Near-perfectly flat — markedly better than GLEAN, whose first leader is penalised. Avoidance has no structural seat advantage worth a pie rule.

### 3.3 Shoot the rot — rare but real

| Players | Shoots (all-skilled) | Shoots (one GreedyBot trying) |
|---|---|---|
| 3 | 0.0% | 1.0% |
| 4 | 0.0% | 1.1% |
| 6 | 0.1% | 1.6% |

Under skilled (ducking) play, shooting essentially never happens — everyone is dumping, so no one wins everything. Even a bot *actively* trying to win every trick succeeds only ~1% of the time. This is exactly the Hearts moonshot profile: **a live, legal, glorious gamble that is rarely realised** — its value is as much in the *threat* (forcing opponents to break it up) as in the rare success. The rule stays; it is not dead, but it is not a reliable strategy either.

### 3.4 Penalty distribution

| Players | Avg penalty/player | Avg spread (max−min) |
|---|---|---|
| 3 | 51.7 | 65.5 |
| 4 | 42.1 | 76.4 |
| 6 | 31.1 | 89.2 |

Large spreads — the round clearly separates the careful from the careless (good for a decisive winner, and consistent with avoidance games where the loser "eats" a lot). The wide spread is why **match play** matters: a single bad round shouldn't sink a player, so penalties accumulate across a rotating-lead match and the lowest total wins.

## 4. Design decisions adopted (v1.0)

1. **Hidden-face penalty, lowest total wins** — the validated core.
2. **Rot pile stored penalty-face-up** — the critical handling fix. Because the penalty is the *hidden* face, storing captured cards as-played would force players to remember which face was down. Flipping each captured card to its penalty face turns the pile into a self-totalling, glanceable record (orientation-as-state, per [physical-handling.md](../.kiro/steering/physical-handling.md)) — no hidden-face memory.
3. **Shoot the rot retained** — rare (~1%) but a genuine threat that shapes play; kept as the iconic high note.
4. **Match play, rotating lead** — smooths the large per-round penalty spread (§3.4); seat fairness (§3.2) means no pie rule is needed.
5. **Only Crowns Bite** teaching variant and **Partners** mode documented; the simplified variant is a scaffold, not the validated game.

## 5. Caveats for the first table test

The sim certifies that BLIGHT terminates, has the collection's steepest 3–4P trick-taking skill gap, is seat-fair, and that shooting the rot is rare-but-possible. It cannot tell us:

- **Does ducking create satisfying agony or passive low-card-dumping?** The central feel question — avoidance games live or die on whether the dodge is tense.
- **Does eating a surprise hidden 9 read as dramatic reckoning or arbitrary gotcha?** The reveal is the emotional core; if it feels random, the game fails even with a good skill gap.
- **Is the shoot threat exciting at ~1% realisation,** or does it feel like a rule that never fires? (Hearts says the threat alone is worth it — the table must confirm.)
- **Does the penalty-face-up rot pile** actually stay frictionless, and does the orientation flip get done reliably mid-game?

Per [playtesting.md](../.kiro/steering/playtesting.md), these are table questions. The recommended first session is 3P (the 2.02× skill gap and clearest duck-and-shed decisions), played as a full match, watching whether the dodge is tense and whether the hidden-9 reveals land as theatre.

---

*Analysis date: June 2026. Sim: `blight_sim.py`, ~4,000 rounds × 3 player counts × 3 measurements, seed 42.*
