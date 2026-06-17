# THE ORRERY — Playtest Report 01

## Setup

- **Game:** THE ORRERY
- **Version tested:** v0.1 (Apprentice / 7-symbol)
- **Players:** 1 (solo)
- **Symbol subset:** 7-symbol / 21-card sub-deck
- **Date:** June 2026
- **Setup condition:** The deal was intentionally pre-balanced — each symbol appeared visible exactly 3 times across the 21 cards. This isolated the arrangement puzzle and removed the need to decide which cards to flip.
- **Mode tested:** Standard Orrery (balanced orbit groups). Clockmaker (single-cycle) examined analytically after play, not solved at the table.

---

## Hypotheses tested

The recorded first-table questions for THE ORRERY (`COLLECTION_OVERVIEW.md`) were:
1. Does it feel distinct from TWELVE TRIALS or like a relabelled cousin?
2. Is sky debt calculation satisfying or tedious?
3. Is hidden-face verification acceptable given that inspection is always free?

### H1: Does it feel distinct from TWELVE TRIALS?

**Left open.** The pre-balanced setup removed the flip/sky-debt layer entirely, so the comparison to TWELVE TRIALS' flip-counting puzzle was not fairly testable this session. The grouping puzzle alone felt different in kind (arrangement into balanced groups vs. pattern-matching triangles), but the full experience comparison needs a normal random-deal test.

### H2: Is sky debt calculation satisfying or tedious?

**Not tested.** Sky debt was bypassed by the pre-balanced setup (debt was zero by construction). Needs a random-deal session to evaluate.

### H3: Is hidden-face verification acceptable?

**Confirmed.** Open information felt completely natural. The player could inspect, reason, rearrange, and verify structure directly with no handling problems. No hidden-face memory was needed. This supports the original design goal.

### H4: Is the standard 7-symbol puzzle meaningfully challenging?

**Confirmed.** Even with a pre-balanced deal (no flips needed), the arrangement puzzle was non-trivial. The player found it genuinely challenging to sort 21 cards into three groups where both visible and hidden faces each contain all seven symbols. This is a strong signal that the base rules do real work — the standard puzzle should not be treated as merely "easy mode."

### H5: Does the word "orbit" mislead about what counts as a valid solution?

**Confirmed (bug).** The player naturally interpreted "orbit" as requiring one continuous loop (a Hamiltonian cycle). When the third group decomposed into a 4-cycle plus a 3-cycle, it felt like a failed result even though it was valid under the written standard rules. The terminology actively directs players toward Clockmaker expectations even when playing standard Orrery.

---

## Bugs found

### 1. Terminology misleads about valid solutions (severity: high)

**Category:** Rules ambiguity / comprehension  
**Observation:** The word "orbit" implies a single continuous cycle. A valid standard solution containing split cycles felt wrong to the player. The rules must explicitly state that a standard orbit may contain several internal cycles.  
**Tied to:** H5 above.

### 2. Three distinct structures conflated in rules language (severity: high)

**Category:** Rules ambiguity  
**Observation:** The playtest surfaced three different structural targets that are too easy to conflate:

| Structure | Description | Game mode |
|---|---|---|
| Balanced cycle cover | Every symbol once visible, once hidden; may contain multiple internal cycles | Standard Orrery |
| Hamiltonian path / single chain | One chain visiting every symbol once, but not looping back | Not a current target |
| Hamiltonian cycle / full loop | One unbroken loop through every symbol, returning to start | Clockmaker variant |

The rulebook needs to distinguish these explicitly before examples.

### 3. Clockmaker difficulty underestimated in current text (severity: medium)

**Category:** Degenerate play / difficulty calibration  
**Observation:** The player could not solve Clockmaker during play. Converting a valid standard solution into three full cycles is a global recolouring/reassignment problem — much harder than the current text implies. Promoting Clockmaker to default would likely make the game too hard, especially at 9 symbols.

---

## Recorded final structure

The player's standard solution produced three balanced 7-card groups:

**Orbits 1 & 2** (full cycles):
```
A → F → B → D → C → E → G → A
A → E → F → D → G → B → C → A
```

**Orbit 3** (split — two smaller cycles):
```
A → D → E → B → A
G → C → F → G
```

This raised the core rules question: does a split pair of cycles count as one standard orbit?  
**Answer under current rules: yes.** The standard game only requires each group to show every symbol once and hide every symbol once.

---

## Outcome data

| Category | Result |
|---|---|
| Standard puzzle solved? | Yes |
| Flip count | 0 (pre-balanced setup) |
| Clockmaker solved at table? | No |
| Hamiltonian paths found? | Yes, but they did not loop back |
| Clockmaker later shown possible? | Unverified for this deal — needs solver |
| Sky debt | 0 (by construction — pre-balanced) |
| Difficulty impression | Challenging even in 7-symbol standard |

---

## What worked

1. **The standard 7-symbol puzzle has genuine bite.** Not a trivial tutorial — challenging enough to be satisfying.
2. **A mathematical discovery moment emerged.** The split third orbit revealed a subtle structural distinction that is interesting rather than broken.
3. **Open information feels right.** No need for hidden information, memory, timed pressure, or procedural turns. The player could inspect and reason directly.
4. **Clockmaker has value as a prestige variant.** Clearly appealing as an expert challenge, clearly too hard as a default.

---

## Rule-change candidates

| # | Change | Tied to observation |
|---|---|---|
| 1 | Add explicit statement: "A standard orbit may contain several internal cycles" | Terminology bug — player felt split cycles were invalid |
| 2 | Add three-level terminology (balanced cycle cover / Hamiltonian path / Hamiltonian cycle) in plain language before examples | Three structures conflated |
| 3 | Add a visible example of a valid split orbit to the rulebook | The exact confusion that occurred |
| 4 | Frame Clockmaker explicitly as a separate prestige challenge, not a scoring tier | Clockmaker difficulty far exceeds standard |
| 5 | Record sky debt explicitly at setup in future tests | Cannot assess scoring without it |

**Suggested rulebook wording for standard:**
> In the standard game, an orbit is a balanced group of cards, not necessarily one continuous loop. It may contain one cycle or several smaller cycles. The machine only cares that every symbol appears once above and once below.

**Suggested Clockmaker framing:**
> CLOCKMAKER is a separate challenge. First solve the deal normally. Then, using the same final orientations if possible, try to rearrange the cards so every orbit is one single loop through all symbols.

---

## Design implications

- **Keep standard rules as the base game.** Already meaningfully challenging; do not harden prematurely.
- **Keep Clockmaker as a prestige variant, not the default.** Converting a valid standard solution to full cycles is a global reassignment problem. Four 9-symbol Hamiltonian cycles would likely want a solver, not a human.
- **Do not make full 9-symbol Clockmaker the standard goal.** Risk of turning Orrery from a table puzzle into a computation.
- **The first-table questions should be revised** (see below).

---

## Revised first-table questions

Based on this session, the following questions should replace or supplement the originals:

1. Does the standard 7-symbol game remain satisfying across multiple deals?
2. Does the standard 9-symbol game feel manageable after learning on 7?
3. How often do standard solutions naturally produce split cycles?
4. Does the rules text make split cycles feel valid rather than disappointing?
5. Can players distinguish balanced cycle covers, single chains, and full loops without graph-theory language?
6. Is Clockmaker enjoyable as a post-solve challenge, or too solver-like for human play?
7. Does the full game (with random deal and sky debt) feel distinct from TWELVE TRIALS?

---

## Verdict: Iterate

The core concept works. The standard 7-symbol puzzle is genuinely challenging and satisfying. Open information handles perfectly. The main issue is terminology — "orbit" misleads about what counts as a valid solution. Fix the rulebook language, add explicit examples of split-cycle validity, and frame Clockmaker cleanly as a prestige variant. Then test with a random (non-pre-balanced) deal to engage the sky debt and flip layers.

**Priority next steps:**
1. Update rulebook terminology: define standard orbits as balanced cycle covers, add split-orbit example, reframe Clockmaker as separate prestige mode.
2. Replay several 7-symbol deals with random orientations — record sky debt at setup, flip count at end.
3. Test one full 9-symbol standard game before revisiting Clockmaker.
4. Watch whether split-cycle standard solutions feel satisfying once explicitly allowed in the rules.
