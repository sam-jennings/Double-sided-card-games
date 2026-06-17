# CROSSROADS — Task List

*Current status: Rung 1 (table-tested, iterating). Last playtest: 01 (9-sym no-flip, 2P). Verdict: iterate.*

*Requires a second player for all table tests.*

---

## Active tasks (in priority order)

### 1. Design and solo-test a table layout that works
- **Type:** Solo prototyping (no opponent needed)
- **Tied to:** Playtest 01 — the organic layout convention (card touches source city, shows destination face) emerged but felt ugly and unpleasant to play on. The game needs a layout that is compact, scannable, and survives flips before the flip economy can be properly tested with a partner.
- **The problem:** 8 cities + up to ~10 built roads + direction encoding + lit/dim city state must all be readable at a glance without sprawling across the table or becoming a mess of overlapping cards.
- **Candidates to prototype:**

  | Layout | Core idea | Direction encoding |
  |---|---|---|
  | **Dual-rail** | Each city has an inbound zone (roads arriving) and outbound zone (roads departing). A road lives in the inbound zone of its destination. | Position: filed under destination city |
  | **Harbour columns** | 8 cities in a row; each has a column below it. Built roads go into the column of their destination city. | Position + visible face = destination |
  | **Compact ring + fan** | Larger ring with real gaps; roads fan between their two cities, leaning toward destination. | Physical angle/lean |
  | **Adjacency grid** | Conceptual 8×8 matrix; roads slot into row=source, col=destination. | Grid position |
  | **Graph drawing** | Freeform; cities drift apart as roads bridge the gaps between them. | Physical bridging + card orientation |

- **Solo test method:** deal yourself 28 roads, build ~10 in varied patterns (including some non-adjacent connections), then assess:
  - [ ] Can I scan the network state in under 5 seconds?
  - [ ] Can I trace a route from city A to city B without picking anything up?
  - [ ] Does flipping a road (reversing direction) feel clean in this layout?
  - [ ] Does it still look reasonable at 10–12 built roads?
  - [ ] Does the lit/dim city state read alongside the roads?
  - [ ] Does it fit comfortably on a normal table?
- **Recommendation:** try **Dual-rail** and **Harbour columns** first (most structured, encode direction by position).
- [ ] Prototype at least two candidates solo.
- [ ] Pick a winner (or a hybrid).
- [ ] Write up the chosen convention clearly enough to teach a partner in under 30 seconds.
- [ ] Update the rulebook with the new layout.

### 2. Table-test v1.1 with flips enabled (Signal Fires)
- **Type:** 2P table session (needs a partner)
- **Tied to:** Playtest 01 conclusion — core mechanic works without flips; the flip economy is the untested layer that addresses the original first-table questions.
- **Blocked by:** Task 1 — the layout must feel good before this test is meaningful.
- **Prep:**
  - [ ] Re-read the Signal Fires rule: flip any built road + dim one lit city; ko stays; 8 flips shared; all cities dark = facings final.
  - [ ] Prepare the deck: 8 city cards in ring/row (symbol-9 face down), 28 roads dealt 14/14.
  - [ ] Brief the second player on the new layout convention from task 1.
- **During play:**
  - [ ] Answer: does eight flips feel scarce — does spending one *ache*?
  - [ ] Answer: does dimming (rotating a city card) read at a glance?
  - [ ] Answer: does the flip economy break or enhance the contract-banking behaviour from playtest 01?
  - [ ] Watch for: last-turn destruction frustration (contracts collapsing at the whistle).
  - [ ] Watch for: flip hoarding (do players save all 8 for the endgame and never flip mid-game?).
  - [ ] Watch for: whether the pie rule (higher pip total chooses who goes first) feels meaningful or arbitrary.
  - [ ] Watch for: does the new layout survive flips cleanly in real play?
- **After:**
  - [ ] Write playtest report 02.
  - [ ] Verdict: iterate / park / cut the flip economy.

### 3. Revisit the end-of-game trigger
- **Type:** Design work (desk) + table confirmation
- **Tied to:** Playtest 01 bug #2 — double-pass feels asymmetric when one player is ready to stop and the other isn't.
- [ ] After playing with flips, assess: does the Signal Fires pool *itself* create a natural end (all cities dim → network frozen → passing is obvious)?
- [ ] If the pool resolves the issue, document why and close.
- [ ] If not, design and test alternatives:
  - Option A: "Last roads" — once both players have ≤N cards in hand, each gets one final build, then score.
  - Option B: "Signal" — a player may declare done; opponent gets exactly 2 more turns; then score.
  - Option C: other (to be designed if A/B fail).
- [ ] Whatever solution emerges, test it in the same or next 2P session.

### 4. Reinforce equal-deal procedure + cut 7-symbol
- **Type:** Desk work (tiny edit)
- **Tied to:** Playtest 01 bug #3 — deal error in 7-symbol game caused unequal hands.
- [ ] Add a sentence to Setup confirming both players must hold exactly 14 roads. (The current text says "deal 14 each" but could be more emphatic for the 7/8-sym variant case.)
- [ ] Note in the rulebook that 7-symbol CROSSROADS is cut — the game plays at 8 or 9 symbols only.

### 5. Assess first-turn paralysis after flip test
- **Type:** Observation (during task 2)
- **Tied to:** Playtest 01 bug #1 — opening move felt arbitrary.
- [ ] After playing with flips, note whether the flip economy gives the opening more structure (e.g. early builds are now "safe" because flips can answer them).
- [ ] If paralysis persists, consider structural openers:
  - Mandatory first build touching the highest-pip city?
  - A "draft" opening (alternate placing 2 roads each before the full game begins)?
  - Do nothing — let experience resolve it?
  - [ ] Record finding; design a fix only if the problem persists across multiple sessions.

---

## Parked / blocked

- **Caravans variant balance:** The design analysis notes that the direction-blind Caravans variant probably doesn't need the flip pool at all. Not worth testing until the base game's flip economy is settled.
- **Toll Roads scoring:** Interesting but a layer on top of a game whose base isn't finalised. Park until v1.1 is confirmed fun.

---

## Completed

- [x] First table test (playtest 01) — no-flip version, 7-sym + 9-sym. Core connection mechanic confirmed at 9 symbols. Layout convention emerged. Asymmetric end-condition and first-turn paralysis flagged. Verdict: iterate.
- [x] Simulation work (design analysis) — ko insufficiency proven, Signal Fires pool designed, pie rule adopted, all v1.0 open questions closed analytically.
