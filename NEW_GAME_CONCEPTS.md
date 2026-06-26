# New Game Concepts

*Eight concept sheets expanding the collection beyond TRIGON and TURNCOAT. Each exploits a property of the all-pairs flip deck that the existing games don't touch. Deck-size fit is stated per game; see [DECK_SIZE_DECISION.md](DECK_SIZE_DECISION.md) for the overall recommendation.*

Portfolio coverage at a glance:

| # | Game | Genre | Players | Key deck property used |
|---|---|---|---|---|
| 1 | JANUS | Co-op communication | 2–4 | The fanned hand shows opposite faces to opposite sides of the table |
| 2 | FALSE FACE | Bluffing | 3–6 | Every lie about a hidden side is eventually falsifiable (pairs are unique) |
| 3 | OUROBOROS | Solo puzzle | 1 | K₇/K₉ have Eulerian circuits — the whole deck chains into one loop |
| 4 | TWELVE TRIALS | Solo / co-op puzzle | 1–3 | The 36-card deck partitions perfectly into 12 symbol-triangles |
| 5 | THE UNPLAYED PAIR | Trick-taking / deduction | 3–5 | One missing card is fully identifiable by elimination *(trick layer parked — superseded by §11/§12; see Parking Lot)* |
| 6 | CROSSROADS | 2P abstract route duel | 2 | Each card is the *only* road between its two symbols |
| 7 | THE COUNCIL | Negotiation / game theory | 3–6 | Every commitment is reversible — but only to one specific alternative |
| 8 | HOT POTATO PAIRS | Party shedding | 3–6 | Both faces constrain legal plays; the back of your card is a liability |
| 9 | THE ORRERY | Solo / co-op sorting puzzle | 1–3 | 36 cards partition into four 9-card orbits, each a permutation of all 9 symbols on both faces |
| 10 | CABAL *(concept stage)* | 2P abstract avoidance | 2 | Goodman: any balanced K₆ split forces ≥2 mono-triangles (mean ~4); 5→6 threshold turns "survivable" into "doomed" |
| 11 | GLEAN | Trick-taking / majority | 3–4–6 | Each captured card scores toward *two* symbol-majorities at once; pair-uniqueness makes the contested card specific |
| 12 | BLIGHT | Trick-taking / avoidance | 3–4–6 | The *hidden* face is the penalty — the back of the card is the poison; shoot-the-moon by taking it all |
| 13 | CAIRN *(concept stage)* | Compact solo chain patience | 1 | A card is an edge; cards chain by a shared sign — the edge-adjacency property, unused since OUROBOROS was cut, now in a ≤4-pile footprint |
| 14 | MERIDIAN *(sim-validated)* | Network route-race / drafting | 2–4 | Each card is a directed road *and* a unique connection goal; "each sign on 8 cards" bounds the map; a flip re-aims a road to make or break a directed route |

Existing games already cover: tactical grid engine (TRIGON) and direct-conflict allegiance (TURNCOAT).

---

## 1. JANUS — co-operative signalling

*2–4 players · ~20 min · co-op*

**The trick that makes it exist:** hold a fan of these cards normally and you see one face of each card while everyone else sees the *other* face. There is no card back — the information split is symmetric, real, and free. No other deck does this. (Inspecting both sides of your own cards is forbidden; you know your side, the table knows the other.)

**Core loop.** Deal each player a fan (held facing out, never inspected). The team must complete a sequence of public **contracts** drawn from the deck — e.g. "play a triangle: three cards connecting three symbols", "play a 4-card chain", "play three cards all containing symbol X". On your turn, play one card from your fan onto the table, choosing which face shows — but you only ever knew *your* side of it; the moment it leaves your hand you discover what the table knew all along. Then give one legal hint to a teammate ("your leftmost card shows Crown to me" is illegal; pointing rules à la Hanabi: "these two cards of yours show the same symbol to us").

**Why it needs this deck.** Each player permanently knows half of every card in their hand, and — because every pair exists exactly once — the two information halves can be intersected: if I see Moon on your card and Moon/Star is already on the table, my Moon card *cannot* be Star on your side. The deduction engine is the pair-uniqueness property itself; the co-op tension is Hanabi's, but with no dead information and no card ever fully hidden.

**Deck-size fit.** Works at any size. Best at **7 symbols / 21 cards** for the focused game (each visible symbol has only 6 possible partners — deductions complete fast); the 36-card deck plays it via a 7-symbol subset. Scales up for harder campaigns.

**Evaluation.** Needs the deck: maximal — the mechanic is physically impossible with normal cards. Flipping meaningful: choosing which face to *play* is the whole decision. Risks: hint grammar must be tuned hard; possible analysis paralysis at 4P.

---

## 2. FALSE FACE — bluffing under verifiable history

*3–6 players · ~20 min · bluffing / hand management*

**Core loop.** Players hold hands (both sides privately known). On your turn, play a card to the centre showing one face and **claim its hidden face aloud** — truthfully or not. Claims build a running "ledger" (e.g. claimed pairs are claimed *gone*). Any player may **challenge** before the next play: flip the card. Liar caught → liar takes the pot of accumulated cards as penalty; honest player challenged → challenger takes it. Shed your hand first to win.

**The engine.** Because every pair exists exactly once, every claim is a statement about a *unique object*, and the set of all claims must be globally consistent. Claim "this Moon hides Crown" when someone is holding the real Moon/Crown and one player at the table *knows* you're lying — but revealing that they know costs them information too. Late game, the ledger becomes so constrained that lies need real skill: you must lie only into the shrinking set of pairs no one can refute.

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

**Why it needs this deck.** "Void in a suit" becomes provable: if Crown/Moon, Crown/Star… have all appeared, your opponent's failure to follow Crown is *informative arithmetic*, not chance. The deck turns trick-taking's fuzzy inference into exact logic — closer to a whodunit.

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

The deck is now fixed at 9 symbols / 36 cards ([DECK_SIZE_DECISION.md](DECK_SIZE_DECISION.md)); concepts were developed to full rulebooks.

1. **JANUS** — ✅ full rulebook ([Janus/](Janus/)). The collection's signature-mechanic candidate. Next: table test the omen economy.
2. **FALSE FACE** — ✅ full rulebook ([False Face/](False%20Face/)). Next: table test ledger pacing.
3. **TWELVE TRIALS** — ✅ promoted to main-game development after OUROBOROS was cut; redesigned as a fully open-information puzzle (no hidden-face memory, no luck-blame) with an exact solver tuning the score tiers ([Twelve Trials/](Twelve%20Trials/)). **Has been table-tested.**
4. **OUROBOROS** — ↩️ developed, simulated, cut after live testing (June 2026), then **revived to the pipeline (Stage 2)** later in June 2026. The cut reasons were re-examined: the buried open-symbol bug is fixed in **v1.1** (lay each card showing its *onward* symbol — both open ends stay face-up, never lift the serpent), and a Monte-Carlo planner put the skill ceiling at **~1.74× (n=9) / ~1.84× (n=7)** over random, above the healthy bar — retiring the "thin skill gap / luck-dominant" verdict that rested on one-ply floor numbers. Kept in [Ouroboros/](Ouroboros/); see [OUROBOROS_design_analysis.md](Ouroboros/OUROBOROS_design_analysis.md) §6. **Next: first table test of v1.1.**
5. **THE UNPLAYED PAIR** — ✅ full rulebook ([The Unplayed Pair/](The%20Unplayed%20Pair/)). The hidden-face trick-rank rule was reworked into a public trick-end reveal per the OUROBOROS lesson; won tricks and morgue stay open for inspection (deduction, never memory). Next: table test at 4P.
6. **THE COUNCIL** — ✅ full rulebook ([The Council/](The%20Council/)). Lone-supporter-takes-all minority game with rollover stacks; palms-commit protocol replaces impossible face-down concealment. Next: table test at 4–5P.
7. **CROSSROADS** — ✅ full rulebook ([Crossroads/](Crossroads/)). Layout solved: the eight symbol-9 cards become the city ring; roads point at the city their visible face names (one-way traffic); contracts are the cards you keep. Perfect-information abstract. **Has been table-tested.**
8. **HOT POTATO PAIRS → TURNOVER** — ✅ full rulebook ([Turnover/](Turnover/)). Renamed; the back-memory chain died with OUROBOROS and is replaced by match-and-turn: all constraints live on the visible top face. Next: party test at 5–6P.
9. **THE ORRERY** — ✅ full rulebook ([The Orrery/](The%20Orrery/)). Open-information orbit-sorting puzzle — sibling to TWELVE TRIALS via a different decomposition (4 permutation orbits vs. 12 triangles). Sky debt gives a visible per-deal lower bound. **Has been table-tested.**

**Note:** TRIGON ([Trigon/](Trigon/)) and TURNCOAT ([Turncoat/](Turncoat/)) are extensively simulation-validated (~22–23k games each) but have **not** been table-tested. They are awaiting their first physical play.

**All nine concepts are now resolved: eight developed to rulebooks, one (OUROBOROS) cut by playtest.** Symbol identity study: [SYMBOL_SETS.md](SYMBOL_SETS.md).

---

## 10. CABAL — the forbidden three *(concept stage — not yet a rulebook)*

*2 players · ~10–15 min · perfect-information abstract / avoidance*

> **Status & scope.** This is a **rung-4 new concept** ([focus-priority.md](.kiro/steering/focus-priority.md)). It is logged for exploration only. Per the circuit breaker, it is **not** to be developed into a full rulebook until at least one rung-2/3 game (TRIGON, TURNCOAT, FACE VALUE, JANUS…) has had its first table test. Working title; alternatives: SCHISM, QUORUM, THE THIRD ROAD. Avoid TRIAD — too close to TRIGON.

**The deck property it exploits.** The 6-symbol subset is **K₆** rendered as 15 cards (each card the unique edge between two of symbols 1–6). The collection has no other **inevitability** mechanic; everything else is about what you *can* build, this is about what you *cannot avoid* ([deck_mathematical_analysis.md](Reference/deck_mathematical_analysis.md) II.4).

> **Framing correction (don't headline Ramsey).** It's tempting to sell this on R(3,3) = 6 ("any 2-split forces a mono-triangle"). That's the *weak* statement and it oversells the theorem: real play produces a roughly **even 8/7 split**, and Ramsey holds for *all* splits including the lopsided ones that never occur. Under the balanced splits a game actually generates, the binding facts are stronger and tighter (verified, `_ramsey_balance_check` — enumerated all 12,870 balanced colourings of K₆):
> - minimum mono-triangles = **2** (Goodman), **mean = 4.0**, max = 7;
> - **no** colouring has exactly 0 or exactly 1 — the count jumps straight from impossible-zero to two.
>
> So a balanced split doesn't force *one* triangle, it forces *several* (≈4), and provably never fewer than two. **Ramsey's only real job here is the no-draw guarantee** (the board can't finish triangle-free) — a footnote, not the hook. The hook is **Goodman's floor of 2 plus the 2→7 spread**: at a fixed balanced count, *structure* (which edges, not how many) swings the result from 2 to 7, and that swing is the entire skill space.

**Design consequence — the game needs agency over the split.** A flat even deal is inert: it *already* forces ≈4 triangles with near-certainty, so nobody is choosing anything. The game only exists when players steer the split. Two levers, only the second of which makes full-strength Ramsey load-bearing:

**Core loop (primary form — agency over *which* edges).** Lay the six symbols as a hex of "houses"; the 15 cards are the roads between them. Players alternate **claiming** one unclaimed card by orienting it toward their side of the table (orientation = ownership colour — fully visible, glanceable, no hidden-face memory; the CROSSROADS technique, [physical-handling.md](.kiro/steering/physical-handling.md) "orientation as state"). The count stays balanced 8/7, but you steer *structure* to push the forced triangles into the opponent's colour. Two win conditions to test:
> - **Sudden-death (Sim):** you lose the instant you own all three roads of a symbol-triangle. Decisive (the no-draw guarantee bites), but the loss can feel like one fatal misstep.
> - **Goodman scoring:** place all 15; each mono-triangle in *your* colour is a debt point; fewer wins. The floor of 2 means there's always blood; the 2→7 spread means structure choices pay off across the whole game. Likely the better game — it rewards play, not a single slip.
>
> **Pie rule** on the opening claim (Sim is a second-player win under perfect play — the seat-asymmetry fix CROSSROADS uses).

**The variant where Ramsey's generality earns its keep — agency over *how many* edges.** A dumping/refusing form: players push unwanted roads onto each other; whoever ends up holding a triangle loses. *Here* the strategy space genuinely visits unbalanced splits — and the point of R(3,3) is precisely that even a lopsided 13/2 hoard can't escape, so refusing-to-take is not a safe out. This is the only framing where "any colouring contains a triangle" is doing visible work rather than sitting in the background. Worth a concept of its own if the claiming form tests well.

**The signature hook — the tightness campaign.** Play a best-of series that *starts* at **5 symbols / 10 cards**, where a triangle-free split provably exists (colour the pentagon vs. the pentagram — each is a triangle-free 5-cycle; verified: the balanced 5/5 split reaches 0 mono-triangles), so a **draw is an achievable skill result**. Then ratchet to **6 symbols**, where avoidance becomes impossible. Players *feel* the threshold instead of being told it: adding one symbol removes the possibility of safety. This 5→6 jump is the most deck-native, most original part of the idea.

**Why it (probably) needs this deck.** "Every pair exactly once" is precisely what lets a card *be* an edge of K₆ — without it you cannot physically lay the complete graph as components, and the forcing theorem has nothing to bite on. Deck-necessity is *moderate* (pencil-and-paper Sim exists), but the physical realisation — roads you can see, a tightness dial you change by adding/removing a symbol's cards — is the part that only this deck delivers.

**Honest evaluation (rubric, [design-principles.md](.kiro/steering/design-principles.md)).**
1. Exploits all-pairs: **yes** (cards as K₆ edges). 2. Physically works: **yes** — open information, orientation-as-state, nothing buried. 3. Visible/deducible: **yes** — zero hidden-face memory. 4. **Flipping matters: weak.** The literal symbol-swap is *structurally inert* for Ramsey — a card is the edge {A,B} regardless of face; only the 2-colouring (orientation/ownership) affects the maths. Do not contort the game to force symbol-swapping. 5. Pair-uniqueness matters: **yes**. 6. Distinct experience: **partially** — inevitability/avoidance mood is new, but it shares "2P perfect-info abstract" with CROSSROADS; the table must confirm they feel different. 7. Gap-fill: a quick 2P avoidance filler + the only inevitability game. 8. Clean to explain: **yes** ("don't be the one who completes a triangle"). 9. Testable on Set D today: **yes**. 10. Fastest falsification: **two short sessions** — (a) does 5-symbol play create real "I survived" tension and earned draws, (b) does 6-symbol forcing read as dramatic inevitability rather than an arbitrary loss?

**Risks / why it might be cut.** Sim is famously more elegant than *fun* — human players struggle to see triangle threats (K₆ has 20 triangles), so the loss can feel arbitrary rather than earned. The physical board (threats visible as roads) and the 5→6 escalation are the bets that make it approachable. If a first table test shows the threat-reading is opaque and the loss feels random, **cut it cleanly and record the lesson** (a thin/illegible decision space is the OUROBOROS failure mode). It overlaps CROSSROADS on player count and information model; it earns its place only if the *mood* is genuinely distinct.

**Deck-size fit — symmetric goals, and the player-count wall.** Both players should avoid the *same* shape (symmetric goals are fairer and cleaner than the earlier asymmetric triangle-vs-clique sketch, now retired). The forbidden shape sets the threshold = the **diagonal Ramsey number** = symbols needed:

- **6 symbols / 15 cards — the legible home (R(C₃,C₃) = 6).** Both avoid a triangle; 5/10 is the escapable first rung (the balanced 5/5 split reaches 0 mono-triangles, verified). Clean, teachable, 20 triangles scannable by eye. **But it uses only 15 of 36 cards — a light 2P filler, not a flagship.** Subset use is legitimate and intended ([deck-structure.md](.kiro/steering/deck-structure.md); cf. JANUS@7) but doesn't *showcase* the master deck.
- **9 symbols / 36 cards — the deck-defining version (R(C₅,C₅) = 9).** Both avoid a **pentagon** (5-cycle). All 36 cards are edges, even 18/18 split, threshold 8→9 (K₈ escapable — witness verified: two K₄ vs K₄,₄, no mono C₅ in either colour; upper bound cited). Fully symmetric, uses the whole deck, and you hunt a **loop** rather than a clique. Cost: a 5-cycle is the hardest of these to scan late-game.
- *(C₄ symmetric, R(C₄,C₄)=6, is also 15 cards but a 4-loop is harder to spot than a triangle with no deck-size gain — no reason to prefer it over triangles.)*

> **Binding finding — this is a 2-player mechanic, permanently.** Symmetric forced-avoidance for *r* players needs the multicolour Ramsey number R_r(H) ≤ 9. But these explode: **R(C₄,C₄,C₄) = 11** (3 players → 11 symbols), **R(C₃,C₃,C₃,C₃) ≈ 51–62** (4 players → ~51 symbols). The deck caps at 9 vertices, so **no 3+ player version can guarantee the forcing — ever.** Verified for the tempting 3-player/C₄ case: unlike the 2-player Goodman case (where the even split *restored* forcing), here the balance loophole fails too — a balanced **12/12/12 C₄-free partition of K₉ exists** (constructed explicitly), so perfect play is a three-way survival with **no guaranteed loser**. A 3-player version therefore loses the inevitability hook entirely (becoming a generic avoidance abstract that fails the deck-necessity test) and invites 2-on-1 kingmaking besides. Don't chase a multiplayer CABAL; the inevitability lives only at two colours. R(C₅,C₅)=9 is the largest forbidden-shape game the deck can host.

**Caveats for the cycle (9-symbol) version:** late-game legibility — a loop is easy to *trace*, but a dense colour class hides many 5-cycles by the endgame; easier than cliques, not free. This is the make-or-break handling question if the 9-symbol form is pursued.

> **Open fork (record, don't resolve yet):** the 6-symbol triangle game (most legible, 15-card filler) vs the 9-symbol pentagon game (whole deck, deck-defining, but the hardest to scan). Prototype the 6-symbol triangle version first — it answers the only question that gates everything else: *is forced-shape avoidance fun at all on this deck?* Only if yes does the 9-symbol pentagon legibility problem become worth solving.


---

## 13. CAIRN — the compact chain patience *(drafted — rulebook v0.1, sim-validated, awaiting first table test)*

*1 player · ~10 min · 3–4 cairns + a hand of 3 · subset-scalable*

> **Status & origin.** Logged June 2026 to fill a real hole: the collection's two solo games (TWELVE TRIALS, THE ORRERY) are both whole-deck open-information puzzles that **sprawl across the table** — "it sprawls" is a logged handling bug on TWELVE TRIALS, and THE ORRERY spreads four 9-card orbits the same way. There is no *contained* solo game you can play on a train tray. CAIRN targets exactly that gap: all state lives in **≤4 stacks plus a small held hand**. Now **sim-validated** ([cairn_sim.py](Cairn/cairn_sim.py)): structure, hand-vs-reserve, and a realistic-information planning-agent check all done — the 7-sign hand version clears the skill gate. Rulebook drafted (v0.1, [CAIRN_rulebook.md](Cairn/CAIRN_rulebook.md)); next step is a first table test.

**The deck property it exploits.** A card *is* an edge {A,B} of K₉; two cards chain when they share a sign. This **edge-adjacency** property has been unused since OUROBOROS was cut — CAIRN restores it, but in piles rather than one long serpent.

**Core loop.** Shuffle the chosen subset into a face-up **stock**. Deal one card to each of **K cairns** (build piles); you pick which face shows — that sign is the cairn's live **top**. Hold a **hand of H cards** drawn from the stock. On your turn, play one hand card onto a cairn whose top sign matches one of its faces, **placing it to show its other face** — the join is consumed and the onward sign becomes the new top — then refill your hand from the stock. If no hand card can be placed on any cairn → **stuck**, game over. Clear the whole stock and hand to win; score by efficiency (tiers below).

> **Design note — hand beats reserve (sim-backed, see below).** An earlier model used a passive *reserve* (draw one card; buffer it if it won't place). The hand variant tested markedly better: holding 3–4 known cards puts a real decision on *every* turn (which card, which sign to expose) rather than only on lucky multi-fit draws, and it roughly doubles the value of the free peek. The reserve is retained only as a lighter/easier alternative. Footprint stays compact: a held fan plus the cairns is still a train-table layout, and a held hand is freely inspectable in solo play (no hidden-information concern).

**Why it needs this deck — and why it is not OUROBOROS.**
- *Edge-adjacency is load-bearing:* the entire verb is "chain edges by a shared vertex," which only exists because a card is a sign-pair. An ordinary deck can't do it.
- *Counting is the skill:* you know the full deck and which cards remain, so a good player exposes the sign with the most still-to-come partners (the "each sign on 8 cards" registry, used as live planning info).
- *The OUROBOROS handling trap is gone by construction.* OUROBOROS failed because its one live sign was **buried** under the serpent's head as involuntary overhead. Here every sign you ever read is a **visible cairn top or a face-up reserve card**. Nothing is buried; buried cards are committed and never re-consulted ([physical-handling.md](.kiro/steering/physical-handling.md): "only the top matters," no hidden-face memory).
- *Multi-pile branching supplies the agency OUROBOROS's single line lacked:* each draw is a choice of which cairn to feed and which sign to expose.

**Deck-size fit.** Runs on any declared subset (the deck's signature move). **7 signs / 21 cards** is the compact home — a true small footprint and the healthiest measured skill curve (K3/H4 or K4/H3). **9 signs / 36 cards** is a longer, harder expert variant: the sweep shows it needs a *bigger held hand* to stay skill-driven (**9/K3/H5** is the pick — three cairns, hand of 5, train-table footprint intact), because at 9 signs a tight hand becomes a luck trap. Even sign counts work fine here (no Eulerian-loop requirement, unlike OUROBOROS), so the subset is chosen for footprint and difficulty, not parity.

**Sim findings — structural check ([cairn_sim.py](Cairn/cairn_sim.py), seed 20260619).** Four agents on identical deals: random; counting-greedy (no foresight); greedy+peek (uses the **free one-card peek** — the stock's top always shows one face, so you know one face of the next card); and a beam-search ceiling (full clairvoyance = perfect-planner upper bound). Two structures compared — a passive **reserve** buffer vs. an active **hand**. Skill gap on cards-left-unplaced.

*Reserve variant (draw one; R-slot buffer):*

| signs / cairns / reserve | random clear | greedy clear | peek clear | ceiling | peek/random |
|---|---:|---:|---:|---:|---:|
| 7 / 4 / 2 | 48% | 74% | 75% | 100% | 1.86× |
| 7 / 3 / 3 | 48% | 72% | 73% | 100% | 1.64× |
| 9 / 4 / 3 | 23% | 40% | 42% | 98% | 1.33× |

*Hand variant (hold H; choose which to play each turn) — the stronger structure:*

| signs / cairns / hand | random clear | greedy clear | peek clear | ceiling | peek/random |
|---|---:|---:|---:|---:|---:|
| 7 / 3 / 4 | 41% | 71% | 73% | 100% | **2.16×** |
| 7 / 4 / 3 | 43% | 68% | 71% | 99% | **2.03×** |
| 7 / 4 / 4 | 54% | 82% | 82% | 98% | 2.74× *(drifting easy)* |
| 9 / 4 / 4 | 15% | 36% | 40% | 98% | 1.53× |

Reads: (1) **Terminating and clearable** — a planner clears ~98–100% of compact deals, so there's always a reachable target and no stall-forever failure. (2) **The hand is the better engine** — it widens the skill gap (peek/random ~2× at 7 signs vs ~1.6–1.9× for the reserve) by putting a real choice on every turn, and it roughly doubles the value of the peek (you now have options to act on what you see coming). (3) **Sweet spot ≈ K3/H4 or K4/H3** — healthy gap, greedy still only ~70% clear (so planning matters), beam ~99%. K4/H4 drifts toward too-easy (greedy 82%). (4) **9 signs stays the hard, planning-heavy variant** — heuristic clears only ~40%, so it's a stretch/expert mode, not the default. (5) Clearing is the win; since it's reachable, the *score* should reward the **margin of safety** (never getting stuck, a smaller hand, fewer near-misses) rather than bare completion — exact tiers are a tuning question for the rulebook stage.

**Planning-agent check — is the skill *reachable*? (decisive)** Two realistic-information planners (no stock-order peeking) were run against the floor and ceiling: a bounded **expectimax (depth 2)** and a **PIMC determinization** (60 sampled worlds, greedy rollouts). They agreed closely — independent methods converging.

| Config | random | greedy | greedy+peek | expectimax d2 | PIMC 60 | ceiling | room recovered |
|---|---:|---:|---:|---:|---:|---:|---:|
| 7 / K3 / H4 | 41% | 71% | 74% | **98%** | **98%** | 100% | ~87–91% |
| 7 / K4 / H3 | 42% | 68% | 71% | **93%** | **93%** | 100% | ~66–68% |
| 9 / K4 / H4 | 17% | 37% | 41% | **78%** | **77%** | 97% | ~52–62% |

(clear rate; *room recovered* = fraction of the greedy+peek→ceiling gap the planner closes with realistic info.) Conclusions: (a) **At 7 signs the skill is genuine and accessible** — realistic planning recovers ~70–90% of the way to clairvoyance, so the gap is reachable rather than future-knowledge. The OUROBOROS "thin gap / luck-driven" worry is answered. (b) **Shallow planning suffices** — depth-2 expectimax matches 60-world PIMC, so looking ~2 moves ahead with position sense plays near-optimally; not savant-tier. (c) **The learning curve is well-shaped** — random ~41%, casual ~74%, careful ~98% at 7/K3/H4.

**The 9-sign space — grow the hand, not the table.** A dedicated 9-sign sweep (same planners) showed 9/4/4 is a mediocre middle, and the choice of buffer size matters enormously:

| 9-sign config | random | greedy+peek | PIMC | ceiling | recovered | verdict |
|---|---:|---:|---:|---:|---:|---|
| K3 / H4 | 4% | 16% | 43% | 100% | 32% | luck-dominated |
| K4 / H3 | 5% | 15% | 31% | 95% | 18% | luck-dominated (worst) |
| K4 / H4 | 17% | 41% | 77% | 97% | ~55% | mediocre middle |
| **K3 / H5** | 17% | 38% | **87%** | 100% | **74%** | **best — strong curve, 3-pile footprint** |
| K4 / H5 | 30% | 62% | 92% | 95% | ~84% | strong but easier/wider |
| K5 / H4 | 32% | 59% | 92% | 93% | ~70% | strong but wider |
| K5 / H5 | 44% | 71% | 98%* | 92%* | — | drifting too easy |

(*at the easy end the beam ceiling under-estimates — it prunes — so PIMC can exceed it; read those as ≥.) The lesson: **tight hands make 9 signs a luck trap (recovery <35%), and the cure is a bigger held hand, not more cairns** — the hand costs no table space, so the footprint stays tiny while skill becomes reachable. The recommended expert variant is therefore **9/K3/H5** (or 9/K4/H5), not 9/4/4.

**Honest risks / why it might be cut.**
- *Luck — the OUROBOROS ghost (lesson #6): resolved for 7 signs, manageable at 9.* The planning-agent check settled this — realistic-information planning recovers ~70–90% of the way to the clairvoyant ceiling at 7 signs, so the skill is genuine and *reachable*, with a well-shaped curve (random ~41% / casual ~74% / careful ~98%). At 9 signs the residual depends entirely on buffer size: a tight hand is a luck trap (recovery <35%), but **9/K3/H5** restores a strong reachable curve (casual ~38% / careful ~87%). Choose the 9-sign config deliberately; don't ship a tight-hand 9-sign variant.
- *Too-easy drift.* A large hand (K4/H4) pushes greedy to ~82% clear and careful play to near-100% — the decisions thin out. The hand size is a real tuning knob; **K3/H4 or K4/H3** keeps it taut.
- *Is it just OUROBOROS again?* The defence is concrete: visible-top handling and per-turn hand choice fix the two specific failures (buried state, thin agency), and the skill is now sim-shown to be accessible. The table must still confirm the chaining decisions *feel* meaningful rather than mechanical counting — that's a first-table fun question, not a structural one.
- *Scoring needs a fun "win margin."* Since a careful player clears ~98% at 7 signs, bare completion is a weak target for experts; the score must reward margin/elegance (smaller hand, no near-stalls, speed). A rulebook-stage tuning task.

**Evaluation (rubric, [design-principles.md](.kiro/steering/design-principles.md)).** 1. All-pairs: **yes** (cards as edges, chained). 2. Physically works: **yes** — visible tops only, nothing buried. 3. Visible/deducible: **yes** — zero hidden-face memory; counting the remaining deck is the skill. 4. Flipping matters: **yes** — choosing which face to expose is every decision. 5. Pair-uniqueness matters: **moderate** — it powers the counting, though chaining alone needs only "shared sign." 6. Distinct experience: **yes** — the only *contained* solo game, and a draw-driven patience unlike the static open-info ORRERY/TRIALS. 7. Gap-fill: a compact, ~10-min, train-table solo. 8. Clean to explain: **yes** ("match a top, expose the other side, don't jam the reserve"). 9. Testable on Set D today: **yes**. 10. Fastest falsification: a lookahead-bot sim run (does planning beat greedy at 9 signs?), then one solo session to feel whether the choices bite.

**Next step (per [focus-priority.md](.kiro/steering/focus-priority.md)).** The structural check, the hand-vs-reserve comparison, and the planning-agent skill check are all done — and the skill gate is **passed for the 7-sign hand version** (K3/H4 or K4/H3). The **rulebook is drafted** ([CAIRN_rulebook.md](Cairn/CAIRN_rulebook.md), v0.1: 7-sign hand game, with **9/K3/H5** as the labelled "Long Trail" expert variant). The next step is a **first table test** — the fun/feel question (do the chaining decisions land as meaningful, or as arithmetic?) and whether getting blocked reads as fair. Remaining design tuning (exact hand size, scoring presentation) is a playtest-driven question.

---

## The trick-taking siblings — GLEAN & BLIGHT

> **Status (June 2026): promoted to full rulebooks + sim-validated** ([Glean/](Glean/), [Blight/](Blight/)), at the owner's direction, ahead of the usual rung-4 gating below. Both now sit at **tier 2 — sim-validated, awaiting first table test** ([glean_sim.py](Glean/glean_sim.py), [blight_sim.py](Blight/blight_sim.py); skill gaps 1.74×/1.67×/1.49× and 2.02×/1.91×/1.41× at 3/4/6P). See each folder's `_design_analysis.md`.

> **Original status & scope (retained for the record).** These began as **rung-4 new concepts** ([focus-priority.md](.kiro/steering/focus-priority.md)), logged for exploration. Per the circuit breaker they were **not** to be developed into full rulebooks until at least one rung-2/3 game had a first table test. They arose from the THE UNPLAYED PAIR design analysis ([UNPLAYED_PAIR_design_analysis.md](The%20Unplayed%20Pair/UNPLAYED_PAIR_design_analysis.md)), which found that trick-taking and "deduce the missing card" fight each other: certainty arrives only on the final trick, so the call mechanic is structurally dead. The conclusion was to **keep the trick-taking, drop the deduction**, and split the slot into two complementary trick-takers. The missing-card deduction idea is preserved in the Parking Lot below for a future, non-trick-taking game.

> Working titles. **GLEAN** alts: GARNER, HOARD, TITHE, AUGURY. **BLIGHT** alts: PARIAH, MILLSTONE, HEX. Naming is the owner's call; the harvest/rot pairing is the pitch.

### The shared engine (both games)

The deck property both games are built on: **you play a card showing one face and hiding the other, and the hidden face decides the trick at the reveal.** Impossible on a single-faced deck.

- **Deal.** Full 36-card deck, dealt evenly. Clean deals at **3P (12 each), 4P (9), 6P (6)** — the even-divisibility property of 36 ([deck-structure.md](.kiro/steering/deck-structure.md)). 5P plays by setting one card aside face-up (a public "kitty") and dealing 7 each, or via the 7-symbol/21-card subset for a shorter 3P game.
- **Lead.** Play any card, either face up; its shown symbol is the **led symbol**.
- **Follow.** You must play a card carrying the led symbol **on either face**, placed showing the led symbol (flipping a hand card to follow is the signature move — and *which* card you flip away from is information). If void, **slough** any card, any face.
- **Reveal & resolve.** When everyone has played, **flip every card in the trick.** Among the followers (cards showing the led symbol), the one whose **hidden face has the highest pip wins** — ties impossible, because every follower hid a different partner of the led symbol (pair-uniqueness). The winner gathers all cards in the trick face-up into a public won-pile and leads the next trick.

That engine is identical in both games. The *only* difference is what you are trying to do with the cards you capture — and the two goals are exact opposites, which is what makes them siblings rather than duplicates (the TRIGON/TURNCOAT pattern: same architecture, opposite soul).

---

### 11. GLEAN — gather the signs *(the accumulation trick-taker)*

*3–4–6 players · ~20 min · trick-taking / area-majority*

**The goal.** Win tricks to **capture cards**, then win the **per-symbol majorities**. At round end, for each of the 9 symbols, whoever captured the most cards showing it (on *either* face, across their won-pile) scores that symbol's pip value (Moon 1 … Crown 9). Most points wins.

**Why the hidden face is your asset.** You *want* to win tricks, so you commit high hidden pips — but you hold only so many strong cards and following suit constrains you, so the craft is choosing *which* tricks to spend strength on. And because every captured card carries **two** symbols, every capture advances you on two majority races at once; the unique Moon/Crown card is fought over by both the Moon-collectors and the Crown-collectors. Winning worthless tricks doesn't help — you want the tricks rich in the symbols you're contesting, which you steer by choosing what to **lead**.

**Why it needs this deck.** Area-majority over symbols only bites because each card is a *pair* (two majorities per card) and each symbol sits on exactly **8 cards** (knowable scarcity — "most of 8" is countable, and all won-piles are public). On an ordinary deck a captured card would advance one suit, not two, and there'd be no unique contested card.

**First-game variant (simpler scoring).** "Plunder" — each captured card just scores the sum of its two pips; most points wins. Teaches the engine before the majority layer is added.

**Evaluation (rubric).** Deck-necessity: high (two-majorities-per-card + 8-card scarcity). Flipping load-bearing: yes (which face you show = which suit you follow = which hidden pip you commit). Pair-uniqueness: yes (the single contested card decides two majorities). Distinct: the collection's only *building/greedy* trick-taker. Physical handling: clean (public reveal, public won-piles, no hidden-face memory). **Key first questions:** does "highest hidden wins" degenerate into whoever-holds-high-cards, or does the majority + follow constraint create real which-trick-to-win choices? Does counting 9 simultaneous majorities stay trackable at the table, or is the "Plunder" variant the real game?

---

### 12. BLIGHT — dodge the rot *(the avoidance trick-taker)*

*3–4–6 players · ~25 min · trick-taking / evasion (Hearts-lineage)*

**The goal.** Capture as **little poison** as possible. The penalty of a won-pile is the **sum of the hidden-face pips** of every card in it — the strength you couldn't see when the cards were played. Lowest total penalty wins. **Shoot the rot:** capture the poison from *every* trick in the round and you score **0** while everyone else takes the maximum — the classic shoot-the-moon reversal.

**Why the hidden face is your liability.** "Highest hidden pip wins" means the trick winner always eats at least their own high hidden pip — *winning is intrinsically costly*. So you want to **lose** tricks, ducking with just-low-enough hidden pips, and **shed** your high-hidden cards as sloughs into tricks others will win. The Moon/Crown card is the signature trap: it shows a harmless Moon (1) so it ducks easily, but if you get stuck winning, its hidden Crown (9) is a disaster — and as a slough you can hand that 9 to a rival.

**Why it needs this deck.** A shedding/avoidance game where the *unseen* half of the card is the dangerous half cannot exist with single-faced cards. Pair-uniqueness makes the big hidden pips countable (each symbol on 8 cards, all revealed at trick-end), so a sharp player tracks where the poison is — deduction, never memory.

**First-game variant.** "Only Crowns bite" — penalty is just the number of Crown-hidden cards you capture (8 in the deck), like Hearts' simplified "only the Queen" teach. Add full hidden-pip scoring once the dodging rhythm is learned.

**Evaluation (rubric).** Deck-necessity: high (the hidden face *is* the penalty). Flipping load-bearing: yes (choosing which follower = which hidden pip you risk). Pair-uniqueness: yes (countable poison). Distinct: the collection's only *cautious/evasion* game and the only one with a shoot-the-moon gambit. Physical handling: clean. **Key first questions:** does ducking create satisfying agony or just passive low-card-dumping? Is shoot-the-rot achievable often enough to threaten without being a coin-flip? Does eating a surprise hidden 9 feel like a dramatic reckoning or an arbitrary gotcha?

---

### Why these two belong together (and what they cost)

- **Complementarity.** Same engine, opposite goal — you learn the trick rules in one and invert them in the other. GLEAN is positive/greedy (build majorities); BLIGHT is negative/cautious (dodge poison, or shoot the rot). They mirror the TRIGON/TURNCOAT sibling pattern the collection already prizes.
- **Coverage.** They restore the **trick-taking mood** (previously only THE UNPLAYED PAIR), now as two distinct experiences, and they add **6-player trick-taking** (clean 6-each deal) — a player-count the collection is thin on. Partnership modes at 4P/6P exploit even divisibility.
- **The honest cost.** Two trick-takers risk crowding the collection (`product-vision.md` "be willing to cut" overlap). The defence: Hearts and Spades coexist as distinct staples in every card canon precisely because accumulation and avoidance are different games. They must each clear distinctness at the table; if one feels like a re-skin of the other, cut it. The shared engine is a teachability asset, not an excuse to ship both unexamined.
- **Process note.** Both are concept-stage and rung-4-gated. The right next step is **not** to write their rulebooks — it is to first-table an existing rung-2/3 game, then build whichever of GLEAN/BLIGHT the slate still wants. A quick majority/penalty simulation (skill gap, does "highest hidden wins" degenerate in GLEAN) is the cheap structural check before either becomes a rulebook.

---

## Parking Lot

*One-line ideas logged per the [focus-priority.md](.kiro/steering/focus-priority.md) circuit breaker. Not developed until the ladder allows.*

- **Guess-the-missing-card deduction** — the "one card removed unseen, deduce its identity by elimination" mechanic from THE UNPLAYED PAIR. The sim showed it does **not** belong bolted onto trick-taking (certainty arrives only on the last trick). It may work as its *own* game where information arrives faster than one-card-per-trick — e.g. a real-time or simultaneous-reveal deduction race, or a game where players actively probe the hidden card. Saved for a future, non-trick-taking design. (Origin: [UNPLAYED_PAIR_design_analysis.md](The%20Unplayed%20Pair/UNPLAYED_PAIR_design_analysis.md).)
---

## Memory mechanics shelved under the OUROBOROS reading — re-inclusion audit

*Added June 2026. Context: a re-reading of the OUROBOROS post-mortem ([`Ouroboros/OUROBOROS_design_analysis.md`](Ouroboros/OUROBOROS_design_analysis.md), [`COLLECTION_AUDIT.md`](COLLECTION_AUDIT.md) §4) found that OUROBOROS was **not** a memory game — it buried **involuntary** state under the serpent's head, a narrow handling defect. The steering now distinguishes that defect from a **deliberate, verifiable** memory game, which is a legitimate and currently **under-served** deck-native genre ([`design-principles.md`](.kiro/steering/design-principles.md) lesson 1; [`physical-handling.md`](.kiro/steering/physical-handling.md) "Default bias" caveat). This audit lists every game that removed or avoided a memory mechanic citing OUROBOROS, and judges whether the removal was sound or an over-correction worth revisiting.*

| Game | What was removed/avoided | Verdict | Re-include? |
|---|---|---|---|
| **TURNOVER** (ex-HOT POTATO PAIRS) | The **back-memory chain**: a played card's hidden face had to *dodge* the remembered hidden face beneath it — "the unseen half of your card is the dangerous half." Killed and replaced with match-and-turn (all constraints on the visible top). | **Over-correction.** The remembered-backs rule was the game's *deliberate, distinctive core*, not involuntary overhead — exactly the kind of memory the deck suits. It was cut by association with OUROBOROS, not on its own evidence. | **Strong candidate.** |
| **THE UNPLAYED PAIR** | Hidden-face trick-**rank** (winning a trick revealed your card's back, feeding deduction) → converted to a public trick-end reveal; "deduction, never memory." | **Mixed.** The conversion was reasonable, but the game was *parked* for a different reason (trick-layer vs. deduction-layer fight), so the memory question was never tested on its own. | Weak — revisit only if the trick/deduction conflict is solved first. |
| **BLIGHT** | Remembering which face of a captured card was the penalty → store the rot pile **penalty-face-up** as a self-totalling, glanceable record. | **Sound.** The penalty total must be glanceable for scoring; remembering it would be *involuntary* bookkeeping, not a chosen challenge. Correct call — leave as is. | No. |
| **FALSE FACE** | Tracking the full claim history → an **oriented public ledger**; "only remembered state is the newest claim." | **Sound.** It is a deduction/bluff game; forced history-recall would be admin, not play. Correct call. | No. |
| **FACE VALUE** | Hidden-face accrual across rounds → folded cards return to hand **unrevealed**, so "no hidden-face memory accrues." | **Sound.** Memory here would be involuntary overhead riding on a betting shell. Correct call. | No. |

**Conclusion.** Four of the five removals were correct: they stripped *involuntary* memory from games whose point lay elsewhere. **TURNOVER is the exception** — its back-memory chain was a deliberate, deck-native memory mechanic discarded by guilt-by-association with OUROBOROS, before it was ever table-tested. It is the prime re-inclusion candidate.

### Re-inclusion candidates

- **TURNOVER's back-memory chain — revive as a deliberate memory game or variant.** Keep the match-and-turn base game (it stands on its own), but restore the remembered-hidden-faces rule as either (a) a **"Long Memory" expert variant** of TURNOVER, or (b) a **distinct shedding/memory game** where the whole point is tracking the pile's buried faces. Must pass the steering's memory guardrails: the memory is *the point*, the load is roughly **symmetric** across players, and it is **verifiable on demand** (the pile can be checked at a challenge, bounded by the every-pair-once registry so sharks *count* rather than merely recall). First question to falsify: is dodging a remembered back *tense and fair*, or just a punishing recall tax at speed?
- **A purpose-built deliberate memory game (new).** The collection has deduction games but no game whose *core challenge* is tracking pressed faces over time. The pair-registry (every pair once, each symbol on 8 cards) bounds what is knowable, turning memory into disciplined counting. Logged as an explicit design target per the updated steering; a concept sheet can be drafted on request.


---

## 14. MERIDIAN — race the nine roads *(concept stage — not yet a rulebook)*

*2–4 players · ~20–25 min · network route-race / drafting · **deck-only, no extra components** · working title (alts: LODESTAR, CONFLUENCE, KEYSTONE, RELAY)*

> **Why this exists.** A clean-sheet **networking game for 2–4 players**, designed to dodge the four bugs that dog CROSSROADS at the table (see [Crossroads/CROSSROADS_design_analysis.md](Crossroads/CROSSROADS_design_analysis.md) §6–§8): 14-card hand overwhelm, the invisible road-vs-contract mental split, the pass-to-win/hoarding exploit, and first-turn paralysis. It is **not** trying to be un-CROSSROADS-like — it reuses the proven "aim the card at a sign / visible face = destination" handling — it is trying to be **un-CROSSROADS-*broken***. Each bug is designed out structurally.
>
> **Component discipline — resolved by simulation.** Two forks were considered: a deck-only **goal-race** (positional ownership) and a **node-majority** version needing a colour-coded cube kit. A structural sim ([Meridian/MERIDIAN_design_analysis.md](Meridian/MERIDIAN_design_analysis.md), [meridian_sim.py](Meridian/meridian_sim.py)) settled it: the **goal-race wins decisively**, including on flip-relevance — the very axis the node-majority fork was supposed to win. So MERIDIAN is **deck-only**; the cube-kit fork is dropped. (Details and the reversed prediction in the design analysis; the alternatives note at the end is retained for the record.)

**The one-sentence deck property.** Every card is simultaneously a **directed road** (to build) and a **unique connection goal** (to claim); because every pair exists once, each goal is the *only* connection between its two signs and the direct road for it is a single scarce card, while a **flip** re-aims a road to make or break the directed route a goal demands.

### Core loop

The nine signs are nine **nodes** (a node simply *is* where roads meet — no node cards). One **communal web** of directed roads is built in the middle; nobody owns roads.

Setup (per the subset table below): separate the chosen subset into a face-up **goal row** of 3 cards, a **stock**, and starting **hands of 3**; the stock feeds a face-up **market** of 3.

Each goal card is laid showing one face — that sign is the goal's **destination** ("reach Crown from Moon"), reusing CROSSROADS's visible-face-is-destination convention.

On your turn:
1. **Draft** — take one card from the face-up market into hand; refill the market from the stock.
2. **Build** — play one road from hand into the communal web, joined at a sign it shares with the web, **aimed at one of its two signs** (traffic flows toward the visible face).
3. **Re-aim** *(optional)* — flip one existing road to swing its direction.

**Claim.** The instant your build or flip makes a **directed route exist into a goal's destination from its other sign**, you take that goal card into your face-up **score pile** and a new goal is revealed. Only the active player claims, and a flip that completes a route claims too — so re-aiming scores directly.

**End & scoring.** The game ends when the stock and market are empty and hands are built out (or the goal deck runs dry). Score = **pip-sum of your claimed goals**. Most wins; tiebreak = most goals.

### How each CROSSROADS bug is designed out

| CROSSROADS bug | MERIDIAN's structural fix |
|---|---|
| **14-card overwhelm** | Hand is **3**, fed by an open draft — never a wall of cards. |
| **Invisible road/contract split** | Hand cards have **one role** — build them. Goals are **public cards** you claim into a pile, never hand cards you secretly nurse. No mental partition. |
| **Pass-to-win / hoarding** | You score **only** by claiming goals, and **only the active player who completes a route claims**. A passer completes nothing, claims nothing, scores zero. The exploit cannot exist. |
| **First-turn paralysis** | The **public goal row** is an explicit target from turn one — you build *toward named connections*, not into a blank canvas. The market further narrows the choice. |
| **Face-up draw-pile handling** (the trap that sank the CROSSROADS draw idea, §8) | The market and goal row are **face-up by design** — the no-card-back property becomes a *feature*, not a problem. |
| **Extra components** | **None.** Goals and score piles are the deck's own cards; ownership is positional. |

### Why it needs this deck

- **Every pair exactly once** → each goal is the *unique* connection between its two signs, and the single direct road for it is one scarce card. Where that card sits — unbuilt in the stock, in a hand, already built (and aimed which way?), or itself a goal — is live, knowable, deck-native tension. Generic components give no such uniqueness.
- **Each sign on exactly 8 cards** → the map's degree at every node is bounded and countable, so route possibilities are finite and readable rather than open-ended.
- **Flipping swaps the active sign** → re-aiming a road makes or breaks a *directed* route, which is the difference between claiming a goal and not. A flip that completes a route scores immediately; a flip can also strand the route a rival is building toward. This is the deck's signature action doing load-bearing, **visible** work (rubric #4), never buried.
- **The deck generates its own state** → the web, the goals, the market, and the score piles are all just cards. Nothing else is needed.

### Built for 2–4 via the subset property

Player count scales by **declared symbol range**, so per-player card-flow and route density stay roughly constant ([deck-structure.md](.kiro/steering/deck-structure.md) subset property):

| Players | Signs | Cards | Node degree (max roads/sign) |
|---:|---:|---:|---:|
| 2 | 7 | 21 | 6 |
| 3 | 8 | 28 | 7 |
| 4 | 9 | 36 | 8 |

Adding a player adds a sign (another node and destination) and its cards (more roads and goals), so the map grows with the table. The *same* game, retuned by the deck's own subset structure rather than by bolted-on rules — the load-bearing answer to "designed for 2–4."

### Honest evaluation (rubric, [design-principles.md](.kiro/steering/design-principles.md))

1. Exploits all-pairs: **yes** (unique goal + unique direct road + 8-card degree bound). 2. Physically works: **yes** — communal web, aimed roads, face-up goals/market/score piles, **no markers, nothing hidden**. 3. Visible/deducible: **yes** — zero hidden-face memory; the whole web is public. 4. **Flipping matters: yes** — re-aiming makes/breaks directed routes and can claim a goal outright (though see the flip-centrality risk). 5. Pair-uniqueness matters: **yes** — each goal and its direct road are singular. 6. Distinct: **yes** — the collection's only *shared-map route-race*; the move to claimed goals (not per-sign majorities) clears the earlier GLEAN overlap. 7. Gap-fill: a 2–4P tactical networking game, deck-only, ~20 min. 8. Clean to explain: **yes** ("draft a card, build a road toward a sign, connect the goals before your rivals"). 9. Testable on Set D today: **yes** (deck only). 10. Fastest falsification: a structural sim (below), then one 2P and one 3P session.

### Risks / why it might be cut

- **Flip-centrality (the main rubric-4 risk).** With instant claim, players may mostly just build toward goals and rarely re-aim, leaving flipping under-used — the opposite of the marker version where re-aiming was the whole game. Mitigations to test: goals that *require* a specific direction (already the design), and/or letting a flip deny a route between an opponent's turns. If flipping turns out inert in practice, this drifts toward a generic connection-race and the deck-tie weakens — a sim/table question.
- **CROSSROADS proximity.** Directed roads + connect-two-signs scoring is CROSSROADS's DNA. The differentiators are real (communal unowned web, public claimed goals, a draft, 2–4P, action-rewarded rather than denial-duel), and the designer has accepted similarity — but if it plays like "CROSSROADS with extra players," fold it back into CROSSROADS instead of shipping both.
- **Goal-rush / low interaction.** If goals fall too easily, the game becomes a parallel solitaire race with little contention. Goal count, hand size, and how connected the early web gets are the tuning knobs.
- **Route-tracing burden.** Directed reachability must stay glanceable on a communal web; small subsets (7–8 signs) help, but this is CROSSROADS's old legibility question and needs the layout work.
- **Dryness.** "Connect the pairs" can feel flat without the denial tension; the scarce-unique-road and re-aim levers are the bets that give it teeth.

### Next step (per [focus-priority.md](.kiro/steering/focus-priority.md))

**Structural sim done — goal-race passes the gate** ([MERIDIAN_design_analysis.md](Meridian/MERIDIAN_design_analysis.md)): terminates at 2–4P (0% caps), skill gap 1.9× / 2.8× / 3.6× (2/3/4P), pass-to-win scores 0 by construction, and flips are relevant (~22–28% of claims come via a re-aim; removing flips drops the skill gap). Now **Stage 2 (validated)**. The remaining work is a short **deck-only rulebook draft**, then a first **2P + 3P table test** for the fun, interaction, route-tracing legibility, and CROSSROADS-distinctness questions a sim can't answer.


### Alternative fork — node-majority (shared cube kit) — *dropped by sim*

*Retained for the record. This fork was the reason the cube-kit component question arose; the [structural sim](Meridian/MERIDIAN_design_analysis.md) rejected it in favour of the deck-only goal-race.*

Same draft-and-build skeleton, but the web is **owned**: when you build a road you drop one of your colour cubes on it and aim it at one of its two signs (one **vote**). At game end, each sign is controlled by whoever has the most votes aimed at it; controlling a sign scores its pip. **Flipping re-aims a vote** — steal a node, deny a leader — which makes re-aiming the central, point-scoring verb rather than an occasional tool.

| | Goal-race (deck-only) | Node-majority (cube kit) |
|---|---|---|
| Components | deck only | + colour-coded cubes (must be a shared, reused kit) |
| Flip-centrality | risk: may be under-used | **strong — re-aiming is the game** |
| GLEAN overlap | cleared | present (per-sign pip majority) |
| Pass-to-win | dead (claim by completing) | dead (control needs built votes) |
| Kingmaking risk | low | **higher** (a re-aim can decide a node — test at 3–4P) |

**Decision rule:** if the goal-race sim shows flips rarely matter (rubric-4 fails), the node-majority fork is the fix — provided the collection is willing to adopt a reusable cube kit and the GLEAN-overlap and kingmaking questions pass at the table. If the goal-race keeps flips relevant on its own, prefer it (no kit, no overlap).

*(Update to the Next step: the structural sim should run **both** forks and report claims/points attributable to flips, so the fork choice is made on data, not taste.)*