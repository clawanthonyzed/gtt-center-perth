"""
Reproduction tests for tools/pm_solver.py.

Purpose: prove the PM solver's illustrative canonical-volume schedule
reproduces the committed 1-staff-per-line PM structure
(data/canonical/staffing.yml staff_pm_massage/hair/nail/beauty), that PM
Restore's two halves are genuinely sequential (never concurrent) for the
same client as the founder directly instructed, that no booking overlaps
within any single staff member's own lane, and that a genuine peak-period
concurrent-demand scenario correctly requires more than one staff member
on the affected lines.

Run:
    python -m pytest tests/test_pm_solver.py -v
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


pm_solver = _load("pm_solver", "pm_solver.py")


class TestCalibration(unittest.TestCase):
    def test_canonical_volume_matches_committed_one_per_line(self):
        per_line, matches, _ = pm_solver.calibrate()
        self.assertTrue(matches)
        for line in pm_solver.LINES:
            self.assertLessEqual(per_line[line], 1)


class TestRestoreSequencing(unittest.TestCase):
    def test_restore_halves_are_sequential_never_concurrent(self):
        """Directly verifies the founder's instruction: PM Restore's two
        components (Nails then Hair) must never run concurrently for the
        same client. Confirms the Hair half's start is always exactly at
        or after the paired Nails half's end."""
        bookings = pm_solver.generate_illustrative_schedule()
        nails_restore = sorted(
            (b for b in bookings["Nails"] if "Restore" in b[3]), key=lambda b: b[0]
        )
        hair_restore = sorted(
            (b for b in bookings["Hair"] if "Restore" in b[3]), key=lambda b: b[0]
        )
        self.assertEqual(len(nails_restore), len(hair_restore))
        for nails_b, hair_b in zip(nails_restore, hair_restore):
            self.assertEqual(
                hair_b[0], nails_b[1],
                "Hair-half start must equal Nails-half end (sequential, not concurrent)",
            )


class TestLaneCorrectness(unittest.TestCase):
    def test_no_staff_member_has_overlapping_bookings(self):
        _, _, lanes = pm_solver.calibrate()
        for line, line_lanes in lanes.items():
            for lane in line_lanes:
                bks = sorted(lane["bookings"], key=lambda b: b[0])
                for i in range(1, len(bks)):
                    self.assertLessEqual(
                        bks[i - 1][1], bks[i][0],
                        f"Overlap found in {line} lane: {bks[i-1]} vs {bks[i]}",
                    )

    def test_every_booking_assigned_exactly_once(self):
        bookings = pm_solver.generate_illustrative_schedule()
        lanes = pm_solver.solve(bookings)
        for line in pm_solver.LINES:
            original_ids = sorted(b[2] for b in bookings[line])
            lane_ids = sorted(b[2] for lane in lanes[line] for b in lane["bookings"])
            self.assertEqual(original_ids, lane_ids)


class TestDemandScaling(unittest.TestCase):
    def test_peak_period_requires_more_than_one_staff_on_affected_lines(self):
        """Illustrative, not a committed figure: a genuine peak-period
        cluster of concurrent arrivals on Nails and Hair must require more
        than 1 staff member on those specific lines, confirming the
        solver's demand-driven behaviour (2-3 staff per role when demand
        genuinely supports it), while lines unaffected by the peak
        (Massage, Beauty) remain at 1."""
        per_line, _ = pm_solver.demand_scaling_scenario()
        self.assertGreater(per_line["Nails"], 1)
        self.assertGreater(per_line["Hair"], 1)
        self.assertEqual(per_line["Massage"], 1)
        self.assertEqual(per_line["Beauty"], 1)


if __name__ == "__main__":
    unittest.main()
