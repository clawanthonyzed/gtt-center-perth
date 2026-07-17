"""
Verify treatment-staff feasibility under SYNCHRONIZED chair starts
(Chair A and Chair B both start their client cohorts at the same clock
time each slot, 40min apart -- 5 slots, 2 clients/slot, 10 total).

This is the check that was previously only ASSERTED, never built:
does synchronizing chair starts create service-line collisions given
only 2 staff per line (massage/beauty/nails/hair)?
"""

TYPES = ['Massage', 'Beauty', 'Nails', 'Hair']
CAP = 2  # staff per line

slots = [0, 0, 40, 40, 80, 80, 120, 120, 160, 160]  # X per client, chair A/B paired
chairs = ['A','B','A','B','A','B','A','B','A','B']

clients = []
for i, x in enumerate(slots):
    s1 = (x+15, x+60)
    s2 = (x+80, x+125)
    clients.append({'id': i+1, 'chair': chairs[i], 'x': x, 's1': s1, 's2': s2})

def overlaps(a, b):
    return a[0] < b[1] and b[0] < a[1]

# per-type interval list -> list of (interval, client_id) already committed
type_bookings = {t: [] for t in TYPES}

def concurrent_count(t, interval, exclude_id=None):
    return sum(1 for iv, cid in type_bookings[t] if cid != exclude_id and overlaps(iv, interval))

def try_assign(client):
    # try every ordered pair of distinct types for (s1_type, s2_type),
    # prefer least-loaded types first for balance
    load = {t: len(type_bookings[t]) for t in TYPES}
    ordered = sorted(TYPES, key=lambda t: load[t])
    for t1 in ordered:
        if concurrent_count(t1, client['s1']) >= CAP:
            continue
        for t2 in ordered:
            if t2 == t1:
                continue
            if concurrent_count(t2, client['s2']) >= CAP:
                continue
            return t1, t2
    return None

assignments = []
for c in clients:
    r = try_assign(c)
    if r is None:
        assignments.append((c['id'], None, None))
        continue
    t1, t2 = r
    type_bookings[t1].append((c['s1'], c['id']))
    type_bookings[t2].append((c['s2'], c['id']))
    assignments.append((c['id'], t1, t2))

def fmt(m):
    h, mi = divmod(m + 7*60, 60)
    return f"{h:02d}:{mi:02d}"

print("=== Synchronized-start treatment assignment (10 clients, 2 per slot) ===\n")
for c, (cid, t1, t2) in zip(clients, assignments):
    print(f"Client {cid} (Chair {c['chair']}, X={fmt(c['x'])}): "
          f"S1 {fmt(c['s1'][0])}-{fmt(c['s1'][1])} = {t1 or 'UNASSIGNED'}, "
          f"S2 {fmt(c['s2'][0])}-{fmt(c['s2'][1])} = {t2 or 'UNASSIGNED'}")

print("\n=== Per-line concurrency verification (max 2 allowed at any instant) ===")
ok = True
for t in TYPES:
    ivs = sorted(type_bookings[t])
    print(f"\n{t}: {len(ivs)} bookings")
    for iv, cid in ivs:
        print(f"  Client {cid}: {fmt(iv[0])}-{fmt(iv[1])}")
    # brute force max concurrency check
    events = []
    for iv, cid in ivs:
        events.append((iv[0], 1))
        events.append((iv[1], -1))
    events.sort()
    cur = 0
    peak = 0
    for time, delta in events:
        cur += delta
        peak = max(peak, cur)
    print(f"  Peak concurrent bookings: {peak} (cap={CAP}) -> {'OK' if peak<=CAP else 'VIOLATION'}")
    if peak > CAP:
        ok = False

unassigned = [a for a in assignments if a[1] is None]
print(f"\nUnassigned clients: {len(unassigned)}")
print(f"\nOVERALL: {'ALL CLIENTS PLACED, ZERO DOUBLE-BOOKING' if ok and not unassigned else 'PROBLEM FOUND'}")
