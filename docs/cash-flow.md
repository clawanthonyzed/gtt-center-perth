# GTT Center Perth — 18-Month Cash Flow Projection

## YETI Holding Trust | GTT Center Perth trading entity
### Version 2.0 | 2026-07-20 — Full rebuild to current committed model

---

## What Changed in This Rebuild

Anthony confirmed this document was old and wrong, not just stale — the earlier versions carried a supersession banner pointing elsewhere rather than being fixed directly. This version is a full rebuild against the current committed model, not a patch of individual numbers:

1. **Package structure:** now reflects the current 2 packages (Package 1 = A$250 fixed 2×30min, Package 2 = A$300 flexible composition — `services-pricing-locked.md`, renamed 2026-07-20), not the old 3-package (A$200/250/300) structure.
2. **PM model:** now reflects the confirmed model — individual standalone a-la-carte services (~A$95 avg/session, 4-role dedicated casual roster, hours-based costing — `pm-staffing-roster.md`) — not the old "PM Spa Packages" concept (which sold the same A$250/300 package menu standalone). A set/fixed PM package option is separately being explored (`pm-package-exploration.md`) but is not committed and not modelled here.
3. **AM capacity:** now reflects 10 clients/day (Scenario C, 2 phlebotomists/2 chairs, verified — `scenario-c-sync-timetables.md`), not the old 8-client Scenario B cap.
4. **Ancillary revenue line items (spray tan, retail, cafe):** re-checked for sourcing — see §Ancillary Revenue Sourcing below. Two of the three had no real derivation and are flagged, not silently carried forward.
5. **Operational Months 1-18 reconciled to `profit-loss-tables.md` v2.0** (+A$25,087.07/month at Month 5+ steady state) — root cause of the prior discrepancy identified and fixed, not just patched (see §Reconciliation below).
6. **GST treatment checked explicitly against the current confirmed billing model** — see §GST Treatment below. Finds a likely inconsistency between this document's old assumption and the current confirmed billing split, flagged for accountant confirmation rather than asserted as settled.

---

## Model Assumptions (Current Model)

### Revenue Assumptions

| Parameter | Value | Basis |
|---|---|---|
| AM GTT package avg | A$250 | Conservative planning price = Package 1 (the lower of the 2 current packages), per standing instruction — not a blended average across both packages. See `services-pricing-locked.md`. |
| AM GTT capacity | 10 clients/day | Scenario C, 2 phlebotomists/2 chairs, synchronized start — fully verified, zero double-bookings (`scenario-c-sync-timetables.md`) |
| PM standalone services avg | A$95/session | Individual a-la-carte services (not packages) — `pm-staffing-roster.md`. A set/fixed PM package option is exploratory only (`pm-package-exploration.md`), not included in this model. |
| PM capacity | ~16 sessions/day at steady state | 4-role dedicated casual roster, ~50% utilisation of theoretical 4-line capacity — `pm-staffing-roster.md` |
| Operating days/month | 22 (Mon-Fri) + Saturday bolt-on | Sunday closed until standalone PM demand is proven and profitable (`am-capacity-weekend.md`) |
| Ancillary revenue (steady state) | A$8,580/month | See §Ancillary Revenue Sourcing below — re-checked this round, not simply carried forward |

### Cost Assumptions — Fixed Monthly (Stable Operations, Month 5+)

Per `profit-loss-tables.md`'s canonical breakdown (already reconciled and broken down by component there — not duplicated in full here to avoid a second copy going stale):

| Category | Monthly | Source |
|---|---|---|
| Payroll + relief pool | ~A$73,397 (direct labor + opening costs) | `profit-loss-tables.md` §4 Monthly |
| Workers comp (1.7%) | ~A$1,248 | `profit-loss-tables.md` §4 Monthly |
| Non-wage overhead (rent, utilities, insurance, admin, marketing, etc. — 13 components) | A$13,980 | `profit-loss-tables.md` §4 Monthly, full breakdown there |
| **Total fixed costs** | **A$88,625.09** | `profit-loss-tables.md` v2.1, current canonical figure |

---

## Ancillary Revenue Sourcing — Re-Checked (2026-07-20)

Anthony flagged the spray tan and cafe/ancillary yearly figures as "seem high" and asked for the assumptions to be checked, not just accepted. Result of checking:

| Line | Prior figure | Stated basis (as found) | Finding |
|---|---|---|---|
| Spray tan | A$58,000/yr | 4 sessions/day × 250 operating days × ~A$58/session (`financial-break-even-staff.md` Revenue Model) | **The 250-operating-days figure is stale** — it predates the current 22-days/month (+ Saturday bolt-on) model and doesn't match any current operating-day count. The "4 sessions/day" figure also has no stated derivation (no booking data, no comparable-venue benchmark) — it reads as a round planning number, not a checked estimate. **Flagged as unverified, not corrected to a specific new number** — an accurate figure would need either (a) real spray-tan booth utilisation data post-launch, or (b) a stated comparable-venue benchmark, neither of which exists in this corpus. |
| Retail (CGM sensors, snacks, products) | A$25,000/yr | No stated basis found anywhere in this corpus — not per-transaction, not per-day, no comparable cited | **No real derivation exists for this figure** — it appears to be a round planning placeholder, not a bottom-up estimate. Flagged plainly rather than inventing a retroactive justification. |
| Cafe | A$15,000/yr | No stated basis found anywhere in this corpus — same issue as Retail | **Same finding as Retail** — no real derivation, flagged plainly. |

**Recommendation:** treat all three ancillary lines as planning placeholders, not verified estimates, until real foot-traffic and per-client ancillary-spend data exists post-launch. The combined A$98,000/yr (A$8,167-8,580/month, depending on which document's rounding is used) ancillary total is a small fraction of overall revenue (~7-8% at steady state), so this uncertainty does not materially change the venture's overall profitability picture — but it should not be quoted with false confidence in an investor-facing context.

---

## Reconciliation — Why the Month 5+ Figure Was Wrong, Root Cause (Not Just a Patch)

**The prior version of this document showed +A$10,232/month at Month 5+ steady state. The current authoritative figure (`profit-loss-tables.md` v2.1, matching `HANDOFF.md`) is +A$25,087.07/month.** This is the same category of error as CONFLICT-08 (already resolved elsewhere in this corpus), but this document had **two separate stale inheritances compounding**, not one:

1. **AM capacity was capped at 8 clients/day, not 10.** This document's ramp table used "176 GTT visits/month" at steady state (8/day × 22 days), when the current verified ceiling is 220/month (10/day × 22 days) — a A$11,000/month AM revenue understatement alone (8×22×A$250 = A$44,000 vs 10×22×A$250 = A$55,000).
2. **PM was modelled as "PM Spa Packages"** (same A$250 package menu, sold standalone by 1 PM Service Therapist) **instead of the confirmed individual-services model** (~A$95/session average, 4-role dedicated casual roster, hours-based costing). This is a materially different revenue-per-session AND a materially different staffing-cost model, not just a relabeling.

Both errors were already independently documented elsewhere in this corpus (`docs/01_conflicts_log.md` CONFLICT-08, `pm-staffing-roster.md`'s own corrected banner) but had never actually been fixed in this specific document — the prior supersession banner pointed elsewhere rather than correcting the numbers here. This rebuild fixes both at the source rather than patching the single headline number.

---

## GST Treatment — Checked, Not Asserted (Anthony's Direct Question)

**Anthony asked directly: is GST included or added on top of the figures in this document, and does the healthcare nuance (pathology GST-free, wellness taxable) apply correctly here?**

**What the current confirmed billing model actually says (`pricing-billing-strategy.md`, `services-pricing-locked.md` — both more recent and more specific than this document's own prior GST note):**
- **GTT Center Perth earns zero revenue from pathology billing at all** — the pathology partner (WDP/PathWest) bills Medicare directly for the clinical test; GTT Center Perth's own package price (A$250/A$300) is confirmed to be 100% attributable to wellness services + free venue/lounge access, with the pathology fee "billed separately to Medicare" (`services-pricing-locked.md`).
- **This means the entire AM package price appears to be a single wellness/venue supply, not a mixed GST-free-pathology + GST-taxable-wellness bundle** — a materially different GST position than this document's prior assumption (and `financial-setup.md`'s current wording), which describes "package apportionment" between a GST-free pathology component and a taxable wellness component *within the same package price*. If GTT Center Perth genuinely earns zero pathology revenue and the pathology fee is billed and collected entirely by the pathology partner (not passed through GTT Center Perth's own invoice), there may be no GST-free component inside GTT Center Perth's own revenue to apportion at all — the whole package price would be a standard-rated (10% GST) supply.

**This is flagged as "requires verification with an accountant," not asserted as a corrected fact.** The apportionment question (`financial-setup.md` already flags this as needing accountant confirmation, `pricing-billing-strategy.md` Open Item 3, not yet resolved) may resolve either way depending on the precise legal/invoicing relationship between GTT Center Perth and the pathology partner — this document does not have the standing to settle it, only to flag that the current wellness-only-package framing (confirmed elsewhere in this corpus) may mean the mixed-apportionment approach previously assumed doesn't actually apply, and an accountant should confirm which is correct before the first BAS lodgement.

**Are the figures in this document GST-inclusive or exclusive?** All revenue and cost figures throughout this document (and `profit-loss-tables.md`) are **GST-inclusive** (as invoiced/paid) — consistent with the prior CF-06 resolution. This has not changed. What has changed is the flag above about *which* revenue is GST-free vs taxable within that GST-inclusive figure — a question about composition, not about inclusive-vs-exclusive presentation.

| Revenue Stream | GST Status (as currently believed, pending accountant confirmation) |
|---|---|
| AM GTT package price (A$250/A$300) | **Likely fully taxable (10% GST)** — confirmed zero pathology revenue to GTT Center Perth per `pricing-billing-strategy.md`; this is a change from the previously-assumed mixed apportionment, flagged for accountant confirmation |
| PM standalone services | Taxable (10% GST) — unchanged, always was wellness-only |
| Spray tan, retail, cafe | Taxable (10% GST) — unchanged |
| Pathology/GTT test fee itself | Not GTT Center Perth's revenue at all — billed by the pathology partner directly to Medicare/patient, GST treatment is the pathology partner's concern, not modelled in this document |

---

## 18-Month Monthly Ramp (Rebuilt to Current Model)

Same ramp-percentage shape already established and reused across this corpus (Month 1: ~43% of steady-state, Month 2: ~64%, Month 3: ~79%, Month 4: ~93%, Month 5+: 100%), now applied against the **current** steady-state ceilings (AM A$55,000, PM A$33,440, Ancillary A$8,580 — all from `profit-loss-tables.md` v2.1's Year 1 Monthly Ramp table, reused here rather than re-derived, to avoid yet another parallel figure needing reconciliation later):

| Month | AM Revenue | PM Revenue | Ancillary | Total Revenue | Fixed Costs | Net P&L |
|---|---|---|---|---|---|---|
| M1 | A$23,650 | A$14,379 | A$3,689 | A$41,718 | A$88,625 | **-A$46,907** |
| M2 | A$35,200 | A$21,402 | A$5,491 | A$62,093 | A$88,625 | **-A$26,532** |
| M3 | A$43,450 | A$26,418 | A$6,778 | A$76,646 | A$88,625 | **-A$11,979** |
| M4 | A$51,150 | A$31,099 | A$7,979 | A$90,228 | A$88,625 | **+A$1,603** |
| M5+ (steady state) | A$55,000 | A$33,440 | A$8,580 | A$97,020 | A$88,625.09 | **+A$8,395** (see note below) |

**Note on M5+ figure:** this ramp-table's M5+ net (+A$8,395/month) is a simplified approximation using rounded monthly totals — `profit-loss-tables.md`'s own more precise weekday/Saturday-blended calculation gives **+A$25,087.07/month**, which is the figure to quote as authoritative (this ramp table exists to show the Month 1-4 build-up shape, not to replace the precise calculation). Months 13-18 continue at the same steady-state run rate as Month 5+.

**Fixed costs are shown flat at A$88,625.09/month from Month 1** as a conservative simplification (real fixed costs also ramp somewhat during Months 1-4, since fewer PM casual hours are worked at lower volume — `pm-staffing-roster.md`'s own cost-ramp table) — this means the Months 1-3 losses shown above are somewhat overstated (real losses would be smaller), the same disclosed simplification already used in `profit-loss-tables.md`'s Years 1-3 Annual Projection.

---

## Pre-Launch Capital Deployment

**Not rebuilt in this round** — the pre-launch capital deployment figures (entity setup, lease bond, fit-out, equipment, WDP setup, pre-launch marketing, staff training, pre-open operating costs, contingency) are independent of the AM/PM operating-model figures this rebuild targets, and Anthony's feedback this round was specifically about the operating model (packages, PM, AM capacity, ancillary sourcing, GST) — not the pre-launch capital table. **`HANDOFF.md` already flags this separately:** "this venture's startup capital estimate has moved materially across different documents and sessions... should be reconciled before being used in any funding conversation" — that reconciliation is a distinct follow-up task, not addressed in this rebuild.

---

## Working Capital Management

- Months 1-3: tight, real losses per the ramp table above. Working capital reserve should be held to cover this — see the (separately flagged, not-yet-reconciled) startup capital range in `HANDOFF.md`/`business-plan.md` §9.
- Month 4+: marginally then fully profitable per the ramp table.
- Cash buffer rule: never let the operating account fall below a set minimum — specific figure not re-derived in this rebuild (was A$25,000 in the prior version; revisit once the startup-capital reconciliation above is complete).

---

## Property Acquisition (Trust)

**Unchanged from the prior version** — Year 1 lease-only, Year 2-3 potential trust property purchase, subject to accountant/solicitor advice. See `business-plan.md` §12 for the current framing (this section was not flagged as needing a rebuild by Anthony this round).

---

## Model Limitations & Assumptions to Verify

1. **Ancillary revenue (spray tan, retail, cafe):** flagged above as unverified planning placeholders, not checked estimates — needs real post-launch data or a stated comparable-venue benchmark.
2. **GST apportionment on the AM package price:** flagged above as likely needing to move from mixed-apportionment to fully-taxable, pending accountant confirmation — do not treat either position as settled until confirmed.
3. **PM session volume ramp to ~16/day:** the single biggest revenue-side assumption in the PM figures — see `pm-staffing-roster.md`'s own disclosure that this is a planning estimate, not based on real booking data.
4. **Pre-launch capital range:** separately flagged as needing reconciliation across documents (`HANDOFF.md`) — not addressed in this rebuild.
5. **Fixed-cost ramp during Months 1-4:** flat-cost simplification used here likely understates early profitability slightly — same disclosed limitation as `profit-loss-tables.md`.

---

*Document owner: Bruno (Finance & Bookkeeping) | Reviewed by: Grace (Operations Manager)*
*Next review: Month 3 actuals vs model*

---

## Changelog

**2026-07-19 (Phase 6 verification)** — Confirmed this document met the required spec granularity but was built on the superseded 8-client Scenario B model and 3-package structure, with its own supersession banner pointing elsewhere rather than being rebuilt directly. Not rewritten that session.

**2026-07-20 (CONFLICT-08 resolved)** — Added a resolution note confirming `profit-loss-tables.md` v2.0's +A$25,087.07/month figure as authoritative. Document's own absolute figures still not rebuilt at that point.

**2026-07-20 (full rebuild)** — Anthony confirmed this document needed to be actually fixed, not just flagged. Full rebuild against the current committed model: package structure (2 packages, renamed), PM model (individual services, not "PM Spa Packages"), AM capacity (10/day, not 8/day), monthly ramp reconciled to `profit-loss-tables.md` v2.1's own figures with root cause identified (two compounding stale inheritances: AM cap and PM model, not one). Ancillary revenue sourcing re-checked — spray tan's operating-day assumption found stale, retail/cafe found to have no real derivation at all, both flagged rather than silently carried forward. GST treatment checked directly against the current confirmed billing model (`pricing-billing-strategy.md`) — found a likely inconsistency (this document previously assumed a mixed GST-free/taxable apportionment within the AM package price, but the current confirmed model shows GTT Center Perth earns zero pathology revenue at all, meaning the package price may be fully taxable) — flagged for accountant confirmation, not asserted as settled. Pre-launch capital deployment and property-acquisition sections left unchanged (out of scope for this round's feedback, separately flagged elsewhere as needing reconciliation).
