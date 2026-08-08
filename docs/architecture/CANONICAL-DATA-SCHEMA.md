# GTT Center Perth — Canonical Data Schema (Design Sketch)

**Purpose:** design the shape of `data/canonical/*.yml` — the machine-readable counterpart to `docs/CURRENT-STATE.md` (see `TARGET-ARCHITECTURE.md` Layer 2). **These are schema sketches, not populated data.** No field below is filled with an invented value. Where a real value already exists in a source document, this file names that source document/section next to the field instead of restating the number — per the phase's hard constraint not to invent or silently resolve data, and to keep this a schema design, not a data-migration.

**Status:** none of these YAML files exist in the repo yet. This document is the design that a future implementation phase would build against.

---

## 0. Common Envelope (used by every domain file)

Every record in every `data/canonical/*.yml` file uses the same envelope, so a single schema validator and a single renderer (the future `CURRENT-STATE.md` generator, see `TARGET-ARCHITECTURE.md`) can process all of them uniformly.

```yaml
# Common record envelope
- id: <unique_snake_case_id>            # stable identifier, referenced by models/ and documents/
  domain: <this file's domain name>      # e.g. "pricing", "staffing"
  value: <the actual figure/fact>        # NOT populated in this design phase — see per-file notes
  unit: <A$ | count | percent | minutes | ...>
  status: <VERIFIED | DECIDED | CALCULATED | MODELLED | SCENARIO | PLACEHOLDER | SUPERSEDED>
  status_detail: <free text — e.g. "assumption: 50% utilisation">   # required if status is MODELLED
  source: <path to the docs/ file this fact is drawn from>
  source_section: <section/table reference within that file, if applicable>
  verified_by: <name/role, or null>
  verified_date: <YYYY-MM-DD, or null>
  superseded_by: <id of the record that replaces this one, or null>   # required if status is SUPERSEDED
  effective_date: <YYYY-MM-DD — when this fact became true/adopted>
  notes: <free text>
```

See `DATA-GOVERNANCE.md` for the full meaning of each `status` value and the rules governing which documents may draw on which statuses.

---

## 1. `data/canonical/business.yml` — Business Info

```yaml
# Sketch — fields only, no values populated.
- id: entity_name
  value: <e.g. "GTT Center Perth" — currently a working placeholder, not locked>
  source: docs/CURRENT-STATE.md / rules/CLAUDE.md standing facts
  status: DECIDED   # placeholder-naming is itself a decision, not a placeholder fact
- id: legal_entity
  value: <YETI Holding Trust / YETI Tipi Holdings PTY LTD as corporate trustee>
  source: C:\Users\azed9\CLAUDE.md (empire-level) / docs/financial-model.md
- id: funding_source
  value: <self-funded, Anthony + Imara joint savings>
  source: rules/CLAUDE.md ("Standing Facts"), corrected 2026-07-29
  status: VERIFIED
- id: venture_status
  value: <STANDBY, pre-revenue — activation trigger: first confirmed booking>
  source: agents/grace.md "Activation Trigger"
- id: launch_date
  value: null
  status: PLACEHOLDER
  source: docs/CURRENT-STATE.md ("not set — sequence roadmap by dependency only")
```

## 2. `data/canonical/services.yml` — Service Catalogue

```yaml
- id: service_massage
  fields: [name, duration_min, staff_category, room_type]
  source: docs/services-master-table.md
- id: service_nails
  fields: [name, duration_min, staff_category, room_type]
  source: docs/services-master-table.md
- id: service_hair
  fields: [name, duration_min, staff_category, room_type]
  source: docs/services-master-table.md
- id: service_beauty
  fields: [name, duration_min, staff_category, room_type]
  source: docs/services-master-table.md
- id: service_gtt_collection
  fields: [name, duration_min="draw event, 5min per docs/CURRENT-STATE.md §1", staff_category=phlebotomist]
  source: docs/gtt-clinical-protocol.md, docs/CURRENT-STATE.md §1
- id: service_3d_scan
  fields: [name, status="future/Phase 2, not launch scope"]
  source: docs/hire-purchase-china.md, docs/market-research-findings.md (CONFLICT-05/06, resolved)
  status: PLACEHOLDER   # future scope, not a current committed service
```

## 3. `data/canonical/pricing.yml` — Pricing

```yaml
- id: package_1_price
  value: null   # source: docs/CURRENT-STATE.md §2 -- A$250
  unit: A$
  status: MODELLED   # per current CURRENT-STATE.md tag: "Anthony's locked launch price, not externally market-tested"
  source: docs/services-pricing-locked.md, docs/CURRENT-STATE.md §2
- id: package_1_composition
  value: null   # source: docs/services-pricing-locked.md -- fixed 2x30min
- id: package_2_price
  value: null   # source: docs/CURRENT-STATE.md §2 -- A$300
  status: MODELLED
- id: package_2_composition
  value: null   # source: docs/services-pricing-locked.md -- flexible (2x45, 1x45+1x30, 2x30)
- id: pm_alacarte_avg
  value: null   # source: docs/CURRENT-STATE.md §2 -- ~A$95/session
  status: MODELLED
  status_detail: "pm-staffing-roster.md planning estimate, no real booking data"
- id: pm_package_pricing
  status: PLACEHOLDER
  source: docs/pm-package-structure.md ("direction confirmed, final pricing not signed off")
- id: price_increase_policy
  value: null   # source: docs/CURRENT-STATE.md item 36 -- no increase before 12 months' trading
  status: DECIDED
```

## 4. `data/canonical/client_assumptions.yml` — Client Volume / Demand

```yaml
- id: am_committed_daily_volume_primary
  value: null   # source: docs/CURRENT-STATE.md §1 Table 1 -- 18 clients/day
  status: MODELLED
  status_detail: "adopted because it strictly dominates Table 2 -- framing flag OPEN, see VERIFICATION-TRACKER.md item 1m"
- id: am_committed_daily_volume_secondary
  value: null   # source: docs/CURRENT-STATE.md §1 Table 2 -- 12 clients/day
  status: SCENARIO
- id: am_proven_ceiling
  value: null   # source: docs/CURRENT-STATE.md §1 -- 14 clients/day
  status: SUPERSEDED
  superseded_by: am_committed_daily_volume_primary
  notes: "dominated by Table 1 at the same headcount -- retained for trace only"
- id: addressable_market_perth_weekly
  value: null   # source: docs/CURRENT-STATE.md §3 -- ~515/week, KPMG/ABS Births Australia 2024
  status: VERIFIED
- id: pm_steady_state_capacity
  value: null   # source: docs/CURRENT-STATE.md §3 -- ~16 sessions/day
  status: MODELLED
  status_detail: "assumption: ~50% utilisation of theoretical 4-line capacity, no real demand data"
```

## 5. `data/canonical/operating_hours.yml` — Trading Days & Hours

```yaml
- id: am_start_time
  value: null   # source: docs/CURRENT-STATE.md §1 -- 07:00 (Table 1) / 08:00 (Table 2)
- id: trading_days
  value: null   # source: docs/CURRENT-STATE.md §1 -- Mon-Sat, Sunday closed
  status: DECIDED
- id: sunday_reopen_condition
  value: null   # source: docs/CURRENT-STATE.md §1 -- conditional on proven standalone PM demand
  status: MODELLED
- id: am_shift_window_staff
  value: null   # source: docs/financial-break-even-staff.md -- 07:00-13:00
```

## 6. `data/canonical/scheduling_assumptions.yml` — Booking/Cadence Rules

```yaml
- id: pair_cadence_minutes
  value: null   # source: docs/CURRENT-STATE.md §1 -- 25 min, uniform
- id: chairs_count
  value: null   # source: docs/CURRENT-STATE.md §1 -- 2
- id: phlebotomists_count
  value: null   # source: docs/CURRENT-STATE.md §1 -- 2
- id: wdp_start_time_guidance
  value: null   # source: docs/CURRENT-STATE.md §1 -- "not normally after 10:30am"
  status: VERIFIED
  source_section: "Carole Rivers, WDP, email, 2026-07-30"
- id: wdp_dispatch_cutoff
  value: null   # source: docs/CURRENT-STATE.md §1 -- conditional, see cutoff-time-CORRECTION.md
  status: VERIFIED
- id: chair_b_opening_policy
  value: null   # source: docs/CURRENT-STATE.md §1 -- opens only on 2nd enquiry per slot
  status: VERIFIED
```

## 7. `data/canonical/clinical_timing.yml` — GTT Clinical Marks

```yaml
- id: draw_1_offset_min
  value: null   # source: tools/draw-event-scheduler.py docstring / docs/gtt-clinical-protocol.md -- X to X+15 (historical spec); CURRENT-STATE.md §1 -- 5min draws under the current synchronized model
- id: draw_2_target_offset_min
  value: null   # source: docs/CURRENT-STATE.md §1 -- exactly +60min, synchronized model
- id: draw_3_target_offset_min
  value: null   # source: docs/CURRENT-STATE.md §1 -- exactly +120min, synchronized model
- id: service_block_duration_min
  value: null   # source: docs/CURRENT-STATE.md §1 -- both service windows fixed at 45min
- id: activity_restriction_policy
  value: null   # source: docs/VERIFICATION-TRACKER.md items 29/29b/29c/29d -- "remain at collection centre," WDP policy layered on NPAAC, not an NPAAC mandate itself
  status: VERIFIED
  notes: "confirmed directly by Carole Rivers, WDP, 2026-08-08 -- see item 29d"
```

## 8. `data/canonical/facilities.yml` — Chairs / Rooms

```yaml
- id: collection_chairs_count
  value: null   # source: docs/CURRENT-STATE.md §1 -- 2
- id: collection_room_spec
  fields: [size_sqm, walls, reclining_chair_or_couch, ventilation, wheelchair_access, impervious_surface, data_power_points]
  source: docs/floor-plan-concept.md, docs/VERIFICATION-TRACKER.md item 30 (5 gaps flagged, not yet closed)
  status: PLACEHOLDER   # 5 of 8 sub-fields unresolved per item 30
- id: nail_stations_count
  value: null   # source: docs/floor-plan-concept.md -- 4
- id: hair_chairs_count
  value: null   # source: docs/floor-plan-concept.md -- 4
- id: floor_area_sqm
  value: null   # source: docs/CURRENT-STATE.md §7.2 -- 239sqm day-one
```

## 9. `data/canonical/staffing.yml` — Positions & Headcount

```yaml
- id: role_venue_manager
  fields: [qty=1, status="new hire, not yet in place"]
  status: PLACEHOLDER
  source: docs/CURRENT-STATE.md §4
- id: role_phlebotomist
  fields: [qty=2, employment_model="OPEN -- in-house vs WDP-supplied, item 1d"]
  status: PLACEHOLDER
  source: docs/CURRENT-STATE.md §4, docs/VERIFICATION-TRACKER.md item 1d
- id: role_treatment_staff_primary
  fields: [qty=8, composition="4 Massage+Beauty pool + 2 Nails + 2 Hair", volume_model=am_committed_daily_volume_primary]
  status: VERIFIED
  source: docs/CURRENT-STATE.md §4
- id: role_receptionist_manager
  fields: [qty=1, shift="split shift"]
  status: MODELLED
  source: docs/CURRENT-STATE.md §4
- id: role_pm_casual_roster
  fields: [qty=4, composition="1 each: massage, hair, nail, beauty"]
  status: MODELLED
  source: docs/CURRENT-STATE.md §4, docs/pm-staffing-roster.md
```

## 10. `data/canonical/wages.yml` — Hourly Rates / Award References

```yaml
- id: award_reference_treatment
  value: null   # source: docs/hr-framework.md, docs/financial-break-even-staff.md
- id: award_reference_phlebotomist
  value: null   # source: docs/hr-framework.md (MA000027 investigated, item 11 -- Saturday carve-out unconfirmed)
  status: PLACEHOLDER
  notes: "no payroll advisor/Fair Work confirmation obtained -- conservative full-penalty assumption used"
- id: casual_min_engagement_hours
  value: null   # source: docs/CURRENT-STATE.md item 1i -- 3-hour minimum, MA000005 cl.11.5/MA000027 cl.11.2
  status: VERIFIED
- id: superannuation_rate
  value: null   # source: docs/01_conflicts_log.md "Other Consistency Checks" -- 12%, consistent across staff-plan.md/hr-framework.md/financial-setup.md
```

## 11. `data/canonical/payroll_costs.yml` — Derived Payroll Totals

```yaml
- id: am_direct_labor_weekday
  value: null   # source: docs/CURRENT-STATE.md §5 -- A$48,254.67/month
  status: CALCULATED   # arithmetic derivation from wages.yml x staffing.yml, no separate named assumption
- id: workers_comp_rate
  value: null   # source: docs/CURRENT-STATE.md §5 -- 1.7% of Direct Labor
  status: MODELLED
- id: phlebotomist_only_cost_annual
  value: null   # source: docs/VERIFICATION-TRACKER.md item 1d-be -- A$104,834-106,631/yr range
  status: MODELLED
  notes: "break-even comparison figure vs a hypothetical WDP-supplied rental fee, item 1c still unquantified"
```

## 12. `data/canonical/opex.yml` — Non-Wage Operating Expenses

```yaml
- id: non_wage_overhead_monthly
  value: null   # source: docs/CURRENT-STATE.md §5 -- A$13,980.00/month, fixed
  status: MODELLED
- id: rent_annual
  status: PLACEHOLDER
  source: docs/rent-budget-2026-07-28.md, docs/VERIFICATION-TRACKER.md items 29/30 (property/venue, unresolved)
- id: marketing_spend_ramp
  value: null   # source: docs/CURRENT-STATE.md §5 -- A$600/800/1000/1200 ramping to A$1,500 steady-state
  status: MODELLED
- id: insurance_monthly
  value: null   # source: docs/CURRENT-STATE.md §7.3 -- ~A$400/month
  status: PLACEHOLDER
  notes: "never an actual quote, corrected 2026-07-31 from an implied-confirmed figure"
```

## 13. `data/canonical/startup_costs.yml` / `data/canonical/capex.yml`

```yaml
- id: equipment_furniture_signage_range
  value: null   # source: docs/CURRENT-STATE.md §7.1 -- A$61,190-140,430
  status: MODELLED
- id: fitout_construction_range
  value: null   # source: docs/CURRENT-STATE.md §7.2 -- A$191,200-298,750
  status: MODELLED
- id: working_capital_legal_range
  value: null   # source: docs/CURRENT-STATE.md §7.3 -- A$105,000-138,000
  status: MODELLED
- id: startup_capital_adopted_total
  value: null   # source: docs/CURRENT-STATE.md §7.4 -- A$292,335-594,900, "Anthony's reconciled figure, adopted as instructed"
  status: DECIDED
  notes: "does not exactly reconcile with the component sum above -- disclosed gap, not resolved, see CURRENT-STATE.md §7.4"
- id: startup_capital_historical_ranges
  status: SUPERSEDED
  notes: "3 earlier unreconciled ranges (investor-memorandum.md, HANDOFF.md, business-plan.md) -- retained for trace, CURRENT-STATE.md §6"
```

## 14. `data/canonical/revenue_assumptions.yml`

```yaml
- id: am_price_used_for_revenue
  value: null   # source: docs/CURRENT-STATE.md §2 -- A$250 (Package 1), deliberate conservative choice, not blended average
  status: DECIDED
- id: ancillary_revenue_spray_tan
  value: null   # source: docs/VERIFICATION-TRACKER.md item 10 -- A$58,000/yr
  status: PLACEHOLDER
  notes: "stale operating-day assumption, no bottom-up derivation"
- id: ancillary_revenue_retail
  value: null   # source: docs/VERIFICATION-TRACKER.md item 10 -- A$25,000/yr
  status: PLACEHOLDER
- id: ancillary_revenue_cafe
  value: null   # source: docs/VERIFICATION-TRACKER.md item 10 -- A$15,000/yr
  status: PLACEHOLDER
```

## 15. `data/canonical/financial_assumptions.yml` — Tax / Structure

```yaml
- id: gst_treatment
  status: PLACEHOLDER
  source: docs/cash-flow.md GST Treatment section, docs/VERIFICATION-TRACKER.md item 7
  notes: "accountant confirmation required -- standard-rated vs mixed apportionment"
- id: trust_distribution_tax_2028_proposal
  status: PLACEHOLDER
  source: docs/financial-model.md §2A, docs/VERIFICATION-TRACKER.md item 9c
  notes: "announced 2026-05-12, not legislated -- dated revisit trigger set"
- id: abn_gst_registration_scope
  status: PLACEHOLDER
  source: docs/financial-model.md §1, docs/VERIFICATION-TRACKER.md item 8
```

## 16. `data/canonical/scenarios.yml` — Named Scenario Registry

```yaml
- id: scenario_table_1
  label: "Table 1 -- 18 clients/day, 07:00 start, g=25"
  status: MODELLED   # PRIMARY committed, per item 1m's still-open framing flag
  is_primary: true
  confirmed_by_anthony: false   # explicitly flagged, per VERIFICATION-TRACKER.md item 1m
- id: scenario_table_2
  label: "Table 2 -- 12 clients/day, 08:00 start, g=25"
  status: SCENARIO
  is_primary: false
- id: scenario_14_client_ceiling
  status: SUPERSEDED
  superseded_by: scenario_table_1
- id: scenario_d_growth
  label: "15 clients/day, 3rd phlebotomist/chair"
  status: SCENARIO
  source: docs/scenario-d-investigation.md
- id: scenario_b_theoretical_max
  label: "36 clients/day, 18 pairs -- theoretical, floor plan insufficient"
  status: SCENARIO
  source: docs/VERIFICATION-TRACKER.md item 1l
  notes: "explicitly not an achievable operating point without a floor-plan rebuild"
```

## 17. `data/canonical/risks.yml`

```yaml
# One record per docs/risk-register.md row: id, description, likelihood, impact, mitigation, owner, status
- id: risk_register_import
  source: docs/risk-register.md
  notes: "full import deferred to implementation phase -- not enumerated here to avoid restating ~15-20 rows as an unpopulated sketch"
```

## 18. `data/canonical/decisions.yml` — Founder Decision Log

```yaml
# Maps 1:1 to docs/VERIFICATION-TRACKER.md's "OTHER FOUNDER-ONLY DECISIONS" table
- id: decision_imara_operational_role
  value: null   # RESOLVED NO, 2026-07-18
  status: DECIDED
  source: docs/VERIFICATION-TRACKER.md item 34
- id: decision_price_increase_timing
  value: null   # no increase until 12+ months trading
  status: DECIDED
  source: docs/VERIFICATION-TRACKER.md item 36
- id: decision_payment_policy
  value: null   # full prepayment, no deposit
  status: DECIDED
  source: docs/VERIFICATION-TRACKER.md item 39
# ... remaining items 35, 37, 38 follow the same pattern
```

## 19. `data/sources/manifest.yml` — Evidence/Citation Manifest

```yaml
# One record per external evidence document, linking it to every canonical field that cites it.
- source_file: docs/wdp-reply-carole-2026-08-07.md
  source_type: correspondence
  party: "Carole Rivers, Western Diagnostic Pathology"
  cited_by: [wdp_start_time_guidance, wdp_dispatch_cutoff, activity_restriction_policy, phlebotomist_only_cost_annual]
- source_file: docs/property-links-2026-07-28.md
  source_type: listing
  cited_by: []   # not yet linked to a canonical field -- venue not yet selected
```

## 20. `data/canonical/verification_status.yml` — Status Index

```yaml
# Auto-derivable in the future (roll-up of every other file's `status` field) rather than
# hand-maintained -- listed here to make explicit that this is a VIEW, not a new source of truth.
# In the interim, docs/VERIFICATION-TRACKER.md continues to serve this role by hand.
```

---

## Design Notes

- **No file above is populated with a real number.** Every `value: null` with a source comment is intentional — migrating the real figures from `docs/CURRENT-STATE.md` into these files is an implementation-phase task, not an architecture-phase one, and doing it now would risk silently transcribing a figure incorrectly without the cross-checking rigor `CURRENT-STATE.md`'s own history shows this venture needs.
- **Every field traces to an existing named source file** so a future migration is mechanical (read `CURRENT-STATE.md` §N, copy the value + tag into the matching `data/canonical/*.yml` field) rather than requiring re-research.
- **The status vocabulary used here (`DECIDED`, `CALCULATED`, `MODELLED`, `SCENARIO`, `SUPERSEDED` alongside the existing `VERIFIED`/`PLACEHOLDER`) is defined and reconciled against `rules/CLAUDE.md`'s existing 3-status system in `DATA-GOVERNANCE.md` — read that file before treating any status label above as authoritative.**
