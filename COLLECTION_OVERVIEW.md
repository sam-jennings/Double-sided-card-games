# Collection Overview

*9 symbols · 36 cards · one deck · eleven games*

The master deck is 36 double-faced cards: every pair of symbols from a set of nine appears exactly once. Any game that runs on fewer than 9 symbols uses a stated subset — no separate deck needed.

A printable prototype deck (Set D Glyphs skin, duplex A4, cut guides) lives in `Print and Play/FLIP_DECK_print_and_play.pdf`.

---

## Quick Selector

### By player count

| Game | 1 | 2 | 3 | 4 | 5 | 6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| TWELVE TRIALS | ✓ | ✓ | ✓ | | | |
| THE ORRERY | ✓ | ✓ | ✓ | | | |
| JANUS | | ✓ | ✓ | ✓ | | |
| TRIGON | | ✓ | ✓ | ✓ | | |
| TURNCOAT | | ✓ | ✓ | ✓ | | |
| CROSSROADS | | ✓ | | | | |
| FACE VALUE | | ✓ | | | | |
| THE UNPLAYED PAIR | | | ✓ | ✓ | ✓ | |
| FALSE FACE | | | ✓ | ✓ | ✓ | ✓ |
| THE COUNCIL | | | ✓ | ✓ | ✓ | ✓ |
| TURNOVER | | | ✓ | ✓ | ✓ | ✓ |

### By play time

| Time | Game | Players | Genre |
|---|---|---|---|
| ~10 min | TURNOVER | 3–6 | Party shedding |
| ~15 min | TWELVE TRIALS | 1–2 (+co-op) | Solo/co-op puzzle |
| ~15–25 min | THE ORRERY | 1–3 | Solo/co-op sorting puzzle |
| ~15–25 min | TRIGON | 2–4 | Tactical grid |
| ~15–25 min | TURNCOAT | 2–4 | Allegiance grid |
| ~20 min | JANUS | 2–4 | Co-op communication |
| ~15–20 min | FACE VALUE | 2 | Bluffing duel |
| ~20 min | FALSE FACE | 3–6 | Bluffing |
| ~20 min | CROSSROADS | 2 | Abstract route duel |
| ~25 min | THE UNPLAYED PAIR | 3–5 | Trick-taking/deduction |
| ~25 min | THE COUNCIL | 3–6 | Negotiation |

### By complexity

| Weight | Game | Notes |
|---|---|---|
| **Light** | TURNOVER | Match and flip; ages 8+ |
| **Light** | THE COUNCIL | No arithmetic, lots of talking |
| **Light–Medium** | FALSE FACE | Bluffing with a shrinking lie-space |
| **Light–Medium** | FACE VALUE | Heads-up betting bluff; the shown face is the claim |
| **Medium** | TRIGON | Grid tactics, 9 symbol abilities |
| **Medium** | TURNCOAT | Same engine as TRIGON, adds allegiance |
| **Medium** | JANUS | Co-op deduction; Hanabi-like hint rules |
| **Medium** | TWELVE TRIALS | Open puzzle; all info visible, no randomness after setup |
| **Medium** | THE ORRERY | Open sorting puzzle; sky debt gives a per-deal lower bound |
| **Medium** | THE UNPLAYED PAIR | Trick-taking with a deduction end-game |
| **Medium** | CROSSROADS | Perfect-information abstract; route + denial |

### By genre / mood

| Mood | Game |
|---|---|
| **Solo / quiet** | TWELVE TRIALS, THE ORRERY |
| **Co-op, no talking** | JANUS |
| **Head-to-head abstract** | CROSSROADS |
| **Tactical engine** | TRIGON, TURNCOAT |
| **Trick-taking** | THE UNPLAYED PAIR |
| **Negotiation / betrayal** | THE COUNCIL |
| **Bluffing** | FALSE FACE, FACE VALUE |
| **Head-to-head bluffing** | FACE VALUE |
| **Party / fast** | TURNOVER |

---

## Development Status

> **Status correction (2026-06-15).** The tier assignments below reflect the actual physical testing history. Games that have been played at the table: OUROBOROS (cut), CROSSROADS, THE ORRERY, TWELVE TRIALS. Games that have **not** been table-tested: TRIGON, TURNCOAT, TURNOVER, and all Tier 3 games.

### 🧪 Table-tested — sim-validated and physically played

These games have been both simulation/mathematically validated and played at the table by humans. Priority is iterating on findings and further playtests.

**TWELVE TRIALS** `Twelve Trials/` · 1–2 (+3P co-op) · ~15 min  
Open-information puzzle. The 36-card deck hides 840 different "almanacs" — ways of sorting all cards into 12 perfect symbol-trios. Find the best one; your score is how few flips it costs to make the deal match it. Exact solver average: 5.3 flips; unoptimised average: 9 flips. Tiers set accordingly.

*First table test (June 2026):* Solo and open-table 2P co-op. The puzzle is engaging and the almanac's season structure surfaced as a genuine discovery moment. Two handling bugs: (1) sideways-orientation flip-tracking doesn't survive constant card regrouping — cards move too much between staging groups for orientation to stay reliable; (2) the game sprawls across the table. The player stopped counting flips mid-session to focus on completion difficulty. Verdict: **iterate** — needs an alternative flip-tracking method and a workspace convention. See `TWELVE_TRIALS_playtest_01.md`.

*Outstanding questions: does a thoughtful solve land near 7 flips (untested — flip-counting was abandoned)? What tracking method replaces sideways orientation? Does a "completion mode" (no scoring, just solve) have value as a learning variant?*

**CROSSROADS** `Crossroads/` · 2 · ~20 min · Abstract · **v1.1, sim-tested**  
Route duel. Sim proved ko alone never ends the game (100% of unlimited-flip duels looped forever), so v1.1 adds **Signal Fires**: eight shared flips, paid by dimming (rotating) the eight city cards — every simulated game now ends in ~20 turns. Measured seat advantage favoured the *second* player, so the start became a pie rule: higher pip total chooses who goes first.

*First table test (June 2026):* Tested a simplified no-flip version at 7 and 9 symbols. The 7-symbol deck was too sparse; 9 symbols worked well. The core connection mechanic produces interesting decisions. Two bugs found: first-turn paralysis (no obvious anchor for the opening move) and an asymmetric end-of-game problem (double-pass rule feels unfair when players are ready to stop at different times). An organic physical layout convention emerged (card touches source city, shows destination face). Verdict: **iterate** — the flip economy (v1.1's Signal Fires) is untested and is the priority next step. See `CROSSROADS_playtest_01.md`.

*Outstanding questions: does eight flips ache properly? Does dimming read at a glance? Does the flip economy break the emergent contract-banking behaviour? Is the end-of-game trigger fair?*

**THE ORRERY** `The Orrery/` · 1–3 · ~15–25 min · Solo/co-op sorting puzzle  
Open-information orbit puzzle. Sort the full 36-card deck into four orbits of 9 cards, each showing all 9 symbols once on its visible faces and all 9 once on its hidden faces. Move cards freely; every flip costs 1 point. The sky debt (over-shown symbols vs. target count of 4) gives an exact lower bound per deal. Sibling to TWELVE TRIALS via a different decomposition (4 permutation orbits vs. 12 triangles).

*First table test (June 2026):* Tested the 7-symbol Apprentice version solo with a pre-balanced deal (sky debt 0, isolating the grouping puzzle). The standard puzzle was genuinely challenging and satisfying. Key finding: the word "orbit" misled the player into expecting a single continuous cycle (Clockmaker), when a valid standard solution can contain split cycles. The player solved standard Orrery but could not solve Clockmaker at the table. Open information handled perfectly. Verdict: **iterate** — fix terminology, keep Clockmaker as prestige variant only, then test with random deals. See `THE_ORRERY_playtest_01.md`.

*Outstanding questions: does the standard game remain satisfying across multiple deals? Does the 9-symbol version feel manageable? Does the full game (with sky debt) feel distinct from TWELVE TRIALS? Do split cycles feel valid once the rules explicitly allow them?*

---

### 🔬 Simulation validated — needs first table test

The design is analytically or simulation complete and the balance numbers are checked, but it has not yet been played by humans.

**TRIGON** `Trigon/` · 2–4 players · ~15–25 min · **~23k simulated games**  
Grid capture. Place cards, trigger symbol abilities, chain reactions. Three matching symbols in a row/column/diagonal = capture. Star is wild. The collection's flagship. Extensively simulation-tuned but never tested at the table.

> *The `Syzygy/` folder is retained as an archive of the pre-rename design record.*

*First table questions: does a capture every ~5 turns feel exciting or exhausting? Does anyone use Aurora? Is the "active player captures everything" rule legible and dramatic? Do new players grasp charging vs. re-charging within one game?*

**TURNCOAT** `Turncoat/` · 2–4 players · ~15–25 min · **~22k simulated games**  
Allegiance grid. Every card serves two signs; the visible face declares loyalty today. Flip an opponent's agent to defect them. Bury your own before rivals turn them. Built on the same engine as TRIGON but feels entirely different. Extensively simulation-tuned but never tested at the table.

*First table questions: is one activation per turn exciting or exhausting over 18 turns? Does the bury-your-own loop teach itself? Does Mask feel like a fun strong pick or a must-pick? Allied Houses versus free-for-all at four?*

**TURNOVER** `Turnover/` · 3–6 · ~10 min · Party · **v1.1, sim-tuned** (~60k games)  
Match-and-turn shedding race. Sim closed all three v1.0 questions: chain 2 and refusal 2 confirmed (zero stalls, flat seats, 1.5–1.8× skill edge, ~5-min races); Hot Well cut (it made games *longer*, not shorter) and replaced by the Wildfire variant (chain 3 — genuinely faster and sharper); Slow Match errata'd to refusal-cost 1, without which the chainless game frequently never ends.

*First table questions: announce-rule policing fun? Does chaining feel as bridge-burning as the maths says?*

---

### 📋 Rulebook complete — untested at the table

These five have full rulebooks incorporating lessons from the TRIGON/TURNCOAT simulation work and the OUROBOROS post-mortem. None have been played.

**JANUS** `Janus/` · 2–4 · ~20 min · Co-op  
Each player sees one face of their own cards; the table sees the other. Co-operate to raise symbol-triangle gates using half-seen hands. Hint grammar à la Hanabi, but the deduction is exact (every pair is unique, so a single hint can fully identify a card).  
*Test focus: omen economy pacing; hint grammar ease of first game.*

**FALSE FACE** `False Face/` · 3–6 · ~20 min · Bluffing  
Play a card and claim its hidden face aloud — truthfully or not. Challenge to force a reveal: liar takes the pot, honest player challenged means the challenger takes it. Because every pair exists once, the lie-space provably shrinks each turn.  
*Test focus: ledger pacing; whether first-game players can price a lie.*

**THE UNPLAYED PAIR** `Unplayed Pair/` · 3–5 · ~25 min · Trick-taking  
One card is removed unseen before dealing. Classic trick structure, two twists: follow by either face of any card; the winning card's hidden face reveals at trick-end (feeding deduction). Final bet: name the unplayed pair for a big bonus.  
*Test focus: hidden-face ranking rule simplicity; 4P balance.*

**FACE VALUE** `Face Value/` · 2 · ~15–20 min · Bluffing duel  
Heads-up betting bluff. Both players commit a duel card — the face you *show* is your only claim about the strength you *hide*. Raise stakes from hand, call to showdown (higher hidden pip; pair-uniqueness makes ties impossible), or fold to keep your card unrevealed. Cold Read: name the exact hidden symbol for double-or-nothing — a gamble early, arithmetic late. Pacing sim-checked (~12 duels, skilled bot beats random 94%).  
*Test focus: fold frequency; cold-read timing; whether acting last reads as the advantage it is.*

**THE COUNCIL** `Council/` · 3–6 · ~25 min · Negotiation  
Three issues tabled each round; everyone secretly commits one card showing their chosen issue. Then, in seat order, anyone may flip their card to defect — to its one specific alternative. Lone backers take an issue's entire pot. Stacks grow for unresolved issues.  
*Test focus: kingmaking at 5–6P; pot arithmetic staying frictionless.*

---

### ❌ Cut

**OUROBOROS** `Ouroboros/` — Solo serpent-building puzzle. Demoted after live testing (June 2026): too luck-driven, and the "open symbol" lived under the serpent's head making it awkward to track. Retained as a design record. Three lessons carried forward to all subsequent designs: (1) solo games on this deck should use open information, not hidden-face memory; (2) any state the player must track constantly must be *visible*; (3) a thin skill gap between random and skilled play predicted a dull table accurately.

---

## Recommended play order for learning the collection

1. **TURNOVER** — learn the deck's flipping feel in 10 minutes, no abilities to track
2. **TRIGON** — the flagship; introduces the ability engine and grid tactics
3. **TURNCOAT** — same engine, now personal and confrontational
4. **TWELVE TRIALS** — solo break; see the deck's mathematical structure from the inside
5. **THE ORRERY** — a different decomposition of the same deck; compare orbits to triangles
6. **CROSSROADS** — tight 2P duel, no hidden information
7. **JANUS** — co-op deduction with the fan-asymmetry trick
8. **THE UNPLAYED PAIR** — trick-taking layer on the deduction engine
9. **FALSE FACE** — bluffing against the pair registry
10. **FACE VALUE** — the bluffing engine distilled to a heads-up duel
11. **THE COUNCIL** — full negotiation, all chaos

---

## Coverage at a glance

| Property | Games that use it |
|---|---|
| Flipping as the core action | TURNOVER, CROSSROADS, TWELVE TRIALS, THE ORRERY |
| Flipping as defection/denial | TURNCOAT, THE COUNCIL |
| Pair uniqueness as deduction engine | JANUS, THE UNPLAYED PAIR, FALSE FACE, CROSSROADS, FACE VALUE |
| Algebraic structure (Steiner triples, permutation orbits, Eulerian circuits) | TWELVE TRIALS, THE ORRERY |
| Symbol abilities / grid engine | TRIGON, TURNCOAT |
| Open / perfect information | CROSSROADS, TWELVE TRIALS, THE ORRERY |
| Hidden information | JANUS, FALSE FACE, THE UNPLAYED PAIR, FACE VALUE |
| Social / negotiation | THE COUNCIL, FALSE FACE |
| Solo or co-op | TWELVE TRIALS, THE ORRERY, JANUS |
