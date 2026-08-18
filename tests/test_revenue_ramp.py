"""
Reproduction tests for docs/architecture/REVENUE-RAMP-METHODOLOGY.md and
tools/revenue_ramp_model.py (Phase 7, 2026-08-09).

Purpose: prove the canonical Month 1-5+ revenue ramp is deterministic,
reproducible directly from data/canonical/*.yml inputs, converges correctly
to the canonical revenue methodology at steady state, responds predictably to
scenario/ramp-curve changes, and never lets PM revenue silently exceed
canonical PM capacity.

Run:
    python tests/test_revenue_ramp.py
    (or: python -m unittest tests.test_revenue_ramp -v, from repo root)
"""

import importlib.util
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIR = REPO_ROOT / "data" / "canonical"
RAMP_MODEL_PATH = REPO_ROOT / "tools" / "revenue_ramp_model.py"

_spec = importlib.util.spec_from_file_location("revenue_ramp_model", RAMP_MODEL_PATH)
ramp_model = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ramp_model)


def load_yaml(filename):
    with (CANONICAL_DIR / filename).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_record(records, record_id):
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


class RevenueRampScenarioLoadingTests(unittest.TestCase):
    """(1) Both scenarios load correctly."""

    def test_both_scenarios_load(self):
        inputs = ramp_model.CanonicalRevenueInputs()
        self.assertIn("scenario_table_1", inputs.client_volume)
        self.assertIn("scenario_table_2", inputs.client_volume)
        self.assertEqual(inputs.client_volume["scenario_table_1"], 18)
        self.assertEqual(inputs.client_volume["scenario_table_2"], 12)

    def test_both_scenarios_compute_without_error(self):
        results = ramp_model.compute_all()
        self.assertEqual(len(results["scenario_table_1"]), 5)
        self.assertEqual(len(results["scenario_table_2"]), 5)


class SteadyStateConvergenceTests(unittest.TestCase):
    """(2) Month 5+ equals steady-state when ramp=100%."""

    def test_table1_m5plus_equals_canonical_steady_state(self):
        """RECALCULATED 2026-08-18 (Priority 1, PM capacity/transaction
        reconciliation) -- was 163721.88 (raw 16/8 staff-session PM count
        used directly, incorrect), now 154710.69 (corrected 12.8128/6.4064
        transaction capacity, docs/architecture/PM-CAPACITY-RECONCILIATION.md).
        Was 155215.80 (A$95 PM placeholder average) before that."""
        inputs = ramp_model.CanonicalRevenueInputs()
        months = ramp_model.compute_ramp("scenario_table_1", inputs)
        m5 = next(m for m in months if m["month"] == "M5plus")
        self.assertEqual(m5["ramp_pct"], 100)
        self.assertAlmostEqual(m5["total_revenue"], 154710.69, places=2)
        self.assertAlmostEqual(m5["total_revenue"], m5["steady_state_total_revenue"], places=2)

    def test_table2_m5plus_equals_canonical_steady_state(self):
        """RECALCULATED 2026-08-18 (Priority 1, PM capacity/transaction
        reconciliation) -- was 124226.88, now 115215.69. Was 115720.80
        before the 2026-08-17 PM-PACKAGES.md rebuild."""
        inputs = ramp_model.CanonicalRevenueInputs()
        months = ramp_model.compute_ramp("scenario_table_2", inputs)
        m5 = next(m for m in months if m["month"] == "M5plus")
        self.assertEqual(m5["ramp_pct"], 100)
        self.assertAlmostEqual(m5["total_revenue"], 115215.69, places=2)
        self.assertAlmostEqual(m5["total_revenue"], m5["steady_state_total_revenue"], places=2)

    def test_m5plus_matches_canonical_revenue_methodology_records(self):
        """Cross-check against revenue_assumptions.yml's own canonical figures --
        the ramp's Month 5+ must not silently diverge from the methodology it's
        supposed to converge to."""
        rev_records = load_yaml("revenue_assumptions.yml")["records"]
        canonical_t1 = find_record(rev_records, "rev_reconstruction_table1_monthly")["value"]
        canonical_t2 = find_record(rev_records, "rev_reconstruction_table2_monthly")["value"]
        inputs = ramp_model.CanonicalRevenueInputs()
        t1_m5 = next(m for m in ramp_model.compute_ramp("scenario_table_1", inputs) if m["month"] == "M5plus")
        t2_m5 = next(m for m in ramp_model.compute_ramp("scenario_table_2", inputs) if m["month"] == "M5plus")
        self.assertAlmostEqual(t1_m5["total_revenue"], canonical_t1, places=2)
        self.assertAlmostEqual(t2_m5["total_revenue"], canonical_t2, places=2)


class MonthlyValuesReproducibleTests(unittest.TestCase):
    """(3) Month 1-4 values are mathematically reproducible."""

    def test_table1_month1_to_4_match_recorded_yaml_values(self):
        ramp_records = load_yaml("revenue_ramp.yml")["records"]
        inputs = ramp_model.CanonicalRevenueInputs()
        computed = {m["month"]: m for m in ramp_model.compute_ramp("scenario_table_1", inputs)}
        for month in ("M1", "M2", "M3", "M4"):
            rec = find_record(ramp_records, f"ramp_table1_{month.lower()}")
            self.assertAlmostEqual(computed[month]["total_revenue"], rec["total_revenue"], places=2)
            self.assertAlmostEqual(computed[month]["am_revenue"], rec["am_revenue"], places=2)
            self.assertAlmostEqual(computed[month]["pm_revenue"], rec["pm_revenue"], places=2)

    def test_table2_month1_to_4_match_recorded_yaml_values(self):
        ramp_records = load_yaml("revenue_ramp.yml")["records"]
        inputs = ramp_model.CanonicalRevenueInputs()
        computed = {m["month"]: m for m in ramp_model.compute_ramp("scenario_table_2", inputs)}
        for month in ("M1", "M2", "M3", "M4"):
            rec = find_record(ramp_records, f"ramp_table2_{month.lower()}")
            self.assertAlmostEqual(computed[month]["total_revenue"], rec["total_revenue"], places=2)
            self.assertAlmostEqual(computed[month]["am_revenue"], rec["am_revenue"], places=2)
            self.assertAlmostEqual(computed[month]["pm_revenue"], rec["pm_revenue"], places=2)

    def test_month1_is_exactly_43_percent_of_steady_state(self):
        """Independently reproduces the ramp-percentage arithmetic itself, not
        just re-reading the stored value."""
        inputs = ramp_model.CanonicalRevenueInputs()
        months = ramp_model.compute_ramp("scenario_table_1", inputs)
        m1 = next(m for m in months if m["month"] == "M1")
        m5 = next(m for m in months if m["month"] == "M5plus")
        self.assertAlmostEqual(m1["total_revenue"], m5["total_revenue"] * 0.43, places=2)


class ScenarioChangeTests(unittest.TestCase):
    """(4) Changing scenario changes the result appropriately."""

    def test_table1_and_table2_differ_only_in_am_component(self):
        inputs = ramp_model.CanonicalRevenueInputs()
        t1 = {m["month"]: m for m in ramp_model.compute_ramp("scenario_table_1", inputs)}
        t2 = {m["month"]: m for m in ramp_model.compute_ramp("scenario_table_2", inputs)}
        for month in ("M1", "M2", "M3", "M4", "M5plus"):
            # PM revenue must be identical between scenarios at every month --
            # PM is not AM-client-volume-dependent.
            self.assertAlmostEqual(t1[month]["pm_revenue"], t2[month]["pm_revenue"], places=2)
            # AM revenue must differ (Table 1 has more clients than Table 2).
            self.assertGreater(t1[month]["am_revenue"], t2[month]["am_revenue"])

    def test_table1_steady_state_exceeds_table2(self):
        inputs = ramp_model.CanonicalRevenueInputs()
        t1_m5 = next(m for m in ramp_model.compute_ramp("scenario_table_1", inputs) if m["month"] == "M5plus")
        t2_m5 = next(m for m in ramp_model.compute_ramp("scenario_table_2", inputs) if m["month"] == "M5plus")
        self.assertGreater(t1_m5["total_revenue"], t2_m5["total_revenue"])


class RampCurveChangeTests(unittest.TestCase):
    """(5) Changing the ramp changes revenue predictably -- proves the curve
    is a swappable input, not hard-wired into the engine."""

    def test_alternative_linear_ramp_produces_different_predictable_result(self):
        inputs = ramp_model.CanonicalRevenueInputs()
        linear_curve = [("M1", 20), ("M2", 40), ("M3", 60), ("M4", 80), ("M5plus", 100)]
        default_months = ramp_model.compute_ramp("scenario_table_1", inputs)
        linear_months = ramp_model.compute_ramp("scenario_table_1", inputs, ramp_curve=linear_curve)
        default_m1 = next(m for m in default_months if m["month"] == "M1")
        linear_m1 = next(m for m in linear_months if m["month"] == "M1")
        # Default curve (43%) must produce more Month 1 revenue than the
        # alternative linear curve (20%) -- a predictable, explainable result.
        self.assertGreater(default_m1["total_revenue"], linear_m1["total_revenue"])
        # Both must still converge to the exact same steady state at M5plus,
        # since only the ramp-in shape changed, not the ceiling.
        default_m5 = next(m for m in default_months if m["month"] == "M5plus")
        linear_m5 = next(m for m in linear_months if m["month"] == "M5plus")
        self.assertAlmostEqual(default_m5["total_revenue"], linear_m5["total_revenue"], places=2)

    def test_zero_pct_ramp_produces_zero_revenue(self):
        inputs = ramp_model.CanonicalRevenueInputs()
        zero_curve = [("M1", 0)]
        months = ramp_model.compute_ramp("scenario_table_1", inputs, ramp_curve=zero_curve)
        self.assertAlmostEqual(months[0]["total_revenue"], 0.0, places=2)


class HistoricalFigureNotUsedTests(unittest.TestCase):
    """(6) No historical inherited revenue figure is accidentally used."""

    def test_ramp_does_not_reproduce_inherited_historical_totals(self):
        rev_records = load_yaml("revenue_assumptions.yml")["records"]
        historical_t1 = find_record(rev_records, "rev_historical_table1_monthly_inherited")["value"]
        historical_t2 = find_record(rev_records, "rev_historical_table2_monthly_inherited")["value"]
        inputs = ramp_model.CanonicalRevenueInputs()
        t1_m5 = next(m for m in ramp_model.compute_ramp("scenario_table_1", inputs) if m["month"] == "M5plus")
        t2_m5 = next(m for m in ramp_model.compute_ramp("scenario_table_2", inputs) if m["month"] == "M5plus")
        # The canonical ramp's steady state must NOT match the old inherited
        # (untraceable-origin) historical totals -- it must match the new
        # canonical methodology instead (already proven in
        # SteadyStateConvergenceTests above).
        self.assertNotAlmostEqual(t1_m5["total_revenue"], historical_t1, places=2)
        self.assertNotAlmostEqual(t2_m5["total_revenue"], historical_t2, places=2)

    def test_revenue_ramp_yaml_historical_reference_entries_are_marked_superseded(self):
        data = load_yaml("revenue_ramp.yml")
        for rec in data.get("historical_ramp_reference", []):
            self.assertEqual(rec["status"], "SUPERSEDED", f"{rec['id']} must be marked SUPERSEDED")


class CanonicalMethodologyUnderlyingTests(unittest.TestCase):
    """(7) The canonical revenue methodology remains the underlying calculation."""

    def test_ramp_steady_state_formula_matches_methodology_module(self):
        """Imports tests/test_revenue_methodology.py's own formula and confirms
        the ramp model's steady-state (100%) output matches it exactly --
        proves the ramp is built ON TOP of the canonical methodology, not a
        separate, disconnected calculation."""
        methodology_spec = importlib.util.spec_from_file_location(
            "test_revenue_methodology", REPO_ROOT / "tests" / "test_revenue_methodology.py"
        )
        methodology = importlib.util.module_from_spec(methodology_spec)
        methodology_spec.loader.exec_module(methodology)

        inputs = ramp_model.CanonicalRevenueInputs()
        methodology_result = methodology.compute_monthly_revenue(
            client_volume=inputs.client_volume["scenario_table_1"],
            am_price=inputs.am_price,
            pm_weekday_sessions=inputs.pm_weekday_sessions,
            pm_saturday_sessions=inputs.pm_saturday_sessions,
            pm_price=inputs.pm_price,
            operating_days_weekday=inputs.operating_days_weekday,
            operating_saturdays=inputs.operating_saturdays,
            ancillary_monthly=inputs.ancillary_monthly,
        )
        ramp_result = next(
            m for m in ramp_model.compute_ramp("scenario_table_1", inputs) if m["month"] == "M5plus"
        )
        self.assertAlmostEqual(methodology_result, ramp_result["total_revenue"], places=2)


class PmCapacityCeilingTests(unittest.TestCase):
    """(8) PM session capacity cannot silently exceed canonical capacity."""

    def test_pm_revenue_never_exceeds_canonical_capacity_ceiling(self):
        inputs = ramp_model.CanonicalRevenueInputs()
        pm_ceiling = (
            inputs.pm_weekday_sessions * inputs.pm_price * inputs.operating_days_weekday
            + inputs.pm_saturday_sessions * inputs.pm_price * inputs.operating_saturdays
        )
        for scenario_id in ("scenario_table_1", "scenario_table_2"):
            for m in ramp_model.compute_ramp(scenario_id, inputs):
                self.assertLessEqual(m["pm_revenue"], pm_ceiling + 0.02)

    def test_overstated_ramp_curve_is_caught(self):
        """A ramp curve that (incorrectly) exceeds 100% must produce PM revenue
        above the canonical ceiling -- proving the ceiling check in
        tools/validate_canonical_data.py's check_revenue_ramp_schema would
        actually catch a real error, not just pass trivially."""
        inputs = ramp_model.CanonicalRevenueInputs()
        broken_curve = [("M1", 150)]  # 150% -- invalid, more than steady state
        months = ramp_model.compute_ramp("scenario_table_1", inputs, ramp_curve=broken_curve)
        pm_ceiling = (
            inputs.pm_weekday_sessions * inputs.pm_price * inputs.operating_days_weekday
            + inputs.pm_saturday_sessions * inputs.pm_price * inputs.operating_saturdays
        )
        self.assertGreater(months[0]["pm_revenue"], pm_ceiling)


class CanonicalIdReferenceTests(unittest.TestCase):
    """(9) All referenced canonical IDs exist."""

    def test_revenue_ramp_derived_from_ids_exist(self):
        ramp_data = load_yaml("revenue_ramp.yml")
        rev_records = load_yaml("revenue_assumptions.yml")["records"]
        rev_ids = {r["id"] for r in rev_records}
        rev_ids.add(ramp_data["ramp_curve"]["id"])  # the ramp curve's own id, self-referenced
        for rec in ramp_data["records"]:
            for ref_id in rec.get("derived_from", []):
                self.assertIn(
                    ref_id, rev_ids,
                    f"{rec['id']}: derived_from references {ref_id!r}, which does not exist "
                    f"in revenue_assumptions.yml or this file's own ramp_curve id",
                )

    def test_revenue_ramp_scenario_ids_exist_in_scenarios_yml(self):
        ramp_records = load_yaml("revenue_ramp.yml")["records"]
        scenario_records = load_yaml("scenarios.yml")["records"]
        valid_scenario_ids = {r["id"] for r in scenario_records}
        for rec in ramp_records:
            self.assertIn(rec["scenario_id"], valid_scenario_ids)


class DeterminismTests(unittest.TestCase):
    """(10) The model is deterministic."""

    def test_repeated_calls_produce_identical_output(self):
        inputs = ramp_model.CanonicalRevenueInputs()
        first = ramp_model.compute_ramp("scenario_table_1", inputs)
        second = ramp_model.compute_ramp("scenario_table_1", inputs)
        self.assertEqual(first, second)

    def test_fresh_inputs_produce_identical_output(self):
        """Re-loading canonical inputs from disk (a fresh CanonicalRevenueInputs
        instance, not the same object) must still produce the same result."""
        first = ramp_model.compute_ramp("scenario_table_2", ramp_model.CanonicalRevenueInputs())
        second = ramp_model.compute_ramp("scenario_table_2", ramp_model.CanonicalRevenueInputs())
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
