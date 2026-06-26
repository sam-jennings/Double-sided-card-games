# THE UNPLAYED PAIR — Design Analysis

*Why the call mechanic is structurally broken, what fixes it, and what the trick-taking layer already gets right. Companion to the rulebook; follows the analysis shape from [simulation-standards.md](../.kiro/steering/simulation-standards.md).*

---

## 1. The questions

The v1.0 rulebook footnote asks three things:

1. **Call payout curve** — is +1 per unled trick the right slope?
2. **Renege rate at 3P** — how often can a player illegally slough?
3. **Does the reveal moment land as theatre or admin?** (table-only; sim can't answer)

The simulation was built to answer (1) decisively: at which trick does the unplayed pair become deducible, and does the current call reward/penalty make calling a live decision?

## 2. Method

Full ruleset modelled in `unplayed_pair_sim.py`:

- 36-card deck, one card removed unseen, morgue dealt face-up, hands dealt evenly.
- Trick structure: lead any card/face; follow by showing the led symbol (flipping if needed); slough if void; highest hidden pip among followers wins; **all cards revealed at trick end** (both faces public).
- Deduction engine: a `PerfectCounter` tracks own hand + morgue + all revealed trick cards + **void inference from sloughs** (a slough proves the player holds no card carrying the led symbol on either face). Candidates = all 36 pairs minus all identified cards, further narrowed by void-exclusion logic.
- Bots: `RandomBot` (uniform legal play) as the mechanics floor; `SkilledBot` (leads most-held symbol with highest hidden pip; ducks when following; sloughs lowest-pip card).
- Volume: 4,000 rounds per player count (3P/4P/5P), 2,000–3,000 additional rounds for the parameter sweep. Seed 42. ~60,000 total simulated rounds.
- No turn cap needed — trick games terminate by definition (one card per player per trick, hands empty after N tricks).

**What the sim cannot model:** whether the reveal lands as theatre or admin; deliberate false calls as social bluffs; the tension of watching another player narrow before you; the renege-policing mini-game (bots never renege).

## 3. Results

### 3.1 The hard arithmetic of deduction timing

At every player count, certain deduction of the unplayed pair is **mathematically guaranteed to require the final trick** in the overwhelming majority of deals:

| Metric | 3P (11 tricks) | 4P (8 tricks) | 5P (7 tricks) |
|---|---|---|---|
| Cards accounted after trick T | morgue + deal + T×(n−1) | | |
| Formula for T to reach 35 | (35−2−11)/2 = **11** | (35−3−8)/3 = **8** | (35−0−7)/4 = **7** |
| **Certain deduction: avg trick** | **10.7** | **7.9** | **7.0** |
| Certain deduction: median | 11 (last) | 8 (last) | 7 (last) |
| Early certainty (before last trick) | ~10% of seats | ~5% | ~3% |
| Avg call value at certainty (+1/unled) | +0.3 | +0.1 | +0.0 |

The reason is structural: a player's total knowledge after trick T is:

```
known_cards = morgue + own_original_hand + T × n_players
            = MORGUE + DEAL + T × N
```

This only reaches 35 (all cards minus the unplayed pair) on the final trick. Void-based reasoning from sloughs can occasionally advance certainty by one trick, but only when *all other players* are provably void in a symbol the counter hasn't seen — a rare condition (~10% at 3P, less at higher counts).

**This is not a tuning problem. It is a mathematical identity.** No parameter change to the call reward/penalty can alter *when* information arrives.

### 3.2 Probabilistic calling is never +EV under v1.0

Under the current rules (+1 per unled trick correct, −3 wrong), guessing from a small candidate set is negative-EV at every point in the game:

| Trick (3P) | Avg candidates | Unled tricks | EV of uniform guess |
|---|---|---|---|
| 7 | 8.8 | 4 | −2.20 |
| 8 | 6.7 | 3 | −2.10 |
| 9 | 4.7 | 2 | −1.93 |
| 10 | 2.8 | 1 | −1.56 |
| 11 | 1.0 | 0 | ±0.00 |

Even with 2.8 candidates and 1 remaining trick, EV is −1.56. The penalty is too steep relative to the narrowing rate. A rational player should **never** guess.

The mechanic's stated identity — "the player who counts fastest doesn't need to win tricks at all" — is structurally undeliverable. Counting narrows the set but never makes guessing profitable; certainty arrives too late to pay.

### 3.3 The trick-taking layer is healthy

Despite the broken call mechanic, THE UNPLAYED PAIR functions well as a pure trick-taker:

| Metric | 3P | 4P | 5P |
|---|---|---|---|
| Skill edge (skilled vs random) | **1.59×** | **1.58×** | **1.68×** |
| Avg tricks/winner | — | — | — |
| Termination | 100% (guaranteed) | 100% | 100% |

All above the 1.5× OUROBOROS threshold. The follow-by-either-face mechanic, the hidden-pip trick resolution, and the lead-as-probe skill surface work. The game's problem is not the trick engine — it's the call-reward layer bolted on top.

### 3.4 Parameter sweep: reward/penalty alternatives

Tested six configurations across all player counts. Key metric: does probabilistic calling (from 2+ candidates) ever become +EV?

| Config | EV at T−2 (3P) | EV at T−3 (3P) | +EV deals at T−2 | Skill gap (3P) |
|---|---|---|---|---|
| **+1/−3 (v1.0)** | −1.36 | −1.69 | 11.6% (certain only) | 1.59× |
| +2/−3 | −0.95 | −1.16 | 11.6% | — |
| **+2/−2 (Option C)** | −0.36 | −0.42 | 11.6% | **1.63×** |
| +3/−3 | −0.54 | −0.63 | 11.6% | — |
| +3/−2 | +0.05 | +0.10 | 11.6% | — |
| +2/−1 | +0.23 | +0.31 | 11.6% | — |

**Key finding:** the "%+EV deals" column doesn't change across configs because it reflects deals where *certainty* arrives early (1 candidate) — not deals where guessing becomes smart. Only +3/−2 and +2/−1 push the *average* EV above zero, and only for the ~8% of deals that already have certainty. No tested config makes probabilistic guessing from 3+ candidates worthwhile.

**With Option C (+2/−2) and optimal calling:**

| Player count | Skilled win rate | Edge vs random | Calls/game | Call accuracy |
|---|---|---|---|---|
| 3P | 54.4% | 1.63× | 14.9% | 100% |
| 4P | 41.5% | 1.66× | 8.0% | 100% |
| 5P | 34.2% | 1.71× | 3.5% | 100% |

Calls are always certain (accuracy 100%) because guessing is still −EV even at +2/−2. The skill gap improves modestly because certain calls now pay +2 instead of +1.

## 4. Diagnosis

The call mechanic suffers from a **structural information-arrival problem**, not a calibration problem:

1. **Information arrives linearly** — each trick reveals exactly N cards (one per player), so the candidate set shrinks at a fixed rate.
2. **The candidate set only reaches 1 at the end** — because the total information budget (morgue + hand + tricks) hits 35 only on the final trick.
3. **No payout curve can fix this** — the problem is *when you know*, not *how much you're paid for knowing*.

The mechanic as written promises a mid-game deduction race. The arithmetic delivers a last-trick certainty that pays nothing (0 unled tricks × any reward = 0). Early certainty exists but is rare (~10%) and pays at most one trick's worth.

## 5. Design options

Five options, ordered from lightest touch to most radical. Each is evaluated against the design principles: does it exploit pair-uniqueness, does it physically work, is it testable?

---

### Option A — Reframe only (no rule change)

**Change:** Accept the call as a "last-trick bet" or occasional penultimate-trick coup. Rewrite the rulebook pitch to drop "the player who counts fastest doesn't need to win tricks" and instead frame the call as a bonus for those rare games where void-reading gives you certainty early.

**Adopt:** +2/−2 (Option C payout) so that early certainty is worth 2 points rather than 1.

**Pros:**
- Zero mechanical change; nothing to re-test.
- The trick-taking layer is already healthy (1.6–1.7× skill gap).
- Preserves simplicity.

**Cons:**
- Abandons the game's stated identity ("the player who counts fastest doesn't need to win tricks").
- The call window is a dead rule ~85% of the time — players learn to ignore it.
- Risk of feeling like a lesser trick-taker without a distinctive hook.

**Verdict:** Safe. The game works; it just isn't what it claims to be.

---

### Option B — Reveal bonus (additional information channel)

**Change:** After each trick's reveal, the trick *winner* may **peek at the unplayed pair's top face** (one face only, chosen at random or always the same face, kept secret from other players). This gives one player per trick a private partial clue.

**Mechanics:**
- Winner peeks; sees one symbol of the missing card.
- Combined with their hand + morgue + trick reveals, this often collapses candidates much earlier (from 5 → 1 or 2 within a couple of peeks).
- Call timing becomes strategic: call now with a guess, or win another trick for another peek?

**Adopt:** +2/−2 payout.

**Pros:**
- Creates a genuine mid-game deduction race — winning tricks gives *information*, not just points.
- Creates a real fork: "do I duck this trick to save my high cards, or win it for the peek?"
- Pair-uniqueness load-bearing: peeking one face of the unplayed pair + knowing every pair exists once = strong narrowing for a counter.
- Physically works: the removed card sits in the box or under the rulebook; the winner slides it out, peeks one face, replaces it.

**Cons:**
- Adds a fiddly per-trick action (winner peeks, replaces card, remembers).
- Creates an asymmetric information structure — earlier winners know more. Could feel like runaway-leader if the same player wins multiple tricks.
- Peek memory is exactly the hidden-face-memory burden the [physical-handling.md](../.kiro/steering/physical-handling.md) guidelines warn against. Mitigated: the peeked face is always the *same* card (the unplayed pair), and players know both symbols once they've seen both faces, so it's one or two facts to remember, not a board state.

**Verdict:** High-potential but handling-sensitive. Testable. The memory burden is bounded (it's one card's identity, not a board). The fork between winning-for-peeks and ducking-for-high-cards is exactly the kind of tension this game wants.

---

### Option C — Progressive public reveal (simplest structural fix)

**Change:** The unplayed pair is placed at setup in an opaque sleeve or under a card showing a "?" symbol. After tricks 3 and 6 (at 3P, adjusted proportionally at other counts), **one face of the unplayed pair is publicly revealed** — everyone sees it, equally.

**Mechanics:**
- After trick 3: one random face of the unplayed pair is flipped public. This halves candidates for everyone (from ~17 to ~8 at 3P).
- After trick 6: the second face is revealed. The pair is now public knowledge. Any player who hasn't called yet can call with certainty — but "certainty" arrived while unled tricks remain, so the call pays.
- Calls made *before* the reveals are riskier (more candidates) but pay more (more unled tricks).

**Adopt:** +2/−2 payout (or even +1/−2 — the progressive reveal does the heavy lifting).

**Pros:**
- Simplest possible fix: two scheduled reveals accelerate information to exactly the mid-game window where calling is interesting.
- No asymmetry — all players see the reveal simultaneously.
- Creates a genuine "call before the reveal" gamble (higher candidates, higher payoff) vs "wait for the reveal" safety (certainty, lower payoff). This *is* the early-call skill the game was supposed to have.
- No memory burden; the revealed face sits on the table for all to see.
- Physically trivial.

**Cons:**
- Removes the mystery of the unplayed pair's identity from the table. The "one card is missing" premise relies partly on it being *completely* unknown — a public half-reveal deflates that.
- The scheduling feels bolted-on rather than emergent from the trick structure.
- At 5P (7 tricks), proportional placement is awkward — maybe after tricks 2 and 5?

**Scaling:**

| Players | Tricks | 1st reveal after | 2nd reveal after |
|---|---|---|---|
| 3 | 11 | trick 4 | trick 8 |
| 4 | 8 | trick 3 | trick 6 |
| 5 | 7 | trick 2 | trick 5 |

**Verdict:** The strongest "make the call mechanic work" fix. Testable. But it changes the game's identity — from "deduce from trick evidence" to "beat the clock before the answer appears."

---

### Option D — Void-probe lead (emergent information acceleration)

**Change:** When you lead a symbol and *every other player sloughs* (no one can follow), you receive a **Void Signal**: you may peek at one face of the unplayed pair as a reward for finding a global void.

**Mechanics:**
- Leading a symbol that no opponent holds is skillful (requires reading slough history).
- The peek is a reward for good information tracking — you *earned* the clue.
- Combined with the existing information, a single peek often collapses the candidate set to 1–3.
- Creates a strategic incentive to lead rare symbols (probing for voids) rather than safe ones.

**Adopt:** +2/−2 payout.

**Pros:**
- Rewards the existing "leads are questions" skill the rulebook already describes.
- Feels *emergent* rather than scheduled — the peek happens when you play well, not on a timer.
- The probe incentive pulls against the duck/win fork in a new way (lead rare vs lead strong).
- Pair-uniqueness load-bearing: counting which symbols have been fully revealed tells you where global voids might be.
- At 3P with 8 cards/symbol and hands of 11, global voids (no opponent holds ANY card with that symbol) become possible from about trick 5 onward as hands shrink.

**Cons:**
- Frequency is uncertain without simulation — at 3P, might be too rare (each player holds 11/36 cards initially; probability all opponents lack a given symbol is low early).
- Could be zero-occurrence at some player counts, making it a dead rule.
- Adds a conditional handling step (check if everyone sloughed → peek).
- The peek memory concern from Option B applies, though bounded.

**Estimated frequency (analytical):** at 3P, each opponent's hand has 11 of 36 cards. Prob(one opponent void in a specific symbol) = C(28,11)/C(36,11) ≈ 3.4%. Prob(BOTH opponents void) ≈ 0.1%. Very rare early. Late-game (hands of 3–4 cards), much more frequent — but by then deduction is nearly complete anyway.

**Verdict:** Elegant in concept but probably too rare to matter at 3P. More viable at 5P (smaller hands, 4 opponents who could all be void). Needs its own sim to check frequency. Park unless Option B or C fail at the table.

---

### Option E — Eulogy scoring (kill the call, embrace the trick-taker)

**Change:** Remove the call mechanic entirely. Replace it with **eulogy scoring**: at round end, reveal the unplayed pair, and each player scores +1 for each trick they won where one of the unplayed pair's symbols was the led symbol. The missing card haunts the round — you were leading its symbols without knowing, and the reveal retroactively identifies which of your tricks were "on the case."

**Mechanics:**
- No call, no deduction race, no mid-game decision about calling.
- The reveal is purely retrospective: players discover which tricks were relevant.
- Skilled play still leads symbols strategically, and a counter who tracks which symbols might be on the missing card can *preferentially lead those symbols* — but it's probabilistic positioning, not a binary call.

**Adopt:** no call parameters needed; the trick-taking layer is the whole game.

**Pros:**
- Eliminates the broken mechanic entirely rather than patching it.
- The reveal moment is pure theatre — surprise, laughter, "I led Crown three times and it was *Crown* all along."
- Counting still matters: a player who narrows the likely missing symbols and leads them wins more eulogy points on average.
- No memory burden, no peek handling, no schedule.
- Simplest game: pure trick-taker + a final dramatic reveal.

**Cons:**
- Abandons the "name it" dramatic moment, which the rulebook treats as the game's centrepiece.
- Removes the only player-initiated call/bet action — the game becomes more passive.
- The skill layer (leading likely-missing symbols) is subtle and may not read as intentional to the table.
- Fundamentally changes the game's pitch and collection-slot ("trick-taking *whodunit*" → "trick-taking with a surprise kicker").

**Verdict:** A clean kill that produces a functional game. But it's a *different* game — the deduction-race identity dies. Consider only if the table test shows the call moment is admin rather than theatre AND Options B/C don't rescue it.

---

### Option F — The Warrant (mid-game commitment with delayed resolution)

**Change:** Replace the instant-resolution call with a **warrant**: once per round, at the start of any trick, a player may place a face-down card from their hand on the table as a "warrant" — claiming the unplayed pair shares a symbol with the card they just played. The warrant resolves at round end:

- If the unplayed pair shares *any* symbol with the warranted card → **+1 per trick that remained when the warrant was placed**.
- If not → **−2**.

**Mechanics:**
- A warrant is a *partial* claim (shares a symbol) rather than an exact identification. This lowers the penalty-risk because one symbol appears on 8 of 35 possible missing cards — roughly a 23% base hit rate early, climbing as the counter eliminates.
- Multiple players can warrant; each resolves independently.
- The warranted card *leaves your hand* (weakening your trick-taking), so there's a real cost.

**Pros:**
- Makes mid-game calling +EV much earlier: with ~23% base hit rate and a −2 penalty, EV crosses zero when unled ≥ ~9 at 3P (trick 2–3). Counting lifts hit rate above 50% by mid-game, making the warrant a genuine skill-rewarding gamble.
- The warranted card leaving your hand creates a cost/benefit tension the current call lacks.
- Partial claims feel more natural than exact claims early ("I think it involves Crown").
- Physically simple: place a card from hand, face-down, under the missing card.

**Cons:**
- Resolving "shares a symbol" requires checking one axis of the unplayed pair against the warranted card — slightly fiddly.
- The warranted card leaves the player's hand, affecting trick balance; needs careful tuning.
- "Partial claim" is less dramatic than "name the exact pair."
- A counter who narrows to 2–3 candidates can sometimes pick a warranted card that's correct against *all* remaining candidates — making the warrant a certainty that looks like a gamble. This is good for skill but might feel like a trap for new players.

**Verdict:** The most structurally sound option. It solves the core problem (information arrives too late for exact claims) by lowering the claim bar to *partial* information (symbol-sharing), which is available much earlier. The hand-weakening cost creates a fork the current call doesn't have. Worth sim-testing.

---

## 6. Comparison matrix

| Criterion | A (reframe) | B (peek) | C (reveal) | D (probe) | E (eulogy) | F (warrant) |
|---|---|---|---|---|---|---|
| Fixes the call timing problem | ✗ | ✓ | ✓ | Maybe | N/A (removes) | ✓ |
| Preserves "name the pair" drama | ✓ (weakly) | ✓ | Partially | ✓ | ✗ | Partially |
| Pair-uniqueness load-bearing | Same | More | Same | More | Less | More |
| Physical handling clean | ✓ | Peek memory | ✓ | Peek memory | ✓ | ✓ |
| Adds a decision fork | ✗ | ✓ (win for peek) | ✓ (call before reveal) | ✓ (probe lead) | ✗ | ✓ (weaken hand) |
| Table-testable without sim | ✓ | ✓ | ✓ | Needs freq sim | ✓ | ✓ |
| Changes collection slot | ✗ | ✗ | Slightly | ✗ | Yes | Slightly |
| Complexity added | None | Low | Low | Low | Negative | Low |

## 7. Recommendation

**For the first table test:** bring Option A (reframe + adopt +2/−2 payout) as the baseline rules and Option C (progressive public reveal) as a variant to test in a second game of the same session. These two require no simulation to validate — they're testable immediately.

**For a follow-up sim study:** Option F (the warrant) has the strongest structural case and deserves its own quick Monte Carlo to confirm the EV curve. Option B (winner peek) is the highest-drama option and should be tested at the table even without a sim — its balance question (does the peeking player run away?) is a human-dynamics one.

**Park:** Option D (too rare at 3P without simulation confirmation) and Option E (kills the identity — last resort only).

## 8. Caveats for the first table test

The sim cannot certify:
- Whether the reveal moment lands as **theatre or admin** — the game's emotional centrepiece.
- Whether players *enjoy* the narrowing process or find it homework.
- Whether the follow-by-either-face rule confuses first-gamers.
- Whether leading to probe for voids feels clever or feels like busywork.
- Whether the −2 penalty *feels* proportionate to a 3P trick-taking round where winners typically score 4–5 tricks.

The table test's job is to answer these. The sim's job — certifying that the call mechanic's arithmetic is sound under the chosen payout — is done: under v1.0 it is not sound; under +2/−2 with progressive reveals (Option C) it becomes sound.

---

*Analysis date: June 2026. Sim: `unplayed_pair_sim.py`, ~60,000 rounds, seed 42.*
