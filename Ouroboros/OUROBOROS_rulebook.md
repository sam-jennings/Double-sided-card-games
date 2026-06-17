# OUROBOROS

*A solitaire of the world-serpent for 1 player · ~10–15 minutes · ages 8+*

Lay the serpent, scale by scale, until it bites its own tail. Every card is one scale; every scale must flow into the next. Run out of road and you must tie a **scar** into the serpent's body. A flawless, scarless serpent — the true ouroboros — is rare enough to chase for weeks.

---

## Components

- The **36-card** all-pairs deck (9 symbols, every pair of symbols on exactly one card, one symbol per face). The **short game** uses any 7 symbols — remove all cards showing either of the other two symbols on either face, leaving exactly 21 cards.

## Setup

1. Shuffle the deck, flipping random chunks so faces are randomised.
2. Draw cards to a **hand of 4** (3 in the short game). Your hand is private to nobody — look at both sides of your hand cards freely, whenever you like.
3. Leave a long stretch of table. Serpents grow.

## How the serpent grows

The serpent is a single line of cards. The rule of the body, with no exceptions:

> **Each card's hidden face must match the next card's visible face.**

So the visible faces along the serpent read as a journey: Sun, Moon, Key, Crown… and each step is vouched for by the hidden face beneath the previous card.

Both ends are open, and each has an **open symbol**:

- **Head** (the growing end): its open symbol is the *hidden* face of the last card. To grow the head, play a hand card **showing the open symbol**; its other face becomes the new open symbol. Say it aloud as you place it — "…and Sun flows to Comet."
- **Tail**: its open symbol is the *visible* face of the first card. To grow the tail, play a hand card whose *hidden* face is the open symbol — i.e. place it showing its **other** symbol, which becomes the new tail symbol.

The first card of the game may be placed either way up. After every play, **refill your hand to 4** from the deck. Cards in the serpent never flip and never move: placement is forever.

## Scars

If **no card in your hand can extend either end**, you must tie a **scar**:

1. Choose any hand card and place it **sideways** (rotated 90°) at the head, either face up.
2. Its visible symbol becomes the new open symbol. Refill your hand and play on.

The serpent survives, but it remembers. Scars are your score.

## The bite

When the deck and your hand are empty, every card is in the serpent. Curl the head round to meet the tail:

- If the head's open symbol **matches** the tail's open symbol — the serpent bites its tail cleanly.
- If not, that final join is **one more scar**.

**A guarantee, and a curse.** The deck's mathematics promise that a perfect serpent — all 36 cards, zero scars — always exists in every shuffled deck *with perfect foresight*. The same mathematics promise something stranger: **you can never finish with exactly one scar.** Scars only come in constellations (0, 2, 3, 4…). If you're carrying one scar into the endgame, the bite cannot save you.

## Scoring

| Scars | Full game (36) | Short game (21) |
|---|---|---|
| 0 | 🐍 **OUROBOROS** — the perfect serpent | 🐍 **OUROBOROS** |
| 2 | Gold | Gold |
| 3–4 | Silver | Silver — *par* |
| 5–6 | Bronze — *par* | Bronze |
| 7+ | The serpent lived. Barely. | — |

*Par reflects strong play measured over thousands of simulated games; see the design analysis.*

## Strategy notes (read after your first serpent)

- **Your hand is your lifeline, not your options.** The deadliest mistake is judging a play by the symbol it shows — judge it by *how many of your remaining hand cards can still reach an open end afterwards*. In testing, this one shift in attention nearly halved scar counts.
- **Count the eights.** Every symbol lives on exactly 8 cards (6 in the short game). When a symbol's last few cards are gone, stop steering toward it.
- **The tail is half your game.** Players fixate on the head. Two open ends means two chances to keep every hand card alive.
- **Scar smart.** A forced scar still offers a choice: which card, which face. Pick the open symbol that revives your hand, not the prettiest one.

## Variants

- **Short Serpent** (first games, lunch breaks): 7 symbols, 21 cards, hand of 3. Perfect serpents come every few sessions instead of every few weeks.
- **Hatchling** (easier): hand of 5. Roughly halves your scars.
- **Elder Serpent** (brutal): scars may only be tied at the head *and* you must announce your hand's dead cards aloud when you scar.
- **Two-Player Ouroboros**: shared serpent, alternating turns, separate hands of 3, no table talk about hands. Count scars as a team.

---

*Design v1.0 — hand size, par, and the scoring ladder tuned over ~36,000 simulated games. See `OUROBOROS_design_analysis.md`.*
