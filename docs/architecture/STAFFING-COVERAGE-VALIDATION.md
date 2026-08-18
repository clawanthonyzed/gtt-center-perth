# Staffing Coverage Validation — Recalculated Against the Corrected Model

**Date:** 2026-08-18 | **Purpose:** Priority 2 of this round's brief — recalculate (not just re-state) the treatment staff, phlebotomist, Venue Manager, and PM Reception coverage requirements against the current, PM-capacity-corrected financial model (`docs/architecture/PM-CAPACITY-RECONCILIATION.md`), using a real, quantified relief-pool method instead of a round-number estimate. Objective, stated explicitly per Anthony's brief: **not minimising wages — a staffing structure that operates reliably without Anthony personally firefighting daily.**

---

## 0. Does the PM Capacity Correction Change Any Headcount Number? — Checked Directly, Not Assumed

**No — checked and confirmed.** The PM capacity/transaction correction (2026-08-18, Priority 1) changed how many CLIENT TRANSACTIONS 16 PM staff-sessions/day convert into (12.8128, not 16) — it did NOT change the underlying STAFF-HOURS capacity (4 treatment lines × 3.08hrs/role weekday, unchanged) that drives both PM labour cost and PM headcount. Treatment-staff and phlebotomist SIMULTANEOUS requirements are set by the AM peak-concurrency solver (`scenario-c-sync-timetables.md` §0.6a: 4 Massage+Beauty, 2 Nails, 2 Hair, 2 phlebotomists), which is entirely independent of PM revenue. **Conclusion: the committed simultaneous headcount (8 treatment + 2 phlebotomists) is unchanged by the PM correction.** What this document DOES recalculate, properly this time, is the RELIEF/BACKUP POOL size — previously a round-number estimate ("10-11", "3-4"), now a quantified reliability calculation.

## 1. Treatment Staff — Quantified Relief-Pool Derivation

### 1a. The Method — Stated Explicitly, Not a Black Box

Each treatment line (Massage+Beauty pool, Nails, Hair) requires a fixed number of staff SIMULTANEOUSLY present every trading day (the committed AM design). Casual staff are not paid-leave employees — but they DO have real, non-zero unavailability on any given day (illness, personal commitments, other casual work, no-shows). This document models that unavailability using a standard workforce-planning technique (binomial reliability), not a guessed round number.

**Disclosed planning assumption, not a verified statistic:** each individual staff member is assumed independently unavailable on ~8% of their rostered shifts (illness, personal leave without pay, other commitments — a commonly-cited planning range for casual hospitality/beauty-industry unplanned absence; NOT independently sourced against real WA hair & beauty industry absence data this round, and CANNOT be verified against real historical data for this venture specifically, since it has not opened yet). This is the single most consequential unverified assumption in this document — flagged prominently, not buried.

**Target reliability:** at least 95% of trading days fully staffed at the committed simultaneous level, for every treatment line except Phlebotomists (held to a higher ~98%+ bar, see §2, because of the clinical/partner-relationship consequence of an unstaffed collection chair).

### 1b. Calculation, Shown

Using the binomial reliability formula P(at least k of n staff available) with per-person availability 92%:

| Treatment line | Required simultaneous (k) | n=k (bare committed) | n=k+1 | n=k+2 | n=k+3 | **Minimum n for ≥95% reliability** |
|---|---|---|---|---|---|---|
| Massage+Beauty pool | 4 | 71.64% | 94.56% | 99.15% | 99.88% | **n=6** (99.15%) — n=5 (94.56%) narrowly misses the 95% bar |
| Nails | 2 | 84.64% | 98.18% | 99.81% | 99.98% | **n=3** (98.18%) |
| Hair | 2 | 84.64% | 98.18% | 99.81% | 99.98% | **n=3** (98.18%) |

**Recalculated recommended employment: 6 (Massage+Beauty) + 3 (Nails) + 3 (Hair) = 12 total**, replacing the prior round's "10-11" estimate. **This is a genuine increase, not a wage-minimisation exercise** — per Anthony's explicit objective, the number is set by a reliability target, not a cost target.

**A defensible alternative, disclosed, not hidden:** if a slightly lower reliability bar is acceptable for the Massage+Beauty pool specifically (94.56% at n=5, roughly 1 short-staffed AM in every 18 trading days ≈ 3 weeks), the total becomes 5+3+3 = **11**, matching the upper end of the prior round's "10-11" estimate almost exactly — a genuine cross-check that the earlier round-number recommendation was broadly reasonable, even though it wasn't derived this rigorously at the time. **This document's own recommendation is 12 (the ≥95%-everywhere figure)**, with 11 flagged as an acceptable, slightly lower-reliability alternative if Anthony prefers to hold the relief pool smaller.

### 1c. Qualifications, Cross-Training, Substitution — Restated From STAFF-PROFILES.md, Not Re-Litigated

- Massage and Beauty are dual-qualification-paired (Cert IV) — this pairing IS the cross-cover mechanism between these two lines, already load-bearing in the AM solver's own headcount math.
- Nails and Hair have **no confirmed dual qualification** with each other or with Massage+Beauty (`scenario-c-sync-timetables.md` §0.4) — each of these two lines can only be covered by staff qualified in that specific line. This is why they each need their own independent relief calculation (§1b above), not a shared pool.

### 1d. What Happens If One Person Calls In Sick? What If Two Do? — Answered Directly Against the Recalculated Pool

**At n=6 (Massage+Beauty), n=3 (Nails), n=3 (Hair):**
- **One person absent, any line:** fully covered — every line has at least 1 spare beyond the committed simultaneous requirement (Massage+Beauty has 2 spare, Nails/Hair have 1 spare each).
- **Two people absent, same line:** Massage+Beauty (2 spare) — still fully covered. Nails or Hair (1 spare each) — a second absence on the SAME line on the SAME day would leave that line short by 1 (a real, quantified residual risk at the 98.18% reliability level, i.e. roughly 1 day in 55 trading days). This is the honest, quantified answer to "what if two people call in sick" — not eliminated, but bounded and disclosed, consistent with never promising 100% reliability from a finite casual pool.
- **Two absences on two DIFFERENT lines, same day:** fully covered independently (each line's own buffer absorbs its own absence).

### 1e. Annual Leave, Public Holidays, Training, Turnover — Addressed, Not Ignored

- **Annual/personal leave:** casual staff (the committed employment model for all treatment positions, `STAFF-PROFILES.md` Positions 03-05) do not accrue NES paid annual/personal leave — the binomial unavailability model in §1a already implicitly captures unplanned personal absence, but does NOT separately model planned, pre-booked time off (e.g. a multi-week holiday). **Genuinely not modelled this round** — a real gap: if 1-2 of the 12-person pool are on a pre-booked multi-week absence simultaneously, the effective pool shrinks and the reliability percentages in §1b degrade accordingly. Flagged as an open operational planning item for the eventual Venue Manager (staggering pre-booked leave across the pool), not solved here.
- **Public holidays:** WA public holidays would need premium-rate coverage (not modelled in this document's cost figures, which use ordinary weekday/Saturday rates only) — a genuinely separate, not-yet-built cost line, flagged as an open item for a future costing pass.
- **Training/induction time:** not modelled as a separate cost or capacity reduction this round — a new hire's induction period would temporarily reduce the effective pool below the nominal headcount. Flagged, not quantified.
- **Turnover/recruitment gaps:** the 12-person (or 11-person alternative) pool size itself is the primary mitigation against turnover — a pool sized only to the bare committed 8 would have zero resilience to a single resignation while recruiting a replacement. Not separately quantified beyond the reliability buffer already built into §1b.

## 2. Phlebotomists — Quantified Relief-Pool Derivation, WDP Dependency Flagged

### 2a. Calculation

Required simultaneous: 2 (both chairs). Using the same binomial method, but held to a stricter internal bar given the higher consequence of an unstaffed chair (clinical process, WDP relationship, cannot substitute from any other role — `STAFF-PROFILES.md` Position 02 confirms zero cross-training capability):

| n | Reliability (P at least 2 of n available, p=92%) |
|---|---|
| 2 (bare committed) | 84.64% |
| 3 | 98.18% |
| 4 | 99.81% |

**Recalculated recommendation: 4 phlebotomists on the books** (not 3) — chosen deliberately ABOVE the 95%-reliability minimum (which n=3 already clears at 98.18%), because phlebotomy is the single highest-consequence, zero-substitution role in the entire staffing model, and the credentialing lead time to add a replacement mid-crisis is real and non-trivial (`STAFF-PROFILES.md` §1). This is a deliberate, disclosed choice to hold extra buffer on the tightest-risk role, consistent with Anthony's stated objective of operational reliability over cost minimisation. **3 remains a defensible lower bound (98.18% reliability) if Anthony prefers a smaller pool** — both figures shown, 4 is this document's recommendation.

### 2b. WDP Employment-Arrangement Dependency — Marked Dependent, Not Assumed, Not Actioned Further

**Restated from `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §7, still open, still not actioned:** whether phlebotomists are ultimately employed directly by this venture or supplied/employed by WDP under a service-fee arrangement remains genuinely open, waiting on Carole Rivers. **This document does NOT send further WDP outreach and does NOT assume an arrangement** — per the explicit standing instruction. If WDP ultimately supplies its own phlebotomists, this entire headcount/wage analysis (§2a above, and the A$11,754.19/month wage line in the financial model) could move off this venture's own payroll into a different cost structure (a per-test service fee) — a materially different shape, not modelled here, marked DEPENDENT ON THIRD PARTY.

## 3. Venue Manager — Confirmed, Not Re-Derived From Scratch

**Verified still correct, checked directly against the current STAFF-PROFILES.md and OPERATING-MODEL-18-CLIENTS.md, not assumed unchanged:**
- Operating hours: 07:00-15:00 (8hr AM-weighted shift).
- **Reception timing check: the venue's first client arrives 07:00, and the Venue Manager personally covers reception from the venue's actual 07:00 opening — confirmed still correct, no 07:00/07:15 gap** (`STAFF-PROFILES.md` §3, `OPERATING-MODEL-18-CLIENTS.md` §2's reception column — every pair's check-in is attributed to the VM starting at 07:00). This was fixed in an earlier round and has not regressed.
- AM reception + coordination duties: personally staffed, not delegated (Position 01 job description).
- Service-qualification requirement: Cert III/IV Beauty/Massage/Hairdressing or dual — real, corrected requirement (not a "Managing Director" framing).
- Staff-management duties: rostering, Fair Work compliance, weekly P&L review, incident management, pathology-partner liaison.
- Opening/closing requirements: VM covers opening (07:00); closing (18:00) is covered by PM Reception, not the VM, since the VM's own shift ends at 15:00 (§4 below).
- **Leave/sickness coverage: still a genuine single point of failure, unchanged this round.** No relief VM proposed at launch — disclosed, not hidden, consistent with every prior round's finding. **Recalculated conclusion: a permanent relief VM is NOT recommended at launch-scale** (the cost of a second salaried, dual-qualified, service-capable manager is disproportionate to a single-site, single-shift-pattern venue at this stage) — instead, the realistic mitigation is (a) cross-training at least one senior treatment staff member or the PM Reception coordinator in basic opening/reception procedures as an emergency fallback (not full VM capability), and (b) accepting the disclosed residual risk of a VM absence requiring an ad hoc arrangement (Anthony personally, or a short-notice external relief booking) until the venue's scale justifies a second manager-capable hire. This is a genuine recommendation, not a restatement of "unresolved."

## 4. PM Reception (13:00-18:00) — Structural Comparison, Not Just a Cost Check

**Four models compared on operational practicality and customer experience, not cost alone:**

| Model | Description | Assessment |
|---|---|---|
| **A — Dedicated PM Reception (current model)** | 1 person, 13:00-18:00, sole responsibility is reception/booking/payment | **Recommended.** Matches real Perth day-spa comparable practice (Le Beau, Keturah, endota — single reception desk at this scale, per `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §2a). Customer experience: consistent single point of contact for the whole PM window, no service interruption to treatment staff. |
| **B — VM extends to cover 15:00-18:00 instead** | VM works a longer shift, no separate PM Reception role | **Rejected.** Would require the VM to work an 11-hour day (07:00-18:00) every trading day — a real fatigue/retention risk for the venue's single most critical role, and removes the VM's own current 2-hour AM-wind-down/admin block (rostering, P&L review, pathology liaison) which has no other home in the schedule. |
| **C — Treatment staff assist with reception between clients** | No dedicated PM reception; a rostered treatment staff member handles check-in/payment during gaps | **Rejected.** Treatment staff are not trained in Fresha/payment-system administration as a primary skill, and pulling a treatment-staff member off the floor for reception duties during their own paid PM session window directly reduces the PM treatment capacity the whole PM revenue model depends on — self-defeating for a role whose entire purpose is generating PM revenue. Customer experience: inconsistent, treatment staff distracted from service delivery. |
| **D — Relief/part-time PM reception (no fixed daily person)** | A rotating pool covers PM reception, no single named person most days | **Rejected as the PRIMARY model, but adopted as the relief mechanism for Model A.** A rotating, unfamiliar face at reception every day is a real customer-experience downgrade (loses the "consistent point of contact" benefit) — but as the BACKUP for Model A's single dedicated person (i.e. who covers Model A's own absence), a small relief pool is exactly right. See §4a below. |

**Conclusion: Model A (dedicated PM Reception) remains the recommended structure — confirmed, not just re-stated, against 3 real alternatives with their trade-offs shown.**

### 4a. PM Reception Relief — the Genuinely Open Item, Now Given a Recommendation

Previously flagged as unresolved (`OPERATING-MODEL-18-CLIENTS.md` §8). **Recommendation this round: a small relief pool of 1 additional person, cross-trained on Fresha/payment administration, drawn from either a treatment-staff member with reception aptitude or a dedicated casual hire, on-call for PM Reception absences specifically.** This does not add to steady-state monthly payroll (only paid when actually covering an absence, per the five-concepts distinction in `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §9) — it closes the previously-disclosed 15:00-18:00 no-coverage gap (the VM's own overlap window only covered 13:00-15:00) without requiring Model B or C.

---

## 5. Recalculated Headcount Summary Table

| Position | Required simultaneous | Prior round recommendation | **This round's recalculated recommendation** | Basis |
|---|---|---|---|---|
| Massage+Beauty pool | 4 | part of "10-11" | **6** (or 5 as a disclosed lower-reliability alternative) | Binomial reliability ≥95%, §1b |
| Nails | 2 | part of "10-11" | **3** | Binomial reliability 98.18%, §1b |
| Hair | 2 | part of "10-11" | **3** | Binomial reliability 98.18%, §1b |
| **Treatment total** | **8** | **10-11** | **12** (or 11 lower-reliability alternative) | §1b |
| Phlebotomists | 2 | 3-4 | **4** | Binomial reliability 99.81%, deliberately above the 95% minimum given zero cross-training + WDP credentialing lead time, §2a |
| Venue Manager | 1 | 1, no relief | **1, no relief (confirmed, not changed)** | §3 — permanent relief VM not justified at this scale |
| PM Reception | 1 | 1, no relief sized | **1 + a small on-call relief pool (newly recommended)** | §4a |

**Financial impact of this recalculation: NONE yet — this is a headcount-establishment recommendation (who to have EMPLOYED and on the books), not a change to the STEADY-STATE PAYROLL figure.** Per the five-concepts distinction (`FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §9), relief-pool staff are only paid when they actually work a shift covering an absence — increasing the recommended employed headcount from "10-11"/"3-4" to "12"/"4" does not itself change `data/canonical/cost_ramp.yml`'s payroll figures, which already correctly model only the COMMITTED simultaneous headcount (8 treatment + 2 phlebotomists) working their full rostered shift. No canonical financial figures require updating from this section.

---

## 6. Wage/Award Verification — Priority 3, Per-Position Summary

**Labels used, per Anthony's explicit instruction this round:** VERIFIED (confirmed against a primary source) / RESEARCHED-BEST-EVIDENCED (a defensible, sourced match, not yet professionally confirmed) / MODELLED (a reasoned planning figure, no direct primary-source citation) / PLACEHOLDER (no reliable source found, explicitly flagged) / WAITING ON THIRD PARTY (depends on an external party's decision). **This section does not reopen or re-verify anything already well-supported from prior rounds — it restates the current status per position, with the label made explicit, and only investigates further where genuinely warranted.**

| Position | Award/classification | Rate | Ordinary hours | Saturday | Super | Workers comp | Other loadings | Employment status | **Label** |
|---|---|---|---|---|---|---|---|---|---|
| Venue Manager | Hair & Beauty Industry Award MA000005, Level 6 ("salon manager") | A$40.00/hr casual | 8hr AM-weighted shift | x1.5 penalty | 12%, universal | 1.7%, see below | 25% casual loading (embedded in the $40.00 rate) | Salaried from Day 1 (casual rate used as the underlying benchmark) | **RESEARCHED-BEST-EVIDENCED, NOT VERIFIED** — real award match found and reasoned (§3c of `FIRST-PRINCIPLES-FINANCIAL-MODEL.md`), but a specific real employment contract's classification still needs accountant/Fair Work confirmation before being treated as final. Not reopened further this round — the research already done stands. |
| Treatment — Massage+Beauty | MA000005 Level 4 | A$37.50/hr casual | 6hr AM shift, booking-driven PM | x1.5 penalty | 12% | 1.7% | 25% casual loading (embedded) | Casual, reviewed for conversion | **RESEARCHED-BEST-EVIDENCED** (2026-08-16 research, not reopened) |
| Treatment — Nails/Hair | MA000005 Level 3 | A$36.81/hr casual | Same as above | x1.5 penalty | 12% | 1.7% | 25% casual loading (embedded) | Casual | **RESEARCHED-BEST-EVIDENCED** (2026-08-16 research, not reopened) |
| Phlebotomists | Health Professionals and Support Services Award MA000027, Support Services Level 1-2 | A$34.375/hr casual (midpoint of A$33.71-35.04 range) | 6hr AM-only shift | x1.5 penalty | 12% | 1.7% | 25% casual loading (embedded) | Casual, reviewed for conversion | **RESEARCHED-BEST-EVIDENCED, closest-match caveat disclosed** — the venue's specific "Pathology Collector Cert III/IV" role does not map to an exact single MA000027 classification (2026-08-16 research, not reopened). **WAITING ON THIRD PARTY** for the employment-arrangement question (direct hire vs. WDP-supplied) — see §2b. |
| PM Reception | Clerks Award MA000002, Level 1 | A$33.71/hr casual | 5hr PM shift | x1.5 penalty | 12% | 1.7% | 25% casual loading (embedded) | Casual | **RESEARCHED-BEST-EVIDENCED** (2026-08-16 research, not reopened) — note this role's OWN classification was not re-examined against MA000005 the way the Venue Manager's was, because a general reception/customer-service role is a genuine Clerks Award fit, unlike the Venue Manager whose duties clearly exceeded a clerical classification. |
| Superannuation (all roles) | Superannuation Guarantee | 12% of OTE, universal application | n/a | n/a | n/a | n/a | n/a | n/a | **MODELLED** — 12% SG rate itself is a well-known current national rate (not independently re-verified against the ATO this round, since it is not in dispute), but this repo's OWN universal-application methodology (applied to 100% of every wage component, replacing the prior partial-coverage treatment) is a disclosed simplification, not independently audited. |
| Workers compensation (all roles) | WorkCover WA, industry classification not confirmed | 1.7% of direct labour | n/a | n/a | n/a | n/a | n/a | n/a | **PLACEHOLDER, UNVERIFIED — confirmed still unresolved this round, NOT converted to verified.** Two genuine attempts made across the last two rounds to obtain WorkCover WA's or Safe Work Australia's actual published rate for this venture's classification — WorkCover WA's PDF returned HTTP 403 Forbidden; Safe Work Australia's comparison table returned a network connection error (`ECONNRESET`). Both are real tooling limitations, not skipped steps. One indirect data point stands (Safe Work Australia's own reported ~1.73% national ALL-INDUSTRY average for 2024-25, with beauty/personal-care services generally lower-risk than that average) — suggestive that 1.7% may be a slight overestimate for this specific lower-risk classification, but this is inference, not verification. **Anthony or a broker should obtain the actual current WorkCover WA Premium Rating Classification rate directly — this cannot be resolved further by automated research this round.** |

**Weekly pay:** RESOLVED (research, `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §1) — not reopened, cross-checked consistent with `docs/financial-setup.md`'s own existing "Weekly payroll run (pay Friday)" convention. **Label: RESEARCHED-BEST-EVIDENCED.**

## Changelog

**2026-08-18 (Priority 2 + 3)** — Created per Anthony's explicit instruction to recalculate (not just re-validate) treatment staff and phlebotomist coverage against the operating model, using a real quantified method (binomial reliability) rather than a round-number estimate. Confirmed the PM capacity correction (Priority 1) does not change any headcount number (staff-hours capacity, which drives headcount, is unaffected — only the transaction-counting used for revenue was wrong). Recalculated recommended treatment-staff employment from "10-11" to **12** (or 11 at a disclosed lower reliability), phlebotomists from "3-4" to **4**. Confirmed VM 07:00 reception coverage has not regressed. Recommended against a permanent relief VM at this scale, with reasoning. Compared 4 structural models for PM Reception and confirmed the dedicated-single-person model, adding a newly-recommended small relief pool for the previously-disclosed 15:00-18:00 coverage gap. Added §6, a full per-position wage/award verification summary with explicit VERIFIED/RESEARCHED-BEST-EVIDENCED/MODELLED/PLACEHOLDER/WAITING-ON-THIRD-PARTY labelling, per Priority 3 -- confirmed workers compensation remains genuinely unresolved after two real, disclosed research attempts (WorkCover WA 403, Safe Work Australia connection error), not converted to "verified." No canonical financial figures changed by this document — headcount-establishment recommendations do not alter the steady-state payroll model, which already correctly prices only the committed simultaneous headcount.
