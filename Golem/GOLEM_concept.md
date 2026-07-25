---
record_type: game
game: "GOLEM"
state: In development
players: [1, 2]
player_count: "1, 2"
duration: "~20 min"
genre: "Co-op boss fight"
complexity: Medium
min_players: 1
max_players: 2
min_minutes: 20
max_minutes: 20
physically_playtested: false
public_document: "Golem/GOLEM_concept.md"
next_step: "Develop a complete rulebook if this concept is selected."
catalog_order: 26
---
# GOLEM — the boss that telegraphs

*1–2 players · ~20 min · co-operative boss fight vs. a deck-driven automa · In development · physically unplayed*

> **Status & scope.** Wildcard batch, second flight (July 2026) — same brief as the first flight (§18–§22): *originality first, rubric waived, unsimmed*, leaning further into the two moves the first flight proved out: **physical inversions** (a supposed weakness of the backless deck becomes the genre — the WISP move) and **format innovations** (the VIGIL move). No rulebook, no sim, no rubric self-score; should not jump the [focus-priority.md](../.kiro/steering/focus-priority.md) queue on novelty alone. Portfolio index: [NEW_GAME_CONCEPTS.md](../NEW_GAME_CONCEPTS.md) §23.

**The trick that makes it exist.** Automa design fakes intelligence with hidden decks; a backless deck can't hide its next card — so stop pretending. The GOLEM is **readable by construction**: the top of its deck shows the sign it will strike *now*, and the pressed face — revealed on resolution — is the follow-through you learn one beat too late. That is exactly the rhythm of a video-game boss fight (telegraph → commit → punish), which cardboard automas famously can't produce, delivered here for free by the physics of the deck. The players aren't outwitting a mind; they are standing in the right place ahead of a machine they can half-read — and the ICARUS registry turns *fully* reading it into an earnable skill.

**Setup.** Shuffle; the GOLEM takes 18 cards as its blow-deck; the players split the other 18 (solo: 12, rest set aside). Nine **stations** — one per sign — are just labelled table space; all state will be cards piling at them.

**A blow.** The top blow shows sign X (public since last turn — you've had a whole turn to prepare). Resolve: any player may **parry** by playing a hand card containing X, laid at station X showing X (armor — the blow-card goes to the spent pile). Unparried: the blow-card itself lands at station X showing X — a **breach**. Either way, the blow's hidden face Y is now revealed as it moves — the **follow-through**: if station Y already holds a breach, rotate that breach sideways — **critical**. Then the next blow's face is already showing.

**Win / loss.** The wall falls (loss) on a third breach at any one station, or a second critical anywhere. Survive all 18 blows: victory, graded by breaches taken.

**The dilemma engine.** Every hand card is one unique edge — spending {X, Z} to parry X *is* discarding your only Z answer (every-pair-once makes all resources dual-purpose and irreplaceable). You provably cannot defend everything with 18 cards against 18 blows; the game is choosing which walls to lose. And the threat forecast is countable: eight cards per sign across the whole deck, minus what you hold, minus what's spent = a tightening bound on what the GOLEM still has.

**Handling audit.** All state is cards at stations, shown faces and rotations — no tokens, no memory. The only hidden things are the blow-deck's interior (the randomness itself) and hidden hands (standard). Dials: blow-deck size, breach/critical thresholds, hand split.

**Fastest falsification.** Two solo games: if knowing the blow one turn early never changes what you'd have done anyway, the telegraph is decoration and the concept is dead — the whole bet is that foreknowledge without spare resources is agony, not comfort.

---

## Campaign extension for review: THE NINE TRIALS OF THE TENTH (July 2026)

*Same players and chassis · nine bosses in pip order · save = a nine-box checklist · In-development proposal*

> Proposed with the story flight ([NEW_GAME_CONCEPTS.md](../NEW_GAME_CONCEPTS.md) §28–§30) but deliberately **not numbered as its own concept**: it stands or falls with GOLEM's telegraph engine, so review the two together. If GOLEM's falsification test fails, this section dies with it.

**The pitch.** GOLEM as written is one fight; the campaign makes it nine. Each boss is a **mechanisation of its sign's archetype verb**, layered as one rule change on the unmodified base chassis: Moon *drains* (each unparried blow also discards your lowest card), Leaf *regrows* (breaches heal a station but seed the next stratum), Wave *carries* (the follow-through lands at an adjacent station, not Y), Flame *burns* (parry armor goes to the dead pile, not the station), Eye *sees* (parry cards must be declared a turn ahead), Mask *swaps* (each critical flips one stationed card's showing face), Key *extracts* (steals the top armor from a breached station), Star *breaks pattern* (blows resolve from a fanned choice of two — the one automa that isn't fully readable), Crown *commands* (parries must be your highest legal card). Difficulty ladder is just pip order.

**Persistence.** Cards lost to a boss stay out of your 18 for the next fight unless you **rest a chapter** — skipping a trial is a real cost, so the story's pacing decision is a rules decision. Save state is a nine-box checklist plus the wound list: one line of writing, almanac-precedent legitimate.

**Assists.** A second player enters as a **champion of a beaten sign**: they bring that sign's 8 cards as their hand and may invoke its verb (as listed above, turned to your side) once per fight.

**The review question.** Can one chassis express nine genuinely different verbs, or do five bosses feel like reskins? Decision path: if the base game's falsification passes, prototype the two most *structurally* different bosses (Wave and Star) before committing to nine. If those two play like the base game with a coat of paint, cut the campaign and keep GOLEM single-fight.
