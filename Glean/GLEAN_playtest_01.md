# GLEAN — Playtest Report 01

**Game:** GLEAN v1.0 (Plunder variant only)  
**Players:** 3 (designer + 2 parents, experienced trick-takers, first time with this deck)  
**Symbol subset:** Full 9-symbol / 36-card deck (12 cards each)  
**Variant:** Plunder (sum of pips, no majorities)  
**Date:** June 2026  
**Preceded by:** TURNOVER (same session)

---

## Setup

First table test of GLEAN. Played Plunder scoring only — full majority scoring was not tested. The prototype uses letters A–I with numbers 1–9 on corresponding faces.

---

## Hypotheses tested

### 1. "Follow-by-either-face is learnable within 2–3 tricks."
**Confirmed (with a caveat).** Players treated the letter as the "suit" and the number on the other side as the "rank." This mental model worked well for the trick engine — following by letter felt natural to experienced trick-takers. The caveat: one player did not realise the letter/number mapping was fixed (A always = 1, B always = 2, etc.) and assumed multiple letters could have a 9. This significantly affected their play — they would have played very differently knowing the rank structure.

### 2. "The simultaneous reveal creates a dramatic beat."
**Left open.** No specific data recorded on whether the reveal felt dramatic. The trick resolution worked mechanically.

### 3. "Players feel meaningful choice in which follower to play."
**Left open.** Insufficient data to confirm or refute. The letter-as-suit / number-as-rank mental model suggests players were choosing follows by conventional trick-taking instinct (play high to win, low to duck), which is correct, but whether the *two-face* aspect added a new decision layer was not clearly observed.

### 4. "Plunder scoring is instant and satisfying."
**Refuted.** Counting the pips on both sides of all captured cards produced scores that were too large and hard to add reliably. Summing 12 cards × two faces × pips 1–9 creates totals up to ~110 per player per round. The arithmetic was tedious.

### 5. "The majority layer adds depth without overwhelming."
**Not tested.** The session did not reach majority scoring.

### 6. "A 3P round completes in 10–12 minutes."
**Confirmed (implicitly).** No length issues reported; the trick engine ran at standard trick-taking pace.

---

## Bugs found

### B1: Plunder scoring is tedious (Severity: high, design)
Summing both pips on all captured cards produces numbers too large for quick mental arithmetic. Even the house modification (score only the hidden/rank face) produced totals up to ~110, which is awkward for a single round. **Plunder needs a simpler scoring method.**

### B2: Fixed letter-number mapping not obvious (Severity: high, deck-wide)
One player did not realise A always corresponds to 1, B to 2, etc. They assumed multiple different letters could hide a 9. This misunderstanding materially affected their strategy (they couldn't price the value of winning a trick because they didn't know the rank distribution). This is a **prototype legibility issue** — the shipping deck's sign+pip design may solve it, but the playtest reveals that the "each sign has a fixed rank" fact needs explicit teaching.

### B3: Public harvests feel wrong (Severity: medium, design tension)
Players disliked public harvests. In their trick-taking experience, remembering which cards have been played is part of the skill. Having all captured cards openly examinable felt like it removed a dimension of play.

**Design tension:** the rulebook mandates public harvests because majority scoring counts both faces, and hiding that information would create a hidden-face memory burden (violating the physical-handling principles). But Plunder doesn't *need* public harvests — it just sums pips. And even for majority scoring, the question is whether *full* inspection of both faces is needed, or whether simply keeping harvests face-up (showing the winning/hidden face, as in BLIGHT's rot pile) is sufficient.

### B4: 9-pip cards feel overpowered (Severity: low–medium, design question)
Under Plunder scoring, a 9-pip hidden face almost guarantees winning the trick *and* is worth the most points. There's no tension between "this card wins" and "this card scores" — they're the same thing. The player with more 9-hidden cards has both the strongest trick-winning power and the highest scoring potential.

**Is this a bug or a feature?** Under majority scoring, this is less of a problem because winning a trick with a 9 doesn't directly score 9 points — it advances you toward the Crown majority (worth 9 if claimed) but also toward whatever sign was led (which might be worth less). The problem is Plunder-specific: when points = pips, high pips dominate both axes.

---

## Observations

- **Letter = suit, number = rank** was the instinctive mental model. Players naturally fanned by letter (grouping same-letter cards, though each letter only appears on one face of each card) and read the number as strength. This is worth noting for how the game presents itself — the trick engine maps cleanly onto conventional trick-taking vocabulary when framed this way.
- **The trick engine works.** Follow-by-either-face functioned without confusion once the letter/suit model clicked. The core mechanic is sound.
- **Plunder as a teaching scaffold did its job** — it got the engine running. But it's not a satisfying game in its own right with current scoring.
- **The session reached the trick engine's questions but not the majority game's questions.** The most important open hypotheses (nine-majority counting, majority-as-motivation-during-play) remain untested.

---

## Verdict: **Iterate**

The trick engine is confirmed as learnable and functional for experienced trick-takers. Plunder scoring needs rework — the current "sum all pips" is arithmetically unpleasant and makes high cards doubly dominant. The majority game remains the intended destination but has not yet been tested. The public-harvest question is a design tension to resolve.

---

## Concrete changes to consider

### Plunder scoring alternatives (for the teaching variant)

The current Plunder rule ("sum both pips of every captured card") fails on two counts: the totals are too large, and high-pip cards dominate both trick-winning and scoring with no tension.

Candidate replacements — each should be evaluated against:
- (a) Is the arithmetic fast?
- (b) Does it create tension between winning and scoring?
- (c) Does it teach something about the full game?

| Candidate | How it works | Total range (12 cards, 3P) | Tension? | Teaches majority? |
|---|---|---|---|---|
| **Count cards** | 1 point per card captured | 0–12 | Win/lose only; no card quality | No |
| **Hidden face only** | Score only the revealed (hidden) pip per captured card | ~30–70 | None — same face wins and scores | No |
| **Shown face only** | Score the face that was *shown to follow* (led sign's pip) per captured card | ~30–70 | Yes — the led sign's pip is the reward, not your hidden strength | Partial |
| **Card count per sign** (proto-majority) | 1 point for each card carrying a sign, most-of-each-sign claims it, claimed sign = 1pt | 0–9 signs | Yes — overlap matters | Yes |
| **Tricks won × trick size** | If N players, each trick = N pts to winner | 0–36 (at 3P: 12 tricks × 3) | Win-only; no card quality | No |
| **Fixed trick value** | Each trick won = 1pt | 0–12 | Pure win/lose | No |

**Recommendation:** "Card count per sign (proto-majority)" is the best bridge — it's the majority game with the pip-value layer removed (every sign is worth 1 point if you claim it). Totals range 0–9, arithmetic is trivial (just count and compare), and it directly teaches the majority mechanic. Then the full game adds "claimed signs are worth their pip" on top. **[ADOPTED — the rulebook's Plunder variant is now proto-majority; the old pip-sum Plunder is retired with a note explaining why.]**

### Public harvests

Three options:
1. **Keep public harvests** (current rule). Accept the "feels wrong" feedback as a learning curve — the majority game genuinely needs countable captures.
2. **Face-up but no inspection.** Harvests show the winning (hidden) face only, as they naturally land. Players can see *what* you won but checking the other face requires memory or deduction. This is closer to normal trick-taking (played cards are face-up in a won-tricks pile, not re-examined).
3. **Hidden harvests.** Won tricks are stacked face-down. Majority counting happens only at round-end. Memory of what's been played matters during the round.

Option 2 is probably the sweet spot for testing next time — it respects their trick-taking instincts while still allowing the majority count at round-end (flip all cards in harvests and count). **[Partially actioned: a *Closed Harvest* variant (option 3 — face-down won tricks, count at round end) is now documented in the rulebook for players who want the memory challenge. The canonical open-harvest rule is unchanged, since the dislike formed during Plunder where the registry did nothing; re-test in the full majority game where it has a purpose.]**

### The 9-dominance question

Under majority scoring, a 9-hidden card wins the trick but doesn't *directly* score 9 — it gives you one more card toward Crown majority (worth 9 only if you end up with the most Crown cards overall). The dominance is diluted. **Test majority scoring before treating this as a bug.** If it persists under majorities, consider: tricks won by sloughs (which can't win) or some other counterweight.

### Deck-wide: teach the rank structure explicitly

The fact that each sign has a *fixed* rank (Crown is always 9, Moon is always 1) must be taught before GLEAN, not assumed. Add to the teaching script: "There are 9 signs, and each one has a rank — Crown is always 9 (the strongest and most valuable), Moon is always 1 (the weakest). A card always pairs two different signs, so it has two different ranks, one per face." **[ADOPTED — a "Sign *is* rank" callout is now in the rulebook's Components section; also logged deck-wide as `DECK_PLAYTEST_FINDINGS.md` F4.]**

---

## What to test next

1. **Majority scoring** — the real game. Use the "proto-majority" variant (1pt per claimed sign) as the entry if full pip-value scoring feels heavy.
2. **Harvests face-up but not freely inspectable** — does this feel better while still supporting end-of-round counting?
3. **Does the 9-dominance flatten under majorities?** Specifically: does winning every trick you contest still guarantee winning the round, or does selective contesting (ducking to save strength for key tricks) emerge?
4. **Re-test with explicit rank teaching** — does knowing the fixed rank structure change the experience?
