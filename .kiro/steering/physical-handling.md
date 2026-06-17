# Physical Handling of Double-Faced Cards

> **Primacy.** This note is part of the project's binding steering set in
> `.kiro/steering/`. Treat these notes as the **primary reference** for all
> design decisions and defer to them over any other document. When you apply
> guidance from here, **cite the specific steering note** you are relying on.

> **This is the centre of the project.** Every rule must survive the physical reality of a card with two faces and no back. Most design failures on this deck are handling failures, not maths failures.

## The hard physical facts

1. **There is no card back.** If a card is on the table, **one of its two faces is showing** — there is no neutral "face-down" state. The other face is hidden only in the sense that it is pressed to the table or angled away.
2. **A card on the table shows exactly one symbol to everyone.** That symbol is fully public. You cannot place a card "face-down" to hide *all* its information — you can only choose *which* of two symbols to expose.
3. **A held card can usually be inspected on both faces** by the holder, unless a specific, enforceable handling rule prevents it. Players naturally see both sides of cards in their hand.
4. **Flipping changes which symbol is active** — it does not conceal or reveal a hidden token; it swaps which public symbol is shown.
5. **The hidden face is recoverable by anyone who saw it.** If a card was ever shown or its other face was ever visible, that information is *deducible*, not secret. Memory and the public pair-registry make "hidden" faces semi-public over time.

## Mandatory checklist for every proposed rule

Before accepting any rule, answer all of these explicitly:

- **What can each player physically see** right now?
- **What can each player inspect freely** (their hand, the table, a pile)?
- **What is supposed to be hidden** — and *is it actually hidden* given double-faced cards?
- **Is any required game state visible**, or is it awkwardly buried under a card / on a down face?
- **Can the table verify legality** without relying on memory?

If a rule fails any of these, redesign it or flag it as a handling bug (see `design-principles.md`).

## Anti-patterns — do not propose these casually

- **Face-down cards / hidden decks / card backs.** There is no back. A "face-down" card still shows a symbol. Don't borrow normal-card conventions.
- **Secret commitments via face-down placement.** You cannot hide both faces by placing. Use a different concealment mechanism (held in hand, palmed, behind a screen) and prove it actually conceals.
- **Hidden hands that the holder can't help seeing.** If concealment depends on a player *not* looking at their own card's other face, it is fragile. JANUS makes this work only with an explicit, policed "never inspect your own face" rule — treat that as the exception that proves the cost.
- **Constantly needed state on the hidden/down face.** Any state players must track repeatedly must be **visible**. (This sank OUROBOROS: the "open symbol" lived under the serpent's head.)
- **Hidden-face memory burden.** Don't require players to remember faces the physical state makes annoying to recheck. Prefer open information, public registries, and exact deduction.

## Handling techniques that *do* work

These have been validated or designed-around in the collection:

- **Open / perfect information.** Everything visible; skill is in reading it (CROSSROADS, TWELVE TRIALS).
- **Symmetric information split via a held fan.** A fan shows you one face and the table the *other* — genuine, free, symmetric hidden information, but only with a strict no-self-inspection rule (JANUS).
- **Public oriented registries.** Played cards laid in an oriented row form a self-recording history that the table can re-read instead of memorising (FALSE FACE, UNPLAYED PAIR's morgue, trick-end reveals).
- **Palms-commit / simultaneous reveal** instead of face-down commitment (THE COUNCIL).
- **Claim-and-challenge.** The hidden face becomes verifiable on demand by flipping; the bluff lives in the gap, and pair-uniqueness bounds the lie-space (FALSE FACE, FACE VALUE).
- **Orientation as state.** Which way a card points (or whether it's dimmed/rotated) is a visible, glanceable state marker (CROSSROADS roads and Signal Fires).

## Default bias

When in doubt, prefer **visible state, public history, and legally-deducible information** over hidden-card conventions imported from ordinary decks. This deck rewards deduction and counting; it punishes hidden-face memory.
