"""
GTT Center Perth -- Draw-event scheduler.

Source of truth for task durations: operations-manual.md "Key Rules" table
(relative to each client's own GTT start time X):

  Draw 1 (fasting + 75g glucose drink) : X      to X+15   -> 15 min IN-CHAIR
  Service 1                            : X+15   to X+60   -> 45 min (client off-chair)
  Transition buffer                    : X+60   to X+70   -> 10 min (client off-chair)
  Draw 2  (target X+75, tolerance +/-5): movable within X+70..X+80 -> 5 min IN-CHAIR
  Service 2                            : X+80   to X+125  -> 45 min (client off-chair)
  Draw 3  (target X+135, tol +/-10)    : movable within X+125..X+145 -> 5 min IN-CHAIR
  Departure                            : ~X+145-150

Real chair/phlebotomist-occupied time per client = 15 + 5 + 5 = 25 min
out of a ~150 min visit (~17% utilisation) -- this is the number Anthony
asked for directly: "how long each draw takes and the time for the work
after the draw."

Hard resource constraint: N_CHAIRS phlebotomist/chairs, each can only run
ONE draw event at a time (no double-booking a chair).

This script does NOT assume a fixed "one client owns one chair for its
whole visit, new client every 40 min" rhythm (that was the old manual
heuristic). Instead it greedily admits new clients as early as possible,
onto whichever chair has room, using the D2/D3 tolerance windows to dodge
collisions -- i.e. actual bin-packing of the short draw events, not a
fixed per-chair cadence.
"""

D1_DUR = 15
D1_START, D1_END = 0, 15
D2_TARGET, D2_TOL, D2_DUR = 75, 5, 5      # window 70-80
D3_TARGET, D3_TOL, D3_DUR = 135, 10, 5    # window 125-145
DEPART_OFFSET = 150

N_CHAIRS = 2
CANDIDATE_STEP = 5   # try admitting a new client every 5 min of sim time
SIM_HORIZON = 400    # generous upper bound for search


def draw_windows(x):
    """Return the three draw intervals for a client starting at x, using the
    EARLIEST slot within tolerance for D2/D3 by default (adjusted later to
    dodge collisions)."""
    d1 = (x + D1_START, x + D1_END)
    d2 = (x + D2_TARGET - D2_TOL, x + D2_TARGET - D2_TOL + D2_DUR)
    d3 = (x + D3_TARGET - D3_TOL, x + D3_TARGET - D3_TOL + D3_DUR)
    return d1, d2, d3


def overlaps(a, b):
    return a[0] < b[1] and b[0] < a[1]


def try_place(chair_bookings, x):
    """Try every combination of D2 offset (within +/-5) and D3 offset
    (within +/-10) in 1-min steps, earliest-first, return the first
    collision-free placement on this chair, else None."""
    d1 = (x + D1_START, x + D1_END)
    if any(overlaps(d1, b) for b in chair_bookings):
        return None
    for d2_off in range(-D2_TOL, D2_TOL + 1):
        d2_start = x + D2_TARGET + d2_off
        d2 = (d2_start, d2_start + D2_DUR)
        if any(overlaps(d2, b) for b in chair_bookings):
            continue
        for d3_off in range(-D3_TOL, D3_TOL + 1):
            d3_start = x + D3_TARGET + d3_off
            d3 = (d3_start, d3_start + D3_DUR)
            if any(overlaps(d3, b) for b in chair_bookings):
                continue
            return d1, d2, d3
    return None


def run(window_end_for_new_starts, label):
    chairs = [[] for _ in range(N_CHAIRS)]   # each: list of (start,end) draw blocks
    clients = []   # (client_num, chair_idx, x, d1, d2, d3)
    x = 0
    n = 0
    while x <= window_end_for_new_starts:
        placed = False
        # try each chair, prefer the one with fewer bookings so far (load-balance)
        for ci in sorted(range(N_CHAIRS), key=lambda i: len(chairs[i])):
            placement = try_place(chairs[ci], x)
            if placement:
                d1, d2, d3 = placement
                chairs[ci].extend([d1, d2, d3])
                n += 1
                clients.append((n, ci, x, d1, d2, d3))
                placed = True
                break
        x += CANDIDATE_STEP

    # verification pass: confirm zero overlaps per chair, independent of admission logic
    ok = True
    for ci, bookings in enumerate(chairs):
        srt = sorted(bookings)
        for i in range(len(srt) - 1):
            if srt[i][1] > srt[i + 1][0]:
                ok = False
                print(f"  COLLISION on chair {ci}: {srt[i]} vs {srt[i+1]}")

    print(f"\n=== {label} (new-start window: 0-{window_end_for_new_starts} min) ===")
    print(f"Clients admitted: {n}  (verification: {'PASS - zero collisions' if ok else 'FAIL'})")
    per_chair = {}
    for c in clients:
        per_chair.setdefault(c[1], []).append(c[0])
    for ci in range(N_CHAIRS):
        print(f"  Chair {chr(65+ci)}: {len(per_chair.get(ci, []))} clients -> {per_chair.get(ci, [])}")

    def fmt(m):
        h, mi = divmod(int(m) + 7 * 60, 60)
        return f"{h:02d}:{mi:02d}"

    print(f"  Last client start: {fmt(clients[-1][2]) if clients else '-'}   "
          f"Last client D3 ends / depart ~: {fmt(clients[-1][5][1] + (DEPART_OFFSET - D3_TARGET - D3_TOL - D3_DUR)) if clients else '-'}")
    return clients, chairs, n


if __name__ == "__main__":
    print("Real chair-occupied ('draw') time per client: "
          f"D1={D1_DUR}min + D2={D2_DUR}min + D3={D3_DUR}min = {D1_DUR+D2_DUR+D3_DUR}min "
          f"out of ~{DEPART_OFFSET}min total visit "
          f"({100*(D1_DUR+D2_DUR+D3_DUR)/DEPART_OFFSET:.0f}% chair utilisation per client)")

    # Scenario 1: same new-client-start window as the current verified Scenario C
    # (07:00 start, last new-draw start assumed 10:05 -> minute 185)
    run(185, "Optimised packing, SAME window as current Scenario C (last start 10:05)")

    # Scenario 2: what if the window extended to last start 11:00 (minute 240)?
    run(240, "Optimised packing, window extended to last start 11:00")
