# GTT Center Perth — Revenue Assumption Audit

**Purpose:** document every revenue assumption found this phase, where it lives in `data/canonical/revenue_assumptions.yml`, and — the phase's central question — whether the repo's own historical monthly revenue totals (specifically +A$63,028.75/month, Table 1's headline Net P&L) can actually be reconstructed from canonical assumptions alone. This document does not force a reconciliation where one doesn't exist.

---

## 1. Every Major Revenue Assumption Found

| Assumption | Source Doc | Canonical Record | Scenario | Status |
|---|---|---|---|---|
| AM client volume (18/day Table 1, 12/day Table 2) | `CURRENT-STATE.md` §1 | `scenarios.yml#scenario_table_1/2.client_volume` (already canonical — referenced, not restated) | Table 1 / Table 2 | VERIFIED |
| AM price used for revenue (A$250, Package 1 only) | `CURRENT-STATE.md` §2 | `pricing.yml#am_price_used_for_revenue` (referenced) | universal | DECIDED |
| Operating days (22/month weekday, 4.33 Saturdays) | `CURRENT-STATE.md` §1 | `client_assumptions.yml#operating_days` (referenced) | universal | DECIDED |
| PM weekday volume (16 sessions/day steady state) | `pm-staffing-roster.md` | `client_assumptions.yml#pm_steady_state_capacity` (referenced) | universal | MODELLED |
| **PM Saturday volume (8 sessions/day)** | `CURRENT-STATE.md` §5, Table 1 walkthrough | `revenue_assumptions.yml#rev_pm_saturday_sessions` — **new capture this phase** | universal | MODELLED |
| PM average price (A$95/session) | `pm-staffing-roster.md` | `pricing.yml#pm_alacarte_average` (referenced) | universal | MODELLED |
| AM package mix — real (unknown) | (no source — genuine gap) | `client_assumptions.yml#service_mix_am_package_split` (referenced) | universal | PLACEHOLDER |
| AM package mix — revenue-calc convention (100% Pkg 1) | `CURRENT-STATE.md` §2 | `revenue_assumptions.yml#rev_am_package_mix_current` — **new capture, makes the real-vs-convention distinction explicit** | universal | DECIDED |
| PM service mix — a-la-carte only, packages excluded | `cash-flow.md` | `revenue_assumptions.yml#rev_pm_service_mix_current` — **new capture** | universal | DECIDED |
| Historical 3-tier package mix (30/40/30) | `financial-break-even-staff.md` | `revenue_assumptions.yml#rev_am_package_mix_historical_3tier` — **new capture** | universal | SUPERSEDED |
| PM theoretical max capacity (~31/day) | `pm-staffing-roster.md` | `revenue_assumptions.yml#rev_pm_theoretical_max_capacity` — **new capture** | universal | MODELLED |
| PM utilisation (~50% source framing / 51.6% calculated) | `pm-staffing-roster.md` | `revenue_assumptions.yml#rev_pm_utilisation_calculated` — **new capture** | universal | CALCULATED |
| Ramp curve, 43/64/79/93/100% of ceiling | `profit-loss-tables.md` | `revenue_assumptions.yml#rev_ramp_pct_curve_historical` — **new capture** | universal (historical basis only) | SUPERSEDED |
| PM session ramp, 4/8/12/15/16/day M1-M5+ | `pm-staffing-roster.md` | `revenue_assumptions.yml#rev_pm_session_ramp_historical` — **new capture** | universal | MODELLED |
| Spray tan ancillary (A$58,000/yr) | `cash-flow.md` | `revenue_assumptions.yml#rev_ancillary_spraytan_historical` — **new capture** | universal | MODELLED |
| Retail ancillary (A$25,000/yr) | `cash-flow.md` | `revenue_assumptions.yml#rev_ancillary_retail_historical` — **new capture** | universal | MODELLED |
| Cafe ancillary (A$15,000/yr) | `cash-flow.md` | `revenue_assumptions.yml#rev_ancillary_cafe_historical` — **new capture** | universal | MODELLED |
| **Ancillary revenue in the current baseline: A$0.00/month** | `profit-loss-tables.md` | `revenue_assumptions.yml#rev_ancillary_excluded_from_baseline` — **new capture** | universal | VERIFIED |
| PM pre-booking discount (10%) | `services-pricing-locked.md` | `revenue_assumptions.yml#rev_discount_pm_prebooking` — **new capture** | universal | VERIFIED |
| Cancellation/no-show revenue-retention effect | `onboarding.md` | `revenue_assumptions.yml#rev_cancellation_noshow_policy` — **new capture** | universal | DECIDED |
| Merchant fees stay in opex, not a revenue deduction | `financial-setup.md` | `revenue_assumptions.yml#rev_merchant_fees_boundary` — **new capture** | universal | DECIDED |

**21 total facts represented — 4 pure references to already-canonical records (no restatement), 17 genuinely new records** (13 substantive assumptions + 2 revenue-reconstruction traceability records + 2 record-level cross-boundary notes).

---

## 2. Conflicting Assumptions (2 Declared)

1. **`conflict_ramp_base_ceiling_mismatch`** — `docs/profit-loss-tables.md`'s Year 1 Monthly Ramp table applies the 43/64/79/93/100% shape to a A$66,000/month AM ceiling (12-client/23-min model, post-2026-07-30). `docs/cash-flow.md`'s own 18-month ramp table applies the SAME shape to a A$55,000/month ceiling (the older 10-client model). Two documents, both presenting as current, disagreeing on the base figure the identical ramp percentages are applied to. **Genuinely new finding this phase** — neither document's own staleness banner previously flagged disagreeing with the other specifically.
2. **`conflict_ancillary_aggregate_vs_itemised`** — the historical ancillary aggregates (spray tan A$58K/yr, retail A$25K/yr, cafe A$15K/yr) have no stated volume assumption connecting them to `services.yml`'s individually-priced café/retail items. Moot for the current baseline (ancillary is A$0), but unresolved if ancillary revenue is ever reintroduced.

---

## 3. Assumptions That Can't Safely Be Migrated

- **A precise per-line-throughput derivation for PM's "~31/day theoretical max"** — the figure itself is sourced, but the arithmetic behind it (which specific combination of 4 lines × hours × service-length produces 31) is not shown anywhere in this repo — recorded as the stated figure only, not reverse-engineered.
- **Any Table 1/Table 2-specific ramp curve** — genuinely does not exist. `CURRENT-STATE.md`'s own changelog confirms the Year 1 Monthly Ramp "has not yet been independently rebuilt against Table 1's higher ceiling." Recorded as `SUPERSEDED` with no `superseded_by` target, since no replacement exists to point to (see §5 below for why this matters).
- **A connecting assumption between ancillary aggregate revenue and per-item café/retail prices** — no "X items sold per client visit" figure exists anywhere; not invented here.
- **A specific "% of PM bookings actually paired with a GTT reservation"** to apply the 10% pre-booking discount against real revenue — the discount rule exists, but nothing in this repo states what share of PM bookings would qualify for it.

---

## 4. Relationships Between Client Volume, Mix, Pricing, and Revenue

Represented directly in `revenue_assumptions.yml`'s two `revenue_reconstruction` records via inline references to canonical IDs (not a separate diagram): each reconstruction states, line by line, which `scenarios.yml`/`pricing.yml`/`client_assumptions.yml`/`revenue_assumptions.yml` id feeds each term of `clients × price × operating_days = revenue`, for both the AM weekday, AM Saturday, PM weekday, and PM Saturday components, summed to a monthly total. See §5.

---

## 5. Can the Historical Monthly Revenue Totals Be Reconstructed? (The Central Question)

**Short answer: mostly yes, with one precisely-identified, disclosed, unreproducible gap of exactly A$2,576.36 — identical for both Table 1 and Table 2.**

### Table 1 (18-client), independently reconstructed from canonical inputs only:

```
Weekday AM: 18 (scenarios.yml#scenario_table_1.client_volume)
            x A$250 (pricing.yml#am_price_used_for_revenue)
            x 22 days                                          = A$99,000.00
Saturday AM: 18 x A$250 x 4.33 Saturdays/month                  = A$19,485.00
Weekday PM: 16 (client_assumptions.yml#pm_steady_state_capacity)
            x A$95 (pricing.yml#pm_alacarte_average)
            x 22 days                                           = A$33,440.00
Saturday PM: 8 (revenue_assumptions.yml#rev_pm_saturday_sessions)
            x A$95 x 4.33                                       = A$3,290.80
Ancillary:  A$0.00 (revenue_assumptions.yml#rev_ancillary_excluded_from_baseline)
─────────────────────────────────────────────────────────────────────────
RECONSTRUCTED TOTAL                                            = A$155,215.80
CURRENT-STATE.md's own stated "canonical" Total Revenue         = A$157,792.16
GAP                                                              = A$2,576.36 (unreproducible)
```

### Table 2 (12-client), same method:

```
Weekday AM: 12 x A$250 x 22                                     = A$66,000.00
Saturday AM: 12 x A$250 x 4.33                                   = A$12,990.00
Weekday PM: 16 x A$95 x 22 (identical to Table 1 -- AM-volume-independent) = A$33,440.00
Saturday PM: 8 x A$95 x 4.33 (identical to Table 1)              = A$3,290.80
Ancillary:  A$0.00
─────────────────────────────────────────────────────────────────────────
RECONSTRUCTED TOTAL                                             = A$115,720.80
CURRENT-STATE.md's own stated Total Revenue                     = A$118,297.16
GAP                                                              = A$2,576.36 (identical to Table 1's gap)
```

### What this proves, precisely

1. **Every input to both reconstructions traces to an existing canonical id** — nothing was invented, and the two builds share 3 of their 5 line items exactly (PM weekday, PM Saturday, ancillary), differing only in the AM lines, which is exactly what should happen when only client volume changes between two scenarios.
2. **The gap is real, not a transcription error in this file** — it was independently reproduced from the canonical layer (not by re-reading `CURRENT-STATE.md`'s prose figures) and lands at exactly A$2,576.36 for both scenarios, matching `CURRENT-STATE.md`'s own claim that this is a "fixed-size" artifact independent of client volume, "present identically at the 10-client, 12-client, and now 18-client stages."
3. **The missing assumption, named precisely:** `CURRENT-STATE.md`'s own delta-built canonical figures (A$157,792.16 / A$118,297.16) come from a "weekly-to-monthly revenue-scaling" step whose exact mechanism is not documented precisely enough anywhere in this repo to reproduce independently. The gap is not a mystery in magnitude (exactly A$2,576.36, confirmed twice) — it is a mystery in *mechanism*. This is the one concrete, nameable gap standing between "the assumptions layer is fully traceable" and "the assumptions layer is fully traceable AND reconciles to the cent."
4. **Not forced to reconcile** — per the coordinator's explicit instruction, this gap is recorded as-is in `revenue_assumptions.yml`'s two `revenue_reconstruction` records, not closed by adjusting any input to make the totals match.

### Net P&L was NOT re-derived

This exercise reconstructs **revenue** only. `+A$63,028.75/month` (Table 1's headline Net P&L) also depends on payroll (`wages.yml`), non-wage overhead (`opex.yml`), and workers comp — all separately canonical, not re-walked here. Confirming the full P&L reconstructs is a different, larger exercise than this phase's scope (a Master Financial Model), not attempted.

---

## 6. What This Audit Does Not Do

It does not close the A$2,576.36 gap, rebuild the ramp curve against Table 1/Table 2, resolve either declared conflict, calculate a revenue forecast, or reconstruct the full Net P&L (payroll + opex layered on top of revenue). It does not choose Table 1 or Table 2 as primary.
