# Combinatorial "Every Pair Once" Double-Sided Card Decks: Prior Art and Market Survey

## TL;DR
- **No published commercial game exactly matches your structure** — a pure complete-graph (K_N) deck of C(N,2) double-sided cards with one symbol per face, every unordered pair appearing exactly once, where grid face-orientation matters. The closest prior art is a 1986 US patent ("Two-value playing cards," US 4,588,193, Scott E. Winston), and the closest commercial relatives each satisfy only part of the requirement: Reiner Knizia's *Ingenious* (every two-color pair of 6 colors, but single-faced and with duplicates/doubles) and Shaun Delaney's *2 Way Cards* (double-sided tiles on a grid where orientation matters, but standard card values, not the pair structure).
- **Your design space is genuinely under-exploited.** The "exactly once" complete-graph constraint is well known in mathematics (round-robin scheduling, K_N edge sets) but has not been turned into a mainstream published game with the one-symbol-per-face twist. This is white space, not a crowded field.
- **Be careful to distinguish your structure from three famous lookalikes** — Dobble/Spot It (finite projective plane: every two cards share one symbol), dominoes (both values on one face, plus doubles), and Ingenious (multiset with doubles, single-faced). None of these is your structure.

## Key Findings

1. **Exact structural match in prior art = a patent, not a product.** US Patent 4,588,193, "Two-value playing cards," granted 1986 to Scott E. Winston of Budd Lake, NJ, describes a deck "comprised such that every specific suit-value pair is coupled once with every other specific suit-value pair in the minimum number of cards." This is precisely the round-robin / complete-pairing structure you describe. It was never a major commercial product.

2. **The closest commercial game is *Ingenious* (Einfach Genial), designed by Reiner Knizia under commission from Sophisticated Games and published in 2004 by Kosmos.** It uses 6 colors and tiles bearing every two-color combination — but it deviates in three ways: it includes "doubles" (same color on both halves), it has multiple copies of each combination, and both symbols sit on one face (domino-style), not one per face of a double-sided tile.

3. **The closest game on the "double-sided tile + grid orientation" axis is *2 Way Cards* by Shaun Delaney (SJD Games / The Happy Puzzle Company).** Players place double-sided tiles into a shared 7×7 vertical grid; each face shows a different value to each player, so orientation/face genuinely matters. But it uses standard playing-card values, not the all-pairs structure.

4. **Dominoes are the canonical "all pairs" object but differ in two critical ways:** a standard double-six set is "one unique piece for each possible combination of two ends," but both values appear on a single face and the set includes doubles (0-0 through 6-6). Your structure excludes doubles (a pair must be two *different* symbols) and puts one symbol per face.

5. **The math is standard and well-documented.** C(N,2) = N(N-1)/2 is exactly the number of games in a single round-robin tournament (each pair meets once) and the number of edges in the complete graph K_N. For N=9, that is 36; this is the same count as a round-robin among 9 players. Designers and mathematicians discuss this structure, but mostly in tournament-scheduling and graph-theory contexts, not published games.

## Details

### Your exact structure, precisely defined
You are describing the **edge set of the complete graph K_N**: N vertices (symbols), and one card per edge (unordered pair of two distinct symbols). The deck has exactly C(N,2) = N(N-1)/2 cards. With N=9, that is 36 cards. The novel physical twist is that each card is **double-sided with one symbol per face**, so which symbol is "showing" depends on orientation — a degree of freedom dominoes and Ingenious tiles do not have, because they print both values on one face.

This is mathematically identical to a **single round-robin schedule**: in a single round robin, each pair meets exactly once, and with n teams that produces n × (n−1) / 2 total games. The same object is the complete graph: graph-theory treatments note that for the complete graph K_n, every pair of vertices is joined by exactly one edge.

### Prior art #1 — US Patent 4,588,193 "Two-value playing cards" (Scott E. Winston, 1986)
This is the single closest documented match to your combinatorial intent. Claim 1 specifies that "the two display areas of the cards of a given playing card deck are comprised such that every specific suit-value pair is coupled once with every other specific suit-value pair in the minimum number of cards," and "the same suit-value pair does not appear in both display areas of any individual card." The preferred embodiment is a 60-card deck (48 "pure" two-value cards realizing the complete-pairing structure plus 12 half-wild cards for divisibility/fairness), using three suits × four values.

Critically, the patent uses a **rotational two-corner arrangement** rather than literally one symbol per physical face: both suit-values appear on the same front face in opposite corners, and rotating the card 180° swaps which one is "up." The rear face is "symmetrical about the imaginary diagonal line which bisects each card" so an opponent cannot tell which way a player rotated the card. So it captures the "orientation determines which symbol is active" idea, just on one face via rotation rather than via a front/back flip. A later patent (US 7,481,435) cites it and summarizes: "A deck of double-valued cards, designed so that every number value of a given suit is paired once with every number value of the other suits, is described in U.S. Pat. No. 4,588,193 to Winston."

### Prior art #2 — US Patent 5,011,146 "Video card game" (double-faced, but N² with doubles)
This patent describes a tile set with indicia on **both faces** (one symbol per face — the true double-sided arrangement you want), but the counting is different: "A game set has N forms of indicia; and the total number of pieces in the set is equal to (N)(N+1)/2+(N)(N-1)/2 = N²," and "each indicia combination occurs twice in the set, except for twin (double) indicia combinations which occur only once." That is N² pieces including doubles — not the pure C(N,2) edge set — but it is the closest documented example of the literal one-symbol-per-face construction.

### Closest commercial game — *Ingenious* (Reiner Knizia, Kosmos, 2004)
*Ingenious* (German: *Einfach Genial*) is the most famous "every two-color combination" tile game. Its tiles are "in the shape of two conjoined hexagons, with one of the coloured symbols in each hexagon." Per Wikipedia: "There are six tiles for each two-colour combination (e.g. red/orange) and five for each double (e.g. blue/blue)" — i.e. 6 copies of each of the 15 mixed pairs plus 5 of each of 6 doubles, for 120 domino-style tiles, each consisting of two conjoined hexes where each hex shows one of six colors. (The smaller Kosmos edition, *Einfach Genial Knobelspass*, instead uses "one of each of the 21 different tile combinations.") Deviations from your structure: (1) the full game includes doubles; (2) it has many copies of each combination rather than exactly one; (3) both colors are on one face (domino-style), so orientation/flip does not hide or change a symbol.

### Closest "double-sided tile on a grid where orientation matters" game — *2 Way Cards* (Shaun Delaney)
*2 Way Cards* (and its sibling *2 Way Words*) from designer Shaun Delaney places double-sided tiles into a shared 7×7 vertical grid. Per Board's Eye View: "two players placing double-sided tiles into a 7 x 7 vertical grid... the tiles show a different card on their reverse, so when you place a card into the grid, the card that appears for your opponent differs from your own card." This is the purest commercial example of the **double-sided + grid + orientation-matters** mechanic — each player sees a different face of the same physical tile. But the tiles carry standard playing-card values: exactly 108 tiles, described as "the equivalent of two standard packs of cards plus four Jokers available to each player" — not the all-pairs combinatorial structure.

### The three famous lookalikes you must distinguish from
- **Dobble / Spot It (finite projective plane).** "Each card has eight different symbols... Any two cards share exactly one matching symbol." This is the projective-plane structure (q²+q+1 cards/symbols; the standard deck uses 55 of a possible 57), completely different from K_N. Here the shared symbol is between *cards*, not a pair printed *on* a card.
- **Dominoes.** "The traditional domino set contains one unique piece for each possible combination of two ends with zero to six spots... 28 unique pieces in a double-six set." All combinations including doubles, both values on one face.
- **Ingenious (above).** Multiset with doubles, single-faced.

### Where designers discuss this idea
- A BGG thread ("Card orientation") describes a near-identical physical concept: "Each card has two values, oriented away from each [other] so the way you reveal the card, the one that is on top is right side up, while the bottom would be upside down... Like a standard playing card, but with two different values." This indicates active designer interest but no canonical published title.
- BGG hosts geeklists specifically cataloguing games that use card backs as functional faces ("Show me your back side - Games where the cards use their backs as well as their fronts") and "dual-sided"/split-card games — useful scouting grounds, but none catalogued there implements the exact C(N,2) one-per-face structure.

## Recommendations

**Stage 1 — Confirm novelty and stake your claim (now).**
- Treat US 4,588,193 (Winston) and US 5,011,146 as the key prior art to design around. Winston covers "every pair once" but via rotation on one face with suits/values; 5,011,146 covers one-symbol-per-face but at N² with doubles. Your combination — **pure C(N,2), no doubles, one symbol per physical face, with grid face-orientation as a live gameplay variable** — appears to be unclaimed white space. If you intend to patent or publish, have a patent attorney run a formal search; my search was non-exhaustive.
- Position your game's hook around the property none of the lookalikes have: **the same physical card is two different "things" depending on which face is up**, combined with the guarantee that every pairing exists exactly once (so the deck is a closed, fully-balanced system).

**Stage 2 — Prototype and pressure-test the math (next).**
- For N=9 you get 36 cards — a clean, box-friendly count and the same as a 9-player round robin. Note the parity fact from round-robin theory: each symbol appears on exactly N−1 cards (degree N−1 in K_N). For N=9 each symbol appears on 8 cards. If you want every symbol to appear an *even* number of times (useful for some grid-balancing schemes), pick odd N (so N−1 is even).
- Use round-robin "circle method" scheduling to generate balanced deal/round structures if your game has rounds; the literature is mature and directly portable.

**Stage 3 — Borrow proven mechanics from the adjacent games (during development).**
- From *2 Way Cards*: the hidden-information tension of each player seeing a different face of the same tile, and "you know what you're giving your opponent" memory play. This is the most directly transferable design lesson.
- From *Ingenious*: scoring that rewards collecting/connecting matching symbols across a grid, and the elegance of a fully enumerated tile set.
- From *Mr. Jack Pocket*: a 3×3 grid of cards whose orientation/visibility can be rotated and swapped as core actions — a proof point that "rotate/flip a card on a small grid" is a viable, published action economy.

**Benchmarks that would change the recommendation:** If a formal patent/BGG search surfaces a published game that is a pure C(N,2) one-symbol-per-face deck, your positioning shifts from "novel structure" to "novel implementation/theme," and you should differentiate on mechanics instead. If playtests show the orientation-tracking is too fiddly (a concern raised in the BGG design threads — players forgetting flip direction), add a physical asymmetry/clip so orientation is unambiguous.

## Caveats
- **"No exact commercial match" is a bounded-search conclusion, not a proof of nonexistence.** I ran roughly 18 web searches plus one focused sub-investigation; BGG's own search was bot-blocked for direct fetching, so some niche or out-of-print titles and self-published/Kickstarter games may not have surfaced. A targeted BGG advanced-search (by mechanism: "Square Grid," "Tile Placement," and "card orientation") and a patent-attorney search are warranted before relying on novelty commercially.
- **The patent grant year (1986) for US 4,588,193 is firmly established, but the exact filing date was not directly confirmed** from the Google Patents / FreePatentsOnline bibliographic panels (those pages would not load or were bot-blocked during research); treat the mid-1980s filing as approximate.
- **Terminology overlap is a real research hazard.** "Double-sided cards" overwhelmingly returns articles about card *backs* (brand identity) and "dual-sided"/split cards (two things on one face). Your structure requires precise framing — "complete graph K_N," "edge set," "every unordered pair exactly once," "one symbol per face" — to retrieve relevant results.
- Several sources here are patents and designer blogs/forums rather than peer-reviewed; patents establish prior-art existence but not commercial significance, and forum posts establish designer interest but not published implementations.