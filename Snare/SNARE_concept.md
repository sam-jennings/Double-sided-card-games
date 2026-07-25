---
record_type: game
game: "SNARE"
state: In development
players: [2]
player_count: "2"
duration: "10–15 min"
genre: "Abstract avoidance"
complexity: Medium
min_players: 2
max_players: 2
min_minutes: 10
max_minutes: 15
physically_playtested: false
public_document: "Snare/SNARE_concept.md"
next_step: "Develop a complete rulebook if this concept is selected."
catalog_order: 21
---
# SNARE — the forbidden three

*2 players · ~10–15 min · perfect-information abstract / avoidance · In development · physically unplayed*

> **Status & scope.** This is a **rung-4 new concept** ([focus-priority.md](../.kiro/steering/focus-priority.md)). It is logged for exploration only. Per the circuit breaker, it is **not** to be developed into a full rulebook until at least one rung-2/3 game (TRIGON, TURNCOAT, FACE VALUE, JANUS…) has had its first table test. Working title; alternatives: SCHISM, QUORUM, THE THIRD ROAD. Avoid TRIAD — too close to TRIGON. Portfolio index: [NEW_GAME_CONCEPTS.md](../NEW_GAME_CONCEPTS.md) §10.

**The deck property it exploits.** The 6-symbol subset is **K₆** rendered as 15 cards (each card the unique edge between two of symbols 1–6). The collection has no other **inevitability** mechanic; everything else is about what you *can* build, this is about what you *cannot avoid* ([deck_mathematical_analysis.md](../Reference/deck_mathematical_analysis.md) II.4).

> **Framing correction (don't headline Ramsey).** It's tempting to sell this on R(3,3) = 6 ("any 2-split forces a mono-triangle"). That's the *weak* statement and it oversells the theorem: real play produces a roughly **even 8/7 split**, and Ramsey holds for *all* splits including the lopsided ones that never occur. Under the balanced splits a game actually generates, the binding facts are stronger and tighter (verified, `_ramsey_balance_check` — enumerated all 12,870 balanced colourings of K₆):
> - minimum mono-triangles = **2** (Goodman), **mean = 4.0**, max = 7;
> - **no** colouring has exactly 0 or exactly 1 — the count jumps straight from impossible-zero to two.
>
> So a balanced split doesn't force *one* triangle, it forces *several* (≈4), and provably never fewer than two. **Ramsey's only real job here is the no-draw guarantee** (the board can't finish triangle-free) — a footnote, not the hook. The hook is **Goodman's floor of 2 plus the 2→7 spread**: at a fixed balanced count, *structure* (which edges, not how many) swings the result from 2 to 7, and that swing is the entire skill space.

**Design consequence — the game needs agency over the split.** A flat even deal is inert: it *already* forces ≈4 triangles with near-certainty, so nobody is choosing anything. The game only exists when players steer the split. Two levers, only the second of which makes full-strength Ramsey load-bearing:

**Core loop (primary form — agency over *which* edges).** Lay the six symbols as a hex of "houses"; the 15 cards are the roads between them. Players alternate **claiming** one unclaimed card by orienting it toward their side of the table (orientation = ownership colour — fully visible, glanceable, no hidden-face memory; the CROSSROADS technique, [physical-handling.md](../.kiro/steering/physical-handling.md) "orientation as state"). The count stays balanced 8/7, but you steer *structure* to push the forced triangles into the opponent's colour. Two win conditions to test:
> - **Sudden-death (Sim):** you lose the instant you own all three roads of a symbol-triangle. Decisive (the no-draw guarantee bites), but the loss can feel like one fatal misstep.
> - **Goodman scoring:** place all 15; each mono-triangle in *your* colour is a debt point; fewer wins. The floor of 2 means there's always blood; the 2→7 spread means structure choices pay off across the whole game. Likely the better game — it rewards play, not a single slip.
>
> **Pie rule** on the opening claim (Sim is a second-player win under perfect play — the seat-asymmetry fix CROSSROADS uses).

**The variant where Ramsey's generality earns its keep — agency over *how many* edges.** A dumping/refusing form: players push unwanted roads onto each other; whoever ends up holding a triangle loses. *Here* the strategy space genuinely visits unbalanced splits — and the point of R(3,3) is precisely that even a lopsided 13/2 hoard can't escape, so refusing-to-take is not a safe out. This is the only framing where "any colouring contains a triangle" is doing visible work rather than sitting in the background. Worth a concept of its own if the claiming form tests well.

**The signature hook — the tightness campaign.** Play a best-of series that *starts* at **5 symbols / 10 cards**, where a triangle-free split provably exists (colour the pentagon vs. the pentagram — each is a triangle-free 5-cycle; verified: the balanced 5/5 split reaches 0 mono-triangles), so a **draw is an achievable skill result**. Then ratchet to **6 symbols**, where avoidance becomes impossible. Players *feel* the threshold instead of being told it: adding one symbol removes the possibility of safety. This 5→6 jump is the most deck-native, most original part of the idea.

**Why it (probably) needs this deck.** "Every pair exactly once" is precisely what lets a card *be* an edge of K₆ — without it you cannot physically lay the complete graph as components, and the forcing theorem has nothing to bite on. Deck-necessity is *moderate* (pencil-and-paper Sim exists), but the physical realisation — roads you can see, a tightness dial you change by adding/removing a symbol's cards — is the part that only this deck delivers.

**Honest evaluation (rubric, [design-principles.md](../.kiro/steering/design-principles.md)).**
1. Exploits all-pairs: **yes** (cards as K₆ edges). 2. Physically works: **yes** — open information, orientation-as-state, nothing buried. 3. Visible/deducible: **yes** — zero hidden-face memory. 4. **Flipping matters: weak.** The literal symbol-swap is *structurally inert* for Ramsey — a card is the edge {A,B} regardless of face; only the 2-colouring (orientation/ownership) affects the maths. Do not contort the game to force symbol-swapping. 5. Pair-uniqueness matters: **yes**. 6. Distinct experience: **partially** — inevitability/avoidance mood is new, but it shares "2P perfect-info abstract" with CROSSROADS; the table must confirm they feel different. 7. Gap-fill: a quick 2P avoidance filler + the only inevitability game. 8. Clean to explain: **yes** ("don't be the one who completes a triangle"). 9. Testable on Set D today: **yes**. 10. Fastest falsification: **two short sessions** — (a) does 5-symbol play create real "I survived" tension and earned draws, (b) does 6-symbol forcing read as dramatic inevitability rather than an arbitrary loss?

**Risks / why it might be cut.** Sim is famously more elegant than *fun* — human players struggle to see triangle threats (K₆ has 20 triangles), so the loss can feel arbitrary rather than earned. The physical board (threats visible as roads) and the 5→6 escalation are the bets that make it approachable. If a first table test shows the threat-reading is opaque and the loss feels random, **cut it cleanly and record the lesson** (a thin/illegible decision space is the OUROBOROS failure mode). It overlaps CROSSROADS on player count and information model; it earns its place only if the *mood* is genuinely distinct.

**Deck-size fit — symmetric goals, and the player-count wall.** Both players should avoid the *same* shape (symmetric goals are fairer and cleaner than the earlier asymmetric triangle-vs-clique sketch, now retired). The forbidden shape sets the threshold = the **diagonal Ramsey number** = symbols needed:

- **6 symbols / 15 cards — the legible home (R(C₃,C₃) = 6).** Both avoid a triangle; 5/10 is the escapable first rung (the balanced 5/5 split reaches 0 mono-triangles, verified). Clean, teachable, 20 triangles scannable by eye. **But it uses only 15 of 36 cards — a light 2P filler, not a flagship.** Subset use is legitimate and intended ([deck-structure.md](../.kiro/steering/deck-structure.md); cf. JANUS@7) but doesn't *showcase* the master deck.
- **9 symbols / 36 cards — the deck-defining version (R(C₅,C₅) = 9).** Both avoid a **pentagon** (5-cycle). All 36 cards are edges, even 18/18 split, threshold 8→9 (K₈ escapable — witness verified: two K₄ vs K₄,₄, no mono C₅ in either colour; upper bound cited). Fully symmetric, uses the whole deck, and you hunt a **loop** rather than a clique. Cost: a 5-cycle is the hardest of these to scan late-game.
- *(C₄ symmetric, R(C₄,C₄)=6, is also 15 cards but a 4-loop is harder to spot than a triangle with no deck-size gain — no reason to prefer it over triangles.)*

> **Binding finding — this is a 2-player mechanic, permanently.** Symmetric forced-avoidance for *r* players needs the multicolour Ramsey number R_r(H) ≤ 9. But these explode: **R(C₄,C₄,C₄) = 11** (3 players → 11 symbols), **R(C₃,C₃,C₃,C₃) ≈ 51–62** (4 players → ~51 symbols). The deck caps at 9 vertices, so **no 3+ player version can guarantee the forcing — ever.** Verified for the tempting 3-player/C₄ case: unlike the 2-player Goodman case (where the even split *restored* forcing), here the balance loophole fails too — a balanced **12/12/12 C₄-free partition of K₉ exists** (constructed explicitly), so perfect play is a three-way survival with **no guaranteed loser**. A 3-player version therefore loses the inevitability hook entirely (becoming a generic avoidance abstract that fails the deck-necessity test) and invites 2-on-1 kingmaking besides. Don't chase a multiplayer SNARE; the inevitability lives only at two colours. R(C₅,C₅)=9 is the largest forbidden-shape game the deck can host.

**Caveats for the cycle (9-symbol) version:** late-game legibility — a loop is easy to *trace*, but a dense colour class hides many 5-cycles by the endgame; easier than cliques, not free. This is the make-or-break handling question if the 9-symbol form is pursued.

> **Open fork (record, don't resolve yet):** the 6-symbol triangle game (most legible, 15-card filler) vs the 9-symbol pentagon game (whole deck, deck-defining, but the hardest to scan). Prototype the 6-symbol triangle version first — it answers the only question that gates everything else: *is forced-shape avoidance fun at all on this deck?* Only if yes does the 9-symbol pentagon legibility problem become worth solving.
