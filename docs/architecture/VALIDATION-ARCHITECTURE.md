# GTT Center Perth — Validation Architecture

**Purpose:** define the future automated checks across every layer (`TARGET-ARCHITECTURE.md`), and state explicitly how they extend `tools/check_consistency.py` rather than replace it. **No new validator is built this phase.** This document specifies what each future check does, what layer it operates on, and which existing finding in this repo (a real bug or a real disclosed gap) motivates it.

---

## 0. Relationship to `tools/check_consistency.py` (read this section first)

`tools/check_consistency.py` does exactly one job today, and does it well: it greps every `docs/*.md` file (excluding `docs/archive/`) for a hand-maintained list of known-stale numeric patterns, sourced from `docs/CURRENT-STATE.md`, and flags any hit that lacks a nearby staleness marker word. Per its own docstring, it is explicitly "not authoritative" — `CURRENT-STATE.md` is — and explicitly "a grep-based sweep, not a semantic parser."

**This script is not replaced by anything in this document.** It continues to be the Layer-1/2 (SOURCE/CANONICAL prose) documentation-consistency check, run before any external conversation, exactly as `rules/CLAUDE.md` companion rule 4 already requires. Everything below is **additional** validation at layers `check_consistency.py` was never designed to reach: the future machine-readable data layer, the model layer, and the document-generation layer. The relationship is layered, not sequential — each layer's checks catch what the others structurally cannot:

| Layer | Existing check | New check proposed here |
|---|---|---|
| `docs/*.md` prose (Layer 1/2 combined) | `tools/check_consistency.py` — regex sweep for known-stale values | Extended pattern list only (see §4) — same tool, same method, more coverage |
| `data/canonical/*.yml` (Layer 2, machine-readable) | None exists | §1 — schema + status validation |
| `models/*` (Layer 3) | None exists (the disclosed weekly-to-monthly rounding gap in `profit-loss-tables.md` was found by hand, three times) | §2 — model consistency checks |
| `models/operations/*` scheduling output | The six `tools/*.py` solver scripts, each ad hoc and scenario-specific | §2.2 — a standing, parameterized version of the same two-method verification |
| `documents/` templates and `outputs/*` generated files | None exists | §3 — generation-layer checks |

---

## 1. Data-Layer Validation (new — `data/canonical/*.yml`)

| Check | What it catches | Real motivating example from this repo |
|---|---|---|
| **Schema validation** | A `data/canonical/*.yml` record missing a required envelope field (`status`, `source`, etc. — see `CANONICAL-DATA-SCHEMA.md` §0) | N/A yet (no data layer exists) — but `CURRENT-STATE.md`'s own history shows figures being added without a tag was exactly what `rules/CLAUDE.md` was created to stop; a schema validator makes an untagged record a hard error, not a discipline that depends on the writer remembering |
| **Status-value validation** | A `status` field set to something outside the 7 allowed values (`DATA-GOVERNANCE.md` §3) | — |
| **`SUPERSEDED` requires `superseded_by`** | A record marked superseded with no pointer to what replaced it | `CURRENT-STATE.md`'s own convention already does this correctly in prose (e.g. the 14-client ceiling explicitly names Table 1 as what supersedes it) — this check makes that convention structurally required, not just stylistically consistent |
| **`MODELLED` requires `status_detail`** | A `MODELLED` record with no named assumption | `rules/CLAUDE.md`'s own definition already requires this ("name the assumption explicitly") — currently enforced by human review only |
| **`PLACEHOLDER` cross-reference to `VERIFICATION-TRACKER.md`** | A `PLACEHOLDER` record in `data/canonical/` with no matching open item in the tracker | Direct implementation of `DATA-GOVERNANCE.md` §5 rule 6 |
| **Orphan-source check** | A `source` field pointing to a `docs/*.md` file that doesn't exist, or a `docs/archive/*` file (a canonical fact should never cite an archived source as current proof) | — |

---

## 2. Model-Layer Validation (new — `models/*`)

### 2.1 Financial Consistency

| Check | What it catches | Real motivating example |
|---|---|---|
| **Revenue reconciliation** | Revenue computed two different ways (e.g. delta-built vs. first-principles) landing on different totals without a disclosed, tracked gap | `CURRENT-STATE.md` §5's own disclosed ~A$2,576/month weekly-to-monthly scaling artifact, present at three separate model revisions (10-, 12-, 18-client) before this document existed to catch it structurally |
| **Payroll reconciliation** | Payroll computed by the Financial Model diverging from the Staffing Model's own payroll output (see `MODEL-ARCHITECTURE.md` §4's cross-model dependency rule) | `rules/CLAUDE.md`'s founding incident: the AM/GTT segment shown as losing money in `pm-staffing-roster.md` nine days after being corrected elsewhere |
| **P&L arithmetic check** | Revenue − COGS − Payroll − Opex ≠ stated Net P&L | — |
| **Cash-flow tie-out** | Cash flow's cumulative position not reconciling to P&L + capex/startup timing | — |
| **Break-even sanity check** | A stated break-even volume that, when run back through the revenue/cost model, doesn't actually net to zero | — |
| **3-hour casual minimum check** | A payroll line costed below the award's minimum casual engagement without the floor being applied | `VERIFICATION-TRACKER.md` item 1i — Saturday PM Direct Labor was genuinely understated (1.54hrs/role/day priced at raw hours) until caught and corrected by hand; flagged as still open for the 14-client ceiling figures at the time they were current |
| **Scenario leakage check** | A `SCENARIO`-tagged input value appearing inside a base-case model run | Direct implementation of `DATA-GOVERNANCE.md` §4's table row for `SCENARIO` |

### 2.2 Operational Consistency

| Check | What it catches | Real motivating example |
|---|---|---|
| **Impossible schedule check** | Any chair or phlebotomist double-booked at a single instant | This is exactly what `tools/sync-treatment-solver.py` and `tools/draw-event-scheduler.py` already do, per-scenario — this check is the standing, parameterized version (per `MODEL-ARCHITECTURE.md` §2's refactor) that runs automatically whenever `scheduling_assumptions.yml` changes, rather than requiring a new one-off script |
| **Staff overlap check** | A staff category's peak concurrency exceeding its rostered headcount | `CURRENT-STATE.md` §4's own two-method verification pattern (sweep-line + greedy first-fit) — this repo already treats "both methods must agree" as the standard of proof; the validator formalises that as a required, automatic check rather than a manual one run at each rebase |
| **Chair conflict check** | Two clients assigned the same chair at overlapping times | Same solver logic as above, chair-specific |
| **Clinical timing conflict check** | A draw event scheduled outside its required offset window (e.g. Draw 2 not landing at exactly +60min under the synchronized model) | `CURRENT-STATE.md` §1's Item 1 finding (2026-08-05) — testing a 7th pair at Table 2's 10:25 slot found an exact chair-level collision; this is precisely the class of check this validator automates going forward rather than requiring a fresh manual sweep each time a new pair-insertion candidate is proposed |
| **Capacity ceiling check** | A document or model claiming a capacity figure the operations model itself cannot reproduce | — |
| **Staffing insufficiency check** | A rostered headcount below the peak-concurrency requirement for the stated volume | `CURRENT-STATE.md` §4's own "testing 7 (pool capped at 3) against the 12-client schedule fails — 2 clients unassignable" finding — proof this class of check catches real errors, currently run by hand |

---

## 3. Documentation & Generation-Layer Validation

| Check | What it catches | Real motivating example |
|---|---|---|
| **Stale figure sweep** | Unchanged — `tools/check_consistency.py`, extended with new pattern entries every time `CURRENT-STATE.md`'s canonical values change (already how it works, per its own `CHECKS` list comments) | Ongoing, by design |
| **Conflicting-volume/staffing cross-check** | Two `docs/*.md` files stating different headcount or client-volume figures for the *same* scenario, with neither marked stale | `01_conflicts_log.md` CONFLICT-03 (Scenario B vs Scenario C) — this is exactly the class of issue that log records were found manually; a structured check comparing every document's stated figures against `data/canonical/*.yml` would catch new instances automatically |
| **Outdated-assumption check** | A document's narrative describing an operating model that no longer matches `data/canonical/scenarios.yml`'s current primary scenario, even where no specific number is wrong (a *prose*-level staleness, not a figure-level one) | `REPOSITORY-AUDIT.md` finding F-2 — `reading-order.md`, `00_document_inventory.md`, and `01_conflicts_log.md` describe the 10-client/+A$25,087 model in prose, dated 2026-07-20, two rebases behind `CURRENT-STATE.md`. `check_consistency.py`'s regex patterns do not currently include the 10-client/A$25,087 pair specifically because those exact figures were retired before the check's pattern list was last extended — this class of drift (prose describing a whole outdated model, not a single wrong digit) is structurally different from what a value-regex sweep catches, and needs its own check: compare each document's "last reconciled against CURRENT-STATE.md" date/version marker (a new required field, not yet in use anywhere) against `CURRENT-STATE.md`'s own latest changelog date |
| **Scenario-presented-as-base-case check** | A document quoting a `SCENARIO`-tagged figure (e.g. Table 2's +A$27,084.69/month) without labelling it as the secondary reference | Direct implementation of `DATA-GOVERNANCE.md` §2's motivating example — this exact failure mode is not currently caught by `check_consistency.py`, since Table 2's figure isn't itself in the stale-pattern list (it's a legitimate secondary reference, not a wrong number) — the gap is about missing context, not a wrong value, which needs a different check than a value-regex |
| **Unresolved-placeholder check** | A `[to be inserted]`/`[PLACEHOLDER]` marker that has been silently smoothed into fluent prose elsewhere in the same or a different document, defeating the purpose of the marker | `rules/CLAUDE.md`'s own founding finding: "roughly 48 of 107 markdown files ... contained placeholders — some ... silently smoothed over elsewhere" |
| **Chart-vs-source-data check** | A generated (or hand-built) HTML/visual output whose displayed figures don't match the `data/canonical/`/`models/` values current at generation time | `docs/scenario-c-sync-timeline.html` / `docs/scenario-c-timeline.html` — the audit found the non-sync `scenario-c-timeline.html` is "likely SUPERSEDED ... not confirmed or flagged this session" per `01_conflicts_log.md` CONFLICT-03's own follow-up list, three weeks ago and still not resolved — a live example of exactly the drift risk this check targets |
| **Template status-disclosure check** | A generated document's template omitting the `status_disclosure: required` rendering for a `MODELLED`/`SCENARIO` field (see `DOCUMENT-GENERATION.md` §3) | Direct implementation of `rules/CLAUDE.md`'s founding incident: `investor-memorandum.md` showing a loss in its body table while a banner above claimed profitability — a generation-time check that a template's every data-bound field carries its status tag through to the rendered output is the structural fix |

---

## 4. Validation Cadence

| When | What runs |
|---|---|
| On every edit to `data/canonical/*.yml` (future, e.g. a pre-commit hook) | §1 schema/status validation |
| On every `models/*` run | §2.1 and §2.2 checks |
| On every document generation | §3 template status-disclosure check |
| Before any external conversation (investor, lease, partner, staff training) — **unchanged, existing rule** | `tools/check_consistency.py`, per `rules/CLAUDE.md` companion rule 4 |
| Periodic sweep (proposed cadence: whenever `CURRENT-STATE.md` is updated) | The full set — data, model, and documentation-layer checks together, since a `CURRENT-STATE.md` update is exactly the kind of event that historically caused cross-document drift in this repo |

---

## 5. What This Document Does Not Do

It does not implement a single validator. It does not modify `tools/check_consistency.py`'s code (only proposes, per §4 above, that its pattern list continue being extended as it already is, using its existing mechanism). It does not run any check against the current repo — every "real motivating example" cited above is drawn from what the existing manual review process (`01_conflicts_log.md`, `VERIFICATION-TRACKER.md`, `CURRENT-STATE.md`'s own changelogs) already found by hand, cited here to justify why each proposed automated check is worth building, not as a new finding from running a tool that doesn't exist yet.
