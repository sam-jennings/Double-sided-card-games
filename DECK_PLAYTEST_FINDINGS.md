# Deck-Wide Playtest Findings

*Cross-game observations from table testing that affect the deck itself, card layout, or handling conventions shared by multiple games. Updated as new sessions produce general findings.*

---

## F1: Hand ordering — no natural sort order (June 2026, WILDFIRE + GLEAN session)

**Observation:** With 12 cards in hand, players instinctively wanted to sort their hand (the first thing any card player does after a deal). They couldn't find a natural ordering because each card belongs to two "suits" simultaneously. There is no single axis to sort by.

**Impact:** Affects every game with a hand of cards. Especially felt at higher hand sizes (9+ cards). Less of an issue in games with small hands or open tableaux.

**Games affected:** WILDFIRE (9 cards), GLEAN/BLIGHT (6–12 cards), JANUS (variable), FORKED TONGUE, FACE VALUE, THE COUNCIL, THE UNPLAYED PAIR.

**Possible mitigations:**
- Players may develop their own conventions with experience (e.g. group by "the sign I'm trying to collect" or "my strongest hidden pips").
- The shipping deck's sign icons and colours may provide a more sortable visual identity than letter+number prototypes.
- Could suggest a default sort in rules (e.g. "sort by the face you can see; re-sort when your strategy shifts") — but this may be over-prescriptive.
- Corner pips may help (see F2) by making scanning faster, even if sorting remains ambiguous.

**Status:** Observed, no action required yet. Monitor whether this recurs with different players or whether experience resolves it naturally.

**Update (June 2026, Lauren & Arran session) — confirmed and sharpened, now HIGH for large hands.** Recurred forcefully across **three** different games in one session: BLIGHT (12 cards, 3P), CROSSROADS (14 cards, 2P), and felt in TRIGON. Two specifics emerged:
- **The re-scan is per-turn, not one-time.** In BLIGHT, every time a sign is led, each follower must check *both faces* of every card for the led sign, **rotate them all to face the same way**, then choose — and because there's no sort axis, this repeats *every trick*. Sorting once doesn't help.
- **Hand size is the dominant comfort lever.** CROSSROADS at 14 cards was "overwhelming, no idea how to start"; dropping to 9 felt markedly manageable. BLIGHT's 3P (12) is its heaviest config; 4P (9) / 6P (6) should be lighter. **Recommendation:** when a game offers a player-count choice, treat *lower hand size* as a real comfort gain, and prefer testing smaller-hand configs before judging a game too heavy. Watch whether the shipping deck's colour/icon identity makes the per-turn re-scan faster.

---

## F2: Corner pips preferred over top-centre for fan readability (June 2026, WILDFIRE + GLEAN session)

**Observation:** Players commented that corner numbers (like traditional playing cards) would allow instant recognition in a fanned hand. They also noted that flipping a fanned hand while keeping the fan shape would show all reverse-side values quickly — useful for assessing hand strength.

**Current layout:** `CARD_LAYOUT.md` specifies a single top-centre pip. The rationale was: the deck has a defined orientation (top-edge marker), so mirrored corners are redundant and contradict the orientation marker.

**Player argument:** the benefit of corner-fan readability outweighs the covering concern. It is easy to cover an entire card with one hand regardless of pip placement — concealment is achieved by the hand's physical grip, not by where the number sits.

**Tension with current design:** Corner pips could imply "either end can be up" (contradicting the orientation marker). However, a single top-left pip (not mirrored) would serve fan readability without implying reversibility.

**Status:** Resolved (June 2026). `CARD_LAYOUT.md` now specifies a **single, non-mirrored top-left corner pip**, replacing the former top-centre pip. The generators (`compose_cards.py`, `compose_template.py`, `make_card_faces.py`) place the pip top-left. One confirmatory print test remains: verify the corner pip reads faster in a fan than top-centre without harming rotated-state legibility (CROSSROADS, TWELVE TRIALS) or colliding with the orientation marker's left end. See `CARD_LAYOUT.md` → "The pip-position question".

---

## F3: Dealing exposes one face of every card to all players (June 2026, WILDFIRE + GLEAN session)

**Observation:** When dealing cards, everyone at the table can see one face of every card as it's dealt — there is no card back to conceal during the deal. This is inherent to the deck's physical nature.

**Impact by game type:**
- **Open-information games (CROSSROADS, TWELVE TRIALS, THE ORRERY):** No issue — all info is public anyway.
- **Games where both faces of your hand are private (GLEAN, BLIGHT, WILDFIRE, THE COUNCIL, FORKED TONGUE, FACE VALUE):** Dealing leaks one face of every player's hand to the table. Whether this matters depends on whether that information is strategically useful.
- **JANUS (asymmetric information):** Dealing may be most problematic here, since the game's entire conceit is that each side of the table sees a different face. A deal that exposes faces to the wrong player could undermine the information asymmetry.

**Severity assessment:**
- For GLEAN/BLIGHT: both faces of your own hand are known to you (you inspect freely), so the leak is "the table glimpsed one face of your cards during the deal." In a fast deal this is likely forgotten, but attentive players could note that Player A received the Crown/Star card. Whether this matters depends on how much early information changes play.
- For WILDFIRE: probably irrelevant — the game is reactive and fast, and the well is public anyway.
- For hidden-commitment games (FORKED TONGUE, FACE VALUE, THE COUNCIL): could matter if a player remembers what was dealt to a rival.

**Possible mitigations:**
- **Deal face-down (one face touching table, scoop up).** Each player scoops their stack. The table saw the dealt face but not the reverse. Players then inspect both faces privately. This is probably the natural convention and limits exposure.
- **Deal from a shuffled stack, one at a time, face inward to the recipient.** Slower but conceals the dealt face from opponents. Only the recipient sees the arriving face.
- **Self-deal:** stack the deck, each player draws their own cards from the top. Fastest concealment — nobody sees anyone else's cards.
- **Accept the leak.** For most games, a glimpsed deal-face is low-value information that degrades quickly with shuffled chunks. Explicitly acknowledge it in rules with "if concealment matters, self-deal from a face-down stack."

**Status:** Open question. Note which games actually care. Suggest a dealing convention in the master rules or deck instructions. Test whether "self-deal from a stack" feels natural.

---

## F4: The "one sign = one rank" structure is not intuitive to traditional trick-takers (June 2026, GLEAN session)

**Observation:** A player experienced with trick-taking games (where each suit contains multiple ranks) did not realise that each sign has a single fixed rank — that Crown is *always* 9, Moon is *always* 1, and there is no "Crown of rank 3." He assumed multiple different signs could share the same rank (i.e. that several letters could have a 9 on their reverse). This misunderstanding lasted the entire GLEAN session and materially affected his play.

**Root cause:** In standard decks, suits and ranks are independent axes (4 suits × 13 ranks). On this deck, sign *is* rank — they're the same axis. A card doesn't have "a suit and a rank"; it has "two signs, each with an inherent rank." This is a fundamental departure from what experienced card players expect.

**Impact:** Any game where rank determines outcomes (GLEAN, BLIGHT, FACE VALUE, THE UNPLAYED PAIR) is affected if a player doesn't understand the rank structure. Games that don't use rank at all (WILDFIRE, CROSSROADS, TWELVE TRIALS, THE ORRERY) are unaffected.

**Mitigations:**
- **Teach explicitly before rank-sensitive games:** "There are 9 signs. Each sign has a fixed strength: Crown is always the strongest (9), Moon is always the weakest (1). A card pairs two different signs — so it always has two different ranks, one per face."
- **Visual design:** the shipping deck should make sign=rank visually obvious. If the icon, the pip, and the colour all reinforce the same identity, the fixed mapping is harder to miss.
- **Prototype improvement:** on the current letter+number prototype, the fact that A is always 1 is a convention, not a visual truth. A future prototype might print the sign name + number together more prominently.

**Status:** Teaching-script addition required for all rank-sensitive games. Monitor whether the shipping deck's visual design resolves this naturally.

---

*Last updated: June 2026. Add new findings as numbered entries (F5, F6, …) after each playtest session that produces deck-general observations.*


---

## F5: 36 open cards demand significant table space (June 2026, TWELVE TRIALS + THE ORRERY sessions)

**Observation:** Games that lay out all or most of the 36-card deck on the table (TWELVE TRIALS, THE ORRERY, CROSSROADS's 8 city cards + road network, TRIGON/TURNCOAT's grid + hands) create a large physical footprint. In TWELVE TRIALS, cards are in near-constant motion between staging groups, compounding the space issue. In THE ORRERY, the 21-card (7-symbol) version was already a significant spread.

**Impact:** Any game that uses open/public card layouts at scale. Less relevant for hand-based games (GLEAN, BLIGHT, WILDFIRE, FORKED TONGUE) where the table holds only a small active area.

**Games affected:** TWELVE TRIALS (36 cards sorted openly), THE ORRERY (21–36 cards in orbit groups), CROSSROADS (8 cities + up to 28 roads), TRIGON/TURNCOAT (3×3 grid + hands + score piles).

**Possible mitigations:**
- Workspace conventions (defined zones for different card states) — flagged in TWELVE TRIALS report.
- Smaller subset games (7-symbol / 21 cards) are inherently more manageable.
- Card size could be a production decision — smaller cards for open-layout games, standard for hand games? (Unlikely — one deck, one size.)
- Accept it as a feature of the open-information games and note "needs a large table" in their rulebooks.

**Status:** Acknowledged. Not a design flaw — it's inherent to open-layout games on a 36-card deck. Ensure rulebooks mention space requirements. Consider workspace conventions per game.

---

## F6: Sideways-orientation as state marker doesn't survive card movement (June 2026, TWELVE TRIALS session)

**Observation:** TWELVE TRIALS uses sideways rotation (90°) to mark a card as "flipped." In practice, cards move so frequently between staging groups during the solve that orientation gets lost. The tracking method conflicts with the physical reality of an exploratory puzzle where you constantly pick up, regroup, and rearrange cards.

**Impact:** Any game that uses card orientation (rotation) as a state marker in a context where cards also need to move freely. CROSSROADS and THE ORRERY also use orientation for state — but in those games, cards are placed once and rarely moved, so the conflict is less severe.

**Games affected:** TWELVE TRIALS (confirmed failure), THE ORRERY (theoretical risk if cards move during a solve), CROSSROADS (low risk — cities stay put, roads stay put once built).

**Key distinction:** Orientation-as-state works when cards are **placed and left** (CROSSROADS dimming, TRIGON grid). It fails when cards are **constantly picked up and regrouped** (TWELVE TRIALS during the solve phase).

**Possible mitigations:**
- Tokens or markers placed on flipped cards (external state, not card orientation).
- A written tally / scoresheet tracking flips.
- A "flipped" zone on the table (cards that have been flipped live in a separate area).
- Accept that orientation tracking only works for placed-and-stable cards, and use a different method for exploratory/sorting games.

**Status:** Confirmed failure for TWELVE TRIALS. Needs an alternative tracking method. Does not invalidate orientation-as-state for games where cards stay put.

---

## F7: No concealable draw deck exists — a stack always exposes the top card's face (June 2026, Lauren & Arran session, JANUS)

**Observation:** Any game that draws from a deck during play has a problem with no clean solution on this deck: **a stack of backless cards always shows one face of its top card to the whole table.** There is no "face-down deck." JANUS v1.1 had specifically tried to fix its v1.0 public-deck-top leak by specifying a *"face-down stack drawn without looking"* — and that fix **failed in physical play**: everyone still saw one face of the top card before it was drawn.

**Attempted fixes by the players (both failed):**
- **Drawing from the bottom of the deck** — physically very hard while also holding a fan (one face to self, one to the table), *and* it merely moves the exposure to the new bottom/top card.
- **Covering the deck with a spare card** (they used a leftover Crown) — a working *hack*, and the clearest pointer to the real solution: a genuine **opaque deck cover, sleeve, or draw-bag** as a component or convention.

**Impact by game type:**
- **Games where the deck-top is intended public (TRIGON, TURNCOAT):** no issue — by design.
- **Hidden-information games that draw mid-game (JANUS especially):** *blocking.* JANUS's entire premise is concealed faces; a leaking draw deck breaks it. This is currently the JANUS blocker (see `Janus/JANUS_playtest_01.md`).
- **Games that deal once and never draw (BLIGHT, GLEAN, CROSSROADS, TWELVE TRIALS, etc.):** unaffected during play (but see F3 for the *deal* exposure).

**Possible mitigations:**
- An **opaque deck cover / sleeve** the deck sits in; draw blind from inside it.
- Draw from a **cloth bag** (shuffle by feel; no face ever exposed).
- **Eliminate the draw deck** for hidden-info games — deal the whole (sub-)deck into hands + a face-up shared area, with no refills. Most deck-honest, but changes pacing and needs re-simulation.

**Status:** Open, and **blocking for JANUS.** Distinct from F3 (which is about the one-time *deal* exposure); F7 is about an ongoing *draw deck* during play. Resolve before JANUS's concealed game can be tested at all. Note any other game that relies on a concealed draw.

---

## F8: Hiding your own card backs while manipulating a hand is physically awkward (June 2026, Lauren & Arran session)

**Observation:** In games where one face of your hand must stay hidden from the table (or, in JANUS, from yourself), the act of **flipping/rotating/realigning cards within the hand** to read both faces risks **flashing the concealed face** to other players. Keeping a consistent "this face to me, that face to them" grip while also sorting, choosing, and playing is genuinely fiddly — and gets worse the more cards are held.

**Impact:** Any hidden-hand game (JANUS most acutely, where concealment is the whole game; also FORKED TONGUE, FACE VALUE, THE COUNCIL to the extent a hidden face matters). Compounds F1 (the per-turn re-scan forces lots of in-hand manipulation, each instance a leak risk).

**Possible mitigations:**
- A **hand screen / holder** for games that truly need concealment (extra component — weigh against the no-game-specific-components preference).
- Rules that **minimise required in-hand flipping** (e.g. decide from the visible face where possible).
- Accept that strict concealment of *your own* hand faces may be incompatible with comfortable handling, and prefer designs where in-hand information is open to the holder (the common case).

**Status:** Open. Most severe for JANUS; monitor in other hidden-hand games as they reach the table.

---

## F9: Draw deck and discard / removed pile are not visually distinguishable (June 2026, Lauren & Arran session, TRIGON + general)

**Observation:** Players repeatedly **confused the draw deck with the discard / removed pile** (and discard piles generally). With no card backs, two face-up stacks look alike — there's no colour or back-art to tell "live deck" from "dead pile" at a glance.

**Impact:** Any game with both a draw deck and a discard/removed pile (TRIGON's removed pile, and any future game with a discard). A misdraw from the wrong pile is a real play error, not just cosmetic.

**Possible mitigations:**
- **Orientation/placement convention:** keep the draw deck upright and lay discards sideways (rotated 90°), or assign fixed table zones for each.
- A small **marker/token** on the active draw deck.
- Discard **into an opaque box/tray** (pairs naturally with the F7 deck-cover idea — one cover for the deck, one tray for the dead pile).

**Status:** Open. Cheap to fix with a placement/orientation convention; note it in the master/deck-level handling instructions rather than per-game.
