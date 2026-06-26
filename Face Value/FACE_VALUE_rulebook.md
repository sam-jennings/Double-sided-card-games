# FACE VALUE

*A heads-up bluffing duel for exactly 2 players · ~15–20 minutes · ages 10+*

Every card you play shows one face and hides the other — and *you* chose which. Showing a 3 whispers "there's a 9 under here." Showing an 8 might mean nothing at all. Stake cards on the strength of what you're hiding, raise until your opponent's nerve breaks, or fold and keep your secret. And because every pair of symbols exists exactly once, the longer the game runs, the more your lies can be *counted*.

---

## Components

- The **36-card** master deck (9 symbols, pips 1–9; every pair of two symbols on exactly one card, one symbol per face).

## Setup

1. Shuffle thoroughly, flipping random chunks so faces are randomised.
2. Deal each player **15 cards**. Your own hand may be examined (both sides) freely at any time.
3. Spread the remaining **6 cards face-up** between you as the **morgue**. Morgue cards are dead and public: **either player may pick up and examine any morgue card at any time** (return it as found). Every pair in the morgue is a pair neither of you can be holding.
4. Each player keeps a **tally** — a face-up overlapping spread of cards they've won. Tallies are public exactly like the morgue: either player may examine any tally card, both sides, at any time.
5. For the first duel, the player who most recently lost a game of anything **acts last** in betting. After that, the **loser of each duel acts last** in the next one.

## A duel, start to finish

The game is a series of duels. Each duel:

### 1. Commit

Both players secretly choose one card from hand *and which face it will show*, hold it flat under a palm, then reveal simultaneously. These are the **duel cards**. They stay on the table, chosen face up, hidden face down against the table — the hidden face is the card's **strength**.

> The face you show is the only claim you make. Both faces always differ, so showing a 3 proves you don't *hide* a 3 — and proves nothing else.

### 2. Bet

Starting with the **first actor** (the previous duel's winner), players alternate taking exactly one action:

- **Raise** — slide one card from your hand, either face up, alongside your duel card. This is your **stake row**. Raising is allowed whether stakes are level or not.
- **Call** — add cards from your hand (faces of your choice) until your stake row equals your opponent's, then go straight to **showdown**. If stakes are already level (including 0–0), calling means showdown immediately.
- **Fold** — concede the duel (see *Folding*).
- **Cold Read** — name the exact symbol you believe your opponent is hiding (see *The Cold Read*).

If you cannot afford to call, you may only raise (if able), fold, or cold read.

### 3. Showdown

Flip both duel cards. **Higher hidden pip wins.** If the hidden pips tie, **higher visible pip wins** — and because every pair exists exactly once, two duel cards can never match on both faces. There is always a winner.

The winner takes **both duel cards and every staked card (both rows)** into their tally.

### Folding

If you fold:

- Your duel card **returns to your hand, unrevealed**. The bluff — or the strength — stays secret.
- Your staked cards go to your opponent's tally, **plus one escape card** from your hand (your choice of card, placed showing whichever face you like).
- Your opponent's duel card and stakes **return to their hand, unrevealed**. They win material; they reveal nothing.

### The Cold Read

On your action, instead of anything else, you may stare your opponent down and name **the exact symbol** their duel card is hiding. Flip it.

- **Right** → you take their duel card, all staked cards, **and two forfeit cards** of their choice from their hand, into your tally. Your own duel card returns to your hand, unrevealed.
- **Wrong** → they take *your* duel card, all staked cards, and **two forfeit cards** of your choice from your hand. Their duel card (now public knowledge) returns to their hand.

Early on, a cold read is a 1-in-8 gamble. Late game — with the morgue, two open tallies, and your own hand all eliminating pairs — it can be arithmetic.

## Ending the game

The game ends immediately when **either player cannot commit a duel card** (hand empty) at the start of a duel.

**Most cards in tally wins.** If tied, compare the total of *all pips, both faces*, across your tally; higher wins. Still tied (it shouldn't be) — the winner of the last duel takes it.

## Why the lies get countable

Your opponent shows a 6. Their hidden face is one of the eight partners of 6 — minus every 6-pair in the morgue, minus every 6-pair in either tally, minus every 6 you're holding yourself. By midgame a shown face often has only two or three live partners. Folding keeps cards secret precisely *because* revealed cards are ammunition: every showdown feeds both tallies, and the tallies are public. The game tightens, duel by duel, by arithmetic alone.

## Edge cases & FAQ

**Can I raise with no intention of calling?** Yes. Raising is pressure, not promise.

**Can stakes get unequal?** Yes — raises don't have to be answered immediately. Showdown only ever happens off a call, which levels them first.

**Can I cold read before any raise?** Yes, any time you have the action. It's usually a bad early bet.

**What if I fold with no cards left after returning my duel card?** You still owe the escape card — your duel card goes instead, unrevealed identity but surrendered. (Rare; you were nearly out anyway.)

**A cold read demands two forfeit cards but the loser holds fewer.** They pay what they have. The duel card still transfers as normal.

**Do returned cards have to keep the same face?** No. Once a card is in your hand it's just a hand card.

**Can both players see whose tally is bigger?** Always. Tallies are open. Pressure is the point.

**Is there hidden randomness after the deal?** None. Every duel is decided by choices.

## Strategy notes (read after your first game)

- **The shown face is a sentence.** Showing low says "I'm hiding strength" so often that showing low *with* weakness is the game's basic bluff. Showing high is stranger — and stranger is harder to read.
- **Fold to stay unreadable.** A fold costs a card but reveals nothing. A cheap showdown loss reveals a pair forever. Sometimes the card is the cheaper price.
- **Count before you cold read.** Eight partners, minus morgue, minus tallies, minus your hand. When the count hits one, the read is free money — if you've actually done the sum.
- **Win duels to keep the tempo.** The winner acts first next duel — first action means committing pressure before information. Losing buys you position. The game self-balances; use it.
- **The escape card is a message.** You choose what to surrender and which face it shows. Feed the tally a lie.

## Variants

- **The Tell** (louder, bridges to FORKED TONGUE): when duel cards are revealed, each player must claim their hidden symbol aloud — truth or lie. If you win a showdown and your spoken claim was *true*, take one extra card of your choice from your opponent's hand. Honesty becomes a weapon; so does the appearance of it.
- **Quick Draw** (~10 min): use the 21-card subset (symbols 1–7). Deal 9 each, morgue of 3. Same rules; the count tightens twice as fast.
- **High Stakes**: a raise may be one *or two* cards. Bigger pots, faster bleed, bolder bluffs.
- **Best of Three**: play a match; tally your tallies.

---

*Design v1.0 — pacing sim-checked (4,000 games per matchup: always terminates, ~12 duels ≈ 15–20 min, threshold bot beats random bot 94% — a healthy skill gap by the OUROBOROS standard), untested at the table. Style exploration and the case for the betting engine over claim-chain and trap-setting at 2P: see `FACE_VALUE_design_analysis.md`. First playtest questions: does fold-to-stay-hidden get used, or do tables call everything? Is the cold read attempted at the right frequency (rarely early, decisively late)? Does acting last feel like the advantage the maths says it is?*
