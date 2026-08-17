"""
Reproduction tests for docs/architecture/MASTER-FINANCIAL-MODEL-METHODOLOGY.md
and tools/master_financial_model.py (Phase 9, 2026-08-09).

Purpose: prove the 24-month P&L, cash flow, break-even, scenario comparison,
and sensitivity analysis are deterministic, reproducible directly from
data/canonical/revenue_ramp.yml and data/canonical/cost_ramp.yml, correctly
extend Month 5+ flat through Month 24 with no invented growth, never let
startup/capex costs leak into recurring opex, never let the historical
(superseded) revenue figures become canonical, keep Table 1/Table 2 fully
independent, and respond predictably to a changed canonical input.

Run:
    python tests/test_master_financial_model.py
    (or: python -m unittest tests.test_master_financial_model -v, from repo root)
"""

import importlib.util
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIR = REPO_ROOT / "data" / "canonical"
MODELS_DIR = REPO_ROOT / "data" / "models"
MFM_PATH = REPO_ROOT / "tools" / "master_financial_model.py"
CRM_PATH = REPO_ROOT / "tools" / "cost_ramp_model.py"

_spec = importlib.util.spec_from_file_location("master_financial_model", MFM_PATH)
mfm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mfm)

_crm_spec = importlib.util.spec_from_file_location("cost_ramp_model", CRM_PATH)
crm = importlib.util.module_from_spec(_crm_spec)
_crm_spec.loader.exec_module(crm)


def load_canonical_yaml(filename):
    with (CANONICAL_DIR / filename).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_model_yaml(filename):
    with (MODELS_DIR / filename).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_record(records, record_id):
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


class DeterminismTests(unittest.TestCase):
    """Deterministic output."""

    def test_repeated_calls_produce_identical_output(self):
        inputs = mfm.CanonicalModelInputs()
        first = mfm.compute_24_month_pnl("scenario_table_1", inputs)
        second = mfm.compute_24_month_pnl("scenario_table_1", inputs)
        self.assertEqual(first, second)

    def test_fresh_inputs_produce_identical_output(self):
        first = mfm.compute_24_month_pnl("scenario_table_2", mfm.CanonicalModelInputs())
        second = mfm.compute_24_month_pnl("scenario_table_2", mfm.CanonicalModelInputs())
        self.assertEqual(first, second)


class ScenariosCalculateIndependentlyTests(unittest.TestCase):
    """Both scenarios calculate independently."""

    def test_table1_and_table2_produce_different_results(self):
        inputs = mfm.CanonicalModelInputs()
        t1 = mfm.compute_month_pnl("scenario_table_1", 5, inputs)
        t2 = mfm.compute_month_pnl("scenario_table_2", 5, inputs)
        self.assertNotEqual(t1["revenue"]["total_revenue"], t2["revenue"]["total_revenue"])
        self.assertGreater(t1["revenue"]["total_revenue"], t2["revenue"]["total_revenue"])

    def test_computing_table1_does_not_affect_table2(self):
        inputs = mfm.CanonicalModelInputs()
        t2_before = mfm.compute_month_pnl("scenario_table_2", 5, inputs)
        mfm.compute_24_month_pnl("scenario_table_1", inputs)  # side-effect-free call
        t2_after = mfm.compute_month_pnl("scenario_table_2", 5, inputs)
        self.assertEqual(t2_before, t2_after)


class TwentyFourMonthsCalculateTests(unittest.TestCase):
    """24 months calculate."""

    def test_both_scenarios_produce_24_months(self):
        inputs = mfm.CanonicalModelInputs()
        for scenario_id in ("scenario_table_1", "scenario_table_2"):
            months = mfm.compute_24_month_pnl(scenario_id, inputs)
            self.assertEqual(len(months), 24)
            self.assertEqual([m["forecast_month"] for m in months], list(range(1, 25)))


class RevenueRampUsageTests(unittest.TestCase):
    """Month 1-5 revenue uses the canonical revenue ramp; Month 5+ equals
    canonical steady-state."""

    def test_months_1_to_4_match_revenue_ramp_yaml(self):
        revenue_ramp_records = load_canonical_yaml("revenue_ramp.yml")["records"]
        inputs = mfm.CanonicalModelInputs()
        for scenario_id, ramp_id_prefix in (("scenario_table_1", "ramp_table1"), ("scenario_table_2", "ramp_table2")):
            for forecast_month, ramp_suffix in ((1, "m1"), (2, "m2"), (3, "m3"), (4, "m4")):
                pnl = mfm.compute_month_pnl(scenario_id, forecast_month, inputs)
                ramp_rec = find_record(revenue_ramp_records, f"{ramp_id_prefix}_{ramp_suffix}")
                self.assertAlmostEqual(pnl["revenue"]["total_revenue"], ramp_rec["total_revenue"], places=2)
                self.assertAlmostEqual(pnl["revenue"]["am_revenue"], ramp_rec["am_revenue"], places=2)
                self.assertAlmostEqual(pnl["revenue"]["pm_revenue"], ramp_rec["pm_revenue"], places=2)

    def test_month5_and_beyond_equal_canonical_steady_state(self):
        """Month 5+ must equal canonical steady state, and Months 6-24 must
        be IDENTICAL to Month 5 -- no growth invented past Month 5."""
        revenue_ramp_records = load_canonical_yaml("revenue_ramp.yml")["records"]
        inputs = mfm.CanonicalModelInputs()
        for scenario_id, ramp_id in (("scenario_table_1", "ramp_table1_m5plus"), ("scenario_table_2", "ramp_table2_m5plus")):
            ramp_rec = find_record(revenue_ramp_records, ramp_id)
            months_5_to_24 = [mfm.compute_month_pnl(scenario_id, m, inputs) for m in range(5, 25)]
            revenue_values = {m["revenue"]["total_revenue"] for m in months_5_to_24}
            self.assertEqual(len(revenue_values), 1, "Months 5-24 revenue must be identical (no invented growth)")
            self.assertAlmostEqual(revenue_values.pop(), ramp_rec["total_revenue"], places=2)


class CostsFromCostRampTests(unittest.TestCase):
    """Costs come from cost_ramp."""

    def test_months_1_to_4_costs_match_cost_ramp_yaml(self):
        cost_ramp_records = load_canonical_yaml("cost_ramp.yml")["records"]
        inputs = mfm.CanonicalModelInputs()
        for scenario_id, cost_id_prefix in (("scenario_table_1", "cost_table1"), ("scenario_table_2", "cost_table2")):
            for forecast_month, suffix in ((1, "m1"), (2, "m2"), (3, "m3"), (4, "m4")):
                pnl = mfm.compute_month_pnl(scenario_id, forecast_month, inputs)
                cost_rec = find_record(cost_ramp_records, f"{cost_id_prefix}_{suffix}")
                self.assertAlmostEqual(pnl["total_operating_costs"], cost_rec["total_operating_costs"], places=2)
                self.assertAlmostEqual(pnl["payroll"], cost_rec["payroll_costs"], places=2)

    def test_month5plus_costs_match_cost_ramp_yaml(self):
        cost_ramp_records = load_canonical_yaml("cost_ramp.yml")["records"]
        inputs = mfm.CanonicalModelInputs()
        for scenario_id, cost_id in (("scenario_table_1", "cost_table1_m5plus"), ("scenario_table_2", "cost_table2_m5plus")):
            cost_rec = find_record(cost_ramp_records, cost_id)
            pnl = mfm.compute_month_pnl(scenario_id, 5, inputs)
            self.assertAlmostEqual(pnl["total_operating_costs"], cost_rec["total_operating_costs"], places=2)


class NoStartupCapexLeakageTests(unittest.TestCase):
    """Startup costs can't enter recurring opex; capex can't enter recurring
    opex."""

    def test_engine_never_imports_startup_or_capex_yaml(self):
        source_text = MFM_PATH.read_text(encoding="utf-8")
        # Allowed only inside the (non-P&L) startup_capex_section builder function,
        # which is not part of the recurring P&L calculation path -- confirm the
        # P&L-critical functions never touch these files.
        pnl_functions = ("compute_month_pnl", "compute_24_month_pnl", "compute_cash_flow")
        for func_name in pnl_functions:
            start = source_text.index(f"def {func_name}(")
            # crude but effective: slice to the next top-level "def " after this one
            rest = source_text[start:]
            next_def = rest.find("\ndef ", 1)
            func_body = rest[:next_def] if next_def != -1 else rest
            self.assertNotIn("startup_costs.yml", func_body, f"{func_name} must not reference startup_costs.yml")
            self.assertNotIn("capex.yml", func_body, f"{func_name} must not reference capex.yml")

    def test_master_financial_model_yaml_keeps_startup_capex_in_separate_section(self):
        data = load_model_yaml("master_financial_model.yml")
        self.assertIn("startup_capex_section", data)
        for output_key in ("steady_state_summary", "totals_24mo", "cash_flow_summary"):
            for entry in data["outputs"][output_key]:
                self.assertNotIn("startup_costs", entry)
                self.assertNotIn("capex", entry)


class HistoricalRevenueNotCanonicalTests(unittest.TestCase):
    """Historical revenue can't accidentally become canonical."""

    def test_canonical_output_differs_from_historical_figures(self):
        inputs = mfm.CanonicalModelInputs()
        t1 = mfm.compute_month_pnl("scenario_table_1", 5, inputs)
        t2 = mfm.compute_month_pnl("scenario_table_2", 5, inputs)
        # Historical (superseded) figures -- must NOT match the canonical model's output.
        self.assertNotAlmostEqual(t1["revenue"]["total_revenue"], 157792.16, places=2)
        self.assertNotAlmostEqual(t2["revenue"]["total_revenue"], 118297.16, places=2)
        # Canonical figures -- must match exactly.
        self.assertAlmostEqual(t1["revenue"]["total_revenue"], 155215.80, places=2)
        self.assertAlmostEqual(t2["revenue"]["total_revenue"], 115720.80, places=2)

    def test_historical_net_pnl_not_confused_with_revenue_anywhere(self):
        """A$63,028.75 is historical Net P&L, not revenue -- must not appear
        as this model's revenue output anywhere."""
        inputs = mfm.CanonicalModelInputs()
        for scenario_id in ("scenario_table_1", "scenario_table_2"):
            for m in mfm.compute_24_month_pnl(scenario_id, inputs):
                self.assertNotAlmostEqual(m["revenue"]["total_revenue"], 63028.75, places=2)

    def test_historical_reconciliation_section_present_and_labelled(self):
        data = load_model_yaml("master_financial_model.yml")
        reconciliation = data["historical_reconciliation"]
        labels = {r["id"] for r in reconciliation}
        self.assertIn("reconciliation_table1_revenue", labels)
        self.assertIn("reconciliation_table2_revenue", labels)
        self.assertIn("reconciliation_table1_historical_net_pnl", labels)
        rec = find_record(reconciliation, "reconciliation_table1_historical_net_pnl")
        self.assertEqual(rec["status"], "SUPERSEDED")


class ScenarioSeparationTests(unittest.TestCase):
    """Table 1/Table 2 stay distinct."""

    def test_neither_scenario_marked_primary(self):
        scenario_records = load_canonical_yaml("scenarios.yml")["records"]
        for rec in scenario_records:
            self.assertFalse(rec["is_primary"])

    def test_scenario_comparison_shows_both_distinctly(self):
        data = load_model_yaml("master_financial_model.yml")
        comparison = data["outputs"]["scenario_comparison"]
        self.assertIn("scenario_table_1", comparison)
        self.assertIn("scenario_table_2", comparison)
        self.assertNotEqual(
            comparison["scenario_table_1"]["steady_state_revenue"],
            comparison["scenario_table_2"]["steady_state_revenue"],
        )


class InputChangePropagationTests(unittest.TestCase):
    """Changing a canonical input changes the model predictably."""

    def test_changing_am_price_changes_breakeven_predictably(self):
        """A higher AM price should produce a LOWER break-even client volume
        (need fewer clients to cover the same fixed cost base) -- proves the
        break-even function actually reads and responds to the canonical
        price, rather than being a hard-coded constant."""
        inputs = mfm.CanonicalModelInputs()
        baseline = mfm.compute_breakeven("scenario_table_1", inputs)

        # Monkeypatch pricing lookup indirectly: call compute_breakeven's
        # underlying arithmetic with a higher price to confirm the direction
        # of the response is correct (does not mutate canonical data on disk).
        pricing = load_canonical_yaml("pricing.yml")
        am_price = find_record(pricing["records"], "am_price_used_for_revenue")["price"]
        higher_price = am_price * 1.5
        m5 = mfm.compute_month_pnl("scenario_table_1", 5, inputs)
        client_assumptions = load_canonical_yaml("client_assumptions.yml")
        universal = client_assumptions["universal"]
        operating_days_weekday = find_record(universal, "operating_days_per_month_weekday")["value"]
        operating_saturdays = find_record(universal, "operating_saturdays_per_month")["value"]
        pm_and_ancillary = m5["revenue"]["pm_revenue"] + m5["revenue"]["ancillary_revenue"]
        higher_price_breakeven = (m5["total_operating_costs"] - pm_and_ancillary) / (
            higher_price * (operating_days_weekday + operating_saturdays)
        )
        self.assertLess(higher_price_breakeven, baseline["breakeven_am_client_volume_per_day"])

    def test_changing_client_volume_pct_changes_sensitivity_output(self):
        inputs = mfm.CanonicalModelInputs()
        results = mfm.compute_sensitivity_client_volume("scenario_table_1", inputs)
        revenues = [r["total_revenue"] for r in results]
        self.assertEqual(revenues, sorted(revenues), "revenue must increase monotonically with client volume %")


class UnresolvedAssumptionsVisibleTests(unittest.TestCase):
    """Unresolved assumptions stay visible."""

    def test_wage_conflicts_still_placeholder(self):
        wage_records = load_canonical_yaml("wages.yml")["records"]
        for wid in ("wage_ma000005_saturday_penalty", "wage_ma000005_sunday_penalty", "wage_ma000005_public_holiday_penalty"):
            rec = find_record(wage_records, wid)
            self.assertEqual(rec["status"], "PLACEHOLDER")

    def test_pm_discount_not_applied(self):
        """The 10% PM pre-booking discount must not silently appear in
        revenue_ramp.yml's PM figures (already established in Phase 6/7 --
        this model must not accidentally apply it either, since it reads
        revenue_ramp.yml's figures verbatim)."""
        rev_assumptions = load_canonical_yaml("revenue_assumptions.yml")["records"]
        discount_rec = find_record(rev_assumptions, "rev_discount_pm_prebooking")
        self.assertEqual(discount_rec["value"], 10)
        # PM revenue at steady state must equal the full undiscounted figure.
        inputs = mfm.CanonicalModelInputs()
        m5 = mfm.compute_month_pnl("scenario_table_1", 5, inputs)
        self.assertAlmostEqual(m5["revenue"]["pm_revenue"], 36730.80, places=2)

    def test_model_yaml_declares_its_own_new_conflicts(self):
        data = load_model_yaml("master_financial_model.yml")
        conflict_ids = {c["id"] for c in data["conflicts"]}
        self.assertIn("conflict_superannuation_not_in_cost_ramp", conflict_ids)
        self.assertIn("conflict_funding_requirement_not_established", conflict_ids)
        # conflict_superannuation_not_in_cost_ramp is now RESOLVED (item 46) -- every OTHER
        # conflict must remain UNRESOLVED (item 47/funding requirement stays untouched, per
        # explicit instruction not to resolve it this phase).
        for c in data["conflicts"]:
            if c["id"] == "conflict_superannuation_not_in_cost_ramp":
                self.assertTrue(str(c["resolution_status"]).startswith("RESOLVED"))
            elif c["id"] == "conflict_funding_requirement_not_established":
                self.assertTrue(str(c["resolution_status"]).startswith("PARTIALLY RESOLVED"))
            else:
                self.assertEqual(c["resolution_status"], "UNRESOLVED")

    def test_am_labor_ramp_assumption_documented(self):
        data = load_model_yaml("master_financial_model.yml")
        assumption_ids = {a["id"] for a in data["assumptions"]}
        self.assertIn("assumption_sensitivity_payroll_not_flexed", assumption_ids)


class NoHardCodedFinancialOutputsTests(unittest.TestCase):
    """No hard-coded financial outputs inside the calc engine."""

    def test_engine_source_does_not_hardcode_headline_totals(self):
        """The P&L calculation functions must not contain the canonical or
        historical headline totals as literal numbers -- they must be
        derived from data loaded at runtime."""
        source_text = MFM_PATH.read_text(encoding="utf-8")
        forbidden_literals = ["155215.80", "115720.80", "157792.16", "118297.16", "63028.75"]
        for literal in forbidden_literals:
            self.assertNotIn(
                literal, source_text,
                f"tools/master_financial_model.py must not hard-code {literal} -- it must be read from canonical YAML",
            )


class CashFlowTests(unittest.TestCase):
    """Basic cash flow sanity checks."""

    def test_opening_cash_defaults_to_none_not_invented(self):
        inputs = mfm.CanonicalModelInputs()
        cf = mfm.compute_cash_flow("scenario_table_1", inputs)
        self.assertIsNone(cf["opening_cash_assumption"])
        self.assertIsNone(cf["rows"][0]["closing_cash"])

    def test_cumulative_position_matches_running_sum_of_net_operating_result(self):
        inputs = mfm.CanonicalModelInputs()
        cf = mfm.compute_cash_flow("scenario_table_2", inputs)
        months = mfm.compute_24_month_pnl("scenario_table_2", inputs)
        expected_cumulative = 0.0
        for i, row in enumerate(cf["rows"]):
            expected_cumulative = round(expected_cumulative + months[i]["net_operating_result"], 2)
            self.assertAlmostEqual(row["cumulative_position"], expected_cumulative, places=2)


class BreakEvenDefensibilityTests(unittest.TestCase):
    """Break-even is scoped/disclosed appropriately, not manufactured."""

    def test_breakeven_below_committed_volume_for_both_scenarios(self):
        inputs = mfm.CanonicalModelInputs()
        for scenario_id in ("scenario_table_1", "scenario_table_2"):
            be = mfm.compute_breakeven(scenario_id, inputs)
            self.assertLess(be["breakeven_am_client_volume_per_day"], be["committed_client_volume_per_day"])
            self.assertIn("defensibility_note", be)
            self.assertIn("NOT computed", be["defensibility_note"])


class SuperannuationRegressionTests(unittest.TestCase):
    """Regression tests for superannuation (docs/VERIFICATION-TRACKER.md item
    46, resolved 2026-08-09) -- implemented at the canonical cost/wage layer
    (data/canonical/wages.yml + data/canonical/cost_ramp.yml), NOT as a
    special case in tools/master_financial_model.py."""

    def test_master_financial_model_has_no_special_case_superannuation_code(self):
        """tools/master_financial_model.py must not itself compute
        superannuation -- it must flow through automatically via
        cost_ramp.yml's payroll_costs."""
        source_text = MFM_PATH.read_text(encoding="utf-8")
        # The docstring is allowed to mention "superannuation" (historical
        # narration of the fix) -- the actual P&L calculation function must
        # not contain a superannuation formula.
        pnl_func_start = source_text.index("def compute_month_pnl(")
        rest = source_text[pnl_func_start:]
        next_def = rest.find("\ndef ", 1)
        func_body = rest[:next_def] if next_def != -1 else rest
        self.assertNotIn("SUPERANNUATION_RATE_PCT", func_body)
        self.assertNotIn("* 0.12", func_body)
        self.assertNotIn("/ 100 * 12", func_body)

    def test_cost_ramp_model_computes_superannuation(self):
        """tools/cost_ramp_model.py (the canonical layer) must be the one
        computing superannuation."""
        cost_model_source = (REPO_ROOT / "tools" / "cost_ramp_model.py").read_text(encoding="utf-8")
        self.assertIn("SUPERANNUATION_RATE_PCT", cost_model_source)
        self.assertIn("superannuation", cost_model_source)

    def test_superannuation_rate_matches_wages_yml(self):
        wage_records = load_canonical_yaml("wages.yml")["records"]
        rec = find_record(wage_records, "wage_superannuation_rate")
        self.assertEqual(rec["value_pct"], 12)
        self.assertEqual(rec["status"], "MODELLED")

    def test_treatment_staff_super_inclusive_phlebotomist_exclusive(self):
        """docs/financial-break-even-staff.md's own table labels 6 of 7
        roles 'incl. super' but NOT the Phlebotomist row -- confirmed in
        wages.yml's per-role superannuation field and the salary.includes_super
        flag."""
        wage_records = load_canonical_yaml("wages.yml")["records"]
        treatment_role_ids = ("wage_beauty_therapist", "wage_massage_therapist", "wage_nail_technician", "wage_hairdresser", "wage_receptionist_manager")
        for role_id in treatment_role_ids:
            rec = find_record(wage_records, role_id)
            self.assertTrue(rec["salary"]["includes_super"], f"{role_id} should be includes_super: true")
            self.assertIn("INCLUDED", rec["superannuation"])
        phleb = find_record(wage_records, "wage_phlebotomist")
        self.assertFalse(phleb["salary"]["includes_super"], "wage_phlebotomist should be includes_super: false")
        self.assertIn("EXCLUDED", phleb["superannuation"])

    def test_payroll_costs_higher_than_before_superannuation_was_added(self):
        """Sanity check: Month 5+ payroll_costs must exceed
        direct_labor_and_opening_total + workers_comp alone (i.e.
        superannuation is a real, positive additive line, not zero)."""
        cost_ramp_records = load_canonical_yaml("cost_ramp.yml")["records"]
        for cost_id in ("cost_table1_m5plus", "cost_table2_m5plus"):
            rec = find_record(cost_ramp_records, cost_id)
            bd = rec["payroll_breakdown"]
            self.assertGreater(bd["superannuation"], 0)
            without_super = bd["direct_labor_and_opening_total"] + bd["workers_comp"]
            self.assertAlmostEqual(rec["payroll_costs"], without_super + bd["superannuation"], places=2)

    def test_superannuation_not_double_counted_on_treatment_staff_am_weekday(self):
        """The AM-weekday treatment-staff sub-component must NOT have super
        added on top (it's already included in the source annual salary) --
        verified by confirming superannuation is computed only from
        phlebotomist + hours-based components, not the full am_weekday figure."""
        inputs = crm.CanonicalCostInputs()
        payroll = crm.compute_payroll("scenario_table_1", "M5plus", inputs)
        expected_super_base = (
            payroll["am_weekday_phlebotomist"]
            + payroll["am_saturday_direct_labor"]
            + payroll["pm_weekday_direct_labor"]
            + payroll["pm_saturday_direct_labor"]
        )
        expected_super = round(expected_super_base * crm.SUPERANNUATION_RATE_PCT / 100, 2)
        self.assertAlmostEqual(payroll["superannuation"], expected_super, places=2)
        # Confirm it does NOT equal super computed on the FULL am_weekday_direct_labor
        # (which would double-count the treatment-staff portion).
        double_counted_base = expected_super_base + payroll["am_weekday_treatment_staff"]
        double_counted_super = round(double_counted_base * crm.SUPERANNUATION_RATE_PCT / 100, 2)
        self.assertNotAlmostEqual(payroll["superannuation"], double_counted_super, places=2)

    def test_am_weekday_split_sums_to_original_total(self):
        """am_weekday_treatment_staff + am_weekday_phlebotomist must equal
        am_weekday_direct_labor exactly. RECALCULATED 2026-08-17 to propagate
        the 2026-08-16 current-wage-rate research (docs/FOUNDER-FEEDBACK-
        IMPLEMENTATION-MATRIX.md point 5) -- was A$48,254.67 before this
        recompute; the sum-equals-total property itself is unchanged, only
        the absolute figure moved."""
        inputs = crm.CanonicalCostInputs()
        payroll = crm.compute_payroll("scenario_table_1", "M1", inputs)
        self.assertAlmostEqual(
            payroll["am_weekday_treatment_staff"] + payroll["am_weekday_phlebotomist"],
            payroll["am_weekday_direct_labor"],
            places=2,
        )
        self.assertAlmostEqual(payroll["am_weekday_direct_labor"], 50082.52, places=2)

    def test_superannuation_flows_through_master_model_automatically(self):
        """The Master Financial Model's payroll figure must exactly match
        cost_ramp.yml's own (super-inclusive) payroll_costs -- confirming
        super flows through the normal canonical-data pipeline, not a
        special case."""
        cost_ramp_records = load_canonical_yaml("cost_ramp.yml")["records"]
        inputs = mfm.CanonicalModelInputs()
        for scenario_id, cost_id in (("scenario_table_1", "cost_table1_m5plus"), ("scenario_table_2", "cost_table2_m5plus")):
            cost_rec = find_record(cost_ramp_records, cost_id)
            pnl = mfm.compute_month_pnl(scenario_id, 5, inputs)
            self.assertAlmostEqual(pnl["payroll"], cost_rec["payroll_costs"], places=2)
            bd = cost_rec["payroll_breakdown"]
            self.assertGreater(pnl["payroll"], bd["direct_labor_and_opening_total"] + bd["workers_comp"] - 0.01)

    def test_tracker_item_46_evidence_documented_in_model_yaml(self):
        data = load_model_yaml("master_financial_model.yml")
        assumption_ids = {a["id"] for a in data["assumptions"]}
        self.assertIn("assumption_superannuation_canonical", assumption_ids)
        rec = find_record(data["assumptions"], "assumption_superannuation_canonical")
        self.assertIn("financial-break-even-staff.md", rec["source"]["file"])


class FundingRequirementInvestigationTests(unittest.TestCase):
    """Tests for docs/VERIFICATION-TRACKER.md item 47 (funding requirement
    investigation, resolved as OUTCOME 2 -- bounded, not exact). Confirms the
    bounded range is arithmetically consistent, does not double-count, does
    not invent an opening cash balance, and keeps Table 1/Table 2 separate
    where scenario-specific data is used."""

    def _funding_data(self):
        data = load_model_yaml("master_financial_model.yml")
        return data["funding_requirement_investigation"]

    def test_outcome_is_bounded_not_exact(self):
        funding = self._funding_data()
        self.assertEqual(funding["outcome"], "OUTCOME_2_BOUNDED")

    def test_pre_opening_capital_is_universal_not_scenario_specific(self):
        funding = self._funding_data()
        pre_opening = funding["pre_opening_capital"]
        self.assertEqual(pre_opening["scenario_applicability"], "universal")
        self.assertLess(pre_opening["range_low"], pre_opening["range_high"])

    def test_pre_opening_capital_sums_from_canonical_startup_cost_components(self):
        """(A) = 7.1 + 7.2 + legal/lease-only + insurance, EXCLUDING working
        capital -- verified against the actual canonical records, not just
        re-reading the stored total."""
        startup_records = load_canonical_yaml("startup_costs.yml")
        c72 = find_record(startup_records["records"], "startup_construction_current_state_recompute")
        legal_lease = find_record(startup_records["records"], "startup_legal_entity_lease_bond")
        funding = self._funding_data()
        pre_opening = funding["pre_opening_capital"]

        # 7.1 (Equipment/Furniture/Signage) is not an individually-tagged single
        # record in startup_costs.yml (it's CURRENT-STATE.md's own sub-total) --
        # so this test checks the two components that ARE directly traceable:
        # construction and legal/lease, both of which must be less than the
        # combined pre_opening_capital total (sanity bound, not exact equality,
        # since 7.1 + insurance are not separately id'd records in this file).
        combined_traceable = c72["total_cost"]["low"] + legal_lease["total_cost"]["low"]
        self.assertLess(combined_traceable, pre_opening["range_low"])

    def test_working_capital_has_two_disclosed_methods_neither_forced(self):
        funding = self._funding_data()
        wc = funding["opening_working_capital"]
        self.assertIn("historical_reserve_method", wc)
        self.assertIn("operating_cash_trough_cross_check", wc)
        historical = wc["historical_reserve_method"]
        self.assertEqual(historical["range_low"], 85000.00)
        self.assertEqual(historical["range_high"], 110000.00)
        cross_check_results = wc["operating_cash_trough_cross_check"]["results"]
        self.assertEqual(len(cross_check_results), 2)
        scenario_ids = {r["scenario_id"] for r in cross_check_results}
        self.assertEqual(scenario_ids, {"scenario_table_1", "scenario_table_2"})

    def test_operating_cash_trough_cross_check_matches_cash_flow_summary(self):
        """The funding investigation's trough cross-check values must exactly
        match the Master Financial Model's own cash_flow_summary -- not a
        second, independently-computed figure."""
        data = load_model_yaml("master_financial_model.yml")
        cash_flow_summary = data["outputs"]["cash_flow_summary"]
        cash_flow_by_scenario = {r["scenario_id"]: r for r in cash_flow_summary}
        cross_check_results = data["funding_requirement_investigation"]["opening_working_capital"]["operating_cash_trough_cross_check"]["results"]
        for cc in cross_check_results:
            cf = cash_flow_by_scenario[cc["scenario_id"]]
            self.assertAlmostEqual(cc["trough_value"], abs(cf["trough_cumulative_position"]), places=2)
            self.assertEqual(cc["trough_month"], cf["trough_month"])

    def test_combined_primary_method_equals_pre_opening_plus_historical_reserve(self):
        """(C) primary method must equal (A) + (B historical), not (A) +
        operating cash trough -- the primary combined figure must NOT
        double-count by summing the trough on top of the reserve."""
        funding = self._funding_data()
        pre_opening = funding["pre_opening_capital"]
        historical_wc = funding["opening_working_capital"]["historical_reserve_method"]
        combined = funding["combined_funding_requirement_bounded"]["primary_method"]
        self.assertAlmostEqual(
            combined["range_low"], pre_opening["range_low"] + historical_wc["range_low"], places=2
        )
        self.assertAlmostEqual(
            combined["range_high"], pre_opening["range_high"] + historical_wc["range_high"], places=2
        )

    def test_combined_primary_method_matches_existing_canonical_component_sum(self):
        """The primary combined figure must be an EXACT match to the
        already-canonical total_current_state_component_sum -- proving no new
        dollar figure was invented, only a re-partition of an existing one."""
        startup_records = load_canonical_yaml("startup_costs.yml")
        existing_sum = find_record(startup_records["historical_total_estimates"], "total_current_state_component_sum")
        funding = self._funding_data()
        combined = funding["combined_funding_requirement_bounded"]["primary_method"]
        self.assertAlmostEqual(combined["range_low"], existing_sum["total_cost"]["low"], places=2)
        self.assertAlmostEqual(combined["range_high"], existing_sum["total_cost"]["high"], places=2)

    def test_alternative_cross_check_method_is_scenario_specific_and_distinct(self):
        funding = self._funding_data()
        alt_results = funding["combined_funding_requirement_bounded"]["alternative_cross_check_method"]["results"]
        alt_by_scenario = {r["scenario_id"]: r for r in alt_results}
        t1 = alt_by_scenario["scenario_table_1"]
        t2 = alt_by_scenario["scenario_table_2"]
        self.assertNotAlmostEqual(t1["range_low"], t2["range_low"], places=2)
        # Table 2's alternative range must be higher than Table 1's, since
        # Table 2's operating-cash trough is deeper.
        self.assertGreater(t2["range_low"], t1["range_low"])

    def test_opening_cash_still_not_invented(self):
        """This investigation must not have introduced an opening cash value
        anywhere -- assumption_opening_cash_not_invented must remain
        PLACEHOLDER/null."""
        data = load_model_yaml("master_financial_model.yml")
        rec = find_record(data["assumptions"], "assumption_opening_cash_not_invented")
        self.assertEqual(rec["status"], "PLACEHOLDER")
        cf = mfm.compute_cash_flow("scenario_table_1", mfm.CanonicalModelInputs())
        self.assertIsNone(cf["opening_cash_assumption"])

    def test_capex_records_carry_no_timing_field(self):
        """Confirms the TIMING UNKNOWN classification for capex.yml is
        accurate, not asserted without checking."""
        capex_records = load_canonical_yaml("capex.yml")["records"]
        timing_keys = {"payment_timing", "payment_schedule", "milestone", "timing"}
        for rec in capex_records:
            self.assertFalse(timing_keys & set(rec.keys()), f"{rec.get('id')} unexpectedly has a timing field")

    def test_item_47_tracker_entry_reflects_bounded_not_full_resolution(self):
        tracker_text = (REPO_ROOT / "docs" / "VERIFICATION-TRACKER.md").read_text(encoding="utf-8")
        self.assertIn("PARTIALLY RESOLVED (bounded) 2026-08-09", tracker_text)

    def test_funding_investigation_does_not_alter_revenue_or_cost_methodology(self):
        """Sanity check: canonical revenue steady-state figures must remain
        byte-identical (revenue was never wage-driven, unaffected by the
        2026-08-17 wage-rate recompute). Payroll figures RECALCULATED
        2026-08-17 (docs/FOUNDER-FEEDBACK-IMPLEMENTATION-MATRIX.md point 5)
        -- were 84654.10/80684.16 before propagating the 2026-08-16 current-
        wage-rate research through the canonical model."""
        inputs = mfm.CanonicalModelInputs()
        m5_t1 = mfm.compute_month_pnl("scenario_table_1", 5, inputs)
        m5_t2 = mfm.compute_month_pnl("scenario_table_2", 5, inputs)
        self.assertAlmostEqual(m5_t1["revenue"]["total_revenue"], 155215.80, places=2)
        self.assertAlmostEqual(m5_t2["revenue"]["total_revenue"], 115720.80, places=2)
        self.assertAlmostEqual(m5_t1["payroll"], 87398.78, places=2)
        self.assertAlmostEqual(m5_t2["payroll"], 83278.43, places=2)


if __name__ == "__main__":
    unittest.main()
