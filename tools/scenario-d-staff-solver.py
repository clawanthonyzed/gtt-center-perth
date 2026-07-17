"""
FIXED: the previous version's concurrent() check counted any existing
booking that overlaps ANY part of the candidate window, which overcounts
(two bookings can each overlap different sub-parts of a window without
ever being simultaneously active together). Correct check: does adding
this candidate interval ever push TRUE simultaneous occupancy above cap,
at any single instant -- computed via a proper sweep line.
"""

def fmt(m):
    h, mi = divmod(m + 7*60, 60)
    return f"{h:02d}:{mi:02d}"

clients_x = {1:0,2:10,3:20,4:40,5:50,6:60,7:80,8:90,9:100,10:120,11:130,12:140,13:160,14:170,15:180}
chair_of = {1:'A',2:'B',3:'C',4:'A',5:'B',6:'C',7:'A',8:'B',9:'C',10:'A',11:'B',12:'C',13:'A',14:'B',15:'C'}
client_pairs = {c: (('Massage','Beauty') if c % 2 == 1 else ('Nails','Hair')) for c in clients_x}
CAP = {'MB': 4, 'Nails': 2, 'Hair': 2}
def pool_of(t): return 'MB' if t in ('Massage','Beauty') else t

client_ids = sorted(clients_x)
windows = {c: ((clients_x[c]+15,clients_x[c]+60),(clients_x[c]+80,clients_x[c]+125)) for c in client_ids}

booked = {'MB': [], 'Nails': [], 'Hair': []}
solution = {}

def true_peak_with(pool, candidate):
    ivs = booked[pool] + [candidate]
    events = []
    for s,e in ivs:
        events.append((s,1)); events.append((e,-1))
    events.sort()
    cur = peak = 0
    for t,d in events:
        cur += d
        peak = max(peak, cur)
    return peak

def backtrack(i):
    if i == len(client_ids):
        return True
    c = client_ids[i]
    s1_win, s2_win = windows[c]
    t_a, t_b = client_pairs[c]
    for (first, second) in [(t_a,t_b),(t_b,t_a)]:
        p1, p2 = pool_of(first), pool_of(second)
        if true_peak_with(p1, s1_win) <= CAP[p1] and true_peak_with(p2, s2_win) <= CAP[p2]:
            booked[p1].append(s1_win)
            booked[p2].append(s2_win)
            solution[c] = (first, s1_win, second, s2_win)
            if backtrack(i+1):
                return True
            booked[p1].pop()
            booked[p2].pop()
            del solution[c]
    return False

ok = backtrack(0)
print(f"Fully feasible solution found: {ok}\n")
if ok:
    for c in client_ids:
        first, s1w, second, s2w = solution[c]
        print(f"Client {c:2d} (Chair {chair_of[c]}, X={fmt(clients_x[c])}): "
              f"S1 {fmt(s1w[0])}-{fmt(s1w[1])} {first:8s}  S2 {fmt(s2w[0])}-{fmt(s2w[1])} {second}")
    print("\n=== Verification (true peak per pool) ===")
    for pool in ['MB','Nails','Hair']:
        events = []
        for iv in booked[pool]:
            events.append((iv[0],1)); events.append((iv[1],-1))
        events.sort()
        cur=peak=0
        for t,d in events:
            cur+=d; peak=max(peak,cur)
        print(f"  {pool}: peak={peak}, cap={CAP[pool]} -> {'OK' if peak<=CAP[pool] else 'VIOLATION'}")
