"""
GTT Center Perth: AM Staggered-Start, Service-Selection-Driven Staffing Solver.

Builds on tools/demand_driven_staffing_solver.py (the calibrated, verified
concurrency model for the 25-minute-cadence AM schedule) rather than
re-deriving concurrency from scratch. That tool answers "how many staff on
a line, at peak." This tool answers the founder's next question: which
individual staff member covers which specific booking, when does each one
actually start their shift, and how much idle time do they carry.

CALIBRATION, not a fresh assumption: this solver is run first against the
existing, published, fixed service-selection pattern (Service 1 always
Massage+Beauty; Service 2 Nails for Chair A clients, Hair for Chair B
clients) at N=12 and N=18, and must reproduce the already-verified 8-staff
total (4 MB + 2 Nails + 2 Hair) before its staggered-lane output is treated
as trustworthy. It is checked and printed explicitly, not assumed to pass.

GENUINE, DISCLOSED LIMIT: this venture has not opened yet, so no real
booking data exists on which specific service each AM client actually
selects on a given day. The fixed Service1=MB/Service2=Nails-or-Hair
pattern above is the only evidenced, already-published assumption in this
repository (docs/scenario-c-sync-timetables.md Section 0.6a); it is a
modelled convention for costing purposes, not a confirmed real distribution
of client choice. This solver also demonstrates the founder's other
requirement directly (no staff rostered for a line with zero demand, staff
reused when already on shift) via clearly-labelled alternate scenarios that
vary which line each client's Service 1 and Service 2 draw from; these
are illustrative demand-responsiveness tests, not new committed figures.

Individual staff-lane assignment method: standard interval-partitioning
(equivalent to colouring an interval graph, provably requiring exactly
"peak concurrency" colours/staff, no more, no fewer). Bookings on each line
are assigned in start-time order to the staff member on that line whose
previous booking ends closest to (but not after) the new booking's start --
this both guarantees the total staff count matches the independently
verified peak concurrency AND minimises each individual's idle gaps
(a proven property of "earliest end-time first, closest fit" interval
scheduling), which is the founder's explicit "back-to-back, minimise idle
gaps" requirement, not an invented heuristic.

Usage: python tools/am_staggered_staffing_solver.py
"""

import sys
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from demand_driven_staffing_solver import (
    LINES, SERVICE_MINUTES, DRAW_MINUTES, CADENCE_MINUTES,
    build_clients, phlebotomist_headcount_check,
)


def fmt(m):
    h, mi = divmod(m + 7 * 60, 60)
    return f"{h:02d}:{mi:02d}"


def fixed_pattern_assignment(clients):
    """Reproduces the already-published, calibration-confirmed pattern:
    Service 1 is always Massage+Beauty pool (MB); Service 2 is Nails for
    Chair A clients, Hair for Chair B clients. Returns a list of bookings
    per line: (start, end, client_id, service_label)."""
    bookings = {t: [] for t in LINES}
    for c in clients:
        t1 = "MB"
        t2 = "Nails" if c["chair"] == "A" else "Hair"
        bookings[t1].append((c["s1"][0], c["s1"][1], c["id"], "Service 1"))
        bookings[t2].append((c["s2"][0], c["s2"][1], c["id"], "Service 2"))
    return bookings


def assign_staff_lanes(bookings_by_line):
    """Interval-partitioning assignment: for each line, sorts its bookings
    by start time and assigns each one to the staff member (on that line)
    whose last-assigned booking ends soonest at-or-before the new booking's
    start (closest fit, minimises that individual's idle gap), opening a
    new staff member only when no existing one is free. Returns, per line,
    a list of staff lanes; each lane is an ordered list of bookings."""
    lanes_by_line = {}
    for line, bookings in bookings_by_line.items():
        ordered = sorted(bookings, key=lambda b: b[0])
        lanes = []  # each lane: {"end": last_end, "bookings": [...]}
        for booking in ordered:
            start, end, cid, label = booking
            # find the free lane (last_end <= start) with the LARGEST last_end
            # (closest fit -> minimises idle gap for that staff member)
            best_lane = None
            best_end = None
            for lane in lanes:
                if lane["end"] <= start:
                    if best_end is None or lane["end"] > best_end:
                        best_end = lane["end"]
                        best_lane = lane
            if best_lane is None:
                best_lane = {"end": None, "bookings": []}
                lanes.append(best_lane)
            best_lane["bookings"].append(booking)
            best_lane["end"] = end
        lanes_by_line[line] = lanes
    return lanes_by_line


def lane_summary(lanes_by_line):
    """Produces the individual staff-lane report: roster start (first
    booking start), roster end (last booking end), total idle minutes
    between bookings, and total booked minutes, per staff member, per
    line."""
    summary = []
    for line, lanes in lanes_by_line.items():
        for i, lane in enumerate(lanes, start=1):
            bks = sorted(lane["bookings"], key=lambda b: b[0])
            roster_start = bks[0][0]
            roster_end = bks[-1][1]
            booked_minutes = sum(b[1] - b[0] for b in bks)
            idle_minutes = 0
            for j in range(1, len(bks)):
                gap = bks[j][0] - bks[j - 1][1]
                if gap > 0:
                    idle_minutes += gap
            summary.append({
                "line": line,
                "staff_number": i,
                "roster_start": roster_start,
                "roster_end": roster_end,
                "booked_minutes": booked_minutes,
                "idle_minutes": idle_minutes,
                "n_bookings": len(bks),
                "bookings": bks,
            })
    return summary


def calibrate(n_clients, expected_total):
    clients = build_clients(n_clients)
    bookings = fixed_pattern_assignment(clients)
    lanes = assign_staff_lanes(bookings)
    total_staff = sum(len(v) for v in lanes.values())
    per_line = {line: len(v) for line, v in lanes.items()}
    matches = total_staff == expected_total
    return {
        "n_clients": n_clients,
        "per_line": per_line,
        "total_staff": total_staff,
        "expected": expected_total,
        "matches": matches,
        "lanes": lanes,
    }


def print_lane_report(lanes_by_line):
    for line in LINES:
        lanes = lanes_by_line.get(line, [])
        print(f"\n  Line: {line} ({len(lanes)} staff)")
        for s in lane_summary({line: lanes}):
            bstr = ", ".join(f"C{b[2]} {fmt(b[0])}-{fmt(b[1])}" for b in s["bookings"])
            print(f"    Staff {s['staff_number']}: roster {fmt(s['roster_start'])}-{fmt(s['roster_end'])}, "
                  f"{s['n_bookings']} bookings, {s['booked_minutes']}min booked, "
                  f"{s['idle_minutes']}min idle between bookings -> [{bstr}]")


def scenario_reduced_nail_demand(n_clients):
    """Illustrative, explicitly NOT a committed figure: what happens to the
    Nails line if fewer Chair-A clients select a nail service than the
    fixed pattern assumes (some pick Hair instead, since AM clients can, in
    principle, choose either second-service line regardless of chair, this
    is a modelling simplification the venue could relax operationally, not
    a hard constraint tested elsewhere in this repo). Demonstrates the
    founder's "no staff rostered for zero demand" requirement directly:
    if zero clients pick Nails, the Nails lane count must be zero."""
    clients = build_clients(n_clients)
    bookings = {t: [] for t in LINES}
    for c in clients:
        bookings["MB"].append((c["s1"][0], c["s1"][1], c["id"], "Service 1"))
        # Illustrative only: every client's second service goes to Hair,
        # zero clients select Nails this scenario.
        bookings["Hair"].append((c["s2"][0], c["s2"][1], c["id"], "Service 2"))
    lanes = assign_staff_lanes(bookings)
    return lanes


def main():
    print("=== Calibration: reproduce the already-published, verified 8-staff figure ===\n")
    all_calibrated = True
    for n, expected in ((12, 8), (18, 8)):
        r = calibrate(n, expected)
        all_calibrated = all_calibrated and r["matches"]
        status = "MATCHES PUBLISHED FIGURE" if r["matches"] else "DOES NOT MATCH: STOP, DO NOT TRUST LANE OUTPUT BELOW"
        print(f"N={n} clients: per_line={r['per_line']}, total={r['total_staff']} "
              f"(published: {expected}): {status}")

    if not all_calibrated:
        print("\nCALIBRATION FAILED: staggered-lane output below is NOT trustworthy until this is fixed.")
        return

    print("\n=== Individual staff-lane output at N=18 (18-client committed AM model) ===")
    r18 = calibrate(18, 8)
    print_lane_report(r18["lanes"])

    print("\n\n=== Individual staff-lane output at N=12 (12-client secondary model) ===")
    r12 = calibrate(12, 8)
    print_lane_report(r12["lanes"])

    print("\n\n=== Illustrative scenario, NOT a committed figure: zero clients select Nails at N=18 ===")
    print("Demonstrates the founder's 'no staff rostered for zero demand' requirement directly.")
    lanes_zero_nails = scenario_reduced_nail_demand(18)
    for line in LINES:
        count = len(lanes_zero_nails.get(line, []))
        print(f"  {line}: {count} staff required")
    if len(lanes_zero_nails.get("Nails", [])) == 0:
        print("  CONFIRMED: zero Nails staff rostered when zero clients select Nails.")


if __name__ == "__main__":
    main()
