# Symbol Set Study

*What nine symbols should the master deck carry? This study works from the eleven games' actual mechanical demands to a shipping recommendation. It treats symbol identity as two separable layers — a **Spec** (the abstract contract every game is built against) and a **Skin** (the art and names that realise it) — and concludes that the Spec is nearly settled while the Skin is a deliberate, reversible art decision.*

> Binding context: this note defers to the steering set in `.kiro/steering/`. The decisive lens throughout is **legibility and physical handling** — `physical-handling.md` makes that the centre of the project, and `design-principles.md` rule 5 forbids accepting an elegant idea that handles badly. Rank facts and the special role of symbol 9 come from `deck-structure.md`. The instruction not to casually re-skin the two finished games comes from `product-vision.md` (tier 1).

---

## 0. The headline finding (read this first)

**The deck can carry only one set of nine symbols, so TRIGON's "celestial bodies" (from its former SYZYGY identity) and TURNCOAT's "guild marks" cannot both be literal on the shipping deck.** At least one of the two finished games is *already* destined to re-skin, regardless of what we choose. The owner's openness to re-theming both isn't a sacrifice — it removes a constraint that was never really satisfiable.

That reframes the whole question. We are not "forcing the deck to fit TRIGON." We are choosing the best nine symbols on their own merits — legibility, a usable rank, a clear apex, and two games' worth of ability mnemonics — and then dressing both flagships in it. A re-skin is **flavour and art only; it touches no rule, no ability, no balance number**, so it does not disturb the ~45k simulated games behind TRIGON and TURNCOAT (`product-vision.md` tier-1 caution is about *re-tuning*, not renaming — but the final call is still the owner's).

Everything below builds the case for that finding and lands on a concrete recommendation.

---

## 1. Two layers: Spec vs Skin

Most of the confusion in symbol choice comes from arguing about art (sky vs court vs beasts) when the games actually program against an abstract contract. Separate them:

- **The Symbol Spec** — the structural promises every game relies on: nine distinguishable identities, an authoritative rank, a special "ninth", face symmetry. This is *almost universal* and *almost settled*. New games should be designed against the Spec, never against a particular skin's story. **This is the answer to "can the games adapt to a more universal symbol set?": they already are universal — they read the Spec, not the theme.**
- **The Skin** — the art, names, and flavour that realise the Spec (Sky / Court / Bestiary / Glyphs). This is what ships on the cards and what the rulebooks narrate. It is a reversible art decision, and it is the only thing genuinely "open".

The rest of the study nails down the Spec (§2–§4), ranks how sensitive each game is to the Skin (§5), then scores the candidate Skins against the *full* demand set (§6) and recommends one (§7).

---

## 2. The Symbol Spec — the universal contract

### Hard requirements (a shipping set MUST meet all of these)

| # | Requirement | Why / which games | Steering |
|---|---|---|---|
| **H1** | **Nine identities distinct at arm's length, when rotated 90°/180°, and for colour-blind players** — shape carries identity, colour is only a secondary cue. | TURNOVER reads at party speed; TWELVE TRIALS turns cards sideways; JANUS fans are read across the table; all games are handled, not stared at. | `physical-handling.md` (legibility), `design-principles.md` (handling decides) |
| **H2** | **A printed index pip 1–9 on both faces, identical placement** — the single authoritative rank. | The three rank games resolve on the pip (see §4). Subset selection ("remove all 8s and 9s") needs it. | `deck-structure.md` (settled) |
| **H3** | **No mark that differs between the two faces or correlates with the hidden face.** Each face shows only its symbol + pip; nothing leaks which symbol is on the back. | The deck's whole hidden-information layer (JANUS, FALSE FACE, FACE VALUE, UNPLAYED PAIR) collapses if the back is deducible from the front's art. | `physical-handling.md` (hard rule), `deck-structure.md` |
| **H4** | **The set must support fast subset selection by pip** — "remove every card showing an 8 or a 9" must be a quick sort. (This is a property of the printed pip H2, not of any symbol's picture.) | JANUS plays at 1–7; other games declare 1–6/1–8 subsets. | `deck-structure.md` (subset property) |
| **H5** | **The set must support two independent ability-mnemonic skins** — TRIGON's nine powers and TURNCOAT's nine powers — including one identity that reads as **"wild / greatest"** (TRIGON) and one that can read as **"neutral / unaligned"** (TURNCOAT). | This is the deepest and most-overlooked demand; see §3. | `design-principles.md` (clean teaching) |

> **Correction (re: symbol 9 and CROSSROADS).** An earlier draft listed "symbol 9 must read as an apex/capital" as a *hard* requirement because its eight cards become CROSSROADS' board. That was wrong: in CROSSROADS those cards are laid **9-face-down**, so symbol 9 is **never seen during play** — the cities show symbols 1–8. Symbol 9's only hard role is *structural* (it is the symbol removed first for subsets, H4) — a property of the pip and the canonical order, not of the picture. Wanting 9 to *feel* like an apex is therefore a **soft** flavour preference (S6 below), earned mainly by the subset-removal story and by the fact that 9 is the top of the pip rank. It is seen and used like any other symbol in the nine other games.

A subtlety on **H3 vs oriented art**: "no asymmetric marks" means *no mark that betrays the hidden face* — a corner notch, a one-sided foil, anything present on one face but not the other. It does **not** forbid a symbol whose shape has a clear orientation (an animal that faces left, a comet with a tail). An oriented symbol drawn identically wherever it appears leaks nothing about the *other* face, because the other face is simply a different symbol. The current steering wording can be misread as banning oriented art; it should not be. Oriented art is in fact *useful* (see S2).

### Soft preferences (rank the skins, don't disqualify them)

| # | Preference | Why it's soft |
|---|---|---|
| **S1** | **Rank should feel intuitive without reading the pip.** | Comfort, not correctness — the pip (H2) is authoritative. A skin only needs to *not contradict* the order, so players' intuition and the printed number agree. This massively relaxes the constraint the previous study worried over. |
| **S2** | **A clearly *readable* orientation** (so a card's facing/rotation is glanceable) **without a narrative "facing" that fights the game.** | CROSSROADS points roads at the named city and dims cities by 90° rotation; TWELVE TRIALS rotates cards. These games need rotation to *read* — which rotationally-symmetric shapes (regular polygons) actually hurt, and oriented shapes (beasts, comets) help. |
| **S3** | **Tonal stretch** — the same nine faces must serve a meditative solo puzzle, a bluffing duel, a trick-taker, a party race, and two heavier games of alignment and betrayal. | Aesthetic coherence, not function. |
| **S4** | **Subset stories** — the 1–7 "night" JANUS is played at, the 1–6/1–8 worlds. | Flavour bonus. |
| **S5** | **Resonance with the structure games** — TWELVE TRIALS' 12-trio / 4-season *almanac*, THE ORRERY's *orbits*. | Flavour bonus; both are mechanically symbol-agnostic. |
| **S6** | **An apex-feeling symbol 9 and an outsider-feeling symbol 1.** | Flavour, not function: makes the subset-removal story ("set aside the greatest") and the TRIGON-wild / TURNCOAT-neutral roles (H5) write themselves. Per the correction above, 9 is never *seen* in CROSSROADS, so this is comfort only. |
| **S7** | **Family-neutrality / per-game reinterpretability** — each symbol should accept many local meanings (a city, an issue, a faction, a strength, a route-endpoint) without absurdity. | The collection is deliberately *eleven different games*, not one setting. A symbol locked to a single family (a literal animal) forces every game into that frame and makes some games apologise — "why is a road a pair of animals?" This pulls **against S3** (single-family coherence): the more committed the theme, the less reinterpretable. The right answer depends on whether the product is one world or many games (see §6 Set F and §7). |

**Everything in §2 except the Skin-flavoured parts of H5 is universal and effectively fixed.** A new game should be handed this contract, not a picture of a fox.

---

## 3. The deepest demand the old study missed: two ability alphabets

TRIGON and TURNCOAT are the same engine with opposite souls, and **each assigns a distinct, must-be-memorable ability to all nine symbols** — two completely different mappings on the *same* nine physical cards:

| Pip | TRIGON power (celestial skin) | TURNCOAT power (court skin) |
|---:|---|---|
| — | Sun: flip any card (central cross) | Blade: remove an adjacent rival |
| — | Moon: flip an adjacent card (edge) | Mask: flip a card in its row/column |
| — | **Star: WILD + draw-and-play (corner)** | Whisper: peek + flip an adjacent card |
| — | Comet: move a card | Coin: draw-and-play |
| — | Eclipse: swap two cards | Veil: swap, then flip the displaced card |
| — | Aurora: peek + flip an adjacent card | Key: extract your own card from its line |
| — | Meteor: discard an adjacent card | Hound: move one adjacent card, then flip it |
| — | Nova: flip the rest of a full line | **Crown: extract *itself* to its owner** |
| — | Void: catch-up draw (isolated) | Ash: burn the leader's top banked card |

Two consequences the previous study did not register:

1. **A skin earns its keep here or nowhere.** Abstract glyphs (a hexagon, an octagon) give *no* mnemonic for "flip the rest of a full line" or "burn the leader's top card." A player must rote-learn 18 symbol→power bindings. A rich, evocative set lets the *picture* carry the rule ("the Owl sees — it peeks"; "the Blade kills — it removes"), which is exactly the clean-teaching the rubric rewards (`design-principles.md`). **This is the single strongest argument against a purely abstract shipping skin** — and the strongest argument *for* one (Glyphs) is accessibility, so the two pull in opposite directions and we resolve it in §7.
2. **The set needs role-flavoured outliers, not just nine distinct shapes.** TRIGON needs one identity that reads as *wild / supreme*. TURNCOAT needs one that reads as *neutral / unaligned* and one that plausibly *sacrifices itself* (Crown). A flat set of equals (most abstract glyphs, most "nine animals of equal billing") makes these roles arbitrary. A set with a natural apex and a natural "lowest/outsider" makes them write themselves.

This lens did not exist in the prior matrix. It is decisive, and it favours **evocative sets with a built-in hierarchy** (Bestiary's food chain, Sky's brightness, Court's precedence) over flat or abstract ones.

---

## 4. Rank, re-examined: the pip does the work, the theme only stays out of the way

Three games make rank **core**, and one uses it for ordering. The critical, clarifying fact: **all of them read the printed pip (H2), never the theme.**

- **FACE VALUE** — every showdown is decided by *higher hidden pip*; the visible pip breaks ties; the tally tiebreak sums pips; the Cold Read names a symbol. Rank is the entire resolution engine. *Reads the pip.*
- **THE UNPLAYED PAIR** — "each symbol's number is its rank, 9 highest"; the trick is won by the highest revealed pip. *Reads the pip.*
- **THE COUNCIL** — "the index pips give each symbol its value — a Sun issue (9) is worth more than a Void issue (1)"; score is the pip-sum of issues carried. *Reads the pip.*
- **CROSSROADS** — cities sit "in pip order clockwise"; the pie-rule start compares hand pip-totals; ties break on pip-sum. *Reads the pip, for ordering and tie-breaks only.*

So the previous study's hand-wringing over "is brightness/precedence a natural enough rank?" was aimed at the wrong target. **The pip is authoritative and unambiguous.** A skin's job is only to satisfy S1 — *not contradict* the order, so a player's gut and the printed number don't fight ("why is the dim Comet worth more than the blazing Aurora?"). A skin with a clean intuitive order (a food chain) is a comfort bonus; a skin with a fuzzy order (brightness) is survivable because the number is right there; only a skin that *actively misleads* (rank that feels backwards) is a problem, and none of the candidates do that.

**Net effect: rank is a much weaker constraint on skin choice than it looks, because H2 already solved it.** It mostly just rewards the food-chain set a little.

---

## 5. How Skin-sensitive is each game? (ranked)

From most to least dependent on *which* symbols ship:

**Tier α — symbol identity is mechanically/structurally load-bearing**

1. **TRIGON** — nine ability mnemonics + a wild (§3). Re-skin candidate. *Most sensitive.*
2. **TURNCOAT** — nine ability mnemonics + a neutral + a self-sacrificing Crown (§3). Re-skin candidate.
3. **CROSSROADS** — pip order seats the ring (clockwise 1–8), the pie-rule start compares hand pip-totals, and ties break on pip-sum. Note its dependence is on the **pip and the structural removal of symbol 9**, *not* on 9's picture: symbol 9 is laid face-down and never seen, so the "capital" identity is pure narrative framing. This makes CROSSROADS more pip-sensitive (Tier β) than identity-sensitive; it sits here only for the structural 9-removal.

**Tier β — rank is core, but carried by the pip (skin only needs S1)**

4. **FACE VALUE** — hidden-pip showdowns; cold-read names a symbol (wants a small, memorable vocabulary).
5. **THE UNPLAYED PAIR** — pip = trick rank.
6. **THE COUNCIL** — pip = issue value and score.

**Tier γ — strong thematic resonance, mechanically symbol-agnostic**

7. **TWELVE TRIALS** — the 12-trio / 4-season *almanac* sings in a sky/zodiac skin (S5) but runs on any distinct nine.
8. **THE ORRERY** — *orbits* want a celestial reading (S5); mechanics are skin-blind.

**Tier δ — pure legibility/distinctness, no identity needs**

9. **TURNOVER** — match-and-flip at party speed; wants maximum glanceable distinctness (the one game that argues for Glyphs).
10. **JANUS** — across-table fan legibility (H1) + the 1–7 subset story (S4).
11. **FALSE FACE** — pair-registry bluffing; players *name* hidden symbols aloud, so memorable, sayable names help slightly.

The takeaway: **the games that decide the skin are the three in Tier α** — and two of them (TRIGON, TURNCOAT) are exactly the ones the owner has freed us to re-theme. The Tier β games are satisfied by the pip. Tiers γ–δ express only preferences (resonance, legibility) already in the Spec.

---

## 6. The candidate skins, scored against the full demand set

The four candidates are unchanged from the prior study; what changes is the lensing — we now score them against §3 (two ability alphabets), the §4 pip-reframing, and the §2 orientation nuance, not just theme and silhouette.

### Set A — The Ninefold Sky *(celestial)*

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| Void | Meteor | Comet | Eclipse | Aurora | Star | Nova | Moon | Sun |

SYZYGY's (now TRIGON's) native skin. Apex (Sun=9) reads as a natural greatest (S6) and gives the subset-removal a clean story ("set aside the Sun and Moon for the 1–7 night"). Ability mnemonics are strong *for TRIGON* (it was authored here) but must be re-invented for TURNCOAT. Rank = brightness, which is genuinely fuzzy (S1 weak — is a Comet brighter than an Aurora?), survivable only because the pip carries it (§4).

*Hard weakness (H1):* four symbols are spiky radiant discs — Sun, Star, Nova, Meteor — a real confusability cluster. Art can separate them, but it is *fighting* the theme to do so.

### Set B — The Nine Courts *(intrigue)*

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| Whisper | Hound | Mask | Coin | Key | Veil | Ash | Blade | Crown |

TURNCOAT's native skin — and note its nine names are literally TURNCOAT's nine guilds, so it makes that game native and TRIGON foreign (the mirror image of Set A; proof of the §0 finding that both can't be native). Crown=9 reads as a natural apex (S6) and gives TURNCOAT its self-sacrificing Crown for free. Ability mnemonics superb for TURNCOAT, re-invented for TRIGON.

*Weaknesses:* the quiet/structure games (TWELVE TRIALS, THE ORRERY, the solo mood) wear court intrigue badly (S3/S5 poor); Mask/Veil and Coin/Key are silhouette-confusable (H1 medium).

### Set C — The Bestiary *(beasts)*

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| Mouse | Hare | Fox | Owl | Wolf | Boar | Stag | Bear | Dragon |

The only candidate that scores well on *every* lens at once:

- **H1 distinctness:** animal silhouettes are the strongest shape-language available — distinct, rotation-robust, colour-blind-safe almost for free. Best in class.
- **S6 apex + outsider:** Dragon=9 is an unmistakable greatest and Mouse=1 a natural outsider, so the subset-removal story ("set aside the Bear and Dragon for the 1–7 deck") and the TRIGON-wild / TURNCOAT-neutral roles write themselves. (CROSSROADS' "every city sits on a hidden Dragon" is *narrative only* — per §2's correction, 9 is never seen there.)
- **H5 two ability alphabets:** beasts carry *both* mappings better than anything else, because animal behaviour is a deep mnemonic well (hunt, hide, mimic, watch, charge, herd, hoard) — see the §7 re-skin sketch. It also has a natural wild (Dragon) *and* a natural neutral/outsider (Mouse).
- **S1 rank:** the food chain is the only candidate a child orders with no pip at all. Fuzzy in the middle (Boar vs Wolf?), but the pip settles it (§4).
- **S2 orientation:** beasts have a clear, readable facing — which *helps* CROSSROADS ("the road points where the beast looks") and reads cleanly when TWELVE TRIALS turns a card sideways, while staying perfectly H3-safe (the facing is identical art, it leaks nothing about the other face).

*Weakness (now neutralised):* "no existing game is native to it." That mattered only while TRIGON/TURNCOAT were frozen. The owner has unfrozen them, so this cost is paid once, in art and rulebook flavour, with zero balance impact.

### Set D — The Glyphs *(abstract)*

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| Dot | Bar | Triangle | Square | Pentagon | Hexagon | Heptagram | Octagon | Nonagram |

The honest prototyping skin and the accessibility ceiling — colour + shape, maximally abstract. **But two claims in the prior study don't survive scrutiny:**

- *"Maximum legibility"* is false at the top end. A side-count gradient means 6-, 7-, 8-, and 9-sided shapes are **not** quickly distinguishable, especially rotated — Hexagon/Heptagram/Octagon/Nonagram blur exactly where TURNOVER needs speed (H1 fails 6–9). Fixing it means using *categorically different* shapes per rank, which *throws away* "rank = side count" (S1) and the pip becomes the only rank cue.
- *Orientation (S2) is actively poor:* near-symmetric polygons make a 90° dim or a card's facing hard to read — the opposite of what CROSSROADS wants.
- **H5 is its real failure:** abstract glyphs give *no* ability mnemonic, so TRIGON and TURNCOAT become 18 rote bindings. Themeless everywhere; the apex/outsider roles (S6) are arbitrary and the structure-game resonance (S5) is nil.

Its genuine, lasting value is **accessibility and prototyping**, not as the shipping identity.

### Set E — The Ninefold Menagerie *(designed: a bestiary that doubles as a zodiac)*

Set C (Bestiary) was already the strongest of the four. Rather than invent a fifth direction for its own sake, the better move is to **fix C's two weaknesses and graft on A's one real strength** — which is what this set does. It is a synthesis, built specifically to dominate the matrix:

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| Mouse | Hare | Fox | Owl | Serpent | Stag | Wolf | Bear | Dragon |

Three deliberate changes over plain Set C:

1. **Species chosen for *cross-body-plan* distinctness (fixes C's only H1 risk).** A naive bestiary clusters silhouettes — Fox/Wolf are both canids, Boar/Bear/Stag are all bulky quadrupeds. This list spreads the nine across maximally different gross shapes: rodent (Mouse), long-eared leaper (Hare), low canid (Fox), round front-facing bird (Owl), **legless coil (Serpent)**, antlered grazer (Stag), running canid (Wolf), great mass (Bear), winged serpent (Dragon). The Serpent replaces the second bulky quadruped (Boar) precisely to add a body plan nothing else shares. **One at-risk pair remains — Fox (3) vs Wolf (7), both canids** — resolved in art by size and pose (Fox small, tail-curled, sitting; Wolf large, head-low, running), or by substituting a **Lynx** for the Fox if the silhouettes still collide in legibility testing.
2. **A zodiac / almanac *framing* layer (recovers A's S5 resonance, without A's legibility cost).** The nine are presented as the **Ninefold Menagerie — a nine-sign zodiac**. TWELVE TRIALS' twelve trios become the twelve *conjunctions* of an almanac of beasts; THE ORRERY's four orbits are the beasts wheeling through the sky; TRIGON aligns *signs*. Crucially this is a **naming and background-texture layer only** — the symbols stay bold filled silhouettes, with at most a faint star-field *behind* them. This is the explicit lesson from rejecting the "Zodiac of Nine": keep the constellation idea as *story*, never as the *rendered mark* (`physical-handling.md`; `design-principles.md` rule 5).
3. **Dual-register mnemonics, designed in (H5).** Each beast was picked so its behaviour reads in *both* TRIGON's placement register and TURNCOAT's conflict register — see the §7 mappings. The apex (Dragon=9, wild/greatest) and outsider (Mouse=1, catch-up/unaligned) roles (S6) are built in.

What E does *not* try to fix is **accessibility/cost**: it still needs commissioned art and is no more colour-blind-dependent than C (shape carries identity, which is good) — but it cannot match Glyphs for zero-cost prototyping. That trade is inherent to any themed set.

### Set F — The Nine Signs *(archetypal, family-neutral)*

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| Void | Root | Wave | Flame | Eye | Mask | Key | Star | Crown |

A different philosophy entirely, and the direct answer to "must every game be animal-themed?" **No** — the Nine Signs deliberately belong to *no single family* (not bodies, not guilds, not beasts). Each is a broad archetype chosen so that any game can give it a *local* meaning without strain. This is the proposal in `Nine Seals Symbols.docx`, and it is strong.

Its governing idea is a **two-layer split** that the rest of this study has been circling:

- **Permanent deck identity** (printed once, forever): pip 1–9, the sign icon + name, a colour/pattern, an orientation marker. No ability text, no pair-specific art.
- **Per-game interpretation** (in each rulebook): the Crown is a *capital city* in CROSSROADS, the *highest-value issue* in THE COUNCIL, an *apex faction* in TURNCOAT. The Eye is *deduction/reveal* in one game, *surveillance* in another. The same Nine Signs carry different truths per game — which is exactly the collection's tagline material: *one deck, many games, every card has two possible truths.*

Scored against the Spec:

- **S7 family-neutrality — best in class (★★★).** This is the lens your concern names, and Signs win it outright. "The road between the Eye and the Flame" reads as two *places*; "the road between the Mouse and the Owl" fights you, because animals insist on being animals. An abstract sign is a vessel; an animal is a character.
- **H5 ability mnemonics — ★★★, and structurally the best.** The archetypes carry verbs cleanly (Eye→peek, Flame→burn/discard, Wave→move, Mask→swap/flip, Key→extract, Root→connect, Void→empty/catch-up) **and** they ship the two role-symbols *as distinct Signs*: **Star = wild** and **Crown = apex** are separate, which matches TRIGON's real design (its wild, Star, is *not* its top symbol) better than Menagerie, which had to collapse the wild into the apex Dragon. Void is a ready-made outsider. TRIGON even keeps the words "Star" and "Void"; TURNCOAT keeps "Mask," "Key," and "Crown."
- **S6 apex + outsider — ★★★** (Crown / Void), with Star as a bonus third role-symbol.
- **S3 tonal stretch — ★★★.** Archetypal Signs sit comfortably across a meditative solo puzzle, a party race, and a game of betrayal. Nothing about "Void, Root, Wave" feels wrong in a quiet puzzle the way "Whisper, Ash, Blade" (Court) does.
- **H1 distinctness — ★★★ achievable.** Nine distinct concept-icons (Star, Crown, Flame, Eye, Mask, Key are universally legible; Void, Root, Wave need deliberate icon design). Far better separated than abstract polygons; roughly on par with animal silhouettes, and easier than animals to keep colour-blind-safe and rotation-readable because icons can be designed for it.
- **S2 orientation — ★★.** Several Signs have a natural "up" (Crown, Flame, Key, Root), a few are near-symmetric (Star, Void, Wave) — which is why the proposal *correctly* builds in an explicit top-edge orientation marker. (Design note: that marker must be **identical on both faces**, or it would breach H3 by hinting at the hidden side.)
- **S1 rank intuition — ★★, the one real weakness.** Void=1 (nothing) and Crown=9 (highest), Star=8 (high) are intuitive, but the middle order (Root<Wave<Flame<Eye<Mask<Key) is essentially arbitrary. This is *survivable* because the pip is authoritative (§4) and no order actively misleads — but it is genuinely weaker than the food chain for the rank games (FACE VALUE, UNPLAYED PAIR), where a player's gut won't pre-sort the symbols.
- **S5 structure resonance — ★★.** "An ancient symbolic system" gives TWELVE TRIALS and THE ORRERY a mystical-puzzle frame, weaker than a literal sky but perfectly serviceable.
- **Accessibility / prototyping — ★★** (needs art, like any themed set; Glyphs still owns the free-prototype slot).

### Do all eleven games actually *read* on each set? (the sense-check)

This is the heart of your question. ✓ natural · ~ works with a line of flavour · ✗ needs an apology.

| Game | What the symbol must *be* in this game | E · Menagerie | F · Nine Signs |
|---|---|:--:|:--:|
| SYZYGY (now TRIGON) | things you align in threes | ✓ beast-signs | ✓ Signs (keeps Star/Void) |
| TURNCOAT | factions/allegiances | ✓ beast-clans | ✓ factions (Mask/Crown native) |
| **CROSSROADS** | **cities joined by roads** | **✗ "a road between two animals?"** | **✓ nine sign-cities** |
| **THE COUNCIL** | **issues with a value** | **~ "a Wolf issue?"** | **✓ the Crown issue, the Flame issue** |
| FACE VALUE | a hidden *strength* (rank) | ✓✓ food chain aids the bluff | ✓ (rank carried by pip) |
| THE UNPLAYED PAIR | ranked trick values | ✓✓ "Bear beats Fox" | ✓ (middle rank leans on the pip) |
| TWELVE TRIALS | almanac/zodiac signs | ✓ beast zodiac | ~ "an almanac of Signs" |
| THE ORRERY | bodies in orbit | ~ beasts wheeling | ~ Signs wheeling |
| TURNOVER | things to match fast | ✓ | ✓ |
| JANUS | gates/contracts | ✓ | ✓ (Key native) |
| FALSE FACE | a hidden identity you claim | ✓ "claim the beast" | ✓✓ Mask-native bluff |

**The answer to your question is no — the Menagerie does *not* let every game read cleanly.** It strains exactly where you suspected: CROSSROADS (cities/roads) and THE COUNCIL (issues), with the structure games a mild stretch. Its compensating win is the rank games, where a food chain genuinely helps the bluff. The Nine Signs read naturally everywhere, are *native* to the intrigue and bluffing games, and pay their only real price in the two rank games — where the pip already does the work. For a collection that is **eleven different games rather than one world**, fewer apologies is the more valuable property.

### Re-scored fit matrix

★★★ native/excellent · ★★ works with effort · ★ fights the demand. Lenses new to this study are marked †.

| Demand | A · Sky | B · Court | C · Bestiary | D · Glyphs | **E · Menagerie** | **F · Signs** |
|---|---|---|---|---|---|---|
| H1 silhouette distinctness (rotation/CB-safe) | ★★ (radiant cluster) | ★★ (Mask/Veil, Coin/Key) | ★★ (canid/quadruped clusters) | ★★ (6–9 blur) | **★★★ (Fox/Wolf flagged)** | ★★★ (Void/Root/Wave need work) |
| S6 apex + outsider feel (flavour) | ★★★ Sun / Void | ★★★ Crown / Whisper | ★★★ Dragon / Mouse | ★ flat | **★★★ Dragon / Mouse** | ★★★ Crown / Void (+Star wild) |
| **H5† ability mnemonics — TRIGON** | ★★★ native | ★★ re-skin | ★★★ behaviour-rich | ★ rote | **★★★ designed-in** | ★★★ (keeps Star/Void) |
| **H5† ability mnemonics — TURNCOAT** | ★★ re-skin | ★★★ native | ★★★ behaviour-rich | ★ rote | **★★★ designed-in** | ★★★ (Mask/Key/Crown) |
| **H5† wild + neutral roles present** | ★★ (Sun wild; weak neutral) | ★★ (Crown; "unaligned" guild) | ★★★ (Dragon wild, Mouse outsider) | ★ flat | **★★★ (Dragon, Mouse)** | ★★★ (Star wild + Crown + Void) |
| S1 rank intuition (backs the pip) | ★ brightness | ★★ precedence | ★★★ food chain | ★★ side-count (lost if H1 fixed) | **★★★ food chain** | ★★ (ends clear, middle arbitrary) |
| **S2† readable orientation for flips/dims** | ★★★ | ★★ | ★★★ | ★ (symmetric) | **★★★** | ★★ (marker needed) |
| S3 tonal stretch (solo→party→intrigue) | ★★★ | ★ | ★★★ | ★★ | **★★★** | ★★★ |
| **S7† family-neutrality / per-game reinterpretability** | ★★ | ★ | ★ (animals insist on being animals) | ★★★ | ★ | ★★★ (the whole point) |
| S5 structure-game resonance (almanac/orbits) | ★★★ | ★ | ★★ zodiac-bestiary | ★ | **★★★ zodiac framing** | ★★ "ancient system" |
| **Accessibility / prototyping** | ★★ | ★★ | ★★ | ★★★ | ★★ | ★★ |

Two sets now top the table, and they win *different* lenses. **Menagerie** maximises coherence, silhouette charm, and rank intuition — ideal if the product is *one world*. **Nine Signs** maximises family-neutrality (S7), tonal stretch, and built-in role-symbols — ideal if the product is *many games*. Glyphs remains the unbeatable free-prototype / accessibility companion to whichever ships.

---

## 7. Recommendation

### Primary: ship **Set F — the Nine Signs** (archetypal, family-neutral); re-interpret each game's symbols per rulebook.

This study's earlier draft recommended the Menagerie. **Your objection — that a committed family forces every game into its frame and makes CROSSROADS and THE COUNCIL apologise — is correct, and it is decisive.** The sense-check (§6) confirms the Menagerie strains for two games and mildly for the structure pair; the Nine Signs strain for none. For a product whose entire identity is *one deck, many genuinely different games* (`product-vision.md`: each game must explore the deck "from a genuinely different angle"), **family-neutrality (S7) is worth more than single-family charm (S3).** The Signs also happen to win the deepest mechanical lens (H5) outright, by shipping the wild (Star), apex (Crown), and outsider (Void) as *distinct* Signs — matching the two flagships' real structure and even preserving their vocabulary.

Why it wins, in priority order of the steering set:

1. **It fits what the collection actually is.** Eleven games, many moods; a vessel-like symbol that becomes a city, an issue, a faction, a strength, or a route-endpoint *as each rulebook declares* (S7). This is the property your question is really asking for.
2. **H5 ability mnemonics — strongest available.** Archetypes carry verbs (Eye→peek, Flame→burn, Wave→move, Mask→swap, Key→extract) *and* provide three role-symbols (Star wild, Crown apex, Void outsider). TRIGON keeps "Star is wild"; TURNCOAT keeps Mask/Key/Crown — these are partial remaps, not full re-skins.
3. **It survives on the primary axis (H1)** with deliberate icon design — Star/Crown/Flame/Eye/Mask/Key are universally legible; Void/Root/Wave are the three to design carefully and legibility-test.
4. **Best tonal stretch and future-proofing (S3, S7):** new games inherit a meaning-flexible alphabet, never a fixed setting to fight.

Adopt the proposal's **two-layer production rule** verbatim, because it is the mechanism that makes all of the above work:

- **Permanent deck identity (printed forever):** pip 1–9 on both faces, sign icon + name, colour/pattern, and an orientation marker. **No ability text, no pair-specific decoration.**
- **Per-game interpretation (in each rulebook):** what the Signs *mean* this game. The Crown is a capital in CROSSROADS, the top issue in THE COUNCIL, the apex faction in TURNCOAT.
- **One H3 caveat to add to the proposal:** the orientation marker must be **identical on both faces**, or it leaks the hidden side (`physical-handling.md`).

### The honest trade-off (and the one alternative worth keeping)

The Signs' only real cost is **S1 rank intuition**: the middle order (Root<Wave<Flame<Eye<Mask<Key) is arbitrary, so in FACE VALUE and THE UNPLAYED PAIR a player's gut won't pre-sort the symbols — they read the pip. That is acceptable (the pip is authoritative, §4) but it is a genuine loss versus a food chain.

So keep **Set E — the Ninefold Menagerie** documented as the leading alternative, for one specific decision: *if the owner decides the product should read as a single coherent world rather than a toolkit of games*, the Menagerie is the better choice — more charming, better rank intuition, richer silhouettes — at the cost of CROSSROADS/COUNCIL needing a line of flavour each. **This is the fork:** Nine Signs for "many games, many meanings"; Menagerie for "one world." Given the collection's stated distinctness-driven identity, the recommendation is Nine Signs.

Reject, as before, the **constellation-rendered "Zodiac of Nine"**: it loses on the primary axis (thin low-contrast line-art) regardless of which family wins (`design-principles.md` rule 5). Whatever ships, render it as **bold, filled, high-contrast icons.**

### Fallbacks, in order

1. **Set E — Menagerie** (the "one world" alternative above).
2. **Set A — Sky, redrawn** (most conservative; keeps SYZYGY (now TRIGON) native, re-skins only TURNCOAT). Sky is also reasonably family-neutral (cities-under-the-sun, the Star faction), so it is a soft middle ground between Signs and Menagerie.
3. **Set D — Glyphs** as the permanent **prototyping skin and accessibility benchmark** — never the primary identity (H5), but the companion the shipping set must not regress against.

### Proof the re-skin is free: sketch mappings (flavour only, zero balance change)

Illustrative — to show the powers fall out of the Signs — not a finished re-theme.

**TRIGON → Nine Signs** (wild stays **Star**, verbatim):

| TRIGON power | Sign | Mnemonic |
|---|---|---|
| Wild + draw (corner) | **Star** | unchanged — Star is still wild |
| Flip any card (cross) | **Crown** | the highest authority overturns anything |
| Flip an adjacent card (edge) | **Key** | a key *turns* |
| Flip the rest of a full line | **Root** | roots run the length of the row |
| Move a card | **Wave** | the current carries it elsewhere |
| Swap two cards | **Mask** | two identities trade places |
| Peek + flip an adjacent card | **Eye** | it sees the hidden face, then turns it |
| Discard an adjacent card | **Flame** | it burns the neighbour off the board |
| Catch-up draw (isolated) | **Void** | unchanged — the empty sign scavenges |

**TURNCOAT → Nine Signs** (Mask, Key, Crown stay native):

| TURNCOAT power | Sign | Mnemonic |
|---|---|---|
| Flip a card in its row/column | **Mask** | unchanged — the Mask turns loyalties |
| Extract your own from its line | **Key** | unchanged — the Key unlocks your agent |
| Extract *itself* to its owner | **Crown** | unchanged — the Crown returns to its head |
| Remove an adjacent rival | **Flame** | it destroys the neighbour |
| Burn the leader's top banked card | **Void** | the front-runner's store is annulled |
| Peek + flip an adjacent | **Eye** | sees the hidden face, then turns it |
| Draw and play | **Star** | a stroke of fate, an extra play |
| Move + flip one adjacent | **Wave** | the current drags a neighbour and turns it |
| Swap + flip the displaced | **Root** | intertwined roots exchange places |

Both mappings keep words the originals already use, and **change no requirement, ability, geometry, or score — only names and art.** (A Menagerie version of these tables, for the "one world" fork, is the §6 Set-E sketch with Serpent in place of the discard slot.)

---

## 8. Future-proofing: design new games against the Spec, never the Skin

The reason this collection can survive a skin change at all is that the games were (mostly) built against the Spec — and the Nine Signs' two-layer rule (§7) makes that explicit and permanent. To keep it that way:

- **New designs reference the Spec (§2) and the sign's *role*, not a setting.** Say "symbol 9 / the apex / the Crown's slot," "the printed rank," "the wild (Star)" — and let the new game's rulebook declare what the signs *mean* locally (cities, suits, resources, claims). Then the deck never needs reprinting for a new game.
- **If a new game needs a per-symbol identity** (like TRIGON/TURNCOAT's abilities), check it against H5: does each sign's archetype give a mnemonic for the power you're attaching? If a power only makes sense under one game's interpretation, that's fine — it lives in *that rulebook*, not on the card.
- **Keep rank on the pip (H2).** A new rank game reads the number; the sign order is only S1 comfort, and (for Signs) deliberately weak in the middle, so lean on the pip.
- **Run the H1/H3/S2 checks** from `physical-handling.md` on any new symbol-dependent rule before it reaches a rulebook — and remember the orientation marker must be identical on both faces (H3).

## 9. Open items / sign-offs needed

- **The fork to decide (owner):** *many games, many meanings* → **Nine Signs (Set F, recommended)**; or *one coherent world* → **Menagerie (Set E)**. Everything else follows from this single call.
- **Owner sign-off to re-interpret TRIGON and TURNCOAT.** Under Nine Signs these are *partial* remaps (TRIGON keeps Star/Void; TURNCOAT keeps Mask/Key/Crown) and are flavour/art only — they touch no simulated balance. `product-vision.md` tier-1 still reserves the call to the owner.
- **This study overturns the "current lean" recorded in `deck-structure.md`** ("a hybrid *Zodiac of Nine* … Bestiary fallback, Sky conservative second"). The recommendation is now **Nine Signs primary; Menagerie the 'one-world' alternative; Sky conservative; Glyphs prototype/accessibility; constellation *rendering* rejected.** Updating that steering line needs owner sign-off — flagged here, not changed unilaterally.
- **Adopt the two-layer production rule** (permanent deck identity vs per-game interpretation) from `Nine Signs Symbols.docx` as the collection's symbol policy, with the H3 fix to the orientation marker.
- **Continue prototyping with Set D Glyphs** in `Print and Play/`: zero cost, stress-tests every rulebook's legibility claims, and is the accessibility benchmark the shipping set must not regress against.
- **Nine Signs art brief** (if adopted): nine bold filled icons; the three to design and legibility-test hardest are **Void, Root, Wave**; pip 1–9 both faces; colour/pattern + a both-faces-identical orientation marker; no ability text, no pair-specific decoration.
