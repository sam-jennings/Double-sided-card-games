# New Game Concepts

*Eight concept sheets expanding the collection beyond TRIGON and TURNCOAT. Each exploits a property of the all-pairs flip deck that the existing games don't touch. Deck-size fit is stated per game; see `DECK_SIZE_DECISION.md` for the overall recommendation.*

Portfolio coverage at a glance:

| # | Game | Genre | Players | Key deck property used |
|---|---|---|---|---|
| 1 | JANUS | Co-op communication | 2–4 | The fanned hand shows opposite faces to opposite sides of the table |
| 2 | FALSE FACE | Bluffing | 3–6 | Every lie about a hidden side is eventually falsifiable (pairs are unique) |
| 3 | OUROBOROS | Solo puzzle | 1 | K₇/K₉ have Eulerian circuits — the whole deck chains into one loop |
| 4 | TWELVE TRIALS | Solo / co-op puzzle | 1–3 | The 36-card deck partitions perfectly into 12 symbol-triangles |
| 5 | THE UNPLAYED PAIR | Trick-taking / deduction | 3–5 | One missing card is fully identifiable by elimination |
| 6 | CROSSROADS | 2P abstract route duel | 2 | Each card is the *only* road between its two symbols |
| 7 | THE COUNCIL | Negotiation / game theory | 3–6 | Every commitment is reversible — but only to one specific alternative |
| 8 | HOT POTATO PAIRS | Party shedding | 3–6 | Both faces constrain legal plays; the back of your card is a liability |
| 9 | THE ORRERY | Solo / co-op sorting puzzle | 1–3 | 36 cards partition into four 9-card orbits, each a permutation of all 9 symbols on both faces |
| 10 | CABAL *(concept stage)* | 2P abstract avoidance | 2 | Goodman: any balanced K₆ split forces ≥2 mono-triangles (mean ~4); 5→6 threshold turns "survivable" into "doomed" |

Existing games already cover: tactical grid engine (TRIGON) and direct-conflict allegiance (TURNCOAT).

---

## 1. JANUS — co-operative signalling

*2–4 players · ~20 min · co-op*

**The trick that makes it exist:** hold a fan of these cards normally and you see one face of each card while everyone else sees the *other* face. There is no card back — the information split is symmetric, real, and free. No other deck does this. (Inspecting both sides of your own cards is forbidden; you know your side, the table knows the other.)

**Core loop.** Deal each player a fan (held facing out, never inspected). The team must complete a sequence of public **contracts** drawn from the deck — e.g. "play a triangle: three cards connecting three symbols", "play a 4-card chain", "play three cards all containing symbol X". On your turn, play one card from your fan onto the table, choosing which face shows — but you only ever knew *your* side of it; the moment it leaves your hand you discover what the table knew all along. Then give one legal hint to a teammate ("your leftmost card shows Sun to me" is illegal; pointing rules à la Hanabi: "these two cards of yours show the same symbol to us").

**Why it needs this deck.** Each player permanently knows half of every card in their hand, and — because every pair exists exactly once — the two information halves can be intersected: if I see Moon on your card and Moon/Star is already on the table, my Moon card *cannot* be Star on your side. The deduction engine is the pair-uniqueness property itself; the co-op tension is Hanabi's, but with no dead information and no card ever fully hidden.

**Deck-size fit.** Works at any size. Best at **7 symbols / 21 cards** for the focused game (each visible symbol has only 6 possible partners — deductions complete fast); the 36-card deck plays it via a 7-symbol subset. Scales up for harder campaigns.

**Evaluation.** Needs the deck: maximal — the mechanic is physically impossible with normal cards. Flipping meaningful: choosing which face to *play* is the whole decision. Risks: hint grammar must be tuned hard; possible analysis paralysis at 4P.

---

## 2. FALSE FACE — bluffing under verifiable history

*3–6 players · ~20 min · bluffing / hand management*

**Core loop.** Players hold hands (both sides privately known). On your turn, play a card to the centre showing one face and **claim its hidden face aloud** — truthfully or not. Claims build a running "ledger" (e.g. claimed pairs are claimed *gone*). Any player may **challenge** before the next play: flip the card. Liar caught → liar takes the pot of accumulated cards as penalty; honest player challenged → challenger takes it. Shed your hand first to win.

**The engine.** Because every pair exists exactly once, every claim is a statement about a *unique object*, and the set of all claims must be globally consistent. Claim "this Sun hides Crown" when someone is holding the real Sun/Crown and one player at the table *knows* you're lying — but revealing that they know costs them information too. Late game, the ledger becomes so constrained that lies need real skill: you must lie only into the shrinking set of pairs no one can refute.

**Why it needs this deck.** In normal bluffing games (Cheat, Liar's Dice) lies are statistical. Here every lie is a forgery of a specific unique card, and the deck is a public registry. The bluffing space *provably tightens* every turn — a structural arc no standard deck provides.

**Deck-size fit.** Needs enough pairs that early lies are safe: **9 symbols / 36 cards** best (36 unique pairs, hands of 6 at 6P). At 15 cards the registry closes too fast — lies die by turn three. 28 playable at 3–4P.

**Evaluation.** Needs the deck: high. Interaction: very high (the challenge economy). Risks: first-game players can't price a lie; needs a strong "what's been claimed" memory aid — the played cards themselves form it if claims are placed as an oriented row.

---

## 3. OUROBOROS — the serpent solitaire

*1 player · ~10 min · solo puzzle*

**Mathematical guarantee.** With 7 or 9 symbols, every symbol sits on an even number of cards (6 or 8) — so the complete deck can be chained into **one closed loop** where every adjacent pair of cards shares a symbol at the join. The perfect solution always exists; the puzzle is finding it from a shuffled deck with limited foresight.

**Core loop.** Shuffle. Draw cards one at a time; you may hold at most 3 in reserve. Each drawn (or reserved) card must be added to either end of a growing line, **placed showing the symbol that matches the exposed symbol at that end** — the join "consumes" the matching face, and the card's *other* symbol becomes the new exposed end. (You always know both sides of a drawn card; cards in the line never flip again — placement is commitment.) Win by placing all cards and closing the loop: the two final exposed ends must match.

**Scoring ladder.** Lose: deck stuck with no legal placement. Bronze: all cards placed, open ends. Silver: closed loop. Gold: closed loop with all 3 reserve slots empty at the end.

**Why it needs this deck.** A card *is* an edge; the solitaire is literally constructing an Eulerian circuit of the symbol graph under draw order — flipping decides which endpoint of the edge faces which neighbour. The all-pairs property means no dead duplicate ever clogs the line.

**Deck-size fit.** **7 symbols / 21 cards** (short coffee-break version) and **9 symbols / 36 cards** (the full serpent) — *only* odd symbol counts work; at 6 or 8 symbols a closed loop is mathematically impossible. A quietly strong argument for an odd master count.

**Evaluation.** Needs the deck: total. Risks: solvability rate from random shuffles with 3 reserves needs simulation to tune the reserve count and scoring tiers.

---

## 4. TWELVE TRIALS — the constellation almanac

*1–3 players · ~15 min · solo/co-op spatial puzzle*

**Mathematical guarantee.** The 36-card deck partitions **perfectly into 12 triangles** (three cards forming three symbols pairwise — a Steiner triple system). Better: those 12 triangles group into **4 "seasons" of 3 triangles, each season using all 9 symbols exactly once**. The deck contains a hidden almanac.

**Core loop.** Deal the full deck into a 6×6 grid, faces random. Players (or the soloist) spend a shared budget of **moves** — flip a card, or swap two orthogonally adjacent cards — to organise the grid into 12 contiguous L/I/triomino groups, where each group's three cards form a perfect symbol-triangle *with all three cards showing three different symbols of that triangle*. Completed triangles lock. Score = triangles completed before the move budget runs out; the campaign version tightens the budget across the 4 seasons.

**Co-op mode.** Players alternate moves, no table talk about hidden faces — each player privately studied a different third of the grid during setup (you saw both sides of your 12 cards as you dealt them). Communication is through moves alone.

**Why it needs this deck.** The win condition is the deck's own combinatorial decomposition. The flip decision is load-bearing: a card in the "right" cell may show the wrong face of the right pair.

**Deck-size fit.** Triangle partitions exist *only* at 7 and 9 symbols. **9/36** is the flagship (12 triangles, 4 seasons); **7/21** gives a small 7-triangle version (the Fano plane!). 6 and 8 symbols cannot host this game at all.

**Evaluation.** Needs the deck: total. Risks: move-budget tuning; locked-triangle adjacency rules need a prototype on a real table.

---

## 5. THE UNPLAYED PAIR — trick-taking with a hole in it

*3–5 players · ~25 min · trick-taking / deduction*

**Core loop.** Remove one card unseen, then deal evenly and place any leftovers face-up as the public **morgue** (3P: 11 each + 2 in the morgue; 4P: 8 each + 3; 5P: 7 each, no morgue — the remainder *is* the mechanic). Morgue cards are flipped once for all to see, then struck off everyone's list. Classic trick structure with two twists: **(1) Follow by either face** — you must follow the led symbol if *either side* of any card in your hand carries it, and flipping a card to follow is the game's signature move; what you flip *away from* is information leaked. **(2)** No fixed ranks: the trick is won by the card whose *hidden* face is highest in a public rotating order — so winning a trick reveals your card's back, feeding the deduction game.

**Endgame.** After the last trick, players secretly bet on the identity of the unplayed pair. Tricks score 1; a correct bet scores 5. Card-counting is unusually clean: every pair exists once, so every card you see (front *or* back) strikes exactly one candidate off the list.

**Why it needs this deck.** "Void in a suit" becomes provable: if Sun/Moon, Sun/Star… have all appeared, your opponent's failure to follow Sun is *informative arithmetic*, not chance. The deck turns trick-taking's fuzzy inference into exact logic — closer to a whodunit.

**Deck-size fit.** **9 symbols / 36 cards**: 11/8/7 tricks at 3/4/5P, and at 5P the deal leaves exactly 1 card over — the unplayed pair removes itself. 28 works at 3P (9 tricks). 15/21 too short for the deduction to mature.

**Evaluation.** Needs the deck: high. Interaction: high. Risks: the hidden-face ranking rule needs simplification passes; may want a "first game: fixed rank order" preset.

---

## 6. CROSSROADS — the only road between two cities

*2 players · ~15 min · abstract route duel*

**Core loop.** Symbols are cities, cards are roads — each card the *only* road between its two cities. Split the shuffled deck evenly; both players see their own hands fully. Players alternate: **build** (add a card to the shared map, joining it at a city its pair shares with the existing network, oriented to show which of its two cities it "serves") or **burn** (discard a card from hand face-chosen to the ditch — that road can now never be built). Each player holds 3 secret **contract** cards set aside at the start (their pairs are routes to complete: "connect city A to city B through the network").

**Scoring.** A contract scores when its two cities are connected by built roads *currently oriented* to serve the route (orientation = flip wars: your opponent can flip a road on their turn instead of building, breaking your route's service while feeding their own). Game ends when hands empty; contracts + longest-served-route bonus decide it.

**Why it needs this deck.** Pair-uniqueness makes every burn a permanent, surgical act of denial — you're not discarding *a* road, you're demolishing *the* bridge between two specific cities. Your opponent's contracts are cards *not in your hand and not in the map*: the deduction writes itself.

**Deck-size fit.** **8 symbols / 28 cards** is the sweet spot — all cities have odd degree (7), so road networks are structurally imperfect and chokepoints real (no Eulerian comfort); 14-card hands, 3 contracts each. 15-card version is a sharp micro-duel. At 36 the map sprawls.

**Evaluation.** Needs the deck: very high. Risks: connectivity + orientation rules must stay physically legible on a table without a board; needs a "served" convention (e.g. pointing the visible face along the route).

---

## 7. THE COUNCIL — reversible commitments

*3–6 players · ~25 min · simultaneous negotiation / game theory*

**Core loop.** Each round, flip three random deck cards: their visible symbols are the **issues** on the table, each carrying a pot (cards from the deck). Players hold small hands. Everyone secretly commits one card, then all reveal simultaneously: your card supports the issue matching its visible face (a card showing none of the three issues is an **abstention** — it banks small but guaranteed). Then one **turncoat round** in seat order: each player may flip their committed card — *to its one specific alternative* — possibly defecting to another issue or into abstention. Majority faction on each issue splits its pot; lone backers take it all.

**The game theory.** Every commitment is public-but-reversible, and everyone can read exactly which defection each card permits (the pair is printed on it, half visible — and the table knows every pair exists once). The negotiation phase before reveal is poker over a *finite, inspectable* defection space: "I can flip to Crown" is a threat whose credibility is literally written on the card backs already seen this game. Chicken, coalition, and credible-threat structures arise from component honesty rather than rules text.

**Why it needs this deck.** A standard card commits absolutely; this card commits to a *pair* of futures. The 2-option defection is the whole game — richer than no options, sharper than all options.

**Deck-size fit.** **9 symbols / 36 cards** at 4–6 players: hands of 5 even at a full table leave 6 deck cards for issues and pots, and 9 symbols keep issue-collisions frequent. At 15–21 cards the pots and hands starve above 3P.

**Evaluation.** Needs the deck: high. Interaction: maximal — it's all interaction. Risks: kingmaking at 5–6P; pot-splitting rules need to stay arithmetic-free.

---

## 8. HOT POTATO PAIRS — the back of your card is the problem

*3–6 players · ~10 min · party shedding*

**Core loop.** Deal the whole deck (36 ÷ 6 = exactly 6 each at full table). One card opens the pile. On your turn, play a card whose **visible face matches the pile's visible face** — or flip a hand card and play it matched. The catch, and the game: **your played card's hidden face must not match the hidden face of the card beneath it** — and the pile's hidden face is public *briefly* (everyone saw the face that was showing before each card landed, so the pile's backs are a public memory chain). Play an illegal back → take the pile. First to empty their hand wins.

**The texture.** Every play is constrained on both sides of the card: the front must match what's showing, the back must dodge what's remembered. Since each symbol appears on exactly 8 cards, "safe backs" run out at a knowable rate, and the endgame becomes a forced-feeding race. Quick, loud, and surprisingly counting-friendly for sharks.

**Why it needs this deck.** A shedding game where the *unseen half* of your card is the dangerous half can't exist with one-faced cards. The flip-to-match move makes the deck's signature action the escape hatch.

**Deck-size fit.** **9 symbols / 36 cards** — the only size dealing cleanly to 3, 4 *and* 6 players. (5P: deal 7 each, one card opens the pile.) Smaller decks cap the table at 3.

**Evaluation.** Needs the deck: medium-high (strongest of the "light filler" options). Risks: the back-memory rule needs a forgiving first-game variant (backs checked only against the top card).

---

## 9. THE ORRERY — the sky machine

*1–3 players · ~15–25 min · solo/co-op sorting puzzle*

**Core loop.** Shuffle the full 36-card deck (randomising which face shows). Spread all cards face-up in a pool (the **sky**). Your goal: sort the 36 cards into **four orbits** of 9 cards each, where every orbit shows all 9 symbols exactly once on its visible faces *and* all 9 symbols exactly once on its hidden faces. Move cards freely between orbits; **every flip costs 1 point**. Your score is total flips — lower is better.

**The sky debt.** Before solving, count how many times each symbol appears as a visible face. In a solved state, each symbol must be visible exactly 4 times (once per orbit). The excess over 4 (summed across all over-shown symbols) is the deal's **sky debt** — an exact lower bound on flips this deal requires. It makes every deal self-calibrating: score = sky debt + your inefficiency.

**Why it needs this deck.** The 36 cards are the 36 edges of K₉. Each orbit is a permutation matrix — 9 directed edges where every vertex has in-degree 1 and out-degree 1 (visible = arrival, hidden = departure). The deck guarantees such decompositions exist (the emergency almanac proves one); the puzzle space is the set of all valid decompositions reachable from a given shuffle. Pair-uniqueness means no two orbits can "fight" over the same card — every edge belongs to exactly one orbit.

**Relationship to TWELVE TRIALS.** Both are open-information flip puzzles that decompose the deck. TWELVE TRIALS sorts into 12 triangles (Steiner triples); THE ORRERY sorts into 4 orbits (permutation matrices). Different combinatorial structure, different search space, same core verb (flip to minimise cost). THE ORRERY adds the sky debt — a visible global lower bound that TWELVE TRIALS lacks.

**Deck-size fit.** **9 symbols / 36 cards** (4 orbits of 9). Odd symbol counts: **7/21** gives 3 orbits of 7 (Apprentice Orrery); **5/10** gives 2 orbits of 5 (Pocket Orrery — mostly a teaching exercise). Even symbol counts don't cleanly partition into orbit permutations, so 6/8 are excluded.

**Evaluation.** Needs the deck: very high — the orbit structure is a genuine K₉ decomposition. Physical handling: exemplary (fully open information, inspection always free, no hidden-face memory). Flipping load-bearing: yes — it is the entire cost function. Risks: potential overlap with TWELVE TRIALS — does it feel like a distinct experience, or a relabelled cousin? The sky debt mechanic and the orbit vs. triangle structure may differentiate sufficiently, but this is a first-table question.

---

## Status (updated June 2026)

The deck is now fixed at 9 symbols / 36 cards (`DECK_SIZE_DECISION.md`); concepts were developed to full rulebooks.

1. **JANUS** — ✅ full rulebook (`Janus/`). The collection's signature-mechanic candidate. Next: table test the omen economy.
2. **FALSE FACE** — ✅ full rulebook (`False Face/`). Next: table test ledger pacing.
3. **TWELVE TRIALS** — ✅ promoted to main-game development after OUROBOROS was cut; redesigned as a fully open-information puzzle (no hidden-face memory, no luck-blame) with an exact solver tuning the score tiers (`Twelve Trials/`). **Has been table-tested.**
4. **OUROBOROS** — ❌ developed, simulated, then **cut after live testing** (June 2026): too luck-driven, and tracking the hidden open symbol at the serpent's head was physically awkward. Kept in `Ouroboros/` as a record; its lessons (open information beats hidden-face memory in solo play; thin bot skill-gaps predict dull tables) now constrain the remaining designs.
5. **THE UNPLAYED PAIR** — ✅ full rulebook (`Unplayed Pair/`). The hidden-face trick-rank rule was reworked into a public trick-end reveal per the OUROBOROS lesson; won tricks and morgue stay open for inspection (deduction, never memory). Next: table test at 4P.
6. **THE COUNCIL** — ✅ full rulebook (`Council/`). Lone-supporter-takes-all minority game with rollover stacks; palms-commit protocol replaces impossible face-down concealment. Next: table test at 4–5P.
7. **CROSSROADS** — ✅ full rulebook (`Crossroads/`). Layout solved: the eight symbol-9 cards become the city ring; roads point at the city their visible face names (one-way traffic); contracts are the cards you keep. Perfect-information abstract. **Has been table-tested.**
8. **HOT POTATO PAIRS → TURNOVER** — ✅ full rulebook (`Turnover/`). Renamed; the back-memory chain died with OUROBOROS and is replaced by match-and-turn: all constraints live on the visible top face. Next: party test at 5–6P.
9. **THE ORRERY** — ✅ full rulebook (`The Orrery/`). Open-information orbit-sorting puzzle — sibling to TWELVE TRIALS via a different decomposition (4 permutation orbits vs. 12 triangles). Sky debt gives a visible per-deal lower bound. **Has been table-tested.**

**Note:** TRIGON (`Trigon/`) and TURNCOAT (`Turncoat/`) are extensively simulation-validated (~22–23k games each) but have **not** been table-tested. They are awaiting their first physical play.

**All nine concepts are now resolved: eight developed to rulebooks, one (OUROBOROS) cut by playtest.** Symbol identity study: `SYMBOL_SETS.md`.

---

## 10. CABAL — the forbidden three *(concept stage — not yet a rulebook)*

*2 players · ~10–15 min · perfect-information abstract / avoidance*

> **Status & scope.** This is a **rung-4 new concept** (`focus-priority.md`). It is logged for exploration only. Per the circuit breaker, it is **not** to be developed into a full rulebook until at least one rung-2/3 game (TRIGON, TURNCOAT, FACE VALUE, JANUS…) has had its first table test. Working title; alternatives: SCHISM, QUORUM, THE THIRD ROAD. Avoid TRIAD — too close to TRIGON.

**The deck property it exploits.** The 6-symbol subset is **K₆** rendered as 15 cards (each card the unique edge between two of symbols 1–6). The collection has no other **inevitability** mechanic; everything else is about what you *can* build, this is about what you *cannot avoid* (`deck_mathematical_analysis.md` II.4).

> **Framing correction (don't headline Ramsey).** It's tempting to sell this on R(3,3) = 6 ("any 2-split forces a mono-triangle"). That's the *weak* statement and it oversells the theorem: real play produces a roughly **even 8/7 split**, and Ramsey holds for *all* splits including the lopsided ones that never occur. Under the balanced splits a game actually generates, the binding facts are stronger and tighter (verified, `_ramsey_balance_check` — enumerated all 12,870 balanced colourings of K₆):
> - minimum mono-triangles = **2** (Goodman), **mean = 4.0**, max = 7;
> - **no** colouring has exactly 0 or exactly 1 — the count jumps straight from impossible-zero to two.
>
> So a balanced split doesn't force *one* triangle, it forces *several* (≈4), and provably never fewer than two. **Ramsey's only real job here is the no-draw guarantee** (the board can't finish triangle-free) — a footnote, not the hook. The hook is **Goodman's floor of 2 plus the 2→7 spread**: at a fixed balanced count, *structure* (which edges, not how many) swings the result from 2 to 7, and that swing is the entire skill space.

**Design consequence — the game needs agency over the split.** A flat even deal is inert: it *already* forces ≈4 triangles with near-certainty, so nobody is choosing anything. The game only exists when players steer the split. Two levers, only the second of which makes full-strength Ramsey load-bearing:

**Core loop (primary form — agency over *which* edges).** Lay the six symbols as a hex of "houses"; the 15 cards are the roads between them. Players alternate **claiming** one unclaimed card by orienting it toward their side of the table (orientation = ownership colour — fully visible, glanceable, no hidden-face memory; the CROSSROADS technique, `physical-handling.md` "orientation as state"). The count stays balanced 8/7, but you steer *structure* to push the forced triangles into the opponent's colour. Two win conditions to test:
> - **Sudden-death (Sim):** you lose the instant you own all three roads of a symbol-triangle. Decisive (the no-draw guarantee bites), but the loss can feel like one fatal misstep.
> - **Goodman scoring:** place all 15; each mono-triangle in *your* colour is a debt point; fewer wins. The floor of 2 means there's always blood; the 2→7 spread means structure choices pay off across the whole game. Likely the better game — it rewards play, not a single slip.
>
> **Pie rule** on the opening claim (Sim is a second-player win under perfect play — the seat-asymmetry fix CROSSROADS uses).

**The variant where Ramsey's generality earns its keep — agency over *how many* edges.** A dumping/refusing form: players push unwanted roads onto each other; whoever ends up holding a triangle loses. *Here* the strategy space genuinely visits unbalanced splits — and the point of R(3,3) is precisely that even a lopsided 13/2 hoard can't escape, so refusing-to-take is not a safe out. This is the only framing where "any colouring contains a triangle" is doing visible work rather than sitting in the background. Worth a concept of its own if the claiming form tests well.

**The signature hook — the tightness campaign.** Play a best-of series that *starts* at **5 symbols / 10 cards**, where a triangle-free split provably exists (colour the pentagon vs. the pentagram — each is a triangle-free 5-cycle; verified: the balanced 5/5 split reaches 0 mono-triangles), so a **draw is an achievable skill result**. Then ratchet to **6 symbols**, where avoidance becomes impossible. Players *feel* the threshold instead of being told it: adding one symbol removes the possibility of safety. This 5→6 jump is the most deck-native, most original part of the idea.

**Why it (probably) needs this deck.** "Every pair exactly once" is precisely what lets a card *be* an edge of K₆ — without it you cannot physically lay the complete graph as components, and the forcing theorem has nothing to bite on. Deck-necessity is *moderate* (pencil-and-paper Sim exists), but the physical realisation — roads you can see, a tightness dial you change by adding/removing a symbol's cards — is the part that only this deck delivers.

**Honest evaluation (rubric, `design-principles.md`).**
1. Exploits all-pairs: **yes** (cards as K₆ edges). 2. Physically works: **yes** — open information, orientation-as-state, nothing buried. 3. Visible/deducible: **yes** — zero hidden-face memory. 4. **Flipping matters: weak.** The literal symbol-swap is *structurally inert* for Ramsey — a card is the edge {A,B} regardless of face; only the 2-colouring (orientation/ownership) affects the maths. Do not contort the game to force symbol-swapping. 5. Pair-uniqueness matters: **yes**. 6. Distinct experience: **partially** — inevitability/avoidance mood is new, but it shares "2P perfect-info abstract" with CROSSROADS; the table must confirm they feel different. 7. Gap-fill: a quick 2P avoidance filler + the only inevitability game. 8. Clean to explain: **yes** ("don't be the one who completes a triangle"). 9. Testable on Set D today: **yes**. 10. Fastest falsification: **two short sessions** — (a) does 5-symbol play create real "I survived" tension and earned draws, (b) does 6-symbol forcing read as dramatic inevitability rather than an arbitrary loss?

**Risks / why it might be cut.** Sim is famously more elegant than *fun* — human players struggle to see triangle threats (K₆ has 20 triangles), so the loss can feel arbitrary rather than earned. The physical board (threats visible as roads) and the 5→6 escalation are the bets that make it approachable. If a first table test shows the threat-reading is opaque and the loss feels random, **cut it cleanly and record the lesson** (a thin/illegible decision space is the OUROBOROS failure mode). It overlaps CROSSROADS on player count and information model; it earns its place only if the *mood* is genuinely distinct.

**Deck-size fit — symmetric goals, and the player-count wall.** Both players should avoid the *same* shape (symmetric goals are fairer and cleaner than the earlier asymmetric triangle-vs-clique sketch, now retired). The forbidden shape sets the threshold = the **diagonal Ramsey number** = symbols needed:

- **6 symbols / 15 cards — the legible home (R(C₃,C₃) = 6).** Both avoid a triangle; 5/10 is the escapable first rung (the balanced 5/5 split reaches 0 mono-triangles, verified). Clean, teachable, 20 triangles scannable by eye. **But it uses only 15 of 36 cards — a light 2P filler, not a flagship.** Subset use is legitimate and intended (`deck-structure.md`; cf. JANUS@7) but doesn't *showcase* the master deck.
- **9 symbols / 36 cards — the deck-defining version (R(C₅,C₅) = 9).** Both avoid a **pentagon** (5-cycle). All 36 cards are edges, even 18/18 split, threshold 8→9 (K₈ escapable — witness verified: two K₄ vs K₄,₄, no mono C₅ in either colour; upper bound cited). Fully symmetric, uses the whole deck, and you hunt a **loop** rather than a clique. Cost: a 5-cycle is the hardest of these to scan late-game.
- *(C₄ symmetric, R(C₄,C₄)=6, is also 15 cards but a 4-loop is harder to spot than a triangle with no deck-size gain — no reason to prefer it over triangles.)*

> **Binding finding — this is a 2-player mechanic, permanently.** Symmetric forced-avoidance for *r* players needs the multicolour Ramsey number R_r(H) ≤ 9. But these explode: **R(C₄,C₄,C₄) = 11** (3 players → 11 symbols), **R(C₃,C₃,C₃,C₃) ≈ 51–62** (4 players → ~51 symbols). The deck caps at 9 vertices, so **no 3+ player version can guarantee the forcing — ever.** Verified for the tempting 3-player/C₄ case: unlike the 2-player Goodman case (where the even split *restored* forcing), here the balance loophole fails too — a balanced **12/12/12 C₄-free partition of K₉ exists** (constructed explicitly), so perfect play is a three-way survival with **no guaranteed loser**. A 3-player version therefore loses the inevitability hook entirely (becoming a generic avoidance abstract that fails the deck-necessity test) and invites 2-on-1 kingmaking besides. Don't chase a multiplayer CABAL; the inevitability lives only at two colours. R(C₅,C₅)=9 is the largest forbidden-shape game the deck can host.

**Caveats for the cycle (9-symbol) version:** late-game legibility — a loop is easy to *trace*, but a dense colour class hides many 5-cycles by the endgame; easier than cliques, not free. This is the make-or-break handling question if the 9-symbol form is pursued.

> **Open fork (record, don't resolve yet):** the 6-symbol triangle game (most legible, 15-card filler) vs the 9-symbol pentagon game (whole deck, deck-defining, but the hardest to scan). Prototype the 6-symbol triangle version first — it answers the only question that gates everything else: *is forced-shape avoidance fun at all on this deck?* Only if yes does the 9-symbol pentagon legibility problem become worth solving.
