"""
Reproduction tests for tools/demand_scenario_financial_model.py.

Purpose: prove this module's headcount-parameterized cost computation
reproduces tools/cost_ramp_model.py's own published constants exactly at
the committed headcount, reproduces the published 18/12/6-client
committed-cadence P&L figures (Chapters 27/28/31) exactly, and reproduces
Chapter 31's own demand-flexed 6-client figures exactly, making a
previously dossier-only calculation into a tested, reproducible one.

Run:
    python -m pytest tests/test_demand_scenario_financial_model.py -v
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


dsfm = _load("demand_scenario_financial_model", "demand_scenario_financial_model.py")


class TestCalibration(unittest.TestCase):
    def test_reproduces_cost_ramp_model_published_constants(self):
        checks, all_match = dsfm.calibrate()
        self.assertTrue(all_match)


class TestCommittedCadenceScenarios(unittest.TestCase):
    """Reproduces the already-published Chapter 27/28/31 figures exactly at
    8 treatment staff (4 MB + 2 Nails + 2 Hair), for all three client
    volumes, confirming this module agrees with the existing tested
    financial model before trusting its demand-flexed output."""

    def _run(self, volume):
        pricing = dsfm.crm.load_yaml("pricing.yml")
        am_price = dsfm.crm.find_record(pricing["records"], "am_price_used_for_revenue")["price"]
        return dsfm.compute_scenario(4, 2, 2, am_price, volume, 24585.37, 0.0)

    def test_18_clients_matches_published(self):
        """RECOMPUTED 2026-09-19 (Venue Manager Mon-Fri, PM Model E 10
        sessions/day) -- was total_revenue 154710.69/opex 110544.52/result
        44166.17."""
        r = self._run(18)
        self.assertAlmostEqual(r["total_revenue"], 143070.37, places=2)
        self.assertAlmostEqual(r["total_operating_costs"], 107883.97, places=2)
        self.assertAlmostEqual(r["net_operating_result"], 35186.40, places=2)

    def test_12_clients_matches_published(self):
        """RECOMPUTED 2026-09-19 -- was total_revenue 115215.69/result
        4671.17. Genuine finding: at the recomputed PM revenue and Venue
        Manager cost, 12/day at the committed 8-staff headcount is now
        LOSS-MAKING (result flips negative), not marginally profitable."""
        r = self._run(12)
        self.assertAlmostEqual(r["total_revenue"], 103575.37, places=2)
        self.assertAlmostEqual(r["total_operating_costs"], 107883.97, places=2)
        self.assertAlmostEqual(r["net_operating_result"], -4308.60, places=2)

    def test_6_clients_matches_published(self):
        """RECOMPUTED 2026-09-19 -- was total_revenue 75720.69/result
        -34823.83."""
        r = self._run(6)
        self.assertAlmostEqual(r["total_revenue"], 64080.37, places=2)
        self.assertAlmostEqual(r["total_operating_costs"], 107883.97, places=2)
        self.assertAlmostEqual(r["net_operating_result"], -43803.60, places=2)


class TestDemandFlexedScenario(unittest.TestCase):
    """Reproduces Chapter 31's own published demand-flexed 6-client figures
    exactly (2 Massage+Beauty + 1 Nail + 1 Hair, Saturday treatment held at
    the committed level per Chapter 31's own disclosed scope)."""

    def test_6_clients_demand_flexed_matches_published(self):
        """RECOMPUTED 2026-09-19 -- was total_operating_costs 88239.03 /
        net_operating_result -12518.34, under the pre-rebuild PM/VM model."""
        pricing = dsfm.crm.load_yaml("pricing.yml")
        am_price = dsfm.crm.find_record(pricing["records"], "am_price_used_for_revenue")["price"]
        r = dsfm.compute_scenario(2, 1, 1, am_price, 6, 24585.37, 0.0)
        self.assertAlmostEqual(r["total_operating_costs"], 85578.48, places=2)
        self.assertAlmostEqual(r["net_operating_result"], -21498.11, places=2)
        self.assertEqual(r["am_treatment_headcount"], 4)

    def test_saturday_scope_matches_chapter_31_disclosure(self):
        """Confirms that flexing weekday headcount alone (without also
        flexing Saturday) is what reproduces this module's own committed
        scope -- a genuine discrepancy was found and fixed when the module
        initially (incorrectly) flexed Saturday too. RECOMPUTED 2026-09-19:
        was total_operating_costs 88239.03 (pre-rebuild PM/VM model)."""
        pricing = dsfm.crm.load_yaml("pricing.yml")
        am_price = dsfm.crm.find_record(pricing["records"], "am_price_used_for_revenue")["price"]
        flexed_saturday_too = dsfm.compute_scenario(
            2, 1, 1, am_price, 6, 24585.37, 0.0, saturday_headcount=(2, 1, 1)
        )
        weekday_only_flexed = dsfm.compute_scenario(2, 1, 1, am_price, 6, 24585.37, 0.0)
        self.assertNotAlmostEqual(
            flexed_saturday_too["total_operating_costs"],
            weekday_only_flexed["total_operating_costs"],
            places=2,
        )
        self.assertAlmostEqual(weekday_only_flexed["total_operating_costs"], 85578.48, places=2)


if __name__ == "__main__":
    unittest.main()
