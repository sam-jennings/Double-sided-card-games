# QUEUE — retired, renamed to HINGE

Retired 25 July 2026. The rotate/flip-top-card mechanic this concept was built on failed solo playtest — it never generated enough matches to reach an endgame. It was replaced by a split-and-block-flip mechanic, which changed the game enough that the QUEUE name (built entirely on the cyclic-rotation idea) no longer fit.

**Current concept and game record:** [Hinge/HINGE_concept.md](../Hinge/HINGE_concept.md).

This file is kept as design history only. It is not a game record (`record_type: game` removed) and should not be treated as a current source of truth for state, catalogue position, or rules.

---

## Original concept (superseded)

*2 players · ~5–10 min per round · pocket abstract · 15 cards (6 signs)*

**The trick that made it exist.** VIGIL asked "what if a game needed no session?"; QUEUE asked "what if a game needed no *surface*?" The entire state was a squared packet held in one hand, face-out; the moves were one-thumb operations. The deck property underneath: a packet has a **cyclic order that cutting preserves** — so "rotate" was a legal, undoable-by-nobody, zero-surface move.

**Setup.** The 6-sign sub-deck, 15 cards, shuffled, squared, held face-out by either player. Players alternate moves; whoever holds it passes it after moving.

**A move.** Exactly one: **rotate** (move the front card to the back), or **flip** the front card in place.

**Scoring — the chord.** If after your move the front three cards all showed the same sign, retire those three; most retired cards wins the round; best of three.

**Why it was retired.** A single-card-per-turn move touches too little state. Rotating only cycles the same 15-card order past a 3-card window; flipping only changes one card's face. Neither move does enough work per turn to build a triple before the packet cycles back on itself — solo testing confirmed it was basically impossible to line up three matching faces. See [HINGE_concept.md](../Hinge/HINGE_concept.md) for the replacement mechanic and full playtest note.
