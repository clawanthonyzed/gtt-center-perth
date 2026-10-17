"""M2 part 2: cheapest and dearest placement of n bookings over the nine slots using the repo solver for BOTH
therapist overlap and phlebotomist draw concurrency (adaptive rule); break-even per pattern; R2 discount model."""
import sys, itertools, math
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import m2_driver as M
D, P, a, n3 = M.D, M.P, M.a, M.n3

def extremes():
    lo, hi = {}, {}
    for counts in itertools.product((0,1,2), repeat=D.SLOTS):
        n = sum(counts)
        if n == 0: continue
        lines, ph, _, _ = D.solve(counts)
        tc = P.total_costs(lines, ph)[0]
        if n not in lo or tc < lo[n][0]: lo[n] = (tc, lines, ph, counts)
        if n not in hi or tc > hi[n][0]: hi[n] = (tc, lines, ph, counts)
    return lo, hi

def be_pattern(costs_by_n, gst=False):
    for n in range(1, 19):
        tc = costs_by_n[n]
        v = P.be(tc, gst)
        if v <= n + 1e-12 and v > n - 1: return round(v, 3), n
    return None

if __name__ == "__main__":
    lo, hi = extremes()
    print("## cheapest / dearest placement per n (adaptive phlebotomists)")
    for n in range(1, 19):
        print(n, "cheapest", a(lo[n][0]), lo[n][1], "ph", lo[n][2], lo[n][3], "| dearest", a(hi[n][0]), hi[n][2])
    plan = {n: P.cost_n(n, "scaled")[0] for n in range(1, 19)}
    stack = {n: P.total_costs(D.solve(D.stacked_counts(n))[0], D.solve(D.stacked_counts(n))[1])[0] for n in range(1, 19)}
    cheap = {n: lo[n][0] for n in range(1, 19)}
    worst = {n: hi[n][0] for n in range(1, 19)}
    for name, cb in (("planning", plan), ("stacked pairs", stack), ("cheapest", cheap), ("dearest", worst)):
        print(name, be_pattern(cb), "GST", be_pattern(cb, True))
    print("## R2 discount")
    N = 18 * D.DAYS
    print("test clients per month", round(N, 2))
    PMP = 117.0
    labour_per_txn = D.PM_LAB * D.ONCOST / (8.6957 * 22 + 4.3478 * 4.33)
    print("txn per month", round(8.6957*22+4.3478*4.33, 2), "PM loaded labour per txn", round(labour_per_txn, 2), "PM_REV", D.PM_REV)
    for s_name, s in (("treatment A$117", 117.0), ("Restore A$135", 135.0), ("Refresh A$185", 185.0)):
        for tk in (0.05, 0.10, 0.15, 0.25, 0.40):
            R = N * tk
            print(s_name, "take-up", tk, "redemptions", round(R, 1), "cost", round(R * s * 0.10, 2), "BE add", n3(R * s * 0.10 / D.REV_PER_CLIENT_MONTH))
    print("X check 118 x 117 x 10%", 118 * 117 * 0.1, " exact", round(N*0.25*117*0.1, 2))
    # break-even uplift: q* = 0.1 s/(s-m)
    for m_name, m in (("idle capacity m=0", 0.0), ("hours added m=loaded labour/txn", labour_per_txn)):
        for s in (117.0, 135.0, 185.0):
            print(m_name, s, "q*", round(0.1 * s / (s - m) * 100, 2), "%")
    # net table at take-up and incremental share
    base_net = 35186.40
    print("net monthly profit effect (steady state 18/day)")
    for m_name, m in (("m=0", 0.0), ("m=labour", labour_per_txn)):
        for tk in (0.05, 0.10, 0.25):
            R = N * tk
            for q in (0.0, 0.10, 0.25, 0.50):
                eff = R * q * (0.9 * 117 - m) - R * (1 - q) * 0.1 * 117
                print(m_name, tk, "q", q, round(eff, 2), "net", round(base_net + eff, 2))
