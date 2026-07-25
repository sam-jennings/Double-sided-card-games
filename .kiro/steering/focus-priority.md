# Focus & Prioritisation

The collection has many games, one designer, and limited table-testing
opportunities. This note offers guidance for **"what should I work on next?"**
— but it is guidance, not a guilt trip. You are free to brainstorm new concepts,
improve a draft, or advance an existing game. The system exists to help you
choose *when you want help choosing*, not to forbid anything.

The live condition of each game — its `state` and `physically_playtested` flag (see
`product-vision.md`), its open questions, its next step — lives in
the YAML properties on its game record and in `COLLECTION_OVERVIEW.md`. For
session logistics, `GAME_CATALOG.md` is the fastest view: start with **All
games** and combine exact player count, min/max players, time, state, depth,
and whether it has been physically played. Read the game record before
applying the guidance below.

## The two modes of work

At any given moment you're doing one of two things:

1. **Advancing a game** — pushing it toward a healthier state
   (writing rules, running sims, preparing a playtest, running a playtest,
   iterating on findings).
2. **Exploring** — brainstorming, sketching new concepts, improving a draft
   you're excited about, revisiting an old idea with fresh eyes.

Both are legitimate. Exploring is how new games enter the collection. Advancing
is how they earn their way into the collection.

## When you want to advance: the priority ladder

Use this when you have a session opportunity (table time, sim time, design
time) and want to spend it efficiently. Work top-down; only skip a rung when
everything on it is blocked or has no actionable next step.

1. **Iterate on your strongest played games with open questions.** Anything
   **Proven**, or **Ready to test** and already physically played, with concrete
   findings and specific next questions. Momentum is cheap to keep.
2. **Take a game to the table.** A single session answers more than another
   thousand sim runs or another rulebook revision. This covers everything
   **Ready to test**: both the *first* test of a game with
   `physically_playtested: false`, and the *re*-test of one that already has
   data pointing at the next session. Within this rung, prefer games testable at
   the player count you can currently field.
3. **Resolve a played game that dropped back to In development.** Don't let a
   game that failed at the table linger unresolved: either schedule the
   redesign/re-test, or shelve it with evidence. A clear decision beats a
   stalled one.
4. **Validate an unvetted rulebook** — sim it, solve it, walk through it deeply —
   to earn a `sim-validated` badge and move it to **Ready to test**.
5. **Develop a concept into a rulebook** — write the rules.

## When you want to explore: the circuit breaker

You don't need permission to brainstorm. But when a new idea arrives, it's
worth a quick sanity check before going deep:

1. **Write one sentence:** what deck property does it exploit?
2. **Check the coverage table:** does an existing game already cover that
   property × genre × player count?
3. If it overlaps heavily → **log it in one line** at the bottom of
   `NEW_GAME_CONCEPTS.md` (Parking Lot) and keep it warm for later.
4. If genuinely novel and gap-filling → write a concept sheet or start
   drafting rules. No gate required.

The point isn't to block new ideas — it's to avoid accidentally re-inventing
something you already have.

## Player count as the logistical constraint

"Can actually test" means you can sit down this week and run a session with the
players you have access to. Solo and 2P games are always testable; 3–4P games
need a willing friend or two; 5–6P games are event-dependent. When planning a
table session, filter by the count you can field.

## Session planning checklist

Before sitting down to work on any game:

- [ ] Read that game's entry in `COLLECTION_OVERVIEW.md` (current state, open
      questions).
- [ ] Read its most recent playtest report or design analysis (if any).
- [ ] Identify the single most important question this session should answer.
- [ ] If it's a table test: write a short playtest plan (per `playtesting.md`).
- [ ] If it's design/iteration work: tie any proposed change to a specific
      observed problem from a prior test.
