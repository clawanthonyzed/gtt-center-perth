"""
Reproduction tests for docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md (adopted
2026-08-09, per Anthony's direct decision).

Purpose: prove the canonical days-based first-principles revenue formula is
deterministic and fully reproducible directly from data/canonical/*.yml inputs --
NOT a hard-coded, unexplained historical number. Every input used below is read
from the canonical YAML files by id; nothing is inlined as a magic constant except
inside the formula itself (client_volume x price x operating_days, summed across
AM/PM x weekday/Saturday -- see the methodology doc for the full derivation).

Run:
    python tests/test_revenue_methodology.py
    (or: python -m unittest tests.test_revenue_methodology -v, from repo root)
"""

import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIR = REPO_ROOT / "data" / "canonical"


def load_yaml(filename):
    path = CANONICAL_DIR / filename
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_record(records, record_id):
    """Return the first record dict in `records` whose id == record_id."""
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


def find_scenario_record(records, scenario_id):
    """scenarios.yml's records list uses id == the scenario id directly."""
    return find_record(records, scenario_id)


class CanonicalInputs:
    """Loads every input the canonical revenue formula needs, by id, from the
    canonical YAML files -- mirrors docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md §3."""

    def __init__(self):
        client_assumptions = load_yaml("client_assumptions.yml")
        scenarios = load_yaml("scenarios.yml")
        pricing = load_yaml("pricing.yml")
        revenue_assumptions = load_yaml("revenue_assumptions.yml")

        universal = client_assumptions["universal"]
        self.pm_weekday_sessions = find_record(universal, "pm_steady_state_capacity")["value"]
        self.operating_days_weekday = find_record(universal, "operating_days_per_month_weekday")["value"]
        self.operating_saturdays = find_record(universal, "operating_saturdays_per_month")["value"]

        scenario_records = scenarios["records"]
        self.client_volume_table1 = find_scenario_record(scenario_records, "scenario_table_1")["client_volume"]["value"]
        self.client_volume_table2 = find_scenario_record(scenario_records, "scenario_table_2")["client_volume"]["value"]

        pricing_records = pricing["records"]
        self.am_price = find_record(pricing_records, "am_price_used_for_revenue")["price"]
        self.pm_price = find_record(pricing_records, "pm_alacarte_average")["price"]

        rev_records = revenue_assumptions["records"]
        self.pm_saturday_sessions = find_record(rev_records, "rev_pm_saturday_sessions")["value"]
        self.ancillary_monthly = find_record(rev_records, "rev_ancillary_excluded_from_baseline")["value"]

        # Canonical/expected outputs and preserved historical figures, also read
        # from the YAML -- not hard-coded, so this test breaks (correctly) if
        # anyone edits the canonical figures without updating the methodology.
        self.canonical_table1_monthly = find_record(rev_records, "rev_reconstruction_table1_monthly")["value"]
        self.canonical_table2_monthly = find_record(rev_records, "rev_reconstruction_table2_monthly")["value"]
        self.historical_table1_monthly = find_record(rev_records, "rev_historical_table1_monthly_inherited")["value"]
        self.historical_table2_monthly = find_record(rev_records, "rev_historical_table2_monthly_inherited")["value"]


def compute_monthly_revenue(
    client_volume,
    am_price,
    pm_weekday_sessions,
    pm_saturday_sessions,
    pm_price,
    operating_days_weekday,
    operating_saturdays,
    ancillary_monthly=0.0,
):
    """The canonical formula -- docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md §4.

    Monthly Revenue =
        (client_volume x am_price x operating_days_weekday)        [AM Weekday]
      + (client_volume x am_price x operating_saturdays)           [AM Saturday]
      + (pm_weekday_sessions x pm_price x operating_days_weekday)  [PM Weekday]
      + (pm_saturday_sessions x pm_price x operating_saturdays)    [PM Saturday]
      + ancillary_monthly                                         [Ancillary]
    """
    am_weekday = client_volume * am_price * operating_days_weekday
    am_saturday = client_volume * am_price * operating_saturdays
    pm_weekday = pm_weekday_sessions * pm_price * operating_days_weekday
    pm_saturday = pm_saturday_sessions * pm_price * operating_saturdays
    return am_weekday + am_saturday + pm_weekday + pm_saturday + ancillary_monthly


class CanonicalRevenueMethodologyTests(unittest.TestCase):
    def setUp(self):
        self.inputs = CanonicalInputs()

    def _table1_result(self):
        i = self.inputs
        return compute_monthly_revenue(
            client_volume=i.client_volume_table1,
            am_price=i.am_price,
            pm_weekday_sessions=i.pm_weekday_sessions,
            pm_saturday_sessions=i.pm_saturday_sessions,
            pm_price=i.pm_price,
            operating_days_weekday=i.operating_days_weekday,
            operating_saturdays=i.operating_saturdays,
            ancillary_monthly=i.ancillary_monthly,
        )

    def _table2_result(self):
        i = self.inputs
        return compute_monthly_revenue(
            client_volume=i.client_volume_table2,
            am_price=i.am_price,
            pm_weekday_sessions=i.pm_weekday_sessions,
            pm_saturday_sessions=i.pm_saturday_sessions,
            pm_price=i.pm_price,
            operating_days_weekday=i.operating_days_weekday,
            operating_saturdays=i.operating_saturdays,
            ancillary_monthly=i.ancillary_monthly,
        )

    def test_table1_matches_canonical_value(self):
        """Table 1 (18 clients/day) computed purely from canonical inputs must equal
        the recorded rev_reconstruction_table1_monthly value exactly (to the cent).
        RECALCULATED 2026-08-17 (Phase C) -- was 155215.80 (A$95 PM placeholder
        average), now 163721.88 (real A$117 PM average, docs/architecture/
        PM-PACKAGES.md §5)."""
        result = self._table1_result()
        self.assertAlmostEqual(result, self.inputs.canonical_table1_monthly, places=2)
        self.assertAlmostEqual(result, 163721.88, places=2)

    def test_table2_matches_canonical_value(self):
        """Table 2 (12 clients/day) computed purely from canonical inputs must equal
        the recorded rev_reconstruction_table2_monthly value exactly (to the cent).
        RECALCULATED 2026-08-17 (Phase C) -- was 115720.80, now 124226.88."""
        result = self._table2_result()
        self.assertAlmostEqual(result, self.inputs.canonical_table2_monthly, places=2)
        self.assertAlmostEqual(result, 124226.88, places=2)

    def test_deterministic(self):
        """Calling the formula twice with the same canonical inputs must produce the
        exact same output -- proves this is a pure, reproducible function, not
        something that varies run to run."""
        first = self._table1_result()
        second = self._table1_result()
        self.assertEqual(first, second)

    def test_pm_component_identical_across_scenarios(self):
        """PM revenue is not AM-client-volume-dependent -- Table 1 and Table 2 must
        produce identical PM Weekday/Saturday components, per
        docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md §9/§14."""
        i = self.inputs
        pm_component = (
            i.pm_weekday_sessions * i.pm_price * i.operating_days_weekday
            + i.pm_saturday_sessions * i.pm_price * i.operating_saturdays
        )
        table1_pm_only = compute_monthly_revenue(
            client_volume=0,
            am_price=i.am_price,
            pm_weekday_sessions=i.pm_weekday_sessions,
            pm_saturday_sessions=i.pm_saturday_sessions,
            pm_price=i.pm_price,
            operating_days_weekday=i.operating_days_weekday,
            operating_saturdays=i.operating_saturdays,
            ancillary_monthly=0.0,
        )
        self.assertAlmostEqual(table1_pm_only, pm_component, places=2)
        # Confirm the difference between Table 1 and Table 2 totals is purely the
        # AM component (the only input that differs between scenarios).
        am_only_delta = (i.client_volume_table1 - i.client_volume_table2) * i.am_price * (
            i.operating_days_weekday + i.operating_saturdays
        )
        self.assertAlmostEqual(self._table1_result() - self._table2_result(), am_only_delta, places=2)

    def test_sensitivity_to_client_volume(self):
        """Increasing client_volume by 1 must increase Monthly Revenue by exactly
        am_price x (operating_days_weekday + operating_saturdays) -- proves the
        formula actually responds to its stated inputs rather than being a
        disguised constant."""
        i = self.inputs
        baseline = compute_monthly_revenue(
            client_volume=i.client_volume_table1,
            am_price=i.am_price,
            pm_weekday_sessions=i.pm_weekday_sessions,
            pm_saturday_sessions=i.pm_saturday_sessions,
            pm_price=i.pm_price,
            operating_days_weekday=i.operating_days_weekday,
            operating_saturdays=i.operating_saturdays,
            ancillary_monthly=i.ancillary_monthly,
        )
        plus_one_client = compute_monthly_revenue(
            client_volume=i.client_volume_table1 + 1,
            am_price=i.am_price,
            pm_weekday_sessions=i.pm_weekday_sessions,
            pm_saturday_sessions=i.pm_saturday_sessions,
            pm_price=i.pm_price,
            operating_days_weekday=i.operating_days_weekday,
            operating_saturdays=i.operating_saturdays,
            ancillary_monthly=i.ancillary_monthly,
        )
        expected_delta = i.am_price * (i.operating_days_weekday + i.operating_saturdays)
        self.assertAlmostEqual(plus_one_client - baseline, expected_delta, places=2)

    def test_canonical_output_differs_from_preserved_historical_figure(self):
        """Per the coordinator's explicit instruction (Part 5, methodology-adoption
        phase): the new canonical figures must NOT be forced to equal the old
        inherited figures. This test pins down that the two are deliberately,
        provably different. RECALCULATED 2026-08-17 (Phase C) -- the original gap
        was +A$2,576.36 (historical figure higher than canonical, at the A$95 PM
        placeholder average, docs/architecture/REVENUE-RECONCILIATION-
        INVESTIGATION.md). Since the canonical PM average was rebuilt to the real
        A$117 figure (docs/architecture/PM-PACKAGES.md §5), the canonical revenue
        figure is now LARGER than the historical figure -- the gap is
        -A$5,929.72 (canonical exceeds historical), a sign flip, not an error.
        Both values remain readable from the canonical data (neither was
        deleted)."""
        i = self.inputs
        table1_gap = i.historical_table1_monthly - self._table1_result()
        table2_gap = i.historical_table2_monthly - self._table2_result()
        self.assertAlmostEqual(table1_gap, -5929.72, places=2)
        self.assertAlmostEqual(table2_gap, -5929.72, places=2)
        self.assertAlmostEqual(table1_gap, table2_gap, places=2)


if __name__ == "__main__":
    unittest.main()
