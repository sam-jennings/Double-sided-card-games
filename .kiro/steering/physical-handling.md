# Physical Handling of Double-Faced Cards

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
- **Constantly-needed, low-payoff state on the hidden/down face.** If a game makes players *repeatedly* consult a buried face just to function — with no real decision riding on it — put that state somewhere visible. (This was the *fixable* part of what sank OUROBOROS: the "open symbol" lived under the serpent's head as **involuntary overhead** — orienting the end card so the open symbol shows resolves it cleanly, the CROSSROADS technique. Note this defect is distinct from a deliberate memory game.) This is **not** a ban on hidden-face memory itself — see below.
- **Involuntary hidden-face bookkeeping.** Don't force players to *constantly* re-track faces as pure overhead, especially when rechecking is awkward and nothing interesting rides on it. A game whose *point* is remembering or deducing the hidden face is a different thing — that's a feature, not this anti-pattern.

## Handling techniques that *do* work

These have been validated or designed-around in the collection:

- **Open / perfect information.** Everything visible; skill is in reading it (CROSSROADS, TWELVE TRIALS).
- **Symmetric information split via a held fan.** A fan shows you one face and the table the *other* — genuine, free, symmetric hidden information, but only with a strict no-self-inspection rule (JANUS).
- **Public oriented registries.** Played cards laid in an oriented row form a self-recording history that the table can re-read instead of memorising (FALSE FACE, UNPLAYED PAIR's morgue, trick-end reveals).
- **Palms-commit / simultaneous reveal** instead of face-down commitment (THE COUNCIL).
- **Claim-and-challenge.** The hidden face becomes verifiable on demand by flipping; the bluff lives in the gap, and pair-uniqueness bounds the lie-space (FALSE FACE, FACE VALUE).
- **Orientation as state.** Which way a card points (or whether it's dimmed/rotated) is a visible, glanceable state marker (CROSSROADS roads and Signal Fires).
- **Hidden-face memory / deduction as the core challenge.** When remembering or deducing the pressed face *is* the game (not incidental bookkeeping), the deck is well-suited to it — the public pair-registry bounds what's knowable and rewards counting. Keep the memory load deliberate and roughly symmetric across players, and give the table a way to verify on demand (a flip, an end-of-round reveal).

## Default bias

When in doubt, prefer **visible state, public history, and legally-deducible information** over hidden-card conventions imported from ordinary decks. This deck rewards deduction and counting; lean on those by default. Deliberate hidden-face memory is a valid choice when it *is* the point of the game — just make it a chosen challenge, not involuntary overhead.

**Caveat on this bias — it has been over-applied.** Nearly every game in the collection now advertises "no hidden-face memory" as a virtue (TURNOVER killed its back-memory chain, THE UNPLAYED PAIR converted its hidden-rank rule to a public reveal, FALSE FACE / FACE VALUE / BLIGHT all engineer memory out). The default-to-visible bias is correct for *involuntary* state, but it has crowded out a legitimate, deck-native genre. A deliberate, verifiable, roughly-symmetric **memory game is currently a gap worth filling**, not a risk to avoid.
