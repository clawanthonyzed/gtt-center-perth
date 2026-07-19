# GTT Center Perth — Full Business Audit

> **2026-07-14 SUPERSEDED — PM MODEL CORRECTED.** References below to a single "PM Service Therapist" delivering "PM Spa Packages" (Package 1/2/3 pricing) are superseded. The confirmed PM model is: **4 dedicated casual hires** (1 massage, 1 hair, 1 nail, 1 beauty), cross-shift qualified with AM staff, delivering **individual standalone services** (not packages) at ~A$95/session average, staffed on actual hours worked — not a blanket shift. Corrected Month 5+ steady state: Total Revenue A$86,020/month, Total Fixed Costs A$79,357/month, **Net P&L +A$6,663/month** — profitable from Month 4 (+A$4,924/month). See `pm-staffing-roster.md` for the full roster, weekly template, and recalculated P&L — this is now the canonical PM reference, superseding this document's PM figures/structure below.
## Failure Modes | Gaps | Improvements
### Version 1.0 | June 2026 | Audited by: Idea Lobster

---

## AUDIT SUMMARY

**Status: PROCEED WITH MAJOR FIXES REQUIRED**

9 documents reviewed. Found:
- 7 critical failures (can kill the business or cause legal liability)
- 8 internal inconsistencies (documents contradict each other)
- 11 operational gaps (things that need to exist but don't)
- 9 missing documents
- 12 improvement opportunities

> **Day 51 supersession note.** The Day 50 figures referenced throughout CF-01, CF-04, IC-02, IC-03, and IC-07 below are further superseded by the Day 51 package-pricing/staffing model: GTT Lounge (A$25)/Wellness (A$225)/Luxe (A$325) → Package 1 (A$200)/Package 2 (A$250)/Package 3 (A$300), no separate venue/lounge fee; the AM/PM cohort split (one of each pair works AM, the other PM) → AM-only staff (8 of 11 AM staff, no PM shift) + 1 new-hire PM Service Therapist (12:00pm-6:00pm); 3D scan operator role removed entirely; payroll A$675,589/yr → A$713,067/yr (incl. A$15,000/yr relief pool); stable monthly Net P&L A$5,646 → +A$10,232 (Month 5+). See `services-pricing-locked.md`, `financial-break-even-staff.md` (CF-01 Day 51), `cash-flow.md`, `staff-plan.md`. Original Day 49/50 resolutions below retained for audit trail.

---

## SECTION 1 — CRITICAL FAILURES

These are conditions that could kill the business, trigger legal liability, or collapse revenue.

---

### CF-01 | Staff Hours vs Afternoon Revenue — Fundamental Conflict

**Status: ✅ RESOLVED Day 50** — afternoon session designed (AM/PM shift split, 12 staff, no new hires). See `financial-break-even-staff.md` v2.0 §Shift Structure (CF-01), `staff-plan.md` §2A AM/PM Shift Roster.

**Severity: 🔴 FATAL — revenue model is broken as documented** *(original analysis retained below for audit trail)*

The cash flow model (cash-flow.md) projects 7 afternoon wellness visits/day from Month 4.
The staff plan (staff-plan.md) shows massage therapist, nail tech, and beauty therapist all on **25 hours/week, 8:00am–1:00pm**.

Staff who finish at 1:00pm cannot serve afternoon patients from 12:00pm–5:00pm.

The gtt-test-reference.md (§8) says: "Practical approach: Massage and nail therapists work full-time (7:30am–4:30pm) and serve both shifts." But the staff plan and financial model both use 25 hrs/week (morning only).

**Full-time staff cost impact (at 38hrs/week vs 25hrs/week):**
- Massage therapist: +A$1,841/month
- Nail tech: +A$1,629/month
- Beauty therapist (expand from casual 3-day to full-time): +A$1,472/month
- Total additional monthly cost: **+A$4,942/month**
- New break-even: ~130 visits/month (~6 visits/day)

**Fix required (superseded — see Status above):**
~~Either (a) update staff plan to full-time hours with correct costs and update break-even, or (b) remove afternoon revenue projections from cash flow and remodel.~~ — resolved Day 50 via a third option: existing 12 staff split into AM/PM cohorts (one of each pair works AM, the other PM, 1hr overlap), no headcount or hours increase, payroll unchanged at A$675,589/yr.

---

### CF-02 | Phlebotomist Schedule Bottleneck at 9:30am

**Status: ✅ RESOLVED Day 49** — 2 phlebotomists + 2 collection chairs (Chair A / Chair B) from Day 1, plus a corrected draw-timing pathway (Draw 1 at arrival X, Draw 2 at X+75min ±5min, Draw 3 at X+135min ±10min) that matches gtt-clinical-protocol.md's actual tolerances. Verified per-client and per-staff timetable for 8 GTT clients/morning with no double-booking is in operations-manual.md's "GTT Scheduling Timetables" section. business-plan.md, cash-flow.md, gtt-test-reference.md updated to match.

**Severity: 🔴 HIGH — operational failure from Day 1** *(original analysis retained below for audit trail)*

The business plan promises 6–9 GTT patients per morning (3 waves). The GTT clinical reference (§9) explicitly states that 1 phlebotomist managing 5 staggered clients creates a moment at 9:30am where **3 draws must occur within a 10-minute window** (Client A T=120, Client C T=60, Client E T=0).

With a difficult venepuncture (1 in 10 patients), a vasovagal episode (5% of patients), or any minor delay, this cascade fails. T=60 must be within ±5 minutes. Miss the window = invalid test = WDP specimen rejection = patient must re-book at PathWest = angry patient + clinical incident report.

**At 6 patients (the low end of the 6-9 claim):** mathematically impossible with 1 phlebotomist without constant draw collisions.

**Fix required (superseded — see Status above):**
- ~~Reduce stated capacity to 5 GTT patients/day with 1 phlebotomist~~
- ~~Second phlebotomist required from Month 1 if projecting 6+ GTT patients/day~~ — both hired from Day 1
- ~~Update capacity tables across business-plan.md and cash-flow.md~~ — done

---

### CF-03 | WDP Rejection Has No Fallback

**Status: ✅ RESOLVED Day 50** — Clinipath added as tertiary/contingency pathology option in `reed-partnerships.md`. WDP remains Priority 1, PathWest Secondary, Clinipath tertiary/contingency.

**Severity: 🔴 HIGH — entire GTT revenue stream depends on one conversation** *(original analysis retained below for audit trail)*

The entire clinical model depends on WDP (Western Diagnostic Pathology) agreeing to partner. If WDP declines (competing centre in the same area, liability concerns, policy change), or delays approval past the lease start date, GTT Center Perth:
- Cannot collect blood specimens
- Cannot market itself as a GTT venue
- Must open as a wellness-only venue
- Loses ~55% of projected revenue

PathWest is listed as "backup" but there is no documented outreach plan to PathWest. No timeline for making the PathWest call. No "wellness-only launch" financial model.

**Fix required (status: see above; remaining items still open):**
- Contact WDP AND PathWest simultaneously (not sequentially) — Clinipath now a documented third contingency option (Day 50), see `reed-partnerships.md`
- Model a "wellness-only" scenario in cash-flow.md (what does break-even look like with no GTT?) — not addressed Day 50, remains open
- Define a go/no-go gate: if WDP approval not received by [specific date], pivot to wellness-only launch — remains open

---

### CF-04 | Internal Package Pricing Contradiction

**Status: ✅ RESOLVED Day 50** — package pricing standardised to GTT Lounge (A$25) / GTT Wellness (A$225) / GTT Luxe (A$325) everywhere. `business-plan.md` and `cash-flow.md` updated. See `financial-break-even-staff.md` v2.0 Package Pricing Model.

**Severity: 🔴 HIGH — cash flow model overstates revenue** *(original analysis retained below for audit trail)*

cash-flow.md (Model Assumptions) states:
> "Morning GTT package avg A$225. Blended: Essential A$195 (40%), Premium A$295 (45%), Luxury A$395 (15%)"

business-plan.md §6 actual pricing:
> Essential A$80, Relax A$195, Restore A$285, Glow A$345, Complete A$395

These are different packages at different price points.

**Blended average using cash-flow.md assumption math:**
(0.40 × 195) + (0.45 × 295) + (0.15 × 395) = 78 + 132.75 + 59.25 = **A$270**

Not A$225 — the model understates its own blended average by A$45.

But if applying business-plan.md pricing with a realistic mix (30% Essential at A$80):
(0.30 × 80) + (0.30 × 195) + (0.20 × 285) + (0.15 × 345) + (0.05 × 395) = 24 + 58.5 + 57 + 51.75 + 19.75 = **A$211**

Not A$225.

The financial model uses A$225 as the blended average but no consistent package structure across documents produces exactly A$225. The model needs a single, agreed package list with a documented blended average calculation.

**Fix required (superseded — see Status above):**
~~Align package names and prices across all documents. Calculate actual blended average from the confirmed package mix.~~ — done Day 50: GTT Lounge (A$25) / GTT Wellness (A$225) / GTT Luxe (A$325), blended A$225.
~~Update cash-flow.md, business-plan.md, financial-model.md §16 to match.~~ — cash-flow.md and business-plan.md updated Day 50; financial-model.md marked superseded in full (§7 banner) rather than edited inline.

---

### CF-05 | Saturday Operations Contradiction

**Status: ✅ RESOLVED** — `cash-flow.md` already states "Mon–Fri, 22 days", consistent with `staff-plan.md`. No content change needed; marker only (Day 50).

**Severity: 🟡 MEDIUM — revenue model overstated or staff model incomplete**

cash-flow.md states: "Operating days/month: 22 days (Mon–Sat, 4.4 weeks)"

Mon–Sat × 4.4 weeks = **26.4 days** — not 22.  
Mon–Fri × 4.4 weeks = **22 days** — consistent with the number used.

The document says "Mon-Sat" but calculates "Mon-Fri." One is wrong.

If Saturday operations are intended: staff plan must include Saturday roster, penalty rates (150% for all award employees on Saturday), and opening/closing procedures. None documented.

If Saturday operations are NOT intended: fix the text to say "Mon–Fri."

**Fix required:** Choose Mon–Fri or Mon–Sat. If Mon–Sat: budget penalty rates (+A$3,800/month), update staff plan, update ops manual. If Mon–Fri: fix the cash flow description.

---

### CF-06 | GST Not Removed from Revenue in P&L

**Status: ✅ RESOLVED Day 50** — GST treatment clarified in `cash-flow.md` CASH FLOW NOTES (GST collected/paid is a BAS item, not a P&L line, for a registered mixed-supply entity).

**Severity: 🟡 MEDIUM — profit overstated** *(original analysis retained below for audit trail)*

GTT Center Perth is a mixed supply business:
- GTT pathology component: GST-free
- Wellness services (massage, nails, brows): taxable at 10%
- Subtenant rental income: taxable at 10%

Revenue figures in the P&L (cash-flow.md, business-plan.md, financial-model.md) appear to be GST-inclusive for the taxable components. GST collected is not GTT Center Perth's revenue — it's a liability.

At stable operations (A$68,715/month total revenue, ~60% taxable): approximately A$3,744/month in GST collected but not owned.

Over 12 months: A$44,928 in overstated profit.

**Fix required (superseded — see Status above):**
~~Confirm with accountant whether financial models use GST-exclusive or GST-inclusive figures. If inclusive: reduce taxable revenue lines by 10% to show GST-exclusive revenue in P&L.~~ — resolved Day 50: figures are GST-inclusive throughout (consistent treatment); GST is a BAS/balance-sheet item, not a P&L adjustment, for this entity type. Accountant to confirm exact quarterly net GST position from Month 1.

---

### CF-07 | TPI Pension Interaction Unresolved

**Status: 🟡 DEFERRED — not blocking at this stage (Anthony, 2026-06-10).** Salary vs trust-distribution split for Imara/Anthony not reviewed this pass. Revisit alongside DVA adviser consultation (see Open Decisions, `reading-order.md`). Original analysis below retained unchanged.

> **Note (2026-07-19):** Founder decision confirmed 2026-07-18 — Imara is not the on-site operational manager; a separate Venue Manager (new hire) fills that role and draws its own salary (see `staff-plan.md`, `hr-framework.md`). This does not resolve the CF-07 question below, which is specifically about Imara's personal remuneration/trust-distribution arrangement and TPI means-testing exposure — that analysis is unchanged and still requires DVA-adviser sign-off. The Venue Manager's salary is a separate payroll line with no TPI/means-testing implication for Anthony (Venue Manager is not his partner).

**Severity: 🔴 HIGH — potential pension loss for Anthony**

Documents repeatedly flag "TPI pension — consult accountant" but never resolve it. The CLAUDE.md states this is non-negotiable. Multiple documents say Imara can receive trust distributions, but:

1. If Anthony and Imara are a de facto couple, trust distributions to Imara may count as household income under DVA means testing rules.
2. If Anthony is a TPI pensioner (Totally and Permanently Incapacitated — DVA), any income his partner earns from a venture he controls may be assessed.
3. The financial model projects Imara receiving A$72,500/year salary from the trust. If this is means-tested against Anthony's pension, it could reduce or eliminate the pension.

This is not a planning question — it's a legal prerequisite before signing any lease or hiring anyone.

**Fix required:** DVA-qualified financial advisor (not just a general accountant) must advise on this before any legal documents are signed. This is a blocking gate.

---

## SECTION 2 — INTERNAL INCONSISTENCIES

Documents that contradict each other, creating confusion and execution errors.

| ID | Conflict | Doc A | Doc B | Resolution Needed |
|---|---|---|---|---|
| IC-01 | Ramp-up assumptions | ~~financial-model.md §16: Month 1 = 30 visits, break-even Month 3~~ | ~~cash-flow.md: Month 1 = 176 visits, break-even Month 1~~ | ✅ RESOLVED Day 50 — `financial-model.md` marked superseded in full (deprecation banner, §7); `cash-flow.md` v1.0 is canonical. Post-Day-50 reconciliation, operational break-even is Month 4, not Month 1 (see Day 50 Reconciliation note). |
| IC-02 | Staff hours | staff-plan.md: massage/nails/beauty = 25hrs/wk (8am–1pm) | cash-flow.md + gtt-test-reference §8: same staff serve afternoon = full-time hours | ✅ RESOLVED Day 51 — AM staff (massage/nails/beauty/hair) stay AM-only (no full-time hours, no afternoon shift); afternoon PM Spa Packages covered by 1 new-hire PM Service Therapist (12:00pm-6:00pm). See Day 51 supersession note above and CF-01. |
| IC-03 | Package pricing | ~~cash-flow.md: "Essential A$195, Premium A$295, Luxury A$395"~~ | ~~business-plan.md §6: "Essential A$80, Relax A$195, Restore A$285, Glow A$345, Complete A$395"~~ | ✅ RESOLVED Day 50 — standardised to GTT Lounge (A$25) / GTT Wellness (A$225) / GTT Luxe (A$325) in both `cash-flow.md` and `business-plan.md`. See CF-04. |
| IC-04 | Operating days | cash-flow.md: "Mon–Fri, 22 days" | staff-plan.md: Mon–Fri only, all staff | ✅ RESOLVED — both docs consistent (Mon–Fri, 22 days). No change needed; marker only (Day 50). See CF-05. |
| IC-05 | GTT capacity | ~~business-plan.md §5: "6–9 GTT patients/morning"~~ | ~~gtt-test-reference §9: "5 GTT slots = 5 morning clients, 6+ requires second phlebotomist"~~ | ✅ RESOLVED Day 49 — both docs now state 8 GTT clients/morning, 2 phlebotomists/2 chairs from Day 1, per operations-manual.md |
| IC-06 | Startup capital | ~~financial-model.md §16: A$187K–A$361K~~ | cash-flow.md: A$209K–A$431K | ✅ RESOLVED Day 50 — `financial-model.md` marked superseded in full (deprecation banner, §7); `cash-flow.md` v1.0 figures (A$209K–A$431K) are canonical |
| IC-07 | Business plan profit | ~~business-plan.md: "A$12,728/month stable profit" with "Month 3 break-even"~~ | cash-flow.md: A$5,646/month at stable (Month 4), post-Day-50 reconciliation | ✅ RESOLVED Day 50 — `financial-model.md` marked superseded in full; `cash-flow.md` v1.0 + `financial-break-even-staff.md` v2.0 are canonical. `business-plan.md` §9 now cross-refs cash-flow.md instead of stating its own figure. |
| IC-08 | Superannuation rate | ~~hr-framework.md §5: "11.5%... Rising to 12% from 1 July 2025"~~ | ~~All other docs: 11.5%~~ | ✅ RESOLVED Day 50 — superannuation rate is 12% (final SG increase, effective 1 July 2025, current for FY2026). Fixed in `hr-framework.md`, `phlebotomist-job-posting.md`, `staff-plan.md`. (Note: the audit's own original recommendation — "fix hr-framework.md to say 11.5%" — was itself wrong; corrected here.) |

---

## SECTION 3 — OPERATIONAL GAPS

These are things the business needs to operate that don't exist yet.

---

### OG-01 | No Custom GTT Booking Constraint System

The GTT booking requires: patient selects GTT start time → only services that fit within their 2.5hr window display → services must not overlap with T=60 and T=120 draw times.

Fresha CANNOT enforce this natively. The ops manual acknowledges a "Fresha workaround" — receptionist manually reviews every booking.

At 8 GTT patients/day × 22 days = 176 manual booking reviews/month (RESOLVED Day 49 capacity — was 5/day). At 15 minutes per review = 44 hours of receptionist time just on booking QA. At A$26.17/hr = A$1,151/month in hidden labor cost.

When volume grows, this becomes a bottleneck that breaks the whole morning.

**Required:** Custom booking logic (website form or Squarespace + Zapier + Fresha integration) that enforces the GTT timing constraint. Specification needed, developer needed, timeline needed.

---

### OG-02 | No Patient Consent Form

**Status: ✅ RESOLVED Day 48** — `consent-form.md` exists (see `reading-order.md` PHASE 10). Audit was stale.

GTT patients are undergoing a clinical procedure (venepuncture × 3) at a non-hospital venue. ~~No documented consent form exists.~~ Required content (for QC review against the existing doc):
- Identity of the performing phlebotomist
- Nature of the procedure
- GTT Center Perth's role (venue + collection only — NOT diagnosis, NOT results)
- That results go to their referring doctor only
- Privacy consent (data held by GTT Center Perth and shared with WDP/PathWest)
- Right to withdraw at any time
- Emergency contact
- Medical history relevant to blood collection (anticoagulants, needle phobia, difficult veins)

Without this: no informed consent = potential liability if anything goes wrong during collection.

---

### OG-03 | No Emergency Response Plan

**Status: ✅ RESOLVED Day 48** — `emergency-plan.md` exists (see `reading-order.md` PHASE 10). Audit was stale.

Documents mention "call 000" and "Venue Manager stays with patient" (updated 2026-07-19 from "Imara stays with patient" — see emergency-plan.md changelog). ~~No formal emergency plan covering:~~ For QC review, `emergency-plan.md` should cover:
- Location of first aid kit (not specified)
- Location of AED/defibrillator (not specified — is there one?)
- Emergency exit routes
- Evacuation assembly point
- Who calls 000 vs who stays with patient vs who manages other patients
- What to do if the Venue Manager is not present
- Pregnancy-specific emergency considerations (ambulance must know patient is pregnant)

WorkSafe WA requires a documented emergency plan. Without it: WHS non-compliance from Day 1.

---

### OG-04 | No Afternoon Demand Generation Strategy

The financial model projects 6–8 afternoon wellness visits/day. But the entire marketing strategy (Poppy's doc, poppy-marketing.md) is built around midwife/OB referrals — which send GTT patients to the morning shift only. 

Afternoon patients are a completely different acquisition challenge:
- They are NOT getting a GTT (no clinical referral)
- They need to find GTT Center Perth through other channels
- Instagram, Google, and word-of-mouth are the only afternoon acquisition channels
- None of these have documented strategies specific to afternoon bookings

No afternoon-specific:
- Content strategy
- Pricing campaigns
- Partnership list (yoga studios, antenatal classes, physios, OBs who recommend massage)
- Conversion funnel from Instagram → Fresha booking

Without this, afternoon slots stay empty and the model loses A$19,250–26,950/month in projected afternoon revenue.

---

### OG-05 | No Website Specification or Developer Assignment

The entire go-to-market depends on:
1. A waitlist page before launch (collect 300+ names)
2. A Fresha booking widget with GTT constraint logic
3. SEO content targeting "GTT test Perth"
4. Instagram link-in-bio destination

None of this exists. No website spec document. No developer assigned. No domain confirmed as registered. The budget says "A$2,000–5,000 website setup" but no one is building it.

The Instagram campaign (Week 9) cannot begin without somewhere to send traffic.

---

### OG-06 | No Patient Intake / Medical Contraindications Screening

**Status: ✅ RESOLVED Day 48** — `patient-intake-form.md` exists (see `reading-order.md` PHASE 10). Audit was stale.

Pregnancy massage has specific contraindications. Before a massage therapist touches a patient, they need (for QC review against the existing doc):
- Gestational age confirmation
- Presence of conditions that contraindicate massage: placenta previa, pre-eclampsia, PUPPP rash, active DVT/clot history, severe morning sickness, abdominal pain
- Medications that affect touch sensation or clotting
- Patient preferences (pressure, areas to avoid)

~~Without a structured intake form, the massage therapist is blind.~~ `patient-intake-form.md` now exists (Day 48). If a patient with a contraindicated condition receives massage and has an adverse outcome despite screening, GTT Center Perth still carries liability — ensure the form is used consistently.

---

### OG-07 | No Privacy Policy or Data Handling Procedure

**Status: ✅ RESOLVED Day 48** — `privacy-policy.md` exists (see `reading-order.md` PHASE 10). Audit was stale.

The waitlist form collects: name, email, suburb, due date, gestational age, services interested. This is sensitive health information under the Privacy Act 1988 (Cth) Schedule 1 (sensitive information = health information).

Requirements:
- Privacy Policy document published on website before first data collection
- Privacy Collection Notice at point of data collection
- Data storage and security procedures
- Data breach response plan (documented — not just "call solicitor")
- Right of access and correction procedures

~~None of these exist. Collecting the waitlist without a privacy policy is a Privacy Act breach from Day 1.~~ `privacy-policy.md` now exists (Day 48) — for QC review, confirm it covers the requirements above.

---

### OG-08 | No No-Show/Cancellation Rate in Financial Model

Industry standard wellness no-show rate: 10–15%. GTT patients are a better bet (they have a medical test booked) but wellness-only afternoon bookings are more discretionary.

At a conservative 10% no-show rate across 330 visits/month = 33 visits lost.
At A$225 avg GTT and A$175 avg wellness: ~A$7,000/month in lost revenue not modelled.

The ops manual has a cancellation policy (A$30 deposit forfeited) but the financial model doesn't model the effective net revenue reduction from cancellations.

**At 10% no-show, the stable-operations profit drops from A$29,192 to ~A$22,192/month. Break-even moves from 108 to ~120 visits/month.** *(original analysis retained for audit trail)*

**⚠ Day 50 update — this risk is now severe, not marginal:** post-reconciliation, stable-operations profit is **A$5,646/month** (not A$29,192). At a 10% no-show rate (~A$7,000/month lost revenue, per the original analysis above), stable-operations profit would turn **negative (~A$(1,354)/month)**. OG-08 remains UNRESOLVED — no-show/cancellation modelling should be added to `cash-flow.md` as a priority, given the much thinner post-Day-50 margin.

---

### OG-09 | Phlebotomist Hire Has No Recruitment Plan

"Hire by Week 7 — must be credentialed by WDP/PathWest before venue opens."

There is no:
- Job advertisement written
- Recruitment channels identified (AIMS job board mentioned — but no LinkedIn strategy, no Seek job posting, no hospital network outreach plan)
- Salary competitiveness confirmed (HPSS HP L2 = A$27–30/hr vs private pathology market rate A$28–35/hr — GTT Center Perth may be below market)
- Interview process defined
- Background check process documented (police clearance, Working with Vulnerable People — who processes these?)

Phlebotomist is the single most critical hire. A weak recruitment plan is a single point of failure for the entire clinical model.

---

### OG-10 | No Financial Infrastructure Setup Plan

Before first revenue:
- Trust bank account (separate from any existing trust accounts)
- EFTPOS terminal (who supplies? Square, Tyro, or bank terminal?)
- Fresha Pay configuration (card-on-file for deposits and no-shows)
- Xero connected to trust ABN
- GST registration with ATO
- BAS lodgement schedule
- Business credit card for expenses

None of this is documented or assigned. Bruno (Finance agent) is responsible but has no setup checklist.

---

### OG-11 | No Glucose Drink Expiry Management

The supply management section tracks reorder thresholds for glucose solution but doesn't address expiry dates. Polycal and commercial glucose drinks (Glucola) have shelf lives of 12–24 months. Using an expired glucose drink:
- May affect test validity
- Could trigger WDP specimen rejection
- Creates a clinical liability

Required: First-in-first-out (FIFO) rotation protocol, expiry date tracking in the supply log, and a procedure for disposing of expired stock.

---

## SECTION 4 — MISSING DOCUMENTS

These documents are referenced or implied but don't exist.

| Priority | Document | Why Needed | Owner |
|---|---|---|---|
| 🔴 Blocking | docs/consent-form.md | Legal — patient consent before any blood collection | Cora + solicitor |
| 🔴 Blocking | docs/privacy-policy.md | Legal — required before waitlist collection begins | Solicitor |
| 🔴 Blocking | docs/emergency-plan.md | WHS compliance — WorkSafe WA requirement | Grace + Operations Director (TBD) |
| 🔴 Blocking | docs/website-spec.md | Marketing — nothing works without a website | Poppy + developer |
| 🟡 High | docs/brand-guide.md | Marketing consistency — Instagram + all materials | Poppy |
| 🟡 High | docs/patient-intake-form.md | Clinical safety — massage contraindications | Cora + massage therapist |
| 🟡 High | docs/financial-setup.md | Operations — bank, EFTPOS, Xero, ABN, GST setup | Bruno |
| 🟡 High | docs/afternoon-marketing-plan.md | Revenue — afternoon slot fill requires separate strategy | Poppy |
| 🟡 Medium | docs/booking-system-spec.md | Operations — GTT timing constraint logic | Ivy + developer |
| 🟡 Medium | docs/phlebotomist-job-posting.md | Hiring — most critical hire, needs JD now | Fern |
| 🟢 Useful | docs/refund-dispute-policy.md | CX — what happens with bad service/non-delivery | Jade |
| 🟢 Useful | docs/competitor-monitoring.md | Strategy — how to track copycat risk | Grace |

---

## SECTION 5 — IMPROVEMENT OPPORTUNITIES

Upside: revenue increases, moat strengthening, cost savings.

---

### IM-01 | GDM Follow-Up Pathway = Recurring Revenue

1 in 6 GTT patients (~55/month at stable) will receive a GDM diagnosis. These women:
- Need ongoing dietary support for the rest of pregnancy (10–14 weeks)
- Many will need post-birth follow-up (GDM increases T2DM risk long-term)
- Are anxious and actively seeking guidance

The dietitian sublet is positioned as a one-off. Reconfigure it as a structured GDM follow-up programme:
- 3-session package (initial consult + 2 follow-ups): A$450–600
- GTT Center Perth takes 15% referral fee from dietitian
- Adds A$2,500–4,500/month additional revenue at full penetration
- Differentiates from any future competitor (end-to-end GDM pathway vs just a lounge)

---

### IM-02 | Corporate / Antenatal Group Bookings

Antenatal education classes (hospital and private) group all their students in the same gestational week cohort. A group GTT booking (8–10 women from the same class, same morning) fills the entire morning wave in one booking.

- One corporate/antenatal class partnership = 8–10 guaranteed bookings per cohort
- Perth's major hospitals run antenatal classes: KEMH, SCGH, St John of God, Joondalup Health
- Private midwives often run their own group antenatal sessions

Not in Reed's partnership list. Should be.

---

### IM-03 | VIP Package at A$495+

Current maximum package: A$395 (Complete — massage + nails + scan).

A VIP tier at A$495–595 could include:
- All Complete inclusions
- Professional bump photography (partner photographer, 20 min)
- Branded keepsake box (Gaia/Weleda/Mustela products — A$40–60 cost)
- Personalised handwritten note from Operations Director
- Priority booking confirmation

This is pure margin improvement — labor cost barely increases, product cost ~A$60. At 15% of GTT bookings taking VIP: +A$3,000–4,000/month revenue.

---

### IM-04 | WDP Co-Marketing (Free Acquisition Channel)

WDP sends pathology request paperwork to pregnant women. If GTT Center Perth is WDP's Licensed Collection Centre, WDP could include a GTT Center Perth insert in their patient communications or on their website.

- Zero cost to GTT Center Perth
- WDP has incentive (premium LCC improves their brand)
- Should be negotiated as part of the WDP partnership agreement

Not mentioned anywhere in current documents.

---

### IM-05 | SEO Content Strategy (Zero Competition)

"GTT test Perth" — zero commercial results currently. A 10-page content strategy would own this search term within 90 days of launch.

Suggested pages:
1. What is the GTT test? (educational)
2. How to prepare for your GTT test (fasting instructions, what to bring)
3. GTT test Perth — what are your options?
4. What happens if I test positive for GDM?
5. Pregnancy massage Perth
6. Safe nail services during pregnancy Perth
7. Gestational diabetes diet — what to eat
8. GTT Center Perth vs standard pathology — comparison
9. Is the GTT test painful?
10. GDM diagnosis in Perth — where to get support

Each page: 800–1,200 words, internal links, schema markup. Estimated organic traffic within 6 months: 200–500/month. Conversion rate 10% = 20–50 extra leads/month. Zero ad cost.

Not assigned to anyone. Poppy's marketing plan focuses on Instagram only.

---

### IM-06 | Postnatal Market (Immediate Extension)

The business plan mentions postnatal expansion "Year 2" but doesn't develop it. New mothers (0–12 months post-birth) are a natural adjacent market:
- Same staff (postnatal massage)
- Same venue
- Massive unmet need in Perth
- Can book the same afternoon slots
- GTT patients convert naturally to postnatal customers

Starting Month 6 (not Year 2): introduce 1 postnatal massage slot per afternoon. No additional cost. Tests demand before committing.

---

### IM-07 | Retail Margin Improvement

Current retail projection: A$800/month (A$8–10/visit average). This is actually very low for a captive premium audience who is there for 2.5 hours.

MIWM Melbourne reportedly does significant retail sales. Products to consider:
- Gaia, Weleda, Mustela: pregnancy skincare (A$15–45/item)
- Pregnancy pillows: A$40–90
- TENS machines for hire → sell (trade-up if they buy)
- Branded GTT Center Perth merchandise (tote bag, tumbler)

At A$25 retail average × 330 visits = A$8,250/month vs current A$800 projection. This requires a proper retail strategy, not just "retail = A$8/visit."

---

### IM-08 | Midwife Lunch-and-Learn Programme

Reed's partnership strategy focuses on referral cards. A stronger moat: invite midwife practices to GTT Center Perth for a 30-minute paid lunch-and-learn (A$30–50 voucher + lunch).

They experience the venue themselves. They see the collection room. They meet the Operations Director. They become advocates not just referrers.

1 lunch-and-learn per quarter, 8–10 midwives attending = 10 new referral relationships per quarter. Much stronger than a referral card drop.

---

### IM-09 | Prenatal Yoga / Education Class Partnership

A prenatal yoga instructor uses the GTT Center Perth afternoon lounge 2x/week:
- Room sublet income for GTT Center Perth (A$100–200/session = A$800–1,600/month)
- Prenatal yoga students become GTT Center Perth customers (captive acquisition)
- Builds community around the brand
- Uses space that is otherwise idle on weekday afternoons

---

### IM-10 | Second Phlebotomist Hire Trigger Should Be Earlier

**Status: ✅ RESOLVED Day 49 (exceeded)** — both phlebotomists now hired pre-launch (Day 1), not Month 2/3/6. See financial-break-even-staff.md (12-staff payroll, A$675,589/yr) and operations-manual.md (verified 8-client/2-chair timetable).

*(original analysis retained below for audit trail)*

Current plan: second phlebotomist at Month 6 "if waitlist overflow justifies."

With a 300+ waitlist at opening, Month 1 will have demand. The scheduling bottleneck (CF-02) means 5 is the safe daily maximum with 1 phlebotomist. At 330 visits/month target (8 GTT/day), you need a second phlebotomist from Month 3, not Month 6.

Hire a part-time sessional phlebotomist (3 days/week) at Month 2 to cover peak Wave 1+2 mornings. Cost: ~A$1,800/month. Revenue unlock: +2 GTT slots/day × 22 days × A$225 = +A$9,900/month. ROI: 5.5:1.

---

### IM-11 | Instagram during fit-out needs a shoot plan

The marketing plan says "behind-the-scenes fit-out content." Without a photographer and a shot list, fit-out Instagram content will be low-quality phone photos of construction. For a premium maternity brand, this sets the wrong first impression.

Budget: A$500–800 for 1 professional shoot session during fit-out peak (venue starting to look beautiful). 20 images. Content calendar planned from these 20 images for the first 4 weeks.

---

### IM-12 | Operations Director Needs a Deputy / Cross-Training Plan

The Operations Director is the single point of failure for:
- Opening the venue (only documented key holder)
- First response for clinical incidents
- WDP liaison
- Payroll approval
- Staff management

If Operations Director is unavailable for 1 week, the business has no fallback. No deputy is named. No cross-training plan documented.

Minimum required: receptionist cross-trained as backup opener; phlebotomist cross-trained as backup clinical incident first responder; Bruno (finance agent) can run payroll without Operations Director's daily input.

---

## ACTION PRIORITY LIST

### Must Fix Before Lease is Signed
1. ~~Resolve TPI/DVA pension question with DVA-qualified advisor (CF-07)~~ **Removed from this GTT action list 2026-07-19 — Anthony's personal matter, handled by him directly, not a GTT Center Perth task (stated twice). CF-07's underlying legal analysis above is unchanged; only its tracking as an action item here is removed.**
2. Resolve staff hours conflict — full-time or part-time? Update all cost models (CF-01)
3. Contact WDP AND PathWest simultaneously (CF-03)
4. Write privacy-policy.md before any waitlist collection begins (OG-07)
5. Draft patient consent form (OG-02)

### Must Fix Before Instagram Launch (Week 9)
6. Build website — assign developer, write website-spec.md (OG-05)
7. Write brand-guide.md (IM-11, IM-05)
8. Align package names and prices across all documents (CF-04)
9. Fix Saturday/Mon-Fri contradiction (CF-05)

### Must Fix Before First Patient
10. Write emergency-plan.md (OG-03, WorkSafe WA requirement)
11. Write patient-intake-form.md for massage contraindications (OG-06)
12. Complete financial-setup.md — bank, EFTPOS, Xero, STP (OG-10)
13. Post phlebotomist job advertisement — SEEK + AIMS (OG-09)
14. Update cash flow to reflect: correct break-even with full-time staff, no-show rate, GST-exclusive revenue (CF-01, CF-06, OG-08)

### Growth Actions (Month 1–3)
15. Develop afternoon demand generation strategy — separate from GTT referral funnel (OG-04)
16. Build SEO content strategy — 10 pages targeting GTT/pregnancy Perth (IM-05)
17. Add GDM follow-up programme to dietitian sublet agreement (IM-01)
18. Add VIP package tier A$495+ to booking system (IM-03)
19. Negotiate WDP co-marketing as part of partnership agreement (IM-04)
20. ~~Plan second phlebotomist hire for Month 2/3 — not Month 6~~ — ✅ DONE Day 49: both phlebotomists hired Day 1 (IM-10)

---

*Audit completed by: Idea Lobster (Claude — Idea Lobster mode) | June 2026*  
*Document owners: Grace (Operations), Bruno (Finance), Cora (Clinical), Jade (CX)*  
*All findings require Anthony sign-off before remediation begins*

---

## Changelog

**2026-07-19** — Founder decision (confirmed 2026-07-18): updated the OG-03 historical finding to reflect the current emergency-plan.md wording ("Venue Manager stays with patient", not "Imara"). Added a clarifying note to CF-07 distinguishing the (unchanged) Imara personal TPI/trust-distribution question from the new, separate Venue Manager payroll role. CF-07's substantive legal analysis about Imara's remuneration and TPI means-testing is unchanged and still requires DVA-adviser sign-off — see `financial-model.md`/`research.md`/`dva-tpi-research.md`.

**2026-07-19 (founder feedback round 3)** — Removed the DVA/TPI item from the "Must Fix Before Lease is Signed" action list — Anthony's personal matter, not a GTT Center Perth task, stated twice. CF-07's underlying legal analysis is unaffected; only its tracking as an active GTT action item is removed.
