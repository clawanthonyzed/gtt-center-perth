"""
Reproduction tests for tools/am_volume_tier_staffing_solver.py.

Purpose: prove the odd-client-count extension reproduces the already-
published, verified 8-staff figure at N=12/N=18 before trusting it on the
new, lower-volume tiers, and confirm the specific headcount finding
(only the 9.00/day tier can drop treatment headcount to 4, all others
stay at 8) is stable and deterministic.

Run:
    python -m unittest tests.test_am_volume_tier_staffing_solver -v
    (from repo root)
"""

import importlib.util
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOLVER_PATH = REPO_ROOT / "tools" / "am_volume_tier_staffing_solver.py"

_spec = importlib.util.spec_from_file_location("am_volume_tier_staffing_solver", SOLVER_PATH)
solver = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(solver)


class CalibrationTests(unittest.TestCase):
    """The odd-count extension must reproduce the already-published, even-N
    committed figures exactly before its new-tier output can be trusted."""

    def test_n12_at_25min_cadence_matches_published_table2(self):
        r = solver.assign_and_check_odd(12, 25)
        self.assertEqual(r["peak_by_line"], {"MB": 4, "Nails": 2, "Hair": 2})
        self.assertEqual(r["total_headcount"], 8)

    def test_n18_at_25min_cadence_matches_published_table1(self):
        r = solver.assign_and_check_odd(18, 25)
        self.assertEqual(r["peak_by_line"], {"MB": 4, "Nails": 2, "Hair": 2})
        self.assertEqual(r["total_headcount"], 8)

    def test_phlebotomist_peak_is_2_at_both_calibration_points(self):
        self.assertEqual(solver.phlebotomist_headcount_check_odd(12, 25), 2)
        self.assertEqual(solver.phlebotomist_headcount_check_odd(18, 25), 2)


class OddClientCountTests(unittest.TestCase):
    """The new odd-count support must produce a valid, collision-free
    schedule (verified by the same sweep-line peak-concurrency method the
    even-count solver already uses)."""

    def test_n9_builds_9_clients_with_one_single_chair_slot(self):
        clients = solver.build_clients_odd(9, 45)
        self.assertEqual(len(clients), 9)
        chair_a_count = sum(1 for c in clients if c["chair"] == "A")
        chair_b_count = sum(1 for c in clients if c["chair"] == "B")
        self.assertEqual(chair_a_count, 5)
        self.assertEqual(chair_b_count, 4)

    def test_n9_at_45min_cadence_reduces_headcount_to_4(self):
        r = solver.assign_and_check_odd(9, 45)
        self.assertEqual(r["peak_by_line"], {"MB": 2, "Nails": 1, "Hair": 1})
        self.assertEqual(r["total_headcount"], 4)

    def test_n9_at_25min_cadence_still_needs_8(self):
        r = solver.assign_and_check_odd(9, 25)
        self.assertEqual(r["total_headcount"], 8)


class VolumeTierLadderTests(unittest.TestCase):
    """The 5 profitability-ladder volumes -- confirms the genuine, disclosed
    finding: only the lowest tier (9.00/day) can reduce treatment headcount
    below 8 within the WDP guidance window, and only via a widened
    (45min+) cadence, not yet a founder decision."""

    def test_9_00_reduces_to_4_treatment_staff(self):
        r = solver.minimum_headcount_for_volume(9.00)
        self.assertEqual(r["rostered_for_n_clients"], 9)
        self.assertEqual(r["treatment_headcount"], 4)
        self.assertEqual(r["phlebotomist_headcount"], 2)
        self.assertGreaterEqual(r["chosen_cadence_minutes"], 45)

    def test_11_29_requires_8_treatment_staff(self):
        r = solver.minimum_headcount_for_volume(11.29)
        self.assertEqual(r["rostered_for_n_clients"], 12)
        self.assertEqual(r["treatment_headcount"], 8)

    def test_13_50_requires_8_treatment_staff(self):
        r = solver.minimum_headcount_for_volume(13.50)
        self.assertEqual(r["rostered_for_n_clients"], 14)
        self.assertEqual(r["treatment_headcount"], 8)

    def test_15_50_requires_8_treatment_staff(self):
        r = solver.minimum_headcount_for_volume(15.50)
        self.assertEqual(r["rostered_for_n_clients"], 16)
        self.assertEqual(r["treatment_headcount"], 8)

    def test_18_00_requires_8_treatment_staff_committed(self):
        r = solver.minimum_headcount_for_volume(18.00)
        self.assertEqual(r["rostered_for_n_clients"], 18)
        self.assertEqual(r["treatment_headcount"], 8)
        self.assertEqual(r["chosen_cadence_minutes"], 25)

    def test_phlebotomist_headcount_unaffected_at_every_tier(self):
        for vol in solver.TARGET_VOLUMES:
            r = solver.minimum_headcount_for_volume(vol)
            self.assertEqual(r["phlebotomist_headcount"], 2)

    def test_every_tier_clears_wdp_guidance_window(self):
        for vol in solver.TARGET_VOLUMES:
            r = solver.minimum_headcount_for_volume(vol)
            self.assertLessEqual(r["last_draw1_minute"], solver.WDP_GUIDANCE_WINDOW_MINUTES)


class WDPGuidanceWindowTests(unittest.TestCase):
    def test_max_feasible_cadence_at_18_clients_matches_committed_25min(self):
        self.assertEqual(solver.max_feasible_cadence(18), 25)

    def test_max_feasible_cadence_at_9_clients_allows_widening_to_50(self):
        self.assertEqual(solver.max_feasible_cadence(9), 50)


if __name__ == "__main__":
    unittest.main()
