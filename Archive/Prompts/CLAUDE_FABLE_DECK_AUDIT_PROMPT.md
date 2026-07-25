# Prompt for Claude Fable: Deck-Wide Bug Audit

> **Completed prompt, retained as provenance.** Its requested audit was carried out; this is not current project guidance.

You are auditing a card game project as a **system**, not a set of isolated games. Read `flip_card_project_goals.md` first for the core premise: one 36-card deck (9 symbols, every pair appears exactly once, no card back — one of the two symbols is always face-up), and a growing collection of games built on top of it (see `NEW_GAME_CONCEPTS.md`, `COLLECTION_OVERVIEW.md`, and the per-game folders: Blight, Cairn, Crossroads, Face Value, Forked Tongue, Glean, Janus, Ouroboros, Relay, Sleeper, The Council, The Orrery, The Unplayed Pair, Trigon, Turncoat, Twelve Trials).

Then read `DECK_PLAYTEST_FINDINGS.md` in full. It documents nine confirmed cross-game bugs (F1–F9) — things like "no natural hand-sort order," "dealing leaks a face to the table," "no way to have a concealed draw deck," "orientation-as-state breaks when cards move," "draw deck and discard pile look identical." These are not bugs in any single game's rules — they are consequences of the deck's physical properties (no back, fixed orientation marker, sign=rank) interacting with different games' needs. Also skim `Lauren and Arran Playtest.md`, `NAMING_REVIEW.md`, and any `*_playtest*.md` files inside individual game folders for additional session notes that may contain findings not yet promoted into F1–F9.

## The actual problem I need you to solve

Every individual game I playtest turns up an issue, and in isolation each one has an easy game-specific fix (add a token, reword a rule, change hand size). But I keep noticing that fixes proposed for one game create, worsen, or contradict a convention needed by another game — because they all share the same physical deck. Examples of the tension already on record:
- A deck-cover/sleeve solves F7 (concealed draw deck) for JANUS, but is "an extra component" the project has otherwise avoided (see the no-game-specific-components preference noted in F8).
- Orientation-as-state (F6) works for CROSSROADS/TRIGON but fails for TWELVE TRIALS — so any deck-wide convention about what rotation *means* has to hold for both "placed and left" and "picked up and regrouped" games simultaneously.
- Pip placement (F2) was resolved to top-left corner, but that decision has to keep working for every game's rotated states, not just the games that motivated the change.
- Dealing/drawing conventions (F3, F7, F9) need one answer that every game can rely on, not sixteen different table conventions.

## What to do

1. Read every game's rules/spec file and every playtest note (not just DECK_PLAYTEST_FINDINGS.md) to build your own list of bugs, ambiguities, and rule inconsistencies — both the ones already logged as F1–F9 and any new ones you find by close reading (contradictions between a game's rules and the deck's physical constraints, rules that assume a card back exists, rules that assume independent suit/rank axes, rules that assume silent/simultaneous reveal that the deck can't support, etc.).
2. For each issue, classify it as: (a) truly game-local (fits one game, fix it there without touching anything else), or (b) deck-wide (touches the physical deck, a shared handling convention, or the core symbol/rank/orientation model, so any fix ripples into other games).
3. For every deck-wide issue, don't propose a fix in isolation — check it against every other game in the collection that touches the same mechanic (hand size, orientation, dealing, drawing, discarding) and confirm the fix doesn't break, contradict, or degrade one of them. Where two games genuinely need contradictory conventions, say so explicitly rather than picking one silently.
4. Propose concrete fixes: rule wording changes, a deck-wide handling/convention section (e.g. one canonical dealing method, one canonical discard/draw distinction, one canonical rotation-as-state contract), or specific per-game rule edits. Where you're confident and the fix is clearly local and non-breaking, make the edit directly in the relevant file. Where a fix is deck-wide, propose it in a new or updated section of DECK_PLAYTEST_FINDINGS.md (or a new DECK_CONVENTIONS.md if that's cleaner) rather than scattering the same convention across every game file, and only apply it to individual game files once it's settled.
5. Finish with a prioritised punch list: which issues are blocking (a game can't be played correctly as written), which are quality-of-life, and which are genuinely open design tensions with no single right answer yet.

Keep the deck's identity intact — the goal is one coherent system all the games share, not sixteen games that each patched around the deck differently.
