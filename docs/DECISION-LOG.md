# Decision Log

**Purpose:** a running, append-only record of major project decisions, so future sessions/agents don't rediscover the same open questions or silently contradict a decision already made. Add new entries at the top. Do not delete or rewrite prior entries — correct forward, the way the rest of this repository's changelogs already work.

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
