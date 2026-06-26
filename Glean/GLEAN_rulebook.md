# GLEAN

*A trick-taking game of gathering signs for 3, 4, or 6 players · ~20 minutes · ages 10+*

Every card carries two signs, and every trick you take is a harvest — because the card you capture counts for **both** of its signs at once. Win the most of a sign and you claim it. The catch: the side you show to follow is never the side that wins the trick. What beats the table is the face you kept hidden. Gather the signs; claim the most; the greatest harvest wins.

*GLEAN is the bright sibling of **BLIGHT** — the same trick engine, the opposite goal. Learn one and you can play the other.*

---

## Components

- The **36-card** master deck (9 signs; every pair of two signs on exactly one card, one sign per face). The corner **index pips (1–9)** are the ranks: Moon 1, Leaf 2, Wave 3, Flame 4, Eye 5, Mask 6, Key 7, Star 8, Crown 9.

> **Sign *is* rank — read this before your first game.** Unlike an ordinary deck (four suits, each holding every rank), here each sign has **one fixed strength**: Crown is *always* 9, Moon is *always* 1. There is no "low Crown" or "high Moon." Every card pairs two *different* signs, so it always carries two different strengths — one per face. Players used to suit-and-rank decks often miss this; say it out loud when teaching.

## Setup

1. Shuffle thoroughly, **flipping random chunks** as you shuffle.
2. Deal the **entire deck** out evenly:
   - **3 players:** 12 each.
   - **4 players:** 9 each.
   - **6 players:** 6 each.
   - *(5 players: set one card aside face-up as a dead **gleaning** — it belongs to no one but everyone can see it — and deal 7 each.)*
3. Examine your hand freely, **both sides**, all game.
4. GLEAN is played as a **match of one round per player**. Each round a different player leads first (pass the lead clockwise). Sum scores across the match; highest total wins. *(Rotating the lead matters — see the design footnote.)*

## How a trick works

The player to lead plays any card from their hand, choosing **which face shows**. That sign is the **led sign**.

Going clockwise, each other player must **follow**: play a card carrying the led sign **on either face**, placed so the led sign shows. If the led sign is on the card's other face, **flip it to follow** — that is the deck's signature move. If you hold no card carrying the led sign at all, **slough**: play any card, any face up. *(Sloughs cannot win the trick.)*

**The reveal.** When everyone has played, **flip every card in the trick.** Among the cards that *followed* (showed the led sign — including the leader's), the one whose **revealed (hidden) face has the highest pip wins the trick.** Ties are impossible: every follower hid a different partner of the led sign, because every pair exists exactly once.

> The face you show to follow is the same sign for everyone — so it can never decide the trick. **What wins is the strength you hid.**

The winner gathers **all** the cards in the trick into their **harvest** — a face-up spread in front of them — and leads the next trick.

## The harvest is public

Your gathered cards lie in an open spread. Like the registries in the collection's other games, **any player may pick up and examine any gathered card, both sides, at any time** (return it as found). Nothing here is remembered; everything is counted from what's on the table.

## Scoring a round

Every card has been gathered by someone. Now claim the signs.

For **each of the 9 signs**, count how many gathered cards carry it (on *either* face) in each player's harvest. **Whoever holds the most cards of that sign claims it**, scoring its pip value:

| Sign | Moon | Leaf | Wave | Flame | Eye | Mask | Key | Star | Crown |
|---|---|---|---|---|---|---|---|---|---|
| **Worth** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

- A sign is worth its pip to whoever gathered the most of it. **Maximum possible in one round: 1+2+…+9 = 45.**
- **Tie for a sign → it goes unclaimed** (deadlocked; nobody scores it). Each sign sits on exactly 8 cards, so majorities are real contests.

Sum your claimed signs. Add up the match across all rounds.

**Round tiebreak (for the per-round winner, if it matters):** most signs claimed; then whoever claimed the **Crown**; then earliest in turn order. **Match tiebreak:** most rounds won outright.

## Edge cases & FAQ

**Must I follow if I can?** Yes. If any card in your hand carries the led sign on either face, you must play one of them showing that sign. Sloughing while able to follow is illegal (and visible at the reveal).

**Can I choose which of several followers to play?** Yes — and it's the heart of the game. Each carries the led sign but hides a different partner; you choose how hard to fight for the trick.

**Why would I ever lose a trick on purpose?** Winning worthless tricks doesn't help — you want the cards that tip the signs you can still win. Spending a strong card to gather signs you've already lost is wasted. Duck, and save your strength.

**A card helps two of my signs at once.** Yes — that's the engine. Gathering the Star/Crown advances you toward *both* the Star and the Crown majorities. The unique high-value cards are fought over from two directions.

**Do I orient gathered cards a particular way?** No — both faces count regardless of which is up. Keep your harvest spread so both you and the table can read it.

**The lead keeps coming back to the trick winner.** Yes. Win a trick and you choose the next attack.

## Strategy notes (read after your first game)

- **Lead what you're long in.** Leading a sign you hold many of funnels its cards toward your harvest — but every lead also tells the table what you're collecting.
- **The hidden face is your weapon; spend it deliberately.** You only have so many high-hidden cards. Win the tricks that matter; throw your low cards into the tricks that don't.
- **Count the eights.** Each sign sits on exactly 8 cards. Once someone holds 5, that sign is clinched — stop fighting for it and pivot.
- **Deadlock the signs you can't win.** Splitting a sign 4–4 robs your rival of its points entirely. Denial scores nothing for you, but nothing for them either.
- **Star and Crown are gravity wells.** Worth 8 and 9, they're fought hardest — and the Star/Crown card alone is contested by both camps.

## Variants

- **Plunder (first game / lighter):** keep the area-majority structure but drop the pip values — for each of the 9 signs, whoever captured the most cards carrying it (either face) scores **1 point** (ties: nobody scores it). Most points wins; the maximum is 9. Teaches the trick engine *and* the majority count without any large-number arithmetic, then the full game is one step away ("each claimed sign is now worth its pip instead of 1 point"). *(Note: only the full pip-value majority game is simulation-validated; Plunder is a teaching scaffold.)*
  - *Earlier pip-sum Plunder (score every captured card's two pips) was dropped after its first table test: the totals ran to ~110 a round, the arithmetic was unpleasant, and high pips dominated both winning and scoring at once.*
- **The Passing (smoother, recommended once learned):** before play each round, pass 3 cards to your left (4P/6P) — Hearts-style — to soften unlucky deals. Reduces how much the deal decides.
- **Partners (4P or 6P):** play in fixed teams sitting alternately; combine teammates' claimed signs. Restores duel tension at larger counts.
- **Closed Harvest (memory variant):** instead of an open, examinable spread, stack your gathered tricks **face-down**; reveal and count majorities only at round end. Trades the public registry for a deliberate memory/counting challenge — a legitimate, deck-native mode (the public pair-registry still bounds what's knowable). Offer it to players who find the open harvest removes the trick-taking skill of remembering what's been played. *(Untested; the open-harvest game is the validated default.)*

---

*Design v1.0 — simulation-validated (`glean_sim.py`; ~4,000 rounds per player count, seed 42), untested at the table. Skilled play beats random by **1.74× (3P) / 1.67× (4P) / 1.49× (6P)** — healthy at 3–4P, thinner at 6P (treat 6P as the lighter, higher-variance option). The deck's reveal is forced, not arbitrary: because every follower shows the led sign, the hidden face is the only thing that can break the trick. **Caveats for the first table test:** (1) the deal carries real weight — under random play the strongest hand wins ~52% at 3P, so GLEAN is played as a **match with rotating lead** to smooth it (and The Passing variant smooths it further); (2) the first leader is slightly disadvantaged, which the rotation answers; (3) scoring nine simultaneous majorities by flipping through harvests is the key handling question — does it stay frictionless, or does the table want the Plunder count? Sibling: **BLIGHT** (same engine, avoidance goal).*
