"""
Reproduction tests for tools/am_demand_tier_financial_ladder.py.

Purpose: confirm the HIGH-headcount tier (the committed 8-treatment-staff
model) reproduces data/canonical/cost_ramp.yml's and revenue_ramp.yml's own
Table 1 M5plus figures EXACTLY (this tool must not silently diverge from the
canonical layer it's built to summarise), and that every payroll breakdown
sums exactly to its own displayed total, per Anthony's explicit instruction.

Run:
    python -m unittest tests.test_am_demand_tier_financial_ladder -v
    (from repo root)
"""

import importlib.util
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CANON_DIR = REPO_ROOT / "data" / "canonical"
LADDER_PATH = REPO_ROOT / "tools" / "am_demand_tier_financial_ladder.py"

_spec = importlib.util.spec_from_file_location("am_demand_tier_financial_ladder", LADDER_PATH)
ladder = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ladder)


def load_yaml(filename):
    with (CANON_DIR / filename).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_record(records, record_id):
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


class CalibrationAgainstCanonicalLayerTests(unittest.TestCase):
    def test_high_tier_total_opex_matches_cost_ramp_table1_m5plus(self):
        payroll = ladder.payroll_for_headcount(*ladder.HIGH_HEADCOUNT)
        cost_ramp = load_yaml("cost_ramp.yml")
        rec = find_record(cost_ramp["records"], "cost_table1_m5plus")
        self.assertAlmostEqual(payroll["total_opex"], rec["total_operating_costs"], places=2)
        self.assertAlmostEqual(payroll["payroll_total"], rec["payroll_costs"], places=2)

    def test_18_00_row_matches_revenue_ramp_table1_m5plus(self):
        row = ladder.ladder_row(18.00)
        revenue_ramp = load_yaml("revenue_ramp.yml")
        rec = find_record(revenue_ramp["records"], "ramp_table1_m5plus")
        self.assertAlmostEqual(row["total_revenue"], rec["total_revenue"], places=2)
        self.assertAlmostEqual(row["am_revenue"], rec["am_revenue"], places=2)
        self.assertAlmostEqual(row["pm_revenue"], rec["pm_revenue"], places=2)


class PayrollAdditivityTests(unittest.TestCase):
    """Anthony's explicit instruction: role-by-role components must sum
    exactly to the displayed payroll total, at every volume tested."""

    def test_low_tier_lines_sum_to_direct_labor_total(self):
        payroll = ladder.payroll_for_headcount(*ladder.LOW_HEADCOUNT)
        self.assertAlmostEqual(sum(payroll["lines"].values()), payroll["direct_labor_and_opening"], places=2)

    def test_high_tier_lines_sum_to_direct_labor_total(self):
        payroll = ladder.payroll_for_headcount(*ladder.HIGH_HEADCOUNT)
        self.assertAlmostEqual(sum(payroll["lines"].values()), payroll["direct_labor_and_opening"], places=2)

    def test_payroll_total_equals_direct_labor_plus_super_plus_workers_comp(self):
        for hc in (ladder.LOW_HEADCOUNT, ladder.HIGH_HEADCOUNT):
            payroll = ladder.payroll_for_headcount(*hc)
            expected = round(payroll["direct_labor_and_opening"] + payroll["superannuation"] + payroll["workers_comp"], 2)
            self.assertAlmostEqual(payroll["payroll_total"], expected, places=2)


class LadderFindingTests(unittest.TestCase):
    """The genuine, disclosed finding: only 9.00/day drops below the
    committed 8-staff headcount; the middle tiers (11.29-15.50) are all
    costed at the same HIGH total_opex as the 18.00 committed tier."""

    def test_9_00_uses_low_headcount_and_is_profitable(self):
        row = ladder.ladder_row(9.00)
        self.assertEqual(row["treatment_headcount"], 4)
        self.assertGreater(row["operating_profit"], 0)

    def test_11_29_uses_high_headcount_and_is_loss_making(self):
        """A genuine finding, not previously modelled: at the recomputed PM
        revenue and Venue Manager cost, 11.29/day (which requires the full
        8-staff HIGH tier) no longer breaks even -- the old 11.29 break-even
        figure is stale post-rebuild."""
        row = ladder.ladder_row(11.29)
        self.assertEqual(row["treatment_headcount"], 8)
        self.assertLess(row["operating_profit"], 0)

    def test_profit_increases_monotonically_within_the_high_tier(self):
        rows = [ladder.ladder_row(v) for v in (11.29, 13.50, 15.50, 18.00)]
        profits = [r["operating_profit"] for r in rows]
        self.assertEqual(profits, sorted(profits))

    def test_18_00_remains_the_most_profitable_committed_tier(self):
        row18 = ladder.ladder_row(18.00)
        for v in (9.00, 11.29, 13.50, 15.50):
            self.assertGreater(row18["operating_profit"], ladder.ladder_row(v)["operating_profit"])


class BreakevenTests(unittest.TestCase):
    def test_low_segment_breakeven_is_within_its_own_valid_range(self):
        be = ladder.breakeven_for_headcount(*ladder.LOW_HEADCOUNT, valid_range=(0, 10.4))
        self.assertTrue(be["in_valid_range"])

    def test_high_segment_breakeven_is_within_its_own_valid_range(self):
        be = ladder.breakeven_for_headcount(*ladder.HIGH_HEADCOUNT, valid_range=(10.4, 18.0))
        self.assertTrue(be["in_valid_range"])

    def test_high_segment_breakeven_exceeds_old_11_29_figure(self):
        """The old, pre-rebuild break-even (11.290/day) is now stale -- the
        recomputed HIGH-segment break-even must be materially higher, not
        approximately the same, confirming this is a genuine finding, not
        noise."""
        be = ladder.breakeven_for_headcount(*ladder.HIGH_HEADCOUNT, valid_range=(10.4, 18.0))
        self.assertGreater(be["breakeven_am_client_volume_per_day"], 12.0)


if __name__ == "__main__":
    unittest.main()
