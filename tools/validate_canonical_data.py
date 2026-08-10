"""
GTT Center Perth -- Canonical data validator (proof of concept).

Validates data/canonical/*.yml files against the schema/governance conventions
established in docs/architecture/CANONICAL-DATA-SCHEMA.md and
docs/architecture/DATA-GOVERNANCE.md. This is a proof-of-concept validator for
twelve files (pricing.yml, client_assumptions.yml, scenarios.yml, staffing.yml,
wages.yml -- Phase 2; opex.yml -- Phase 3; startup_costs.yml, capex.yml --
Phase 4; services.yml -- Phase 5; revenue_assumptions.yml -- Phase 6;
revenue_ramp.yml -- Phase 7; cost_ramp.yml -- Phase 8) -- it is not a general
schema engine and does not validate every field type strictly.

Checks performed:
  1. YAML validity (parse error -> hard failure)
  2. Expected top-level structure: every file must have `schema_version` and
     `dataset` keys, and at least one list-of-records key
     (records / universal / scenario_dependent / historical_scenarios /
     operational_buffers / open_items / historical_staffing_scenarios).
  3. Only the 7 permitted statuses are used anywhere in the file (recursive
     scan for any `status` key at any nesting depth).
  4. Every non-PLACEHOLDER value carries a `source` reference (a dict with at
     least a `file` key) -- checked at the same level as each `status` key.
  5. Duplicate ID detection -- within each list, records must have unique
     `id` values, EXCEPT `scenario_dependent` in client_assumptions.yml,
     where the same conceptual `id` deliberately repeats once per
     `scenario_id` (a documented, intentional schema choice -- see that
     file's own comments) -- duplicates there are keyed on (id, scenario_id).
     Also checked GLOBALLY across every file validated in a single run (a
     `records[*].id` should not collide across different canonical files
     either).
  6. Conflicting-value detection -- within a file's `records` list, two
     non-SUPERSEDED/non-PLACEHOLDER records sharing the same
     (category, name) but a different `price` are flagged. Also surfaces
     anything explicitly listed under a file's own `conflicts:` key.
  7. Scenario-registry invariant (scenarios.yml only) -- both
     `scenario_table_1` and `scenario_table_2` must exist, and BOTH must have
     `is_primary: false`. This is a deliberate, phase-specific invariant (see
     docs/VERIFICATION-TRACKER.md item 1m) -- revisit this check the day
     Anthony actually resolves which scenario is primary.
  8. (Phase 2, staffing.yml) Required fields per record (id, role, category,
     status) and `category` restricted to a known vocabulary (treatment,
     phlebotomy, management_admin, other) -- preserves the coordinator's
     instruction to keep these groupings distinguishable, not free text.
  9. (Phase 2, wages.yml) Every record that carries a rate/value field
     (`hourly_rate`, `salary`, `value`, `value_pct`, `value_hours`) must have
     that field's presence consistent with its `status`: a `PLACEHOLDER`
     record must NOT assert a concrete value (that would be an invented
     figure smuggled in under an honest-sounding label), and a
     non-PLACEHOLDER "rate-shaped" record must not be null (a status implying
     confidence with nothing behind it).
  10. (Phase 2) Scenario-reference validity -- any `staffing_scenario` or
      `scenario_id` field found anywhere (staffing.yml, client_assumptions.yml)
      must be either the literal string `universal` or an id that actually
      exists in scenarios.yml's `records` or `historical_scenarios` lists
      (loaded automatically from data/canonical/scenarios.yml regardless of
      which files were passed as targets, so a malformed/typo'd scenario
      reference is always caught).
  11. (Phase 3, opex.yml) Required fields per record (id, category, name,
      status, frequency, cost_type); `frequency` restricted to a known
      vocabulary (weekly/monthly/quarterly/annual/one_off/per_transaction/
      not_specified); `cost_type` restricted to the coordinator's 8-value
      vocabulary (FIXED/VARIABLE/SEMI_VARIABLE/ONE_OFF/STARTUP/CAPEX/COGS/
      PAYROLL).
  12. (Phase 3, opex.yml) `amount` (and `monthly_equivalent`/
      `annual_equivalent`, where present) must be `null`, a plain number, or
      a dict whose every value is a plain number (covers low/high ranges,
      per-month ramps, etc.) -- anything else is a malformed numeric value.
      A `PLACEHOLDER` record must have `amount: null` (a real record with a
      concrete value is not a placeholder, whatever its confidence level);
      a non-`PLACEHOLDER`/non-`SUPERSEDED` record must NOT have `amount: null`
      (a confident status needs something behind it) -- same rule already
      applied to wages.yml's rate fields (§9), reused here.
  13. (Phase 3, opex.yml) Monthly/annual normalisation correctness -- where
      `frequency` is `monthly`/`quarterly`/`annual` and `amount` is present,
      any stated `monthly_equivalent`/`annual_equivalent` must arithmetically
      match `amount` at that frequency (within a small floating-point
      tolerance). Records with `frequency` of `one_off`/`per_transaction`/
      `not_specified`, or with `amount: null`, are skipped -- no normalised
      equivalent should exist to check in those cases.
  14. (Phase 4, startup_costs.yml + capex.yml) Required fields per record
      (id/category/item/status for startup_costs.yml `records`;
      id/asset_category/asset_name/status for capex.yml `records`).
      `total_cost`, `unit_cost`, `value_pct`, and `quantity` fields (wherever
      present, in `records`, `funding_requirements`, `historical_total_estimates`,
      and `contingency_assumptions`) must be `null`, a plain number, or a dict
      whose every value is a plain number -- same malformed-numeric-value and
      status-vs-value consistency rules as opex.yml's `amount` field (§12),
      reused here across four list keys instead of one.
  15. (Phase 4) Quantity x unit-cost consistency -- where a record has
      `quantity`, `unit_cost`, and `total_cost` all present and numeric (or
      numeric dicts with matching keys), `total_cost` must be within 0.5% of
      `quantity x unit_cost`. Records missing any of the three (very common in
      this dataset -- most section-total records have `quantity: null` or
      `unit_cost: null` deliberately, since the source doesn't itemise a
      per-unit rate) are skipped, not treated as a failure.
  16. (Phase 4, capex.yml only) No invented depreciation assumptions -- a
      record with a non-null `useful_life_years` or `depreciation_method`
      must carry a `status_detail` explaining its basis (the coordinator's
      explicit instruction: "do NOT invent useful lives or depreciation
      methods, mark unresolved/PLACEHOLDER if the repo doesn't state them" --
      this validator enforces that any such field, if ever populated in a
      future edit, cannot appear silently unexplained). `useful_life_years`,
      if set, must be a positive number; `depreciation_method`, if set, must
      be a non-empty string.
  17. (Phase 4) `scenario_applicability` (used by startup_costs.yml and
      capex.yml, alongside the existing `staffing_scenario`/`scenario_id`
      fields from Phase 2) is now also validated against the scenario
      registry (§10) -- must be `universal` or a real id from scenarios.yml.
  18. (Phase 5, services.yml) Required fields per `records` entry (id,
      category, name, status, lifecycle); `lifecycle` restricted to
      current/proposed/historical/superseded -- a field distinct from the
      governance `status`, per the coordinator's explicit instruction not to
      invent an 8th governance status for this.
  19. (Phase 5) Pricing-reference validity -- any `pricing_ref` field must be
      an id that actually exists in data/canonical/pricing.yml's own
      `records` list (loaded automatically, regardless of which files are
      targeted, same pattern as the scenario-registry check). A record with
      a `pricing_ref` is exempted from needing its own `price`/`price_range`
      (the price lives in pricing.yml, referenced not restated -- see
      services.yml's own header for the full architecture rationale).
  20. (Phase 5) Status-vs-value consistency, adapted for services.yml's
      dual price representation (`price`, a number, OR `price_range`, a
      free-text range string, since several source documents state prices as
      hyphenated ranges rather than clean bounds) -- a `PLACEHOLDER` record
      must have both `price` and `price_range` null; a non-`PLACEHOLDER`/
      non-`SUPERSEDED` record must have at least one of `price`,
      `price_range`, or `pricing_ref` set.
  21. (Phase 6, revenue_assumptions.yml) Required fields per `records` entry
      (id, category, name, status). `service_ref`/`pricing_ref`, where set,
      must exist in services.yml/pricing.yml respectively (same pattern as
      §19, extended to a second reference field). `frequency`, where set,
      uses the same controlled vocabulary as opex.yml (§11) plus `daily`
      (added for this file's per-day client/session-volume records).
  22. (Phase 6) Percentage range check -- any `value` field (a plain number
      or a dict) whose record's `unit` is `"%"` must have every numeric
      value between 0 and 100 inclusive.
  23. (Phase 6) Status-vs-value consistency, generalised beyond a single
      `price`/`amount` field -- a non-`PLACEHOLDER`/`SUPERSEDED` record must
      have at least one of: `value` (not null), `service_ref`, `pricing_ref`,
      or a non-empty `description` (several records in this file are
      qualitative/policy facts with no single numeric value -- a real,
      sourced description satisfies the "needs something asserted" rule the
      same way a number or a reference does). A `PLACEHOLDER` record must
      have `value: null`.
  24. (Phase 6) Service-mix-totals-100 check -- applied ONLY when a record
      explicitly sets `mix_complete: true` (the coordinator's explicit
      instruction: do not require mix percentages to sum to 100% otherwise,
      since most mix-adjacent records in this file are deliberately partial
      or represent a single modelling convention, not a complete
      mutually-exclusive split). Where `mix_complete: true`, every `_pct`-
      suffixed key in the record's `value` dict must sum to 100 (+/- 0.5).
  25. (Phase 7, revenue_ramp.yml) Required fields per `records` entry (id,
      scenario_id, month, status); `month` restricted to M1/M2/M3/M4/M5plus;
      duplicate (scenario_id, month) pairs are rejected. `am_revenue`,
      `pm_revenue`, `ancillary_revenue`, `total_revenue`, and
      `steady_state_revenue` are checked for malformed numeric shape, and
      `am_revenue + pm_revenue + ancillary_revenue` must sum to
      `total_revenue`. `pct_of_steady_state` must arithmetically match
      `total_revenue / steady_state_revenue x 100`. At Month 5plus (100%),
      `pm_revenue` must not exceed the canonical PM capacity revenue ceiling
      (`pm_steady_state_capacity` + `rev_pm_saturday_sessions`, priced at
      `pm_alacarte_average`, scaled by the canonical operating-day
      assumptions) -- PM session volume cannot silently exceed canonical
      capacity. Status-vs-value consistency mirrors §23.

  26. (Phase 8, cost_ramp.yml) Required fields per `records` entry (id,
      scenario_id, month, status); `month` restricted to M1/M2/M3/M4/M5plus
      (§25's vocabulary, reused); duplicate (scenario_id, month) pairs are
      rejected. `fixed_costs`, `variable_costs`, `payroll_costs`, and
      `total_operating_costs` are checked for malformed numeric shape, and
      `fixed_costs + variable_costs + payroll_costs` must sum to
      `total_operating_costs`. Where present, `payroll_breakdown`'s 6 core
      components must sum to its own `direct_labor_and_opening_total`, and
      `direct_labor_and_opening_total + workers_comp + superannuation`
      (§27, `superannuation` defaults to 0 if absent) must sum to the
      record's own `payroll_costs` -- a cross-check ensuring every payroll
      component is genuinely recurring labor cost, not a smuggled-in
      startup/capex figure. Status-vs-value consistency mirrors §25.
  27. (Phase 9 resume, cost_ramp.yml, 2026-08-09) Superannuation --
      `payroll_breakdown.am_weekday_treatment_staff` +
      `.am_weekday_phlebotomist` must sum to `.am_weekday_direct_labor`,
      where all three are present (the split required to correctly apply
      superannuation only to the phlebotomist portion, per
      docs/financial-break-even-staff.md's own "incl. super" labelling
      asymmetry -- see tools/cost_ramp_model.py's SUPERANNUATION_RATE_PCT
      docstring for the full sourced reasoning).

Exit code: 0 if all checks pass across all validated files, 1 if any check
fails in any file. Usable in CI / pre-commit, same convention as
tools/check_consistency.py.

Usage:
    python tools/validate_canonical_data.py
    python tools/validate_canonical_data.py data/canonical/pricing.yml [...]
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required (pip install pyyaml).")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
CANON_DIR = REPO_ROOT / "data" / "canonical"
MODELS_DIR = REPO_ROOT / "data" / "models"  # Phase 9 -- Layer 3 (MODELS), generic checks only

ALLOWED_STATUSES = {
    "VERIFIED", "DECIDED", "CALCULATED", "MODELLED", "SCENARIO",
    "PLACEHOLDER", "SUPERSEDED",
}

REQUIRED_TOP_KEYS = {"schema_version", "dataset"}
RECORD_LIST_KEYS = {
    "records", "universal", "scenario_dependent", "historical_scenarios",
    "operational_buffers", "open_items", "historical_staffing_scenarios",
    "funding_requirements", "historical_total_estimates", "adopted_planning_scenarios",
    "contingency_assumptions",
    "historical_services", "future_services", "historical_ramp_reference",
    "historical_cost_reference", "marketing_ramp_reference",
    "assumptions", "historical_reconciliation", "traceability", "conflicts",
}

# staffing.yml -- category vocabulary the coordinator asked to be preserved,
# not left as free text.
KNOWN_STAFFING_CATEGORIES = {"treatment", "phlebotomy", "management_admin", "other"}
STAFFING_RECORD_REQUIRED_FIELDS = {"id", "role", "category", "status"}

# wages.yml -- field names that carry an actual rate/value, checked for
# consistency with the record's status (see check_wages_schema).
WAGE_VALUE_FIELDS = ("hourly_rate", "salary", "value", "value_pct", "value_hours")

# Fields, found anywhere in a file, that must reference a real scenario id
# (or the literal string "universal") -- validated against scenarios.yml.
SCENARIO_REF_FIELDS = {"staffing_scenario", "scenario_id", "scenario_applicability"}

# opex.yml -- required fields, and the two controlled vocabularies the
# coordinator specified (Part 2's cost-classification list; a frequency list
# derived from what Part 4's normalisation actually needs to distinguish).
OPEX_RECORD_REQUIRED_FIELDS = {"id", "category", "name", "status", "frequency", "cost_type"}
ALLOWED_OPEX_FREQUENCIES = {
    "weekly", "monthly", "quarterly", "annual", "one_off", "per_transaction", "not_specified",
    "daily",  # added Phase 6 for revenue_assumptions.yml's per-day client/session-volume records
}
ALLOWED_OPEX_COST_TYPES = {
    "FIXED", "VARIABLE", "SEMI_VARIABLE", "ONE_OFF", "STARTUP", "CAPEX", "COGS", "PAYROLL",
}
# Frequencies for which a monthly/annual equivalent is meaningful and checked.
NORMALISABLE_OPEX_FREQUENCIES = {"monthly", "quarterly", "annual"}
NUMERIC_TOLERANCE = 0.02  # AUD, floating-point/rounding slack for equivalence checks

# startup_costs.yml / capex.yml -- required fields per `records` entry.
STARTUP_COST_RECORD_REQUIRED_FIELDS = {"id", "category", "item", "status"}
CAPEX_RECORD_REQUIRED_FIELDS = {"id", "asset_category", "asset_name", "status"}
# Fields (wherever found, across records/funding_requirements/
# historical_total_estimates/contingency_assumptions) subject to the same
# malformed-numeric-value + status-vs-value consistency rules as opex.yml's
# `amount` field.
STARTUP_CAPEX_VALUE_FIELDS = ("total_cost", "unit_cost", "value_pct")
# Relative tolerance for the quantity x unit_cost == total_cost cross-check --
# looser than NUMERIC_TOLERANCE's flat AUD amount, since these figures often
# involve back-calculated per-unit rates with real (not error) rounding.
QUANTITY_UNIT_COST_RELATIVE_TOLERANCE = 0.005  # 0.5%

# services.yml -- required fields, lifecycle vocabulary (a field distinct
# from the 7 governance statuses, per the coordinator's explicit instruction).
SERVICES_RECORD_REQUIRED_FIELDS = {"id", "category", "name", "status", "lifecycle"}
ALLOWED_SERVICE_LIFECYCLES = {"current", "proposed", "historical", "superseded"}

# revenue_assumptions.yml -- required fields per `records` entry.
REVENUE_ASSUMPTIONS_RECORD_REQUIRED_FIELDS = {"id", "category", "name", "status"}

# revenue_ramp.yml (Phase 7) -- required fields per `records` entry, and the
# controlled month vocabulary (Month 1-4 individually, Month 5+ combined into
# one steady-state label, matching every historical ramp table's own shape).
REVENUE_RAMP_RECORD_REQUIRED_FIELDS = {"id", "scenario_id", "month", "status"}
ALLOWED_RAMP_MONTHS = {"M1", "M2", "M3", "M4", "M5plus"}
# Fields subject to the malformed-numeric-value check (same rule as opex.yml's
# `amount`, capex.yml's `total_cost`, etc.).
REVENUE_RAMP_VALUE_FIELDS = ("am_revenue", "pm_revenue", "ancillary_revenue", "total_revenue", "steady_state_revenue")
REVENUE_RAMP_TOLERANCE = 0.02  # AUD, floating-point/rounding slack -- same as NUMERIC_TOLERANCE

# cost_ramp.yml (Phase 8) -- required fields per `records` entry, reusing
# revenue_ramp.yml's month vocabulary (§25) since both files share the same
# Month 1-5+ shape.
COST_RAMP_RECORD_REQUIRED_FIELDS = {"id", "scenario_id", "month", "status"}
COST_RAMP_VALUE_FIELDS = ("fixed_costs", "variable_costs", "payroll_costs", "total_operating_costs")
COST_RAMP_TOLERANCE = 0.02  # AUD, floating-point/rounding slack

# scenario_dependent intentionally repeats `id` once per scenario_id -- see
# data/canonical/client_assumptions.yml's own header comment.
DUPLICATE_KEY_OVERRIDES = {
    "scenario_dependent": lambda rec: (rec.get("id"), rec.get("scenario_id")),
}


class Findings:
    def __init__(self, filename):
        self.filename = filename
        self.errors = []
        self.warnings = []

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    @property
    def ok(self):
        return not self.errors


def walk_status_fields(node, path="root"):
    """Yield (path, dict) for every dict in the structure that has a 'status' key."""
    if isinstance(node, dict):
        if "status" in node:
            yield path, node
        for k, v in node.items():
            yield from walk_status_fields(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from walk_status_fields(item, f"{path}[{i}]")


def check_structure(data, f: Findings):
    if not isinstance(data, dict):
        f.error("Top-level YAML content is not a mapping/dict.")
        return
    missing = REQUIRED_TOP_KEYS - set(data.keys())
    if missing:
        f.error(f"Missing required top-level key(s): {sorted(missing)}")
    present_lists = [k for k in RECORD_LIST_KEYS if k in data]
    if not present_lists:
        f.error(
            f"No recognised record-list key found (expected at least one of "
            f"{sorted(RECORD_LIST_KEYS)})."
        )


def check_statuses(data, f: Findings):
    for path, node in walk_status_fields(data):
        status = node.get("status")
        if status not in ALLOWED_STATUSES:
            f.error(f"{path}: disallowed status value '{status}' (allowed: {sorted(ALLOWED_STATUSES)})")


def check_sources(data, f: Findings):
    for path, node in walk_status_fields(data):
        status = node.get("status")
        if status == "PLACEHOLDER":
            continue  # a PLACEHOLDER is explicitly allowed to have no source
        source = node.get("source")
        if source is None:
            f.error(f"{path}: status={status} but no 'source' key present (required for any non-PLACEHOLDER value)")
        elif isinstance(source, dict):
            if not source.get("file"):
                f.error(f"{path}: 'source' present but missing a 'file' field")
        elif isinstance(source, str):
            f.warn(f"{path}: 'source' is a plain string, not a {{file, section}} dict -- allowed but not the preferred structured form")
        else:
            f.error(f"{path}: 'source' has an unexpected type ({type(source).__name__})")


def check_duplicate_ids(data, f: Findings):
    for list_key in RECORD_LIST_KEYS:
        items = data.get(list_key)
        if not isinstance(items, list):
            continue
        key_fn = DUPLICATE_KEY_OVERRIDES.get(list_key, lambda rec: rec.get("id"))
        seen = {}
        for i, rec in enumerate(items):
            if not isinstance(rec, dict):
                continue
            key = key_fn(rec)
            if key in seen:
                f.error(f"{list_key}[{i}]: duplicate key {key!r} (first seen at index {seen[key]})")
            else:
                seen[key] = i


def check_conflicting_values(data, f: Findings):
    declared = data.get("conflicts")
    if declared:
        for c in declared:
            f.warn(f"Declared conflict present in file's own 'conflicts' list: {c}")

    records = data.get("records")
    if not isinstance(records, list):
        return
    grouped = {}
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            continue
        status = rec.get("status")
        if status in ("SUPERSEDED", "PLACEHOLDER", "SCENARIO"):
            continue  # these are allowed to legitimately differ / not yet be singular truth
        price = rec.get("price")
        if price is None:
            continue
        key = (rec.get("category"), rec.get("name"))
        grouped.setdefault(key, []).append((i, price, rec.get("id")))
    for key, entries in grouped.items():
        prices = {p for _, p, _ in entries}
        if len(entries) > 1 and len(prices) > 1:
            f.error(
                f"Conflicting prices for {key}: {[(rid, p) for _, p, rid in entries]} "
                f"-- two sources/records disagree and this was not resolved to a single value"
            )


def check_scenario_registry_invariant(data, f: Findings):
    if data.get("dataset") != "scenarios":
        return
    records = data.get("records", [])
    by_id = {r.get("id"): r for r in records if isinstance(r, dict)}
    required = {"scenario_table_1", "scenario_table_2"}
    missing = required - set(by_id.keys())
    if missing:
        f.error(f"scenarios.yml is missing required scenario record(s): {sorted(missing)}")
        return
    for sid in required:
        is_primary = by_id[sid].get("is_primary")
        if is_primary is not False:
            f.error(
                f"scenarios.yml: '{sid}'.is_primary is {is_primary!r}, expected False -- "
                f"neither Table 1 nor Table 2 may be marked primary until "
                f"docs/VERIFICATION-TRACKER.md item 1m is resolved by Anthony"
            )
    primaries = [rid for rid, r in by_id.items() if r.get("is_primary") is True]
    if primaries:
        f.error(f"scenarios.yml: unexpected is_primary=true on {primaries} -- this phase requires both false")


def check_staffing_schema(data, f: Findings):
    if data.get("dataset") != "staffing":
        return
    records = data.get("records", [])
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            f.error(f"records[{i}]: not a mapping -- cannot check required fields")
            continue
        missing = STAFFING_RECORD_REQUIRED_FIELDS - set(rec.keys())
        if missing:
            f.error(f"records[{i}] (id={rec.get('id')!r}): missing required staffing field(s): {sorted(missing)}")
        category = rec.get("category")
        if category is not None and category not in KNOWN_STAFFING_CATEGORIES:
            f.error(
                f"records[{i}] (id={rec.get('id')!r}): category {category!r} is not one of "
                f"the known staffing categories {sorted(KNOWN_STAFFING_CATEGORIES)}"
            )


def check_wages_schema(data, f: Findings):
    if data.get("dataset") != "wages":
        return
    records = data.get("records", [])
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            f.error(f"records[{i}]: not a mapping -- cannot check required fields")
            continue
        if "id" not in rec or "role" not in rec or "status" not in rec:
            f.error(f"records[{i}] (id={rec.get('id')!r}): missing one of required wage fields (id, role, status)")
            continue

        status = rec.get("status")
        present_value_fields = [vf for vf in WAGE_VALUE_FIELDS if vf in rec]
        if not present_value_fields:
            continue  # a record with no rate/value field at all (rare, but not itself an error)

        for vf in present_value_fields:
            val = rec.get(vf)
            is_null = val is None
            if status == "PLACEHOLDER" and not is_null:
                f.error(
                    f"records[{i}] (id={rec.get('id')!r}): status=PLACEHOLDER but '{vf}' is "
                    f"{val!r}, not null -- a PLACEHOLDER record must not assert a concrete "
                    f"value (that would be an invented figure under an honest-sounding label)"
                )
            if status not in ("PLACEHOLDER", "SUPERSEDED") and is_null:
                f.error(
                    f"records[{i}] (id={rec.get('id')!r}): status={status} but '{vf}' is null -- "
                    f"a non-PLACEHOLDER/SUPERSEDED record must have a real value backing its status"
                )


def _is_number(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _is_valid_amount_shape(x) -> bool:
    """None, a plain number, or a dict whose every value is a plain number."""
    if x is None:
        return True
    if _is_number(x):
        return True
    if isinstance(x, dict):
        return all(_is_number(v) for v in x.values())
    return False


def check_opex_schema(data, f: Findings):
    if data.get("dataset") != "opex":
        return
    records = data.get("records", [])
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            f.error(f"records[{i}]: not a mapping -- cannot check required fields")
            continue
        rid = rec.get("id")

        missing = OPEX_RECORD_REQUIRED_FIELDS - set(rec.keys())
        if missing:
            f.error(f"records[{i}] (id={rid!r}): missing required opex field(s): {sorted(missing)}")
            continue  # further checks below assume these fields exist

        freq = rec.get("frequency")
        if freq not in ALLOWED_OPEX_FREQUENCIES:
            f.error(
                f"records[{i}] (id={rid!r}): frequency {freq!r} is not one of "
                f"the known frequencies {sorted(ALLOWED_OPEX_FREQUENCIES)}"
            )

        cost_type = rec.get("cost_type")
        if cost_type not in ALLOWED_OPEX_COST_TYPES:
            f.error(
                f"records[{i}] (id={rid!r}): cost_type {cost_type!r} is not one of "
                f"the known cost types {sorted(ALLOWED_OPEX_COST_TYPES)}"
            )

        status = rec.get("status")
        for field_name in ("amount", "monthly_equivalent", "annual_equivalent"):
            if field_name not in rec:
                continue
            val = rec[field_name]
            if not _is_valid_amount_shape(val):
                f.error(
                    f"records[{i}] (id={rid!r}): '{field_name}' is a malformed numeric value "
                    f"({val!r}) -- must be null, a number, or a dict of numbers"
                )

        amount = rec.get("amount")
        if status == "PLACEHOLDER" and amount is not None:
            f.error(
                f"records[{i}] (id={rid!r}): status=PLACEHOLDER but 'amount' is {amount!r}, "
                f"not null -- a PLACEHOLDER record must not assert a concrete value"
            )
        if status not in ("PLACEHOLDER", "SUPERSEDED") and amount is None:
            f.error(
                f"records[{i}] (id={rid!r}): status={status} but 'amount' is null -- "
                f"a non-PLACEHOLDER/SUPERSEDED record must have a real value backing its status"
            )

        # Monthly/annual normalisation correctness.
        if freq in NORMALISABLE_OPEX_FREQUENCIES and _is_number(amount):
            expected_monthly = {"monthly": amount, "annual": amount / 12, "quarterly": amount / 3}[freq]
            expected_annual = {"monthly": amount * 12, "annual": amount, "quarterly": amount * 4}[freq]
            me = rec.get("monthly_equivalent")
            ae = rec.get("annual_equivalent")
            if _is_number(me) and abs(me - expected_monthly) > NUMERIC_TOLERANCE:
                f.error(
                    f"records[{i}] (id={rid!r}): monthly_equivalent={me} does not match "
                    f"amount={amount} at frequency={freq} (expected ~{expected_monthly:.2f})"
                )
            if _is_number(ae) and abs(ae - expected_annual) > NUMERIC_TOLERANCE:
                f.error(
                    f"records[{i}] (id={rid!r}): annual_equivalent={ae} does not match "
                    f"amount={amount} at frequency={freq} (expected ~{expected_annual:.2f})"
                )
        elif freq in NORMALISABLE_OPEX_FREQUENCIES and isinstance(amount, dict):
            me, ae = rec.get("monthly_equivalent"), rec.get("annual_equivalent")
            for key, val in amount.items():
                if not _is_number(val):
                    continue
                expected_monthly = {"monthly": val, "annual": val / 12, "quarterly": val / 3}[freq]
                expected_annual = {"monthly": val * 12, "annual": val, "quarterly": val * 4}[freq]
                if isinstance(me, dict) and key in me and _is_number(me[key]):
                    if abs(me[key] - expected_monthly) > NUMERIC_TOLERANCE:
                        f.error(
                            f"records[{i}] (id={rid!r}): monthly_equivalent.{key}={me[key]} does "
                            f"not match amount.{key}={val} at frequency={freq} "
                            f"(expected ~{expected_monthly:.2f})"
                        )
                if isinstance(ae, dict) and key in ae and _is_number(ae[key]):
                    if abs(ae[key] - expected_annual) > NUMERIC_TOLERANCE:
                        f.error(
                            f"records[{i}] (id={rid!r}): annual_equivalent.{key}={ae[key]} does "
                            f"not match amount.{key}={val} at frequency={freq} "
                            f"(expected ~{expected_annual:.2f})"
                        )


def _check_value_field_consistency(rec, i, list_key, f: Findings):
    """Shared status-vs-value + malformed-numeric-value check for startup_costs.yml
    and capex.yml, reused across all four list keys those files use."""
    rid = rec.get("id")
    status = rec.get("status")
    for field_name in STARTUP_CAPEX_VALUE_FIELDS:
        if field_name not in rec:
            continue
        val = rec[field_name]
        if not _is_valid_amount_shape(val):
            f.error(
                f"{list_key}[{i}] (id={rid!r}): '{field_name}' is a malformed numeric value "
                f"({val!r}) -- must be null, a number, or a dict of numbers"
            )
    # Only enforce status-vs-value consistency against the PRIMARY value field
    # for each list (total_cost for cost records) -- value_pct-only records
    # (e.g. contingency percentages) are checked on value_pct instead.
    primary_field = "value_pct" if "value_pct" in rec and "total_cost" not in rec else "total_cost"
    if primary_field not in rec:
        return
    val = rec[primary_field]
    if status == "PLACEHOLDER" and val is not None:
        f.error(
            f"{list_key}[{i}] (id={rid!r}): status=PLACEHOLDER but '{primary_field}' is "
            f"{val!r}, not null -- a PLACEHOLDER record must not assert a concrete value"
        )
    if status not in ("PLACEHOLDER", "SUPERSEDED") and val is None:
        f.error(
            f"{list_key}[{i}] (id={rid!r}): status={status} but '{primary_field}' is null -- "
            f"a non-PLACEHOLDER/SUPERSEDED record must have a real value backing its status"
        )


def check_startup_costs_schema(data, f: Findings):
    if data.get("dataset") != "startup_costs":
        return
    for list_key in RECORD_LIST_KEYS:
        items = data.get(list_key)
        if not isinstance(items, list):
            continue
        for i, rec in enumerate(items):
            if not isinstance(rec, dict):
                f.error(f"{list_key}[{i}]: not a mapping -- cannot check required fields")
                continue
            if list_key == "records":
                missing = STARTUP_COST_RECORD_REQUIRED_FIELDS - set(rec.keys())
                if missing:
                    f.error(
                        f"records[{i}] (id={rec.get('id')!r}): missing required "
                        f"startup_costs field(s): {sorted(missing)}"
                    )
            _check_value_field_consistency(rec, i, list_key, f)
            check_quantity_unit_cost_consistency(rec, i, list_key, f)


def check_capex_schema(data, f: Findings):
    if data.get("dataset") != "capex":
        return
    records = data.get("records", [])
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            f.error(f"records[{i}]: not a mapping -- cannot check required fields")
            continue
        rid = rec.get("id")
        missing = CAPEX_RECORD_REQUIRED_FIELDS - set(rec.keys())
        if missing:
            f.error(f"records[{i}] (id={rid!r}): missing required capex field(s): {sorted(missing)}")

        _check_value_field_consistency(rec, i, "records", f)
        check_quantity_unit_cost_consistency(rec, i, "records", f)

        # No invented depreciation assumptions.
        uly = rec.get("useful_life_years")
        dep = rec.get("depreciation_method")
        if uly is not None:
            if not _is_number(uly) or uly <= 0:
                f.error(f"records[{i}] (id={rid!r}): useful_life_years must be a positive number, got {uly!r}")
            if not rec.get("status_detail"):
                f.error(
                    f"records[{i}] (id={rid!r}): useful_life_years is set but no 'status_detail' "
                    f"explains its basis -- do not invent a useful life without a stated source"
                )
        if dep is not None:
            if not isinstance(dep, str) or not dep.strip():
                f.error(f"records[{i}] (id={rid!r}): depreciation_method must be a non-empty string, got {dep!r}")
            if not rec.get("status_detail"):
                f.error(
                    f"records[{i}] (id={rid!r}): depreciation_method is set but no 'status_detail' "
                    f"explains its basis -- do not invent a depreciation method without a stated source"
                )


def check_quantity_unit_cost_consistency(rec, i, list_key, f: Findings):
    """total_cost should be ~= quantity x unit_cost when all three are present
    and numeric (scalar or matching-key numeric dicts). Records missing any of
    the three are skipped -- very common in this dataset by design."""
    if not isinstance(rec, dict):
        return
    rid = rec.get("id")
    qty, uc, tc = rec.get("quantity"), rec.get("unit_cost"), rec.get("total_cost")
    if qty is None or uc is None or tc is None:
        return
    if not _is_number(qty):
        return  # qty malformed is already caught elsewhere if it's a value field; not one here

    def _check_pair(uc_val, tc_val, label=""):
        if not (_is_number(uc_val) and _is_number(tc_val)):
            return
        expected = qty * uc_val
        if expected == 0:
            return
        rel_diff = abs(tc_val - expected) / abs(expected)
        if rel_diff > QUANTITY_UNIT_COST_RELATIVE_TOLERANCE:
            f.error(
                f"{list_key}[{i}] (id={rid!r}): total_cost{label}={tc_val} does not match "
                f"quantity({qty}) x unit_cost{label}({uc_val})={expected:.2f} "
                f"(off by {rel_diff*100:.2f}%, tolerance {QUANTITY_UNIT_COST_RELATIVE_TOLERANCE*100:.1f}%)"
            )

    if _is_number(uc) and _is_number(tc):
        _check_pair(uc, tc)
    elif isinstance(uc, dict) and isinstance(tc, dict):
        for key in uc:
            if key in tc:
                _check_pair(uc[key], tc[key], label=f".{key}")


def load_valid_pricing_ids() -> set:
    """Load data/canonical/pricing.yml (if present) to build the set of valid
    pricing_ref ids. Mirrors load_valid_scenario_ids -- returns an empty set
    (no error raised here) if pricing.yml is missing or unparseable."""
    valid = set()
    pricing_path = CANON_DIR / "pricing.yml"
    if not pricing_path.exists():
        return valid
    try:
        pdata = yaml.safe_load(pricing_path.read_text(encoding="utf-8"))
    except yaml.YAMLError:
        return valid
    if not isinstance(pdata, dict):
        return valid
    for rec in pdata.get("records", []) or []:
        if isinstance(rec, dict) and rec.get("id"):
            valid.add(rec["id"])
    return valid


def check_services_schema(data, f: Findings):
    if data.get("dataset") != "services":
        return
    valid_pricing_ids = load_valid_pricing_ids()
    records = data.get("records", [])
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            f.error(f"records[{i}]: not a mapping -- cannot check required fields")
            continue
        rid = rec.get("id")

        missing = SERVICES_RECORD_REQUIRED_FIELDS - set(rec.keys())
        if missing:
            f.error(f"records[{i}] (id={rid!r}): missing required services field(s): {sorted(missing)}")

        lifecycle = rec.get("lifecycle")
        if lifecycle not in ALLOWED_SERVICE_LIFECYCLES:
            f.error(
                f"records[{i}] (id={rid!r}): lifecycle {lifecycle!r} is not one of "
                f"the known lifecycle states {sorted(ALLOWED_SERVICE_LIFECYCLES)}"
            )

        pricing_ref = rec.get("pricing_ref")
        if pricing_ref is not None and pricing_ref not in valid_pricing_ids:
            f.error(
                f"records[{i}] (id={rid!r}): pricing_ref {pricing_ref!r} does not exist in "
                f"data/canonical/pricing.yml's records -- malformed pricing reference"
            )

        status = rec.get("status")
        price = rec.get("price")
        price_range = rec.get("price_range")
        for field_name, val in (("price", price), ("price_range", price_range)):
            if val is not None and not (_is_number(val) if field_name == "price" else isinstance(val, str)):
                f.error(f"records[{i}] (id={rid!r}): '{field_name}' has an unexpected type ({val!r})")
        if status == "PLACEHOLDER" and (price is not None or price_range is not None):
            f.error(
                f"records[{i}] (id={rid!r}): status=PLACEHOLDER but price/price_range is set "
                f"-- a PLACEHOLDER record must not assert a concrete value"
            )
        if status not in ("PLACEHOLDER", "SUPERSEDED"):
            if price is None and price_range is None and pricing_ref is None:
                f.error(
                    f"records[{i}] (id={rid!r}): status={status} but none of price/price_range/"
                    f"pricing_ref is set -- a non-PLACEHOLDER/SUPERSEDED record needs a value or a reference"
                )


def _sum_pct_fields(value_dict):
    """Sum every key ending in '_pct' in a value dict -- used by the
    mix_complete: true check. Returns None if no such keys exist."""
    pct_vals = [v for k, v in value_dict.items() if k.endswith("_pct") and _is_number(v)]
    if not pct_vals:
        return None
    return sum(pct_vals)


def check_revenue_assumptions_schema(data, f: Findings):
    if data.get("dataset") != "revenue_assumptions":
        return
    valid_service_ids = load_valid_service_ids()
    valid_pricing_ids = load_valid_pricing_ids()
    records = data.get("records", [])
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            f.error(f"records[{i}]: not a mapping -- cannot check required fields")
            continue
        rid = rec.get("id")

        missing = REVENUE_ASSUMPTIONS_RECORD_REQUIRED_FIELDS - set(rec.keys())
        if missing:
            f.error(f"records[{i}] (id={rid!r}): missing required revenue_assumptions field(s): {sorted(missing)}")

        service_ref = rec.get("service_ref")
        if service_ref is not None and service_ref not in valid_service_ids:
            f.error(
                f"records[{i}] (id={rid!r}): service_ref {service_ref!r} does not exist in "
                f"data/canonical/services.yml's records -- malformed service reference"
            )
        pricing_ref = rec.get("pricing_ref")
        if pricing_ref is not None and pricing_ref not in valid_pricing_ids:
            f.error(
                f"records[{i}] (id={rid!r}): pricing_ref {pricing_ref!r} does not exist in "
                f"data/canonical/pricing.yml's records -- malformed pricing reference"
            )

        freq = rec.get("frequency")
        if freq is not None and freq not in ALLOWED_OPEX_FREQUENCIES:
            f.error(
                f"records[{i}] (id={rid!r}): frequency {freq!r} is not one of "
                f"the known frequencies {sorted(ALLOWED_OPEX_FREQUENCIES)}"
            )

        value = rec.get("value")
        if not _is_valid_amount_shape(value):
            f.error(f"records[{i}] (id={rid!r}): 'value' is a malformed numeric value ({value!r})")

        # Percentage range check (0-100), when unit == "%".
        if rec.get("unit") == "%":
            check_vals = []
            if _is_number(value):
                check_vals = [value]
            elif isinstance(value, dict):
                check_vals = [v for v in value.values() if _is_number(v)]
            for v in check_vals:
                if not (0 <= v <= 100):
                    f.error(f"records[{i}] (id={rid!r}): percentage value {v} is outside the valid 0-100 range")

        # Status-vs-value consistency, generalised: value OR service_ref OR
        # pricing_ref OR a real description satisfies "needs something".
        status = rec.get("status")
        has_something = (
            value is not None or service_ref is not None or pricing_ref is not None
            or bool(rec.get("description"))
        )
        if status == "PLACEHOLDER" and value is not None:
            f.error(f"records[{i}] (id={rid!r}): status=PLACEHOLDER but 'value' is {value!r}, not null")
        if status not in ("PLACEHOLDER", "SUPERSEDED") and not has_something:
            f.error(
                f"records[{i}] (id={rid!r}): status={status} but none of value/service_ref/"
                f"pricing_ref/description is set -- nothing is actually asserted"
            )

        # mix_complete: true -> the record's own *_pct value-dict keys must sum to 100.
        if rec.get("mix_complete") is True and isinstance(value, dict):
            total = _sum_pct_fields(value)
            if total is not None and abs(total - 100) > 0.5:
                f.error(
                    f"records[{i}] (id={rid!r}): mix_complete=true but *_pct fields in 'value' "
                    f"sum to {total}, not 100"
                )


def check_revenue_ramp_schema(data, f: Findings):
    if data.get("dataset") != "revenue_ramp":
        return
    records = data.get("records", [])
    seen_scenario_months = {}
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            f.error(f"records[{i}]: not a mapping -- cannot check required fields")
            continue
        rid = rec.get("id")

        missing = REVENUE_RAMP_RECORD_REQUIRED_FIELDS - set(rec.keys())
        if missing:
            f.error(f"records[{i}] (id={rid!r}): missing required revenue_ramp field(s): {sorted(missing)}")

        month = rec.get("month")
        if month is not None and month not in ALLOWED_RAMP_MONTHS:
            f.error(
                f"records[{i}] (id={rid!r}): month {month!r} is not one of "
                f"the known ramp months {sorted(ALLOWED_RAMP_MONTHS)}"
            )

        scenario_id = rec.get("scenario_id")
        if scenario_id is not None and month is not None:
            key = (scenario_id, month)
            if key in seen_scenario_months:
                f.error(
                    f"records[{i}] (id={rid!r}): duplicate (scenario_id, month) pair {key} -- "
                    f"already used by {seen_scenario_months[key]!r}"
                )
            else:
                seen_scenario_months[key] = rid

        for vf in REVENUE_RAMP_VALUE_FIELDS:
            if vf in rec and not _is_valid_amount_shape(rec[vf]):
                f.error(f"records[{i}] (id={rid!r}): '{vf}' is a malformed numeric value ({rec[vf]!r})")

        # am_revenue + pm_revenue + ancillary_revenue must sum to total_revenue.
        am_rev, pm_rev, anc_rev, total_rev = (
            rec.get("am_revenue"), rec.get("pm_revenue"), rec.get("ancillary_revenue"), rec.get("total_revenue"),
        )
        if all(_is_number(v) for v in (am_rev, pm_rev, anc_rev, total_rev)):
            expected_total = am_rev + pm_rev + anc_rev
            if abs(expected_total - total_rev) > REVENUE_RAMP_TOLERANCE:
                f.error(
                    f"records[{i}] (id={rid!r}): am_revenue + pm_revenue + ancillary_revenue = "
                    f"{expected_total:.2f}, does not match total_revenue {total_rev:.2f}"
                )

        # total_revenue / steady_state_revenue x 100 must match pct_of_steady_state.
        steady_state = rec.get("steady_state_revenue")
        pct = rec.get("pct_of_steady_state")
        if _is_number(total_rev) and _is_number(steady_state) and _is_number(pct) and steady_state:
            expected_pct = total_rev / steady_state * 100
            if abs(expected_pct - pct) > 0.1:
                f.error(
                    f"records[{i}] (id={rid!r}): total_revenue/steady_state_revenue x 100 = "
                    f"{expected_pct:.2f}%, does not match pct_of_steady_state {pct}"
                )

        # PM revenue at 100% (Month 5+) must not exceed the canonical PM steady-state capacity's
        # own revenue value -- i.e. the ramp cannot silently invent PM capacity beyond
        # pm_steady_state_capacity + rev_pm_saturday_sessions's own combined revenue ceiling.
        if month == "M5plus" and _is_number(pm_rev):
            pm_capacity_ceiling = _load_pm_capacity_revenue_ceiling()
            if pm_capacity_ceiling is not None and pm_rev - pm_capacity_ceiling > REVENUE_RAMP_TOLERANCE:
                f.error(
                    f"records[{i}] (id={rid!r}): pm_revenue {pm_rev:.2f} at M5plus (100%) exceeds "
                    f"the canonical PM capacity revenue ceiling {pm_capacity_ceiling:.2f} -- PM "
                    f"session volume cannot silently exceed pm_steady_state_capacity + "
                    f"rev_pm_saturday_sessions"
                )

        status = rec.get("status")
        has_something = total_rev is not None or bool(rec.get("am_utilisation_assumption")) or bool(rec.get("pm_utilisation_assumption"))
        if status == "PLACEHOLDER" and total_rev is not None:
            f.error(f"records[{i}] (id={rid!r}): status=PLACEHOLDER but 'total_revenue' is {total_rev!r}, not null")
        if status not in ("PLACEHOLDER", "SUPERSEDED") and not has_something:
            f.error(
                f"records[{i}] (id={rid!r}): status={status} but nothing is actually asserted "
                f"(no total_revenue, am_utilisation_assumption, or pm_utilisation_assumption)"
            )


_PM_CAPACITY_REVENUE_CEILING_CACHE = None


def _load_pm_capacity_revenue_ceiling():
    """PM Weekday capacity (client_assumptions.yml#pm_steady_state_capacity) x
    pricing.yml#pm_alacarte_average x operating_days_per_month_weekday, plus PM
    Saturday capacity (revenue_assumptions.yml#rev_pm_saturday_sessions) x the
    same price x operating_saturdays_per_month -- the canonical PM revenue
    ceiling a ramp's M5plus PM revenue must not exceed. Returns None (skip the
    check) if any required canonical file/record is missing, rather than
    erroring on an unrelated file's absence."""
    global _PM_CAPACITY_REVENUE_CEILING_CACHE
    if _PM_CAPACITY_REVENUE_CEILING_CACHE is not None:
        return _PM_CAPACITY_REVENUE_CEILING_CACHE
    try:
        client_assumptions = yaml.safe_load((CANON_DIR / "client_assumptions.yml").read_text(encoding="utf-8"))
        pricing = yaml.safe_load((CANON_DIR / "pricing.yml").read_text(encoding="utf-8"))
        revenue_assumptions = yaml.safe_load((CANON_DIR / "revenue_assumptions.yml").read_text(encoding="utf-8"))
        universal = {r["id"]: r for r in client_assumptions.get("universal", []) if isinstance(r, dict) and r.get("id")}
        pricing_by_id = {r["id"]: r for r in pricing.get("records", []) if isinstance(r, dict) and r.get("id")}
        rev_by_id = {r["id"]: r for r in revenue_assumptions.get("records", []) if isinstance(r, dict) and r.get("id")}
        pm_weekday_sessions = universal["pm_steady_state_capacity"]["value"]
        operating_days_weekday = universal["operating_days_per_month_weekday"]["value"]
        operating_saturdays = universal["operating_saturdays_per_month"]["value"]
        pm_price = pricing_by_id["pm_alacarte_average"]["price"]
        pm_saturday_sessions = rev_by_id["rev_pm_saturday_sessions"]["value"]
        ceiling = (
            pm_weekday_sessions * pm_price * operating_days_weekday
            + pm_saturday_sessions * pm_price * operating_saturdays
        )
        _PM_CAPACITY_REVENUE_CEILING_CACHE = ceiling
        return ceiling
    except (OSError, yaml.YAMLError, KeyError, TypeError):
        return None


def check_cost_ramp_schema(data, f: Findings):
    if data.get("dataset") != "cost_ramp":
        return
    records = data.get("records", [])
    seen_scenario_months = {}
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            f.error(f"records[{i}]: not a mapping -- cannot check required fields")
            continue
        rid = rec.get("id")

        missing = COST_RAMP_RECORD_REQUIRED_FIELDS - set(rec.keys())
        if missing:
            f.error(f"records[{i}] (id={rid!r}): missing required cost_ramp field(s): {sorted(missing)}")

        month = rec.get("month")
        if month is not None and month not in ALLOWED_RAMP_MONTHS:
            f.error(
                f"records[{i}] (id={rid!r}): month {month!r} is not one of "
                f"the known ramp months {sorted(ALLOWED_RAMP_MONTHS)}"
            )

        scenario_id = rec.get("scenario_id")
        if scenario_id is not None and month is not None:
            key = (scenario_id, month)
            if key in seen_scenario_months:
                f.error(
                    f"records[{i}] (id={rid!r}): duplicate (scenario_id, month) pair {key} -- "
                    f"already used by {seen_scenario_months[key]!r}"
                )
            else:
                seen_scenario_months[key] = rid

        for vf in COST_RAMP_VALUE_FIELDS:
            if vf in rec and not _is_valid_amount_shape(rec[vf]):
                f.error(f"records[{i}] (id={rid!r}): '{vf}' is a malformed numeric value ({rec[vf]!r})")

        # fixed_costs + variable_costs + payroll_costs must sum to total_operating_costs.
        fixed, variable, payroll, total = (
            rec.get("fixed_costs"), rec.get("variable_costs"), rec.get("payroll_costs"), rec.get("total_operating_costs"),
        )
        if all(_is_number(v) for v in (fixed, variable, payroll, total)):
            expected_total = fixed + variable + payroll
            if abs(expected_total - total) > COST_RAMP_TOLERANCE:
                f.error(
                    f"records[{i}] (id={rid!r}): fixed_costs + variable_costs + payroll_costs = "
                    f"{expected_total:.2f}, does not match total_operating_costs {total:.2f}"
                )

        # payroll_breakdown, when present, must itself be internally consistent:
        # its 6 core components sum to direct_labor_and_opening_total, and
        # direct_labor_and_opening_total + workers_comp + superannuation (added
        # Phase 9 resume, 2026-08-09 -- defaults to 0 if absent, for
        # backward compatibility with any record predating this field) sums to
        # this record's own payroll_costs (a real cross-check that
        # STARTUP/CAPEX values cannot silently be smuggled into recurring
        # payroll -- every field here is a genuine recurring labor cost, by
        # construction).
        breakdown = rec.get("payroll_breakdown")
        if isinstance(breakdown, dict):
            component_fields = (
                "am_weekday_direct_labor", "am_saturday_direct_labor", "pm_weekday_direct_labor",
                "pm_saturday_direct_labor", "opening_time_increment", "receptionist_relief",
            )
            components = [breakdown.get(cf) for cf in component_fields]
            direct_labor_total = breakdown.get("direct_labor_and_opening_total")
            workers_comp = breakdown.get("workers_comp")
            superannuation = breakdown.get("superannuation", 0)
            if all(_is_number(c) for c in components) and _is_number(direct_labor_total):
                expected_dl = sum(components)
                if abs(expected_dl - direct_labor_total) > COST_RAMP_TOLERANCE:
                    f.error(
                        f"records[{i}] (id={rid!r}): payroll_breakdown's 6 components sum to "
                        f"{expected_dl:.2f}, does not match direct_labor_and_opening_total {direct_labor_total:.2f}"
                    )
            if _is_number(direct_labor_total) and _is_number(workers_comp) and _is_number(superannuation) and _is_number(payroll):
                expected_payroll = direct_labor_total + workers_comp + superannuation
                if abs(expected_payroll - payroll) > COST_RAMP_TOLERANCE:
                    f.error(
                        f"records[{i}] (id={rid!r}): payroll_breakdown's direct_labor_and_opening_total + "
                        f"workers_comp + superannuation = {expected_payroll:.2f}, does not match this record's own "
                        f"payroll_costs {payroll:.2f}"
                    )
            # am_weekday_treatment_staff + am_weekday_phlebotomist, where present, must sum to am_weekday_direct_labor.
            treatment = breakdown.get("am_weekday_treatment_staff")
            phlebotomist = breakdown.get("am_weekday_phlebotomist")
            am_weekday = breakdown.get("am_weekday_direct_labor")
            if _is_number(treatment) and _is_number(phlebotomist) and _is_number(am_weekday):
                if abs((treatment + phlebotomist) - am_weekday) > COST_RAMP_TOLERANCE:
                    f.error(
                        f"records[{i}] (id={rid!r}): am_weekday_treatment_staff + am_weekday_phlebotomist = "
                        f"{treatment + phlebotomist:.2f}, does not match am_weekday_direct_labor {am_weekday:.2f}"
                    )

        status = rec.get("status")
        has_something = total is not None or bool(rec.get("ramp_behaviour")) or bool(rec.get("calculation_basis"))
        if status == "PLACEHOLDER" and total is not None:
            f.error(f"records[{i}] (id={rid!r}): status=PLACEHOLDER but 'total_operating_costs' is {total!r}, not null")
        if status not in ("PLACEHOLDER", "SUPERSEDED") and not has_something:
            f.error(
                f"records[{i}] (id={rid!r}): status={status} but nothing is actually asserted "
                f"(no total_operating_costs, ramp_behaviour, or calculation_basis)"
            )


def load_valid_service_ids() -> set:
    """Load data/canonical/services.yml (if present) to build the set of
    valid service_ref ids. Mirrors load_valid_pricing_ids."""
    valid = set()
    services_path = CANON_DIR / "services.yml"
    if not services_path.exists():
        return valid
    try:
        sdata = yaml.safe_load(services_path.read_text(encoding="utf-8"))
    except yaml.YAMLError:
        return valid
    if not isinstance(sdata, dict):
        return valid
    for rec in sdata.get("records", []) or []:
        if isinstance(rec, dict) and rec.get("id"):
            valid.add(rec["id"])
    return valid


def load_valid_scenario_ids() -> set:
    """Load data/canonical/scenarios.yml (if present) to build the set of valid
    scenario ids ('universal' plus every id in records/historical_scenarios).
    Returns an empty set (with no error raised here) if scenarios.yml is
    missing or unparseable -- the caller decides how to react."""
    valid = {"universal"}
    scenarios_path = CANON_DIR / "scenarios.yml"
    if not scenarios_path.exists():
        return valid
    try:
        sdata = yaml.safe_load(scenarios_path.read_text(encoding="utf-8"))
    except yaml.YAMLError:
        return valid
    if not isinstance(sdata, dict):
        return valid
    for list_key in ("records", "historical_scenarios"):
        for rec in sdata.get(list_key, []) or []:
            if isinstance(rec, dict) and rec.get("id"):
                valid.add(rec["id"])
    return valid


def find_scenario_ref_fields(node, path="root"):
    """Yield (path, field_name, value) for every SCENARIO_REF_FIELDS key found anywhere."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in SCENARIO_REF_FIELDS:
                yield path, k, v
            yield from find_scenario_ref_fields(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from find_scenario_ref_fields(item, f"{path}[{i}]")


def check_scenario_references(data, f: Findings, valid_scenario_ids: set):
    for path, field_name, value in find_scenario_ref_fields(data):
        values = value if isinstance(value, list) else [value]
        for v in values:
            if v not in valid_scenario_ids:
                f.error(
                    f"{path}.{field_name}: references unknown scenario id {v!r} -- "
                    f"must be 'universal' or an id defined in data/canonical/scenarios.yml "
                    f"(known ids: {sorted(valid_scenario_ids)})"
                )


def validate_file(path: Path):
    """Returns (Findings, parsed_data_or_None)."""
    try:
        display_name = str(path.relative_to(REPO_ROOT))
    except ValueError:
        display_name = str(path)
    f = Findings(display_name)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        f.error(f"Could not read file: {e}")
        return f, None
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as e:
        f.error(f"YAML parse error: {e}")
        return f, None
    if data is None:
        f.error("File parsed to empty/None content.")
        return f, None

    check_structure(data, f)
    if f.ok or True:  # continue running remaining checks even if structure check found issues, to surface everything at once
        check_statuses(data, f)
        check_sources(data, f)
        check_duplicate_ids(data, f)
        check_conflicting_values(data, f)
        check_scenario_registry_invariant(data, f)
        check_staffing_schema(data, f)
        check_wages_schema(data, f)
        check_opex_schema(data, f)
        check_startup_costs_schema(data, f)
        check_capex_schema(data, f)
        check_services_schema(data, f)
        check_revenue_assumptions_schema(data, f)
        check_revenue_ramp_schema(data, f)
        check_cost_ramp_schema(data, f)
        check_scenario_references(data, f, load_valid_scenario_ids())

    return f, data


def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    if argv:
        targets = [Path(a) if Path(a).is_absolute() else REPO_ROOT / a for a in argv]
    else:
        if not CANON_DIR.exists():
            print(f"ERROR: {CANON_DIR} not found.")
            return 2
        targets = sorted(CANON_DIR.glob("*.yml"))
        # Phase 9 -- also validate data/models/*.yml (Layer 3, MODEL-ARCHITECTURE.md) with
        # the same generic status/source/structure/scenario-reference checks. Model-layer
        # files are a genuinely different shape from canonical-layer files (nested
        # outputs/assumptions rather than a flat records list), so the dataset-specific
        # schema checks (§8-26 above) do NOT run against them -- only the checks that walk
        # the tree generically regardless of top-level structure (check_statuses,
        # check_sources, check_scenario_references) apply.
        if MODELS_DIR.exists():
            targets += sorted(MODELS_DIR.glob("*.yml"))

    if not targets:
        print("No files to validate.")
        return 2

    all_ok = True
    total_errors = 0
    total_warnings = 0
    all_findings = []

    # Global (cross-file) duplicate-id tracking -- a records[*].id should not
    # collide across different canonical files either, not just within one.
    global_id_seen = {}  # id -> filename it was first seen in

    for path in targets:
        if not path.exists():
            print(f"\n{path}: FILE NOT FOUND")
            all_ok = False
            continue
        findings, data = validate_file(path)

        if isinstance(data, dict):
            for rec in data.get("records", []) or []:
                if not isinstance(rec, dict) or not rec.get("id"):
                    continue
                rid = rec["id"]
                if rid in global_id_seen and global_id_seen[rid] != findings.filename:
                    findings.error(
                        f"records[*].id {rid!r} also appears in {global_id_seen[rid]} -- "
                        f"canonical record ids must be globally unique across data/canonical/*.yml"
                    )
                else:
                    global_id_seen.setdefault(rid, findings.filename)

        all_findings.append(findings)
        status = "PASS" if findings.ok else "FAIL"
        print(f"\n{findings.filename}: {status}")
        for e in findings.errors:
            print(f"  ERROR: {e}")
        for w in findings.warnings:
            print(f"  WARN:  {w}")
        if not findings.ok:
            all_ok = False
        total_errors += len(findings.errors)
        total_warnings += len(findings.warnings)

    print("\n" + "=" * 72)
    print(
        f"validate_canonical_data: {len(targets)} file(s) checked, "
        f"{total_errors} error(s), {total_warnings} warning(s)."
    )
    if all_ok:
        print("All checks passed.")
        return 0
    else:
        print("One or more checks FAILED -- see ERROR lines above.")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
