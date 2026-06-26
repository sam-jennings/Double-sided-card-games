# CAIRN

*A compact solo chain-patience for 1 player · ~10 minutes · ages 10+*

A trail crosses bare country. You mark it by raising **cairns** — small stacks of stones, each stone carved with two waymarks. A stone can only be added to a cairn when one of its waymarks matches the sign on top; you set it down so its *other* waymark now faces the sky, and the trail reaches on. Lay every stone and the trail is complete. Box yourself in and the trail dies where you stand.

Everything fits on a tray. There is never more than a small hand of stones, a face-up draw pile, and three short stacks.

---

## Components

The **36-card** master deck: 9 signs, every possible pair of signs appearing on exactly one double-faced card.

The standard game uses a **7-sign sub-deck of 21 cards**. Set aside the two greatest signs — **Star (8)** and **Crown (9)** — by removing every card that shows either of them on either face. That removes 15 cards and leaves the complete 7-sign deck: signs **Moon (1), Leaf (2), Wave (3), Flame (4), Eye (5), Mask (6), Key (7)** — every pair among the seven, once each.

No tokens, board, or paper are required.

> Each card shows **one sign per face**. There is no card back: a card on the table always shows exactly one of its two signs. You may freely look at both faces of any card in your hand.

---

## Core idea

Each card is a **link between two signs**. A cairn is a stack whose **top card shows one sign** — the cairn's current **waymark**.

To extend a cairn, play a card that carries its waymark. The two cards meet at that shared sign (the *join*), so you place the new card showing its **other** sign. The old waymark is now buried and finished with; the new sign becomes the cairn's waymark, and the trail continues from there.

You are trying to lay **all 21 cards** onto your three cairns without ever reaching a position where nothing in your hand can be played.

---

## Setup

1. Build the 21-card sub-deck (signs 1–7) as above.
2. Shuffle thoroughly, flipping random chunks as you go so each card's showing face is randomised.
3. Square the cards into a face-up **stock** (a draw pile). Only its top card is visible; that is fine.
4. Deal three cards to start the three **cairns**, in a row. For **each**, choose which face shows — that sign is the cairn's starting waymark.
5. Draw **four cards** into your **hand**. You may look at both faces of your hand cards at any time.

The stock now holds 14 cards. You are ready.

---

## How to play

On your turn:

1. **Play one card from your hand** onto a cairn whose waymark matches one of that card's two signs. Set it on top, turned so its **other** sign now shows — that becomes the cairn's new waymark.
2. **Refill** your hand to four by drawing the top card of the stock. (Once the stock is empty, your hand simply shrinks as you keep playing.)

That is the whole turn: play one, draw one.

**The free look.** The stock's top card always shows one face. Before you commit, you already know one sign of the card you will draw next — use it. (You never need to touch the stock to learn this; it is just sitting there, face up.)

**Buried stones are done.** Once a card is covered on a cairn, you never consult it again. The only live information is the three waymarks on top and the cards in your hand.

---

## Winning and losing

- **You win** when every card is on the cairns — the stock is empty and your hand is empty. The trail is complete.
- **You are blocked** (the trail dies) when, at the start of your turn, **no card in your hand can be legally played on any cairn**. The game ends immediately.

Your **score is the number of stones left unlaid** — the cards still in your hand (plus any still in the stock). **Zero is a win.** Lower is closer.

| Stones left | Result |
|---:|---|
| **0** | **Trail complete** — a clean crossing |
| 1–2 | The trail all but reaches; one bad ridge |
| 3–5 | Lost in the open |
| 6+ | Turned back early |

A clean crossing is the real goal. When you win comfortably, raise the difficulty (see Variants) rather than chasing a sub-score — CAIRN's rating ladder is its difficulty levels, not points.

---

## Why it belongs to this deck

A card here is literally an **edge between two signs**, and the whole game is chaining edges by a shared vertex — something an ordinary deck cannot do, because an ordinary card carries no second sign to chain from. Three properties of the all-pairs deck carry the game:

- **A card is a link.** Placing it consumes one sign at the join and exposes its partner. The trail *is* a walk through the sign-graph.
- **Each sign sits on a known number of cards** (six, in the 7-sign deck). Because you can see the whole deck, you always know how many cards bearing a given sign are still unplaced — so you can keep your waymarks on **live** signs and avoid stranding a cairn on a sign whose cards are all spent.
- **Every pair is unique**, so the card showing one face of the stock is one specific unplaced link, and the candidates shrink as you play — the counting that rewards a careful player.

It also stays honest about double-faced cards. The only state you ever read is the **visible top** of three short stacks plus your hand. Nothing important is ever buried or pressed face-down — the failure that sank OUROBOROS. There is no hidden-face memory; there is deliberate, open counting.

---

## Strategy notes

- **Keep your waymarks alive.** A cairn topped by a sign with no unplaced cards left is a **dead stack** — nothing can ever extend it. Before exposing a sign, ask how many of its cards remain.
- **Keep the three waymarks different.** Two cairns showing the same sign waste a landing spot and both feed on one dwindling supply. Diversity keeps your options open.
- **Use the free look.** If the next stock card shows Flame, leaving a cairn topped with Flame guarantees that card a home. Steering your play toward the sign you can already see coming is the cheapest skill in the game.
- **Look two moves ahead.** You rarely need to plan deeper than the card in front of you and the one after it. A little foresight beats a lot of luck here.
- **Spend your awkward cards early**, while you still have cairns flexible enough to take them; don't hoard a card that only fits one fading sign.

---

## Variants

### First Trail (gentle)

Use **four** cairns instead of three (deal four starting cards). The extra landing spot makes blocking much rarer — the best way to learn the flow before tightening to three.

### Pathfinder (hard)

Hold a hand of **three** instead of four. Less choice each turn, more dead-ends to foresee. The same 21-card trail, sharper.

### The Long Trail (expert · whole deck)

Use all **9 signs / 36 cards**, **three** cairns, and a hand of **five**. The full deck is a genuinely harder crossing — the larger hand is what keeps it a game of planning rather than luck (a tight hand at nine signs is mostly draw-luck; the wider hand restores control without spreading you across the table). Recommended only once the standard trail feels comfortable.

> The hand grows, the table does not — The Long Trail still lives in three short stacks plus a held fan. That is the whole design: when the country gets harder, you carry more stones, you don't build wider.

---

## Edge cases & FAQ

**Must I play a card every turn?**
Yes. If you *can* play, you must. You only stop when you win (everything placed) or you are blocked (nothing playable).

**Can I choose not to draw?**
No. After playing, you always refill to a full hand while the stock lasts. The shrinking hand at the end is part of the squeeze.

**What if two cairns share the same waymark and my card matches both?**
Play it on either — you choose. (The result is the same exposed sign either way; pick the cairn whose position you prefer.)

**My card matches one cairn on *both* of its signs — what happens?**
That only occurs if a cairn's waymark equals one of the card's signs; you expose the other sign as normal. A single card can't match the same cairn two different ways, because a cairn shows only one waymark.

**Can I look at the buried cards in a cairn?**
There is no need, and the game is built so you never have to. Treat buried cards as gone.

**Can I rearrange my hand or inspect both faces of held cards?**
Freely. Held cards are yours to study on both sides; that is legal and expected.

**The stock ran out — now what?**
Keep playing from your hand without refilling. You win if you empty it; you lose if you get stuck first.

**Is it ever impossible to win a deal?**
Rarely, yes — a few shuffles cannot be cleared even with perfect play. Simulation suggests a careful player clears the great majority of standard deals, so a loss usually means a better line existed.

---

## Open playtest questions

*To be answered at the first table test.*

1. **Do the chaining choices feel meaningful, or like arithmetic?** The central fun question — is "which waymark do I expose?" a satisfying decision or dry bookkeeping?
2. **Does getting blocked feel fair?** When the trail dies, does it read as a foreseeable mistake (good) or an arbitrary bad shuffle (bad)?
3. **Is a hand of four the right size** for the standard 7-sign trail — enough choice without trivialising it?
4. **Is the free look actually used?** Do players naturally exploit the stock's visible top, or does it go unnoticed and need teaching?
5. **Is the footprint genuinely tray-sized** in practice (three growing stacks + a held fan), including The Long Trail at nine signs?
6. **Does the difficulty ladder land** — First Trail → standard → Pathfinder → The Long Trail — as a satisfying progression?

---

*Design v0.1 — sim-validated, awaiting first table test. Structure, hand-vs-reserve, and realistic-information planning agents checked in `cairn_sim.py`; the 7-sign hand game cleared the skill gate (careful play approaches the clairvoyant ceiling). See concept sheet §13 in `NEW_GAME_CONCEPTS.md`.*
