# CROSSROADS — Playtest Report 01

## Setup

- **Game:** CROSSROADS
- **Version tested:** Pre-v1.1 (simplified — flips disabled)
- **Players:** 2
- **Symbol subset:** 7-symbol (game 1), 9-symbol (game 2)
- **Date:** June 2026
- **Conditions:** Deliberate no-flip condition to isolate the core connection mechanic before layering in the flip economy.

---

## Hypotheses tested

The recorded first-table questions for CROSSROADS ([COLLECTION_OVERVIEW.md](../COLLECTION_OVERVIEW.md)) are:
1. Does eight flips ache properly?
2. Does dimming read at a glance?

These were **not directly testable** in this session because flips were disabled. The session instead addressed a prior question: *does the core connection and contract mechanic work at all before adding the flip economy?*

### H1: The 7-symbol deck provides enough decision space for meaningful play

**Refuted.** The 7-symbol deck did not provide enough options to build meaningful connections or fulfil contracts. With fewer cities and roads, the network was too sparse and the choice space too small to generate interesting decisions. Additionally, a deal error meant players did not hold equal hands, which felt unfair and undermined confidence in the results.

**Conclusion:** 7 symbols is too small for CROSSROADS. The 8-symbol / 28-card configuration specified in the current rulebook is correct.

### H2: The 9-symbol connection mechanic produces interesting decisions without flips

**Confirmed with caveats.** The larger deck played better. Both players found meaningful choices in route-building and contract management. However, two problems emerged (see Bugs below).

### H3: Perfect information creates a manageable cognitive load

**Confirmed.** Both players independently discovered a natural cognitive shortcut: setting aside cards from hand that were already fulfilled contracts (roads they would never build). This reduced the active decision space over time and made the game feel more manageable as it progressed. The behaviour was unprompted and emerged in both players.

---

## Bugs found

### 1. First-turn paralysis (severity: medium)

**Category:** Downtime / unfun incentives  
**Observation:** With 14 cards each and 28 possible builds, the opening move felt arbitrary. There was no obvious anchor for decision-making and no clear "good" first play. This slowed the start and may be inherent to the game's wide-open structure.  
**Possible mitigations:** Experience may resolve it; alternatively, a structural opener (e.g. mandatory first build touching a specific city) could anchor the start. Needs further testing before designing a fix.

### 2. Asymmetric readiness to end (severity: high)

**Category:** Unfun incentives / pacing  
**Observation:** Both players reached points where their hand felt optimised and further builds would only help the opponent. The instinct was to stop and score — but the current double-pass end condition means player A, ready to pass, must watch player B continue taking beneficial turns. This felt unfair.  
**Variant discussed:** Player A signals readiness; player B gets one more turn; then score. Flagged as potentially encouraging premature signalling to cut off an opponent.

### 3. Deal equality not enforced (severity: low, setup issue)

**Category:** Rules ambiguity  
**Observation:** A deal error in the 7-symbol game meant unequal hands, which felt unfair. The rulebook should reinforce that equal hands are critical.

---

## Flip mechanic — discussed but untested

The group discussed the implications of adding the v1.1 flip economy without playing it. Key concerns:

- **Instability of banked contracts.** The emergent contract-banking behaviour works because commitments are stable without flips. With flips, a single road reversal could break multiple contracts across both hands simultaneously. The mental overhead of tracking this is significant.
- **Last-turn destruction.** A player could have critical roads flipped on the final move, collapsing contracts at the whistle. Whether this is exciting conflict or frustrating is the central design question.
- **Possible upside.** The flip economy may be what gives the game its strategic depth and differentiates it from a pure connection puzzle. The Signal Fires pool as a visible shared resource could make conflict feel meaningful rather than arbitrary.

---

## Physical handling

**What worked:** A layout convention emerged organically and was consistent between players — when building a road from city A to city B, place the card with city B's face up, touching city A's card, angled roughly toward city B. This keeps the source city as a physical anchor and the destination face immediately readable.

**Recommendation:** Formalise this convention in the rulebook.

---

## Rule-change candidates

| # | Change | Tied to observation |
|---|---|---|
| 1 | Formalise the physical layout convention (card touches source city, shows destination face) | Physical handling — emerged organically in both players |
| 2 | Reinforce equal-deal procedure in setup text | Deal error in 7-symbol game |
| 3 | Revisit end-of-game trigger (double-pass may need replacing) | Asymmetric readiness bug |

---

## Verdict: Iterate

The core connection mechanic works at 9 symbols without flips. The game produced interesting decisions, emergent cognitive shortcuts, and real end-game tension. Two significant bugs (first-turn paralysis, asymmetric end condition) need attention but are addressable.

**Priority next steps:**
1. Table-test the 9-symbol deck *with* flips enabled (full v1.1 rules) to assess the flip economy — this will finally address the recorded first-table questions about whether eight flips ache and whether dimming reads.
2. Revisit the end-of-game trigger.
3. Formalise the physical layout convention in the rulebook.
4. Confirm equal deal procedure is clearly stated in setup.
