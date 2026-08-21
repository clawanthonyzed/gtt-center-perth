"""
Regression tests for the Canonical Startup Cost Adoption phase (2026-08-10).

Pins down: the new adopted_planning_scenarios record in
data/canonical/startup_costs.yml reconciles internally (component_breakdown
sums to the stated total), the pre-existing historical_total_estimates
records were NOT deleted or altered, and
data/models/master_financial_model.yml's new updated_planning_case_2026_08_10
section combines the new pre-opening-capital planning figure with the
UNCHANGED working-capital reserve range without touching the previous
bounded range (combined_funding_requirement_bounded.primary_method).

Run:
    python tests/test_startup_cost_mvp_adoption.py
    (or: python -m unittest tests.test_startup_cost_mvp_adoption -v, from repo root)
"""

import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CANON_DIR = REPO_ROOT / "data" / "canonical"
MODELS_DIR = REPO_ROOT / "data" / "models"


def load_yaml(path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find(records, record_id):
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


class AdoptedPlanningScenarioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startup_costs = load_yaml(CANON_DIR / "startup_costs.yml")

    def test_adopted_planning_scenarios_list_exists(self):
        self.assertIn("adopted_planning_scenarios", self.startup_costs)
        self.assertIsInstance(self.startup_costs["adopted_planning_scenarios"], list)
        self.assertEqual(len(self.startup_costs["adopted_planning_scenarios"]), 1)

    def test_new_record_total_matches_founder_review(self):
        rec = find(self.startup_costs["adopted_planning_scenarios"], "startup_mvp_adopted_planning_2026_08_10")
        self.assertEqual(rec["total_cost"], 251198.00)
        self.assertEqual(rec["status"], "DECIDED")
        self.assertIn("source", rec)
        self.assertTrue(rec["source"].get("file"))

    def test_component_breakdown_reconciles_to_total(self):
        rec = find(self.startup_costs["adopted_planning_scenarios"], "startup_mvp_adopted_planning_2026_08_10")
        cb = rec["component_breakdown"]
        category_keys = [
            "premises_acquisition", "design_and_approvals", "fitout",
            "furniture_fixtures_fittings", "equipment", "opening_inventory_consumables",
            "technology_systems", "staffing_before_opening", "marketing_and_launch",
            "professional_services",
        ]
        subtotal = round(sum(cb[k] for k in category_keys), 2)
        self.assertEqual(subtotal, cb["subtotal_before_contingency"])
        self.assertEqual(round(subtotal + cb["contingency_12pct"], 2), cb["total"])
        self.assertEqual(cb["total"], rec["total_cost"])

    def test_contingency_is_twelve_percent(self):
        rec = find(self.startup_costs["adopted_planning_scenarios"], "startup_mvp_adopted_planning_2026_08_10")
        cb = rec["component_breakdown"]
        expected_contingency = round(cb["subtotal_before_contingency"] * 0.12, 2)
        self.assertAlmostEqual(cb["contingency_12pct"], expected_contingency, delta=1.00)

    def test_previous_historical_totals_not_deleted_or_altered(self):
        """Every historical_total_estimates record must still exist, unchanged."""
        hist = self.startup_costs["historical_total_estimates"]
        component_sum = find(hist, "total_current_state_component_sum")
        self.assertEqual(component_sum["total_cost"], {"low": 357390.00, "high": 577180.00})
        adopted = find(hist, "total_current_state_adopted")
        self.assertEqual(adopted["total_cost"], {"low": 292335.00, "high": 594900.00})
        # Spot-check the full original count is unchanged (9 historical records).
        self.assertEqual(len(hist), 9)

    def test_funding_working_capital_reserve_untouched(self):
        wc = find(self.startup_costs["funding_requirements"], "funding_working_capital_reserve")
        self.assertEqual(wc["total_cost"], {"low": 85000.00, "high": 110000.00})


class UpdatedPlanningCaseModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = load_yaml(MODELS_DIR / "master_financial_model.yml")
        cls.fri = cls.model["funding_requirement_investigation"]

    def test_previous_bounded_range_unchanged(self):
        primary = self.fri["combined_funding_requirement_bounded"]["primary_method"]
        self.assertEqual(primary["range_low"], 357390.00)
        self.assertEqual(primary["range_high"], 577180.00)

    def test_updated_planning_case_exists_and_reconciles(self):
        case = self.fri["updated_planning_case_2026_08_10"]
        self.assertEqual(case["revised_pre_opening_capital"]["value"], 251198.00)
        combined = case["combined_updated_planning_case"]
        self.assertEqual(combined["range_low"], 251198.00 + 85000.00)
        self.assertEqual(combined["range_high"], 251198.00 + 110000.00)

    def test_operating_cash_trough_figures_untouched(self):
        """The updated planning case (this phase) must not itself have altered
        the Master Financial Model's cash-flow trough figures -- those remain
        sourced only from cash_flow_summary, never recalculated by THIS phase.
        RECALCULATED 2026-08-21 (later same day -- Position 06/RCO01
        dedicated PM Reception REMOVED, per Anthony's direct founder
        decision) -- was 64275.46/117360.02 earlier the same day (relief_
        absence_allowance reverted to 0.00), 76532.52/172138.34 under the
        2026-08-18 relief-allowance-added version before that (itself was
        63658.78/116126.66 under the Priority 1 PM capacity/transaction
        reconciliation, 54016.81/96821.83 under the 2026-08-18 VM wage audit
        correction, 52363.17/94341.40 under the 2026-08-17 first-principles
        rebuild, 34860.52/74110.43 under the same-day proportional-wage-
        scaling recompute before that). Legitimately moved again by this
        round's real, founder-directed correction (a separate, later,
        authorised phase) -- this test's own guard (this specific phase
        didn't touch them) is unaffected by that different phase's change.
        Table 2's trough is now Month 3, within the historical reserve's
        own upper bound for the first time under any 2026-08-18-or-later
        cost base."""
        results = self.fri["opening_working_capital"]["operating_cash_trough_cross_check"]["results"]
        t1 = next(r for r in results if r["scenario_id"] == "scenario_table_1")
        t2 = next(r for r in results if r["scenario_id"] == "scenario_table_2")
        self.assertEqual(t1["trough_value"], 53353.76)
        self.assertEqual(t2["trough_value"], 98125.17)


if __name__ == "__main__":
    unittest.main()
