# Decision Log

**Purpose:** a running, append-only record of major project decisions, so future sessions/agents don't rediscover the same open questions or silently contradict a decision already made. Add new entries at the top. Do not delete or rewrite prior entries — correct forward, the way the rest of this repository's changelogs already work.

---

## 2026-10-17: Floor plan v2 corrections (Anthony, directive items F1 to F8)

**Decisions (Anthony, 2026-10-17):** fix wall placement and corridors so every room has unblocked access; resize hair and nails to commercial proportions with the freed area to the lounge; remove the separate fridge room (an under-counter clinical specimen fridge in each collection room); standardise both collection rooms at equal size; route staff to the staff room without passing the service and linen zone; remove the staff toilet.

**Applied (workstream F):** both collection rooms 19.0 sqm (middle of the 18 to 20 sqm range in the venue room schedule and pathology partner brief); hair 23.9 sqm and nails 22.4 sqm (5 to 6 sqm per station); lounge 44.7 sqm; staff WC removed; separate service entry and staff-only corridor. Files: `outputs/DESIGN/CONCEPT-FLOOR-PLAN.svg`, `outputs/PRESENTATION/floor-plan-v2.html`, `docs/overhaul-2026-10-17/F-floorplan/`. Open for the architect and pathology partner: collection room size confirmation, NCC toilet count, second fridge, recliner and centrifuge quantities (not priced in the model).

## 2026-10-17: Phlebotomists on the adaptive roster; 10% post-test discount adopted (Anthony)

**Decisions (Anthony, 2026-10-17, directive items R1 and R2):**

- **(R1) Phlebotomists are rostered adaptively from confirmed advance bookings**, like every other role. The fixed minimum of 2 per GTT morning (recorded 2026-10-11, kept open on 2026-10-16) is retired. Rule: **1 phlebotomist when 1 to 9 clients are booked and no two share a slot; 2 phlebotomists when 10 to 18 are booked** (two chairs running pairs); **none in the afternoon**. On mornings of 9 or fewer a named second collector is on call for a difficult draw or a faint, and is paid only when called in (assumed; the repo has no standby allowance, so none is invented). Options priced: a 3-hour second shift every light morning (A$3,341.13 a month, break-even 7.758); a second collector on Saturdays only (A$1,523.12 a month, break-even 7.482).
- **(R2) The 10% post-test discount is adopted.** Any expecting mother who completes a GTT test can redeem 10% off standalone wellness treatments or multi-service packages. It is **not limited to the afternoon**: it is valid immediately, so a morning client who completes her test can redeem the same day. The precise terms (exclusions, stacking, one use per test, expiry, recording) are **proposals pending Anthony's sign-off**, in `docs/overhaul-2026-10-17/M-model/R2-POST-TEST-DISCOUNT.md`.

**Clinical-safety conditions recorded (proposals, from `docs/gtt-clinical-protocol.md`):** (1) difficult draw: maximum 2 attempts by the first collector, then the on-call second collector, and if she cannot attend in time, reschedule or refer back per the pathology partner's protocol; (2) fainting and vasovagal response: client kept seated or lying, Venue Manager called, 000 if unconscious, recovery chair used, and the Venue Manager takes over the client so the sole collector can continue; (3) Saturday has no Venue Manager, so a second collector on every Saturday is recommended until first-aid cover is confirmed (not in the headline); (4) every light-morning roster names the on-call collector; (5) the pathology partner must confirm that one collector per chair meets its collection-site conditions.

**Dependency flag:** the pathology partner and the Medicare and lab-employment rules (see `docs/overhaul-2026-10-17/L-medicare/` when it appears; not yet published when this was written) **may require the lab to supply or employ the collectors. If so, the phlebotomist roster is the lab's decision and the figures below for phlebotomist wages change to a lab arrangement.** The 2026-09-19 decision (GTT employs both phlebotomists directly) stands until that is answered.

**Results (calculators re-run with one changed input, the phlebotomist count; no new calculator):**

| Figure | Before (2 phlebotomists always) | After (adaptive) |
|---|---|---|
| Break-even, AM clients a day (one client per slot) | 8.266 | **7.250** (40.3% of 18; margin of safety 10.750, 59.7%) |
| Break-even if bookings stack in pairs from 07:00 | 12.655 | 12.655 (both chairs run) |
| GST-stress break-even | 9.255 spaced / 14.083 planning | **8.138** |
| Morning labour per month, 1 to 9 booked | A$42,255.18 (4 therapists + 2 phlebotomists) | **A$35,572.95**, saving A$6,682.23 a month |
| Net operating profit a month at 9 booked | +A$4,834.58 | **+A$11,516.81** |
| Net operating profit at 1 / 5 booked | -A$33,380.10 / -A$21,495.42 | -A$26,697.87 / -A$14,813.19 |
| Saturday contribution at 9 booked | +A$25.65 | **+A$377.41** |
| Saturday direct-labour break-even (4 therapists) | 8.90 clients | **7.49** |
| Steady state at 18 a day (month / Year 1 / margin) | +A$35,186.40 / A$422,236.80 / 24.6% | unchanged (both chairs run) |
| Saturday proof at 18 | +A$754.82 | unchanged |
| GST-stress Year 1; peak funding; payback | A$281,310.96; A$251,198.00; Month 8 / Month 11 | unchanged |
| Year 1 if only half a morning fills (9 a day) | A$58,015 (GST-stress -A$18,283), payback Month 55 | **A$138,202 (GST-stress A$61,904), payback Month 23** |
| Headcount on the books | 21 (4 phlebotomists) | 21 (4 phlebotomists; peak need still 2; pool unchanged) |

Discount cost (R2): at A$117 a booking, 5% / 10% / 25% / 40% take-up costs A$277 / A$555 / A$1,386 / A$2,218 a month if every redeemer would have booked anyway (3.9% of monthly profit at 25%); it pays for itself if 10% of redeemers are new bookings (idle therapist time) or 24.2% (extra hours must be paid). X's A$1,381 a month at 25% is A$1,386.27 on the exact 118.49 redemptions. Cost is not deducted from the headline model and upside is not added; take-up and new-booking share are assumptions.

**Medicare findings (workstream L, 2026-10-17) applied:** Medicare pays only where the specimen is collected by the pathologist or an employee of the approved pathology authority, so the lab may have to supply the collectors. If it does and charges nothing, GTT saves A$6,682.28 a month per collector (A$13,364.52 for two), break-even is 6.235 and net at 18 a morning is +A$48,550.92. If Medicare does not pay and GTT absorbs the A$25.85 schedule fee, break-even is 8.087 on the adaptive roster (9.219 on the old fixed roster) and net at 18 is +A$22,935.05. Workings: R1 section 11.

**Flags for Anthony:** (a) the phlebotomist job posting offers permanent part-time 25 hours a week; an adaptive roster cannot guarantee that (9 to 18 hours a week each on a pool of 4), so engage as casual or set a guaranteed minimum (employment type TO CONFIRM); (b) the adopted discount replaces the earlier 10% pre-booking discount and lifts the "no discount on same-day upsells" rule for standalone treatments and packages (`docs/services-pricing-locked.md` updated, subject to your sign-off on the proposed terms); (c) the previous "Open question" in the 2026-10-16 entry is now closed by this entry.

**Documents updated:** `docs/CURRENT-STATE.md`, `outputs/FINANCIALS/3-WAY-FINANCIAL-MODEL-AUD.md`, `outputs/FINANCIALS/PROFIT-AND-LOSS.md`, `outputs/FINANCIALS/CASHFLOW-FORECAST.md`, discount wording in `docs/services-pricing-locked.md`, `docs/financial-break-even-staff.md`, `docs/ITEMS-TO-CONFIRM.md`, `docs/VERIFICATION-TRACKER.md` and the X-market workings. Slides and the business plan are left for the documents agent.

**Related documents:** `docs/overhaul-2026-10-17/M-model/R1-ADAPTIVE-PHLEBOTOMY.md`, `docs/overhaul-2026-10-17/M-model/R2-POST-TEST-DISCOUNT.md`, `docs/overhaul-2026-10-17/M-model/FOR-DOCUMENTS-AGENT.md`, `docs/reviews/ANTHONY-DIRECTIVE-2026-10-17.md`.

---

## 2026-10-16: Permanent Cadence Law, adaptive rostering, no ramp-up, afternoon structure (Anthony)

**Decision (Anthony, 2026-10-16, line-by-line review, items L1, L2, L3, S11b, P8d, P8e, P16a, P19c):**

- **(a) Cadence.** The earlier alternative pair cadence is **retired permanently**. The **25-minute pair cadence is the only cadence** in every plan, booking, roster and calculator. First booking **07:00** (expecting mothers arrive fasted 10 minutes before, 06:50). Pairs at 07:00, 07:25, 07:50 and so on. Last first draw **10:20** (check: 07:00 + 8 x 25 minutes = 10:20; 9 pairs = 18 clients at most). Full-capacity time slots are offered; bookings are taken **2 to 4 weeks ahead**.
- **(b) True adaptive rostering.** Staff are called in to match the confirmed slots, AM and PM. Idle staff are never rostered. One booked client does not trigger a full roster.
- **(c) No ramp-up.** The plan opens at the full 18 clients a morning, filled through marketing and a pre-launch waitlist. The 43% / 64% / 79% / 93% ramp is removed from every model.
- **(d) Afternoon.** Stand-alone pre-booked services, not bound by the 2-hour GTT clock. Walk-ins only if staff are free. Rostered adaptively to the pre-booked services.
- **(e) AM packages** include any service-menu option that fits the 30 or 45 minute wellness window. (This 45 is a **service length**, not a cadence, and stays.)

**Reason:** the earlier alternative cadence was adopted to justify a 4-therapist roster on quiet mornings. Anthony has ruled that the 25-minute cadence is the only one and that rostering must follow the confirmed bookings. The 25-minute cadence supports a small roster by itself when bookings fall one per slot (at most two first services overlap at once, so 4 therapists cover up to 9 clients), so the model does not need a second cadence. Removing the ramp is Anthony's decision; the marketing and waitlist plan has to deliver it.

**Nature of the change:** a decision plus a model rebuild. Calculators re-run (tools/am_volume_tier_staffing_solver.py, tools/cost_ramp_model.py, tools/am_demand_tier_financial_ladder.py); no new calculator replaces them. Results:

| Figure | Earlier ramped model | Now |
|---|---|---|
| Steady state per month (Table 1, 18 clients a day) | +A$35,186.40 | **+A$35,186.40** (unchanged, 24.6% margin) |
| Steady state per year | A$422,236.80 | **A$422,236.80** |
| Break-even (AM clients a day) | 8.266 | **8.266**, re-derived on the 25-minute cadence (planning case, bookings one per slot); 12.655 if every booking stacks in pairs from 07:00; 7.250 if one phlebotomist is allowed on mornings of 9 or fewer |
| Year 1 net (repo basis / GST-stress) | A$322,014.93 / A$196,608.65 | **A$422,236.80 / A$281,310.96** (12 full-capacity months) |
| Peak funding / lowest cash | A$267,771.03 / A$68,426.97 | **A$251,198.00 / A$85,000.00** (reserve never drawn) |
| Payback (repo / after GST) | Month 11 / Month 15 | **Month 8 / Month 11** |

**Superseded by this entry:** the 2026-10-11 entry below (cadence part; its text has been reduced to a superseded stub per this law) and the 2026-10-13 wording-only entry. `docs/CURRENT-STATE.md` section 10 and the 3-way model have been rebuilt.

**Open question for Anthony, flagged not decided:** the model keeps **2 phlebotomists on any morning with a GTT booking**. That minimum is not a regulation found in this repo. It comes from GTT's own clinical standard recorded on 2026-10-11 and from the difficult-blood-draw protocol (a second on-site phlebotomist attempts after two failed attempts, `docs/gtt-clinical-protocol.md`). On the 25-minute cadence one chair carries up to 9 clients with no overlapping draws, so mornings of 9 or fewer could run 1 phlebotomist: saving A$234.51 a weekday morning (A$6,682.23 a month) and lowering break-even to 7.250. L3 can be read either way ("do NOT roster 2 phlebotomists and 8 therapists" for 1 client). Until Anthony decides, 1 booked client rosters 2 phlebotomists and 2 therapists, never 8 therapists. Worth asking the pathology partner whether it requires 2 collectors.

**Documents updated:** `docs/CURRENT-STATE.md` (new section 00, sections 0, 4, 10), `outputs/FINANCIALS/3-WAY-FINANCIAL-MODEL-AUD.md` (v0.5), `outputs/FINANCIALS/PROFIT-AND-LOSS.md`, `outputs/FINANCIALS/CASHFLOW-FORECAST.md`, comments in `tools/`, and the workings and document-ready wording under `docs/overhaul-2026-10-16/M-model/`.

**Related documents:** `docs/reviews/ANTHONY-REVIEW-2026-10-16.md`, `docs/overhaul-2026-10-16/M-model/MODEL-WORKINGS.md`.

---

## 2026-10-13: Wording only, CURRENT-STATE section 10 break-even wording (SUPERSEDED 2026-10-16)

**Superseded.** Section 10 of `docs/CURRENT-STATE.md` was rebuilt on 2026-10-16 (see the entry above). No figure in this entry is current.

---

## 2026-10-11: Low-volume cadence decision, break-even and peak funding lock (SUPERSEDED 2026-10-16, retired permanently)

**Superseded.** Retired by Anthony on 2026-10-16 under the Permanent Cadence Law (entry above). The 25-minute pair cadence is the only cadence. The figures this entry locked are replaced: break-even is re-derived on the 25-minute cadence (8.266, planning case), peak funding is now A$251,198, and the scheduling standard of advance booking 2 to 4 weeks ahead plus a waitlist is kept. The line "2 phlebotomists on every GTT morning" is held as an open question for Anthony (see the entry above). The detailed cadence text of this entry was removed, not preserved, because Anthony's law is to eradicate every mention; the earlier text remains in version history.

---

## 2026-10-03: Rent budget stays at A$8,000/month for budgeting — footprint-growth gap acknowledged, revisit at lease stage

**Decision:** Anthony reviewed `docs/research/RENT-ECONOMICS-FORENSICS.md` §1's finding that the A$8,000/month rent line was set 2026-07-28 against a 200sqm planning footprint and never recalculated after the venue program grew to 239-249sqm across two later founder decisions (implying A$9,560-9,960/month at the same A$40/sqm/month rate) and instructed: **"leave rent as is for budgeting."**

**Reason:** the gap is real and quantified, but no precise rent figure can be meaningfully fixed before a real venue and lease exist — whatever real quote eventually comes in will supersede any planning estimate regardless of which number sits in the model today. Revisiting now would replace one unverified estimate with another, not add certainty.

**Nature of the change — a decision, not a dollar change.** No figure in `data/canonical/*.yml`, `docs/CURRENT-STATE.md`, or any downstream revenue/cost/profit/break-even calculation changes. The A$8,000/month figure remains exactly as it was; only its status moves from an unflagged internal gap to a disclosed, deliberate planning choice, explicitly scheduled for revisit once a real venue and lease are on the table, not before.

**Documents updated:** `docs/CURRENT-STATE.md` §0 (new item 5), `docs/VERIFICATION-TRACKER.md` (new item 54, plus a Changelog entry), `docs/research/RENT-ECONOMICS-FORENSICS.md` (decision banner added; the finding and sensitivity analysis themselves are unchanged and still stand as reported).

**Related documents:** `docs/research/RENT-ECONOMICS-FORENSICS.md`, `docs/research/ROUND-3-SYNTHESIS.md`, `docs/research/MODEL-BREAKPOINTS.md`.

---

## 2026-09-04: Collection room specimen storage stays physically segregated from the cafe/wellness-lounge operation

**Decision:** Anthony has confirmed: the Blood Collection Room(s)' specimen storage (medical-grade specimen fridge) stays physically segregated from the venue's cafe/wellness-lounge food & drink operation (the Cafe/Refreshments Counter and the GTT Lounge's own cafe counter feature).

**Reason:** NPAAC's Guidelines for Approved Pathology Collection Centres (Third Edition 2013, Tier 3B — the same primary source already relied on elsewhere in this repository, e.g. `docs/VERIFICATION-TRACKER.md` items 29/29b, `docs/architecture/WDP-PARTNERSHIP-ACTIVATION-PLAN.md` §2b-i) requires that specimens "must not be stored with food, drink, or pharmaceuticals" — directly relevant to GTT since the same venue also runs a cafe/wellness-lounge food & drink operation.

**Nature of the change — confirmation, not a design change.** Checked directly against the current floor plan before logging this decision: `docs/floor-plan-concept.md`'s Room Schedule and Critical Design Requirements, and `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`'s venue-program table, already show the Blood Collection Room(s) as solid-walled rooms with their own dedicated medical-grade specimen fridge, physically separate from the Cafe/Refreshments Counter's own solid-walled room and separate mini fridge — no shared storage unit or shared space between clinical specimens and food/drink exists anywhere in the current design. This outcome already existed for other reasons (the Blood Collection Room's solid-wall/privacy requirement confirmed 2026-07-31; the Cafe's own separate kitchenette room, in this document since its original version) — it was not previously documented as satisfying this specific NPAAC requirement. **This decision confirms existing design intent and adds the regulatory citation to the documentation trail; it does not require moving any room, wall, or piece of equipment.**

**Documents updated:** `docs/floor-plan-concept.md` (Blood Collection Room Critical Design Requirements — new confirmed bullet with NPAAC citation, plus changelog entry), `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md` (Notes section cross-reference, plus changelog entry).

**Related documents:** `docs/architecture/WDP-PARTNERSHIP-ACTIVATION-PLAN.md` (same NPAAC primary source cited in §2b-i/§2c research this session), `docs/architecture/CAFE-FOOD-SERVICE-INVESTIGATION.md` (the cafe's own food-risk-classification research; unaffected by this decision — that document concerns the cafe's own WA food-business risk tier, not specimen storage).

---

## 2026-09-04 — Entity-structure investigation write-up started (research only, no decision made)

**What happened:** `docs/FOUNDER-FEEDBACK-IMPLEMENTATION-MATRIX.md` row 37 flagged an "entity structure investigation write-up" as PLANNED and never actually written, and `docs/financial-setup.md` Step 1 independently flagged the trust-direct vs. PTY LTD question as a genuine open founder decision. Grace produced the write-up: `docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md`.

**Trigger:** on 2026-09-03 the federal Treasurer released exposure draft legislation for a 30% minimum tax on discretionary trusts from 1 July 2028, with public consultation open until approximately 18 September 2026. YETI Holding Trust (GTT Center Perth's parent structure, corporate trustee YETI Tipi Holdings PTY LTD) is a discretionary trust and falls within scope. The draft also introduces a new option — electing fixed distributions to pre-nominated beneficiaries — as an alternative to restructuring, exempting the trust from the minimum tax without stamp duty exposure but at the cost of the trust's discretionary distribution flexibility. This converts the previously two-way question (trust-direct vs. new PTY LTD) into a three-way question.

**This is NOT a decision.** The new document lays out all three options (trust-direct/current setup, new operating PTY LTD under the trust, fixed-distribution election) neutrally with tradeoffs (tax, liability, admin cost, TPI pension implications for Anthony, impact on Imara's position as beneficiary/funding partner — no operational role assigned to her), and a list of specific questions for the upcoming accountant conversation. No option is recommended or selected. The actual decision remains with Anthony and the accountant.

**Documents updated:** `docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md` (new), `docs/financial-setup.md` Step 1 (added cross-reference, checklist itself not rewritten), `docs/FOUNDER-FEEDBACK-IMPLEMENTATION-MATRIX.md` row 37 (status PLANNED -> IN PROGRESS, dossier Ch12 rebuild itself still outstanding, consistent with the Phase L pattern already used for items 4a/6/22/23/24).

**Related documents:** `docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md`, `docs/financial-setup.md`, `docs/revenue-extraction-options.md`, `docs/dva-tpi-research.md`, `docs/01_conflicts_log.md` (CF-07).

---

## 2026-08-27: Blood Collection Room count: 2 rooms, one per phlebotomist, founder decision overrides evidence-based recommendation

**Decision:** Anthony has decided: **2 Blood Collection Rooms, one per phlebotomist (Chair A/Room 1, Chair B/Room 2), specifically for extra client privacy.** This overrides the evidence-based "1 room, built and serviced for 3 chairs from day one" recommendation reached in `docs/architecture/FIT-OUT-PROGRAM-DECISION-ANALYSIS.md` Part B (Round 3, 2026-08-22) after extensive evidence review. The evidence-based recommendation was sound on its own terms and is retained in full for trace, not deleted or found to be wrong, it is simply overridden by direct founder instruction, a founder's prerogative, not to be second-guessed or reopened.

**Nature of the change:** this is a room-configuration change, not a capacity change. Total phlebotomists (2) and chairs (2) are unchanged, split across 2 separate rooms rather than sharing 1 room. The 18-clients/day AM model, staffing model, and financial figures in `docs/CURRENT-STATE.md` are unaffected.

**New open questions this decision introduces, flagged not resolved:** (1) the growth path: the single-room design's own documented 3rd-chair growth lever no longer straightforwardly applies once the room is split into 2 separate 1-chair rooms; whether growth means a 3rd room or a 2nd chair added to one of the 2 existing rooms is undecided. (2) whether the centrifuge, specimen fridge, and vasovagal recliner are shared between the 2 rooms or duplicated (a real cost question, not decided). (3) whether the per-chair curtain (previously for partitioning multiple chairs within 1 shared room) is still needed now each chair has its own solid door.

**Real consequences propagated:** floor area increases by an estimated ~18-20sqm (using the already-evidenced Option 2 minimum-floor-area estimate from the same decision-analysis document, not a newly invented figure); day-one venue footprint moves from ~239sqm to ~257-259sqm. The existing day-one fit-out dollar cost range (A$228,142-457,559) has NOT been recalculated for the larger footprint, flagged as an open item pending a confirmed venue, not invented here. Room-level fixed infrastructure (solid walls/door, biohazard/no-entry signage, emergency call button) confirmed doubled in the procurement register; several other items (centrifuge, specimen fridge, vasovagal recliner, sharps/waste bins, clinical sink, ventilation, per-chair curtain) flagged as genuinely open shared-vs-duplicated questions, not asserted either way.

**Documents updated:** `docs/architecture/FIT-OUT-PROGRAM-DECISION-ANALYSIS.md` (Part B closure banner, Part D consolidated table, Part F gap list), `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md` (Blood Collection row, Notes, Changelog), `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (Section E header banner plus individual line items E31/E33/E35/E36 confirmed doubled, E03/E04/E15/E16/E24/E32/E38 flagged as open questions), `docs/architecture/PROCUREMENT-CONSTRUCTION-FITOUT.md`, `docs/architecture/FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` (§3.2 contradiction resolved, §5 chair spec updated), `docs/floor-plan-concept.md` (Room Schedule split into 2 rooms, subtotals recalculated), `docs/business-plan.md` (venue footprint and room-count wording corrected, v5.2 -> v5.3), `outputs/master-dossier-v2/index.html` and `outputs/gtt-dash/index.html` (decision registers and narrative mentions updated).

**Related documents:** `docs/architecture/FIT-OUT-PROGRAM-DECISION-ANALYSIS.md`, `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`, `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` Section E.

---

## 2026-08-14 — Naming: conditional leader is SOLENA; retail-strategy question closed

**Decision:** SOLENA is the current conditional naming leader (71.6% on the weighted three-way comparison), ahead of ELOWEN (68.8%) and ELOWYN (65.9%). Not locked.

**Reason:** Three-way comparison in `docs/naming/NAMING-FINAL-COMPARISON.md`, combined with the founder's confirmed business strategy. Elowyn was given a fair Phase 2 evaluation and its severe referral/spelling friction was independently confirmed by two separate design passes, weighing it below the other two despite the cleanest trademark position. Solena's strategic strength (repeat-visit desirability, execution cost, non-pregnancy lifestyle fit) now carries more relative weight because the one thing that most threatened it — a live Class 3 trademark blocking a future product line — has been confirmed not to threaten a business ambition that actually exists.

**Founder input received (2026-08-14):** Is a name-branded retail/product line a genuine strategic ambition? **Answer: NO / not a priority.** Third-party resale (Gaia, Weleda, Mustela) remains the retail strategy. This question is now closed and should not be reopened unless the business model itself changes — see `docs/naming/NAMING-DECISION-STATE.md`.

**Outstanding:** Trademark professional validation, deliberately deferred. Legal status is **KNOWN RISK — NOT YET PROFESSIONALLY CLEARED**, not "clear" or "safe." No attorney has been engaged and none is authorised to be paid at this venture stage. `docs/naming/AUSTRALIAN-TRADEMARK-CLEARANCE-BRIEF.md` is prepared and held for a later validation/funding milestone.

**Reversal condition:** Revisit SOLENA specifically if either (a) a future professional trademark assessment identifies a meaningful Class 44 obstacle (not just the known Class 3 conflict), or (b) a proprietary Class 3 product line later becomes a genuine strategic ambition — in which case re-run the weighting in `docs/naming/NAMING-FINAL-COMPARISON.md` §3 with that new fact, rather than assuming the current percentages still hold.

**Related documents:** `docs/naming/SOLENA-ELOWEN-STRATEGIC-HANDOVER-DECISION-AUDIT.md`, `docs/naming/NAMING-FINAL-COMPARISON.md`, `docs/naming/AUSTRALIAN-TRADEMARK-CLEARANCE-BRIEF.md`, `docs/naming/NAMING-DECISION-STATE.md`.

---

## 2026-08-14 — Brand/experience strategy work proceeds while naming stays conditionally open

**Decision:** Begin name-agnostic brand strategy and customer-experience documentation now, rather than waiting for the naming decision to lock.

**Reason:** The naming decision has two remaining, well-defined blockers (attorney clearance, deliberately deferred; and the retail-strategy question, now answered) that don't touch the underlying business/brand strategy, customer psychology, or experience design — all of which are identical regardless of whether Solena or Elowen ultimately wins. Direct founder instruction: the naming decision should not become an excuse for the rest of the venture's development to stall.

**Documents created:** `docs/strategy/BRAND-STRATEGY-NAME-AGNOSTIC.md`, `docs/experience/CUSTOMER-JOURNEY.md`, `docs/experience/RETURN-LOOP.md`, `docs/strategy/BRAND-ARCHITECTURE.md`, `docs/strategy/PREMIUM-POSITIONING.md`.

**Explicit boundary:** none of the above lock a final logo, palette, type system, signage, packaging, uniforms, or production website for either candidate name — that remains gated on the naming decision per `docs/naming/NAMING-DECISION-STATE.md`'s "DO NOT START YET" list.
- 2026-10-16: shortlist replaced by outputs/LEASING/PROPERTY-SHORTLIST-2026-10.md; old list archived in docs/archive.

## 2026-10-18: Anthony is under the MRCA, not the VEA (permanent correction)

**Decision:** Anthony receives the Special Rate Disability Pension under the Military Rehabilitation and Compensation Act 2004 (MRCA s199). The work threshold is **10 hours a week of remunerative work** (s199(1)(d); cessation s209(b)). Earlier GTT documents that used the VEA 8-hour test (s24A) for Anthony are superseded on that point. Passive trust distributions, dividends and investment income are not remunerative work. Management or employment in the business is. Verify with DVA in writing before relying on it.

**Source:** statute text ingested 2026-10-18 into second-brain knowledge/legal/MRCA-SRDP.md (MRCA compilation No. 77, 29 Sep 2026).


## 2026-10-19: Medicare item numbers corrected; non-pregnancy glucose testing added as a secondary stream

**Decision (Anthony):** (1) Use the verified MBS items: 66548 pregnancy OGTT (A$19.90), 66542 non-pregnancy OGTT (A$18.95), 73928 collection (A$5.95). Remove 66551 and 66554 (HbA1c tests) wherever they were used as the GTT. Files corrected: research/PATHOLOGY-PARTNER-ECONOMICS.md, financial-break-even-staff.md, overhaul-2026-10-16/X-market/PATHOLOGY-PARTNER-TABLE.md, market-research-findings.md. (2) Add non-pregnancy adult female glucose testing (item 66542) as a secondary client stream. GTTs core identity remains a luxury womens day spa and sanctuary.

**Not changed:** every financial figure. No volume, revenue or capacity assumption was added for the new stream.

## 2026-10-19 (round 9): GST and capital return planning basis
Anthony asked for one GST journey. Planning profit before company tax is the after-GST A$281,310.96 a year (A$23,442.58 a month); the old A$422,236.80 counted the ATO's GST as profit and is retired for planning. Owners' startup funds go in as written shareholder loans and are repaid before dividends (steady state: month 15; cautious ramp: month 19). Files: docs/overhaul-2026-10-19/L4-capital/ and L5-r9/. Lounge to stay pregnancy-only (Catherine, SEX-DISCRIMINATION-GTT). Not yet approved by Anthony: staffing re-decision, lab letters.

## 2026-10-20 - Pregnancy only for the whole clinic (Anthony, Round 10)
Anthony: "We will stick with pregnancy only for the whole clinic." Non-pregnancy testing (item 66542) is dropped from the plan. Supersedes the 2026-10-19 non-pregnancy stream. Routes under study: Route 1 (lab runs the collection centre in GTT) and an own specialised lab; no route chosen yet.

## 2026-10-20 - Project name is a placeholder; fertility clinics; letters personal (Anthony, Round 11)
Anthony: "GTT Center Perth" is an unregistered internal placeholder. No ABN, company or address exists. Official letters go from Anthony Zed personally (Founder and Private Healthcare Investor) with the working title only, and must not claim a Pty Ltd, ABN, lease or address. Fertility clinics are a target audience for partnership; GTT serves expecting mothers only (item 66548). Note: Anthony's 2026-09-19 decision that GTT employs both phlebotomists conflicts with Medicare s16A(5AB)(c); to be re-decided.

## 2026-10-25: Founder interview, 24 answers locked (Anthony, Round 18)

**Decision (Anthony):** the 24 founder interview answers are locked as Founder Rules in docs/CURRENT-STATE.md (section 000), outputs/OPERATIONS/CLINICAL-OPERATIONS-PLAN.md (section 13) and outputs/FINANCIALS/3-WAY-FINANCIAL-MODEL-AUD.md (last section). Full list with the file each went into: docs/overhaul-2026-10-19/L13-r18/FOUNDER-INTERVIEW-LOCKED.md.

Headlines: Package 1 A$300 (2 x 30 min services) and Package 2 A$350 (2 services up to 45 min), GST inside, plan on 100 percent Package 1; 20 minute midwife consult; one consult room; two collection rooms with one chair each; venue manager 06:30, clients 06:50, first draw 07:00, midwives 09:00; 2 permanent part-time midwives (fortnightly block, then swap) plus 1 casual; government emails first, then all 4 labs at once with fresh contacts; payroll tax accepted.

**Not changed:** every calculator number and model output. The models still show the previous price set (A$250 and A$300) until Anthony approves copying Theodore R18's results (docs/overhaul-2026-10-19/L13-r18/THEODORE-R18.md) into them. **Open:** answer 23 (refund cap) stays pending until Anthony accepts Theodore R18 Q23; answer 8 (collection item 73928 or 73938) waits for AskMBS.

## 2026-10-26: Financial Center of Truth created (pointer, Theodore R19)

**Pointer only, no decision changed:** docs/FINANCIAL-CENTER-OF-TRUTH.md (and docs/overhaul-2026-10-19/L14-r19/center_of_truth.yml) now hold every money variable in one place, regenerated by theodore_r19.py. R19 adds the card fee the repo never counted on afternoon sales. No calculator number or master figure was changed. Price change (+A$20 on lounge + service) is a recommendation only, awaiting Anthony: docs/overhaul-2026-10-19/L14-r19/THEODORE-R19.md.


## 2026-10-26: Consult timing locked (Anthony, Round 19)

**Founder Rule (Anthony):** the midwife consult happens 1 to 28 days BEFORE the test, on a different day from the test. The client needs the consult to get the referral. The client picks BOTH the consult slot and the test date and time at booking. The consult produces the referral (the pathology request). Never ask this again. Anthony's words: "Before!!! The client needs the consult to get the referral. The consult happens 1-28 days before the test. The client selects their consult appointment and test date and time at booking."

**Consequences (details in docs/overhaul-2026-10-19/L14-r19/WORKFLOW-LOCKED-R19.md):** the 09:00 midwife start no longer clashes with the 07:00 draws; consult demand is 108 a week x 20 minutes = 36.0 hours against 45 paid hours (80 percent) and one consult room; the booking engine must block same-day consult and test and enforce the 1 to 28 day gap.

**Not changed:** every calculator number and model output. Also written into docs/CURRENT-STATE.md (section 000, item 25) and outputs/OPERATIONS/CLINICAL-OPERATIONS-PLAN.md (section 13, item 25).

## 2026-10-27: Round 23 operations lock-in (Anthony, Round 23; recorded by Grace)

**Decision (Anthony):** Anthony is Owner and Director with administrator authority and 0 operational hours; a hired venue manager runs the floor. Midwife roster locked Mon to Sat (2 permanent part-time + 1 casual), midwife day is a lock, fixed daily wage, Path B clients never see a midwife. Meal breaks are rostered in for all staff, never worked through, staff choose stay or leave. Late rule sentence approved. A slot opening inside 48 hours goes to the waitlist and the public page at once. Welcome card and abnormal-results rules as in GTT-READ-FIRST.md. Three companies, Route B, no revenue ramp.

**Operations effect:** written as locked one-line rules in docs/overhaul-2026-10-26/L18-r23/GRACE-R23-OPERATIONS-LOCK-IN.md and PART-2. docs/operations-manual.md updated (banner, opening time, cancellation and waitlist, late arrival, results line, overbooking, new section 9). Fair Work meal-break check done against MA000034, MA000005, MA000027, MA000002 (details in the lock-in file). Timesheet codes MB and MB-R and the 30 minute written agreement for Hair and Beauty staff are proposals awaiting Anthony.

**Not changed:** every calculator number and model output.
