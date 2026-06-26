# TWELVE TRIALS

*An open-information puzzle for 1–2 players (plus a table co-op mode) · ~15 minutes · ages 10+*

Hidden inside every shuffle of the 36-card deck is an **almanac**: a way of sorting all the cards into twelve perfect trios. Each trio is a closed ring of three symbols — three cards, three faces, each card vouching for the next. The almanac is always there. The trial is finding it without turning the world upside-down.

**Nothing is hidden in this game.** You may pick up and examine any card at any time — just return it as it was. No memory, no luck to blame: only the search.

---

## Components

- The **36-card** master deck (9 symbols, every pair on exactly one card). No markers, no tokens: a flipped card is tracked by **turning it sideways**, like tapping — the cards themselves keep score.

## Setup

Shuffle, flipping random chunks. Deal all 36 cards face-up in a rough 6×6 spread, all straight (portrait). Sideways means flipped, so everything starts straight.

## What you're building

A **trio** is the three cards connecting three symbols — Crown/Moon, Moon/Key, Key/Crown — arranged to show all three symbols: Crown, Moon, Key. Three cards, three different faces, a closed ring. (Check any claimed trio by examining the cards: the three hidden faces must be the same three symbols again. If they are, it's real — there are no impostor trios.)

The deck's mathematics guarantee the full deck always sorts into **12 trios** — that's the almanac.

## How to play

Rearrange cards freely — sliding and regrouping costs nothing. Examine any card freely — **return it exactly as found** (same face, same rotation). When you need a card's *other* face in a trio, **flip it and set it down sideways** (rotated 90°). Sideways cards stay sideways; that's the mark of a flip. Change your mind? Flip it back and straighten it — no harm done, only the final state counts.

**Forming trios:** when three cards make a valid trio, push them together and slide the group to the edge of the spread — your growing almanac row. Set-aside trios are **never locked**: pull one apart and return its cards to the spread whenever you like. (You will. The third trio you set aside is often the one strangling the last three.)

You're done when you **declare the trial complete**: all 36 cards sit in 12 valid trios, each showing three different symbols.

**Your score is the number of sideways cards.** Lower is better.

A useful theorem while you work: any trio you've chosen is either already perfect as dealt, or fixable by flipping **exactly one** of its three cards — never two. If you're flipping twice inside one trio, there's a better trio.

## Tiers

| Sideways cards | Result |
|---|---|
| ≤ 4 | **Master of the Almanac** |
| 5 | Gold |
| 6–7 | Silver |
| 8–9 | Bronze |
| 10+ | The almanac kept its secret |

*Honesty note: the perfect deal barely exists — across thousands of simulated shuffles the true optimum averaged just over 5 flips, and no deal allowed zero. Master tier means you matched a computer searching all 840 possible almanacs roughly one deal in three.*

## Modes

### Solo
As above. For a pure no-luck challenge, **replay the same deal**: the sideways cards mark exactly what you changed, so you can restore the original deal perfectly (flip each sideways card back and straighten it) and try to beat yourself.

### Duel (2 players, zero luck)
Deal once. Player 1 solves while Player 2 watches (or times them); record the flip count, **restore the deal** using the sideways markers, and swap. Lower flip count wins. Identical information, identical deal — the purest skill contest in the collection.

### Round the Table (co-op, 2–5)
One shared spread, table talk open, but flips are rationed: the table has a shared budget of **6 flips** (5 for veterans). Make the almanac or bust. A relaxed puzzle-night mode.

### First Trial (tutorial, one play)
The collection's reference card prints **one** almanac — 12 trios in 4 "seasons" of 3, each season using all nine symbols once. Sort the deal into *exactly those* printed trios, flipping where needed. There's nothing to search for, so it isn't the real game — but ten minutes with the printed almanac teaches the trio shape, the one-flip law, and why the real game is about *choosing* almanacs: the printed one will cost you around 9 flips, and the freedom of all 840 is how you get to 5.

## Strategy notes (read after your first trial)

- **Hunt rings, not pairs.** Two cards showing Crown and Moon tempt you to find "the Key cards" — but the question is whether Moon/Key and Key/Crown are *showing* Moon-Key-Crown's ring already. Read what's dealt before imagining what could be.
- **Perfect trios first, but loosely.** Locking the dealt-perfect rings early feels great and is usually right — but the deck has 840 different almanacs, and the third perfect trio you lock can strand the rest. If your last few trios all need flips, unpick one early lock.
- **One flip per trio is the law.** Count your planned flips as planned trios-needing-help. Five problem trios = five flips. The skill is choosing the almanac with the fewest problems, not fixing problems cheaply.
- **Symbols appear on 8 cards each.** A symbol showing far more or less than 4 times in the deal is where your problem trios will cluster — start your search there.

---

*Design v1.1 — score tiers set by exact computer search of all 840 almanacs over thousands of deals; see `TWELVE_TRIALS_design_analysis.md`. Designed under the OUROBOROS post-mortem rules: open information, no hidden-face memory, luck answerable by replay. v1.1 (designer review): flip marker changed to sideways rotation, trio set-aside made explicit, printed-almanac tutorial added.*
