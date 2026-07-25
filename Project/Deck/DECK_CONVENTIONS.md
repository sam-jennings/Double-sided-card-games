# Deck Conventions

*One canonical set of handling conventions for every game in the collection. Written July 2026 from the deck-wide audit (see `DECK_BUG_AUDIT.md`). Rationale and evidence live in `DECK_PLAYTEST_FINDINGS.md` (F1–F12); this file states only the rules of the house.*

*Each convention is marked **Settled** (already true in every rulebook, codified here), **Proposed** (checked against every game, no contradictions found, awaiting adoption), or **Open** (a genuine design tension — do not silently pick a side).*

**Why this exists:** every game keeps rediscovering the same physical facts (no back, one face always showing, sign = rank), and per-game patches have started to contradict each other. Any fix that touches dealing, drawing, discarding, orientation, or concealment must be checked here first, then applied per game — never invented per game.

---

## C1 · Shuffling — **Settled**

Shuffle by **flipping random chunks** so which face lands up is randomised. Already worded identically in every rulebook. Never change this phrasing per game.

## C2 · The information ladder for deals and draws — **Proposed**

The physics: **any card leaving the top of a squared stack has already shown one face to the whole table** (F7), and **any card lying on the table shows one face to everyone, including its future owner** (F3). No wording can change this; games choose a rung on the ladder instead:

| Rung | Method | What leaks | Use when |
|---|---|---|---|
| 1 | **Open deal** — deal flat in front of each player, scoop up | Table glimpses one face of each dealt card | Open-info games, and hand games where the glimpse is low-value (WILDFIRE, GLEAN, BLIGHT, TRIGON, TURNCOAT) |
| 2 | **Self-deal** — squared stack passed round; each player takes their own cards straight into hand | Only the deck-top face at each moment (seen by all, owned by the taker) | Hidden-commitment hand games (FORKED TONGUE, FACE VALUE, THE COUNCIL) when the table wants tighter concealment |
| 3 | **Blind Cut** — take the deck below the table edge (or behind cupped hands), cut it, slide the new top card off unseen; return the deck | Nothing — the previously-public top face is buried by the cut | Any **one-off secret card**: SLEEPER's loyalty deal, THE UNPLAYED PAIR's removal (or slide a card from the middle of the squared deck, edges only) |
| 4 | **Opaque container** — deck sits inside the box base / a bag / a sleeve; draw blind from inside | Nothing, repeatedly | The only method that supports **repeated concealed draws** (JANUS) — see Open tension T1 |

Rungs 1–3 are deck-native and component-free. Rung 4 is the one concealment the deck cannot do by itself.

**Deck-wide law (F10):** a rule may never say "draw/remove a card unseen" without naming the rung that makes it physically true.

## C3 · Live stacks vs dead piles — **Proposed**

Two face-up squared stacks are indistinguishable (F9). House rule, checked against every game with no collisions:

- A **live** stack (draw deck, stock, well, Court deck) sits **upright**, squared.
- A **dead** pile (removed pile, spent pile, any discard that is out of the game) sits **rotated 90° sideways**, squared, in its own spot away from the live stack.
- A pile that must be **read as history** is never squared — it is an **overlapping cascade or row** (FORKED TONGUE's ledger, WILDFIRE's pile), because a squared stack shows only its top card.

Games this touches: TRIGON (removed pile), TURNCOAT (removed pile), SLEEPER (spent pile), WILDFIRE (pile = cascade, well = live stack). No game uses sideways *piles* for anything else, so the meaning is unambiguous.

## C4 · Orientation-as-state — the contract — **Settled principle (F6)**

Rotation is reliable state **only for cards that are placed and left** (CROSSROADS dimming, OUROBOROS scars, BLIGHT's penalty-face-up pile, the C3 dead-pile mark). It is **not valid** for cards that are repeatedly picked up and regrouped (TWELVE TRIALS' failed sideways flip-mark).

Namespace rule so meanings never collide: **sideways on a squared pile always means "dead" (C3); sideways on a single placed card means whatever that game declares, and each game must declare it.** Current declarations: CROSSROADS = dimmed city; TWELVE TRIALS = flipped (being replaced, F12); OUROBOROS = scar; proposed TRIGON = anonymous Moon-taken card in a score pile.

## C5 · Flip tallies in regrouping games — **Proposed (F12)**

Where flips must be counted but cards keep moving (TWELVE TRIALS, THE ORRERY): use the **sanctioned generic counter kit** (any small objects — the same house kit JANUS's omens and THE COUNCIL's Speaker token already draw on): take one counter per flip. If a mode must also record *which* cards were flipped (TWELVE TRIALS' restore-the-deal replay), place the counter **on** the card and lift it only when the card is restored. Orientation-marking stays legal for games where cards sit still.

## C6 · Score piles and public registries — **Proposed**

Default: captured/won/dead cards lie in a **face-up spread, both faces examinable by anyone at any time, returned exactly as found** (GLEAN's harvest, FORKED TONGUE's registry, FACE VALUE's morgue and tallies, THE UNPLAYED PAIR's morgue and won tricks). Use the same sentence in every rulebook: *"anyone may pick up and examine any card here, both sides, at any time — return it as found."*

Declared exceptions (each earns its deviation): BLIGHT's rot pile is **orientation-encoded** (penalty face up, self-totalling); TURNCOAT's score pile is an **ordered squared stack** (Moon reads the top; keep banking order); TRIGON's Moon-taken cards are **sideways = anonymous**.

## C7 · Teaching canon — **Settled (F4)**

Before any rank-sensitive game (GLEAN, BLIGHT, FACE VALUE, THE UNPLAYED PAIR, THE COUNCIL), say aloud: *"There are 9 signs. Each sign has one fixed strength — Crown is always 9, Moon is always 1. Every card pairs two different signs, so it always has two different strengths, one per face."* GLEAN and BLIGHT print this callout; add it to any new rank game.

## C8 · Hand-size comfort — **Settled guidance (F1)**

There is no natural sort order and the both-faces re-scan repeats every turn, so **hand size is the dominant comfort lever**. Table-tested: 14 overwhelming, 12 heavy, 9 manageable. When a game offers a player-count or variant choice, teach at the smaller hand first; new designs should justify any starting hand above 9.

## C9 · Table space — **Settled guidance (F5)**

Open-layout games (TWELVE TRIALS, THE ORRERY, CROSSROADS, TRIGON/TURNCOAT) must say "needs a large table" in their rulebooks and may define workspace zones. Not a defect; a footprint fact.

---

## Compatibility matrix

Checked July 2026 — each proposed convention against every game that touches the mechanic. ✓ = compatible as written · — = not applicable.

| Game | C2 deal rung | C3 piles | C4/C5 orientation & tallies | C6 registries |
|---|---|---|---|---|
| TRIGON | 1 | ✓ removed pile sideways | ✓ Moon-sideways proposed | ✓ (score pile) |
| TURNCOAT | 1 | ✓ removed pile sideways | ✓ none | ✓ ordered-stack exception |
| WILDFIRE | 1 | ✓ pile = cascade, well = live | ✓ none | ✓ |
| GLEAN / BLIGHT | 1 (2 optional) | — | ✓ BLIGHT penalty-face-up | ✓ / declared exception |
| CROSSROADS | 1 | — | ✓ dimming (placed-and-left) | ✓ |
| TWELVE TRIALS | — | — | **C5 counters replace sideways** | ✓ |
| THE ORRERY | — | — | **C5 counters (rulebook had no method)** | ✓ |
| OUROBOROS | — (solo; stock top public = fair info) | — | ✓ scars (placed-and-left) | — |
| CAIRN | — (stock top public = the free look, by design) | — | ✓ none | — |
| JANUS | **4 required — unresolved (T1)** | — | ✓ none | ✓ archive |
| FORKED TONGUE | 1–2 | ✓ ledger = cascade | ✓ none | ✓ registry |
| FACE VALUE | 1–2 | — | ✓ flat concealment | ✓ morgue/tallies |
| THE COUNCIL | 1–2 | — | ✓ palms-commit | ✓ discard row |
| SLEEPER | **3 for the loyalty card** | ✓ spent pile sideways | ✓ one guarded flat card | ✓ Court row |
| THE UNPLAYED PAIR | 1, removal via 3 | — | ✓ none | ✓ morgue/won tricks |
| RELAY (concept) | open market — face-up by design | — | ✓ aimed roads | ✓ score piles |

No convention above contradicts any shipped rule. The unresolved cells are listed below, not papered over.

---

## Open tensions — decisions the conventions cannot make

**T1 · JANUS concealment vs the no-components identity.** JANUS needs rung 4 (opaque container) for *both* its deal and its refills — no deck-native method lets a holder receive a card without either the holder or the table seeing a face. Options: (a) the **game box itself** as the draw container (arguably free — every copy owns a box; prototype: a mug or envelope); (b) a cloth **bag** (new component class, currently justified by one game — fails the reuse bar); (c) **redesign JANUS with no draw deck** (deal everything at setup via a screen/box moment; most deck-honest, changes pacing, needs re-sim). Blocking for JANUS (F7). *Not chosen here.*

**T2 · Reference cards vs deck-only.** TRIGON's reference overhead (playtest Bug 2) begs for per-player sign references; the component policy resists bespoke pieces. Middle paths: a tear-out/back-page shared reference in each rulebook, or one **generic Nine Signs reference** (sign + pip + archetype verb) reused by TRIGON, TURNCOAT and any future ability game — which the graduated policy would permit if genuinely shared. Related pending decision: the SIGN_MNEMONICS Leaf/Key relabel (balance-neutral, unapplied).

**T3 · TWELVE TRIALS' restore-the-deal modes.** C5 counters fix the tally but the Duel/replay modes also need *which cards* flipped; counter-on-card works but is untested. If it fails at the table, the replay modes may need a written note instead — or to be cut.

**T4 · Open registries vs the memory game.** GLEAN's playtest found players *missing* the memory skill (public harvests "feel wrong"); the steering separately flags a deliberate memory game as an under-served target. The C6 default stays open-registry, but Closed Harvest-style variants are the sanctioned outlet — don't resolve this per game in contradictory directions.

**T5 · CROSSROADS v1.2 pending.** Deal-9 + Toll-in-base + 2–4P are **decided** (design analysis §6–7) but deliberately unapplied while the end trigger (Phase 3) is open. The rulebook currently contradicts the settled decisions; that is tracked in `Crossroads/CROSSROADS_tasks.md` Phase 6, banner added to the rulebook. Don't cite the v1.1 rulebook as current design intent.
