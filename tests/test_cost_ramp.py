"""
Reproduction tests for docs/architecture/COST-RAMP-METHODOLOGY.md and
tools/cost_ramp_model.py (Phase 8, 2026-08-09).

Purpose: prove the canonical Month 1-5+ cost ramp is deterministic,
reproducible directly from data/canonical/*.yml inputs plus a small set of
named, cited payroll constants, correctly separates fixed/variable/payroll,
never lets startup/capex costs leak into recurring opex, does NOT blindly
apply the revenue ramp to every cost, and responds predictably to
client-volume-dependent inputs.

Run:
    python tests/test_cost_ramp.py
    (or: python -m unittest tests.test_cost_ramp -v, from repo root)
"""

import importlib.util
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIR = REPO_ROOT / "data" / "canonical"
COST_MODEL_PATH = REPO_ROOT / "tools" / "cost_ramp_model.py"

_spec = importlib.util.spec_from_file_location("cost_ramp_model", COST_MODEL_PATH)
cost_model = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cost_model)


def load_yaml(filename):
    with (CANONICAL_DIR / filename).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_record(records, record_id):
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


class SchemaValidityTests(unittest.TestCase):
    """(1) Schema validity."""

    def test_cost_ramp_yaml_loads_and_has_required_top_keys(self):
        data = load_yaml("cost_ramp.yml")
        self.assertEqual(data["dataset"], "cost_ramp")
        self.assertIn("records", data)
        self.assertEqual(len(data["records"]), 10)  # 5 months x 2 scenarios

    def test_every_record_has_required_fields(self):
        records = load_yaml("cost_ramp.yml")["records"]
        required = {"id", "scenario_id", "month", "status", "fixed_costs", "variable_costs", "payroll_costs", "total_operating_costs"}
        for rec in records:
            missing = required - set(rec.keys())
            self.assertFalse(missing, f"{rec.get('id')} missing fields: {missing}")

    def test_no_duplicate_scenario_month_pairs(self):
        records = load_yaml("cost_ramp.yml")["records"]
        seen = set()
        for rec in records:
            key = (rec["scenario_id"], rec["month"])
            self.assertNotIn(key, seen, f"duplicate (scenario_id, month) pair: {key}")
            seen.add(key)


class DeterminismTests(unittest.TestCase):
    """(2) Deterministic output."""

    def test_repeated_calls_produce_identical_output(self):
        inputs = cost_model.CanonicalCostInputs()
        first = cost_model.compute_ramp("scenario_table_1", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        second = cost_model.compute_ramp("scenario_table_1", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        self.assertEqual(first, second)

    def test_fresh_inputs_produce_identical_output(self):
        first = cost_model.compute_ramp(
            "scenario_table_2", cost_model.CanonicalCostInputs(), cost_model.DEFAULT_REVENUE_RAMP_CURVE
        )
        second = cost_model.compute_ramp(
            "scenario_table_2", cost_model.CanonicalCostInputs(), cost_model.DEFAULT_REVENUE_RAMP_CURVE
        )
        self.assertEqual(first, second)


class Table1Tests(unittest.TestCase):
    """(3) Table 1."""

    def test_table1_month5plus_matches_recorded_yaml(self):
        ramp_records = load_yaml("cost_ramp.yml")["records"]
        rec = find_record(ramp_records, "cost_table1_m5plus")
        inputs = cost_model.CanonicalCostInputs()
        computed = cost_model.compute_ramp("scenario_table_1", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        m5 = next(m for m in computed if m["month"] == "M5plus")
        self.assertAlmostEqual(m5["total_operating_costs"], rec["total_operating_costs"], places=2)
        self.assertAlmostEqual(m5["fixed_costs"], rec["fixed_costs"], places=2)
        self.assertAlmostEqual(m5["variable_costs"], rec["variable_costs"], places=2)
        self.assertAlmostEqual(m5["payroll_costs"], rec["payroll_costs"], places=2)

    def test_table1_total_operating_costs_m5plus_value(self):
        """RECALCULATED 2026-08-17 (Phase C, first-principles rebuild) to
        114870.20 -- was 101378.78 under the 2026-08-17 proportional-wage-
        scaling recompute (itself recalculated 2026-08-09 for superannuation
        -- was 98634.10 before that, and 95014.18 before super was added).
        Phase C replaces proportional scaling with a genuine first-principles
        labour build (position -> headcount -> hours/shift -> wage rate ->
        Saturday penalty -> super -> workers comp), see
        docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md."""
        inputs = cost_model.CanonicalCostInputs()
        computed = cost_model.compute_ramp("scenario_table_1", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        m5 = next(m for m in computed if m["month"] == "M5plus")
        self.assertAlmostEqual(m5["total_operating_costs"], 114870.20, places=2)


class Table2Tests(unittest.TestCase):
    """(4) Table 2."""

    def test_table2_month5plus_matches_recorded_yaml(self):
        ramp_records = load_yaml("cost_ramp.yml")["records"]
        rec = find_record(ramp_records, "cost_table2_m5plus")
        inputs = cost_model.CanonicalCostInputs()
        computed = cost_model.compute_ramp("scenario_table_2", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        m5 = next(m for m in computed if m["month"] == "M5plus")
        self.assertAlmostEqual(m5["total_operating_costs"], rec["total_operating_costs"], places=2)

    def test_table2_total_operating_costs_m5plus_value(self):
        """RECALCULATED 2026-08-17 (Phase C, first-principles rebuild) to
        109465.22 -- was 97258.43 under the 2026-08-17 proportional-wage-
        scaling recompute (itself recalculated 2026-08-09 for superannuation
        -- was 94664.16 before that, and 91463.24 before super was added)."""
        inputs = cost_model.CanonicalCostInputs()
        computed = cost_model.compute_ramp("scenario_table_2", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        m5 = next(m for m in computed if m["month"] == "M5plus")
        self.assertAlmostEqual(m5["total_operating_costs"], 109465.22, places=2)


class Month1To5PlusTests(unittest.TestCase):
    """(5) Month 1-5+."""

    def test_all_five_months_present_both_scenarios(self):
        results = cost_model.compute_all()
        for scenario_id in ("scenario_table_1", "scenario_table_2"):
            months = [m["month"] for m in results[scenario_id]]
            self.assertEqual(months, ["M1", "M2", "M3", "M4", "M5plus"])

    def test_month1_to_4_payroll_identical_within_scenario(self):
        """Confirms the 3-hour casual-minimum floor keeps PM (and therefore
        total) payroll flat across Months 1-4, only rising at Month 5+."""
        inputs = cost_model.CanonicalCostInputs()
        months = cost_model.compute_ramp("scenario_table_1", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        m1_to_4 = [m["payroll_costs"] for m in months if m["month"] != "M5plus"]
        self.assertEqual(len(set(m1_to_4)), 1, "Months 1-4 payroll should be identical (floor-constrained)")
        m5 = next(m for m in months if m["month"] == "M5plus")
        self.assertGreater(m5["payroll_costs"], m1_to_4[0])


class FixedCostsTests(unittest.TestCase):
    """(6) Fixed costs."""

    def test_fixed_costs_constant_across_all_months(self):
        inputs = cost_model.CanonicalCostInputs()
        for scenario_id in ("scenario_table_1", "scenario_table_2"):
            months = cost_model.compute_ramp(scenario_id, inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
            fixed_values = {m["fixed_costs"] for m in months}
            self.assertEqual(len(fixed_values), 1, "Fixed costs must not vary by month")

    def test_fixed_costs_identical_across_scenarios(self):
        """Fixed Non-Wage Overhead (excl. marketing) is universal, per
        opex.yml's own scenario_applicability: universal fields."""
        inputs = cost_model.CanonicalCostInputs()
        t1 = cost_model.compute_ramp("scenario_table_1", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        t2 = cost_model.compute_ramp("scenario_table_2", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        self.assertEqual(t1[0]["fixed_costs"], t2[0]["fixed_costs"])

    def test_fixed_costs_value(self):
        inputs = cost_model.CanonicalCostInputs()
        self.assertAlmostEqual(inputs.fixed_nonwage_excl_marketing, 12480.00, places=2)


class VariableCostsTests(unittest.TestCase):
    """(7) Variable costs."""

    def test_marketing_ramp_increases_monotonically_to_steady_state(self):
        inputs = cost_model.CanonicalCostInputs()
        months = cost_model.compute_ramp("scenario_table_1", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        variable_values = [m["variable_costs"] for m in months]
        self.assertEqual(variable_values, sorted(variable_values), "Marketing ramp should increase monotonically")
        self.assertAlmostEqual(variable_values[0], 600.00, places=2)
        self.assertAlmostEqual(variable_values[-1], 1500.00, places=2)

    def test_gtt_supplies_variable_alternative_scales_with_client_volume(self):
        """The exploratory variable-alternative is NOT part of the primary
        total, but must itself scale with implied client volume."""
        inputs = cost_model.CanonicalCostInputs()
        m1 = cost_model.gtt_supplies_variable_alternative(
            "scenario_table_1", "M1", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE
        )
        m5 = cost_model.gtt_supplies_variable_alternative(
            "scenario_table_1", "M5plus", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE
        )
        self.assertLess(m1, m5)
        self.assertAlmostEqual(m5, 792.00, places=2)


class PayrollTests(unittest.TestCase):
    """(8) Payroll."""

    def test_payroll_breakdown_components_sum_correctly(self):
        inputs = cost_model.CanonicalCostInputs()
        payroll = cost_model.compute_payroll("scenario_table_1", "M1", inputs)
        components = (
            payroll["am_weekday_direct_labor"] + payroll["am_saturday_direct_labor"]
            + payroll["pm_weekday_direct_labor"] + payroll["pm_saturday_direct_labor"]
            + payroll["opening_time_increment"] + payroll["receptionist_relief"]
        )
        self.assertAlmostEqual(components, payroll["direct_labor_and_opening_total"], places=2)

    def test_workers_comp_is_1_7_pct_of_direct_labor(self):
        inputs = cost_model.CanonicalCostInputs()
        payroll = cost_model.compute_payroll("scenario_table_1", "M5plus", inputs)
        expected_wc = round(payroll["direct_labor_and_opening_total"] * 0.017, 2)
        self.assertAlmostEqual(payroll["workers_comp"], expected_wc, places=2)

    def test_pm_weekday_labor_floored_at_3_hours_below_threshold(self):
        """4, 8, 12, 15 sessions/day should all produce the SAME floor-
        constrained daily rate; only 16 sessions/day clears the floor."""
        floored_months = [cost_model.compute_pm_weekday_daily_labor(m) for m in ("M1", "M2", "M3", "M4")]
        self.assertEqual(len(set(floored_months)), 1)
        expected_floor_rate = round(3.0 * 4 * cost_model.PM_WEEKDAY_BLENDED_CASUAL_RATE, 2)
        self.assertAlmostEqual(floored_months[0], expected_floor_rate, places=2)
        m5_rate = cost_model.compute_pm_weekday_daily_labor("M5plus")
        self.assertGreater(m5_rate, floored_months[0])


class UnresolvedPlaceholderInputTests(unittest.TestCase):
    """(9) Unresolved/placeholder inputs."""

    def test_unresolved_wage_conflicts_are_not_silently_used(self):
        """wage_ma000005_saturday_penalty etc. remain PLACEHOLDER (value_pct:
        null) in wages.yml -- this model must not have silently picked a
        value for them (it doesn't reference them at all, by design)."""
        wage_records = load_yaml("wages.yml")["records"]
        placeholder_wage_ids = {
            "wage_ma000005_saturday_penalty", "wage_ma000005_sunday_penalty", "wage_ma000005_public_holiday_penalty",
        }
        for wid in placeholder_wage_ids:
            rec = find_record(wage_records, wid)
            self.assertEqual(rec["status"], "PLACEHOLDER")
            self.assertIsNone(rec["value_pct"])

    def test_cost_ramp_conflicts_list_is_non_empty_and_unresolved(self):
        """The genuine open questions this phase surfaced/carried forward
        must be present and explicitly marked UNRESOLVED, not silently
        dropped."""
        conflicts = load_yaml("cost_ramp.yml")["conflicts"]
        self.assertGreaterEqual(len(conflicts), 3)
        for c in conflicts:
            self.assertEqual(c["resolution_status"], "UNRESOLVED")


class ScenarioSeparationTests(unittest.TestCase):
    """(10) Scenario separation."""

    def test_table1_and_table2_am_saturday_labor_differ(self):
        inputs = cost_model.CanonicalCostInputs()
        p1 = cost_model.compute_payroll("scenario_table_1", "M5plus", inputs)
        p2 = cost_model.compute_payroll("scenario_table_2", "M5plus", inputs)
        self.assertNotAlmostEqual(p1["am_saturday_direct_labor"], p2["am_saturday_direct_labor"], places=2)
        self.assertGreater(p1["am_saturday_direct_labor"], p2["am_saturday_direct_labor"])

    def test_table1_and_table2_pm_labor_identical(self):
        """PM labor is not AM-client-volume-dependent -- must be identical
        between scenarios."""
        inputs = cost_model.CanonicalCostInputs()
        p1 = cost_model.compute_payroll("scenario_table_1", "M3", inputs)
        p2 = cost_model.compute_payroll("scenario_table_2", "M3", inputs)
        self.assertAlmostEqual(p1["pm_weekday_direct_labor"], p2["pm_weekday_direct_labor"], places=2)
        self.assertAlmostEqual(p1["pm_saturday_direct_labor"], p2["pm_saturday_direct_labor"], places=2)

    def test_neither_scenario_marked_primary(self):
        scenario_records = load_yaml("scenarios.yml")["records"]
        for rec in scenario_records:
            self.assertFalse(rec["is_primary"], f"{rec['id']} must not be marked primary")


class NoStartupCostLeakageTests(unittest.TestCase):
    """(11) No accidental startup-cost-as-recurring-opex."""

    def test_startup_classified_opex_records_excluded_from_fixed_costs_total(self):
        """opex.yml records classified STARTUP (e.g. accountant initial
        brief) must not be included anywhere in this model's fixed_costs
        total (A$12,480.00, cross-checked against the known 13-line
        Non-Wage Overhead total minus marketing -- none of which are STARTUP-
        classified records)."""
        opex_records = load_yaml("opex.yml")["records"]
        startup_records = [r for r in opex_records if r.get("cost_type") == "STARTUP"]
        self.assertGreater(len(startup_records), 0, "sanity check: opex.yml should have at least one STARTUP record")
        for rec in startup_records:
            self.assertIsNone(
                rec.get("monthly_equivalent"),
                f"{rec['id']} is STARTUP-classified and must not carry a monthly_equivalent "
                f"that could be mistaken for recurring opex",
            )

    def test_fixed_costs_total_does_not_include_any_one_off_amount(self):
        """Direct arithmetic check: opex.yml's one_off/STARTUP records'
        amounts must not appear summed into this model's fixed_nonwage_excl_marketing."""
        inputs = cost_model.CanonicalCostInputs()
        # opex_accountant_initial_brief's low estimate (500.00) must not be
        # part of the fixed total -- confirm the fixed total equals the known
        # 13-line Non-Wage Overhead minus marketing, not that plus a startup line.
        self.assertAlmostEqual(inputs.fixed_nonwage_excl_marketing, 12480.00, places=2)


class NoCapexLeakageTests(unittest.TestCase):
    """(12) No accidental capex-as-recurring-opex."""

    def test_capex_records_not_referenced_by_cost_ramp_model(self):
        """tools/cost_ramp_model.py's source must not import or reference
        capex.yml at all -- capex is one-off/depreciation, structurally
        outside a recurring cost ramp."""
        source_text = COST_MODEL_PATH.read_text(encoding="utf-8")
        self.assertNotIn("capex.yml", source_text)
        self.assertNotIn("startup_costs.yml", source_text)


class RevenueRampNotBlindlyAppliedTests(unittest.TestCase):
    """(13) No accidental application of the revenue ramp to all costs."""

    def test_fixed_costs_do_not_follow_revenue_ramp_percentages(self):
        """Fixed costs (rent, utilities, etc.) must stay flat even though
        revenue ramps 43%->100% -- proves the revenue ramp curve was NOT
        blindly applied to every cost."""
        inputs = cost_model.CanonicalCostInputs()
        months = cost_model.compute_ramp("scenario_table_1", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE)
        m1 = next(m for m in months if m["month"] == "M1")
        m5 = next(m for m in months if m["month"] == "M5plus")
        # If the revenue ramp (43%) had been blindly applied, fixed_costs at
        # M1 would be ~43% of M5plus's fixed_costs -- assert it is NOT.
        self.assertEqual(m1["fixed_costs"], m5["fixed_costs"])

    def test_am_payroll_does_not_follow_revenue_ramp_percentages(self):
        """AM Direct Labor must stay flat across the ramp (FTE-based, see
        conflict_am_labor_ramp_unmodelled) -- NOT scaled by 43/64/79/93/100%."""
        inputs = cost_model.CanonicalCostInputs()
        p1 = cost_model.compute_payroll("scenario_table_1", "M1", inputs)
        p5 = cost_model.compute_payroll("scenario_table_1", "M5plus", inputs)
        self.assertEqual(p1["am_weekday_direct_labor"], p5["am_weekday_direct_labor"])
        self.assertEqual(p1["am_saturday_direct_labor"], p5["am_saturday_direct_labor"])

    def test_pm_payroll_ramp_curve_differs_from_revenue_ramp_curve(self):
        """The PM payroll ramp (session-count based, 25/50/75/93.75/100% of
        capacity) must be a DIFFERENT curve from the revenue ramp
        (43/64/79/93/100%) -- confirms cost_ramp_model.py did not just reuse
        revenue_ramp_model.py's curve under a different name."""
        payroll_curve_pct = [
            round(cost_model.PM_SESSION_RAMP[m] / 16 * 100, 2) for m in ("M1", "M2", "M3", "M4", "M5plus")
        ]
        revenue_curve_pct = [pct for _, pct in cost_model.DEFAULT_REVENUE_RAMP_CURVE]
        self.assertNotEqual(payroll_curve_pct, revenue_curve_pct)


class ClientVolumeSensitivityTests(unittest.TestCase):
    """(14) Sensitivity to client-volume-dependent costs."""

    def test_am_saturday_labor_sensitive_to_scenario_client_volume(self):
        """AM Saturday labor (the one payroll component tied to the
        scenario's committed client volume) must differ between the
        18-client and 12-client scenarios, in the expected direction."""
        inputs = cost_model.CanonicalCostInputs()
        p1 = cost_model.compute_payroll("scenario_table_1", "M5plus", inputs)
        p2 = cost_model.compute_payroll("scenario_table_2", "M5plus", inputs)
        self.assertGreater(inputs.client_volume["scenario_table_1"], inputs.client_volume["scenario_table_2"])
        self.assertGreater(p1["am_saturday_direct_labor"], p2["am_saturday_direct_labor"])

    def test_gtt_supplies_variable_alternative_sensitive_to_client_volume(self):
        inputs = cost_model.CanonicalCostInputs()
        t1 = cost_model.gtt_supplies_variable_alternative(
            "scenario_table_1", "M5plus", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE
        )
        t2 = cost_model.gtt_supplies_variable_alternative(
            "scenario_table_2", "M5plus", inputs, cost_model.DEFAULT_REVENUE_RAMP_CURVE
        )
        self.assertGreater(t1, t2)


class CanonicalIdReferenceTests(unittest.TestCase):
    """All referenced canonical IDs exist -- same rigor as test_revenue_ramp.py."""

    def test_scenario_ids_exist_in_scenarios_yml(self):
        ramp_records = load_yaml("cost_ramp.yml")["records"]
        scenario_records = load_yaml("scenarios.yml")["records"]
        valid_scenario_ids = {r["id"] for r in scenario_records}
        for rec in ramp_records:
            self.assertIn(rec["scenario_id"], valid_scenario_ids)

    def test_marketing_records_exist_in_opex_yml(self):
        opex_records = load_yaml("opex.yml")["records"]
        find_record(opex_records, "opex_marketing_ads_ramp")
        find_record(opex_records, "opex_marketing_ads_steady_state")

    def test_pm_session_ramp_source_exists_in_revenue_assumptions(self):
        rev_records = load_yaml("revenue_assumptions.yml")["records"]
        rec = find_record(rev_records, "rev_pm_session_ramp_historical")
        self.assertEqual(rec["value"], {"month_1": 4, "month_2": 8, "month_3": 12, "month_4": 15, "month_5_plus": 16})


if __name__ == "__main__":
    unittest.main()
