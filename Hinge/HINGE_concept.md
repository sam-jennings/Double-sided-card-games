---
record_type: game
game: "HINGE"
state: In development
players: [2]
player_count: "2"
duration: "5–10 min"
genre: "Pocket abstract"
complexity: Light
min_players: 2
max_players: 2
min_minutes: 5
max_minutes: 10
physically_playtested: true
public_document: "Hinge/HINGE_concept.md"
next_step: "Formalise the 2-player turn structure for the split-and-flip mechanic, then run a 2-player table test."
catalog_order: 29
---
# HINGE — split it, flip it, chase the run

*2 players · ~5–10 min per round · pocket abstract · 15 cards (6 signs) · In development · physically played; mechanic replaced after solo test*

> **Status & scope.** Wildcard batch, second flight (July 2026) — *originality first, rubric waived, unsimmed*. Renamed from QUEUE on 25 July 2026 after the original rotate/flip-top-card mechanic failed solo playtest and was replaced by the split-and-flip mechanic below. Still needs a 2-player table test before it can move past `In development`. Portfolio index: [NEW_GAME_CONCEPTS.md](../NEW_GAME_CONCEPTS.md) §26.

## Playtest note — original QUEUE mechanic rejected (25 July 2026)

Solo test of the original rules (rotate front-to-back, or flip the front card in place; score when the front three match) found it **basically impossible** to line up three matching faces. The problem was structural, not bad luck: a single-card-per-turn move touches too little state. Rotating only ever cycles the same 15-card order past a 3-card window; flipping only ever changes one card's face. Neither move does enough work per turn to build a triple before the packet cycles back on itself. The honest risk flagged in the original concept (parity-solvable, not a real game) undersold the actual failure — it wasn't solvable *or* unsolvable, it just never generated enough matches to reach an endgame. That concept is retired at [Queue/QUEUE_concept.md](../Queue/QUEUE_concept.md).

## The mechanic — split and flip

**The move.** On your turn, cut the held packet at any point (choose how many cards from the front, 1 to n−1), then flip *that entire sub-packet over as one block* — like flipping a stack of pancakes on the hinge of the cut. This does two things at once: it reverses the internal order of every card in the flipped block, **and** it flips each of those cards to its other face. The untouched remainder of the packet keeps its order and faces.

This is the fix for the old problem: one move now reorders *and* reveals multiple cards simultaneously, instead of moving or flipping exactly one card. A single well-chosen cut can create, destroy, or shift several matches at once — and the name follows the physical action: every move pivots the packet on a hinge point you choose.

**Scoring.** After a move, scan the packet for any run of three or more adjacent cards showing the same sign. If one exists, claim it: pocket those cards and close the gap in the packet (the remaining cards slide together). A move can create more than one run; claim all of them.

**Why it works.** Solo testing confirmed matches now form reliably within a handful of moves — the block-flip is expressive enough to hunt for and construct runs, the way a pancake-sort puzzle has real structure to search. It also keeps the original premise intact: no surface needed, the packet is still held in one hand, and the move is still a single thumb action (a cut-and-flip).

## Open question — extending to two players

Confirmed solo; **not yet tested with two players.** The mechanic itself (cut, flip the block, scan for runs) doesn't change with player count, but the turn economy needs deciding before a 2P test:

- **Turn order.** Simplest version: strict alternation, packet passes after every move regardless of whether it scored — same "the pass is the turn marker" property as the original.
- **On a claim.** Does claiming end your turn (pass anyway), or earn a bonus move (claim-and-go-again, tic-tac-toe style)? Untested; alternation-only is the safer first hypothesis since it preserves the thinning-packet clock cleanly.
- **Endgame.** Carried over: round ends when fewer than 3 cards remain, or after a set number of chordless moves; most claimed cards wins; best of three.

**Next step:** pick one turn-economy hypothesis (recommend: strict alternation, no bonus move, first pass) and run it as a real 2-player table test before touching anything else.
