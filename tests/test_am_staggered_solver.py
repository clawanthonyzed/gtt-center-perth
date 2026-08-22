"""
Reproduction tests for tools/am_staggered_staffing_solver.py.

Purpose: prove the individual staff-lane assignment (interval partitioning)
reproduces the same total headcount as the already-calibrated
tools/demand_driven_staffing_solver.py at N=12 and N=18, that no single
staff member's lane contains overlapping bookings (a genuine correctness
check on the new assignment code, not just a headcount count), and that
the demand-driven "zero staff for zero demand" behaviour holds.

Run:
    python -m pytest tests/test_am_staggered_solver.py -v
    (or: python tests/test_am_staggered_solver.py)
"""

import importlib.util
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = REPO_ROOT / "tools"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, TOOLS_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


demand_solver = _load("demand_driven_staffing_solver", "demand_driven_staffing_solver.py")
lane_solver = _load("am_staggered_staffing_solver", "am_staggered_staffing_solver.py")


class TestCalibration(unittest.TestCase):
    def test_n18_matches_published_8_staff(self):
        r = lane_solver.calibrate(18, 8)
        self.assertTrue(r["matches"])
        self.assertEqual(r["total_staff"], 8)
        self.assertEqual(r["per_line"], {"MB": 4, "Nails": 2, "Hair": 2})

    def test_n12_matches_published_8_staff(self):
        r = lane_solver.calibrate(12, 8)
        self.assertTrue(r["matches"])
        self.assertEqual(r["total_staff"], 8)
        self.assertEqual(r["per_line"], {"MB": 4, "Nails": 2, "Hair": 2})

    def test_lane_count_matches_independently_verified_peak_concurrency(self):
        """Cross-checks the new lane-assignment tool's per-line staff count
        against demand_driven_staffing_solver's own independently-verified
        (two-method) peak concurrency, for both N=12 and N=18."""
        for n in (12, 18):
            expected = demand_solver.assign_and_check(n)
            r = lane_solver.calibrate(n, expected["total_headcount"])
            self.assertEqual(r["per_line"], expected["peak_by_line"])
            self.assertTrue(expected["methods_agree"])


class TestLaneCorrectness(unittest.TestCase):
    def test_no_staff_member_has_overlapping_bookings(self):
        """A genuine correctness check on the new interval-partitioning
        code: no single staff member's own lane may contain two bookings
        that overlap in time."""
        for n in (12, 18):
            r = lane_solver.calibrate(n, 8)
            for line, lanes in r["lanes"].items():
                for lane in lanes:
                    bookings = sorted(lane["bookings"], key=lambda b: b[0])
                    for i in range(1, len(bookings)):
                        prev_end = bookings[i - 1][1]
                        cur_start = bookings[i][0]
                        self.assertLessEqual(
                            prev_end, cur_start,
                            f"Overlap found in {line} lane at N={n}: "
                            f"{bookings[i-1]} vs {bookings[i]}",
                        )

    def test_every_booking_assigned_exactly_once(self):
        """Every original booking (from the fixed-pattern assignment) must
        appear in exactly one staff lane, no booking dropped, none
        duplicated."""
        for n in (12, 18):
            clients = demand_solver.build_clients(n)
            original_bookings = lane_solver.fixed_pattern_assignment(clients)
            lanes = lane_solver.assign_staff_lanes(original_bookings)
            for line in demand_solver.LINES:
                original_ids = sorted(b[2] for b in original_bookings[line])
                lane_ids = sorted(
                    b[2] for lane in lanes[line] for b in lane["bookings"]
                )
                self.assertEqual(original_ids, lane_ids)


class TestDemandResponsiveness(unittest.TestCase):
    def test_zero_nail_selections_produces_zero_nail_staff(self):
        """Illustrative scenario, not a committed figure: if zero clients
        select a Nails service, the solver must not roster any Nails
        staff. Confirms the founder's explicit 'no staff rostered for zero
        demand' requirement."""
        lanes = lane_solver.scenario_reduced_nail_demand(18)
        self.assertEqual(len(lanes.get("Nails", [])), 0)
        # MB and Hair demand must still be fully covered (no client dropped).
        self.assertEqual(len(lanes.get("MB", [])), 4)
        self.assertEqual(len(lanes.get("Hair", [])), 4)


if __name__ == "__main__":
    unittest.main()
