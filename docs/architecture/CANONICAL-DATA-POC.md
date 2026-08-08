# GTT Center Perth — Canonical Data Proof of Concept

**Purpose:** document the first real implementation slice of the architecture designed in `docs/architecture/` — SOURCE DOCUMENTS → CANONICAL YAML → VALIDATOR, for exactly three domains (pricing, client assumptions, scenarios), nothing more. This is a proof of concept: it proves the pattern works end-to-end on a bounded slice, not a completed migration.

**Scope of this phase, explicitly:** `data/canonical/pricing.yml`, `data/canonical/client_assumptions.yml`, `data/canonical/scenarios.yml`, `tools/validate_canonical_data.py`, plus corrections to `README.md` and four nav/meta docs (`docs/reading-order.md`, `docs/00_document_inventory.md`, `docs/01_conflicts_log.md`, `docs/HANDOFF.md`). **Not built this phase:** the Master Financial Model, the Master Operations Model, any XLSX/PDF/DOCX generation, the remaining ~130 markdown files' migration, and — deliberately — a resolution of Table 1 vs. Table 2 as primary.

---

## 1. What Canonical Data Exists, and Where

```
data/canonical/
├── pricing.yml              AM/PM headline pricing + a representative slice of individual services
├── client_assumptions.yml   universal + scenario-dependent operational assumptions
└── scenarios.yml            Table 1 and Table 2, both explicit, neither marked primary
```

All three files live under `data/canonical/` — the first real content in the `data/` layer proposed in `docs/architecture/TARGET-ARCHITECTURE.md` Layer 2. `docs/CURRENT-STATE.md` remains the authoritative human-readable canonical file; these three YAML files are a machine-readable **subset** of it, not a replacement, and not (yet) auto-generated from it or vice versa — a human (this session) transcribed values from `CURRENT-STATE.md` and its cited sources into YAML, checking each one against the source rather than re-deriving anything.

---

## 2. How Each Dataset Is Sourced

Every record in every file carries a `source: {file, section}` reference (per the coordinator's Part 5 instruction) pointing at a real file and a real section heading/table name in this repo — never a fabricated line number. Two sourcing patterns are used:

- **Direct citation** — the value is transcribed from a named document, tagged `source.file`/`source.section`. Used for the large majority of records.
- **Derived citation** — the value is computed from *other canonical records*, not re-derived from a document. These carry `status: CALCULATED` and a `derived_from: [record_id, ...]` list naming the canonical records it comes from, per Part 5's explicit instruction ("If a value is derived from another canonical value, say so explicitly instead of re-citing a doc"). Example: `scenario_table_1.total_staffing` is `derived_from: [treatment_staffing, phlebotomy_staffing]`, both of which live in the same file.

**No fake precision was added.** Where a source document itself only states something qualitatively (e.g. `CURRENT-STATE.md`'s "well inside the shift window," not an exact minute count), the canonical record mirrors that qualitative statement rather than inventing a number — see `client_assumptions.yml`'s `shift_window_buffer` record.

---

## 3. How Statuses Work

The 7-status vocabulary from `docs/architecture/DATA-GOVERNANCE.md` is used throughout: `VERIFIED`, `DECIDED`, `CALCULATED`, `MODELLED`, `SCENARIO`, `PLACEHOLDER`, `SUPERSEDED`. A few concrete examples from the populated data, chosen to show the distinction actually doing work rather than being cosmetic:

| Status | Example record | Why this status, not another |
|---|---|---|
| `VERIFIED` | `client_assumptions.yml` → `wdp_start_time_guidance` | Confirmed directly by Carole Rivers (WDP), by email, with a real date |
| `DECIDED` | `pricing.yml` → `am_price_increase_policy` | Anthony's choice (no increase until 12+ months), not a calculation or external fact |
| `CALCULATED` | `scenarios.yml` → `scenario_table_1.total_staffing` | Plain arithmetic (8 + 2 = 10) from two other canonical fields, no named assumption |
| `MODELLED` | `scenarios.yml` → `scenario_table_1.monthly_financial_result` | A delta-reconciliation build with a named, disclosed methodology, not a hard external confirmation |
| `SCENARIO` | *(not used at the record-level status field in this pass — see note below)* | See §6 |
| `PLACEHOLDER` | `pricing.yml` → `pm_package_duo` | Anthony has not signed off a final price; two proposed options are recorded, neither is guessed as final |
| `SUPERSEDED` | `scenarios.yml` → `historical_scenarios[*]` | The 14-client ceiling and the old 12-client/23-min model, retained for trace, never fed into a live calculation |

**Note on `SCENARIO` not appearing as a record-level status in this pass:** per `docs/architecture/DATA-GOVERNANCE.md` §3, `SCENARIO` means "a labelled what-if, explicitly not adopted as the committed baseline." Both Table 1 and Table 2 are live, real candidates for the committed baseline (the question is *which one*, not whether either is a discarded alternative) — so neither was tagged `SCENARIO` at the top level; each is tagged `MODELLED` (reflecting the least-certain field, the financial result) with `is_primary: false` doing the work of "not yet adopted," rather than overloading the `status` field to also carry that meaning. This is a judgment call made explicit here rather than silently — a reasonable alternative reading would tag both `SCENARIO` until item 1m resolves; flagged for Anthony/a future session to weigh in on if it matters for downstream tooling.

---

## 4. How Scenarios Work

`data/canonical/scenarios.yml` represents Table 1 (18 clients/day) and Table 2 (12 clients/day) as fully parallel records — same field set, same level of sourcing detail, same status rigor. **Both carry `is_primary: false`**, per the coordinator's explicit instruction, and each record's `is_primary_note` field explains *why* — notably, that this is a **more conservative stance than `docs/CURRENT-STATE.md`'s own prose**, which does describe Table 1 as "PRIMARY committed daily model" (while itself flagging that adoption as an unconfirmed framing choice, item 1m). This file does not silently match `CURRENT-STATE.md`'s prose framing, and does not silently override it either — it states the discrepancy directly (§2's `is_primary_note` fields) so a reader hits it immediately, not after digging.

`client_assumptions.yml` links to these scenario records by `scenario_id` (in its `scenario_dependent` list) rather than restating client volume, start time, or headcount independently — the single-source-of-truth rule applies within the canonical layer itself, not just between the canonical layer and documents.

**Historical scenarios** (the 14-client ceiling, the old 12-client/23-minute model, the original 10-client model) are recorded in a separate `historical_scenarios` list, minimally populated (id, status, `superseded_by`, source pointer, one-line note) rather than fully re-transcribed — the full detail remains in `docs/CURRENT-STATE.md`'s own historical sections, which this file points to rather than duplicates.

---

## 5. How Validation Works

`tools/validate_canonical_data.py` runs 7 checks (full detail in its own docstring):

1. YAML validity
2. Expected top-level structure (required keys present)
3. Only the 7 permitted statuses used, anywhere in the file (recursive scan)
4. Every non-`PLACEHOLDER` value has a `source` reference
5. Duplicate ID detection (with a documented exception for `client_assumptions.yml`'s `scenario_dependent` list, which intentionally repeats an `id` once per `scenario_id`)
6. Conflicting-value detection (two non-superseded records sharing a name/category but a different price)
7. Scenario-registry invariant — both `scenario_table_1` and `scenario_table_2` must exist in `scenarios.yml`, and **both must have `is_primary: false`** (a phase-specific rule, not a permanent one — revisit the day Anthony resolves item 1m)

**This validator was sanity-checked against deliberately broken test data before being trusted** (not committed to the repo — run from the session scratchpad and discarded): it correctly caught an invalid status, two missing-source violations, a duplicate ID, a conflicting price pair, and a `scenarios.yml` missing `scenario_table_2`. This is disclosed because a validator that only ever reports "0 findings" against real data is not, by itself, proof that it works — see §8 below for a related caution about `tools/check_consistency.py`.

### How to Run It

```bash
python tools/validate_canonical_data.py
# or, to check specific files:
python tools/validate_canonical_data.py data/canonical/pricing.yml
```

No arguments = validates every `data/canonical/*.yml` file found. Exit code 0 = all pass, 1 = at least one failure (same convention as `tools/check_consistency.py`).

### Actual Result (this session, 2026-08-08)

```
data\canonical\pricing.yml: PASS

data\canonical\client_assumptions.yml: PASS

data\canonical\scenarios.yml: PASS

========================================================================
validate_canonical_data: 3 file(s) checked, 0 error(s), 0 warning(s).
All checks passed.
```

---

## 6. Known Unresolved Conflicts / Open Items

**No genuine cross-source price or figure disagreement was found** during this pass — `docs/CURRENT-STATE.md`, `docs/services-pricing-locked.md`, and `docs/pm-package-structure.md` all agree on every figure transcribed into `pricing.yml`. `conflicts: []` in all three files reflects a real check, not an unchecked assumption — see §2 and each file's own header comment for what was cross-referenced.

What *is* recorded as genuinely open (not a data-entry conflict, but a real unresolved question):

- **`docs/VERIFICATION-TRACKER.md` item 1m** — Table 1 vs. Table 2 as the committed daily target. Represented in `scenarios.yml`'s `open_items` list. This proof of concept deliberately does not resolve it.
- **`docs/VERIFICATION-TRACKER.md` item 1o** — whether Table 2's 08:00 start still incurs the 07:00-sourced "opening-time increment." Represented the same way.
- **PM package final pricing** — `pm_package_duo`/`refresh`/`glow` in `pricing.yml`, each `PLACEHOLDER` with both proposed discount tiers (10%/15%) recorded, neither picked.
- **Saturday client volume for Table 1/Table 2** — `client_assumptions.yml`'s `saturday_volume_assumption` record is explicitly flagged as an *inference* (not a directly-quoted `CURRENT-STATE.md` figure) — see that record's `status_detail` for the exact reasoning chain and why it's `MODELLED` rather than `VERIFIED`.
- **AM Package 1/2 booking mix** — `service_mix_am_package_split` is `PLACEHOLDER`, `value: null` — genuinely no data exists (pre-launch venture), not estimated.

---

## 7. Values That Could Not Safely Be Migrated (and Why)

- **The full a-la-carte service menu** (`docs/services-pricing-locked.md` Part A add-ons, all of Part B afternoon-only services, Part D cafe, Part E retail) — only a representative 7-item slice of Part A's base services was migrated into `pricing.yml`, to demonstrate the schema handles individual services alongside packages without committing to transcribing ~50+ rows (and the transcription-error risk that implies) in a single POC pass. Flagged as the clearest next-migration candidate (§9).
- **Exact Saturday client-volume figures for Table 1/Table 2** — not directly stated as a number anywhere in `docs/CURRENT-STATE.md`'s Table 1/2 structure (only inferable from a labor-scaling ratio) — recorded as an inference with full reasoning shown, not silently treated as equally certain to the directly-quoted weekday figures.
- **Phlebotomist employment model cost impact** — `docs/VERIFICATION-TRACKER.md` item 1d (in-house vs. WDP-supplied) is a live, unresolved dependency that could materially change `pricing.yml`/`client_assumptions.yml`'s payroll-adjacent figures if resolved — not migrated at all this pass (payroll/wages domains are explicitly out of scope, see §9), flagged here only because it's the kind of change that would ripple into scenario financial results once that domain is built.
- **PM package "final" price** — genuinely does not exist yet (Anthony has not signed off); recording a single number would have violated the explicit "don't invent prices" instruction, so both proposed tiers are shown instead.

---

## 8. A Note on `tools/check_consistency.py` (relevant to trusting "0 findings")

While preparing this proof of concept, a real bug was found in the existing `tools/check_consistency.py`'s staleness-marker detection: its `STALENESS_MARKERS` regex includes the bare substring `prior` (intended to catch the word "prior"/"previously") with no word boundary, so it also matches inside unrelated words like **"priority"** — e.g. "Pathology partner (WDP, **priority** 1) has been emailed" in `docs/reading-order.md` was enough to suppress a genuine, otherwise-unflagged stale figure (`10 GTT clients/day`) sitting three lines later, purely because "priority" happened to be within the script's 3-line lookback window. This was confirmed by directly invoking the script's own `scan_file()`/`has_marker()` functions against the real file content, not inferred.

**This means `tools/check_consistency.py` returning "0 findings" is not, by itself, proof that a document is fully current** — it is a real, useful check, but has at least one confirmed false-negative pattern. Part 1's corrections in this session were made by manual review (cross-referencing every nav/meta doc's stated model against `docs/CURRENT-STATE.md` directly), not by trusting the checker's clean report. **This bug was not fixed this phase** — fixing `tools/check_consistency.py` was not in this phase's authorised scope (only `README.md` and the four nav/meta docs could be modified; "everything else stays additive/new files only"). Flagged here explicitly so it isn't lost, and is a natural candidate for a small, standalone fix in a future session (change `prior` to `\bprior\b` or similar).

---

## 9. Recommended Next Migration Domain

**`data/canonical/staffing.yml` and `data/canonical/wages.yml`**, in that order, for two reasons:

1. They are the most direct dependency of the Financial Model's payroll module and the Operations Model's roster-requirement module (`docs/architecture/MODEL-ARCHITECTURE.md` §4's "cross-model dependency rule") — building them next means the next domain migrated is also the next one that unblocks real model-building, not just more inert data.
2. They have a real, disclosed, previously-actually-occurring bug to validate against: `docs/VERIFICATION-TRACKER.md` item 1i (the Saturday PM 3-hour-minimum casual engagement rule being under-applied, then corrected) is exactly the kind of error a `staffing.yml`/`wages.yml` pair with a payroll-calculation validator (extending `tools/validate_canonical_data.py` per `docs/architecture/VALIDATION-ARCHITECTURE.md` §2.1's "3-hour casual minimum check") would catch automatically going forward.

`services.yml` (the full a-la-carte catalog deferred in §7) is the next-best alternative if a lower-risk, non-financial domain is preferred first.

---

## 10. What This Document Does Not Do

It does not build the Master Financial Model, Master Operations Model, any document generator, or any output format. It does not migrate `staffing.yml`, `wages.yml`, `payroll_costs.yml`, `opex.yml`, `startup_costs.yml`, or any other domain from `docs/architecture/CANONICAL-DATA-SCHEMA.md`'s original 20-domain sketch. It does not resolve Table 1 vs. Table 2. It does not fix `tools/check_consistency.py`'s disclosed bug (§8).
