# GTT Center Perth: Executive Pitch Deck (DRAFT v0.1)

**Status:** DRAFT for Anthony's sign-off. Nothing here has been sent or published.
**Prepared by:** Grace (Operations Manager). Strategy lens: Alexander (Australian market, moat, honest sizing).
**Date:** 2026-10-10 | **Money:** all A$ (Australian dollars)
**Repo checked:** clawanthonyzed/gtt-center-perth, branch main, latest commit seen 2026-10-08.

**How to read this**
- 🟢 = confirmed in the repo | 🟡 = planning figure or in progress | 🔴 = blocked or not yet true
- "TO CONFIRM" = not in the repo, or the repo disagrees. Anthony decides.
- Every figure traces to a repo file (links at the bottom). Figures are planning estimates. There is no venue and no trading data yet.
- Acronyms are explained the first time they appear.

**Headline number choice (needs your OK).** The deck uses the repo's current canonical numbers file (CURRENT-STATE, 2026-10-03). That file shows **+A$35,186.40/month** at 18 clients a day. The older "conservative" baseline (+A$25,087.07/month, 570 visits) is marked historical in the repo. See Conflict C1.

---

## SLIDE 1: Cover

- **GTT Center Perth** (working name; SOLENA is the conditional front-runner, not locked, trademark not cleared) 🟡
- WA's first premium waiting experience for pregnant women having the Glucose Tolerance Test (GTT).
- Our research found no equivalent venue in WA. This is our own finding, not an audit.
- Pre-launch. No venue yet. No launch date set. Status: STANDBY.
- DRAFT 2026-10-10. For Anthony's sign-off only.

**Visual:** Full-bleed warm-stone photo or colour field, centred wordmark. Palette from the brand tokens (`outputs/brand/warm-stone-tokens.css`). Small "DRAFT" stamp bottom right.
**Source:** [README.md][README]; [docs/naming/NAMING-DECISION-STATE.md][NAMING]; [docs/DECISION-LOG.md][DL] (2026-08-14 entry).

---

## SLIDE 2: The Problem

- The GTT is a standard pregnancy screening test. Mothers fast first, then sit for about 2 to 2.5 hours (some sources say up to 3).
- Today that wait is a bare pathology waiting room, with blood draws at set times.
- Mothers cannot leave, cannot eat, and are often tired and uncomfortable.
- Demand is not optional. Nearly every pregnant woman is screened.
- Gap: our research found no WA venue that turns this wait into a care experience.

| Today | What mothers get |
|---|---|
| Wait time | About 2 to 2.5 hours |
| Setting | Pathology waiting room |
| Care during wait | None |

**Visual:** Simple timeline bar: fasting draw, 60 min draw, 120 min draw, with the gaps shaded "dead time".
**Source:** [docs/executive-summary.md][EXEC] (The Problem); [docs/market-research-findings.md][MKT]; [docs/business-plan.md][BP] (Market Size).
**Alexander lens:** Non-discretionary demand is the strongest asset. Marketing does not have to create the test, only the choice of where to have it.

---

## SLIDE 3: The Wellness Solution

- Turn the wait into a restorative visit: massage, nails, hair, beauty (facials, brows).
- Blood is drawn on site, in a private collection room, by GTT's own certified phlebotomists (people trained to draw blood).
- Services fit between draws. A draw never interrupts a service.
- Staff are employed (casual or permanent). Not subtenants.
- Venue and lounge access is free inside every package.
- **Not in launch scope:** 3D keepsake ultrasound (possible Phase 2; never diagnostic). Spray tan removed from the concept.

| Launch menu | Status |
|---|---|
| Pregnancy massage, facial, nails, hair, brows | 🟡 planned |
| Lounge, tea, birth plan tablet | 🟡 planned |
| 3D keepsake scan | 🔴 not launch scope (Phase 2 idea only) |

**Visual:** Four icon tiles (massage, nails, hair, beauty) around a blood-draw chair icon. Keep it calm and clean.
**Source:** [README.md][README]; [docs/services-pricing-locked.md][PRICE]; [docs/market-research-findings.md][MKT] (3D reframe note); [docs/CURRENT-STATE.md][CS] §0 item 1.
**Alexander lens:** First-mover edge is the experience itself. Be honest: this is not a hard-to-copy product. The moat has to come from referral relationships, a compliant collection room and brand.

---

## SLIDE 4: Market Size (Perth and WA)

| Measure | Figure | Note |
|---|---|---|
| WA births per year | about 33,570 | Source year: 2024 |
| Greater Perth births per year | about 26,790 | Source year: 2024 |
| Perth GTT tests per year (proxy) | about 26,790 | Assumes near-universal screening. Births used as a stand-in. TO CONFIRM |
| Perth GTT tests per week | about 515 | 26,790 divided by 52 |
| Women diagnosed with gestational diabetes (of those tested) | about 18% | Business plan; verify against a current clinical source before external use |

- Our planning capacity is 108 AM slots a week, about **21%** of Perth's weekly tests.
- Break-even needs about **14.9%** of the Perth market (see Slide 9). That is roughly 1 in 7 Perth GTT mothers.

**Visual:** Nested circles (WA 33,570 > Perth 26,790 > our capacity 21% > break-even 14.9%). Add a footnote: "ABS Births, Australia 2024, as analysed by KPMG; preliminary figures."
**Source:** [docs/CURRENT-STATE.md][CS] §3 and §10; [docs/investor-memorandum.md][IM] (market table); [docs/business-plan.md][BP] (Market Size, Addressable Market).
**Alexander lens:** The honest question is not "is the market big?" (it is). It is "can we win about 1 in 7 Perth GTT mothers through referrals?" That is a stretch for a single site and needs midwife and obstetrician relationships from day one.

---

## SLIDE 5: How a Visit Works

1. Book and pay online in advance. 🟡
2. Arrive fasted. Check in and consent forms.
3. Draw 1 (about 5 minutes), then service 1.
4. Draw 2 at 60 minutes, then service 2.
5. Draw 3 at 120 minutes. Relax in the lounge.
6. One courier pickup of the day's samples at the end of the morning. Lab tests; results go to the mother's doctor. GTT does not diagnose or interpret results.

| Operating detail | Planning figure |
|---|---|
| First client | 07:00 start |
| Clients per day | up to 18 (9 pairs, 25 minutes apart) |
| Collection chairs | 2 chairs, 2 phlebotomists |
| Treatment staff | 8 (4 massage/beauty pool, 2 nails, 2 hair) |
| Trading days | Monday to Saturday (no Sunday) |

**Visual:** Horizontal swim-lane timeline: one mother's 2 hours, draws as red dots, services as blue bars, lounge as soft green.
**Source:** [docs/CURRENT-STATE.md][CS] §1 and §4; [docs/scenario-c-sync-timetables.md][SYNC] §0.6a (the schedule was checked by solver for zero clashes); [docs/executive-summary.md][EXEC] ("GTT does not diagnose").
**TO CONFIRM:** who supplies the glucose drink (PathWest said it is excluded from its free supplies), and how the patient's pathology fee is billed under the new model.

---

## SLIDE 6: Pathology Partner Value Proposition

**What we offer a pathology partner**

| We provide | Status |
|---|---|
| A steady morning stream of GTT patients at one site (up to 108 a week at capacity) | 🟡 capacity, not a forecast |
| Our own certified phlebotomists, employed and supervised by us | 🟢 decided 2026-09-19 |
| 1 or 2 purpose-built collection rooms built to national standards (NPAAC = National Pathology Accreditation Advisory Council) | 🟡 design stage |
| One pickup a day at end of morning, not timed pickups per patient | 🟢 put to PathWest |
| We earn nothing from pathology billing. The partner keeps its testing revenue | 🟢 repo position |
| Willing to send pathology to one partner exclusively | 🟡 prepared position, not offered in writing. TO CONFIRM |

**What we ask:** courier pickup, lab testing, results reporting to the doctor, tubes and bags, collection-room spec in writing, and costs.

- New direction (Anthony, verbal): GTT collects, partner provides courier and lab. Terms and costs TO CONFIRM. 🟡

**Visual:** Two-column handshake diagram. Left: GTT (venue, room, phlebotomists, mothers). Right: Partner (courier, lab, reporting, Medicare billing). Arrow in the middle: samples out, results back.
**Source:** [docs/CURRENT-STATE.md][CS] §0 item 1 and §4; [docs/pathology-partnership-brief.md][PPB] §3 (written under an older model; see Conflict C8); [docs/pathwest-clinipath-outreach-2026-07-27.md][PWC] §4e.
**Alexander lens:** The partner's incentive is volume it would not otherwise capture. Say it as a hypothesis until a partner agrees. A regulatory moat exists only if our rooms and processes clear the bar that copycats find hard.

---

## SLIDE 7: Revenue Streams

| Stream | A$ per month (steady state, planning case) | Share |
|---|---|---|
| AM GTT packages (18 clients a day, A$250 each, about 26.33 trading days) | 118,485.00 (derived) | about 83% |
| PM standalone services and packages (10 sessions a day) | 24,585.37 | about 17% |
| **Total revenue** | **143,070.37** | 100% |

**Not counted in the baseline (upside only):**
- Cafe and retail (ancillary): set to A$0 by founder decision.
- Staff downtime fill and early-release savings: tracked separately, unproven.
- Package 2 upgrades (A$300): baseline prices every client at A$250.
- 3D keepsake scan: Phase 2 idea only.

**Visual:** Stacked bar (AM 83% / PM 17%), plus a greyed-out "upside, not counted" box.
**Source:** [docs/CURRENT-STATE.md][CS] §0 (items 3, 4), §5, §8; AM split derived as 18 x A$250 x 26.33 days = A$118,485.00 (adds exactly to the total with PM).
**TO CONFIRM:** this is a full-capacity case. No ramp-up (months 1 to 4) has been rebuilt for 18 clients a day. Conflict C5.

---

## SLIDE 8: Pricing

| Offer | Price | What it is |
|---|---|---|
| GTT Package 1 | **A$250** | Venue and lounge free + 2 x 30-minute services (fixed) |
| GTT Package 2 | **A$300** | Venue and lounge free + choice of 2 x 45, or 45 + 30, or 2 x 30 minutes |
| PM Refresh | **A$185** | 75 minutes: massage + mini facial (A$212 if bought separately) |
| PM Restore | **A$135** | 75 minutes: manicure + blow-dry (A$150 if bought separately) |

- Baseline uses A$250 for every GTT client. Deliberately cautious.
- Prices are our own. Not tested with customers yet. 🟡
- Pathology fee is separate from our packages. Out-of-pocket estimate A$0 to A$80, pending partner confirmation. TO CONFIRM
- Perth comparison: discounted spa packages average about A$140.

**Visual:** Four clean price cards. Package 2 labelled "most flexible".
**Source:** [docs/CURRENT-STATE.md][CS] §2; [docs/architecture/PM-PACKAGES.md][PMP]; [docs/services-pricing-locked.md][PRICE]; [docs/market-research-findings.md][MKT] §2.
**Note:** PM Refresh and PM Restore prices signed off by Anthony 2026-10-03.

---

## SLIDE 9: Unit Economics

| Measure | Figure |
|---|---|
| Revenue per AM client | A$250 (Package 1) |
| Extra revenue per extra AM client a day, per month | A$6,582.50 (derived: A$250 x 26.33) |
| Break-even | **12.655 AM clients a day** (about 333 a month) |
| Break-even as share of the 18-a-day plan | 70.3% |
| Margin of safety | 5.345 clients a day (29.7%) |
| Break-even share of Perth market | about 14.9% |

**Profit ladder (A$ per month, operating profit)**

| AM clients a day | Treatment staff | Revenue | Costs | Profit |
|---|---|---|---|---|
| 9 (45-min spacing, not approved) | 4 | 83,827.87 | 78,993.30 | +4,834.57 |
| 11.29 | 8 | 98,901.79 | 107,883.97 | **-8,982.18** |
| 13.5 | 8 | 113,449.12 | 107,883.97 | +5,565.15 |
| 15.5 | 8 | 126,614.12 | 107,883.97 | +18,730.15 |
| **18 (planning case)** | 8 | 143,070.37 | 107,883.97 | **+35,186.40** |

- Staff cost is mostly fixed once the 8-person team is rostered. Below about 12.7 clients a day we lose money.
- 12-client alternative (08:00 start): +A$1,096.40 a month. Barely above zero.

**Visual:** Line chart of profit against clients a day, with a dotted vertical line at 12.655 and a shaded "loss valley" between 9 and 12.7.
**Source:** [docs/CURRENT-STATE.md][CS] §10. (Per-client figures derived from the ladder.)
**Alexander lens:** This is a high fixed-cost model. The business wins or loses on fill rate. Referrals must be proven before the lease is signed.

---

## SLIDE 10: Financial Baseline

| Planning case (full 18 a day) | A$ per month | A$ per year |
|---|---|---|
| Revenue | 143,070.37 | 1,716,844.44 (derived) |
| Payroll (including workers comp) | 93,595.63 | |
| Other costs (rent budget A$8,000, insurance, admin) | 14,288.34 | |
| **Total costs** | **107,883.97** | |
| **Operating profit** | **+35,186.40** | **+422,236.80** |
| Profit margin | about 24.6% (derived) | |

| Startup funding (planning) | A$ |
|---|---|
| Pre-opening capital (approved in principle, 2026-08-10) | 251,198 |
| Working capital reserve | 85,000 to 110,000 |
| **Combined planning case** | **336,198 to 361,198** |
| Funding on hand (joint savings, as stated in repo) | about 200,000 |
| Gap (derived) | about 136,198 to 161,198 |

- 🔴 Profit is steady state at full capacity. No trading data. Fit-out has not been repriced for the larger footprint (see Slide 12).
- 🟡 The repo holds several unreconciled startup ranges. Anthony's own adopted range is A$292,335 to A$594,900. Accountant and quantity surveyor to confirm.
- Older "conservative" baseline (A$113,712.16 revenue, A$88,625.09 costs, +A$25,087.07, 570 visits): historical. See Conflict C1.

**Visual:** Waterfall: revenue 143k, less payroll 94k, less other 14k, equals profit 35k. Below it, a bar showing funds on hand against the planning need.
**Source:** [docs/CURRENT-STATE.md][CS] §5, §6; `data/models/master_financial_model.yml` (updated_planning_case_2026_08_10); [docs/executive-summary.md][EXEC] (funding line); [docs/risk-register.md][RISK] #8.

---

## SLIDE 11: Partnership Status: Where We Are

| Partner | Last known position (repo) | Status |
|---|---|---|
| **WDP** (Western Diagnostic Pathology) | Contact: Carole Rivers. Engaged since 2026-07-28. Her reply on 2026-09-08: "I think I have provided all the information I can as a Customer and Commercial Manager." The rental figure never arrived. | 🟡 stalling |
| **PathWest** | 2026-08-28: no capacity "to provide collection staff to non-PathWest collection sites". 2026-09-01: "We can definitely accommodate courier pick ups for Fluoro ox tubes" and tubes and bags at no cost if volume is large. We asked for costs 2026-09-03. No reply recorded. | 🟡 open: courier yes, costs unknown |
| **Clinipath** | 3 contacts (2026-07-27, 08-27, 09-07). No reply. They were pitched the self-collection model. | 🔴 silent |
| **Way ahead (Anthony, verbal)** | GTT's own certified phlebotomist collects. A partner provides courier and lab testing. | 🟡 TO CONFIRM: which partner, terms, costs |

- Nothing is signed. No partner has committed in writing to the new model.
- The repo's records stop at 2026-09-08. Anything after that is not yet logged. TO CONFIRM.

**Visual:** Traffic-light table (as above), plus a one-line arrow: "Self-collect + courier + lab".
**Source:** [docs/wdp-followup-draft-2026-08-20.md][WDP]; [docs/pathwest-clinipath-outreach-2026-07-27.md][PWC] §4d, §4e-vi, §4e-vii; [docs/reed-partnerships.md][REED]; [docs/CURRENT-STATE.md][CS] §0 item 1.

---

## SLIDE 12: Site and Lease Plan

| Item | Position |
|---|---|
| Venue size | Day-one need about 257 to 259 sqm (two collection rooms). Search brief minimum 239 to 242 sqm. Preferred 260 to 280. |
| Rent budget | **A$8,000 a month** (founder decision 2026-10-03; revisit at lease stage) |
| Gap flagged | At the same rate per sqm the larger footprint implies about A$9,560 to 9,960. Known, accepted for now. |
| Lease terms to seek | 3 years + 3-year option; no landlord contribution counted |
| Lease bond and legal | About A$19,600 to 27,600 (modelled) |
| Status | No venue. No lease. No heads of agreement. 🔴 |

**Shortlist leaders (Tier 1, not verified as available today)**

| Property | Size | Rent | Notes |
|---|---|---|---|
| [6/325 Harborne St, Osborne Park](https://reiwa.com.au/6-325-harborne-street-osborne-park-4941752/) | 268 sqm | A$55,000 a year + A$23,785 outgoings (about A$6,565/month + GST) | Blank shell. Plumbing unknown. Re-checked 2026-08-14. |
| 25 Mills St, Cannington | up to 302 sqm | Not disclosed | Existing medical fit-out near Bentley Hospital. No direct listing link in repo. Needs verifying. |

- Rule: get the partner's collection-room spec in writing before signing any lease. Partner may now differ. TO CONFIRM
- A professional architect is needed once a site is picked. The in-house floor plan is parked.
- Collection room standards: NPAAC (Guidelines for Approved Pathology Collection Centres, 3rd edition 2013). Specimen fridge kept apart from food and drink.

**Visual:** Perth map with Osborne Park and Cannington pinned; side table of rent vs the A$8,000 budget line.
**Source:** [docs/strategy/PERTH-PROPERTY-SHORTLIST.md][SHORT]; [docs/DECISION-LOG.md][DL] (2026-10-03, 2026-08-27, 2026-09-04); [docs/rent-budget-2026-07-28.md][RENT]; [docs/floor-plan-concept.md][FLOOR]; [docs/location-scouting.md][LOC]; [docs/CURRENT-STATE.md][CS] §7.3.

---

## SLIDE 13: Risks and Mitigations

| # | Risk | Level | Mitigation |
|---|---|---|---|
| 1 | No venue secured. Blocks hiring, fit-out and everything after | 🔴 Critical | Two Tier-1 candidates; verify rent and availability; inspect |
| 2 | No signed pathology partner for the new model | 🔴 High | Chase PathWest costs; reopen WDP; try Clinipath by phone; get terms in writing |
| 3 | Funding gap: planning need about A$336k to A$361k vs about A$200k on hand | 🔴 High | Founder funding decision; accountant; staged fit-out. TO CONFIRM |
| 4 | Demand unproven. Need about 70% fill (12.7 of 18 a day) | 🟡 High | Referral network and waitlist from day one; ramp not yet modelled |
| 5 | Courier cut-off time unconfirmed (docs show 11:30 and 12:30, neither sourced) | 🟡 Medium-High | Confirm with the partner in writing before locking the schedule |
| 6 | Rent budget below implied cost for the bigger footprint | 🟡 Medium | Deliberate choice; real quote replaces the estimate at lease stage |
| 7 | Collection-room compliance and cost; architect not engaged | 🟡 Medium | Brief architect after site pick; confirm spec with partner |
| 8 | Tax: proposed 30% minimum tax on discretionary trusts from 1 July 2028 (exposure draft, not law) | 🟡 Low-Medium | Accountant review; verify against Treasury source before external use |

**Visual:** 3 x 3 heat map (likelihood vs impact) with the eight numbers plotted.
**Source:** [docs/risk-register.md][RISK] (older; items re-ranked by Grace against newer files); [docs/CURRENT-STATE.md][CS] §6, §10; [docs/cutoff-time-CORRECTION.md][CUT]; [docs/DECISION-LOG.md][DL] (2026-09-04, 2026-10-03).
**Alexander lens:** Risks 1 to 3 are the same single point of failure: no site and no partner means no revenue. Fix order matters more than anything else on this slide.

---

## SLIDE 14: Roadmap and Launch Gates

No calendar dates. The repo keeps launch undated by standing instruction.

| Stage | What happens | Gate | Status |
|---|---|---|---|
| 0 | Search for venue. Pathology partner talks. Marketing waitlist can start early | none | 🟡 in progress |
| **Gate A** | **Pathology partner agreed** | needs written terms | 🔴 open |
| **Gate B** | **Venue location confirmed** | needs site and lease terms | 🔴 open |
| 1 | After Gates A and B: Venue Manager hire (job ad ready, **on hold behind both gates**). Lease or heads of agreement. Architect and fit-out quotes | A + B | not started |
| 2 | Phlebotomist and treatment staff recruitment; contracts | Venue Manager in place | not started |
| 3 | Partner site inspection. Training. Test runs. Soft open for waitlist. Public launch | Fit-out done and staff hired | not started |
| Go-live trigger | First confirmed customer booking: Grace reports to Anthony; manager registration requested | | not started |

**Visual:** Left-to-right gate diagram with two red locks (Gate A, Gate B) before Stage 1.
**Source:** [docs/project-timeline-milestones.md][TIME]; [docs/venue-manager-job-posting.md][VM] (status banner 2026-07-29); [docs/floor-plan-concept.md][FLOOR]; [README.md][README].

---

## SLIDE 15: The Ask / Next Steps

**Decisions for Anthony (nothing has been sent)**

| # | Decision or action | Owner |
|---|---|---|
| 1 | Confirm which financial baseline goes in front of people: +A$35,186.40 (current) or the older +A$25,087.07 | Anthony |
| 2 | Confirm the pathology way ahead in writing: which partner, what they supply, price | Anthony, Reed |
| 3 | Follow up PathWest on courier and lab costs (asked 2026-09-03); decide whether to reopen WDP; try Clinipath another way | Anthony, Reed |
| 4 | Pick a site to verify first (Harborne St or Mills St); confirm rent, plumbing, availability | Anthony |
| 5 | Decide how to cover the funding gap (planning need A$336k to A$361k vs about A$200k) and brief the accountant on entity structure | Anthony |
| 6 | Appoint an architect once a site is chosen | Anthony |
| 7 | Approve this deck, then Grace exports PDF/Keynote | Anthony |

- **We are not asking for money in this draft.** The repo says no external investor has been sought. The funding route is TO CONFIRM.

**Visual:** Numbered checklist with owner icons; big "Gate A + Gate B" lock graphic at the bottom.
**Source:** [docs/CURRENT-STATE.md][CS]; [docs/VERIFICATION-TRACKER.md][VT]; [docs/venue-manager-job-posting.md][VM]; [docs/executive-summary.md][EXEC] (funding line).

---

# ONE-PAGE EXECUTIVE SUMMARY

**GTT Center Perth** (working name; SOLENA conditional, not locked) turns the 2 to 2.5 hour Glucose Tolerance Test wait into a care experience: massage, nails, hair and beauty between blood draws. DRAFT, 2026-10-10.

**Why it matters.** The test is a standard pregnancy screen with near-universal take-up. About 26,790 births a year in Greater Perth (about 33,570 in WA; ABS 2024) gives roughly 515 tests a week. Our research found no equivalent WA venue.

**The model.** Employed staff, not subtenants. GTT's own certified phlebotomists draw blood in on-site collection rooms. A pathology partner provides courier and lab testing (terms TO CONFIRM). GTT earns no pathology revenue. Two GTT packages (A$250, A$300) and two afternoon packages (A$185, A$135). Mon to Sat. Up to 18 morning clients a day.

**The numbers (planning case, full capacity).** Revenue A$143,070.37 a month; costs A$107,883.97; operating profit +A$35,186.40 (about A$422k a year). Break-even is 12.655 morning clients a day (about 70% of capacity, about 14.9% of the Perth market). Below that the venue loses money. At 12 clients a day the profit is only +A$1,096.40. Rent is budgeted at A$8,000 a month.

**Money needed.** Planning need A$336,198 to A$361,198 (A$251,198 pre-opening plus A$85,000 to 110,000 working capital) against about A$200,000 in joint savings. Gap about A$136k to A$161k. No external investor sought. Funding route TO CONFIRM.

**Where we are.** 🔴 No venue. 🔴 No signed pathology partner. WDP has gone quiet (last reply 2026-09-08). PathWest confirmed courier pickup and free tubes, but cannot supply collection staff; costs asked 2026-09-03, no reply logged. Clinipath silent after 3 attempts. Anthony reports a way ahead (GTT collects; partner couriers and tests). The Venue Manager hire waits behind both gates.

**Strategy view (Alexander).** Demand is real and non-discretionary, and we are first. But this is a high fixed-cost model with no hard moat yet. The moat has to be built from midwife and obstetrician referrals, a compliant collection room and a trusted partner. The fill needed (about 1 in 7 Perth mothers) is the number to prove first.

**Next steps.** Lock a pathology partner in writing. Verify one site. Decide funding. Engage an architect. Then hire.

---

# CONFLICTS & OPEN ITEMS

Rule applied: newest document marked current wins. Disagreements listed here.

| # | Topic | What the documents say | Used in deck | Action |
|---|---|---|---|---|
| C1 | Financial baseline | Brief and `outputs/FOUNDER-CFO-ANALYSIS.md` (2026-10-08): A$113,712.16 revenue, A$88,625.09 costs, +A$25,087.07, 570 visits, ancillary excluded, "confirmed current". `docs/CURRENT-STATE.md` (2026-09-19/10-03): A$143,070.37, A$107,883.97, +A$35,186.40, 18 clients a day. `docs/profit-loss-tables.md` is v3.0 (rebased 2026-08-05); the A$113,712 figure is called a historical 10-client figure that included ancillary revenue (`docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md` §2). Ancillary-excluded versions of that old baseline were A$16,507.07 then A$28,488.42, not A$25,087.07. | CURRENT-STATE | Anthony to confirm which baseline to present. CFO analysis needs a refresh. |
| C2 | 570 visits | 220 AM + 350 PM equals the old 10-client / 16-session model. Current model is 18 AM a day and 10 PM sessions a day. | Current model | Drop 570 from external use. |
| C3 | Table 2 (12 a day) profit | `docs/CURRENT-STATE.md` §5 says +A$10,076.16; §10 (newer, 2026-09-19) says +A$1,096.40. | +A$1,096.40 | Fix §5 in repo. |
| C4 | AM capacity per month | §3 says 396 a month (22 weekdays). Revenue maths and break-even use about 26.33 days (Saturdays included), about 474 a month. | 108 a week; revenue as per model | Clarify in CURRENT-STATE. |
| C5 | Ramp-up | Month 1 to 4 ramp not rebuilt for 18 a day (`docs/CURRENT-STATE.md` §5). No Year 1 view available. | Steady state only | Rebuild before any funding talk. |
| C6 | 18 vs 12 clients framing | `docs/VERIFICATION-TRACKER.md` item 1m says the 18-client framing is still open for Anthony to confirm. Later Sept/Oct decisions build on 18. | 18 as planning case, 12 as downside | Anthony to confirm. |
| C7 | PathWest 2026-08-28 | Older changelog line says "effectively declines". Later entries correct this: reply was ambiguous, then 2026-09-01 gave unconditional courier pickup. Brief says "declined collection staff". Only collection staff were declined. | Courier yes; staff no | None. Record kept accurate. |
| C8 | Pathology model | `docs/pathology-partnership-brief.md` (Option A, WDP licensed collection centre, 8 clients a day, 7:30 to 12:30) and `docs/executive-summary.md` v2.0 (partner covers accreditation; PathWest and Clinipath "not yet contacted") are stale. Decision 2026-09-19: GTT collects; partner does transport and lab only. Anthony's verbal update goes further. | 2026-09-19 decision plus Anthony's note | Update those docs. Written terms TO CONFIRM. |
| C9 | WDP status | `docs/VERIFICATION-TRACKER.md` 1c says "actively progressing, not stalled" (2026-08-08). `docs/reed-partnerships.md` and `docs/wdp-followup-draft-2026-08-20.md` say closing tone after 2026-09-08. | Stalling | Update tracker. |
| C10 | Venue Manager gate | `docs/CURRENT-STATE.md` §4 and risk register #10: one gate (location). `docs/venue-manager-job-posting.md` (2026-07-29): two gates (partner and location). | Two gates | Update CURRENT-STATE. |
| C11 | Startup capital | Five unreconciled figures in `docs/CURRENT-STATE.md` §6: A$144.5k to 242.5k; A$209k to 431k; A$292,335 to 594,900 (Anthony adopted); A$357,390 to 577,180 (component sum); A$336,198 to 361,198 (2026-08-10 planning case). Fit-out cost not recalculated for 257 to 259 sqm. | 2026-08-10 planning case, others noted | Accountant and quantity surveyor to confirm. |
| C12 | Funding on hand | About A$200,000 joint savings (`docs/executive-summary.md`, `docs/swot-analysis.md`). Not re-verified since 2026-07-29. | As stated | TO CONFIRM current balance. |
| C13 | Rent vs footprint | A$8,000 set against 200 sqm; footprint now 257 to 259 sqm (implied A$9,560 to 9,960). Search brief minimum 239 to 242 sqm predates the two-room decision. | A$8,000 (founder decision) | Revisit at lease stage. |
| C14 | Market numbers | Older files still show ~18,000 WA births, ~14,400 Perth, ~277 tests a week (`docs/risk-register.md`, `docs/swot-analysis.md`). Corrected 2026-07-31 to ABS 2024 via KPMG. Figures are preliminary. Births are used as a proxy for tests. | 33,570 / 26,790 / 515 | Check for newer ABS release; mark year on every slide. |
| C15 | 3D keepsake scan | README intro and the venture brief list it as part of the offer. Same README and `docs/market-research-findings.md` say not launch scope, Phase 2 only. | Excluded; never diagnostic | None. |
| C16 | Entity and ownership | `docs/executive-summary.md` and README say YETI Holding Trust. `docs/DECISION-LOG.md` (2026-09-04) says the structure is under review (trust direct, new company, or fixed distributions). Executive summary also calls Imara "funding partner" and "founder". | Entity not stated beyond "see repo" | Accountant. No role for Imara. Fix wording in executive summary. |
| C17 | Option B timeline | `docs/pathology-partnership-brief.md`: 7 to 9 months. `docs/executive-summary.md`: 12 to 18 months. | Not used | Reconcile if raised. |
| C18 | Pathology consumables cost | `outputs/FOUNDER-CFO-ANALYSIS.md` uses A$2.27 a visit. PathWest said it would supply tubes and bags free (volume permitting). Glucose drink excluded. | Not used | TO CONFIRM. |
| C19 | Medicare billing and "GTT earns zero from pathology" | Written under the old WDP model. New model billing path not documented. | Stated as repo position, flagged | TO CONFIRM with partner. |
| C20 | Launch timing | `docs/pathology-partnership-brief.md` mentions an October 2026 launch. Repo says no launch date set. | Undated | None. |
| C21 | Partner news after 2026-09-08 | Repo has no logged replies after 2026-09-08. | Slide 11 notes this | Log any new emails. |
| C22 | Savings and exclusive-referral claims | "Willing to refer all pathology to one partner" is a prepared call script, not an offer made. | Marked TO CONFIRM | Anthony to approve before use. |
| C23 | Tax proposal | Decision log cites an exposure draft (released 2026-09-03; consultation to about 2026-09-18). Not checked against a Treasury source in this draft. | Flagged as proposed | Verify before external use. |
| C24 | Clinical claims | "About 18% diagnosed" and the 2 to 2.5 hour test length come from repo documents, not re-checked against a current Australian clinical source in this draft. | Marked for check | Verify against a current clinical guideline before any external use. |

---

## Source links

All files in the venture repo: https://github.com/clawanthonyzed/gtt-center-perth (branch main).

[README]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/README.md
[CS]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/CURRENT-STATE.md
[DL]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/DECISION-LOG.md
[VT]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/VERIFICATION-TRACKER.md
[EXEC]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/executive-summary.md
[BP]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/business-plan.md
[IM]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/investor-memorandum.md
[MKT]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/market-research-findings.md
[PRICE]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/services-pricing-locked.md
[PMP]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/PM-PACKAGES.md
[SYNC]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/scenario-c-sync-timetables.md
[PPB]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/pathology-partnership-brief.md
[PWC]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/pathwest-clinipath-outreach-2026-07-27.md
[WDP]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/wdp-followup-draft-2026-08-20.md
[REED]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/reed-partnerships.md
[SHORT]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/strategy/PERTH-PROPERTY-SHORTLIST.md
[RENT]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/rent-budget-2026-07-28.md
[FLOOR]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/floor-plan-concept.md
[LOC]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/location-scouting.md
[RISK]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/risk-register.md
[CUT]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/cutoff-time-CORRECTION.md
[TIME]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/project-timeline-milestones.md
[VM]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/venue-manager-job-posting.md
[NAMING]: https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/naming/NAMING-DECISION-STATE.md
