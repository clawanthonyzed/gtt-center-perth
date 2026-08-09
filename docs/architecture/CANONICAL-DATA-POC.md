# GTT Center Perth — Canonical Data Proof of Concept

**Purpose:** document the first real implementation slice of the architecture designed in `docs/architecture/` — SOURCE DOCUMENTS → CANONICAL YAML → VALIDATOR. This is a proof of concept: it proves the pattern works end-to-end on a bounded slice, not a completed migration.

**Phase 1 scope (2026-08-08):** `data/canonical/pricing.yml`, `data/canonical/client_assumptions.yml`, `data/canonical/scenarios.yml`, `tools/validate_canonical_data.py`, plus corrections to `README.md` and four nav/meta docs (`docs/reading-order.md`, `docs/00_document_inventory.md`, `docs/01_conflicts_log.md`, `docs/HANDOFF.md`).

**Phase 2 scope (2026-08-08, same day, follow-on):** a fix to a real bug found in `tools/check_consistency.py` during Phase 1 (§8 below, now resolved — see §11), a new regression test suite (`tests/test_check_consistency.py`), and two new canonical domains: `data/canonical/staffing.yml` and `data/canonical/wages.yml`, with matching validator extensions. See §10-§16 below for full Phase 2 detail.

**Phase 3 scope (2026-08-09, follow-on):** one new canonical domain, `data/canonical/opex.yml` (non-payroll operating expenses), with matching validator extensions and 6 new tracker items. See §20-§25 below for full Phase 3 detail.

**Not built any phase so far:** the Master Financial Model, the Master Operations Model, any XLSX/PDF/DOCX generation, the remaining canonical domains from `docs/architecture/CANONICAL-DATA-SCHEMA.md`'s original ~20-domain sketch (payroll_costs, startup_costs, capex, revenue_assumptions, financial_assumptions, risks, decisions, sources, verification_status), and — deliberately, across every phase so far — a resolution of Table 1 vs. Table 2 as primary.

---

## 1. What Canonical Data Exists, and Where

```
data/canonical/
├── pricing.yml              AM/PM headline pricing + a representative slice of individual services       [Phase 1]
├── client_assumptions.yml   universal + scenario-dependent operational assumptions                        [Phase 1]
├── scenarios.yml            Table 1 and Table 2, both explicit, neither marked primary                    [Phase 1]
├── staffing.yml             every role, headcount, category, skills, shift assumptions                    [Phase 2]
├── wages.yml                hourly rates, super, workers comp, casual-minimum rule, penalty-rate conflicts [Phase 2]
└── opex.yml                 non-payroll operating expenses -- premises/tech/professional/insurance/        [Phase 3]
                              marketing/consumables, 28 records, 3 conflicts
```

All five files live under `data/canonical/` — real content in the `data/` layer proposed in `docs/architecture/TARGET-ARCHITECTURE.md` Layer 2. `docs/CURRENT-STATE.md` remains the authoritative human-readable canonical file; these YAML files are a machine-readable **subset** of it (plus, for staffing/wages, of `docs/financial-break-even-staff.md`, `docs/hr-framework.md`, `docs/pm-staffing-roster.md`, and `docs/HANDOFF.md`), not a replacement, and not (yet) auto-generated from it or vice versa — a human (this session) transcribed values from source documents into YAML, checking each one against the source rather than re-deriving anything.

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

## 8. A Note on `tools/check_consistency.py` (relevant to trusting "0 findings") — bug found Phase 1, FIXED Phase 2 (see §11)

While preparing this proof of concept, a real bug was found in the existing `tools/check_consistency.py`'s staleness-marker detection: its `STALENESS_MARKERS` regex includes the bare substring `prior` (intended to catch the word "prior"/"previously") with no word boundary, so it also matches inside unrelated words like **"priority"** — e.g. "Pathology partner (WDP, **priority** 1) has been emailed" in `docs/reading-order.md` was enough to suppress a genuine, otherwise-unflagged stale figure (`10 GTT clients/day`) sitting three lines later, purely because "priority" happened to be within the script's 3-line lookback window. This was confirmed by directly invoking the script's own `scan_file()`/`has_marker()` functions against the real file content, not inferred.

**This means `tools/check_consistency.py` returning "0 findings" is not, by itself, proof that a document is fully current** — it is a real, useful check, but has at least one confirmed false-negative pattern. Part 1's corrections in this session were made by manual review (cross-referencing every nav/meta doc's stated model against `docs/CURRENT-STATE.md` directly), not by trusting the checker's clean report. **This bug was not fixed this phase** — fixing `tools/check_consistency.py` was not in this phase's authorised scope (only `README.md` and the four nav/meta docs could be modified; "everything else stays additive/new files only"). Flagged here explicitly so it isn't lost, and is a natural candidate for a small, standalone fix in a future session (change `prior` to `\bprior\b` or similar).

---

## 9. Recommended Next Migration Domain (Phase 1 recommendation — actioned in Phase 2, see §12-§13)

**`data/canonical/staffing.yml` and `data/canonical/wages.yml`**, in that order, for two reasons:

1. They are the most direct dependency of the Financial Model's payroll module and the Operations Model's roster-requirement module (`docs/architecture/MODEL-ARCHITECTURE.md` §4's "cross-model dependency rule") — building them next means the next domain migrated is also the next one that unblocks real model-building, not just more inert data.
2. They have a real, disclosed, previously-actually-occurring bug to validate against: `docs/VERIFICATION-TRACKER.md` item 1i (the Saturday PM 3-hour-minimum casual engagement rule being under-applied, then corrected) is exactly the kind of error a `staffing.yml`/`wages.yml` pair with a payroll-calculation validator (extending `tools/validate_canonical_data.py` per `docs/architecture/VALIDATION-ARCHITECTURE.md` §2.1's "3-hour casual minimum check") would catch automatically going forward.

`services.yml` (the full a-la-carte catalog deferred in §7) was the next-best alternative if a lower-risk, non-financial domain was preferred first — not chosen; Anthony approved the staffing/wages route instead (§10 below). **See §16 for the Phase 2 recommendation of what comes after staffing/wages.**

---

# PHASE 2 (2026-08-08, same day) — Consistency-Checker Fix, Staffing, Wages

Sequence followed, per the coordinator's explicit instruction: **CONSISTENCY CHECKER FIX → STAFFING DATA → WAGE DATA → VALIDATION.**

## 10. Consistency-Checker Fix

The bug disclosed in §8 (the `prior` substring matching inside `priority`) was fixed by anchoring the regex to `\bprior\b`. Full before/after evidence:

**Before the fix** (confirmed by running `has_marker()` against a temporary copy of the pre-fix regex, then deleted — not left in the repo):
```
BEFORE FIX -- has_marker on a line containing only 'priority': True (bug: True means falsely triggered)
BEFORE FIX -- has_marker on the real stale-figure line (3 lines after 'priority'): True (bug: True means the genuine stale finding was suppressed)
BEFORE FIX -- has_marker on a line using 'prior' as an intentional marker: True (expected True either way)
```

**After the fix:**
```
test_prior_as_whole_word_still_matches ... ok
test_priority_substring_does_not_match ... ok
test_genuine_stale_finding_near_priority_is_still_detected ... ok
test_existing_markers_unaffected ... ok
test_scan_file_end_to_end_on_real_repo_docs ... ok

Ran 5 tests in 0.007s
OK
```

The fix (`tools/check_consistency.py`, `STALENESS_MARKERS` regex): `prior` → `\bprior\b`, with an inline comment explaining why, pointing to the regression test. **Smallest safe change, as instructed** — no other marker pattern was touched, and the checker's overall method (grep-based sweep, not a semantic parser) was not replaced.

## 11. Regression Test

New file: `tests/test_check_consistency.py` — 5 tests (see the actual output in §10 above). This is the **first automated test suite in this repo** — no `tests/` directory or test infrastructure existed before this session, so "run the full existing consistency test suite" (per the coordinator's Part 2 instruction) is satisfied by this new suite plus the full whole-repo `check_consistency.py` run in §12 below, since no other test suite pre-existed to run.

Tests cover, specifically: `prior` still works as an intentional marker (✓); `priority` does not trigger it (✓); a genuine stale finding reconstructed from the real `docs/reading-order.md` bug case is still detected even with `priority` nearby (✓); five other existing marker words are unaffected by the fix (✓); an end-to-end run of the real `scan_file()` against the real `docs/reading-order.md` completes without error (✓).

## 12. Full Consistency Run (Post-Fix)

```
check_consistency: 0 findings across all docs/*.md (excluding archive/).
All tracked figures consistent with docs/CURRENT-STATE.md.
```

**This "0 findings" result is now genuinely trustworthy, not just unexamined**, for a specific reason: a diagnostic sweep (not committed, run ad hoc this session) counted **533 raw pattern hits** across the corpus — every line anywhere in `docs/*.md` matching one of `check_consistency.py`'s tracked stale-figure patterns, *before* the staleness-marker suppression logic runs at all. After the marker-suppression logic (with the `prior`/`priority` bug now fixed), **all 533 are correctly suppressed** — spot-checking a sample of the raw hits confirms each sits inside genuinely historical/superseded prose (the word "historical" or "superseded" literally appears in nearly every sampled line). This means the 0-findings result reflects 533 correctly-classified historical mentions, not 533 silently-swallowed live errors. No findings were suppressed, deleted, archived, or altered to force this result — this is the checker's genuine output against the repo as it stands, per the coordinator's explicit instruction not to manufacture a clean pass.

## 13. Staffing Data Migrated (`data/canonical/staffing.yml`)

11 current-model records (`records`) + 2 historical stub records (`historical_staffing_scenarios`), covering every category the coordinator asked to be preserved:

| Category | Records |
|---|---|
| `management_admin` | Venue Manager (PLACEHOLDER — not hired), Receptionist/Manager |
| `phlebotomy` | Phlebotomist ×2 (headcount VERIFIED, employment model OPEN per item 1d) |
| `treatment` | Massage+Beauty pool ×4, Nails ×2, Hair ×2 — all VERIFIED, identical under both Table 1 and Table 2 |
| `other` | PM dedicated casual roster ×4 (1 each: massage/hair/nail/beauty), Casual Relief Pool (budget line) |

**Table 1 vs. Table 2 — both preserved, neither chosen, as instructed:** AM treatment + phlebotomy headcount is identical under both scenarios (a genuine finding already established in `docs/CURRENT-STATE.md` §4, not something this file re-derives) — represented via `staffing_scenario: [scenario_table_1, scenario_table_2]` on each affected record, rather than picking one. Where headcount *does* differ (the historical 14-client ceiling, 9 staff instead of 8), both figures are preserved via `historical_staffing_scenarios`, marked `SUPERSEDED`, not deleted.

**Sources used:** `docs/CURRENT-STATE.md` §4 (primary, for current headcount), `docs/financial-break-even-staff.md` (Receptionist split-shift detail, AM shift window), `docs/pm-staffing-roster.md` (PM roster structure, Locked Decisions), `docs/multirole-CORRECTION.md`/`docs/VERIFICATION-TRACKER.md` item 1d (dual-qualification pairing and phlebotomist employment-model status).

## 14. Wage Data Migrated (`data/canonical/wages.yml`)

18 records covering hourly/annual rates for every role, plus employer-cost items (superannuation, payroll tax, workers comp) and award-provision rules (casual minimum engagement, MA000027 Saturday carve-out, MA000005/MA000002 penalty rates).

**A material finding, not previously logged anywhere in this repo:** cross-referencing `docs/financial-break-even-staff.md`, `docs/hr-framework.md`, and `docs/HANDOFF.md` surfaced **two genuine, previously-undisclosed conflicts**, both recorded in `wages.yml`'s `conflicts` list rather than silently resolved:

1. **MA000005 penalty rates disagree three ways.** Saturday: 133% (`financial-break-even-staff.md`) vs. "133% permanent/150% casual" (`HANDOFF.md`) vs. 150% flat (`hr-framework.md`). Sunday: 200% vs. 200% vs. 175%. Public Holiday: 250% vs. "250-275%" vs. 250%. None of the three cites a fetched primary source for the exact percentages.
2. **Base hourly rates disagree materially** between `financial-break-even-staff.md` (the rates every current P&L figure is arithmetically built from — verified directly: 4×A$62,774 + 4×A$60,456 = A$492,920/yr, exactly matching `docs/CURRENT-STATE.md` §5's 8-treatment-staff figure) and `docs/hr-framework.md`'s own "Indicative rate (2026)" table (materially lower, e.g. Nail/Hair Level 3: $28.50/hr vs. ~$23.49/hr) — the latter is self-labelled indicative/needs-confirmation, so this wasn't forced into a false resolution either.

Neither conflict was picked a winner on — both are recorded, sourced, and left open, per the coordinator's explicit instruction.

**A third finding, also new:** every wage rate in this repo is dated "Effective 1 July 2025" or "Indicative (2026)," and this session's date (2026-08-08) is after the Fair Work Commission's typical 1 July annual wage review date — none of these rates has been re-checked against a possible 1 July 2026 review outcome. Recorded as `conflict_award_rate_staleness`, an explicit unresolved verification requirement, not silently assumed current.

**Sources used:** `docs/financial-break-even-staff.md` (Award Wage Summary — primary), `docs/hr-framework.md` (cross-check, surfaced the conflicts above), `docs/HANDOFF.md` (cross-check, surfaced the penalty-rate conflict), `docs/pm-staffing-roster.md` (confirms the same AM rates apply to PM roles), `docs/CURRENT-STATE.md` §5 (workers comp rate).

## 15. The 3-Hour Casual Minimum — Investigation Finding

Investigated per the coordinator's explicit 5-step instruction, not adopted blindly (full detail in `wages.yml`'s `wage_casual_minimum_engagement` record):

1. **What the repo says:** a 3-consecutive-hour minimum casual engagement (MA000005 clause 11.5, MA000027 clause 11.2).
2. **Where it came from:** `docs/financial-break-even-staff.md`'s Staff Downtime Protocol section, tagged `[VERIFIED — Fair Work Ombudsman/Fair Work Commission, checked via direct WebFetch, 2026-07-30]` — a real external-source citation with a method and a date.
3. **Supporting/disputing evidence in the repo:** supporting — the rule was actively *applied* to correct a real costing bug (`docs/VERIFICATION-TRACKER.md` item 1i: Saturday PM Direct Labor corrected from A$335.55/day to A$654.32/day once the 3-hour floor was properly enforced). No disputing evidence found anywhere.
4. **Can it safely be marked VERIFIED:** **yes** — on the strength of the repo's own documented external check — but disclosed honestly: this session did not independently re-fetch the Fair Work source itself; the VERIFIED status traces to the prior session's own direct-WebFetch check (2026-07-30), not a fresh verification performed while building this file.
5. **N/A** — resolved at step 4.

**Explicitly distinguished from a different, genuinely still-unconfirmed MA000027 provision** (whether Saturday 8am-4:30pm counts as *ordinary hours* for phlebotomists, which would reduce Saturday penalty cost) — recorded separately as `wage_ma000027_saturday_carveout`, `PLACEHOLDER`, per `docs/VERIFICATION-TRACKER.md` item 11's own "capability gap flagged, unconfirmed" status. These are two different provisions and were not conflated.

## 16. Validator Extensions and Test Result

`tools/validate_canonical_data.py` extended with 3 new check categories (full detail in the script's own docstring): (a) `staffing.yml` required-field + category-vocabulary checks, (b) `wages.yml` status/value consistency checks (a `PLACEHOLDER` record may not carry a concrete value; a non-`PLACEHOLDER`/`SUPERSEDED` "rate-shaped" record may not be null), (c) scenario-reference validity (`staffing_scenario`/`scenario_id` fields must resolve to a real id in `scenarios.yml`, auto-loaded regardless of which files are targeted) and a new global cross-file duplicate-ID check (an id must be unique across *all* `data/canonical/*.yml` files, not just within one).

**Real-data result** (all 5 files):
```
data\canonical\client_assumptions.yml: PASS
data\canonical\pricing.yml: PASS
data\canonical\scenarios.yml: PASS
data\canonical\staffing.yml: PASS
data\canonical\wages.yml: PASS
  WARN: [x3 -- the disclosed conflicts.yml entries in wages.yml, correctly surfaced as warnings, not failures]

validate_canonical_data: 5 file(s) checked, 0 error(s), 3 warning(s).
All checks passed.
```

**Deliberately-broken test result** (scratch fixtures, not committed — same discipline as Phase 1, per the coordinator's explicit instruction):
```
bad_staffing.yml: FAIL
  ERROR: disallowed status value 'BOGUS' ...
  ERROR: category 'not_a_real_category' is not one of the known staffing categories ...
  ERROR: missing required staffing field(s): ['category']
  ERROR: staffing_scenario references unknown scenario id 'scenario_table_99' ...

bad_wages.yml: FAIL
  ERROR: status=MODELLED but no 'source' key present ...
  ERROR: Conflicting prices for ('base_rate', 'Nail Technician base rate') ...
  ERROR: status=PLACEHOLDER but 'value_pct' is 42, not null ...
  ERROR: status=VERIFIED but 'value_pct' is null ...
  ERROR: records[*].id 'staff_x' also appears in bad_staffing.yml ...

validate_canonical_data: 2 file(s) checked, 9 error(s), 0 warning(s).
```

All 6 required test cases (invalid status, duplicate ID, missing source, conflicting wage/rate, missing required field, malformed scenario reference) were confirmed caught, plus 2 bonus cases (`PLACEHOLDER`-with-value and `VERIFIED`-with-null-value) the wages-specific check also catches. Fixtures deleted after the test run, not committed.

---

## 17. Unresolved Issues (Phase 2, carried forward — not resolved this pass)

- **The 3 wage conflicts** (§14) — penalty rates, base-rate discrepancy, award-staleness — all genuinely open. Recommend adding tracker rows to `docs/VERIFICATION-TRACKER.md` in a future session (not done this pass, to stay within this phase's authorised file list — only `data/`, `tools/`, `tests/`, and `docs/architecture/` were touched).
- **The 7-vs-8 treatment-staff daily-rostering finding** (staffing.yml's `staff_treatment_massage_beauty_pool` note) — valid at the historical 12-client/23-min model, not independently re-verified against Table 1/Table 2's 25-min cadence.
- **Receptionist/Manager's AM 07:00-12:00 shift block** — written against the pre-rebase 07:00 start assumption, not re-checked against Table 2's 08:00 start.
- **MA000027 Saturday ordinary-hours carve-out** (item 11) — still unconfirmed, same status as before this pass; no external verification attempted.
- **Payroll tax** — recorded as `PLACEHOLDER` in `wages.yml` on the basis that "not addressed anywhere in this repo's documents" (checked `hr-framework.md` and `financial-setup.md`'s Payroll Setup/Superannuation sections at the time). **Correction, 2026-08-09 (Phase 3):** this was incomplete, not wrong in spirit — `docs/financial-setup.md` STEP 1's accountant-brief checklist *does* address it: "Payroll tax threshold advice (WA: A$1M/year threshold — not triggered at launch but confirm)." Found while researching `opex.yml` sources, outside `wages.yml`'s own scope to fix this pass (see the coordinator's Phase 3 scope limits) — flagged here rather than silently left uncorrected. `data/canonical/wages.yml`'s `wage_payroll_tax` record was NOT edited this pass; a future session touching `wages.yml` should update it to reflect this finding (WA's A$1M/yr threshold, current total payroll ~A$700-900K/yr, genuinely not triggered at launch — reassuring, not concerning, but still worth recording accurately).

## 18. Recommended Next Canonical Migration Domain (Phase 1 recommendation — actioned in Phase 3, see §20-§25)

**`data/canonical/opex.yml`** (non-wage operating expenses — rent, utilities, insurance, Fresha/Resend/marketing, GTT supplies, laundry, cleaning, accounting, consumables), for two reasons:

1. It's the other direct input the Master Financial Model's P&L module needs alongside `staffing.yml`/`wages.yml` (per `docs/architecture/MODEL-ARCHITECTURE.md` §1's dependency graph) — completing it means the P&L's cost side is fully sourced from canonical data, not just payroll.
2. `docs/CURRENT-STATE.md` §6/§7's startup-capital reconciliation gap (3-6 unreconciled ranges, explicitly disclosed as never resolved) sits directly adjacent to opex — migrating opex first would surface whether the same "which source document is authoritative" question recurs there too, before attempting the harder `startup_costs.yml`/`capex.yml` domains.

`services.yml` (the full a-la-carte catalog, deferred twice now — Phase 1 §7 and Phase 1 §9) remained the next-best lower-risk alternative if a non-financial domain was preferred — not chosen; Anthony approved the opex route instead. **See §26 for the Phase 3 recommendation of what comes after opex.**

---

# PHASE 3 (2026-08-09) — Non-Payroll Operating Expenses (`opex.yml`)

## 20. Opex Data Migrated (`data/canonical/opex.yml`)

28 records + 3 declared conflicts, covering every category the coordinator asked to be searched for, where the repo actually supported a finding:

| Category | Records | Notable finding |
|---|---|---|
| `premises` | Rent, rent-outgoings ambiguity, utilities, cleaning, laundry, medical waste | Medical waste contract real and sourced but missing from the modelled total (item 21) |
| `technology` | Fresha booking software, internet+phone, Resend, Xero (bundled, not itemised), EFTPOS software fee, EFTPOS transaction fee | Booking software cost conflict (item 20); EFTPOS entirely un-modelled (item 23) |
| `professional` | Accounting/bookkeeping, accountant initial brief (STARTUP), ASIC business name, Food Safety Supervisor cert (STARTUP), commercial lease solicitor (PLACEHOLDER) | Correctly separates recurring opex from one-off STARTUP costs within the same category, per Part 6's instruction |
| `insurance` | Modelled flat PL+PI line, itemised PL, itemised PI, workers-comp cross-reference, property/contents, business interruption | The single highest-materiality finding this phase (item 19) |
| `marketing` | Meta/Instagram ads (steady state + Month 1-4 ramp) | Ramp recorded as per-month values, no single `monthly_equivalent` manufactured |
| `consumables` | GTT supplies, general consumables, misc/contingency | Stale volume basis + FIXED-vs-VARIABLE classification disagreement (item 22) |

**Cross-checked arithmetically, not assumed:** the 13 line items that sum to `docs/profit-loss-tables.md`'s canonical A$13,980.00/month Non-Wage Overhead total were individually transcribed and re-summed — they total exactly A$13,980.00, confirming no transcription error before any conflict analysis began.

**Sources used:** `docs/profit-loss-tables.md` §4 (primary, for the 13-line canonical breakdown), `docs/cash-flow.md` (cross-check, agrees), `docs/rent-budget-2026-07-28.md` (rent cross-check, agrees exactly), `docs/financial-setup.md` (STEP 1, 2, 5, 6, 8, 9 — the richest single source of previously-unmigrated real cost figures), `docs/equipment-costs.md` §1/§8 (medical waste, stale booking-software alternative), `docs/ivy-booking-system.md` (actual Fresha pricing detail), `docs/unit-economics.md` (historical, cited only for the FIXED-vs-VARIABLE classification finding), `docs/external-resources-and-advisors.md` (professional-services context), `docs/grace-startup-plan.md` and `docs/property-links-2026-07-28.md` (rent/outgoings context).

## 21. Conflicts Discovered

Three declared in `opex.yml`'s own `conflicts` list, all also formalised into `docs/VERIFICATION-TRACKER.md` (§23 below):

1. **`conflict_insurance_estimate`** — modelled A$400/month vs. itemised A$11,700-19,000/year (2.4-4x higher, 3 missing policy types). The single highest-materiality finding across all three phases of this canonical-data effort so far.
2. **`conflict_booking_software_cost`** — three figures for the same platform (Fresha), with the modelled figure likely the least accurate of the three and, unusually, on the *high* side (the model may currently overstate this specific cost).
3. **`conflict_variable_vs_fixed_classification`** — GTT supplies, general consumables, and laundry are FIXED per the current model but VARIABLE per `unit-economics.md` (historical). A genuine either-or, not a numeric disagreement.

## 22. Unresolved Items / Gaps Found (Beyond the 3 Declared Conflicts)

- **Medical waste disposal contract** (A$50-100/month) — real, sourced, never incorporated into the canonical total (a gap, not a conflict — nothing to disagree with, it's simply absent).
- **EFTPOS terminal/software/transaction-fee costs** — entirely absent from the modelled total; provider choice (Tyro vs. Square) not made.
- **Rent outgoings** — whether the modelled A$8,000/month is net or gross of outgoings is unstated anywhere; a general (not venture-specific) Perth-market note suggests outgoings could add 15-25%.
- **GTT supplies' stale volume basis** — "200 tests/month" predates both current committed scenarios (Table 1: 396, Table 2: 264).

## 23. Verification Items Added

`docs/VERIFICATION-TRACKER.md` items **19, 20, 21, 22, 23, 24** (FINANCIAL — NEEDS ACCOUNTANT CONFIRMATION section, continuing the sequential numbering from item 18) — full detail in that file. Each includes: issue, affected data/model, source documents, current status, required verification/action, and impact if unresolved, matching the tracker's existing dense-entry convention.

## 24. Startup vs. Opex Classification Issues

Handled per Part 6's instruction — classified from the repo itself, not general accounting assumptions:

- **Accountant initial brief** (A$500-1,500) — correctly `cost_type: STARTUP`, not recurring opex, despite living in the same "Professional" category as the genuinely recurring `opex_accounting_bookkeeping` record. No `monthly_equivalent`/`annual_equivalent` computed for it (would misrepresent a one-off as recurring).
- **Food Safety Supervisor certificate** (A$100-200) — same treatment, `cost_type: STARTUP`; renewal cadence genuinely unknown (not stated anywhere), flagged rather than assumed one-off-forever.
- **EFTPOS terminal purchase** (Square's A$299 one-off) — explicitly noted as CAPEX, NOT itemised as its own opex.yml record (only the ongoing software fee and transaction-fee percentage are recorded here).
- **Workers compensation** — the one deliberate `cost_type: PAYROLL` record in this file (`opex_insurance_workers_comp_estimate`), included only because `financial-setup.md` itself bundles it inside an "Insurance" cost table alongside genuine opex lines — explicitly marked cross-reference-only, not a second source of truth competing with `wages.yml`'s `wage_workers_comp_rate`.
- **`docs/CURRENT-STATE.md` §6/§7's startup-capital reconciliation problem** was not touched or re-opened — the one deliberate overlap point (`opex_insurance_modelled`'s note referencing §7.3's "First-year insurance" line using the same A$400/month figure) was confirmed as an intentional, already-disclosed cross-reference in the source repo, not a new duplication error.

## 25. Validator Extensions and Test Result

`tools/validate_canonical_data.py` extended with `opex.yml`-specific checks (full detail in the script's own docstring, checks 11-13): required-field validation, `frequency`/`cost_type` controlled-vocabulary checks, numeric-value-shape validation (`amount`/`monthly_equivalent`/`annual_equivalent` must be null, a number, or a dict of numbers), status-vs-value consistency (reusing the wages.yml pattern), and — new this phase — monthly/annual normalisation-correctness checking against the actual `amount` at the record's stated `frequency`.

**Real-data result** (all 6 files):
```
validate_canonical_data: 6 file(s) checked, 0 error(s), 6 warning(s).
All checks passed.
```

**Deliberately-broken test result** (scratch fixture, not committed):
```
bad_opex.yml: FAIL
  ERROR: disallowed status value 'NOT_A_REAL_STATUS' ...
  ERROR: status=MODELLED but no 'source' key present ...
  ERROR: duplicate key 'opex_dup' ...
  ERROR: frequency 'fortnightly' is not one of the known frequencies ...
  ERROR: cost_type 'NOT_A_TYPE' is not one of the known cost types ...
  ERROR: 'amount' is a malformed numeric value ('not a number') ...
  ERROR: annual_equivalent=5000 does not match amount=100 at frequency=monthly (expected ~1200.00) ...
  ERROR: scenario_id references unknown scenario id 'scenario_table_999' ...

validate_canonical_data: 1 file(s) checked, 8 error(s), 0 warning(s).
```

All 8 required test cases (invalid status, duplicate ID, missing source, invalid frequency, invalid cost type, malformed numeric value, incorrect monthly/annual calc, invalid scenario reference) confirmed caught. Fixture deleted after the test run, not committed.

## 26. Recommended Next Canonical Migration Domain

**`data/canonical/startup_costs.yml` / `data/canonical/capex.yml`**, tackled together, for two reasons:

1. They are the last major domain directly feeding the Master Financial Model's cost side (`docs/architecture/MODEL-ARCHITECTURE.md` §1) — with `staffing.yml`, `wages.yml`, and `opex.yml` now built, startup/capex is what remains before a real P&L/cash-flow model could theoretically be assembled from canonical data alone (still not attempted — out of scope).
2. `docs/CURRENT-STATE.md` §6/§7 already documents, in its own words, an explicit "financial model moved 5+ times" startup-capital reconciliation failure (3-6 unreconciled ranges, an adopted figure that doesn't exactly match its own component sum) — this is the single most consequential unresolved numeric question in the entire repo, and canonicalising it (WITHOUT resolving it — preserving every range, exactly as `opex.yml`/`wages.yml` preserved their own conflicts) would make that reconciliation problem visible to any future automated check, rather than only living in prose.

`services.yml` (the full a-la-carte catalog, deferred three times now) remains the next-best lower-risk, non-financial alternative if a smaller domain is preferred first.

---

## 27. What This Document Does Not Do (as of Phase 3)

It does not build the Master Financial Model, Master Operations Model, any Excel/XLSX workbook, P&L, cash-flow model, chart, PDF, or DOCX. It does not migrate `startup_costs.yml`, `capex.yml`, `services.yml` (full a-la-carte catalog), `payroll_costs.yml` (a derived/model-layer domain, not yet built), or any other remaining domain from `docs/architecture/CANONICAL-DATA-SCHEMA.md`'s original ~20-domain sketch. It does not resolve Table 1 vs. Table 2 as primary. It does not resolve any of the wage conflicts (tracker items 16-18) or the opex conflicts/gaps added this phase (tracker items 19-24) — all six are recorded, sourced, and left open. It does not touch or resolve `docs/CURRENT-STATE.md` §6/§7's startup-capital reconciliation problem, beyond confirming (not re-litigating) that one specific cross-reference within it (the A$400/month insurance figure) is a deliberate, already-disclosed linkage rather than a new duplication.
