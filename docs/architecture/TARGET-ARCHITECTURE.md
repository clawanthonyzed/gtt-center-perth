# GTT Center Perth — Target Architecture

**Purpose:** Propose the future repository architecture that separates SOURCE MATERIAL → CANONICAL DATA → BUSINESS MODELS → DOCUMENT/REPORT OUTPUTS, so that a generated document can never become a source of truth. This document is a **proposal**, not an implementation — no directories described below are created by this phase (see `docs/architecture/REPOSITORY-AUDIT.md` for what exists today, and the final report's "Recommended next implementation step" for how this would actually get built).

**Naming decision:** the prompt's suggested layer names (`01_SOURCE` … `08_TOOLS`) are used here as **conceptual layer labels**, not literal directory names. This repo already has `docs/`, `rules/`, `tools/`, and `docs/archive/` doing real, working jobs — renaming them wholesale would be a large, disruptive rewrite for no functional gain, and is explicitly out of scope for this phase anyway. Instead, each conceptual layer below maps onto either an existing directory (extended, not renamed) or one new directory with a narrow, single-purpose job.

---

## 1. The Four-Layer Flow (non-negotiable)

```
SOURCE MATERIAL  -->  CANONICAL DATA  -->  BUSINESS MODELS  -->  DOCUMENT / REPORT OUTPUTS
   (evidence)          (facts, tagged)      (calculations)         (generated artifacts)
```

**The rule this exists to enforce:** a generated document (an XLSX, a DOCX, a PDF, an HTML dashboard) is never itself edited to "fix" a wrong figure, and never cited as the source of a fact. If a number in an output is wrong, the fix happens in CANONICAL DATA or BUSINESS MODELS, and the output is regenerated. This is the direct architectural answer to the failure mode `rules/CLAUDE.md` was created to stop by hand (see that file's "Why This Rule Exists" section) — the goal is to make the failure structurally harder to repeat, not just procedurally discouraged.

---

## 2. Layer-by-Layer Design

### Layer 1 — SOURCE (maps to: `docs/`, existing, extended)

**Purpose:** raw, unprocessed evidence — external correspondence, listings, regulatory documents, market research, primary-source citations. Source material is never a number itself; it's what a canonical fact *points to* as proof.

**Maps to existing:** `docs/wdp-reply-carole-*.md`, `docs/property-links-2026-07-28.md`, `docs/industry-standards-reference-2026-07-28.md`, `docs/market-research-findings.md`, `docs/research.md`, `docs/dva-tpi-research.md`, `docs/standards-floorplan-crosscheck-2026-07-28.md`, `docs/reference-floorplans-2026-07-28.md`. These stay exactly where they are — no move is proposed. What changes going forward: any new canonical fact added to Layer 2 must cite a specific file in this layer (or be tagged `PLACEHOLDER`/`DECIDED` if there is no external evidence — see `DATA-GOVERNANCE.md`).

**Does NOT include:** `docs/CURRENT-STATE.md` or `docs/VERIFICATION-TRACKER.md` — these are governance/index documents that sit across Layers 1–2, described below.

### Layer 2 — CANONICAL (maps to: new `data/canonical/` directory + existing `docs/CURRENT-STATE.md` + `docs/VERIFICATION-TRACKER.md`)

**Purpose:** the single set of facts the venture currently believes to be true, each carrying exactly one status tag (see `DATA-GOVERNANCE.md`). This is the layer nothing above it may bypass.

**Two representations of the same layer, kept deliberately in sync, not competing:**
- **`docs/CURRENT-STATE.md`** — the existing, human-readable, narrative canonical file. **Stays exactly as-is in role and location.** It remains the document a person reads to understand "what does this venture currently believe."
- **`data/canonical/*.yml`** (proposed, not built this phase) — the machine-readable counterpart, one file per domain (see `CANONICAL-DATA-SCHEMA.md`). This is what Layer 3 (models) and Layer 4 (document generation) actually read from programmatically. `CURRENT-STATE.md` would, in the target end-state, become a generated *rendering* of `data/canonical/*.yml` rather than an independently-maintained file — removing the last hand-maintained "two places to update the same number" risk. **This is a future-state description, not a change made this phase** — `CURRENT-STATE.md` keeps being hand-maintained until the data layer and a renderer both exist.
- **`docs/VERIFICATION-TRACKER.md`** — stays as-is; becomes the open-items ledger for gaps in the `data/canonical/` layer specifically (as well as its existing broader role), i.e. every `PLACEHOLDER`-tagged field in `data/canonical/*.yml` should have a matching row here.

**Governance:** `rules/CLAUDE.md` already governs this layer (the tagging rule) and needs no structural change — see `DATA-GOVERNANCE.md` for how its 3-status system reconciles with the fuller 7-status system this architecture proposes.

### Layer 3 — MODELS (new `models/` directory, not built this phase)

**Purpose:** the calculation logic that turns Layer 2 facts into derived figures — P&L, cash flow, break-even, capacity tables, rosters. Models read Layer 2, never Layer 1 directly, and never hardcode a fact that could instead be a Layer-2 reference.

**Three sub-areas**, detailed fully in `MODEL-ARCHITECTURE.md`:
- `models/financial/` — Master Financial Model. Maps to the calculation logic currently embedded in `docs/profit-loss-tables.md`, `docs/cash-flow.md`, `docs/break-even-sensitivity-analysis.md`, `docs/unit-economics.md`, `docs/financial-break-even-staff.md`.
- `models/operations/` — Master Operations Model (capacity, scheduling, timetables). Maps to `docs/scenario-c-sync-timetables.md`'s underlying method and, critically, to the six existing `tools/*.py` solver scripts — these scripts are the seed logic for this sub-area, currently living in `tools/` (Layer "Tools," below) because they were written as one-off checks rather than a reusable model. The target architecture treats them as the first draft of `models/operations/`, needing parameterization (reading scenario inputs from `data/canonical/` instead of hardcoded dicts) rather than a rewrite from scratch.
- `models/staffing/` — Staffing Model (FTE, payroll, rostering rules). Maps to `docs/staff-plan.md`, `docs/financial-break-even-staff.md`, `docs/am-staffing-by-volume.md`, and `tools/multirole-analysis.py`.

### Layer 4 — DOCUMENTS (new `documents/templates/` directory, not built this phase)

**Purpose:** the *specification* for each generated output document — what sections it has, which Layer-2/Layer-3 fields feed each section, what narrative/qualitative content (not derivable from data) it also needs. A template is not the output itself.

Full list of document types and their template-to-output mapping: `DOCUMENT-GENERATION.md`.

**Maps to existing:** every current hand-authored narrative document (`business-plan.md`, `executive-summary.md`, `investor-memorandum.md`, `feasibility.md`, `operations-manual.md`, etc.) is the *prior art* for what a template needs to cover — both its structure and its qualitative/narrative content (vision statements, market positioning language, risk narrative) which a data layer can never generate on its own. In the target end-state, the quantitative tables currently embedded by hand in these documents get replaced by references to Layer 2/3; the prose stays authored content that a template pulls in alongside the data. **These existing files are not rewritten this phase or implied to be replaced imminently** — see the Hard Constraints in the phase brief.

### Layer 5 — OUTPUTS (new `outputs/` directory, not built this phase)

**Purpose:** the actual generated artifacts — XLSX, DOCX, PDF, HTML, CSV. Every file here is regeneratable from Layers 2–4 and is never hand-edited. Proposed convention: timestamped or versioned subfolders (e.g. `outputs/2026-Q3/business-plan.pdf`) so a generated snapshot is never silently overwritten, and old outputs remain available for audit even after the underlying data changes. Git-tracking policy (commit binary outputs vs. `.gitignore` them and regenerate on demand) is an open implementation decision, not resolved by this architecture phase — flagged in the final report.

### Layer 6 — DASHBOARDS (new `dashboards/` directory, not built this phase)

**Purpose:** chart/KPI-dashboard specifications and their generated HTML/PNG outputs — a specialised subset of Layer 5 that gets its own directory because dashboards are typically regenerated far more often than formal documents (e.g. daily/weekly KPI refresh vs. a quarterly business plan). Maps to the existing `docs/scenario-c-sync-timeline.html` / `docs/scenario-c-timeline.html` as prior art (hand-built, not data-driven — the gap this layer closes).

### Layer 7 — ARCHIVE (maps to: `docs/archive/`, existing, unchanged)

**Purpose:** unchanged from today. Superseded source material, canonical-data snapshots, or old model versions get moved here via `git mv`, preserving history, per `rules/CLAUDE.md` companion rule 1. **No change proposed to this layer's role or location.**

### Layer 8 — TOOLS (maps to: `tools/`, existing, extended)

**Purpose:** generation and validation scripts — the code that reads Layers 2–3 and produces Layer 5 outputs, plus the code that checks consistency within and across all layers.

**Maps to existing:** `tools/check_consistency.py` (stays exactly as-is — the Layer-1/2 documentation-consistency sweep) plus the six scenario solver scripts (become the seed of `models/operations/` per Layer 3 above — a script can conceptually live in both places during a transition: `tools/` for "this is a script you run," `models/` for "this is the reusable calculation logic it's built from"). New scripts this architecture anticipates (not built this phase): a `data/canonical/` schema validator, a model-output reconciliation checker, and document generators — all detailed in `VALIDATION-ARCHITECTURE.md` and `DOCUMENT-GENERATION.md`.

---

## 3. Full Directory Map (Proposed End-State — Not Built This Phase)

```
gtt-center-perth/
├── CLAUDE.md, README.md, rules/CLAUDE.md      unchanged
├── agents/                                     unchanged — out of scope
├── .claude/skills/                             unchanged — out of scope
│
├── docs/                                       Layer 1 (SOURCE) + governance index — unchanged location
│   ├── CURRENT-STATE.md                          Layer 2 human-readable rendering (unchanged this phase)
│   ├── VERIFICATION-TRACKER.md                   Layer 2 open-items ledger (unchanged this phase)
│   ├── architecture/                             THIS deliverable set — new this phase
│   ├── archive/                                  Layer 7 (ARCHIVE) — unchanged
│   └── [~90 existing narrative/research/status files — untouched, reclassified only]
│
├── data/                        [NEW, not built this phase]  Layer 2 (CANONICAL) machine-readable layer
│   ├── canonical/                 *.yml per domain — see CANONICAL-DATA-SCHEMA.md
│   ├── sources/                   citation manifest: canonical field -> source file + status tag
│   └── schema/                    JSON Schema / YAML schema definitions validating canonical/*.yml
│
├── models/                      [NEW, not built this phase]  Layer 3 (MODELS)
│   ├── financial/                 assumptions -> revenue/COGS/payroll/opex -> P&L/cashflow/break-even
│   ├── operations/                 capacity/scheduling/timetable engine (evolves tools/*.py solvers)
│   └── staffing/                   FTE/payroll/roster-requirement engine
│
├── documents/                   [NEW, not built this phase]  Layer 4 (DOCUMENTS) — templates, not outputs
│   └── templates/                  one spec per output type — see DOCUMENT-GENERATION.md
│
├── outputs/                     [NEW, not built this phase]  Layer 5 (OUTPUTS) — generated artifacts only
│
├── dashboards/                  [NEW, not built this phase]  Layer 6 (DASHBOARDS)
│
└── tools/                                       Layer 8 (TOOLS) — existing, extended
    ├── check_consistency.py                       unchanged
    ├── draw-event-scheduler.py, multirole-analysis.py,
    │   scenario-d-staff-solver.py, scenario-d-staffing.py,
    │   sync-treatment-solver.py                    unchanged location; seed logic for models/operations/
    └── [future: schema validators, model-reconciliation checks, document generators]
```

---

## 4. Why This Mapping, Not a Wholesale Rename

Three reasons, all grounded in what the audit found rather than a general preference for minimal change:

1. **`docs/CURRENT-STATE.md` and `docs/VERIFICATION-TRACKER.md` are working, trusted, actively-maintained files with a real changelog and real governance behind them** (`rules/CLAUDE.md`). Moving or renaming them would break every existing in-repo hyperlink referencing them (dozens, per the audit) for zero functional benefit — the new `data/canonical/` layer sits *underneath* them, it doesn't replace their role.
2. **The six `tools/*.py` scripts are genuinely reusable seed logic, not disposable scratch work.** Moving them wholesale into `models/` before they're actually refactored to read from `data/canonical/` would be a cosmetic move that implies more architectural progress than has actually happened. They stay in `tools/` until the refactor (an implementation-phase task, not this phase) actually happens.
3. **`docs/archive/` already correctly implements Layer 7's role**, including git-history preservation via `git mv` — there is nothing to design here, only to keep using it as-is.

---

## 5. What This Document Does Not Do

- It does not create any of the new directories (`data/`, `models/`, `documents/`, `outputs/`, `dashboards/`) — see the final report's "Recommended next implementation step."
- It does not decide implementation technology (Python vs. a spreadsheet-native tool for `models/`; Jinja/docxtpl/openpyxl vs. something else for `documents/`+`outputs/`) — that is an implementation-phase decision, informed by but not made in this architecture phase.
- It does not move, rename, or edit a single existing file.
