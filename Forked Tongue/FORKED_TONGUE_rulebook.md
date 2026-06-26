# FORKED TONGUE

*A game of forgery and finite lies for 3–6 players · ~20 minutes · ages 10+*

Every card in the deck is a unique pair — there is exactly one Moon/Crown in the world. So when you slap down a card showing Moon and purr *"…and beneath it, Crown,"* you haven't told a vague fib. You've forged a specific, unique object — one that someone at this table may be holding. Shed your hand first to win. Lie whenever you like. But the deck is a public registry, and every game the space for lies grows smaller.

---

## Components

- The **36-card** master deck (9 symbols; every pair of two symbols on exactly one card, one symbol per face).

## Setup

1. Shuffle thoroughly, flipping random chunks so faces are randomised.
2. Deal every player a hand: **3P: 8 · 4P: 7 · 5P: 6 · 6P: 5**. Your own hand may be examined (both sides) freely at any time.
3. Spread the remaining cards face-up as the **registry** (3P: 12 cards · 4P: 8 · 5P/6P: 6). Registry cards are dead and public: **anyone may pick up and examine any registry card at any time** (return it as found). Every pair in the registry is a pair nobody can be holding — and a lie waiting to be caught.
4. Whoever most recently got away with something goes first. Play clockwise.

## The ledger

The centre of the table holds the **ledger** — a single overlapping row of played cards, every visible face still showing. The ledger is the game's memory, kept entirely by the cards themselves:

> Each card in the ledger — except the card that **opened** the row — was played *showing the symbol its previous player claimed was hidden*. The row of visible faces **is** the history of claims. Only the **newest claim** lives in the air — and anyone may ask the claimant to repeat it at any time (they must answer truthfully about *what they claimed*).

## Your turn

The newest claim names a symbol — say, **Crown**. Do one of these:

### 1. Play and claim

Play a card from your hand **showing Crown** (either side of any card can face up — flipping a hand card to show its other face is always allowed), overlapping the ledger's end. Then **claim its hidden face aloud**: *"Crown… hiding Moon."*

Your claim may be the truth or a lie. It becomes the new requirement for the next player. You may not claim the symbol that's showing (every card's two faces differ — the table knows it).

*Opening a fresh ledger (first turn, or after a pick-up): play any card, any face, and claim.*

### 2. Decline

Take the **newest card** of the ledger into your hand and end your turn. The requirement then **rewinds one link**: the next player must show whatever symbol the card you just took was showing (that symbol is the previous claimant's claim — they restate it on request). If taking the card empties the ledger, the next player opens fresh.

Decline because you can't show Crown — or because you won't. Nobody knows which.

## Challenges

After a play-and-claim, before the next player acts, **any** player may cry *"False face!"* — closest to the claimant's left wins ties. Flip the played card:

- **The claim was a lie** → the claimant takes the **entire ledger** into their hand. The challenger glows.
- **The claim was true** → the **challenger** takes the entire ledger.

Either way the ledger is now empty; play passes to the player after the claimant, who opens fresh. (The flipped card goes with the rest — its identity is now public knowledge, for those keeping count.)

## Winning

Play your final card, make your claim, and **survive the challenge window**:

- Unchallenged, or challenged and truthful → **you win**.
- Challenged and lying → take the ledger and play on, paler than before.

A final-card claim is the game's signature moment: with one card left, your claim is about a *specific known object* — and everything the table has seen all game points at it.

## A short example (3 players)

A six-turn slice, to show how the cards record the story by themselves. **A**, **B**, **C** play clockwise. We only need to track a handful of cards.

**Setup snapshot.** In the registry, dead and public: among others, **Leaf/Mask**. A is holding **Leaf/Crown**; B is holding **Leaf/Wave**; A is also holding **Leaf/Star**.

Notation: `Crown · Leaf` means a card lying with **Crown** face up and **Leaf** face down. The bracketed phrase after each turn is the live claim — the symbol the next player owes.

---

**Turn 1 — A opens.** A plays Leaf/Crown showing **Crown**, and tells the truth: *"Crown, hiding Leaf."*

```
Ledger ▸ [ Crown · Leaf ]                            owe: Leaf
```

Nobody challenges. B must now show Leaf.

---

**Turn 2 — B plays a lie that the table can't disprove.** B has Leaf/Wave but doesn't want Wave on the air. B plays it showing **Leaf** and claims *"Leaf, hiding Eye."* The card is actually hiding Wave.

```
Ledger ▸ [ Crown · Leaf ] [ Leaf · Eye? ]            owe: Eye
```

Nobody can prove the lie yet — Leaf/Eye is neither in the registry nor in the ledger. The claim passes. C must show Eye.

---

**Turn 3 — C declines, and rewinds the demand.** C's only Eye card is precious. C would rather eat a card than burn it. C takes the **newest** ledger card into hand (the card showing Leaf). The requirement rewinds one link: the taken card was showing **Leaf**, so the next player owes Leaf again.

```
Ledger ▸ [ Crown · Leaf ]                            owe: Leaf
C's hand ▸ … + Leaf/Wave
```

Privately, C now flips the card in hand and sees Wave on its back — so C *knows* B's "hiding Eye" was a lie. But the challenge window has closed; the knowledge is ammunition for later, not a refund now.

---

**Turn 4 — A overreaches.** A still wants to steer with Leaf and plays another Leaf card (Leaf/Star) showing **Leaf**, claiming *"Leaf, hiding Crown."*

```
Ledger ▸ [ Crown · Leaf ] [ Leaf · Crown? ]          owe: Crown
```

**Turn 5 — C challenges from the ledger alone.** Before B acts, C looks at the row: the **Leaf/Crown** card is *already in it* — A played it on turn 1. Every pair exists exactly once, so a second Leaf/Crown cannot exist. C cries **"False face!"** and flips A's top card. It hides Star, not Crown.

A takes the entire ledger into hand. The row is now empty; play passes to **B**, who opens fresh.

---

**What this shows.** The ledger records *what was claimed*, not what was true — turn 2's lie sits in the row, invisible, until a flip or a recycle. Declining never invents a claim; it only shortens the row from its newest end and restores the demand from one step earlier. And the further the game runs, the smaller the lie-space gets: by turn 4, the deck's own arithmetic convicts A without anyone needing to remember a thing.

## Why lies run out (read once, then feel it)

Every pair exists once. The registry kills 6–12 pairs at setup, in public. Every challenge flips a card and kills its pair. Every truthful claim, believed, parks a pair in everyone's reckoning. Early game, a lie is a coin in a fountain; by the endgame, claiming "Moon hiding Key" when the Moon/Key is dead in the registry is a gift to the table — and the *good* lies must thread the few pairs still unaccounted for. The game tightens like a noose, by arithmetic alone.

## Edge cases & FAQ

**Can I claim a pair that's visible in the registry?** Legally, yes. It's a lie, and a free meal for whoever's paying attention. The registry is examinable precisely so that paying attention is skill, not memory.

**Can I challenge my own incoming requirement?** You challenge claims, not requirements — and only in the window before the next play.

**Two players shout at once?** Closest to the claimant's left challenges.

**What happens to the requirement when I decline?** It rewinds one link: removing the top card re-exposes the link beneath it, so the next player owes the symbol your taken card was showing. Because the ledger is only ever shortened from its newest end, the row of visible faces stays an honest history — it can never come to record a claim that was never made.

**Does a decline reveal anything?** Only that you chose it. You may decline holding a fistful of Crowns. Cold-blooded.

**The same player keeps winning challenges.** They're counting pairs. The registry and ledger are open — count back.

**Can the game stall?** Hands shrink by playing and grow by declining/challenges; ledgers recycle. If a table circles, play the **Long Con** scoring variant — rounds end faster than fairness disputes.

## Strategy notes (read after your first game)

- **Lie early, truth late.** Early claims are unfalsifiable; endgame claims are checkable against everything seen. The skilled curve runs from brazen to immaculate.
- **Claims are steering.** Claiming a symbol the next player can't show forces a decline — watch what they've declined before. You can bleed a player a card at a time, and rewind the demand back onto the table, without ever lying.
- **Truth is ammunition.** A true claim, challenged, hands the challenger the whole ledger. Walking into a challenge on purpose is the game's best feeling.
- **Count the eights.** Each symbol sits on exactly 8 cards. Registry plus flips plus your own hand often proves a claim impossible — the table's loudest players usually haven't done the sum.

## Variants

- **Long Con** (scored): play a set number of rounds; when someone sheds, others score −1 per card in hand. Most points after 3 rounds wins.
- **Apprentice Forgers** (first game): challenges only cost/award the **3 newest** ledger cards, not the whole row. Gentler swings while the table learns to count.
- **The Auditor** (5–6P): the player who most recently took a ledger may, once per round, demand any one ledger card be flipped public. Keeps big tables honest.

---

*Design v1.1 — untested at the table. The claim-chain (each card showing the previous claim) keeps all history physical: the only remembered state is the newest claim, repeatable on demand — a deliberate constraint from the OUROBOROS post-mortem. **v1.1: declining now takes only the newest card and rewinds the requirement one link, instead of taking two cards while the claim floated free — the old rule corrupted the self-recording ledger (it could leave the table requiring a symbol no card recorded, and let a later play falsely read as a claim nobody made).** First playtest questions: decline penalty size (one card may be too cheap a dodge — watch the decline rate), ledger swing size (whole-row vs Apprentice), and whether 3P has enough challenge pressure.*
