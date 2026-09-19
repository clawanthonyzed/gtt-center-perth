"""
GTT Center Perth -- AM Demand-Driven Volume-Tier Staffing Solver.

Extends tools/demand_driven_staffing_solver.py (the calibrated, verified
concurrency model) in two ways needed to answer Anthony's direct instruction
("do not use a flat 8 service staff every day assumption across every
client-volume scenario"): (1) supports ODD client counts (the last pair-slot
uses only Chair A, no Chair B client) so a real day's booking count does not
need to be rounded to an even pair, and (2) sweeps pair cadence for each
target AM client-volume tier to find the minimum treatment headcount
achievable within the WDP guidance window (last Draw 1 no later than
10:30am, i.e. no more than 210 minutes after a 07:00 start).

CALIBRATION, not a fresh assumption: build_clients_odd/assign_and_check_odd
below are checked against the same already-published N=12/N=18 answers
(8 treatment staff, 4/2/2) before being trusted on any new volume tier --
see tests/test_am_volume_tier_staffing_solver.py.

Target volumes tested (Anthony's own profitability-ladder points, per
docs/CURRENT-STATE.md §8): 9.00, 11.29, 13.50, 15.50, 18.00 AM clients/day.
Since these are continuous AVERAGE daily-volume planning figures (used
elsewhere for revenue as volume x price x days), not literal whole-number
daily bookings, each is rounded UP (ceiling) to the nearest whole client
count for ROSTERING purposes only -- you cannot roster a fractional client,
and rounding up avoids understaffing risk. Revenue calculations elsewhere in
this repo continue to use the exact fractional volume; only the STAFFING
tier lookup in this module rounds.

Usage: python tools/am_volume_tier_staffing_solver.py
"""

import math

LINES = ["MB", "Nails", "Hair"]
SERVICE_MINUTES = 45
DRAW_MINUTES = 5
WDP_GUIDANCE_WINDOW_MINUTES = 210  # 07:00 to 10:30, last Draw 1 must be <= this


def build_clients_odd(n_clients, cadence_minutes):
    """Same synchronized-pair structure as
    demand_driven_staffing_solver.build_clients, extended to support ODD
    n_clients: floor(n/2) full pairs (Chair A + Chair B), plus one further
    Chair-A-only client if n is odd (the last pair-slot's Chair B simply
    doesn't open -- consistent with this repo's own already-established
    Chair B enquiry-threshold policy, docs/CURRENT-STATE.md §1, not an
    invented mechanic)."""
    n_pairs_full = n_clients // 2
    has_extra = n_clients % 2 == 1
    n_slots = n_pairs_full + (1 if has_extra else 0)
    clients = []
    for slot_idx in range(n_slots):
        x = slot_idx * cadence_minutes
        chairs = ("A", "B")
        if has_extra and slot_idx == n_slots - 1:
            chairs = ("A",)
        for chair in chairs:
            s1 = (x + DRAW_MINUTES, x + DRAW_MINUTES + SERVICE_MINUTES)
            s2 = (x + 60 + DRAW_MINUTES, x + 60 + DRAW_MINUTES + SERVICE_MINUTES)
            clients.append({"id": len(clients) + 1, "chair": chair, "x": x, "s1": s1, "s2": s2})
    return clients


def assign_and_check_odd(n_clients, cadence_minutes):
    """Same fixed, calibration-confirmed assignment rule as
    demand_driven_staffing_solver.assign_and_check (Service 1 always MB;
    Service 2 Nails for Chair A, Hair for Chair B), extended to odd
    n_clients via build_clients_odd above."""
    clients = build_clients_odd(n_clients, cadence_minutes)
    line_bookings = {t: [] for t in LINES}
    for c in clients:
        t1 = "MB"
        t2 = "Nails" if c["chair"] == "A" else "Hair"
        line_bookings[t1].append(c["s1"])
        line_bookings[t2].append(c["s2"])

    peak_by_line = {}
    for t in LINES:
        events = []
        for iv in line_bookings[t]:
            events.append((iv[0], 1))
            events.append((iv[1], -1))
        events.sort()
        cur = peak = 0
        for _, delta in events:
            cur += delta
            peak = max(peak, cur)
        peak_by_line[t] = peak

    last_draw1_minute = max((c["x"] for c in clients), default=0)
    last_departure_minute = max((c["s2"][1] + DRAW_MINUTES for c in clients), default=0)

    return {
        "n_clients": n_clients,
        "cadence_minutes": cadence_minutes,
        "peak_by_line": peak_by_line,
        "total_headcount": sum(peak_by_line.values()),
        "last_draw1_minute": last_draw1_minute,
        "last_departure_minute": last_departure_minute,
    }


def phlebotomist_headcount_check_odd(n_clients, cadence_minutes):
    """Draw 1/2/3 concurrency check, extended for odd n_clients -- confirms
    whether the committed 2-phlebotomist figure is structurally sufficient
    at a given tier (it always is, since at most 2 clients ever draw
    simultaneously in this synchronized-pair model, by construction)."""
    clients = build_clients_odd(n_clients, cadence_minutes)
    draws = []
    for c in clients:
        x = c["x"]
        draws.append((x, x + DRAW_MINUTES))
        draws.append((x + 60, x + 60 + DRAW_MINUTES))
        draws.append((x + 120, x + 120 + DRAW_MINUTES))
    events = []
    for iv in draws:
        events.append((iv[0], 1))
        events.append((iv[1], -1))
    events.sort()
    cur = peak = 0
    for _, delta in events:
        cur += delta
        peak = max(peak, cur)
    return peak


def max_feasible_cadence(n_clients, granularity=5, floor_cadence=25):
    """Largest cadence (rounded down to the nearest `granularity` minutes,
    floored at `floor_cadence`) such that the last pair-slot's Draw 1 still
    falls at or before the WDP guidance window boundary (210 minutes after
    a 07:00 start)."""
    n_slots = math.ceil(n_clients / 2)
    if n_slots <= 1:
        return WDP_GUIDANCE_WINDOW_MINUTES
    raw_max = WDP_GUIDANCE_WINDOW_MINUTES // (n_slots - 1)
    stepped = (raw_max // granularity) * granularity
    return max(floor_cadence, stepped)


def minimum_headcount_for_volume(target_volume, granularity=5, floor_cadence=25):
    """For a target AM client-volume/day (a continuous planning average, per
    this module's own docstring), rounds UP to the nearest whole client
    count for staffing purposes, sweeps every feasible cadence from
    `floor_cadence` to the WDP-guidance-window maximum, and returns the
    cadence/headcount combination with the SMALLEST cadence that achieves
    the MINIMUM headcount found in that sweep (the smallest cadence keeps
    client-to-client spacing as tight as reasonably possible for a given
    headcount, rather than widening the day further than needed)."""
    n_ceil = math.ceil(target_volume)
    if n_ceil < 1:
        n_ceil = 1
    max_cadence = max_feasible_cadence(n_ceil, granularity=granularity, floor_cadence=floor_cadence)

    sweep = []
    cadence = floor_cadence
    while cadence <= max_cadence:
        r = assign_and_check_odd(n_ceil, cadence)
        sweep.append(r)
        cadence += granularity

    best = None
    for r in sweep:
        if best is None or r["total_headcount"] < best["total_headcount"]:
            best = r
        elif r["total_headcount"] == best["total_headcount"] and r["cadence_minutes"] < best["cadence_minutes"]:
            best = r

    phleb_peak = phlebotomist_headcount_check_odd(n_ceil, best["cadence_minutes"])

    return {
        "target_volume": target_volume,
        "rostered_for_n_clients": n_ceil,
        "chosen_cadence_minutes": best["cadence_minutes"],
        "max_feasible_cadence_minutes": max_cadence,
        "treatment_peak_by_line": best["peak_by_line"],
        "treatment_headcount": best["total_headcount"],
        "phlebotomist_headcount": phleb_peak,
        "last_draw1_minute": best["last_draw1_minute"],
        "last_departure_minute": best["last_departure_minute"],
        "cadence_sweep": sweep,
    }


TARGET_VOLUMES = [9.00, 11.29, 13.50, 15.50, 18.00]


def fmt_time(minutes_after_7am):
    h, m = divmod(420 + minutes_after_7am, 60)
    return f"{h:02d}:{m:02d}"


def main():
    print("=== Calibration: reproduce the already-published, verified 8-staff figure (even N) ===\n")
    all_calibrated = True
    for n, expected in ((12, 8), (18, 8)):
        r = assign_and_check_odd(n, 25)
        matches = r["total_headcount"] == expected
        all_calibrated = all_calibrated and matches
        status = "MATCHES" if matches else "DOES NOT MATCH -- STOP"
        print(f"N={n} @ 25min cadence: {r['peak_by_line']}, total={r['total_headcount']} (expected {expected}) -- {status}")
    if not all_calibrated:
        print("\nCALIBRATION FAILED -- results below are not trustworthy.")
        return

    print("\n=== Minimum solver-verified headcount per AM volume tier ===\n")
    for vol in TARGET_VOLUMES:
        r = minimum_headcount_for_volume(vol)
        print(
            f"Target {vol:.2f}/day -> rostered for {r['rostered_for_n_clients']} clients, "
            f"cadence={r['chosen_cadence_minutes']}min (max feasible {r['max_feasible_cadence_minutes']}min): "
            f"treatment={r['treatment_peak_by_line']} (total {r['treatment_headcount']}), "
            f"phlebotomists={r['phlebotomist_headcount']}, "
            f"last Draw1={fmt_time(r['last_draw1_minute'])}, last departure={fmt_time(r['last_departure_minute'])}"
        )


if __name__ == "__main__":
    main()
