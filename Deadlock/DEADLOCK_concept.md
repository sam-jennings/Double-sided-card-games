---
record_type: game
game: "DEADLOCK"
state: Proven
players: [2]
player_count: "2"
duration: "~20 min"
genre: "Territory duel"
complexity: Medium
min_players: 2
max_players: 2
physically_playtested: true
public_document: "Deadlock/DEADLOCK_rulebook.md"
next_step: "Table v1.0: play the default two-game match (seats swapped) and check whether the match length and the Crown tiebreak feel right."
catalog_order: 25
---
# DEADLOCK (formerly VIGIL) — the game that waits on the windowsill

*2 players · a match of two games, ~20 minutes (one game ~10) · perfect-information territory duel · full 36 · Proven · physically played*

> **Renamed and v1.0 (23 November 2026).** Renamed from VIGIL, because a "vigil" (a long watch) described the over-days format the table didn't take to; a **deadlock** is the 3–3 line that scores for nobody, the game's sharpest move. [DEADLOCK_rulebook.md](DEADLOCK_rulebook.md) v1.0 makes one sitting the main format, a two-game match with seats swapped the default, and South's point or South's ties the single-game options. The shelf format is now an untested variant.

> **First playtest (23 November 2026).** Played in one sitting with Noah: very positive from both players, with the right balance of strategy and simplicity. It took about 10 minutes and felt like a game to play straight through, so it does **not** meet the original over-days brief below, but it stays in the collection as a proven short duel. See [DEADLOCK_playtest_01.md](DEADLOCK_playtest_01.md).

> **Status (November 2026).** A draft rulebook now exists: [DEADLOCK_rulebook.md](DEADLOCK_rulebook.md) v0.1, simulated in [DEADLOCK_design_analysis.md](DEADLOCK_design_analysis.md) ([deadlock_sim.py](deadlock_sim.py)). No stalls, a strong skill gap (careful play beats random 100%, 2.5× the points) and flipping is load-bearing, but the first mover wins about 70% of careful games and no single-field bonus is even at every skill level. It can also be played in one sitting. This page remains the game record and the concept's reasoning; the draft's *Decisions to review* list holds every open choice.

> **Status & scope.** Wildcard batch, first flight (July 2026). Written to a deliberately different brief: *maximum originality, rubric waived, no simulation required.* Playable as written, but no rulebook, no sim, no rubric self-score, and it should not jump the [focus-priority.md](../.kiro/steering/focus-priority.md) queue on novelty alone. Carries the two house disciplines: a full physical-handling audit and a fastest-falsification test. Portfolio index: [NEW_GAME_CONCEPTS.md](../NEW_GAME_CONCEPTS.md) §22.

**The trick that makes it exist.** A game designed for a shelf, not a session: you move when you pass it; your opponent moves when they pass; nobody remembers whose turn it is or what the state was, because **the deck is the save file**. The design constraint everything serves is *total legibility after three days of not looking* — no hidden information, no memory, no notation, no clock. And the tamper-evidence is structural: a deck with no facedown state cannot be disturbed without changing what it publicly shows. This is less one game than a **format** the collection doesn't know it has yet.

**Setup.** Shuffle and deal a 6×6 field (the exact-grid property), every card pointing **East** (neutral). Players own **North** and **South**. Whose move? Count claimed cards: even total = North. The turn marker computes itself from the board — nothing to remember, nothing to knock over.

**Move.** Choose any card still pointing East. **Optionally flip it**, then turn it to point at your seat. Claimed cards are locked forever. That is the entire grammar: 36 moves and the game ends — a fortnight of kitchen diplomacy at one move per passing.

**Scoring (over a coffee, when the last card turns).** Twelve lines (6 rows, 6 columns). A line is won by whoever claimed **4+** of its 6 cards (3–3: nobody). A won line scores **the largest count of any single shown sign in it** (2–6) — a value that was set one irreversible flip at a time, by both of you. Most points wins; tie goes to whoever's claimed cards show more Crowns.

**The texture.** Every claim braids three decisions: *territory* (which line-majorities to chase), *value* (flip to concentrate a sign in your line, or to dilute one in theirs), and *denial* (claiming into an enemy line turns 4–2 into 3–3 and deletes it — poisoning is always available, so majorities must be assembled quietly). Each sign existing on exactly 8 cards puts a hard, visible ceiling on concentration.

**Why it needs this deck.** Exactly 36 for the 6×6; flips as one-shot value-setting; and the both-faces-identical orientation marker is what makes *flip-then-claim* trustworthy across days — ownership survives the flip physically, not by agreement.

**Handling audit.** Perfect information, zero memory between moves, self-computing turn parity, ratcheting state (claimed = locked) — every property chosen so that a glance reconstructs everything. The audit *is* the design brief.

**The larger experiment.** If the shelf format works, it is a lens for the whole collection: CROSSROADS and SNARE both have slow-correspondence variants waiting inside them.

**Fastest falsification.** One full field with a housemate: if either player ever has to ask "whose move is it?" or "what happened here?", the legibility constraint failed. If the last ten claims feel forced (all lines already decided), the scoring needs the diagonals added or the majority threshold moved.
