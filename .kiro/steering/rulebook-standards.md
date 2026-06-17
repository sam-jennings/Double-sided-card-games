---
inclusion: fileMatch
fileMatchPattern: '*rulebook*'
---

# Rulebook Writing Standards

How to write and edit player-facing rulebooks. The benchmark is `Trigon/TRIGON_rulebook.md` — match its structure, tone, and physical clarity.

## House structure

In order:

1. **Title + one-line banner** — players · time · ages (e.g. *"for 2–4 players · ~15–25 minutes · ages 10+"*).
2. **Flavour hook** — one short paragraph naming the fantasy and the core action. Pronounce unusual titles.
3. **Components** — always restate the deck honestly: *36 double-faced cards, 9 symbols, every pair once, each symbol on 8 cards.* Name what the player needs mid-game.
4. **Setup** — numbered. For any game needing randomised faces, **explicitly tell players to randomise which face is up** while shuffling (there is no back). State the deal/grid and divisibility ("2/3/4 players get 18/12/9 turns").
5. **Turn overview / core loop** — numbered steps a player repeats.
6. **Subsystems** — abilities, scoring triggers, special actions, in their own sections with tables.
7. **Game end & scoring** — win condition, then tiebreakers as an ordered list.
8. **Edge cases & FAQ** — Q&A covering the corner cases play will actually hit.
9. **Strategy notes** — labelled "read after your first game".
10. **Card manifest** — the full 36-card pair list, where relevant.
11. **Designer's variants** — first-game/lighter and harder/meaner options.
12. **Version footnote** — e.g. *"Design v1.2 — balanced over ~23,000 simulated games."*

Not every game needs every section, but follow this order for the ones it has.

## Physical-clarity rules (non-negotiable)

Because of the no-back deck (see `physical-handling.md`):

- Never say "face-down" to mean hidden. State precisely **which face shows** and **what stays hidden and how** (in hand, palmed, behind a screen).
- For any hidden information, the rulebook must say **how the physical handling actually conceals it**, and whether players may inspect their own cards' other faces.
- Make required state **visible**. If a rule needs tracking, point to the visible thing that records it (an oriented row, a dimmed card, the morgue).
- Spell out **how the table verifies legality** without memory ("the played row shows every claim so far").
- Declare the **symbol subset** up front if the game uses fewer than 9 ("use symbols 1–7; remove every card showing 8 or 9").

## Voice & formatting

- Direct, second-person, warm but concise. Short sentences. Match the existing rulebooks' tone.
- Use **bold** for the first mention of a defined game term, then use it consistently.
- Use tables for anything enumerable (symbol abilities, deal sizes, rank orders).
- Use a worked example (a short indented walkthrough) for any subsystem with timing/chaining subtlety.
- Bracket flavour vs. rules clearly — flavour in italics/intro, rules in plain imperative text.

## Quality bar before a rulebook is "done"

- A new player can reach first-turn play from the rulebook alone.
- Every corner case a careful reader can invent is answered (or knowingly deferred to FAQ).
- No rule silently assumes ordinary-card conventions.
- Terminology is consistent across the rulebook and with the rest of the collection.
- First-game flow is gentle; a lighter variant exists if the base game is sharp.
