# CONCORD

*A repeated “I divide, you choose” drafting game for 2 players · 25–35 minutes · working prototype v0.1*

> **Status:** fully specified fast prototype, not balance-validated. D5 (distinctness) and D6 (gap-filling) are intentionally excluded from the evaluation.

---

## 1. Design target

Build a game in which **“I divide, you choose” is the repeated core decision**, not a setup device or occasional action, while satisfying the remaining collection rubric:

- **D1 — Deck-necessity:** the two-faced all-pairs deck must be essential.
- **D2 — Physical handling:** no fake face-down state, concealed stack, large hand, or remembered hidden information.
- **D3 — Flipping:** flipping must change the value of an offer and the outcome of scoring.
- **D4 — Pair uniqueness:** “every pair exactly once” must define what players are building.
- **D7 — Teachability:** the turn should remain explainable in a few sentences.

The deck is used openly. All card faces may be inspected; cards are always returned showing the same face unless a rule explicitly flips them.

---

## 2. Candidate concepts

### A. CONCORD — divide bonds, build exact triangles

Reveal six cards. The Divider splits them into two lots of three, flips one card, and the Chooser takes one lot. Players use acquired cards to form exact three-sign triangles: AB, AC, and BC. A triangle scores best when its three cards visibly show A, B, and C once each.

**Strengths:** the lot size matches the scoring structure; pair uniqueness defines every scoring set; orientation changes value; all information is open.

### B. MERIDIAN — divide roads, build directed routes

Each card is a directed road from its hidden sign to its visible sign. Players have different capital signs. The Divider creates two road bundles; the Chooser takes the one better for their own network. Score signs that can reach your capital.

**Why it lost:** strong D1/D3, but physical route tracing across two separate 18-card networks is cumbersome. Players would repeatedly lift cards to verify sources, and reachability scoring is much harder to teach and audit.

### C. THE INHERITANCE — divide assets and liabilities

The visible sign of each card is an asset; its reverse is a liability. The Divider creates two estates and the Chooser selects one. End-game symbol majorities score assets but duplicate liabilities reduce them.

**Why it lost:** easiest handling and teach, but pair uniqueness does little. A generic double-sided suit deck would produce almost the same game, so D4 fails.

### D. THE GREAT CUT — divide the whole deck once

One player partitions all 36 cards into two equal estates; the other chooses one. Each estate is then scored as a graph.

**Why it lost:** purest fair-division concept, but one enormous cut is an analysis-paralysis exercise rather than a game. Repeated small cuts create adaptation, bluffing, and changing valuations.

### Candidate rubric

| Concept | D1 | D2 | D3 | D4 | D7 | Verdict |
|---|:---:|:---:|:---:|:---:|:---:|---|
| CONCORD | 9 | 9 | 9 | 10 | 8 | Develop |
| MERIDIAN | 9 | 6 | 9 | 8 | 5 | Reject: tracing burden |
| THE INHERITANCE | 7 | 9 | 7 | 4 | 9 | Reject: uniqueness incidental |
| THE GREAT CUT | 9 | 8 | 7 | 9 | 3 | Reject: one decision is too large |

---

## 3. Iteration into the final structure

### Iteration 1 — four-card offers, split 2–2

This produced nine rounds with the full deck. It was mechanically clean, but two-card lots did not resemble the three-card objects players were trying to build. Each cut felt indirect.

**Change:** reveal six and split 3–3. The full deck now produces exactly six rounds, each player Divides three times and Chooses three times, and every lot is itself a possible triangle.

### Iteration 2 — recipients choose all card orientations

This made the drafting work, but flipping became cosmetic: every acquired card simply entered in its preferred orientation.

**Change:** revealed orientation persists. The Divider must flip exactly one card after dividing and before the choice. Later flips require a limited Amendment counter.

### Iteration 3 — unlimited repairs

Any structural triangle can be made visibly balanced with one flip. Unlimited repairs therefore erased orientation and reduced the game to triangle collection.

**Change:** each player receives only **2 Amendment counters**. A repaired triangle scores less than one assembled without repair.

### Iteration 4 — solve the whole 18-card holding at game end

This created a large final packing puzzle and encouraged players to postpone all organisation.

**Change:** after every cut, each player may ratify at most one Concord. Ratified cards are locked. Waiting preserves flexibility but risks running out of ratification windows.

### Iteration 5 — rank-based tiebreak

Using pip totals would add the deck’s fixed-rank teaching burden without improving the core mechanism.

**Change:** signs have no rank in CONCORD. Ties are broken by breadth: more different signs represented across ratified Concords.

---

# 4. Complete prototype rules

## CONCORD

*Split every offer as fairly as you can—because your rival chooses first.*

Each card is a bond between two Signs. Three bonds can form a **Concord** when they connect every pair among exactly three Signs. But a true Concord must also give every Sign a visible voice. Divide the bonds into two offers, turn one card, and hope your rival leaves you the future you planned.

### Players and time

- Exactly **2 players**
- Approximately **25–35 minutes**
- Medium-light strategy

### Components

- The full **36-card, 9-Sign deck**
- **4 generic counters** from the shared kit: 2 per player

No Nine Signs ability reference is needed. Sign strengths are not used.

### Objective

Ratify valuable three-card Concords.

- **Natural Concord:** 3 points
- **Amended Concord:** 2 points

Highest score wins.

---

## Key definition: a Concord

Choose three different Signs: A, B, and C.

The three cards **A/B, A/C, and B/C** are the unique bonds among them. Together they are a **triangle**.

They become a scoring **Concord** when their visible faces show **A, B, and C exactly once each**.

### Example

Moon/Leaf, Moon/Flame, and Leaf/Flame form a triangle.

- If they show **Moon, Flame, Leaf**, they are already a Natural Concord.
- If they show **Moon, Moon, Leaf**, flipping the Moon/Flame card to Flame makes the three visible Signs different. Spend an Amendment counter to ratify it as an Amended Concord.

A useful property: whenever three cards form a triangle but do not currently show all three Signs, **exactly one of the three cards can be flipped to repair it**.

---

## Setup

1. Give each player **2 Amendment counters**.
2. Shuffle the full deck, **flipping random chunks** so the showing faces are randomised.
3. Place the deck upright between the players. The visible top face is public and irrelevant; every offer will be fully open.
4. Randomly choose the first **Divider**. The other player is the first **Chooser**.
5. Give each player space for:
   - an open **Workshop** of loose cards;
   - up to six three-card **Concords**.

All cards are public. Either player may inspect both faces of any loose card or offered card, then return it showing the same face.

---

## The six rounds

Each round has four steps.

### 1. Reveal six bonds

Deal the next **6 cards** face-up into the centre, preserving the faces dealt.

Both players may inspect both sides of all six cards. Return every card as found.

### 2. Divide

The Divider separates the six cards into **two lots of exactly three cards**.

The Divider may rearrange cards freely but may not turn them over yet.

### 3. Turn one

After the two lots are final, the Divider must **flip exactly one card** in either lot.

This flip is free and permanent. It is part of the offer.

### 4. Choose

The Chooser takes either complete lot and adds its three cards to their Workshop, preserving their showing faces.

The Divider receives the other lot.

Then both players may ratify Concords.

---

## Ratifying Concords

After each round, beginning with the Chooser, each player may ratify **zero or one** Concord from cards in their Workshop.

To ratify:

1. Select the three exact pair-cards among three Signs.
2. If they already show all three Signs once each, place them together as a **Natural Concord**.
3. Otherwise, you may spend one Amendment counter:
   - flip the unique card that makes all three Signs visible;
   - place the spent counter beside the group;
   - this is an **Amended Concord**.
4. Ratified cards are locked. They can never move, flip, or be used in another Concord.

You may deliberately leave a possible Concord loose to preserve its cards for a different triangle later. However, there are only six ratification windows, including the one after the final round.

After ratification, swap roles: the previous Chooser becomes Divider.

---

## End of the game

After six rounds:

- the deck is empty;
- each player owns 18 cards;
- each player has had three turns as Divider and three as Chooser;
- the ratification step after round six is the final opportunity to score.

### Scoring

- Natural Concord: **3 points**
- Amended Concord: **2 points**
- Loose cards: **0 points**
- Unspent Amendment counters: **0 points**

The higher score wins.

### Tiebreak

Count how many **different Signs** appear across all your ratified Concords. More different Signs wins.

If still tied, share the victory. Do not use seat order as an arbitrary tiebreak until playtesting demonstrates a real seat advantage.

---

## Clarifications

- **The Divider flips exactly one offered card every round.** They cannot decline and cannot flip more than one.
- **A lot is chosen whole.** The Chooser cannot exchange cards between lots.
- **Loose cards retain their showing face.** Picking one up to inspect its reverse does not count as flipping it; return it as found.
- **Only two effects flip cards:** the Divider’s compulsory offer flip and spending an Amendment while ratifying.
- **A structural triangle does not score by itself.** It must be ratified while visibly showing all three Signs.
- **You cannot amend without a counter.** Once both are spent, only Natural Concords can be ratified.
- **One ratification per player per round.** You cannot save unused ratifications or ratify extra Concords after round six.
- **Signs have no strength in this game.** Pips are identifiers only.

---

## Teaching script

> “Six cards appear. I split them into two groups of three and flip one card. You choose a whole group; I get the other. We are collecting exact triangles: AB, AC, and BC. They score when the three cards show A, B, and C once each. You have two counters to repair two bad orientations. After every split, each of us may lock one triangle.”

Then demonstrate one valid triangle and one non-triangle.

---

## Strategic texture intended

### The Divider’s problem

A good division is not “make two objectively equal piles.” Valuations differ because each player’s Workshop differs. The Divider wants to construct two offers where:

- the Chooser’s preferred lot leaves a useful remainder;
- obvious completed triangles are paired with cards that improve the other player more;
- the compulsory flip changes which lot looks naturally ratifiable;
- unique bonds needed by one player are separated from their companion bonds.

### The Chooser’s problem

The most immediately valuable lot may not be the best one. The Chooser must compare:

- a Natural Concord now;
- an exact missing bond for a stronger later triangle;
- denying the Divider a unique edge;
- preserving limited Amendment counters;
- breadth for the tiebreak.

### Pair uniqueness as interaction

There is only one A/B card. Once one player owns it, the other can never form any Concord requiring that exact bond. Taking one card can therefore kill several of the opponent’s possible triangles while opening several of your own.

---

# 5. Mathematical sanity check

This is not a balance proof; it only checks whether the proposed score scale is plausible.

For a random 18-card half of the 36-card deck:

- it contains about **9.6 structural triangle candidates** on average, but they overlap heavily;
- the maximum number of edge-disjoint triangles is about **4.0** on average;
- with random showing faces and no repairs, an optimal grouping yields about **1.67** visible Concords;
- with 1 Amendment, about **2.62**;
- with 2 Amendments, about **3.33**;
- with 3 Amendments, about **3.76**, already close to the structural ceiling.

Therefore **2 counters per player** is the useful starting point: it repairs enough bad orientation to prevent hopeless holdings, but does not make orientation irrelevant.

Model limitations:

- ownership was random rather than produced by strategic divide-and-choose;
- grouping was optimised at the end rather than locked sequentially;
- it does not model human visibility, tempo, or analysis paralysis.

The calculations justify prototyping, not publication.

---

# 6. Rubric assessment

D5 and D6 are deliberately omitted.

| Dimension | Score | Reason |
|---|:---:|---|
| **D1 — Deck-necessity** | **9/10** | Cards physically encode unique bonds and their current visible voice. An ordinary deck cannot support the triangle identity and orientation economy without extensive remapping. Held below 10 because a bespoke domino/edge set could imitate it. |
| **D2 — Physical handling** | **9/10** | Fully open information; no hands; no concealed draw; no remembered hidden state; only six cards are evaluated centrally. Personal areas grow to 18 cards but ratified groups compress the layout. |
| **D3 — Flipping** | **9/10** | Every Divider must alter one offer by flipping; visible orientation separates 3-point natural from 2-point amended scoring; only two later repairs are available. Removing flips materially changes both drafting and scoring. |
| **D4 — Pair uniqueness** | **10/10** | A Concord is precisely the three unique pair-cards among three Signs. Taking one unique edge permanently removes every opponent triangle requiring it. Duplicate pairs would break the denial and triangle registry. |
| **D7 — Teachability** | **8/10** | The turn is split six, flip one, choose three. The only conceptual hurdle is recognising AB/AC/BC triangles; a physical example teaches it. Planning depth may slow first turns but does not expand the rule set. |

---

# 7. First playtest plan

The first session should test the mechanism, not tune points broadly.

## Configuration

- 2 players
- Full 36-card deck
- 2 Amendment counters each
- Six rounds
- 3/2 scoring
- One ratification per player per round

## Questions

1. **Does cutting feel like the main skill?** The Divider should spend time constructing two genuinely difficult alternatives, not merely dump three good and three bad cards.
2. **Does the compulsory flip improve cuts or just add calculation?** Record whether players use it as bait, repair, or sabotage.
3. **Can players recognise triangles without repeatedly sorting the whole Workshop?** If not, the game fails D7 even though the rule is simple.
4. **Does one ratification per round create useful commitment?** Watch for frustration when a player has multiple late Concords but only one window.
5. **Are two Amendments scarce?** They should be spent deliberately, not automatically in the first two available triangles.
6. **Does the final score reflect decisions rather than offer luck?** Ask each player to identify one cut or choice they regret.
7. **Footprint:** can each Workshop stay readable without exceeding a normal table half?

## Fast falsification gates

Cut or structurally redesign if either occurs:

- players cannot evaluate a six-card cut without exhaustive, slow triangle searches every round;
- the Chooser’s decision is usually obvious because one lot completes a triangle and the other does not.

Iterate rather than cut if:

- triangle recognition works but ratification timing is awkward;
- the flip is meaningful but two counters are wrong;
- score ties are frequent but the core choices are good.

## Variants to test only after the base loop works

- **Open Ratification:** remove the one-per-round limit; ratify any number after round six. Tests whether timing adds value or merely friction.
- **One Amendment:** sharper orientation pressure.
- **Four-card Cut:** nine rounds of 2–2 for a lighter but less triangle-shaped version.
- **Silent Cut:** Divider may not explain the intended equality of the lots; likely unnecessary unless table talk becomes coercive.

---

## 8. Current verdict

CONCORD is ready for a first physical prototype. Its main risk is not balance; it is **cognitive legibility**. The game succeeds only if players can scan their loose bonds and assess a six-card division without turning every round into a graph-search exercise. The first test should therefore use the plainest available glyph set, open inspection, clearly separated Workshops, and no extra theme rules.
