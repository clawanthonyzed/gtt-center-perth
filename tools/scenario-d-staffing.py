from multirole_analysis import peak_concurrent, fmt

# Scenario D: 15 clients, 3 chairs (A offset 0, B offset +10, C offset +20),
# each chair 5 clients at 40min spacing -- X values from the verified
# Scenario D timetable (am-capacity-weekend.md, 2026-07-17).
clients_x = {
    1:0, 2:10, 3:20, 4:40, 5:50, 6:60, 7:80, 8:90, 9:100,
    10:120, 11:130, 12:140, 13:160, 14:170, 15:180,
}

# Service-type assignment: odd client -> Massage(S1)/Beauty(S2),
# even client -> Nails(S1)/Hair(S2). Simplification for load modelling --
# real mix depends on actual bookings, but this spreads load the same way
# Scenario C's manual table did.
ALL = []
for c, x in clients_x.items():
    s1 = (x+15, x+60)
    s2 = (x+80, x+125)
    if c % 2 == 1:
        ALL.append((s1[0], s1[1], 'M', c))
        ALL.append((s2[0], s2[1], 'B', c))
    else:
        ALL.append((s1[0], s1[1], 'N', c))
        ALL.append((s2[0], s2[1], 'H', c))

M = [iv for iv in ALL if iv[2]=='M']
B = [iv for iv in ALL if iv[2]=='B']
N = [iv for iv in ALL if iv[2]=='N']
H = [iv for iv in ALL if iv[2]=='H']
MB = [iv for iv in ALL if iv[2] in ('M','B')]
NH = [iv for iv in ALL if iv[2] in ('N','H')]

print("=== Scenario D (15 clients, 3 chairs) treatment-staff peak demand ===\n")
print(f"Massage alone: {peak_concurrent(M)[0]}")
print(f"Beauty alone: {peak_concurrent(B)[0]}")
print(f"Massage+Beauty POOLED (realistic cross-train): {peak_concurrent(MB)[0]} at {fmt(peak_concurrent(MB)[1])}")
print(f"Nails alone: {peak_concurrent(N)[0]}")
print(f"Hair alone: {peak_concurrent(H)[0]}")
print(f"Nails+Hair if (incorrectly) pooled: {peak_concurrent(NH)[0]}")
print()
mb_need = peak_concurrent(MB)[0]
n_need = peak_concurrent(N)[0]
h_need = peak_concurrent(H)[0]
print(f"CORRECTED staff needed at Scenario D peak = M+B pool({mb_need}) + Nails alone({n_need}) + Hair alone({h_need}) = {mb_need+n_need+h_need}")
print(f"vs current 8-person single-skill model (2/line) -- was that ever exceeded? "
      f"Massage peak={peak_concurrent(M)[0]}, Beauty peak={peak_concurrent(B)[0]}, "
      f"Nails peak={peak_concurrent(N)[0]}, Hair peak={peak_concurrent(H)[0]} -- "
      f"{'all <=2, 8-person model still covers it' if max(peak_concurrent(M)[0],peak_concurrent(B)[0],peak_concurrent(N)[0],peak_concurrent(H)[0])<=2 else 'EXCEEDS 2 somewhere -- 8-person model insufficient too'}")
