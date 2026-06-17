# THE ORRERY

*A solo / co-operative sorting puzzle for 1–3 players · ~15–25 minutes · ages 10+*

The sky is wrong. The symbols rise in clumps, vanish from whole circles, and repeat where they should not. Rebuild the machine: four perfect orbits, each carrying every symbol once above and once below. Move cards as much as you like. Every **flip** is the cost.

---

## Components

The **36-card** master deck: 9 symbols, every possible pair appearing exactly once.

The standard game uses all 9 symbols. The short game uses any 7-symbol sub-deck: remove every card showing either of the other two symbols on either face, leaving 21 cards.

No tokens are required. Paper helps for scoring, but is not necessary.

---

## Core idea

In the 9-symbol game, you are trying to divide the 36 cards into **four orbits** of 9 cards each.

An orbit is correct when:

1. Its **visible faces** show all 9 symbols exactly once.
2. Its **hidden faces** also contain all 9 symbols exactly once.

That's it. An orbit is a **balanced group** — every symbol appears once above the table, once beneath it, and no card is wasted. The cards within an orbit do not need to connect into a single chain or loop. They may form one cycle, two smaller cycles, or any internal arrangement — the machine doesn't care about the wiring, only that every symbol is present exactly once on each side.

*(If you want a harder challenge where each orbit must form one unbroken loop, see the Clockmaker variant.)*

---

## Setup

1. Shuffle thoroughly, flipping random chunks as you shuffle so each card's showing face is randomised.
2. Spread all 36 cards face-up in a loose pool. This is the **sky**. The face currently showing is that card's **starting face**.
3. Leave space for four rows of nine cards. These will become the **orbits**.
4. Optional but recommended: count how many cards currently show each symbol. In the 9-symbol game, each symbol must end the puzzle showing exactly **4** times total, because there will be four orbits and each orbit shows every symbol once. The amount by which over-shown symbols exceed 4 is the deal's **sky debt** — a lower bound on the number of flips this deal can possibly need.

Example: if the visible counts are `6, 5, 5, 4, 4, 4, 3, 3, 2`, the excess over 4 is `2 + 1 + 1 = 4`. The sky debt is 4. You cannot solve this deal in fewer than 4 flips.

**Open-information rule:** any player may pick up any card at any time, inspect both faces, and return it to the same showing face. Inspection is free. Changing which face is showing is a flip and must be counted.

---

## How to play

There are no turns.

- Move cards freely between the sky and the four orbit rows.
- Reorder cards within an orbit freely; left-to-right order has no meaning in the base game.
- Inspect both faces of any card freely, as long as you return it with the same face showing.
- Whenever you turn a card over so its other face shows, count **1 flip**.

Your aim is to arrange all cards into four complete orbits while spending as few flips as possible.

When you think an orbit is complete, check it:

1. The nine visible faces must be nine different symbols.
2. The nine hidden faces must also be nine different symbols.

If both are true, the orbit is locked. You may unlock it later if you find a better solution, but any flips already spent still count.

---

## Winning and scoring

You win when all 36 cards are locked into four correct orbits.

Your score is the number of flips you spent.

For a fairer rating, compare your flips to the deal's **sky debt**:

| Result | Calibrated score |
|---|---:|
| **Perfect mechanism** | sky debt + 0 |
| **Gold** | sky debt + 1–2 |
| **Silver** | sky debt + 3–4 |
| **Bronze** | sky debt + 5–6 |
| **The sky turns, grudgingly** | sky debt + 7 or more |

The sky debt is only a lower bound, not a promise. Some deals may require extra flips even with perfect play. That uncertainty is part of the puzzle until an exact solver exists.

For a first untimed game, ignore the rating and just solve the sky. Then replay the same deal and try to cut two flips.

---

## Why it belongs to this deck

Treat each symbol as a point and each card as the unique road between two points. THE ORRERY asks you to orient and sort those roads into four balanced directed systems: in every orbit, each symbol has exactly one visible arrival and one hidden departure.

The deck guarantees this kind of structure exists. One fixed emergency solution is shown below. The puzzle is not whether the sky can be repaired; it is how close you can get to the best repair for this particular shuffle.

This is the sibling of TWELVE TRIALS, not a replacement for it:

- TWELVE TRIALS sorts the deck into twelve perfect **triangles**.
- THE ORRERY sorts the deck into four complete **orbits**.
- Both are open-information flip puzzles.
- Both turn the all-pairs deck into a search space of possible decompositions.
- THE ORRERY adds a visible global lower bound — the sky debt — so each deal tells you how many flips are unavoidable before you start.

---

## The emergency almanac

Do not use this while solving unless you are stuck. It proves the full 9-symbol deck can always be divided into four legal orbits.

Number the symbols 1–9 by their pips. Each line below is one orbit. Use the card for each adjacent pair, including the final pair that loops back to the start.

1. `9 – 1 – 2 – 8 – 3 – 7 – 4 – 6 – 5 – 9`
2. `9 – 2 – 3 – 1 – 4 – 8 – 5 – 7 – 6 – 9`
3. `9 – 3 – 4 – 2 – 5 – 1 – 6 – 8 – 7 – 9`
4. `9 – 4 – 5 – 3 – 6 – 2 – 7 – 1 – 8 – 9`

For example, the first orbit uses the cards `9/1`, `1/2`, `2/8`, `8/3`, `3/7`, `7/4`, `4/6`, `6/5`, and `5/9`.

To orient an orbit, choose a direction around the line and make each card show the next symbol in that direction. The visible faces will contain all nine symbols exactly once, and the hidden faces will also contain all nine exactly once.

This almanac gives a legal solution. It is almost never the best solution for the deal in front of you.

---

## Edge cases & FAQ

**Can I look at hidden faces without paying a flip?**  
Yes. This is an open puzzle. Pick up the card, inspect both faces, and put it back exactly as it was. Only changing the showing face costs a flip.

**Do the rows need to be in a specific order?**  
No. An orbit is just a set of nine cards. Row order is only for readability.

**Can a valid orbit contain split cycles?**  
Yes. In the standard game, an orbit only needs every symbol once visible and once hidden. If you treat each card as an arrow (visible → hidden), the arrows might form one big loop through all nine symbols, or two smaller loops (say a 4-cycle and a 5-cycle), or even three. All of these are valid standard orbits.

*Example (7-symbol Apprentice):* Suppose an orbit's cards produce the arrows A→F, F→B, B→D, D→A and G→C, C→E, E→G. That's a 4-cycle (A–F–B–D) plus a 3-cycle (G–C–E). Every symbol appears once as a visible face and once as a hidden face — orbit complete.

**If an orbit shows all nine symbols, is it automatically correct?**  
No. Its hidden faces must also contain all nine symbols. A row can look perfect on top and still have two hidden Moons and no hidden Key.

**Can I flip a card twice?**  
Yes, but both flips count. In good play this should almost never be necessary.

**Can I move a locked card?**  
Yes. Locking is only a declaration that the row currently passes. If you later see a better global arrangement, unlock it. The puzzle is cooperative, not procedural.

**Does the 7-symbol game work the same way?**  
Yes. Use 21 cards and make **three** orbits of 7 cards. Each orbit must show every symbol once and hide every symbol once. The global target is 3 visible cards per symbol, so calculate sky debt against 3 instead of 4.

**Does this work with 6 or 8 symbols?**  
Not cleanly. The orbit structure wants an odd number of symbols: 5, 7, or 9. Six- and eight-symbol versions need a dummy bye symbol or a different target structure, so they are not part of the standard rules.

---

## Strategy notes

- **Balance the sky before sorting too hard.** If one symbol is showing 7 times and another is showing once, no orbit layout can survive. Your first flips should usually reduce visible-count debt.
- **Build by shortages, not favourites.** A row missing hidden Crown does not need “a Crown card”; it needs a card whose *other* face is Crown while its visible face fills a visible gap in that same row.
- **Visible perfection is only half a solve.** Four rows can each show all nine symbols while their hidden faces are a mess. Check undersides early, not after everything looks beautiful.
- **Swap before flipping.** If two orbits each have a duplicate hidden symbol, the answer is often a clean exchange, not another flip.
- **Use the emergency almanac as a teacher, then stop using it.** It shows what a complete sky looks like, but leaning on it turns the puzzle into bookkeeping instead of search.

---

## Variants

### Apprentice Orrery

Use any 7 symbols: 21 cards, three orbits of 7 cards, target count 3 per visible symbol. Faster, less intimidating, and probably the best first play.

### Pocket Orrery

Use any 5 symbols: 10 cards, two orbits of 5 cards, target count 2. This is mostly a teaching exercise; experienced players will solve it quickly.

### Clockmaker (prestige challenge)

A separate, harder puzzle layered on top of a completed standard solve. **Do not attempt Clockmaker until you are comfortable solving the standard game.**

In Clockmaker, a locked orbit must not merely show and hide every symbol once — it must also form **one single cycle** through all symbols.

To test this: treat each card in the orbit as an arrow from its visible symbol to its hidden symbol. Pick any symbol and follow the arrows. A Clockmaker orbit is valid only if you visit every symbol exactly once before returning to the start.

A standard orbit may contain split cycles (a 4-cycle and a 5-cycle, for example). Clockmaker forbids that — every orbit must be one unbroken loop. This is significantly harder than the standard game: converting a valid standard solution into four full cycles is a global rearrangement problem, not a quick tidy-up. Expect to need many more flips, and expect some deals to resist Clockmaker solutions entirely.

**Scoring Clockmaker:** use the same sky-debt-relative tiers, but treat any successful Clockmaker solve as a victory regardless of flip count. The challenge is completion, not optimisation.

### Silent Observatory

Co-op with restricted communication. Players may freely discuss visible counts and public shortages, but may not name a specific card another player is holding or moving. Less efficient, more meditative.

---

## Open playtest questions

*Updated after playtest 01. Questions answered or superseded are struck.*

1. ~~Is base THE ORRERY satisfying once players understand the visible/hidden double-check, or should Clockmaker become the standard rule?~~ *Answered: standard is satisfying; Clockmaker is prestige only.*
2. Does calculating sky debt feel clever and fair, or does it slow down setup too much?
3. ~~Is the hidden-face verification acceptable at the table, given that inspection is always legal?~~ *Answered: yes, open information feels completely natural.*
4. Does the emergency almanac help players learn, or does it tempt them into a dull fixed solve?
5. What does a thoughtful first 9-symbol game score relative to sky debt?
6. Does the standard 7-symbol game remain satisfying across multiple random deals?
7. Does the 9-symbol game feel manageable after learning on 7, or does it tip into solver territory?
8. Do split-cycle solutions feel valid and satisfying now that the rules explicitly allow them?

---

*Design v0.2 — terminology clarified after playtest 01: standard orbits explicitly allow split cycles; Clockmaker reframed as a separate prestige challenge. See `THE_ORRERY_playtest_01.md` for the findings that motivated these changes.*
