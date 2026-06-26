# Collection Overview

*9 symbols · 36 cards · one deck · three in the collection, ten more in the pipeline*

The master deck is 36 double-faced cards: every pair of symbols from a set of nine appears exactly once. Any game that runs on fewer than 9 symbols uses a stated subset — no separate deck needed.

A printable prototype deck (Set D Glyphs skin, duplex A4, cut guides) lives in [Print and Play/FLIP_DECK_print_and_play.pdf](Print%20and%20Play/FLIP_DECK_print_and_play.pdf).

---

## Quick Selector

### By player count

| Game | 1 | 2 | 3 | 4 | 5 | 6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| TWELVE TRIALS | ✓ | ✓ | ✓ | | | |
| THE ORRERY | ✓ | ✓ | ✓ | | | |
| CAIRN | ✓ | | | | | |
| OUROBOROS | ✓ | | | | | |
| JANUS | | ✓ | ✓ | ✓ | | |
| TRIGON | | ✓ | ✓ | ✓ | | |
| TURNCOAT | | ✓ | ✓ | ✓ | | |
| CROSSROADS | | ✓ | | | | |
| FACE VALUE | | ✓ | | | | |
| GLEAN | | | ✓ | ✓ | | ✓ |
| BLIGHT | | | ✓ | ✓ | | ✓ |
| FALSE FACE | | | ✓ | ✓ | ✓ | ✓ |
| THE COUNCIL | | | ✓ | ✓ | ✓ | ✓ |
| TURNOVER | | | ✓ | ✓ | ✓ | ✓ |

### By play time

| Time       | Game          | Players      | Genre                       |
| ---------- | ------------- | ------------ | --------------------------- |
| ~10 min    | TURNOVER      | 3–6          | Party shedding              |
| ~10 min    | CAIRN         | 1            | Solo chain patience         |
| ~15 min    | TWELVE TRIALS | 1–2 (+co-op) | Solo/co-op puzzle           |
| ~15–25 min | THE ORRERY    | 1–3          | Solo/co-op sorting puzzle   |
| ~15–25 min | TRIGON        | 2–4          | Tactical grid               |
| ~15–25 min | TURNCOAT      | 2–4          | Allegiance grid             |
| ~20 min    | JANUS         | 2–4          | Co-op communication         |
| ~15–20 min | FACE VALUE    | 2            | Bluffing duel               |
| ~20 min    | FALSE FACE    | 3–6          | Bluffing                    |
| ~20 min    | CROSSROADS    | 2            | Abstract route duel         |
| ~20 min    | GLEAN         | 3–4–6        | Trick-taking (accumulation) |
| ~25 min    | BLIGHT        | 3–4–6        | Trick-taking (avoidance)    |
| ~25 min    | THE COUNCIL   | 3–6          | Negotiation                 |

### By complexity

| Weight | Game | Notes |
|---|---|---|
| **Light** | TURNOVER | Match and flip; ages 8+ |
| **Light–Medium** | CAIRN | Solo patience; chain by a shared sign, don't box yourself in |
| **Light** | THE COUNCIL | No arithmetic, lots of talking |
| **Light–Medium** | FALSE FACE | Bluffing with a shrinking lie-space |
| **Light–Medium** | FACE VALUE | Heads-up betting bluff; the shown face is the claim |
| **Medium** | TRIGON | Grid tactics, 9 symbol abilities |
| **Medium** | TURNCOAT | Same engine as TRIGON, adds allegiance |
| **Medium** | JANUS | Co-op deduction; Hanabi-like hint rules |
| **Medium** | TWELVE TRIALS | Open puzzle; all info visible, no randomness after setup |
| **Medium** | THE ORRERY | Open sorting puzzle; sky debt gives a per-deal lower bound |
| **Medium** | GLEAN | Trick-taking; each capture feeds two sign-majorities |
| **Medium** | BLIGHT | Avoidance trick-taking; the hidden face is the poison |
| **Medium** | CROSSROADS | Perfect-information abstract; route + denial |

### By genre / mood

| Mood | Game |
|---|---|
| **Solo / quiet** | TWELVE TRIALS, THE ORRERY, CAIRN |
| **Co-op, no talking** | JANUS |
| **Head-to-head abstract** | CROSSROADS |
| **Tactical engine** | TRIGON, TURNCOAT |
| **Trick-taking** | GLEAN (accumulation), BLIGHT (avoidance) |
| **Negotiation / betrayal** | THE COUNCIL |
| **Bluffing** | FALSE FACE, FACE VALUE |
| **Head-to-head bluffing** | FACE VALUE |
| **Party / fast** | TURNOVER |

---

## Development Status

### The Collection (table-tested and promoted)

These games have been physically played at the table, received an "iterate" verdict, and earned their place in the collection. They are the games that would ship.

**TWELVE TRIALS** [Twelve Trials/](Twelve%20Trials/) · 1–2 (+3P co-op) · ~15 min · Stage 3  
Open-information puzzle. The 36-card deck hides 840 different "almanacs" — ways of sorting all cards into 12 perfect symbol-trios. Find the best one; your score is how few flips it costs to make the deal match it. Exact solver average: 5.3 flips; unoptimised average: 9 flips. Tiers set accordingly.

*First table test (June 2026):* Solo and open-table 2P co-op. The puzzle is engaging and the almanac's season structure surfaced as a genuine discovery moment. Two handling bugs: (1) sideways-orientation flip-tracking doesn't survive constant card regrouping — cards move too much between staging groups for orientation to stay reliable; (2) the game sprawls across the table. The player stopped counting flips mid-session to focus on completion difficulty. Verdict: **iterate** — needs an alternative flip-tracking method and a workspace convention. See [TWELVE_TRIALS_playtest_01.md](Twelve%20Trials/TWELVE_TRIALS_playtest_01.md).

*Outstanding questions: does a thoughtful solve land near 7 flips (untested — flip-counting was abandoned)? What tracking method replaces sideways orientation? Does a "completion mode" (no scoring, just solve) have value as a learning variant?*

**CROSSROADS** [Crossroads/](Crossroads/) · 2 · ~20 min · Abstract · **v1.1, sim-tested** · Stage 3  
Route duel. Sim proved ko alone never ends the game (100% of unlimited-flip duels looped forever), so v1.1 adds **Signal Fires**: eight shared flips, paid by dimming (rotating) the eight city cards — every simulated game now ends in ~20 turns. Measured seat advantage favoured the *second* player, so the start became a pie rule: higher pip total chooses who goes first.

*First table test (June 2026):* Tested a simplified no-flip version at 7 and 9 symbols. The 7-symbol deck was too sparse; 9 symbols worked well. The core connection mechanic produces interesting decisions. Two bugs found: first-turn paralysis (no obvious anchor for the opening move) and an asymmetric end-of-game problem (double-pass rule feels unfair when players are ready to stop at different times). An organic physical layout convention emerged (card touches source city, shows destination face). Verdict: **iterate** — the flip economy (v1.1's Signal Fires) is untested and is the priority next step. See [CROSSROADS_playtest_01.md](Crossroads/CROSSROADS_playtest_01.md).

*Second table test (June 2026, off-spec):* an **off-spec** session (drifted to 3P / 9 cards; Signal Fires barely used) that again failed to test the flip economy, but surfaced a **CRITICAL pass-to-win line** — passing every turn (building nothing, keeping every card as a contract) won overwhelmingly because the network connected nearly every pair anyway, so the "keeping a road deletes it" tension didn't bite. Also re-confirmed the **end-trigger unfairness** (now twice-flagged) and **14-card hands overwhelming first-timers** (9 felt far better). Verdict: **iterate, on notice** — the pass-to-win finding must be reproduced (or refuted) under **proper 2P + Signal Fires** play, where flips can deny a passer's routes; the leading candidate fix is promoting the **Toll Roads** scoring (rewards roads you built) into the base game. See [CROSSROADS_playtest_02.md](Crossroads/CROSSROADS_playtest_02.md).

*Outstanding questions (priority): under 2P with Signal Fires actually used, does pass-to-win survive? Does an eighth-dim end trigger fix the end-of-game unfairness? Do the recorded flip questions (does eight flips ache? does dimming read at a glance?) finally get tested? Does a reduced-hand teaching ramp cure the 14-card cold start?*

**THE ORRERY** [The Orrery/](The%20Orrery/) · 1–3 · ~15–25 min · Solo/co-op sorting puzzle · Stage 3  
Open-information orbit puzzle. Sort the full 36-card deck into four orbits of 9 cards, each showing all 9 symbols once on its visible faces and all 9 once on its hidden faces. Move cards freely; every flip costs 1 point. The sky debt (over-shown symbols vs. target count of 4) gives an exact lower bound per deal. Sibling to TWELVE TRIALS via a different decomposition (4 permutation orbits vs. 12 triangles).

*First table test (June 2026):* Tested the 7-symbol Apprentice version solo with a pre-balanced deal (sky debt 0, isolating the grouping puzzle). The standard puzzle was genuinely challenging and satisfying. Key finding: the word "orbit" misled the player into expecting a single continuous cycle (Clockmaker), when a valid standard solution can contain split cycles. The player solved standard Orrery but could not solve Clockmaker at the table. Open information handled perfectly. Verdict: **iterate** — fix terminology, keep Clockmaker as prestige variant only, then test with random deals. See [THE_ORRERY_playtest_01.md](The%20Orrery/THE_ORRERY_playtest_01.md).

*Outstanding questions: does the standard game remain satisfying across multiple deals? Does the 9-symbol version feel manageable? Does the full game (with sky debt) feel distinct from TWELVE TRIALS? Do split cycles feel valid once the rules explicitly allow them?*

---

### The Pipeline

Games below are works in progress at various stages. No obligation to advance them in any order. See [product-vision.md](.kiro/steering/product-vision.md) for stage definitions.

#### Stage 2 — Validated (sim/solver complete, untested at the table)

> *June 2026: TRIGON and BLIGHT have since had their first table tests (now Stage 3, verdict iterate) — see their annotated entries below. They remain listed here pending a clear promotion decision.*

**OUROBOROS** [Ouroboros/](Ouroboros/) · 1 · ~10–15 min · Solo serpent-building puzzle · **v1.1, revived** · Stage 2  
Lay the all-pairs deck into one serpent until it bites its tail; forced mismatches are *scars* (your score), and exactly one scar is provably impossible. **Cut in June 2026, revived June 2026** after the cut reasons were re-examined: the buried open-symbol bug is fixed in v1.1 (cards are laid showing their *onward* symbol, so both open ends stay face-up — orientation-as-state, never lift the serpent), and a Monte-Carlo planning bot put the skill ceiling at **~1.74× (n=9) / ~1.84× (n=7)** over random — above the ~1.5× healthy bar, retiring the "thin skill gap / luck-dominant" verdict that rested on one-ply floor numbers. See [OUROBOROS_design_analysis.md](Ouroboros/OUROBOROS_design_analysis.md) §6.  
*First table questions (v1.1): does the open-symbol-shown layout genuinely remove all lifting? Is hand-stewardship learnable at the table (does a player climb out of the greedy near-random band within a session)? Does shuffle variance now read as tension, not luck-blame?*

**CAIRN** [Cairn/](Cairn/) · 1 · ~10 min · Solo chain patience · **v0.1, sim-validated** · Stage 2
Compact solitaire built for a tray, not a tabletop — the contained solo game the collection lacked (TWELVE TRIALS and THE ORRERY both sprawl). All state lives in **three short cairns plus a held hand**: each card is a link between two signs, and you extend a cairn by playing a card carrying its top sign, exposing the partner sign. Lay all 21 cards (7-sign sub-deck) without boxing yourself in. Sim-validated in three stages — structure, a hand-beats-reserve comparison, and a realistic-information planning check (depth-2 expectimax and PIMC both clear ~93–98% at 7 signs, recovering ~70–90% of the way to the clairvoyant ceiling), which answers the OUROBOROS luck worry: the skill is genuine and reachable. See [NEW_GAME_CONCEPTS.md](NEW_GAME_CONCEPTS.md) §13 and [cairn_sim.py](Cairn/cairn_sim.py).

*First table questions: do the chaining choices feel meaningful or like arithmetic? Does getting blocked read as a foreseeable mistake or an arbitrary shuffle? Is a hand of four right? Is the free look (the stock's visible top) actually used? Does the difficulty ladder — First Trail → standard → Pathfinder → the 9-sign Long Trail — land?*

**TRIGON** [Trigon/](Trigon/) · 2–4 players · ~15–25 min · **~23k simulated games · Stage 3 (first table test June 2026)**  
Grid capture. Place cards, trigger symbol abilities, chain reactions. Three matching symbols in a row/column/diagonal = capture. Star is wild. The collection's flagship candidate. Extensively simulation-tuned; now has its first table test.

> *The `Syzygy/` folder is retained as an archive of the pre-rename design record.*

*First table test (June 2026, 3P):* the engine never got a fair run — the session was bottlenecked by **handling/onboarding**, not mechanics. Two HIGH bugs: (1) the **grid is not physically defined**, so play slipped into unfixed-grid (Instinkt) habits, which breaks the position-based ability requirements; (2) **reference overhead** — every player checked both faces' requirements and abilities every turn off a shared laptop, making turns very slow. Comprehension hurdles around requirement-vs-ability and chaining order/limits (the rulebook answers both, but they're hard to find mid-turn). Verdict: **iterate** — fix the grid (proposed: first card = centre cell, no new components) and the reference problem before re-testing feel/balance. Not yet promotable. See [TRIGON_playtest_01.md](Trigon/TRIGON_playtest_01.md).

*Outstanding questions: does centre-first grid definition kill the unfixed-grid drift? With references sorted, does capture cadence and the "active player captures everything" swing read as drama? Does a second game lift play out of aimless placement, or is the real skill hidden behind a near-random obvious line? (Re-test at 2P.)*

**TURNCOAT** [Turncoat/](Turncoat/) · 2–4 players · ~15–25 min · **~22k simulated games**  
Allegiance grid. Every card serves two signs; the visible face declares loyalty today. Flip an opponent's agent to defect them. Bury your own before rivals turn them. Built on the same engine as TRIGON but feels entirely different. Extensively simulation-tuned but never tested at the table.

*First table questions: is one activation per turn exciting or exhausting over 18 turns? Does the bury-your-own loop teach itself? Does Mask feel like a fun strong pick or a must-pick? Allied Houses versus free-for-all at four?*

**TURNOVER** [Turnover/](Turnover/) · 3–6 · ~10 min · Party · **v1.1, sim-tuned** (~60k games)  
Match-and-turn shedding race. Sim closed all three v1.0 questions: chain 2 and refusal 2 confirmed (zero stalls, flat seats, 1.5–1.8× skill edge, ~5-min races); Hot Well cut (it made games *longer*, not shorter) and replaced by the Wildfire variant (chain 3 — genuinely faster and sharper); Slow Match errata'd to refusal-cost 1, without which the chainless game frequently never ends.

*First table questions: announce-rule policing fun? Does chaining feel as bridge-burning as the maths says?*

**GLEAN** [Glean/](Glean/) · 3–4–6 · ~20 min · Trick-taking (accumulation) · **sim-validated**  
Gathering trick-taker. Follow by either face; the hidden face wins the trick. Each captured card counts toward **two** sign-majorities at once — win the most of a sign to claim its pip value (Crown 9 highest). The bright sibling of BLIGHT: same engine, opposite goal. Skill gap 1.74×/1.67×/1.49× (3/4/6P); deal-sensitive, so played as a match with rotating lead.

*First table questions: is counting nine simultaneous majorities frictionless or fiddly? Does the deal-sensitivity feel fair across a match? Do captures feel meaningful turn-to-turn or too deferred?*

**BLIGHT** [Blight/](Blight/) · 3–4–6 · ~25 min · Trick-taking (avoidance) · **sim-validated · Stage 3 (first table test June 2026)**  
Avoidance trick-taker. Same engine, inverted: a captured card's penalty is its **hidden** pip — the back of the card is the poison. Lowest total wins; the rot pile is stored penalty-face-up so nothing is remembered. Shoot the rot (take every trick) to score 0. The dark sibling of GLEAN. Steepest trick-taking skill gap (2.02×/1.91×/1.41×); seat-fair.

*First table test (June 2026, 3P, one round):* the session's **standout** — Lauren read the rules unaided and called them clear, and said it was the game she'd expected from this deck. Played clean, no rules disputes. Defining moment: Arran held ~6 Crowns, sloughed them away (dumping hidden 9s into others' piles) and **won** — the slough-as-weapon line working exactly as designed, though it surprised the table (a good depth signal + a teaching note). Two open issues: large-hand handling (12 cards, both faces, no sort, realign every trick — cross-game F1) and a **fun split** (Lauren disliked a "bad hand with no recovery"; Sam/Arran noted two-faced cards give more recovery than normal trick-takers). Verdict: **iterate** — strong promotion candidate. See [BLIGHT_playtest_01.md](Blight/BLIGHT_playtest_01.md).

*Outstanding questions: at 4P (9) / 6P (6) does the hand-handling load drop to comfortable? Over a full match (one round per player), does the hand-luck complaint wash out? Does the shoot-the-rot threat ever light up the table?*

#### Stage 1 — Draft (rulebook exists, untested)

> *June 2026: JANUS has since had a first table test (now Stage 3, verdict iterate) — but its core concealment was abandoned in play, so the game as designed remains unproven. See its annotated entry below.*

**JANUS** [Janus/](Janus/) · 2–4 · ~20 min · Co-op · **Stage 3 (first table test June 2026 — but core concealment untested)**  
Each player sees one face of their own cards; the table sees the other. Co-operate to raise symbol-triangle gates using half-seen hands. Hint grammar à la Hanabi, but the deduction is exact (every pair is unique, so a single hint can fully identify a card).  

*First table test (June 2026, 3P Apprentice):* the table **abandoned the fan-asymmetry concealment** and played open-information, so JANUS-as-designed was **not actually tested**. The session's value was a **blocking handling discovery**: v1.1's "face-down draw stack" is **physically impossible** on a backless deck — the top card's face always shows, exactly the leak v1.1 claimed to fix. Players hacked it with a spare Crown as a deck cover. Terminology drift worth noting: the group reached for "locks / keys / clues" over gates/keystones/omens. Verdict: **iterate** — JANUS regresses to "needs a sound concealment model" (opaque deck cover, draw-bag, or a no-draw deal) before its real hypotheses can be tested. Not promotable. See [JANUS_playtest_01.md](Janus/JANUS_playtest_01.md) and DECK_PLAYTEST_FINDINGS F7–F8.  
*Outstanding questions: with a real opaque-draw method, does the concealed game run without face leaks? Can the table sustain the no-self-inspection rule for a whole game? Under genuine concealment, does locking a gate produce the deduction payoff?*

**FALSE FACE** [False Face/](False%20Face/) · 3–6 · ~20 min · Bluffing  
Play a card and claim its hidden face aloud — truthfully or not. Challenge to force a reveal: liar takes the pot, honest player challenged means the challenger takes it. Because every pair exists once, the lie-space provably shrinks each turn.  
*Test focus: ledger pacing; whether first-game players can price a lie.*

**FACE VALUE** [Face Value/](Face%20Value/) · 2 · ~15–20 min · Bluffing duel  
Heads-up betting bluff. Both players commit a duel card — the face you *show* is your only claim about the strength you *hide*. Raise stakes from hand, call to showdown (higher hidden pip; pair-uniqueness makes ties impossible), or fold to keep your card unrevealed. Cold Read: name the exact hidden symbol for double-or-nothing — a gamble early, arithmetic late. Pacing sim-checked (~12 duels, skilled bot beats random 94%).  
*Test focus: fold frequency; cold-read timing; whether acting last reads as the advantage it is.*

**THE COUNCIL** [The Council/](The%20Council/) · 3–6 · ~25 min · Negotiation  
Three issues tabled each round; everyone secretly commits one card showing their chosen issue. Then, in seat order, anyone may flip their card to defect — to its one specific alternative. Lone backers take an issue's entire pot. Stacks grow for unresolved issues.  
*Test focus: kingmaking at 5–6P; pot arithmetic staying frictionless.*

#### ⏸ Parked

**THE UNPLAYED PAIR** [The Unplayed Pair/](The%20Unplayed%20Pair/) · 3–5 · ~25 min · Trick-taking  
One card is removed unseen before dealing; classic trick structure, follow by either face, with a final bet naming the missing card. **Parked (June 2026):** simulation showed the trick-taking and missing-card-deduction layers fight each other — certainty arrives only on the final trick, so the call mechanic is structurally dead (see [UNPLAYED_PAIR_design_analysis.md](The%20Unplayed%20Pair/UNPLAYED_PAIR_design_analysis.md)). The trick-taking slot is now filled by **GLEAN** and **BLIGHT**; the "guess the missing card" idea is preserved for a future non-trick-taking game (Parking Lot in [NEW_GAME_CONCEPTS.md](NEW_GAME_CONCEPTS.md)). Folder retained as a design record.

---

### ❌ Cut

*No games are currently cut. OUROBOROS — the collection's only cut game — was **revived to the pipeline (Stage 2)** in June 2026 after its cut reasons were re-examined; see the Stage 2 entry above and [OUROBOROS_design_analysis.md](Ouroboros/OUROBOROS_design_analysis.md) §6.*

The OUROBOROS episode is retained here as the worked example of confronting-then-revisiting a cut. The lessons it taught remain binding, in their corrected form:

1. Solo games should avoid *involuntary* hidden-face bookkeeping — but **deliberate, verifiable memory or deduction is welcome when it is the point** (OUROBOROS's buried open symbol was forced overhead, now fixed by showing the open symbol face-up).
2. Any constantly-needed, low-payoff state must be *visible*, never buried on a down-face (orientation-as-state resolves it).
3. A thin skill gap warns of a dull game — but **read the gap honestly**: distinguish the *obvious* strategy's gap from the *ceiling*, and remember a one-ply bot is a floor (OUROBOROS's "thin gap" was a one-ply artefact; a planner clears the healthy bar).

---

## Recommended play order for learning the collection

1. **TURNOVER** — learn the deck's flipping feel in 10 minutes, no abilities to track
2. **TRIGON** — the flagship; introduces the ability engine and grid tactics
3. **TURNCOAT** — same engine, now personal and confrontational
4. **TWELVE TRIALS** — solo break; see the deck's mathematical structure from the inside
5. **THE ORRERY** — a different decomposition of the same deck; compare orbits to triangles
6. **CROSSROADS** — tight 2P duel, no hidden information
7. **JANUS** — co-op deduction with the fan-asymmetry trick
8. **GLEAN** — trick-taking on the deck: capture signs, win majorities
9. **BLIGHT** — the same trick engine inverted: dodge the hidden rot
10. **FALSE FACE** — bluffing against the pair registry
11. **FACE VALUE** — the bluffing engine distilled to a heads-up duel
12. **THE COUNCIL** — full negotiation, all chaos

---

## Coverage at a glance

| Property | Games that use it |
|---|---|
| Flipping as the core action | TURNOVER, CROSSROADS, TWELVE TRIALS, THE ORRERY |
| Edge-adjacency / chaining cards by a shared sign | CAIRN |
| Flipping as defection/denial | TURNCOAT, THE COUNCIL |
| Pair uniqueness as deduction engine | JANUS, FALSE FACE, CROSSROADS, FACE VALUE |
| Two-faces / hidden-face as score driver | GLEAN (two majorities per card), BLIGHT (hidden face is the penalty) |
| Algebraic structure (Steiner triples, permutation orbits, Eulerian circuits) | TWELVE TRIALS, THE ORRERY |
| Symbol abilities / grid engine | TRIGON, TURNCOAT |
| Trick-taking (follow by either face) | GLEAN, BLIGHT |
| Open / perfect information | CROSSROADS, TWELVE TRIALS, THE ORRERY |
| Hidden information | JANUS, FALSE FACE, FACE VALUE |
| Social / negotiation | THE COUNCIL, FALSE FACE |
| Solo or co-op | TWELVE TRIALS, THE ORRERY, JANUS, CAIRN |


---

## Component inventory (verified — single source of truth)

*Verified June 2026 by reading the Components section of every rulebook. This table is the canonical answer to "what does game X need on the table?" — cite it (or re-read the rulebooks) rather than asserting component facts from memory.*

| Game | Components beyond the 36-card deck |
|---|---|
| **JANUS** | **6 omen tokens** — *"any 6 small objects"* (coins/pebbles); a shared hint-economy counter pool |
| **THE COUNCIL** | **1 Speaker token** — *"any object"*; rotating first-player/turn-order marker |
| **THE ORRERY** | none required — paper *optional* for scoring ("helps, but is not necessary") |
| TURNOVER · TWELVE TRIALS · TURNCOAT · TRIGON · THE UNPLAYED PAIR · BLIGHT · GLEAN · FACE VALUE · OUROBOROS · FALSE FACE · CROSSROADS · CAIRN | **none — deck only** |

### The component policy this reveals

- **State is encoded in the cards by default** — boards built from the deck (CROSSROADS), **orientation** (sideways = flipped, "orientation as state"), **position** (your pile/area), and printed **pips**. This is the first preference and what most games do.
- A **small, generic, reusable shared counter kit is sanctioned**, not banned. JANUS (6 omens) and THE COUNCIL (1 speaker token) already establish a house kit of "any small objects." A new game **may** draw on the *same* generic counters when they genuinely improve play — if a counter already earns its place for JANUS and helps elsewhere, that is a point in its favour, not a violation.
- **The graduated guideline for new designs:**
  1. *Prefer* encoding state in the cards (positional ownership, orientation, pips) when it's clean.
  2. *Acceptable freely:* the existing generic shared-counter kit (identical small tokens, player-supplied).
  3. *Justify at collection level:* introducing a **new class** of shared component (e.g., a set of small **colour-coded cubes** for per-player ownership). Permissible if it is small, generic, off-the-shelf, and **reused by more than one game** — not bespoke to one. The bar is "would several games want this kit?", not "never."
  4. *Avoid:* bespoke/printed/game-specific pieces, large components, or anything only one game could ever use.
- So per-player ownership markers are **not forbidden** — they need a shared, reusable, generic kit to justify them, ideally adopted by multiple games rather than introduced for one.
