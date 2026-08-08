"""
GTT Center Perth -- Canonical data validator (proof of concept).

Validates data/canonical/*.yml files against the schema/governance conventions
established in docs/architecture/CANONICAL-DATA-SCHEMA.md and
docs/architecture/DATA-GOVERNANCE.md. This is a proof-of-concept validator for
five files (pricing.yml, client_assumptions.yml, scenarios.yml, staffing.yml,
wages.yml, added Phase 2) -- it is not a general schema engine and does not
validate every field type strictly.

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

ALLOWED_STATUSES = {
    "VERIFIED", "DECIDED", "CALCULATED", "MODELLED", "SCENARIO",
    "PLACEHOLDER", "SUPERSEDED",
}

REQUIRED_TOP_KEYS = {"schema_version", "dataset"}
RECORD_LIST_KEYS = {
    "records", "universal", "scenario_dependent", "historical_scenarios",
    "operational_buffers", "open_items", "historical_staffing_scenarios",
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
SCENARIO_REF_FIELDS = {"staffing_scenario", "scenario_id"}

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
