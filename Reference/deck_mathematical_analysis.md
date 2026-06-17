# Mathematical Analysis of the Flip Deck

## Executive Summary

The deck is best understood as a physical model of the complete graph **K₉**:

- **Symbols are vertices.**
- **Cards are edges.**
- **Each card joins exactly two symbols.**
- **Flipping a card changes which endpoint is currently visible.**

With 9 symbols, the full deck contains:

```math
C(9,2) = 36
```

cards, with every possible pair appearing exactly once. This gives the deck several overlapping mathematical identities:

| Mathematical object | Deck interpretation | Design use |
|---|---|---|
| Complete graph K₉ | Every pair of symbols exists once | Networks, routes, contracts, pair deduction |
| 2-(9,2,1) block design | Every pair is a unique card | Exact claims, exact lies, exact eliminations |
| Reversible edge set | Each card can show either endpoint | Flips as movement, betrayal, voting, reversal |
| Line graph L(K₉) | Cards are adjacent if they share a symbol | Chain games, hand texture, compatibility |
| Tournament orientation | A full face-up state orients every pair | Elections, dominance, pairwise contests |
| Steiner triple substrate | Cards can be grouped into symbol triangles | Almanacs, rituals, gates, trio puzzles |
| Eulerian graph | All cards can form a closed trail | Serpents, tours, route puzzles |

The important correction is that the deck itself is **not** a Steiner triple system. It is the **pair layer underneath** one. A Steiner triple system on 9 symbols is a way of grouping the 36 pair-cards into 12 symbol-triangles so every card is used exactly once.

The current collection already makes strong use of pair uniqueness, flipping, triangle closure, and some graph structure. The most promising underused structures are:

1. **Tournament orientations** — every visible deck state is a complete set of pairwise results.
2. **Matchings** — sets of non-overlapping cards with no repeated symbols.
3. **Graph cuts** — cards crossing between symbol factions.
4. **Resolvable Steiner systems** — the 36 cards partitioned into four rounds of three disjoint triangles.
5. **7-symbol balance** — in K₇, each card has exactly as many compatible as incompatible partners.

---

# 1. The Deck as K₉

Let the symbol set be:

```math
V = {1,2,3,4,5,6,7,8,9}
```

Every card is an unordered pair:

```math
{i,j}, i ≠ j
```

So the card set is:

```math
E = C(V,2)
```

This is exactly the edge set of the complete graph **K₉**.

## Basic Counts

| Quantity | Formula | Value |
|---|---:|---:|
| Symbols | n | 9 |
| Cards | C(9,2) | 36 |
| Cards touching each symbol | n - 1 | 8 |
| Possible symbol-triangles | C(9,3) | 84 |
| Possible 4-symbol complete subgraphs | C(9,4) | 126 |
| Maximum matching size | floor(9/2) | 4 |
| Edges in a full K₉ orientation | C(9,2) | 36 |

Each symbol appears on exactly 8 cards. This is one of the simplest but most useful facts in the deck. It supports counting, deduction, exhaustion, and symbol-based ownership.

---

# 2. Sub-Deck Sizes: Why 6, 7, 8, and 9 Symbols Feel Different

Any n-symbol subset gives the complete graph Kₙ.

| Symbols | Cards | Degree per symbol | Possible triangles | Mathematical character | Design feel |
|---:|---:|---:|---:|---|---|
| 6 | 15 | 5 | 20 | Small, non-Eulerian, no Steiner triple decomposition | Microgame-friendly, but less symmetrical |
| 7 | 21 | 6 | 35 | Fano-plane-compatible; Eulerian | Excellent medium size for deduction and puzzles |
| 8 | 28 | 7 | 56 | Natural even network; no Euler circuit | Great for route/road games and 2-player splits |
| 9 | 36 | 8 | 84 | Full system; STS(9), Eulerian, maximum richness | Best master deck, but heaviest for ability games |

## Design Implication

The full 36-card deck is valuable as the **master system**, but not every game should use all 36 cards.

- **6 symbols / 15 cards:** compact microgames.
- **7 symbols / 21 cards:** deduction, co-op, and puzzle games.
- **8 symbols / 28 cards:** clean 2-player splits, route games, matchings.
- **9 symbols / 36 cards:** flagship games, deep puzzles, full mathematical structure.

This suggests the product should remain a 9-symbol master deck, while individual games should freely specify smaller sub-decks when that produces better play.

---

# 3. Pair Uniqueness: The Deck’s Strongest General-Purpose Property

Every pair exists exactly once. This turns the deck into a public registry of possible facts.

If a card shows symbol A, its hidden face is initially one of 8 possible partners:

```math
A/B, A/C, A/D, ...
```

As cards become known, those possibilities shrink.

```math
Live hidden options for shown A = 8 - known eliminated A-pairs
```

Known eliminations can come from:

- cards in your own hand,
- public registry cards,
- discarded/archive cards,
- revealed challenges,
- score piles,
- cards already known from previous play,
- locked sets or completed objectives.

## Current Uses

| Game | Use of pair uniqueness |
|---|---|
| FALSE FACE | Claims name exact hidden pairs; lies become countable |
| FACE VALUE | Shown face creates a range of possible hidden strengths |
| JANUS | One legal hint can fully identify a card to its holder |
| THE UNPLAYED PAIR | Players deduce the one missing card |
| CROSSROADS | Full hand inference from complementary road sets |

## Design Potential

Pair uniqueness is ideal for games involving:

| Mechanic | Use |
|---|---|
| Bluffing | Lie about a specific physical card, not a vague category |
| Deduction | Eliminate possible hidden partners |
| Betting | Visible face defines a calculable hidden range |
| Co-op hinting | One clue can collapse uncertainty |
| Murder-mystery logic | “The only remaining Sun/Key must be…” |
| Auctions | Bid on a card whose hidden partner has a shrinking range |
| Social accusation | Claims can be mathematically disproven |

## Design Warning

Pair deduction is already heavily represented in the collection. It is one of the deck’s strongest identities, but new games should avoid becoming yet another version of:

> “Claim a hidden face; others count whether it is possible.”

Future games should combine pair uniqueness with less-used structures such as matchings, cuts, or tournaments.

---

# 4. The Deck as a Network

Because cards are edges, the deck naturally supports route, map, and connectivity games.

## Graph Concepts Available

| Graph concept | Deck meaning | Game use |
|---|---|---|
| Edge | Card | Road, relationship, contract, conflict |
| Vertex | Symbol | City, faction, candidate, guild |
| Path | Sequence of cards sharing endpoints | Route, chain, journey |
| Cycle | Closed route | Serpent, loop, ritual circuit |
| Cut | Cards crossing between symbol groups | War fronts, trade routes, border conflicts |
| Degree | Number of visible/touching cards | Influence, exhaustion, control |
| Connected component | Isolated symbol group | Territory, network completion |
| Orientation | Which face is visible | Direction, winner, loyalty, vote |

## Current Use: CROSSROADS

CROSSROADS is the clearest current network game. It removes one symbol and uses the remaining 28 cards as the roads of K₈. The eight cards involving the removed ninth symbol become city markers. Each road is one-way depending on which face is visible.

This is structurally strong because K₈ has 28 edges, which divides perfectly between two players as 14 cards each.

## Underused Area: Graph Cuts

A **cut** partitions the symbols into two groups and looks at all cards crossing between them.

For K₉, the number of cross-faction cards is:

```math
k(9-k)
```

| Partition | Cross-faction cards |
|---|---:|
| 1 vs 8 | 8 |
| 2 vs 7 | 14 |
| 3 vs 6 | 18 |
| 4 vs 5 | 20 |
| 3 vs 3 vs 3 | 27 between factions, 9 internal |

## Game Design Direction: Faction-Cut Game

A game could divide symbols into factions. Cards within a faction are domestic resources; cards between factions are conflicts, treaties, trade routes, or spies.

The interesting twist is that factions could change during play. Moving one symbol from one faction to another instantly reclassifies many cards.

Possible theme:

> Nine houses form unstable alliances. Every card is either an internal asset or a border dispute depending on the current political map.

This would use a genuinely graph-theoretic property that the current collection has not yet fully explored.

---

# 5. Line Graph Structure: Cards That Touch Cards

The line graph **L(K₉)** treats cards as the objects and connects two cards if they share a symbol.

For the 36-card deck:

- Each card shares a symbol with 14 other cards.
- Each card is disjoint from 21 other cards.
- The line graph is strongly regular with parameters:

```math
(36, 14, 7, 4)
```

Meaning:

| Parameter | Meaning |
|---|---|
| 36 | There are 36 card-vertices |
| 14 | Each card is adjacent to 14 cards sharing a symbol |
| 7 | Two adjacent cards have 7 common neighbours |
| 4 | Two disjoint cards have 4 common neighbours |

## Why This Matters

Many possible games are not really about symbols. They are about **card compatibility**:

- Can this card follow that card?
- Can these two cards coexist?
- Can I build a chain?
- Can I form a set where every card touches every other?
- Can I form a set where no card touches another?

## Compatibility Counts by Sub-Deck

| Symbols | Cards | Cards sharing a symbol with any given card | Cards disjoint from it |
|---:|---:|---:|---:|
| 6 | 15 | 8 | 6 |
| 7 | 21 | 10 | 10 |
| 8 | 28 | 12 | 15 |
| 9 | 36 | 14 | 21 |

The 7-symbol deck is especially interesting because each card has:

- 10 compatible cards,
- 10 incompatible cards.

That makes K₇ unusually balanced for games where “share a symbol” and “avoid sharing a symbol” are opposing forces.

## Current Use: TURNOVER

TURNOVER is a simple walk through this compatibility structure. The current target symbol asks for any card incident to that symbol. When the card is played and turned over, its other symbol becomes the next target.

Every card in hand is therefore an “exit door” from the current symbol to one specific other symbol.

## Design Directions

| Structure | Possible game use |
|---|---|
| Chains of adjacent cards | Domino-like shedding, racing, route-building |
| Pairwise adjacent sets | Conspiracies, cliques, symbol clusters |
| Pairwise disjoint sets | Clean contracts, independent missions |
| Alternating adjacent/disjoint cards | Pattern puzzles |
| K₇ equal compatibility | Balanced tactical duel or co-op puzzle |

---

# 6. Stars, Triangles, and Matchings

There are three especially important local structures in the deck.

## 6.1 Stars: All Cards Touching One Symbol

A symbol-star consists of all cards containing a given symbol.

In the full 9-symbol deck, each star has 8 cards:

```math
{A/1, A/2, ..., A/9} minus {A/A}
```

Stars support:

- symbol ownership,
- guilds or factions,
- counting exhaustion,
- majority control,
- “all cards touching X” effects,
- target matching,
- suits without suits.

This is the most intuitive structure for players. They do not need graph theory to understand that “every symbol appears on eight cards.”

## 6.2 Triangles: Three Symbols, Three Cards

A symbol triangle on A, B, C consists of:

- A/B,
- A/C,
- B/C.

There are:

```math
C(9,3) = 84
```

possible triangles in the full deck.

The key property is **closure**:

> Any two cards in a triangle imply the third.

For example:

- A/B and A/C imply B/C.
- A/B and B/C imply A/C.
- A/C and B/C imply A/B.

## Current Use: JANUS

JANUS uses this elegantly. A keystone A/B needs two pillars A/X and B/X. Together, the three cards form the triangle A, B, X.

## Design Directions

| Triangle property | Design use |
|---|---|
| Two cards imply the third | Deduction, contracts, missing-piece puzzles |
| Triangle uses 3 cards and 3 symbols | Gates, rituals, recipes, alliances |
| Triangle closure can be blocked | Denial games, hostage cards |
| Each card lies in 7 triangles | Multi-use objectives |
| Triangles can partition the deck | Scenario books, almanacs, campaign puzzles |

## 6.3 Matchings: Cards With No Shared Symbols

A matching is a set of cards where no two cards share a symbol.

In K₉:

- maximum matching size is 4 cards,
- one symbol is always left unused.

In K₈:

- a perfect matching has 4 cards,
- all 8 symbols are used exactly once.

This is a powerful structure for simultaneous-play games because a matching creates clean, non-overlapping contests.

## Round-Robin Structure in K₈

K₈ can be decomposed into 7 perfect matchings. This is the same structure as a round-robin tournament with 8 teams:

- 8 symbols,
- 7 rounds,
- 4 pairwise matchups per round,
- every pair meets exactly once.

## Design Direction: Matching-Round Game

Possible concept:

> Use 8 symbols as teams, candidates, gods, or houses. Each round reveals four non-overlapping pair contests. Players secretly influence, bet on, or manipulate outcomes. Across 7 rounds, every possible pair occurs exactly once.

This is one of the most promising unused structures because the rule is easy to explain:

> “No symbol appears twice this round.”

---

# 7. Steiner Triple Systems

A Steiner triple system STS(n) is a collection of 3-symbol blocks such that every pair of symbols appears in exactly one block.

Because the deck consists of pair-cards, an STS(9) is exactly:

> a way to partition all 36 cards into 12 perfect symbol-triangles.

Each triple uses 3 symbols and therefore 3 cards. Twelve triples use:

```math
12 × 3 = 36
```

cards.

## Existence by Sub-Deck Size

A Steiner triple system STS(n) exists exactly when:

```math
n ≡ 1 or 3 mod 6
```

For relevant deck sizes:

| Symbols | STS exists? | Cards | Triangles in full decomposition | Notes |
|---:|---|---:|---:|---|
| 6 | No | 15 | — | Cannot partition into triples |
| 7 | Yes | 21 | 7 | Fano plane |
| 8 | No | 28 | — | Cannot partition into triples |
| 9 | Yes | 36 | 12 | Affine plane of order 3 |

## STS(7): The Fano Plane

The 7-symbol deck supports the Fano plane:

- 7 symbols,
- 7 triples,
- 21 cards,
- every pair appears in exactly one triple.

This is excellent for compact puzzle and deduction games.

## STS(9): The Affine Plane of Order 3

The 9-symbol deck supports Steiner triple systems with:

- 9 symbols,
- 12 triples,
- 36 cards,
- every pair-card used exactly once.

There are 840 labelled STS(9) systems. In the current collection, TWELVE TRIALS uses these as “almanacs”: different ways to sort the whole deck into 12 perfect symbol-trios.

## Resolvable Structure

STS(9) has an extra property: its 12 triples can be grouped into 4 parallel classes.

Each parallel class contains:

- 3 disjoint triples,
- covering all 9 symbols exactly once.

So an STS(9) can be viewed as:

| Level | Structure |
|---|---|
| Full almanac | 12 triangles covering all 36 cards |
| Parallel class | 3 disjoint triangles covering all 9 symbols |
| Triangle | 3 symbols and 3 pair-cards |

## Design Direction: Four-Season Almanac Game

Possible concept:

> Reveal or construct one almanac. The game has four rounds. Each round scores one parallel class: three disjoint symbol-triangles covering all nine symbols. Players compete to control, complete, corrupt, or predict those triangles.

This uses the deepest structure of the deck, but in a form players can see one round at a time.

## Design Warning

Steiner systems are mathematically beautiful but can be invisible. If players need to constantly consult a reference chart, the structure becomes admin rather than play.

Best uses:

- solo puzzles,
- co-op puzzles,
- scenario cards,
- one revealed almanac at a time,
- round-based objectives,
- hidden campaign logic.

Worst uses:

- making players memorise 12 arbitrary triples,
- asking casual players to understand STS theory,
- competitive games where the scoring map is not visible.

---

# 8. Eulerian Circuits and Trails

A graph has an Eulerian circuit if every edge can be traversed exactly once in a closed loop.

Kₙ is Eulerian when every vertex has even degree. Since K₉ has degree 8 at every symbol, K₉ is Eulerian.

So the full 36-card deck can always be arranged as a closed chain where consecutive cards share a symbol and every card is used exactly once.

## Relevant Sub-Decks

| Symbols | Degree | Eulerian? | Meaning |
|---:|---:|---|---|
| 6 | 5 | No | Cannot make one closed all-card trail |
| 7 | 6 | Yes | 21-card closed trail possible |
| 8 | 7 | No | Needs multiple trails or open trails |
| 9 | 8 | Yes | 36-card closed trail possible |

## Game Uses

| Eulerian property | Game use |
|---|---|
| All cards can form one closed loop | Serpent, pilgrimage, circuit puzzle |
| Every card used exactly once | Full-deck challenge |
| Consecutive cards share symbols | Domino-style tableau |
| 7 and 9 symbols are Eulerian | Natural puzzle sizes |
| 6 and 8 are not Eulerian | Built-in need for breaks, scars, or multiple routes |

## Lesson from OUROBOROS

The Eulerian structure is strong, but hidden-face memory can make it physically awkward. A constantly important state must be visible. If players must repeatedly remember an open symbol hidden under a card, the math may be elegant but the table experience suffers.

Better implementations:

- open-information trail puzzle,
- visible endpoint markers,
- shared co-op planning,
- route cards with explicit orientation,
- multiple visible trails rather than one hidden-state serpent.

---

# 9. Tournament Orientations: The Most Underused Structure

If every card has one visible face, then every pair of symbols has a visible winner.

That is a **tournament** on 9 vertices:

- each symbol is a competitor,
- each card is a pairwise contest,
- the visible face is the winner,
- the hidden face is the loser.

A full face-up state of the deck gives 36 pairwise results.

## Possible Interpretations

| Visible face means… | Theme |
|---|---|
| This candidate beats the hidden candidate | Election / debate |
| This faction dominates the hidden faction | War / influence |
| This city receives traffic from the hidden city | Route network |
| This guild currently controls the agent | Allegiance |
| This god receives tribute | Mythic economy |
| This argument defeats the other | Courtroom / philosophy duel |

## Mathematical Features

For each symbol, count its visible wins:

```math
score(A) = number of cards involving A that show A
```

Each symbol’s score is between 0 and 8.

Across all symbols:

```math
sum(scores) = 36
```

A symbol with score 8 is a **Condorcet winner**: it beats every other symbol pairwise.

Cycles can occur:

```math
A > B, B > C, C > A
```

These are majority-cycle-like structures, familiar from voting theory.

## Design Direction: CONDORCET

Possible concept:

> Nine candidates compete in every pairwise matchup. Players flip cards to make their backed candidate win contests. A candidate scores by out-degree, but bonus objectives reward creating or breaking 3-cycles.

This would use the deck in a way that is highly distinctive and currently underrepresented.

## Why This Is Promising

The deck literally contains every pairwise contest. That is rare and elegant.

A tournament game could support:

- hidden candidate loyalties,
- public manipulation,
- agenda control,
- kingmaking,
- cycle bonuses,
- majority paradoxes,
- “make X beat Y, but not too obviously” objectives.

This is probably the most important unexplored mathematical design space.

---

# 10. Pips and Ordered-Symbol Structure

If the 9 symbols also have pip values 1–9, then every card gains numerical properties:

- lower endpoint,
- higher endpoint,
- sum,
- difference,
- average,
- hidden value range.

## Difference Distribution

The number of cards with difference d is:

```math
9 - d
```

| Difference | Number of cards |
|---:|---:|
| 1 | 8 |
| 2 | 7 |
| 3 | 6 |
| 4 | 5 |
| 5 | 4 |
| 6 | 3 |
| 7 | 2 |
| 8 | 1 |

The pair 1/9 is the unique maximum-gap card. Adjacent pairs are common.

## Sum Distribution

| Sum | Number of cards |
|---:|---:|
| 3 | 1 |
| 4 | 1 |
| 5 | 2 |
| 6 | 2 |
| 7 | 3 |
| 8 | 3 |
| 9 | 4 |
| 10 | 4 |
| 11 | 4 |
| 12 | 4 |
| 13 | 3 |
| 14 | 3 |
| 15 | 2 |
| 16 | 2 |
| 17 | 1 |

Middle sums are common; extreme sums are rare.

## Design Uses

| Numerical feature | Game use |
|---|---|
| Higher pip | Strength, rank, authority |
| Lower pip | Stability, foundation, cost |
| Sum | Resource value, contract value, pot size |
| Difference | Volatility, damage, distance, risk |
| Adjacent pair | Safe/common card |
| Extreme pair | Rare powerful card |
| Hidden pip | Bluffing strength |

## Design Warning

Pips break symbol symmetry. That can be useful, but it can also overload games where symbols already have unique powers.

Avoid combining all three unless necessary:

1. unique symbol powers,
2. pip arithmetic,
3. hidden-face deduction.

That risks turning an elegant deck into a bookkeeping exercise.

---

# 11. Automorphism and Balance

Without pips, powers, colours, or special roles, the deck has full symbol symmetry. Any relabelling of the 9 symbols preserves the structure.

Mathematically, the automorphism group is:

```math
S₉
```

This means the raw deck is extremely balanced.

But symmetry is broken when you assign:

- symbol abilities,
- pip values,
- wild symbols,
- player factions,
- fixed board positions,
- thematic roles,
- special scoring rules.

## Design Principle

> Use the deck’s symmetry for fairness, then break it deliberately for personality.

The deck gives you a fair mathematical substrate. The design work is deciding where asymmetry is worth the learning cost.

In particular, 9 unique symbol abilities should not be the default for every game. They work for flagship tactical games, but many future games should use the structure of the deck rather than assigning a rule to every symbol.

---

# 12. Existing Coverage in the Collection

The current collection already covers many of the strongest structures.

| Structure | Current games using it |
|---|---|
| Flipping as the core action | TURNOVER, CROSSROADS, TWELVE TRIALS |
| Flipping as defection or denial | TURNCOAT, THE COUNCIL |
| Pair uniqueness as deduction | JANUS, THE UNPLAYED PAIR, FALSE FACE, CROSSROADS, FACE VALUE |
| Triangle closure | JANUS, TWELVE TRIALS |
| Steiner systems | TWELVE TRIALS |
| Network graph | CROSSROADS |
| Symbol abilities | SYZYGY, TURNCOAT |
| Hidden information | JANUS, FALSE FACE, FACE VALUE, THE UNPLAYED PAIR |
| Open information | CROSSROADS, TWELVE TRIALS |
| Social negotiation | THE COUNCIL, FALSE FACE |

## What Is Saturated

The following areas are already well represented:

- hidden-face deduction,
- exact pair claims,
- bluffing about hidden symbols,
- tactical grid play,
- flipping as betrayal,
- triangle-based gates/puzzles.

These can still produce more games, but they are no longer the most distinctive new territory.

## What Is Underused

The most underused structures are:

1. **Tournament orientation** — all pairwise contests visible at once.
2. **Matchings** — non-overlapping simultaneous contests.
3. **Graph cuts** — faction borders and alliance shifts.
4. **Resolvable STS(9)** — four parallel classes of three triangles.
5. **K₇ compatibility balance** — each card has equal share/disjoint options.

---

# 13. Promising New Game Directions

## 13.1 Pairwise Election Game

### Structure Used

Tournament orientation of K₉.

### Core Idea

Each card is a contest between two symbols. The visible face is the current winner. Players flip cards to manipulate pairwise results.

### Possible Scoring

- Back one secret candidate.
- Score by that candidate’s out-degree.
- Bonus for creating a Condorcet winner.
- Bonus for creating or breaking cycles.
- Public polls reveal partial standings.

### Why It Is Promising

The deck literally contains every pairwise matchup. This is too natural not to explore.

## 13.2 Matching-Round Tournament Game

### Structure Used

Perfect matchings in K₈.

### Core Idea

Use 8 symbols. Each round has four pairwise contests with no repeated symbols. Across seven rounds, every pair occurs exactly once.

### Possible Themes

- sports league,
- gladiator arena,
- debating tournament,
- gods duelling,
- faction war,
- magical trials.

### Possible Mechanics

- bet on winners,
- secretly boost one symbol,
- flip contests,
- draft sponsors,
- predict final standings.

### Why It Is Promising

“No symbol appears twice this round” is simple, physical, and mathematically clean.

## 13.3 Faction-Cut Negotiation Game

### Structure Used

Graph cuts in K₉.

### Core Idea

Symbols belong to shifting factions. Cards crossing faction boundaries are conflicts or trade routes. Cards within factions are internal resources.

### Possible Mechanics

- vote to move symbols between factions,
- score border cards,
- manipulate alliances,
- profit from war or peace,
- secretly back a faction configuration.

### Why It Is Promising

It uses the complete graph globally rather than focusing on individual hidden pairs.

## 13.4 Resolvable Almanac Game

### Structure Used

STS(9) with four parallel classes.

### Core Idea

One almanac partitions the deck into 12 triangles. These are grouped into 4 rounds of 3 disjoint triangles.

### Possible Mechanics

- each round reveals one parallel class,
- players complete or corrupt triangles,
- control the most cards in a triangle,
- predict which triangle will score,
- use off-class cards as interference.

### Why It Is Promising

It makes the deepest math visible in manageable chunks.

## 13.5 K₇ Compatibility Duel

### Structure Used

In K₇, each card has 10 sharing partners and 10 disjoint partners.

### Core Idea

A 21-card duel or co-op puzzle where players alternate between needing cards that share a symbol and cards that avoid sharing a symbol.

### Possible Mechanics

- play a card sharing a symbol to attack,
- play a disjoint card to defend,
- build alternating chains,
- score balanced patterns,
- complete objectives requiring both connection and separation.

### Why It Is Promising

K₇ gives an unusually clean balance between compatibility and incompatibility.

---

# 14. Practical Product Recommendation

The deck should be presented as a **single mathematical game system**, not merely as a set of unrelated games.

The product identity could be built around four pillars.

## Pillar 1: Pair Registry

Every pair exists once.

Used for:

- exact deduction,
- hidden-face claims,
- bluffing,
- public elimination,
- “name the missing pair” games.

## Pillar 2: Reversible Edges

Every card can point, defect, vote, or belong in either direction.

Used for:

- flipping,
- betrayal,
- route direction,
- allegiance,
- pairwise outcomes.

## Pillar 3: Triangle Closure

Two pair-cards imply the third.

Used for:

- gates,
- rituals,
- almanacs,
- trio puzzles,
- co-op deduction.

## Pillar 4: Graph Scheduling

The complete graph supports matchings, cuts, tours, and tournaments.

Used for:

- simultaneous contests,
- faction borders,
- round-robin structures,
- full-deck trails,
- election games.

## Current Position

The existing games strongly exploit pillars 1–3. Pillar 4 is the most fertile area for future development.

The next major design push should therefore focus on:

1. a tournament-orientation game,
2. a matching-round game,
3. a faction-cut game.

These would broaden the collection and prove that the deck is not just a hidden-face deduction toy, but a genuinely versatile mathematical game system.

---

# Part II — Deeper Structures (verified)

> The sections below extend the analysis above. Every structural claim here is
> constructed and checked by `deck_analysis_verify.py` (see Appendix A), per
> `simulation-standards.md` ("compute, don't assert"). They go beyond §1–14 by
> exposing *decompositions* — ways the whole 36-card deck splits cleanly into
> repeatable rounds, loops, and seasons — rather than single local structures.

The recurring theme of Part I was *what one card, star, triangle, or matching
is*. The recurring theme of Part II is *how the entire deck partitions* — and
why those partitions are unusually friendly to the physical-handling
constraint (`physical-handling.md`), because a partition is a way to keep the
table state **visible and self-recording** instead of remembered.

---

## II.1 The Deck as a Tournament Organiser (edge-colourings)

§6.3 noted that K₈ splits into 7 perfect matchings. That is one instance of a
general fact: a **proper edge-colouring** of Kₙ assigns every card a "round"
so that no two cards in the same round share a symbol. The minimum number of
rounds is the chromatic index:

| Deck | Chromatic index | Round structure | Physical meaning |
|---|---:|---|---|
| K₈ (28 cards) | **7** | 7 rounds × 4 disjoint cards | Every symbol plays once per round; **none rests** |
| K₉ (36 cards) | **9** | 9 rounds × 4 disjoint cards | Every symbol plays once per round; **exactly one rests** |

The odd case is the interesting one. K₉ cannot have perfect matchings (9 is
odd), so each round is a **near-perfect matching**: four cards using eight
symbols, with **one symbol sitting out**. Rotate the rester through all nine
symbols and you get a complete, edge-disjoint cover of all 36 cards in nine
rounds — *each symbol rests exactly once* (verified: §2 of the harness).

This is a stronger, cleaner scheduling primitive than the K₈ round-robin in
§6.3, and it uses the **full** deck:

> **Nine rounds. Each round: four head-to-head contests, one symbol benched.
> Over the season every pair meets once and every symbol sits out once.**

Design payoff:

- The "one rests" rule is a *free, self-balancing* asymmetry — a built-in
  catch-up or rotating-dealer hook that needs no extra component.
- Round membership is **physically checkable** ("no symbol appears twice this
  round; one is missing") — no hidden-face memory, satisfying the
  `physical-handling.md` verify-without-memory test.
- It is a genuinely different scheduler from CROSSROADS' K₈-split: 9 rounds of
  4 on the whole deck, versus a static 14/14 two-player partition.

This sharpens §13.2's matching-round concept: prefer the **K₉ nine-round** form
over the K₈ seven-round form when you want every symbol in play and a built-in
rotating exemption.

---

## II.2 Hamiltonian Decomposition — Four Bracelets, Not One Serpent

§8 covered the Eulerian circuit: all 36 cards in **one** closed loop where
consecutive cards share a symbol. OUROBOROS showed why that single long loop is
physically dangerous — the live "open symbol" lives buried under the chain.

There is a different, underused decomposition. Because K₉ has even degree 8, it
splits into **4 edge-disjoint Hamiltonian cycles** — four separate loops, each
of **9 cards**, each visiting **all nine symbols exactly once** (verified: §1
of the harness; Walecki construction).

| Decomposition | Pieces | Each piece | State to track |
|---|---|---|---|
| Eulerian (§8) | 1 trail | 36 cards, one buried endpoint | Heavy hidden-face memory (OUROBOROS) |
| **Hamiltonian** | **4 loops** | **9 cards, visits every symbol once** | Each loop short, fully visible at once |

Why this dodges the OUROBOROS trap: a 9-card loop is small enough to lay out
**entirely in view**. There is no long tail of hidden state; the whole loop is
glanceable. Four such bracelets is a fundamentally more table-friendly object
than one 36-link serpent.

Design directions:

- **Four-bracelet solitaire / co-op:** reconstruct the four loops from a shuffled
  deck; each loop is a self-checking constraint (does every symbol appear once?
  do neighbours share a symbol?).
- **Race to close a bracelet:** players build toward completing one of four
  9-card loops; flipping a card changes which symbol it offers to its neighbours,
  so a flip can poach or break a forming loop.
- **Seasons as loops** rather than as triangle-sets — a thematic alternative to
  the almanac (II.3).

This is the clean answer to "we want a tour/route game but OUROBOROS proved the
single hidden-state loop fails": **use four short visible loops instead of one
long buried one.**

---

## II.3 The 3×3 Grid: Where the Four-Season Almanac Comes From

`deck-structure.md` ships a reference almanac — 12 triangles in 4 seasons of 3,
each season covering all nine symbols once. Part I (§7) called this a resolvable
STS(9). Part II identifies *exactly what it is* and gives a construction you can
do at the table from memory.

Write the nine symbols in a 3×3 grid in canonical order:

```
1 2 3
4 5 6
7 8 9
```

The almanac's four seasons are simply the four **line directions** of this grid
(diagonals wrap around, mod 3):

| Season | Direction | Triangles |
|---|---|---|
| I | rows | 1-2-3, 4-5-6, 7-8-9 |
| II | columns | 1-4-7, 2-5-8, 3-6-9 |
| III | diagonals ↘ | 1-5-9, 2-6-7, 3-4-8 |
| IV | anti-diagonals ↙ | 1-6-8, 2-4-9, 3-5-7 |

The harness (§4) confirms this grid reproduces the steering almanac *exactly*
and that it is a valid resolvable STS(9): 12 triples, every pair once, each
season a partition of all nine symbols.

This is the **affine plane of order 3, AG(2,3)**: nine points, twelve lines,
four parallel classes (the four directions), three parallel lines per class.
Consequences worth knowing:

- **STS(9) is unique up to relabelling.** The §7 figure of "840 labelled
  systems" is just the 9! relabellings divided by the automorphisms of this one
  grid — there is essentially **one** almanac, presentable as a 3×3 square. That
  is a strong simplification for TWELVE TRIALS: you are not choosing among
  structurally different almanacs, only among rotations/relabellings of one.
- **Constructible from memory.** A player can regenerate the entire 12-triangle
  almanac by writing 1–9 in a square and reading off rows/cols/diagonals — no
  reference chart, directly answering §7's "Steiner systems can be invisible"
  warning.
- **The two diagonal seasons are the two MOLS(3)** (mutually orthogonal Latin
  squares of order 3). The whole almanac is the smallest non-trivial finite
  geometry, which is why nine symbols feels "complete" and six or eight do not
  (no STS at those sizes — §7).

Design payoff: present TWELVE TRIALS' almanac as a 3×3 square, not a table of
twelve trios. "Rows, columns, and both diagonals" is a one-breath teach for the
deepest structure in the deck.

---

## II.4 Unavoidable Triangles (Ramsey & Goodman)

Every structure so far has been about what players *can* build. This one is
about what they **cannot avoid** — a different and underused design lever.

Split the cards of the **6-symbol deck** (K₆, 15 cards) into two groups by any
rule at all — two players, two piles, two colours, mine/yours. Because the
Ramsey number **R(3,3) = 6**, *some* symbol-triangle is guaranteed to be
**monochromatic**: three cards forming a triangle that all landed in the same
group. There is no way to divide them to prevent it (verified: §5 — every one
of the 2¹⁵ colourings of K₆ contains a mono triangle; K₅ has colourings that
escape, so six is the tight threshold).

Goodman's bound sharpens it: the *minimum* over all splits is **two**
monochromatic triangles (verified: §6). You cannot get below two.

Design payoff — "inevitability" mechanics, which the collection currently lacks:

- A game where **completing a triangle is bad** (a debt, a tell, a closed
  conspiracy). At six symbols, no player can keep their cards triangle-free
  forever — the deck *forces* a closure. The skill is in *who* is forced and
  *when*, not whether.
- Six symbols is the **exact tightness point**: at five symbols a player can
  stay clean, at six they cannot. That threshold is itself a tunable knob —
  start at five (escapable), grow to six (inescapable).
- This is a property an ordinary deck does **not** wear on its sleeve, because an
  ordinary deck has no "every pair exactly once" triangle structure to force.
  Passes the deck-necessity test in `product-vision.md`.

Caveat: triangle-detection at the table must stay cheap. Keep it to the
6-symbol subset (15 cards) where the forced triangle is findable by eye; do not
ask players to scan K₉'s 84 triangles.

---

## II.5 Deduction Dynamics, Quantified

§3 described pair uniqueness qualitatively ("the lie-space shrinks"). Here is the
exact arithmetic, which is a balance lever for FALSE FACE and FACE VALUE.

A shown symbol **A** sits on a card whose hidden face is one of A's other
partners. A touches exactly 8 cards. Excluding the card in question, there are
**7 candidate hidden partners**. Each A-card whose location becomes known
(your hand, the registry, the morgue, a resolved challenge, the score pile)
removes exactly one candidate (verified: §7):

```
live hidden partners for shown A = 7 − (other A-cards already located)
```

| A-cards located elsewhere | Live hidden partners | Bluff state |
|---:|---:|---|
| 0 | 7 | wide open — a claim is cheap, hard to disprove |
| 3 | 4 | tightening — claims start to carry risk |
| 5 | 2 | near-pinned — a coin-flip to call |
| 7 | 0 | **forced** — the hidden face is publicly known |

Design implications:

- **Bluffing has a clock.** Early, a lie about A's hidden face is nearly safe (7
  options); late, the same lie is suicidal (1–2 options). FALSE FACE's "can a
  first-gamer price a lie?" question (`COLLECTION_OVERVIEW.md`) is *exactly* this
  curve — the price of a lie is `1 / (live partners)`, and it is computable at
  the table by counting visible A-cards.
- **The 8-card budget per symbol is the meter.** Because each symbol is on
  precisely 8 cards (§1), players have a hard denominator to count against.
  That is the deck-native skill FACE VALUE and FALSE FACE reward, and it is why
  these games need *this* deck and not a generic one.
- **Subset size sets the starting uncertainty:** in K₇ a shown symbol starts with
  5 live partners, in K₉ with 7. Choosing the symbol range is choosing how long
  the bluff window stays open — a direct balance knob for fold-frequency tuning.

This converts §3's qualitative "shrinking lie-space" into a number a designer can
target and a player can count.

---

## II.6 Which New Structures Survive the Table

Part II's structures are mathematically clean, but `physical-handling.md` is the
final judge. Ranking them by handling safety:

| Structure | Visible/self-recording? | Handling verdict |
|---|---|---|
| II.1 Nine-round scheduler | Yes — "no symbol twice, one missing" is glanceable | **Strong** |
| II.3 3×3 almanac | Yes — reconstructable from a square | **Strong** |
| II.5 Deduction clock | Yes — count visible A-cards | **Strong** (already the FALSE FACE/FACE VALUE engine) |
| II.2 Four bracelets | Yes if laid out; each loop short | **Good** — far safer than the §8 single serpent |
| II.4 Forced triangles | Yes at 6 symbols (15 cards) | **Good** if kept to the small subset; risky at K₉ |

The pattern matches Part I's closing principle: the structures that decompose the
deck into **small, fully visible, self-checking pieces** (rounds, a 3×3 square,
short loops, a countable 8-card budget) are the ones worth building on. The ones
that hide state in a long chain (the single Eulerian serpent) are the ones the
deck punishes.

---

# 15. Final Assessment

The deck has unusually strong structure for such a small component set. Its core strengths are:

- perfect pair uniqueness,
- high symmetry,
- physical reversibility,
- triangle closure,
- graph completeness,
- scalable sub-decks,
- multiple deep structures available without adding components.

The main design risks are:

- overusing hidden-face deduction,
- asking players to memorise too much,
- assigning 9 unique abilities too often,
- hiding important state under cards,
- making the mathematical structure invisible or reference-heavy.

The strongest future-proof design principle is:

> Make the mathematical structure visible as physical play.

When the structure can be read directly from the table — visible pairs, visible flips, visible routes, visible triangles, visible matchings — the deck feels clever without feeling academic.

Part II reinforces this from a new angle: the deck's richest unused territory is
its **clean decompositions** — nine rotating rounds with one rester (II.1), four
nine-card bracelets (II.2), the one 3×3-grid almanac (II.3), forced triangles at
six symbols (II.4), and the countable eight-card deduction clock (II.5). These
matter precisely because each breaks the whole deck into **small, visible,
self-checking pieces**, which is the handling property the deck rewards and the
single Eulerian serpent (OUROBOROS) lacked. The next design push — a nine-round
scheduler, a four-bracelet tour, or a forced-triangle game — should be built on a
decomposition that stays glanceable on the table.


---

# Appendix A — Verification of Part II Claims

Per `simulation-standards.md` ("any structural/maths claim should be computed,
not asserted... construct explicit witnesses... record the verification
method in an appendix"), every Part II claim is checked by constructing an
explicit witness in `deck_analysis_verify.py` (top level, beside this file).

Run:

```
python deck_analysis_verify.py
```

What each check constructs and confirms (all currently **PASS**):

| § | Claim | Witness constructed | Check |
|---|---|---|---|
| 1 | K₉ = 4 edge-disjoint Hamiltonian cycles (II.2) | Walecki cycles | 4 loops, each 9 cards visiting all 9 symbols, edge-disjoint, cover all 36 |
| 2 | K₉ = 9 near-perfect matchings, one rester each (II.1) | Rotational circle method | 9 rounds × 4 disjoint cards, rester absent, cover all 36 |
| 3 | K₈ = 7 perfect matchings (§6.3, confirmed) | Circle method | 7 rounds × 4 cards, all 8 symbols/round, cover all 28 |
| 4 | 3×3 grid = resolvable STS(9) = steering almanac (II.3) | Rows/cols/diagonals of AG(2,3) | 12 triples, 4 parallel classes covering all 9, every pair once; matches `deck-structure.md` almanac exactly |
| 5 | R(3,3) = 6 (II.4) | Exhaustive over all 2¹⁵ colourings of K₆; all 2¹⁰ of K₅ | Every K₆ split forces a mono triangle; K₅ does not (6 is tight) |
| 6 | Goodman minimum = 2 mono triangles in K₆ (II.4) | Exhaustive over all K₆ colourings | Minimum is 2 |
| 7 | Hidden-partner lie-space = 7 − located (II.5) | Direct enumeration of A's 8-card star | Live partners 7→0 as A-cards are located |
| 8 | Basic counts (cards, degree, triangles, matching) | `math.comb` | Matches §1 table |

The harness asserts all checks at the end; a non-zero exit means a claim in
Part II has regressed and must be corrected before relying on it.
