# WISP — the trail tells where you were

*2–3 players (one Wisp vs. one or two hunters playing as a side) · ~20 min · hidden movement / pursuit · 9 signs, 36 cards · In development · physically unplayed*

> **Status & scope.** Wildcard batch, first flight (July 2026). Written to a deliberately different brief: *maximum originality, rubric waived, no simulation required.* Thought-through and playable as written, but no rulebook, no sim, no rubric self-score, and it should not jump the [focus-priority.md](../.kiro/steering/focus-priority.md) queue on novelty alone. It still carries the two house disciplines that survive any brief: a full physical-handling audit and a fastest-falsification test. Portfolio index: [NEW_GAME_CONCEPTS.md](../NEW_GAME_CONCEPTS.md) §18.

**The trick that makes it exist.** Hidden movement (Scotland Yard, Fury of Dracula) supposedly *needs* what this deck lacks: a way to write down a secret. The inversion — the deck is a **tamper-proof movement log**. A trail card is placed showing the sign you *left* and pressing down the sign you *arrived at*. The chain rule (each new card's shown face must equal the previous card's hidden face) means the trail **publicly confirms your position exactly one step late**, while hiding where you are *now*. At game end the trail is excavated in reverse and every link checks — the fugitive physically cannot lie about the past. Hidden movement with no board, no pencil, and no trust required.

**Setup.** The map is the complete graph itself: nine signs, every pair joined by exactly one road, so no board exists or is needed. Shuffle; deal the Wisp a hand of 12 (a held fan is legitimately private — physical fact #3, [physical-handling.md](../.kiro/steering/physical-handling.md)). Spread the remaining 24 as a public **atlas** sorted by pip: the hunters consult it freely, and by complement they know *exactly* which 12 roads the Wisp holds. Full deduction, zero trust.

**Play.** The Wisp moves every turn (compulsory): play one card from hand onto the trail — an overlapped row, CROSSROADS-style, never a squared stack — **showing the sign being departed**. The first card therefore shows the start position publicly (the Scotland Yard convention) and presses the first true position to the table. Legality: every trail card must contain the current position on one face; because every pair exists once, **no road can ever be re-travelled** — the no-backtrack rule enforces itself.

After each move the hunters may spend one of their **4 Raids**: name a sign. If it is the Wisp's current position, caught — hunters win. The Wisp escapes if the trail reaches **8 cards**. A Wisp whose hand contains no card with the current position is **cornered** — caught by exhaustion.

**Sprint.** Twice per game the Wisp may play *two* cards squared as one packet (announced). The intermediate position is never shown — the packet still audits perfectly at excavation. Sprints break the hunters' one-step-lag anchor at the cost of hand cards (the trail still needs 8 cards total, so a sprint buys ambiguity, not speed).

**The deduction texture.** The hunters always know where the Wisp was one move ago, and the candidate set for *now* is exactly the partners of that sign among the Wisp's remaining (publicly known) cards — typically 2–4 signs. The Wisp's craft is **hand-shaping**: steering toward the signs where the road-book branches widest, spending sprints exactly when the candidate set would have collapsed to one.

**Handling audit.** Everything is visible or self-recording; the only secret is the top card's pressed face — the Wisp's own committed move, which the Wisp may privately re-tip if memory slips (their secret, their peek). No involuntary memory anywhere; the audit is deliberate, terminal, and total. One genuine question: can an 8-card overlapped trail plus a sprint packet be excavated cleanly without card-slippage? (Table question, not a design one.)

**Tuning dials (for the table, not a sim).** Hand size 12 · raid budget 4 · escape length 8 · sprints 2. **Dark variant:** the atlas is squared away unseen — the hunters lose the complement read and the game shifts from chess toward poker.

**Fastest falsification.** One 2P session at base dials: if the hunters' candidate arithmetic reads as homework rather than a tightening noose, or the Wisp is caught by move 3 in every game, the lag mechanic is a proof, not a game.
