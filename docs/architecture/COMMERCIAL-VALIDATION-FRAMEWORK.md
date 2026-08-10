# Commercial Validation Framework

**Phase:** Commercial Validation Phase — pure documentation/planning. This phase builds the frameworks and checklists needed to convert the model from internally-validated to externally-defensible. It resolves nothing, changes no assumption, and does not modify the financial model. Every fact below is sourced to an existing document in this repository; nothing new is invented.

**Date:** 2026-08-10
**Model/document version used as source of truth:** commit `cb4856c` (Financial Model Decision Review) on top of `fdf8e17`/`8727317`.

**Source documents used:** `docs/VERIFICATION-TRACKER.md`, `docs/CURRENT-STATE.md` §6/§7, `docs/architecture/STARTUP-COST-RECONCILIATION.md`, `docs/architecture/FUNDING-REQUIREMENT-INVESTIGATION.md`, `docs/architecture/REVENUE-RAMP-METHODOLOGY.md`, `docs/location-scouting.md`, `docs/floor-plan-concept.md`, `docs/rent-budget-2026-07-28.md`, `docs/property-links-2026-07-28.md`, `docs/grace-startup-plan.md`, `docs/financial-setup.md`, `docs/cash-flow.md`, `docs/pm-staffing-roster.md`, `docs/referral-partnership-plan.md`, `docs/poppy-marketing.md`, `docs/market-research-findings.md`, `data/canonical/*.yml`, `data/models/master_financial_model.yml`.

---

## 1. Venue Dependency Resolution Plan

### 1.1 Every financial-model item dependent on venue confirmation

| Model item | Current basis | What changes once a real venue exists |
|---|---|---|
| Rent (`opex.yml#opex_rent`, A$8,000/month) | A planning estimate: 200sqm @ A$40/sqm/month, anchored to a Subiaco/Nedlands rate (`rent-budget-2026-07-28.md`) | Replaced by the real quoted rent — `location-scouting.md`'s own search has already widened well beyond Subiaco/Nedlands (Osborne Park, Joondalup, Cannington, Myaree/Murdoch all carry different A$/sqm rates), so this figure could move materially in either direction |
| Rent outgoings ambiguity (item 24) | Unknown whether A$8,000/month is net or gross of rates/building insurance/maintenance | Only resolvable once a real lease states outgoings explicitly — a real lease is the only thing that closes this item |
| Construction/fit-out cost (§7.2, A$191,200–298,750 vs. `floor-plan-concept.md`'s independent A$162,452–306,029) | Both are sqm-rate or itemised estimates against an assumed 239sqm layout, not a real floor plate | `STARTUP-COST-RECONCILIATION.md` §4 states this directly: sqm-rate construction estimates are "inherently provisional without a real tenancy" — a confirmed floor plate is the precondition for the 3 real builder quotes this section already recommends |
| Equipment/furniture/signage (§7.1, A$61,190–140,430) | Modelled against the current room-concept (4 nail stations, 4 hair chairs, 2 massage rooms, blood collection room) | Partially venue-independent (most equipment is fixed regardless of address), but real room count/shape could force a different fixture count if the venue's floor plate doesn't match the 239sqm concept |
| Legal/entity setup, lease bond (§7.3, ~A$19,600–27,600, stated as "~2 months' rent") | Derived FROM the modelled A$8,000/month rent figure | Changes automatically once real rent is known — this line is not independent of the rent line above |
| Working capital reserve (A$85,000–110,000, historical Month 1–3 loss basis) | Built on the modelled rent figure inside the Month 1–3 P&L it's based on (`CURRENT-STATE.md` §7.3) | Indirectly venue-dependent — a materially different real rent changes the Month 1–3 loss estimate this reserve is sized against |
| Commercial property/contents insurance (`financial-setup.md` STEP 8, A$1,500–2,500/yr) | A range estimate | Needs the confirmed fit-out + equipment replacement value at the specific venue, which itself depends on the confirmed construction/equipment costs above |
| WDP collection-room compliance | Not yet obtained — `location-scouting.md`'s own explicit rule: "WDP collection room spec must be obtained BEFORE signing any lease" | Determines venue viability directly, and could add fit-out cost if a shortlisted venue needs adaptation to meet WDP's minimum room dimensions/plumbing spec |
| WDP courier/dispatch logistics | Item 1's 2026-07-30 resolution ("overnight storage viable in some circumstances") is conditional on storage/handling conditions not yet spelled out | A specific venue's distance/drive-time to WDP's lab and courier pickup windows determines whether the same-day cutoff or the conditional overnight option actually applies in practice |
| Floor plan / room-count implications | `floor-plan-concept.md`'s Room Schedule assumes a 239sqm layout fitting: Blood Collection Room, GTT Lounge, 4 open-plan nail stations, 4 open-plan hair chairs, Treatment Rooms, Reception, Accessible WC | If a real venue's shape/size doesn't match, some rooms may need to shrink, merge, or be reconfigured — this could also affect the chair/room-count constraint behind the 8-staff/Table 1 (18-client) or Table 2 (12-client) scheduling model, a scheduling-solver question, not just a cost one |
| Pre-Opening Capital timing (`funding_requirement_investigation.pre_opening_capital.timing_classification`, currently "TIMING PARTIALLY VERIFIED") | Week-based sequencing confirmed only against `grace-startup-plan.md`'s stale 2026-06-05 dollar figures | A real lease commencement date and fit-out schedule would let this be upgraded to fully verified, and would let the Pre-Opening Capital vs. operating-P&L sequencing be re-confirmed against the current (larger) dollar figures |
| "Former health/beauty tenancy" discount scenario | Explicitly declined — `STARTUP-COST-RECONCILIATION.md` §2 states inventing a discount percentage with no basis in this repo was requested against and refused | Only becomes assessable once a specific venue candidate (with a known prior use) exists |
| Contingency (15%, `investor-memorandum.md`'s risk table) | Whether it applies on top of, or is already inside, the current headline ranges is genuinely unknown | Not directly venue-dependent, but a real itemised build (which needs a venue first) is the natural point at which this question would finally get answered |

### 1.2 Venue Data Capture Checklist

The concrete list of facts to gather the moment a venue is confirmed — grouped by the model area each fact feeds.

**A. Rent & Occupancy Cost**
- [ ] Face rent (A$/sqm/month and total A$/month)
- [ ] Outgoings — included in the quoted rent, or additional (rates, building insurance, maintenance)? — closes item 24
- [ ] GST treatment of the rent charge (confirm standard-rated, input tax credit claimable — per `financial-setup.md`'s GST coding table)
- [ ] Actual usable floor area (sqm) — not gross building area
- [ ] Lease term, rent review mechanism (fixed CPI vs. market review), rent-free/incentive period, personal guarantee cap
- [ ] Bond amount (weeks/months of rent)
- [ ] Landlord fit-out contribution, if any, and the real dollar amount (currently excluded from every headline figure per Anthony's instruction — capture the real number regardless, don't assume it stays zero)

**B. Construction / Fit-Out**
- [ ] Confirmed floor plate shape and usable sqm, vs. the 239sqm planning assumption
- [ ] Prior tenancy use (raw shell, existing health/beauty fit-out, or other) — resolves the currently-declined "former health/beauty tenancy discount" question
- [ ] 3 real builder quotes against the confirmed floor plate
- [ ] Existing services present: 3-phase power, plumbed wet-area count, HVAC, accessible WC
- [ ] Whether the existing plumbed wet-area count meets the "minimum 2 plumbed wet areas" requirement, or requires new plumbing

**C. Room / Floor-Plan Fit**
- [ ] Whether the confirmed venue supports the current 8-room concept without modification
- [ ] If not, which rooms need to shrink/merge/be dropped, and whether that changes the chair-based scheduling model itself (flag for a scheduling-solver re-run, not assumed)

**D. Pathology Partner Requirements**
- [ ] WDP/PathWest's confirmed minimum collection-room dimensions and plumbing spec (obtain BEFORE signing any lease, per `location-scouting.md`'s own rule)
- [ ] Drive time / courier logistics from the specific venue to WDP's lab, and the specimen handling conditions that make the conditional overnight-storage option (item 1) actually usable
- [ ] Whether the venue's location affects the WDP GTT-start-time guidance (item 1b) given real client travel times

**E. Insurance**
- [ ] Confirmed fit-out + equipment replacement value (feeds commercial property/contents insurance)
- [ ] Landlord's own building-insurance requirements and certificate-of-currency expectations for this specific lease

**F. Timing / Cash-Flow Sequencing**
- [ ] Real lease commencement date and fit-out period length
- [ ] Re-confirm the Week 1–20 schedule (`grace-startup-plan.md`'s FINANCIAL GATES table) against current, larger dollar figures — not just the stale 2026-06-05 figures the week-based timing was originally attached to

**G. Parking / Access** (operational, not a dollar line, but demand-relevant — see Section 3)
- [ ] Confirmed dedicated parking count (minimum 8–10, per `location-scouting.md`'s non-negotiable criterion)
- [ ] Confirmed ground-floor access and accessible WC location

---

## 2. External Validation Requirements Register

What is precisely needed to close each open verification item — not attempted here, only specified.

| Item(s) | What's needed to close it | Output that would actually close it |
|---|---|---|
| 16, 17, 18 — Fair Work wage rates & penalty percentages | A direct Fair Work Commission award-database lookup for MA000005 (Hair & Beauty)/MA000027/MA000002 current base rates and Saturday/Sunday/Public Holiday penalty percentages, OR a payroll advisor / Fair Work Infoline (13 13 94) confirmation call, cross-checked against the two disagreeing internal sources (`financial-break-even-staff.md` vs. `hr-framework.md`) | A single confirmed rate table with an explicit "effective from" date, replacing both existing tables |
| 19 — Insurance | 3 real broker quotes (BizCover, per `financial-setup.md` STEP 8's own instruction) for public liability (min A$20M), professional indemnity (min A$5M), workers compensation (WorkCover WA registration), commercial property/contents (needs the venue-dependent equipment value from Section 1), business interruption (optional) | Certificates of currency for each active policy, obtainable before first patient enters the venue |
| 1c, 1d — WDP commercial terms & phlebotomist employment model | WDP's own commercial-team quote for the venue-based collection clinic — already in motion (Carole actively chasing WDP's State Business Manager, per the tracker's 2026-08-08 update) | A single real dollar figure (or range) for the annual rental/staffing fee, to compare against the already-computed A$104,800–106,600/yr in-house break-even threshold (item 1d-be) |
| 24 — Rent/outgoings | See Section 1's venue checklist item A | A real signed lease (or heads-of-agreement) explicitly stating whether the quoted rent is net or gross of outgoings |
| 25, 26 — Startup-cost reconciliation (6–9 unreconciled historical ranges) | Per `STARTUP-COST-RECONCILIATION.md` §4, five things would need to be true/provided together: (1) a confirmed venue (Section 1) — sqm-rate estimates are inherently provisional without one; (2) a single reconciled construction-cost methodology, choosing between `floor-plan-concept.md`'s itemised build and `CURRENT-STATE.md` §7.2's sqm-rate recompute, or explicitly retaining both with a stated reason; (3) a decision on whether the 15% contingency (`investor-memorandum.md`'s risk table, the only place this percentage appears) applies on top of, or is already inside, the current headline ranges; (4) a decision on whether `grace-startup-plan.md`'s legal/lease lines (A$8,000–21,000 combined) are additive to, or the same as, `CURRENT-STATE.md` §7.3's single legal/lease-bond line (A$19,600–27,600); (5) real quotes — 3 builder quotes, an insurance broker (see item 19), and a quantity surveyor sign-off | A single, defensible, non-bounded startup-capital figure — only achievable once all five conditions above are met together; partial progress on any one narrows, but does not close, the range |
| 41, 42 — PM ramp conflict & ramp-curve origin | Either (a) an external benchmark or comparable-venue client-acquisition curve, or (b) real Month 1–4 booking data (once trading begins) compared against both existing ramp shapes | A determination of which (if either) ramp shape actually describes real demand — see Section 3 for the full evidence framework |
| 39 — PM pre-booking discount | Real booking-mix data (post-launch): what share of PM bookings are paired with a GTT reservation at time of booking (discount-eligible) vs. standalone afternoon bookings | A measured attach rate, tracked from Day 1 as an operational KPI |
| 22 — GTT supplies stale volume basis | No external party required — an internal recalculation updating the "200 tests/month" basis to Table 1/Table 2's real volumes (396/264 tests/month) | A same-session arithmetic fix, the cheapest item in this entire register |
| 7 — GST apportionment | Accountant confirmation of whether the AM package price is a single fully-taxable wellness/venue supply (the current best reading, per `cash-flow.md`'s own investigation) or requires apportionment | A written accountant determination, needed before first BAS lodgement |
| 6, 8, 9, 9b, 9c — Accountant-confirmation items (startup-capital sign-off, ABN/GST registration scope, trust-distribution tax modelling, Imara's employment-status interaction) | A single scoped accountant engagement covering all of these together (`financial-setup.md` STEP 1, already flagged BLOCKING, Week 1) | Cheaper to resolve in one sitting with one advisor than piecemeal — flagged as a bundling opportunity, not a new requirement |

---

## 3. Revenue Ramp Evidence Framework

**The current 43/64/79/93/100% ramp curve is not changed by this section.** This section documents what real-world evidence would be needed to validate or challenge it — a data-collection framework, not a re-modelling exercise.

### 3.1 What the ramp currently rests on (and what it doesn't)

The ramp curve is reused, not re-derived (`REVENUE-RAMP-METHODOLOGY.md` §6, §12) — it reproduces the historical P&L tables' own numbers exactly, but no document anywhere in this repo, at any point in its history, states where the specific numbers (43/64/79/93/100) came from. No external benchmark, referral-pipeline model, or client-acquisition curve is cited.

### 3.2 Lead generation assumptions that currently exist

- **Referral partnerships:** named private midwifery practices, OB/GYN clinics, and public-sector maternal-child-health channels already exist in `poppy-marketing.md` §1 / `referral-partnership-plan.md` — a real, specific list, not invented. **Outreach has explicitly not yet started** — `referral-partnership-plan.md`'s own sequencing note states outreach is gated on venue confirmation (Section 1), since there is not yet a physical address to refer patients to.
- **Paid marketing:** a spend ramp exists (A$600 → A$800 → A$1,000 → A$1,200 → A$1,500/month, `profit-loss-tables.md`'s "Marketing Spend Ramp") and is already implemented in `data/canonical/cost_ramp.yml`'s variable-cost component.
- **Organic:** a waitlist landing page and SEO target list exist in `poppy-marketing.md` §4/§6, not yet live.

### 3.3 What is genuinely missing

- **Conversion rates:** no document anywhere in this repo states a lead-to-booking, enquiry-to-booking, or referral-to-booking conversion assumption for any channel. This is the single largest, currently-unfilled gap in the evidence chain behind the ramp curve.
- **Referral volume assumptions:** the named referral practices have no attached volume estimate anywhere (e.g. "Practice X sees Y GTT-eligible patients/month and would refer Z% of them") — `referral-partnership-plan.md`'s own "What's Missing" section flags the practice list itself as not independently re-verified for currency, on top of this.
- **Spend-to-booking relationship:** the marketing spend ramp (A$600→A$1,500/month) has no stated or evidenced relationship to booking volume — there is no basis anywhere in this repo for why A$600 in Month 1 should produce 43% of steady-state volume rather than 30% or 60%.
- **Client acquisition targets:** the ramp curve's implied client volumes (Table 1: ≈7.74/11.52/14.22/16.74 clients/day for Months 1–4; Table 2: ≈5.16/7.68/9.48/11.16) are an *output* of the reused percentage shape, not an independently-set target validated against the referral list's real capacity.

### 3.4 Evidence that would help — pre-launch (before first revenue)

- Direct conversations with the named referral practices asking a concrete, quantifiable question — "how many GTT-eligible patients do you see per month, and would you refer them here?" — currently absent from every document in this repo.
- A genuine waitlist signup count once outreach begins (post-venue-confirmation), compared against the ramp's implied Month 1 volume as an early directional signal.
- A comparable-venue benchmark: `market-research-findings.md` already references MIWM Melbourne as a competitor but does not capture their actual post-launch client-acquisition curve — worth requesting if accessible (public growth signals or direct competitor intelligence), not assumed transferable to Perth without disclosure.

### 3.5 Evidence that would help — post-launch (once trading begins)

- Real Month 1–4 client-volume counts by day, per scenario, compared directly against the ramp's implied volumes above.
- Real referral-source attribution per booking — which named practices (if any) actually convert, and at what rate.
- Real marketing spend and bookings attributable specifically to paid channels, establishing a real cost-per-acquisition figure that does not exist even as an estimate today.
- Real PM booking counts compared against **both** existing ramp shapes (the blanket 43/64/79/93/100% curve vs. `pm-staffing-roster.md`'s session-count 25/50/75/93.75/100% curve) — this single comparison would resolve item 41's PM ramp conflict with real evidence, something neither existing document can do on its own.

### 3.6 Ramp-Validation Checklist (for a future phase, not attempted here)

- [ ] Collect real Month 1–4 client volume by day, by scenario
- [ ] Collect real referral-source attribution per booking
- [ ] Collect real marketing spend and bookings by channel
- [ ] Compare real PM booking counts against both existing ramp shapes to test item 41
- [ ] If real data diverges materially from the reused ramp, a future phase would rebuild the ramp from real data — explicitly out of scope for this phase, and not attempted here

---

## 4. Investor/Lender Readiness Gap Report

Compares the current deliverables (`outputs/GTT-Center-Perth-Financial-Model.xlsx`, `*.docx`, `*.pdf`, and the canonical data layer) against what is actually required for three real-world audiences. Gap-by-gap only — no investor/lender materials are created in this phase.

### 4.1 Bank finance (commercial/business loan)

| Typically required | Currently have | Gap |
|---|---|---|
| Multi-year financial projections | 24-month P&L (both scenarios) | Partial — no Year 3 projection exists |
| Confirmed security/collateral or personal guarantee structure | None modelled — this venture is self-funded (joint savings), no debt/repayment structure exists in any canonical record | Structural gap, not just an evidentiary one — `assumption_opening_cash_not_invented` and the funding investigation's `deliberate_non_assumptions` explicitly state no financing/debt/equity assumption is used anywhere |
| An exact loan amount request | A bounded range, A$357,390–A$577,180 | Not exact — a lender typically wants a single number |
| Accountant-prepared or audited financial statements | Neither exists — item 6 explicitly states accountant sign-off has not occurred | Full gap |
| Confirmed venue/lease as security context | None confirmed | Full gap — same root cause as Section 1 |
| Cash-flow serviceability analysis for loan repayments | An operating-cash accrual-basis proxy only, explicitly not a true cash-basis forecast, and no loan-repayment schedule is modelled at all | Full gap, and structural — no debt structure to service in the first place |

**Conclusion: NOT bank-finance-ready.** The core gap is as much structural (no debt/repayment structure modelled, by design) as evidentiary.

### 4.2 Private investor (equity or informal)

| Typically required | Currently have | Gap |
|---|---|---|
| A clear ask (equity % or fixed investment amount) | None — this venture is explicitly self-funded, no equity-raise structure exists anywhere in this repo | Full gap |
| Return/exit modelling (IRR, payback period, multiple) | None — explicitly out of scope: `master_financial_model.yml`'s own stated scope boundary lists EBITDA, EBIT, NPV, IRR, and investor return as things this model does NOT calculate | Full gap, by design |
| Market sizing / TAM-SAM-SOM | `market-research-findings.md` has a named competitor analysis (MIWM Melbourne) and Perth demographic context exists in `location-scouting.md`, but no formal addressable-market sizing exists | Partial |
| Founder/team credibility narrative | `business-plan.md` exists with narrative content | Not assessed this phase — outside a financial-model-focused review's remit |
| Risk register | `docs/VERIFICATION-TRACKER.md`, `risk-register.md`, and `02_issues_and_risks.md` are unusually thorough for a pre-revenue venture | Strong — arguably the best-covered gap on this list, though it is currently written for an internal/technical audience (governance-status tags, internal jargon) and would need re-packaging, not rebuilding, for an investor-facing summary |

**Conclusion: PARTIAL readiness at best.** The financial-model rigor is unusually strong for a pre-revenue venture, but there is no equity structure, no return modelling, and no investor-appropriate narrative packaging.

### 4.3 Landlord negotiation

| Typically required | Currently have | Gap |
|---|---|---|
| Evidence of financial capacity to pay rent | Self-funded position exists in principle (joint savings) but no formal proof-of-funds document exists anywhere in this repo | Gap, but likely the simplest of the three audiences to close |
| A stated business concept and expected occupancy/usage pattern | Strong — the operations model, staffing, and clientele profile are all well documented (`CURRENT-STATE.md`, `floor-plan-concept.md`) | None |
| Public liability insurance certificate of currency | Not yet — insurance has not been purchased pre-lease (item 19 unresolved); `financial-setup.md` STEP 8 itself states this is required "before lease signing" | Gap, but a known, scoped one (see Section 2) |
| A stated fit-out plan/timeline (for negotiating a rent-free/incentive period) | A floor-plan concept and a week-based schedule exist, though the week-based FINANCIAL GATES table is flagged stale (dollar figures from 2026-06-05) | Partial — the timing structure itself is usable, the dollar figures attached to it are not current |

**Conclusion: this is the closest of the three to being ready.** The venture already has a real business concept and occupancy story to present. The two concrete gaps are a proof-of-funds document (not currently in this repo, likely the simplest to produce) and public liability insurance (unconfirmed, needed for many landlords even to view seriously).

### 4.4 Summary

| Audience | Readiness | Primary blocker |
|---|---|---|
| Bank finance | NOT ready | No debt/repayment structure exists at all (structural), plus no accountant sign-off, no venue, no exact figure |
| Private investor | PARTIAL | No equity structure or return modelling exists (by design/scope), strong risk documentation needs re-packaging |
| Landlord negotiation | CLOSEST to ready | Proof-of-funds document and public liability insurance are the only two concrete, closeable gaps |

---

## Validation — Confirmed No Model Changes Occurred

- `git status --short` before this phase: clean.
- Files created this phase: `docs/architecture/COMMERCIAL-VALIDATION-FRAMEWORK.md` only. `git diff --stat` confirms zero changes to `data/canonical/`, `data/models/`, or `tools/*.py`.
- Full pytest suite: **114 passed**, 0 failed (re-run, unchanged from the prior two phases).
- `tools/validate_canonical_data.py`: **13 files checked, 0 errors, 27 warnings** (identical to both prior phases — no new errors, no new warnings).
- `tools/check_consistency.py`: **0 findings** (identical to both prior phases).
- No canonical YAML, financial formula, revenue/cost methodology, or scenario definition was touched. No open tracker item was resolved. No new financial assumption was introduced.

## Recommended Next Step

The single cheapest, highest-value action available today with zero external dependency is closing item 22 (GTT supplies stale volume basis) — a same-session arithmetic fix. Beyond that, this framework's own findings point to the same conclusion as the prior Decision Review: venue confirmation is the one external dependency that unlocks the largest number of items in both the Venue Dependency Resolution Plan (Section 1) and the External Validation Requirements Register (Section 2) simultaneously. The Revenue Ramp Evidence Framework (Section 3) identifies a parallel, independent track — direct conversations with the already-named referral practices — that does not require a venue to begin, since it asks a quantifiable question ("how many GTT-eligible patients do you see, and would you refer them here?") that any named practice could answer today, ahead of formal outreach.
