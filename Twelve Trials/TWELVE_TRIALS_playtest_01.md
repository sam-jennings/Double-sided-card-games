# TWELVE TRIALS — Playtest Report 01

## Setup

- **Game:** TWELVE TRIALS
- **Version tested:** v1.0
- **Players:** 1 (solo), also tried open-table 2P co-op
- **Symbol subset:** 9-symbol / 36-card full deck
- **Date:** June 2026
- **Conditions:** Exploratory first play. Stopped tracking flips partway through to focus on understanding the puzzle structure and testing completion difficulty.

---

## Hypotheses tested

The recorded first-table questions for TWELVE TRIALS (`COLLECTION_OVERVIEW.md`) are:
1. Does a thoughtful first game land near 7 flips?
2. Does the trio-verification flow feel fiddly?
3. Does the 840-almanac depth reveal itself or stay invisible?

### H1: Does a thoughtful first game land near 7 flips?

**Left open.** The player stopped counting flips mid-session to focus on whether the puzzle could be completed at all. No final flip count recorded.

### H2: Does the trio-verification flow feel fiddly?

**Confirmed — fiddliness is real, but from a different source than expected.** The issue is not checking whether three cards form a valid trio — it's the physical overhead of constantly moving cards between staging groups (individual cards sorted by face-up letter, completed trios, sets of trios with distinct symbols). The game takes up a lot of table space and cards are in near-constant motion.

### H3: Does the 840-almanac depth reveal itself or stay invisible?

**Partially confirmed.** The player initially tried to find trios without worrying about seasons. Eventually realised that trios need to be assembled in sets of three Steiner triples (seasons where each uses all 9 symbols once) after studying how the almanac is structured. The deeper combinatorial structure did surface — it was a discovery moment, not invisible — but it required active study of the almanac layout rather than emerging naturally from play.

---

## Bugs found

### 1. Table space and card movement overhead (severity: high)

**Category:** Physical handling / downtime  
**Observation:** Cards are constantly being moved between different staging groups — sorted by visible symbol, then into candidate trios, then into trial seasons. The game sprawls across the table. This is not a handling *error* (all information is open and inspectable) but it is a handling *burden*. The physical cost of exploring the puzzle is high.

### 2. Tracking flips by card orientation is unintuitive (severity: high)

**Category:** Physical handling  
**Observation:** The current rule marks a flipped card by turning it sideways. In practice, keeping cards in a fixed orientation is not realistic given how much they move between groups during the solve. The tracking method conflicts with the physical reality of the puzzle — you need to pick cards up, regroup them, compare them to other cards, and put them back. Orientation gets lost.

### 3. Flip-counting abandoned mid-game (severity: medium)

**Category:** Pacing / cognitive load  
**Observation:** The player chose to stop tracking flips and focus purely on completion. This suggests the flip-counting scoring layer adds cognitive overhead on top of an already demanding spatial puzzle. Whether players will naturally want to optimise flips or just solve the puzzle is an open question — but the instinct to drop the scoring in favour of "can I do this at all?" is a signal.

---

## What worked

1. **The puzzle is genuinely engaging solo.** The player found it satisfying to work through the trio-finding and season-assembly challenge.
2. **Open-table co-op works naturally.** Two players discussing the same open puzzle felt comfortable — no hidden information means no co-op friction.
3. **The almanac structure reveals itself.** The shift from "find any trios" to "trios must form complete seasons" was a real discovery moment.

---

## Rule-change candidates

| # | Change | Tied to observation |
|---|---|---|
| 1 | Find an alternative to sideways-orientation for tracking flips — tokens, a separate "flipped" zone, or a written tally | Orientation tracking fails when cards move constantly |
| 2 | Consider whether the game needs a physical "workspace" convention (e.g. designated zones for unsorted / candidate trios / locked seasons) | Table space sprawl |
| 3 | Consider a "completion mode" variant where flips aren't scored — just solve the almanac | Player instinct was to drop scoring and focus on completion |

---

## Verdict: Iterate

The core puzzle works and is engaging. The almanac structure surfaces as a genuine discovery. Open-table co-op feels natural. But the physical handling needs attention: the sideways-orientation flip-tracking method doesn't survive contact with the reality of constant card regrouping, and the game's table footprint is large. These are solvable problems — a different tracking method (tokens or tally) and a clearer workspace convention could address both.

**Priority next steps:**
1. Design and test an alternative flip-tracking method that survives constant card movement.
2. Try a structured workspace layout (zones for unsorted / candidate / locked cards).
3. Replay with flip-counting from start to finish — does a thoughtful solve land near 7?
4. Test whether a "completion mode" (no flip scoring, just solve the almanac) has value as a learning/introductory variant.
