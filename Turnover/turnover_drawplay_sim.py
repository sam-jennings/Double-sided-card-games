"""TURNOVER — sim check for the proposed 'Draw Two, Play One' rule.

Playtest 01 (June 2026) house rule: when a player is FORCED to refuse
(no playable card), after drawing the refusal cost they may immediately
play ONE card matching the (still-current) target — match and turn, no chain.

This softens the refusal pump (a drawn card that matches can leave again
at once), so the open question is whether it:
  - still terminates (the pump is what makes the game end at all),
  - keeps the healthy skill gap (~1.5-1.8x at the default config),
  - keeps seats roughly flat,
  - and what it does to game length.

Reuses the validated engine from turnover_sim.py; only the turn loop changes.
Baseline = standard v1.1 (chain 2, refuse 2). Variant = baseline + draw-play.
"""

import random
from collections import Counter

from turnover_sim import (
    GameState, HAND_SIZE, TURN_CAP,
    random_choose, skilled_choose,
)


def _play_one(state, pid, rng, skilled):
    """Play exactly one playable card (match + turn), no chain.
    Returns 1 if a card was played, else 0. Uses the same selection logic
    the bots use for a single card (chain_limit=1)."""
    if not state.playable(pid):
        return 0
    if skilled:
        return skilled_choose(state, pid, 1, rng)
    return random_choose(state, pid, 1, rng)


def run_game_drawplay(n, chain_limit, refusal_cost, bots, skilled_flags,
                      rng, draw_play):
    """Like turnover_sim.run_game, but with the optional draw-play rule.

    skilled_flags[pid] tells us which single-card selector to use when the
    draw-play follow-up fires."""
    state = GameState(n, rng)
    pid = 0
    while state.turns < TURN_CAP:
        state.turns += 1
        played = bots[pid](state, pid, chain_limit, rng)
        if played == 0:
            state.refuse(pid, refusal_cost)
            if draw_play:
                # after the forced draw, you may play one (no chain)
                got = _play_one(state, pid, rng, skilled_flags[pid])
                if got and not state.hands[pid]:
                    return pid, state
        else:
            if played > 1:
                state.chains_used += 1
            if not state.hands[pid]:
                return pid, state
        pid = (pid + 1) % n
    return None, state


def pct(x):
    return f"{100*x:.1f}%"


def experiment(n_games=4000, seed=42):
    rng = random.Random(seed)
    print("=" * 80)
    print("TURNOVER — 'DRAW TWO, PLAY ONE' RULE CHECK")
    print(f"{n_games} games per configuration · seed {seed}")
    print("baseline = chain 2 / refuse 2 (v1.1) · variant adds draw-play")
    print("=" * 80)

    # ---- length / stalls / seat balance, all-skilled mirror ----
    print("\n--- ALL-SKILLED MIRROR (length, stalls, seats) ---")
    print(f"{'players':>7} {'rule':>10} | {'avg turns/p':>11} {'stalls':>7} "
          f"{'refus/game':>10} {'seat1 win':>9} {'lastseat':>8}")
    for n in (3, 4, 5, 6):
        for draw_play in (False, True):
            wins = Counter()
            turns = []
            stalls = 0
            refus = []
            flags = [True] * n
            for _ in range(n_games):
                bots = [skilled_choose] * n
                w, st = run_game_drawplay(n, 2, 2, bots, flags, rng, draw_play)
                if w is None:
                    stalls += 1
                else:
                    wins[w] += 1
                    turns.append(st.turns / n)
                    refus.append(st.refusals)
            done = n_games - stalls
            label = "draw-play" if draw_play else "baseline"
            print(f"{n:>7} {label:>10} | {sum(turns)/max(len(turns),1):>11.1f} "
                  f"{stalls:>7} {sum(refus)/max(done,1):>10.1f} "
                  f"{pct(wins[0]/max(done,1)):>9} "
                  f"{pct(wins[n-1]/max(done,1)):>8}")

    # ---- skill gap: 1 skilled vs (n-1) random, seat randomised ----
    print("\n--- SKILL GAP: one skilled bot vs random bots (seat randomised) ---")
    print(f"{'players':>7} {'rule':>10} | {'skilled win':>11} "
          f"{'baseline':>8} {'edge':>6}")
    for n in (3, 4, 5, 6):
        for draw_play in (False, True):
            sw = 0
            done = 0
            for _ in range(n_games):
                seat = rng.randrange(n)
                bots = [random_choose] * n
                bots[seat] = skilled_choose
                flags = [False] * n
                flags[seat] = True
                w, st = run_game_drawplay(n, 2, 2, bots, flags, rng, draw_play)
                if w is not None:
                    done += 1
                    if w == seat:
                        sw += 1
            base = 1 / n
            label = "draw-play" if draw_play else "baseline"
            print(f"{n:>7} {label:>10} | {pct(sw/max(done,1)):>11} "
                  f"{pct(base):>8} {sw/max(done,1)/base:>5.2f}x")

    # ---- estimated real-time length (8s/turn) ----
    print("\n--- ESTIMATED REAL-TIME LENGTH (8s/turn) ---")
    for n in (3, 4, 5, 6):
        for draw_play in (False, True):
            tl = []
            flags = [True] * n
            for _ in range(1000):
                w, st = run_game_drawplay(n, 2, 2, [skilled_choose] * n,
                                          flags, rng, draw_play)
                if w is not None:
                    tl.append(st.turns * 8 / 60)
            label = "draw-play" if draw_play else "baseline"
            print(f"  {n}P {label:>10}: {sum(tl)/len(tl):.1f} min avg, "
                  f"p90 {sorted(tl)[int(0.9*len(tl))]:.1f} min")


if __name__ == "__main__":
    experiment()
