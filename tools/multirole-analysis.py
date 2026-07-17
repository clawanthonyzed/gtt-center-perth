"""
Multi-role staffing analysis for the synchronized Scenario C timetable.
Answers 3 concrete questions with real computation, not guesses:
  A) If treatment staff are cross-trained, how many on-duty staff are
     genuinely needed at peak (vs the current 8, 2-per-line)?
  B) If all 10 clients picked the SAME first service (Hair), does it
     actually work with only 2 Hair-qualified staff? What's the real wait?
  C) Real usable >=45min gaps per staff member, for standalone bookings.
"""

def fmt(m):
    h, mi = divmod(m + 7*60, 60)
    return f"{h:02d}:{mi:02d}"

# All 20 service intervals: (start, end, type, client)
S1 = [(15,60,'M',1),(15,60,'N',2),(55,100,'M',3),(55,100,'N',4),
      (95,140,'M',5),(95,140,'N',6),(135,180,'M',7),(135,180,'N',8),
      (175,220,'M',9),(175,220,'N',10)]
S2 = [(80,125,'B',1),(80,125,'H',2),(120,165,'B',3),(120,165,'H',4),
      (160,205,'B',5),(160,205,'H',6),(200,245,'B',7),(200,245,'H',8),
      (240,285,'B',9),(240,285,'H',10)]
ALL = S1 + S2

def peak_concurrent(intervals):
    events = []
    for s,e,*_ in intervals:
        events.append((s,1)); events.append((e,-1))
    events.sort()
    cur = peak = 0
    peak_time = None
    for t,d in events:
        cur += d
        if cur > peak:
            peak = cur
            peak_time = t
    return peak, peak_time

print("=== A) Peak concurrent treatment demand under different pooling models ===\n")

peak_all, t_all = peak_concurrent(ALL)
print(f"Fully cross-trained pool (all 4 lines, any staff can do any service): "
      f"peak concurrent = {peak_all} at {fmt(t_all)}")

mb = [iv for iv in ALL if iv[2] in ('M','B')]
nh = [iv for iv in ALL if iv[2] in ('N','H')]
peak_mb, t_mb = peak_concurrent(mb)
peak_nh, t_nh = peak_concurrent(nh)
print(f"Realistic pairing (Massage+Beauty pool, separate from Nails+Hair pool):")
print(f"  Massage+Beauty pool peak concurrent = {peak_mb} at {fmt(t_mb)}")
print(f"  Nails+Hair pool peak concurrent   = {peak_nh} at {fmt(t_nh)}")
print(f"  Total staff needed (2 pools) = {peak_mb + peak_nh}  (vs current 8, 2/line)")

print(f"\nIf fully cross-trained across all 4 (best case, all 4 lines everyone qualified):")
print(f"  Staff needed at peak = {peak_all}  (vs current 8)")

print("\n=== B) All 10 clients request the SAME first service (Hair), only 2 Hair staff ===\n")
# All 10 S1 windows become Hair-type, use earliest-available greedy (like a real queue)
hair_requests = [(15,1),(15,2),(55,3),(55,4),(95,5),(95,6),(135,7),(135,8),(175,9),(175,10)]
staff_free_at = [0, 0]  # 2 hair staff, when each becomes free
DUR = 45
waits = []
for want_start, cid in hair_requests:
    # pick the staff member who's free soonest
    idx = 0 if staff_free_at[0] <= staff_free_at[1] else 1
    actual_start = max(want_start, staff_free_at[idx])
    wait = actual_start - want_start
    staff_free_at[idx] = actual_start + DUR
    waits.append((cid, want_start, actual_start, wait))
    print(f"  Client {cid}: wants Hair at {fmt(want_start)}, "
          f"actual start {fmt(actual_start)}, wait = {wait}min "
          f"(staff Hair-{idx+1})")

max_wait = max(w[3] for w in waits)
total_wait_clients = sum(1 for w in waits if w[3] > 0)
print(f"\nMax wait: {max_wait}min. Clients affected: {total_wait_clients}/10.")

print("\n=== C) Real >=45min gaps per staff member (Scenario C, current 2-per-line assignment) ===\n")
staff_bookings = {
    'Staff 1 (was M1)': [(15,60,'C1'),(95,140,'C5'),(175,220,'C9')],
    'Staff 2 (was M2)': [(55,100,'C3'),(135,180,'C7')],
    'Staff 3 (was B1)': [(80,125,'C1'),(160,205,'C5'),(240,285,'C9')],
    'Staff 4 (was B2)': [(120,165,'C3'),(200,245,'C7')],
    'Staff 5 (was N1)': [(15,60,'C2'),(95,140,'C6'),(175,220,'C10')],
    'Staff 6 (was N2)': [(55,100,'C4'),(135,180,'C8')],
    'Staff 7 (was H1)': [(80,125,'C2'),(160,205,'C6'),(240,285,'C10')],
    'Staff 8 (was H2)': [(120,165,'C4'),(200,245,'C8')],
}
DAY_START, DAY_END = 0, 330  # 07:00-12:30
total_gap_capacity = 0
for name, bookings in staff_bookings.items():
    bookings = sorted(bookings)
    gaps = []
    prev_end = DAY_START
    for s,e,c in bookings:
        if s - prev_end >= 45:
            gaps.append((prev_end, s))
        prev_end = e
    if DAY_END - prev_end >= 45:
        gaps.append((prev_end, DAY_END))
    gap_str = ', '.join(f"{fmt(g[0])}-{fmt(g[1])} ({g[1]-g[0]}min)" for g in gaps)
    print(f"  {name}: {gap_str if gaps else 'no gap >=45min'}")
    total_gap_capacity += sum((g[1]-g[0])//45 for g in gaps)

print(f"\nTotal standalone-appointment-sized (45min) slots available across all 8 staff: ~{total_gap_capacity}/day")
