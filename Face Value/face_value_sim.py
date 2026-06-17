"""FACE VALUE quick pacing sim — termination, duel count, economy.
Cards = frozenset pairs from 9 symbols (pips 1-9). Hidden pip known to owner.
Crude bots: skilled (threshold + occasional bluff) vs random-ish.
"""
import random, statistics

def deck():
    return [(a, b) for a in range(1, 10) for b in range(a + 1, 10)]

def play_game(p0_skill, p1_skill, rng):
    cards = deck()
    rng.shuffle(cards)
    hands = [cards[:15], cards[15:30]]
    tally = [[], []]
    first_actor = rng.randrange(2)
    duels = 0
    folds = showdowns = coldreads = 0
    while hands[0] and hands[1] and duels < 200:
        duels += 1
        # ante: each picks a card; skilled hides high pip, random picks random face
        duel = []
        for p in range(2):
            skill = (p0_skill, p1_skill)[p]
            c = max(hands[p], key=lambda c: max(c)) if skill and rng.random() < .7 else rng.choice(hands[p])
            hands[p].remove(c)
            hi, lo = max(c), min(c)
            if skill and rng.random() < .8:
                show, hide = lo, hi          # show low, hide strength
            else:
                show, hide = rng.choice([(lo, hi), (hi, lo)])
            duel.append((show, hide, c))
        stakes = [[], []]
        actor = first_actor
        result = None  # (winner, mode)
        while result is None:
            show, hide, c = duel[actor]
            opp = 1 - actor
            skill = (p0_skill, p1_skill)[actor]
            n_raises = len(stakes[actor]) + len(stakes[opp])
            can_raise = len(hands[actor]) > len(stakes[opp]) - len(stakes[actor]) + 1
            if skill:
                if hide >= 8 and can_raise and n_raises < 4 and rng.random() < .6:
                    act = 'raise'
                elif hide >= 5 or rng.random() < .15:   # .15 = bluff-call
                    act = 'call'
                elif stakes[opp] or stakes[actor]:
                    act = 'fold'
                else:
                    act = 'call' if rng.random() < .5 else 'fold'
            else:
                act = rng.choices(['raise', 'call', 'fold'],
                                  [.2 if can_raise else 0, .6, .2])[0]
            if act == 'raise':
                stakes[actor].append(hands[actor].pop(rng.randrange(len(hands[actor]))))
                actor = opp
            elif act == 'call':
                need = len(stakes[opp]) - len(stakes[actor])
                if need > len(hands[actor]):
                    act = 'fold'
                else:
                    for _ in range(need):
                        stakes[actor].append(hands[actor].pop(rng.randrange(len(hands[actor]))))
                    # showdown
                    a, b = duel
                    if duel[0][1] != duel[1][1]:
                        w = 0 if duel[0][1] > duel[1][1] else 1
                    else:
                        w = 0 if duel[0][0] > duel[1][0] else 1
                    tally[w] += [duel[0][2], duel[1][2]] + stakes[0] + stakes[1]
                    result = (w, 'showdown'); showdowns += 1
            if act == 'fold':
                opp = 1 - actor
                hands[actor].append(duel[actor][2])           # duel card back
                tally[opp] += stakes[actor]
                if hands[actor]:
                    tally[opp].append(hands[actor].pop(rng.randrange(len(hands[actor]))))  # escape card
                hands[opp] += stakes[opp] + [duel[opp][2]]    # opp keeps everything
                result = (opp, 'fold'); folds += 1
        first_actor = result[0]  # winner acts first next duel (catch-up for loser: acts last = advantage)
    return duels, len(tally[0]), len(tally[1]), folds, showdowns, \
           (1 if len(tally[0]) > len(tally[1]) else 0)

rng = random.Random(7)
for label, s0, s1 in [('skilled vs skilled', 1, 1), ('skilled vs random', 1, 0)]:
    D, T0, T1, F, S, W = [], [], [], [], [], []
    for _ in range(4000):
        d, t0, t1, f, s, w = play_game(s0, s1, rng)
        D.append(d); T0.append(t0); T1.append(t1); F.append(f); S.append(s); W.append(w)
    print(f"{label}: duels avg {statistics.mean(D):.1f} (max {max(D)}), "
          f"folds {statistics.mean(F):.1f}, showdowns {statistics.mean(S):.1f}, "
          f"P0 winrate {statistics.mean(W):.2f}, "
          f"tally sizes {statistics.mean(T0):.1f}/{statistics.mean(T1):.1f}")
