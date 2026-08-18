# Staff Profiles, Coverage Model, and Relief Pool Sizing

**Date:** 2026-08-17 | **Purpose:** Comprehensive staff profiles for every position at the 18-client/day (Table 1) planning model, plus a real headcount-with-coverage analysis (annual leave, sick leave, relief, operational resilience) — not just the bare committed headcount.

---

## 1. Coverage Model — Why the Bare Committed Headcount Is Not Enough

The committed design headcount (8 treatment staff + 2 phlebotomists + 1 Venue Manager) is the number required to run a single day at full 18-client volume with zero absences. It is not a safe operating headcount on its own — any single sick day or leave request with no backup would either cancel bookings or force the venue below its committed capacity on that day.

**Phlebotomists (highest coverage risk — only 2 committed, both required simultaneously for both chairs to run):**
- Committed: 2, both rostered every trading day.
- **RECALCULATED 2026-08-18 — recommended coverage pool: 4 phlebotomists on the books** (was "3-4", now a single recommended figure, quantitatively derived — see `docs/architecture/STAFFING-COVERAGE-VALIDATION.md` §2 for the full binomial reliability calculation: n=4 gives 99.81% reliability against a 92% per-person availability assumption, deliberately held above the 95% minimum given zero cross-training capability and the WDP credentialing lead time). Not all 4 rostered every day — only paid for actual worked hours.
- Rationale: phlebotomy requires a specific pathology-partner credential (Chapter 12) — a same-day replacement cannot be sourced casually the way a beauty therapist shift gap might be covered; the lead time to get a new phlebotomist credentialed under the partner's accreditation is real and non-trivial. A standing pool of extra credentialed phlebotomists is the only realistic mitigation.
- **WDP employment-arrangement dependency, restated:** whether phlebotomists are ultimately employed directly by this venture or supplied by WDP under a service-fee arrangement remains open, waiting on Carole Rivers — this headcount/wage figure assumes direct employment; not actioned further this round.

**Treatment staff (common AM/PM pool):**
- Committed: 8 (4 Massage+Beauty pool + 2 Nails + 2 Hair).
- **RECALCULATED 2026-08-18 — recommended: 12 on the books** (was "10-11", now quantitatively derived via binomial reliability targeting ≥95% of trading days fully staffed per line — see `docs/architecture/STAFFING-COVERAGE-VALIDATION.md` §1 for the full calculation: 6 Massage+Beauty + 3 Nails + 3 Hair). An 11-person alternative (5+3+3, ~94.6% reliability on the Massage+Beauty line) is disclosed as a defensible lower-reliability option if a smaller pool is preferred. Rostered across both AM and PM as the common pool already established.
- This is a reliability-driven recommendation, not a cost-minimisation exercise, per Anthony's explicit objective (`docs/architecture/STAFFING-COVERAGE-VALIDATION.md` intro).

**Venue Manager:**
- Committed: 1, covering AM operations and reception (see §3 below).
- **RECALCULATED 2026-08-18 — confirmed no permanent relief VM is recommended at launch scale** (`docs/architecture/STAFFING-COVERAGE-VALIDATION.md` §3: the cost of a second salaried, dual-qualified, service-capable manager is disproportionate to a single-site venue at this stage). Genuinely a single point of failure, flagged honestly rather than smoothed over. Realistic mitigation: cross-train at least one senior treatment staff member or the PM Reception coordinator in basic opening/reception procedures as an emergency fallback (not full VM capability); accept the disclosed residual risk of an ad hoc arrangement for a genuine VM absence until scale justifies a second hire.

**Reception/Coordinator (PM-hours role, distinct from the VM's own AM reception coverage):**
- 1 role, lighter hours, covering the PM window specifically (see §3 for the reasoning this role exists at all).
- **RECALCULATED 2026-08-18 — a small on-call relief pool (1 additional person, cross-trained on Fresha/payment administration) is now recommended**, closing the previously-disclosed 15:00-18:00 no-coverage gap. Compared against 3 structural alternatives (VM extending hours, treatment staff assisting, a rotating relief-only model) — dedicated PM Reception with this small backup remains the recommended structure. Full comparison: `docs/architecture/STAFFING-COVERAGE-VALIDATION.md` §4.

**2026-08-18 audit round addendum — five distinct staffing concepts, not to be conflated:** required operating positions (the functional roles), actual scheduled weekly hours (per the solver-verified timetable), employment headcount required (real people employed), relief/backup pool (additional people, only paid when covering an absence), and paid hours actually included in the financial model (committed headcount's full rostered shift only, relief pool excluded from steady-state payroll unless an absence actually occurs) are five different numbers and must not be used interchangeably. Full structural breakdown: `docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §9.

## 2. Staff Profiles

### Position 01 — Venue Manager

**Role purpose:** Operational leadership of the venue and its people, covering reception duties personally during the AM window (not a separate "Managing Director" role — corrected 2026-08-17, this position is operational, hands-on, and reception-facing in the morning, not a purely administrative executive title).

**Job description:** Runs daily venue operations, manages staff rostering and performance, is the first-response contact for any clinical or customer incident, liaises with the pathology partner, and personally staffs reception during the AM window.

**Job tasks:** Opening/closing procedures; AM reception (greeting, check-in, Fresha calendar management) personally, not delegated; staff rostering and Fair Work compliance; weekly P&L review; incident management; pathology-partner liaison.

**Responsibilities:** Full accountability for the venue's day-to-day operation, staff welfare, and compliance.

**Hours:** 07:00-15:00 (8-hour AM-weighted shift, covering the client-facing AM window plus wind-down).

**Roster pattern:** Monday-Saturday, fixed (not rotating), since this is the one role the venue's operational continuity depends on most directly.

**Wage:** **CORRECTED 2026-08-18 (Phase C audit round)** — this role was previously priced against the Clerks Award MA000002 Level 2 casual rate (A$36.81/hr), audited and found to be a likely misclassification. This role's own job description below (runs daily venue operations, manages staff rostering/performance, requires a genuine service qualification) matches the Hair & Beauty Industry Award MA000005's own Level 6 classification ("Diploma-qualified beauty therapist or salon manager responsible for staff and operations") far more closely than a generic clerical award. Current best-evidenced rate: **A$40.00/hr** (MA000005 Level 6 casual, 2026/27, includes 25% casual loading) — or a salaried equivalent once converted from casual, per the venture's own "casual initially, review for conversion" policy. **Status: MODELLED/CORRECTED, NOT VERIFIED** — a specific real employment contract's award classification should still be confirmed with an accountant or Fair Work professional before being treated as final. Full reasoning: `docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §3c/§15.

**Employment type:** Salaried from Day 1 (the one confirmed exception to the "all staff casual initially" rule, given the critical-path, safety-and-compliance-adjacent nature of the role).

**Required qualifications:** A genuine service qualification (Cert III/IV in Beauty Therapy, Massage, or Hairdressing) or a dual qualification spanning two of these — this is a real, corrected requirement (previously not stated), reflecting the desirability that the VM can step into treatment/service work if the roster genuinely needs it, not just supervise it.

**Desirable qualifications:** Prior venue/salon/day-spa management experience; First Aid/Fire Warden certification (a real, separate compliance requirement per `docs/emergency-plan.md`, distinct from the service qualification above).

**Coverage requirements:** No dedicated relief VM at launch — a genuine single point of failure, disclosed not hidden. First Aid/Fire Warden backup certification should exist in at least one other staff member so the venue is never without emergency-response coverage if the VM is briefly unavailable on-site.

**Leave/relief considerations:** As a salaried role, standard NES annual/personal leave entitlements apply once converted from casual — genuinely requires either a second trained VM-capable staff member or an external relief arrangement before the venue can safely cover a VM's own leave, not resolved in this document.

**Reporting line:** Reports directly to Anthony Zed/YETI Tipi Holdings (the ownership layer) — no intermediate management tier exists at this venture's scale. Every other position (§Positions 02-06 below) reports to the Venue Manager.

**Experience:** No minimum years specified anywhere in this repo's prior research — genuinely unresolved, not assumed. A defensible planning assumption (2+ years in a supervisory beauty/wellness/hospitality role) is suggested here for hiring-brief purposes only, explicitly flagged as NOT independently researched or sourced this round.

**Super/workers comp:** 12% superannuation (universal, `wages.yml#wage_superannuation_rate`) + 1.7% workers compensation (`wages.yml#wage_workers_comp_rate`, PLACEHOLDER — not upgraded to VERIFIED this round, see `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §10) — both applied identically to every position in this document, not restated per-position below.

**Skills:** Staff rostering/Fair Work compliance literacy; Fresha (or equivalent booking platform) administration; basic P&L literacy (weekly review); incident-management composure; genuine hands-on service delivery capability (per the required qualification above).

**Compliance:** First Aid/CPR certification (mandatory, `docs/emergency-plan.md`); Fire Warden certification (mandatory); WA Working with Children Check NOT required (no unsupervised minors in this venture's service model); RSA not required (no licensed premises).

**Cross-training/substitution capability:** The VM's own required service qualification (Cert III/IV) means the VM CAN step into a treatment-staff shift in a genuine emergency — but this leaves reception/management duties uncovered simultaneously (see `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §6), so it is not a free substitution. No other position can substitute for the VM's own management/compliance responsibilities.

### Position 02 — Phlebotomist (×2 committed, ×4 on the books, RECALCULATED 2026-08-18)

**Role purpose:** Perform GTT blood collection under the pathology partner's accreditation umbrella.

**Job description:** Conducts fasting, 1-hour, and 2-hour draws for each AM client pair, following the pathology partner's collection protocol and the venue's own synchronized two-chair schedule.

**Job tasks:** Client identification and consent confirmation; venepuncture at each of the three fixed clinical marks; specimen labelling, storage, and courier handover per the pathology partner's requirements.

**Responsibilities:** Clinical accuracy and patient safety at the single highest-anxiety point in the client journey; strict adherence to the partner's collection-centre protocol (Chapter 12).

**Hours:** 07:00-13:00 (AM window only — phlebotomists are not rostered for any PM/general-venue duties, a settled, non-negotiable scope boundary).

**Roster pattern:** Monday-Saturday, 2 rostered per trading day (Chair A/Chair B), drawn from a pool of 4.

**Wage:** Current researched Health Professionals and Support Services Award MA000027, Support Services Level 1-2 casual rate, A$33.71-35.04/hr (2026-08-16 research; the venue's specific "Pathology Collector Cert III/IV" role does not map to an exact single classification, closest-match caveat disclosed).

**Employment type:** Casual initially, reviewed for conversion once regular hours are proven.

**Required qualifications:** Cert III/IV in Pathology Collection, credentialed under the pathology partner's own NATA-accredited umbrella (not an independent accreditation held by the venue).

**Coverage requirements:** See §1 above — 4 on the books (recalculated, binomial reliability method), not all rostered daily.

**Leave/relief considerations:** Genuinely the tightest coverage constraint in the whole staffing model, given the credentialing lead time — the relief pool size recommendation above exists specifically to address this.

**Reporting line:** Reports to the Venue Manager (Position 01). No dedicated clinical-lead position exists above the phlebotomist role at this venture's scale — clinical protocol authority sits with the pathology partner (WDP or equivalent), not an internal role, per the partner-credentialed accreditation model.

**Experience:** Not independently researched this round — genuinely unresolved. Real-world pathology collection centres typically expect prior collection-centre experience alongside the Cert III/IV, but this venture has not sourced a specific minimum from WDP or an equivalent partner.

**Skills:** Venepuncture proficiency across a range of patient presentations (including pregnancy-specific considerations); calm, reassuring bedside manner (the single highest-anxiety point in the client journey, per the job description above); precise specimen labelling and chain-of-custody discipline.

**Compliance:** Pathology partner's own Licensed Collection Centre QMS (Quality Management System) induction and ongoing compliance — this is the credentialing umbrella itself, not a separate requirement. First Aid/CPR desirable but not the primary compliance requirement (the partner accreditation supersedes it clinically).

**Cross-training/substitution capability:** **None** — phlebotomy cannot be cross-covered by any other position in this venture (`docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §7). This is the one position in the whole staffing model with zero substitution capability from any other role, which is precisely why its own relief-pool sizing (§1 above) is the most conservative (proportionally) of any position.

**Employment-arrangement dependency, flagged not assumed:** whether phlebotomists are ultimately employed directly by this venture or supplied/employed by the pathology partner under a service-fee arrangement is a still-open commercial question, waiting on WDP/Carole Rivers — see `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §7 for the full disclosure. This profile's wage figure assumes direct employment; that assumption may not hold.

### Position 03 — Treatment Staff, Massage+Beauty pool (×4 committed, common AM/PM pool)

**Role purpose:** Deliver massage and beauty/facial services across both the AM window (as part of GTT packages and gap-fill) and the PM window (standalone and package bookings) — one role, not two, per the venue's common-pool staffing model.

**Job description:** Delivers pregnancy-safe massage and beauty/facial treatments per the service catalogue, rostered flexibly across AM and PM per actual booking demand.

**Job tasks:** Full-quality massage/facial service delivery within the fixed AM package slot times or PM booking durations; maintaining pregnancy-safe product/technique standards.

**Hours:** Staggered per first-client service time (see the Operating Hours section of the dossier), minimum 3-hour engagement, released early if the final 2-3 hours of a pencilled shift aren't needed.

**Roster pattern:** Booking-driven, not a fixed daily headcount — rostered to what confirmed bookings actually require that day.

**Wage:** Current researched Hair & Beauty Industry Award MA000005 Level 4 casual rate, A$37.50/hr (2026-08-16 research).

**Required qualifications:** Cert IV in Massage Therapy and/or Beauty Therapy (dual-qualification preferred, per the confirmed Massage+Beauty pool pairing).

**Desirable qualifications:** Pregnancy-massage-specific specialisation.

**Coverage requirements:** Part of the 12-strong common treatment pool (§1, recalculated 2026-08-18 via binomial reliability method).

**Reporting line:** Reports to the Venue Manager (Position 01).

**Experience:** Not independently researched this round — genuinely unresolved, no minimum years sourced.

**Skills:** Pregnancy-safe technique adaptation (positioning, pressure, product selection) across both massage and beauty/facial modalities; time-discipline within the fixed 45-minute AM service blocks (a real constraint per the exact-clinical-mark timetable, `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §2).

**Compliance:** Standard beauty-industry infection-control/hygiene practice; product safety awareness for pregnancy-safe formulations (no accreditation body governs this specifically — an internal training/induction requirement, not an external certification).

**Cross-training/substitution capability:** Massage and Beauty are dual-qualification-paired as ONE shared pool (the venue's own confirmed common-pool model) — this pairing IS the cross-cover mechanism between these two specific service lines. NOT confirmed cross-qualified with Nails or Hair (`scenario-c-sync-timetables.md` §0.4 — no confirmed Nails+Hair pairing either).

### Position 04 — Treatment Staff, Nail Technician (×2 committed, common AM/PM pool)

**Role purpose, hours, roster pattern, employment type:** Same structure as Position 03.

**Wage:** MA000005 Level 3 casual rate, A$36.81/hr (2026-08-16 research).

**Required qualifications:** Cert III in Nail Technology.

**Operational note:** 4 physical nail stations exist day-one (Chapter 7), but only 2 are staffed at the committed 18-client volume — the extra 2 stations provide rostering flexibility and PM standalone-booking headroom, not a mandatory extra hire.

**Reporting line:** Reports to the Venue Manager (Position 01).

**Experience:** Not independently researched this round — genuinely unresolved.

**Skills:** Gel/SNS/acrylic application proficiency (per the service catalogue); time-discipline within fixed AM service blocks (same 45-minute constraint as Position 03).

**Compliance:** Standard nail-industry infection-control (tool sterilisation, single-use files where applicable) — an internal training/induction requirement, no external accreditation body specific to this role in WA beyond the Cert III itself.

**Cross-training/substitution capability:** NOT confirmed cross-qualified with any other line (Massage+Beauty pool, or Hair) — `scenario-c-sync-timetables.md` §0.4 explicitly flags no confirmed Nails+Hair pairing. The 2 Nail Technicians can only substitute for each other.

### Position 05 — Treatment Staff, Hairdresser (×2 committed, common AM/PM pool)

**Role purpose, hours, roster pattern, employment type:** Same structure as Position 03.

**Wage:** MA000005 Level 3 casual rate, A$36.81/hr (2026-08-16 research).

**Required qualifications:** Cert III in Hairdressing.

**Operational note:** Same 2-of-4-stations principle as Nails, above.

**Reporting line:** Reports to the Venue Manager (Position 01).

**Experience:** Not independently researched this round — genuinely unresolved.

**Skills:** Blow-dry/styling proficiency matching the service catalogue's PM Restore package component and standalone offerings; time-discipline within fixed AM service blocks.

**Compliance:** Standard hairdressing hygiene/sanitation practice — internal training/induction requirement, no external accreditation body specific to this role in WA beyond the Cert III itself.

**Cross-training/substitution capability:** NOT confirmed cross-qualified with any other line (same disclosed gap as Nails, above). The 2 Hairdressers can only substitute for each other.

### Position 06 — Reception/Coordinator (PM-hours role)

**Role purpose:** Covers reception, booking management, and customer-facing coordination during the PM window specifically — this role exists because the Venue Manager's own AM-weighted hours (07:00-15:00) do not extend to the venue's 18:00 close, a genuine coverage gap identified this round.

**Job description:** PM check-in, Fresha calendar management, payment processing, phone/email enquiries, closing procedures.

**Hours:** Approximately 13:00-18:00 (lighter than the VM's own hours, sized to the PM window only), exact hours to be confirmed against real PM booking-volume data once trading.

**Wage:** Current researched Clerks Award MA000002 Level 1 casual rate, A$33.71/hr (2026-08-16 research).

**Employment type:** Casual.

**Required qualifications:** Beauty/wellness-industry customer service experience (not solely admin/medical reception background, per the venue's existing hiring preference).

**Reporting line:** Reports to the Venue Manager (Position 01) — overlaps with the VM's own rostered hours 13:00-15:00 only (`docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §4); no VM presence 15:00-18:00, a genuine, disclosed reporting/coverage gap for the back half of the PM shift.

**Experience:** Not independently researched this round — genuinely unresolved.

**Skills:** Fresha (or equivalent) booking-platform proficiency; payment processing; phone/email customer service; basic retail/upsell conversation ability (per the venue's ancillary-retail offering).

**Compliance:** No external accreditation required — an internal training/induction role.

**Cross-training/substitution capability:** No confirmed backup — see §1's relief-pool gap and `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §8 for the full disclosure (genuinely unresolved, not assumed zero-risk). The Venue Manager could plausibly cover a SHORT absence during the 13:00-15:00 overlap window only, not during 15:00-18:00.

## 3. Reception Coverage — the 07:00 vs 07:15 Inconsistency, Corrected

**Previous inconsistency (corrected this round):** an earlier document had reception "opening" at 07:15, 15 minutes after the first client's 07:00 arrival — a real, disclosed inconsistency, now fixed. **The Venue Manager personally covers reception from the venue's actual 07:00 opening**, per Position 01's corrected job description above — there is no gap between the first client's arrival and reception being staffed. The separate Reception/Coordinator role (Position 06) covers the PM window, not the AM open.

---

## Changelog

**2026-08-18 (Phase D)** — Completed the full field list Anthony specified: reporting line, experience (honestly flagged as not independently researched where genuinely unresolved, not invented), skills, compliance, cross-training/substitution capability added to all 6 positions. Cross-referenced against `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` (new this round) rather than duplicating its timetable/reconciliation content. Every position's substitution capability is now stated explicitly, including the genuine gaps (Phlebotomy: none; Nails/Hair: only within their own line; PM Reception: none confirmed, VM can only partially cover a 13:00-15:00 window). **Now COMPLETE** for the field list itself — the underlying open items (VM wage professional confirmation, PM Reception relief sizing, phlebotomist WDP-employment dependency) remain genuinely open and are cross-referenced, not hidden by marking this document complete.

**2026-08-18 (audit round)** — Corrected Venue Manager wage from Clerks Award MA000002 L2 ($36.81/hr, audited and found likely misclassified) to Hair & Beauty Industry Award MA000005 L6 ($40.00/hr, the role's own real award match) — flagged MODELLED/CORRECTED, not VERIFIED, professional confirmation still needed. Added the five-distinct-staffing-concepts cross-reference and flagged PM Reception's own relief pool as a genuinely unresolved open item (was previously silent on this). Full reasoning: `docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §3c/§9/§10/§15. **Still not done this pass (disclosed gap, not silently deferred):** the full field list Anthony specified (reporting line, years of experience, explicit super/workers-comp fields per role, detailed skills/compliance/cross-training matrix) is only partially present in the profiles below — hours, wage, qualifications, and coverage are present for every position; reporting line, experience level, and a dedicated skills/compliance/cross-training matrix are NOT yet built out. Flagged as PARTIAL, not COMPLETE.

**2026-08-17** — Created per the founder's explicit instruction for comprehensive staff profiles (all listed fields), a real coverage/relief-pool analysis, and correction of the Venue Manager role (no "Managing Director" framing, requires a service qualification, covers AM reception personally, current researched wage rate) and the 07:00/07:15 reception-opening inconsistency.
