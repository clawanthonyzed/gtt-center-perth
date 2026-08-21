"""
GTT Center Perth -- Cost Ramp Model (deterministic calculation module).

Rebuilds the Month 1-5+ cost ramp for Table 1 (18-client) and Table 2
(12-client) -- the cost-side counterpart to tools/revenue_ramp_model.py. Full
investigation and rationale: docs/architecture/COST-RAMP-METHODOLOGY.md.

This module contains NO unexplained hard-coded financial values. Every input
is either (a) read directly from data/canonical/*.yml by id, or (b) a named,
individually-cited constant sourced to a specific line in
docs/profit-loss-tables.md's own "Appendix -- How Every Figure Is Calculated"
or docs/CURRENT-STATE.md §5 -- the same pattern tools/revenue_ramp_model.py
uses for its RAMP_CURVE constant.

Does NOT calculate: Net P&L, EBITDA, cash balance, break-even, or any other
figure requiring revenue to be netted against costs -- cost side only, per
the coordinator's explicit financial-model boundary.

Usage:
    python tools/cost_ramp_model.py               # print both scenarios' cost ramp tables
    python tools/cost_ramp_model.py --scenario scenario_table_1
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

MONTHS = ["M1", "M2", "M3", "M4", "M5plus"]

# ---------------------------------------------------------------------------
# NAMED, CITED PAYROLL CONSTANTS -- each sourced to a specific, already-
# canonical line in docs/profit-loss-tables.md's Appendix or
# docs/CURRENT-STATE.md §5. None of these is invented; all are the venture's
# own already-published figures, reused here as first-principles calculation
# inputs (not restated financial "facts" -- see the STATUS field on each
# corresponding data/canonical/cost_ramp.yml record for governance status).
# ---------------------------------------------------------------------------

# AM Direct Labor (weekday) -- FTE-based, "UNCHANGED... same headcount,
# same fixed-salary roles" -- identical under both Table 1 and Table 2, and
# does NOT ramp (fixed headcount hired from Month 1 regardless of actual
# ramp-period booking volume -- see docs/architecture/COST-RAMP-METHODOLOGY.md
# §4 for the disclosed rationale/limitation of this treatment).
# Source: docs/CURRENT-STATE.md §5, "AM Direct Labor, both models -- UNCHANGED
# at A$48,254.67/month".
#
# SPLIT INTO TWO SUB-COMPONENTS (Phase 9 resume, 2026-08-09) -- required for
# correct superannuation treatment (see SUPERANNUATION_RATE_PCT below):
# docs/financial-break-even-staff.md's own "Award Wage Summary" table (lines
# 29-37) explicitly labels 6 of 7 roles' annual figures "incl. super"
# (Receptionist/Manager, Beauty therapist, Nail technician, Hairdresser,
# Massage therapist, PM Service Therapist) but does NOT apply that label to
# the Phlebotomist row ("A$43,068 (25hr/wk each)" -- no "incl. super" text).
# This is a real, disclosed asymmetry in the source document itself, not an
# inference -- the 8 treatment staff's annual salaries already include
# superannuation; the 2 phlebotomists' annual salary (A$86,136/yr total)
# does not.
# RECOMPUTED 2026-08-17, per direct instruction to propagate the 2026-08-16
# wage/award research through the canonical model, not leave it researched-
# but-unpropagated. METHOD: proportional scaling -- the exact per-staff-
# member hour allocation behind the old A$41,076.67/A$7,178.00 figures is
# NOT preserved as a rebuildable worksheet anywhere in this repo (confirmed
# directly, docs/profit-loss-tables.md's own Appendix: "the specific per-
# staff-member hour allocation behind the exact total is not saved as a
# standalone worksheet in this repo"). Rebuilding it from scratch against
# scenario-c-sync-timetables.md's per-client service-time entries is a
# genuinely separate, larger task, not attempted here (would risk silently
# inventing a schedule reconstruction not independently verified this pass).
# Instead: each role's OLD casual rate -> NEW casual rate (financial-break-
# even-staff.md, researched 2026-08-16) gives a defensible, disclosed scale
# factor, applied to the existing dollar total. This is the SAME proportional-
# scaling method this file already uses elsewhere (e.g. AM_SATURDAY_DAILY_LABOR
# below), not a new methodology invented for this recompute.
#   Treatment staff (8): 4x Massage+Beauty (old $37.00/hr -> new $37.50/hr)
#     + 2x Nails (old $35.63/hr -> new $36.81/hr) + 2x Hair (same as Nails).
#     Old weighted-hourly sum = 4(37.00)+2(35.63)+2(35.63) = 290.52
#     New weighted-hourly sum = 4(37.50)+2(36.81)+2(36.81) = 297.24
#     Scale factor = 297.24 / 290.52 = 1.023133
#   Phlebotomists (2): old $30.63/hr -> new SS Level 1-2 range $33.71-35.04/hr,
#     midpoint $34.375/hr used as the single defensible new rate (the old
#     figure was also a single rate, not a range).
#     Scale factor = 34.375 / 30.63 = 1.122266
# RECOMPUTED 2026-08-17 (Phase C) -- REPLACES the 2026-08-17-earlier
# proportional-scaling method entirely, per explicit instruction to stop
# scaling and rebuild from first principles instead. Full derivation:
# docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md §3. Method: position
# -> headcount -> hours/shift (07:00-13:00 = 6hrs, AM window) -> operating
# days (22 weekdays/month) -> current researched casual rate -> monthly
# total. No early-release saving assumed in this headline figure (the
# conservative, full-shift planning basis) -- early-release remains a
# separate, disclosed, tagged upside (docs/CURRENT-STATE.md §8), not blended
# in here.
#   Treatment (8): 4x Massage+Beauty @ $37.50/hr x 6hrs x 22 days = $19,800.00
#     + 2x Nails @ $36.81/hr x 6hrs x 22 days = $9,717.84
#     + 2x Hair @ $36.81/hr x 6hrs x 22 days = $9,717.84
#     = $39,235.68/month
#   Phlebotomists (2): $34.375/hr (SS Level 1-2 midpoint) x 6hrs x 22 days
#     x 2 people = $9,075.00/month
AM_WEEKDAY_TREATMENT_STAFF_MONTHLY = 39235.68   # was A$42,027.66 (proportional-scaled) -> first-principles A$39,235.68
AM_WEEKDAY_PHLEBOTOMIST_MONTHLY = 9075.00        # was A$8,055.97 (proportional-scaled) -> first-principles A$9,075.00
AM_WEEKDAY_DIRECT_LABOR_MONTHLY = round(AM_WEEKDAY_TREATMENT_STAFF_MONTHLY + AM_WEEKDAY_PHLEBOTOMIST_MONTHLY, 2)  # was A$50,083.63 -> A$48,310.68

# AM Direct Labor (Saturday) -- hours-based, scales with the scenario's
# COMMITTED client volume (not the ramp-period actual volume, which has no
# documented rostering methodology anywhere in this repo -- see COST-RAMP-
# METHODOLOGY.md §4). Source: docs/profit-loss-tables.md §2 (old model, now
# historical) and the PRIMARY REBASED MODEL section (Table 1).
# RECOMPUTED 2026-08-17 (Phase C, first principles). Table 1: 8 treatment
# staff + 2 phlebotomists, same 6hr shift as weekday, x1.5 Saturday penalty
# (MA000005/MA000027 casual Saturday rate, researched 2026-08-16):
#   Treatment Saturday: (4x$56.25 + 2x$55.215 + 2x$55.215)/hr x 6hrs = $2,675.16/day
#   Phlebotomist Saturday: 2 x $51.5625/hr x 6hrs = $618.75/day
#   Table 1 combined = $3,293.91/day
# Table 2: no separately-rebuilt Saturday schedule exists for the shorter
# 08:00-start cadence this pass -- the OLD model's own disclosed Table1:
# Table2 Saturday ratio (1612.74/2419.11 = 0.6667, reflecting Table 2's
# shorter Saturday schedule) is reapplied to the new Table 1 figure as a
# disclosed, reused approximation, not a fresh derivation -- flagged as a
# genuine simplification, not fabricated precision.
AM_SATURDAY_DAILY_LABOR = {
    "scenario_table_1": 3293.91,                          # was 2,510.80 (proportional-scaled) -> first-principles 3,293.91
    "scenario_table_2": round(3293.91 * 0.6667, 2),        # was 1,673.87 -> 2,196.05 (reused ratio, disclosed approximation)
}

# RENAMED IN SUBSTANCE 2026-08-17 (Phase C, first principles) -- this field
# retains its original YAML key name ("opening_time_increment") for backward
# structural compatibility, but its VALUE and MEANING are now the Venue
# Manager's real, first-principles daily labour cost (position 01,
# docs/architecture/STAFF-PROFILES.md), not the old vague "opening-time
# increment" concept.
#
# CORRECTED 2026-08-18 (Phase C audit round) -- AWARD RECLASSIFICATION.
# The Phase C figure ($36.81/hr, Clerks Award MA000002 Level 2) was audited
# and found to be a likely misclassification, not verified against the
# actual duties. STAFF-PROFILES.md's own Position 01 job description
# ("runs daily venue operations, manages staff rostering and performance...
# a genuine service qualification required") matches the Hair & Beauty
# Industry Award MA000005's OWN Level 6 classification far more closely --
# MA000005 Level 6 is explicitly "Diploma-qualified beauty therapist or
# salon manager responsible for staff and operations" (researched
# 2026-08-18, rosterelf.com/guides/award-rates/hair-beauty, cross-checked
# against fairwork.gov.au's MA000005 award-classification framework; NOT
# independently confirmed against the primary Fair Work Ombudsman award
# text itself this pass -- WorkCover/FWO PDF sources returned 403 Forbidden
# to automated fetch, a genuine tooling limitation, not skipped). MA000005
# Level 6 casual rate: $40.00/hr (2026/27, includes 25% casual loading) --
# HIGHER than the previously-used Clerks Award L2 rate ($36.81/hr).
# STATUS: MODELLED/CORRECTED, NOT VERIFIED -- this is the best-evidenced
# classification found this pass, applied because the VM's own real duties
# (service-qualified, salon-operations-managing) match MA000005 L6's
# definition far better than a generic clerical award, but a Fair Work
# award-classification decision for a specific real employment contract
# should still be confirmed with an accountant/HR professional before being
# treated as final -- flagged explicitly, not silently upgraded to VERIFIED.
# VM: 1 x 8hrs x $40.00/hr (MA000005 L6 casual) = $320.00/day (weekday
# basis; Saturday handled separately in compute_payroll via the same x1.5
# penalty pattern as other roles).
OPENING_TIME_INCREMENT_DAILY = 320.00   # was A$44.50 (undocumented) -> A$294.48 (Phase C, Clerks Award L2, likely misclassified) -> A$320.00 (Phase C audit, MA000005 L6, corrected classification)
VENUE_MANAGER_SATURDAY_DAILY = round(320.00 * 1.5, 2)  # $480.00/day, x1.5 Saturday penalty

# REMOVED 2026-08-21 (Founder Decision round), per Anthony's direct
# instruction, overriding docs/architecture/STAFFING-COVERAGE-VALIDATION.md
# section 4's prior Model A recommendation: PM Reception is no longer a
# dedicated position (Position 06/RCO01). The confirmed model is Model C
# ("service-staff coverage during booking gaps") -- rostered PM treatment
# staff (PMM01/PMH01/PMN01/PMB01) handle check-in/payment/Fresha admin
# during natural gaps in their own PM session bookings, already paid for
# via pm_weekday_direct_labor/pm_saturday_direct_labor below -- no separate
# payroll line. Kept at 0.00, not deleted, for schema stability and trace.
# See docs/architecture/STAFFING-COVERAGE-VALIDATION.md section 4 (updated,
# not rewritten) for the full superseded reasoning and the founder-decision
# override, and docs/architecture/DEMAND-DRIVEN-STAFFING-MODEL.md section 5
# for this round's full disclosure.
#
# PRE-2026-08-21 VALUE (retained for trace, not deleted): "RENAMED IN
# SUBSTANCE 2026-08-17 (Phase C, first principles) -- retains its original
# YAML key name ("receptionist_relief") for backward structural
# compatibility, but its VALUE and MEANING are now the PM Reception/
# Coordinator's real, first-principles daily labour cost (position 06,
# docs/architecture/STAFF-PROFILES.md), replacing the old unclear "~A$339/day"
# approximation. PM Reception: 1 x 5hrs x $33.71/hr (MA000002 L1) = $168.55/day."
# Was 168.55/day weekday (was ~A$339.00 unclear approximation before that),
# 253.83/day Saturday (x1.5 penalty).
RECEPTIONIST_RELIEF_WORKERS_COMP_DAILY = 0.00   # was A$168.55/day (Position 06/RCO01, first-principles) -> A$0.00 (Position 06 removed, 2026-08-21 founder decision)
PM_RECEPTION_SATURDAY_DAILY = 0.00   # was A$252.83/day (x1.5 Saturday penalty on A$168.55) -> A$0.00, same reason

# PM Direct Labor (Saturday) -- fixed regardless of ramp, because even at the
# full 8-session/day steady-state PM Saturday volume, hours/role/day
# (8 / 4 roles / 1.3 sessions/hr = 1.54hrs) is already below the 3-hour
# casual-minimum-engagement floor (wages.yml#wage_casual_minimum_engagement,
# VERIFIED) -- so PM Saturday labor cannot fall below this floor amount at
# ANY session-count ramp assumption, making the ramp question moot for this
# specific cost. Source: docs/profit-loss-tables.md §2's 3-hour-minimum
# correction note (A$654.32/day, backed-out blended Saturday casual rate
# A$54.53/hr).
# RECOMPUTED 2026-08-17 (Phase C, first principles) -- 4 PM roles x 3hr
# minimum-engagement floor (8 Saturday sessions/4 roles/1.3 throughput =
# 1.54hrs, below the floor) x $55.7325/hr (blended current rate x1.5
# Saturday penalty) = docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md §3e.
PM_SATURDAY_DAILY_LABOR = 668.78  # was 669.46 (proportional-scaled) -> first-principles 668.78, materially unchanged

# PM Direct Labor (weekday) -- genuinely ramps, per the session-count curve
# below and the 3-hour casual-minimum-engagement floor. Blended weekday
# casual rate = average of the 4 PM roles' casual rates
# (wages.yml#wage_massage_therapist/wage_beauty_therapist = A$37.00/hr,
# wages.yml#wage_nail_technician/wage_hairdresser = A$35.63/hr).
# RECOMPUTED 2026-08-17 -- current researched casual rates (financial-break-
# even-staff.md, 2026-08-16): Massage/Beauty $37.50/hr, Nails/Hair $36.81/hr.
PM_WEEKDAY_BLENDED_CASUAL_RATE = (37.50 + 37.50 + 36.81 + 36.81) / 4  # was 36.315 -> 37.155
PM_ROLES = 4
PM_THROUGHPUT_SESSIONS_PER_HOUR = 1.3  # docs/pm-staffing-roster.md, established elsewhere in this repo
CASUAL_MINIMUM_ENGAGEMENT_HOURS = 3.0  # wages.yml#wage_casual_minimum_engagement, VERIFIED

# PM session-count ramp -- REUSED from data/canonical/revenue_assumptions.yml's
# rev_pm_session_ramp_historical (docs/pm-staffing-roster.md's own PM staffing
# table), NOT the blanket 43/64/79/93/100% revenue-ramp curve. This is the
# one genuine, disclosed departure from "reuse the revenue ramp for costs" --
# justified because PM labor cost is a DIRECT function of session count via
# the hours-based costing formula already established in
# docs/pm-staffing-roster.md, whereas the blanket curve was built for revenue
# specifically. See docs/architecture/COST-RAMP-METHODOLOGY.md §5.
PM_SESSION_RAMP = {"M1": 4, "M2": 8, "M3": 12, "M4": 15, "M5plus": 16}

# Month 5+ PM weekday daily labor is anchored to the already-canonical,
# independently-verified A$440.00/day figure (docs/profit-loss-tables.md §1),
# NOT to this module's own formula output (which gives ~A$446.95/day -- the
# repo's own Appendix already discloses this exact "within rounding, not
# exact" gap for the identical calculation, a pre-existing imprecision, not
# introduced here).
# RECOMPUTED 2026-08-17 (Phase C, first principles) -- 4 PM roles x 3.08hrs/role
# (16 weekday sessions/4 roles/1.3 throughput, clears the 3hr floor) x
# $37.155/hr (blended current rate) = docs/architecture/FIRST-PRINCIPLES-
# FINANCIAL-MODEL.md §3e.
PM_WEEKDAY_M5PLUS_DAILY_LABOR_CANONICAL_ANCHOR = 457.75  # was 450.18 (proportional-scaled) -> first-principles 457.75

WORKERS_COMP_RATE_PCT = 1.7  # wages.yml#wage_workers_comp_rate, MODELLED

# ---------------------------------------------------------------------------
# SUPERANNUATION (Phase 9 resume, 2026-08-09) -- data/canonical/wages.yml's
# wage_superannuation_rate (12% of Ordinary Time Earnings, MODELLED), applied
# here for the first time to the ACTUAL payroll figures -- previously the
# rate existed in wages.yml but was never applied anywhere in this repo's
# payroll modelling (docs/VERIFICATION-TRACKER.md item 46).
#
# INCLUSIVE/EXCLUSIVE TREATMENT -- read directly off
# docs/financial-break-even-staff.md's own Award Wage Summary table, not
# inferred or invented:
#   - AM Weekday Direct Labor, TREATMENT STAFF portion (A$41,076.67/month):
#     ALREADY INCLUDES super, per that table's explicit "incl. super" label
#     on 6 of 7 roles (Beauty/Massage/Nail/Hair/PM Service Therapist/
#     Receptionist-Manager) -- no super added here, adding it again would
#     double-count.
#   - AM Weekday Direct Labor, PHLEBOTOMIST portion (A$7,178.00/month): does
#     NOT include super -- that table's Phlebotomist row states "A$43,068
#     (25hr/wk each)" with no "incl. super" text, a real, disclosed asymmetry
#     in the source itself. Super IS added here.
#   - AM Saturday, PM Weekday, PM Saturday Direct Labor: all built from the
#     raw hourly `casual_loaded` award rate (e.g. A$37.00/hr), which the
#     source table's own structure treats as EXCLUSIVE of super (super only
#     appears once the figure is annualised into a fully-loaded package cost)
#     -- super IS added here, on top of the hours-based calculation.
#   - Opening-time increment, Receptionist/Relief Pool: these are bundled,
#     non-role-specific operational figures (the Receptionist/Relief figure
#     is itself only an approximate "~A$339.00/day" per docs/profit-loss-
#     tables.md's own Appendix, not cleanly decomposable back to the
#     Receptionist's own annual salary) -- super treatment for these two
#     components is genuinely UNRESOLVED, not guessed at. No super is added
#     to them. See conflict_superannuation_partial_coverage in cost_ramp.yml.
#
# ELIGIBILITY RULE: not stated anywhere in this repo's canonical or source
# documents (no minimum-earnings threshold, no age threshold is mentioned).
# This module therefore applies the 12% rate universally to every eligible
# wage component above, without any earnings-threshold carve-out -- flagged
# as an unconfirmed assumption, not independently verified against current
# Australian SG eligibility rules (which this module does not attempt to
# state as fact).
# ---------------------------------------------------------------------------
SUPERANNUATION_RATE_PCT = 12.0  # wages.yml#wage_superannuation_rate, MODELLED

# GTT supplies variable-alternative rate -- opex.yml#opex_gtt_supplies' own
# stated basis ("200 tests x A$2"), reused here per-test, per-day (weekday
# only, matching that record's own already-disclosed "~A$792/month at 396
# tests" estimate methodology exactly -- not a new assumption).
GTT_SUPPLIES_PER_TEST_RATE = 2.00


def load_yaml(filename):
    path = CANON_DIR / filename
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_record(records, record_id):
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


class CanonicalCostInputs:
    """Every purely-canonical (non-hard-coded) input this module needs, read
    by id from data/canonical/*.yml."""

    def __init__(self):
        client_assumptions = load_yaml("client_assumptions.yml")
        scenarios = load_yaml("scenarios.yml")
        opex = load_yaml("opex.yml")

        universal = client_assumptions["universal"]
        self.operating_days_weekday = find_record(universal, "operating_days_per_month_weekday")["value"]
        self.operating_saturdays = find_record(universal, "operating_saturdays_per_month")["value"]

        scenario_records = scenarios["records"]
        self.client_volume = {
            "scenario_table_1": find_record(scenario_records, "scenario_table_1")["client_volume"]["value"],
            "scenario_table_2": find_record(scenario_records, "scenario_table_2")["client_volume"]["value"],
        }

        opex_records = opex["records"]
        self.marketing_ramp = find_record(opex_records, "opex_marketing_ads_ramp")["amount"]
        self.marketing_steady_state = find_record(opex_records, "opex_marketing_ads_steady_state")["amount"]

        # Fixed Non-Wage Overhead = the full A$13,980.00/month canonical total
        # (docs/profit-loss-tables.md §4) minus the marketing line, which is
        # the ONE component with a documented, sourced Month 1-4 ramp
        # (opex_marketing_ads_ramp above). No other opex.yml record has a
        # stated ramp anywhere in this repo -- reused at face value, FIXED
        # from Month 1, including the 3 records under the disclosed, UNRESOLVED
        # FIXED-vs-VARIABLE classification conflict (opex_gtt_supplies,
        # opex_consumables_general, opex_laundry) -- this module does NOT
        # resolve that conflict, it carries forward the status-quo FIXED
        # classification already in opex.yml's own cost_type field, per the
        # coordinator's explicit "don't resolve just to make the model run"
        # instruction. See gtt_supplies_variable_alternative() below for the
        # disclosed, non-primary exploratory alternative.
        # CORRECTED 2026-08-18 (Financial Finalisation round) -- insurance
        # line investigated, not blindly preserved. The old A$400.00/month
        # figure (docs/profit-loss-tables.md §4) was an unexplained round
        # guess. A later "revised placeholder" of A$1,279.00/month
        # (opex.yml#opex_insurance_modelled, 2026-08-16) was found this round
        # to be methodologically flawed: it was the midpoint of an $11,700-
        # 19,000/year sum that DOUBLE-COUNTS workers compensation (already
        # charged separately as 1.7% of direct labour below -- the insurance-
        # bucket's own workers-comp cross-reference line is explicitly
        # labelled "NOT the modelled figure" in opex.yml, yet was summed in
        # anyway) and includes an explicitly-OPTIONAL business-interruption
        # line as if it were committed. CORRECTED: Public Liability
        # (A$2,500-4,500/yr) + Professional Indemnity (A$2,000-4,000/yr) +
        # Property/Contents (A$1,500-2,500/yr) = A$6,000-11,000/yr =
        # A$500.00-916.67/month, midpoint A$708.34/month -- externally
        # sanity-checked against real 2026 Australian small-business PL/PI
        # premium research (this venture's higher-risk client profile,
        # pregnant clients + health-adjacent services, justifies sitting
        # above generic small-business averages). STATUS: MODELLED/BALLPARK-
        # ESTIMATE, NOT VERIFIED -- real broker quotes already in motion,
        # docs/insurance-broker-quote-request-draft.md. Old total A$13,980.00
        # (embedding A$400 insurance) -> new A$14,288.34 (embedding A$708.34).
        total_nonwage = 14288.34  # docs/architecture/FINANCIAL-ASSUMPTION-REGISTER.md -- insurance corrected, was 13980.00 (embedded A$400 insurance placeholder)
        self.fixed_nonwage_excl_marketing = round(total_nonwage - self.marketing_steady_state, 2)

        # NEW 2026-08-18 (Financial Finalisation round) -- Relief/Absence
        # Coverage Allowance. Previously, this cost model priced ONLY the
        # committed simultaneous roster (8 treatment + 2 phlebotomists + 1 VM
        # + 1 PM Reception) working every trading day with zero absences --
        # unrealistic. This allowance is a real, quantified, disclosed
        # planning figure for the EXPECTED cost of relief staff actually
        # covering absences, using an 8% per-person per-shift unavailability
        # planning assumption (STATUS: MODELLED/BALLPARK-ESTIMATE -- a
        # commonly-cited casual-hospitality/beauty planning range, NOT
        # independently verified against real data for this pre-opening
        # venture -- docs/architecture/STAFFING-COVERAGE-VALIDATION.md §1a)
        # and FULL-SHIFT replacement (not the bare 3-hour casual-minimum-
        # engagement floor -- a relief person covering a colleague's full
        # rostered shift realistically works the full shift, not the legal
        # minimum). Treatment: 8 committed x 8% x (22 weekday + 4.33
        # Saturday) = 16.85 expected relief-shifts/month x 6hrs x blended
        # A$37.155/hr (weekday) / A$55.7325/hr (Saturday, x1.5) =
        # A$4,065.53/month. Phlebotomists: 2 x 8% x same days = 4.21 shifts
        # x 6hrs x A$34.375/hr (A$51.5625 Saturday) = A$940.34/month. PM
        # Reception: 1 x 8% x same days = 2.11 shifts x 5hrs x A$33.71/hr
        # (A$50.565 Saturday) = A$384.23/month. Subtotal A$5,390.09/month +
        # 12% super (A$646.81) + 1.7% workers comp (A$91.63) = TOTAL
        # A$6,128.53/month. Modelled as its OWN recurring opex line (not
        # blended into Direct Labour), per the explicit decision in
        # docs/architecture/FINANCIAL-ASSUMPTION-REGISTER.md: an expected-
        # value planning allowance is the defensible treatment for a real,
        # recurring-in-aggregate (even though individually stochastic) cost,
        # same convention as budgeting a maintenance/contingency reserve --
        # kept visibly separate so the committed-roster Direct Labour figure
        # is never confused with the full realistic cost base.
        # REVERTED 2026-08-21 (Financial Model Rebuild round), per direct
        # founder instruction: absence/relief coverage is treated as already
        # absorbed within normal payroll (the committed roster's own casual/
        # relief hiring, not a separate expected-value planning line stacked
        # on top of it) unless a genuine, itemised cost basis for a SEPARATE
        # line is identified. No such separate basis has been identified --
        # the A$6,128.53/month figure above was itself a modelled planning
        # allowance (8% per-person unavailability x full-shift replacement),
        # not a real invoiced or contracted cost. Kept here, at 0.00, rather
        # than deleted, so the full prior derivation (still printed in the
        # comment block above this line) remains readable for trace, per
        # this repo's "never delete history, mark superseded" convention.
        # See conflict_relief_absence_allowance_reverted in cost_ramp.yml.
        self.relief_absence_allowance = 0.00


def compute_pm_weekday_daily_labor(month):
    """PM Direct Labor (weekday), per session-count ramp + 3-hour casual
    minimum floor. Month5plus is anchored to the canonical figure (see
    PM_WEEKDAY_M5PLUS_DAILY_LABOR_CANONICAL_ANCHOR's own docstring)."""
    if month == "M5plus":
        return PM_WEEKDAY_M5PLUS_DAILY_LABOR_CANONICAL_ANCHOR
    sessions = PM_SESSION_RAMP[month]
    hours_per_role = max(
        CASUAL_MINIMUM_ENGAGEMENT_HOURS,
        sessions / PM_ROLES / PM_THROUGHPUT_SESSIONS_PER_HOUR,
    )
    return round(hours_per_role * PM_ROLES * PM_WEEKDAY_BLENDED_CASUAL_RATE, 2)


def compute_payroll(scenario_id, month, inputs: CanonicalCostInputs):
    """Returns a dict of payroll components for one (scenario, month).

    RESTRUCTURED 2026-08-17 (Phase C, first principles). Two methodology
    changes from the pre-2026-08-17 version, both disclosed:
    (1) opening_increment/receptionist_relief now carry real Saturday-penalty
        components (Venue Manager / PM Reception, docs/architecture/
        STAFF-PROFILES.md), not just a flat weekday-only figure.
        UPDATED 2026-08-21: receptionist_relief is now 0.00 -- Position 06/
        RCO01 (dedicated PM Reception) was removed per Anthony's direct
        founder decision, superseding STAFFING-COVERAGE-VALIDATION.md
        section 4's prior Model A recommendation. PM reception duties are
        now covered by rostered PM treatment staff during booking gaps
        (already paid for via pm_weekday_direct_labor/pm_saturday_direct_labor),
        not a separate payroll line. opening_increment (Venue Manager) is
        unaffected -- AM reception remains VM01's role.
    (2) Superannuation is now applied UNIVERSALLY (12%) to every wage
        component, not just the previously-confirmed-exclusive subset -- a
        cleaner, more defensible treatment than the prior partial-coverage
        approach, per docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md
        §3g. This is a genuine methodology simplification, disclosed, not a
        silent change -- see conflict_superannuation_partial_coverage in
        cost_ramp.yml for the historical partial-coverage record, retained
        for trace.
    """
    am_weekday_treatment = AM_WEEKDAY_TREATMENT_STAFF_MONTHLY
    am_weekday_phlebotomist = AM_WEEKDAY_PHLEBOTOMIST_MONTHLY
    am_weekday = round(am_weekday_treatment + am_weekday_phlebotomist, 2)
    am_saturday = round(AM_SATURDAY_DAILY_LABOR[scenario_id] * inputs.operating_saturdays, 2)
    pm_weekday_daily = compute_pm_weekday_daily_labor(month)
    pm_weekday = round(pm_weekday_daily * inputs.operating_days_weekday, 2)
    pm_saturday = round(PM_SATURDAY_DAILY_LABOR * inputs.operating_saturdays, 2)
    opening_increment = round(
        OPENING_TIME_INCREMENT_DAILY * inputs.operating_days_weekday
        + VENUE_MANAGER_SATURDAY_DAILY * inputs.operating_saturdays, 2
    )
    receptionist_relief = round(
        RECEPTIONIST_RELIEF_WORKERS_COMP_DAILY * inputs.operating_days_weekday
        + PM_RECEPTION_SATURDAY_DAILY * inputs.operating_saturdays, 2
    )

    direct_labor_and_opening = round(
        am_weekday + am_saturday + pm_weekday + pm_saturday + opening_increment + receptionist_relief, 2
    )
    workers_comp = round(direct_labor_and_opening * WORKERS_COMP_RATE_PCT / 100, 2)

    # Superannuation -- applied universally (12%) to every wage component,
    # per the methodology change disclosed in this function's own docstring.
    superannuation = round(direct_labor_and_opening * SUPERANNUATION_RATE_PCT / 100, 2)

    payroll_total = round(direct_labor_and_opening + workers_comp + superannuation, 2)

    return {
        "am_weekday_direct_labor": am_weekday,
        "am_weekday_treatment_staff": round(am_weekday_treatment, 2),
        "am_weekday_phlebotomist": round(am_weekday_phlebotomist, 2),
        "am_saturday_direct_labor": am_saturday,
        "pm_weekday_direct_labor": pm_weekday,
        "pm_saturday_direct_labor": pm_saturday,
        "opening_time_increment": opening_increment,
        "receptionist_relief": receptionist_relief,
        "direct_labor_and_opening_total": direct_labor_and_opening,
        "superannuation": superannuation,
        "workers_comp": workers_comp,
        "payroll_total": payroll_total,
    }


def compute_fixed_and_variable_opex(month, inputs: CanonicalCostInputs):
    """Fixed Costs = Non-Wage Overhead excl. marketing (unchanged Month 1-5+).
    Variable Costs = marketing spend ramp (the only opex.yml component with a
    documented, sourced monthly ramp)."""
    fixed = inputs.fixed_nonwage_excl_marketing
    variable = inputs.marketing_ramp[f"month_{MONTHS.index(month) + 1}"] if month != "M5plus" else inputs.marketing_steady_state
    return round(fixed, 2), round(variable, 2)


def gtt_supplies_variable_alternative(scenario_id, month, inputs: CanonicalCostInputs, ramp_curve):
    """Exploratory, NON-PRIMARY calculation: what GTT supplies would cost if
    treated as VARIABLE (per-test) instead of the current FIXED A$400.00/month
    modelled figure -- investigating, not resolving,
    conflict_variable_vs_fixed_classification (opex.yml). Uses
    opex_gtt_supplies' own stated basis (A$2/test), applied to weekday-only
    test volume at the ramp-period's implied client volume -- matching that
    record's own already-disclosed "~A$792/month at 396 tests" methodology
    exactly, not a new assumption."""
    pct = dict(ramp_curve)[month]
    client_volume = inputs.client_volume[scenario_id] * pct / 100
    tests_per_month = client_volume * inputs.operating_days_weekday
    return round(tests_per_month * GTT_SUPPLIES_PER_TEST_RATE, 2)


def compute_ramp(scenario_id, inputs: CanonicalCostInputs, revenue_ramp_curve):
    months_out = []
    for month in MONTHS:
        payroll = compute_payroll(scenario_id, month, inputs)
        fixed, variable = compute_fixed_and_variable_opex(month, inputs)
        relief = inputs.relief_absence_allowance
        # REVERTED 2026-08-21 -- relief_absence_allowance is now 0.00 (see
        # CanonicalCostInputs.relief_absence_allowance's own comment for the
        # full reasoning). Was added 2026-08-18 as a separate expected-value
        # planning line; removed per direct founder instruction that normal
        # payroll/rostering should absorb absence coverage unless a genuine,
        # itemised separate cost basis exists. The dict key is kept (at 0.00)
        # for schema stability and trace, not deleted.
        total = round(fixed + variable + payroll["payroll_total"] + relief, 2)
        months_out.append(
            {
                "scenario_id": scenario_id,
                "month": month,
                "fixed_costs": fixed,
                "variable_costs": variable,
                "payroll_costs": payroll["payroll_total"],
                "relief_absence_allowance": relief,
                "total_operating_costs": total,
                "payroll_detail": payroll,
                "gtt_supplies_variable_alternative": gtt_supplies_variable_alternative(
                    scenario_id, month, inputs, revenue_ramp_curve
                ),
            }
        )
    return months_out


# Default revenue ramp curve, imported lazily to avoid a hard dependency at
# module-load time if revenue_ramp_model.py is ever moved -- mirrors
# tools/revenue_ramp_model.py's own RAMP_CURVE exactly (used here ONLY for
# the GTT-supplies variable-alternative's implied-client-volume calculation,
# NOT applied to payroll or any other cost -- see
# docs/architecture/COST-RAMP-METHODOLOGY.md §5 for why costs do NOT
# automatically inherit the revenue ramp).
DEFAULT_REVENUE_RAMP_CURVE = [("M1", 43), ("M2", 64), ("M3", 79), ("M4", 93), ("M5plus", 100)]


def compute_all():
    inputs = CanonicalCostInputs()
    return {
        "scenario_table_1": compute_ramp("scenario_table_1", inputs, DEFAULT_REVENUE_RAMP_CURVE),
        "scenario_table_2": compute_ramp("scenario_table_2", inputs, DEFAULT_REVENUE_RAMP_CURVE),
    }


def _print_table(scenario_id, months):
    print(f"\n{scenario_id}")
    print(f"{'Month':<8}{'Fixed':>12}{'Variable':>12}{'Payroll':>14}{'Total OpEx':>14}")
    for m in months:
        print(
            f"{m['month']:<8}{m['fixed_costs']:>12,.2f}{m['variable_costs']:>12,.2f}"
            f"{m['payroll_costs']:>14,.2f}{m['total_operating_costs']:>14,.2f}"
        )


def main(argv):
    all_results = compute_all()
    if "--scenario" in argv:
        idx = argv.index("--scenario")
        target = argv[idx + 1]
        _print_table(target, all_results[target])
    else:
        for scenario_id, months in all_results.items():
            _print_table(scenario_id, months)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
