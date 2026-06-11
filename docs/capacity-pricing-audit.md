# GTT Center Perth — Capacity, Pricing & Profit Audit

**Version:** 1.0 | **Date:** 2026-06-11 (Day 51)
**Author:** Idea Lobster (internal review, requested by Anthony for Phase 1 confidence before lease/hire commitments)
**Status:** Internal working document — not yet linked from reading-order.md pending Anthony's review

---

## 0. Purpose & Scope

Anthony asked four things ahead of any lease/hire commitment:

1. **(a)** Full capacity of 2 phlebotomists + current 8 service staff under 15-min vs 20-min GTT stagger, cross-checked against worst-case Package 3 (2x45min) demand, plus a sketch of allocations for a future 3-chair expansion.
2. **(b)** Whether 8 service staff (2 per category) genuinely cover worst-case demand.
3. Pricing sanity-check: are Package 1/2/3 (A$200/250/300) competitive against MIWM and the Perth pregnancy day-spa market?
4. Reconcile the multiple profit figures scattered across the 45 docs into one number, with improvement levers — open to changes on phlebotomist count, chairs, pricing, etc.

This document answers all four with verified, checkable numbers (Python-backtracked schedules — same method used to verify Scenario B on Day 49). It also adds a sick-day/relief-coverage analysis that falls naturally out of the phlebotomist-count question.

**Bottom line up front:**
- **Scenario A (10 clients, 2 chairs, 30-min/chair spacing) is feasible but has ZERO scheduling slack** — verified to require the full ±10min Draw 3 tolerance on 8 of 10 clients. It's a "free" +A$125K/yr step (no new hires/capex) but operationally tight.
- **A 3-chair/3-phlebotomist model (12 clients) is *more* comfortable than Scenario A** despite serving more clients — it inherits Scenario B's proven-comfortable per-chair pattern exactly. It costs ~A$43-45K/yr (1 more phlebotomist + a A$600-1,500 chair) for ~+A$250K/yr revenue.
- **8 service staff (2/category) are structurally sufficient for both 10 and 12 clients/day**, even under 100% Package 3 demand — utilisation rises from 33% (B) to 46% (10 clients) to 52.5% (12 clients), all comfortably below the ~75-100% "6-8 sessions/shift" ceiling used elsewhere in the financial model.
- **Pricing is broadly well-positioned** vs the Perth market, with one stark outlier (MIWM's A$50 "Standard" package) that needs a marketing explanation, not a price match.
- **The canonical profit figure is +A$10,232/month (+A$122,784/yr, ~12.1% margin) at Month 5+.** Five other figures appear in the doc set; all are superseded — table below.
- **The 2-phlebotomist model has a single-point-of-failure risk** on sick days (Day 1 model requires both simultaneously). Recommend starting WDP/PathWest credentialing for a casual 3rd phlebotomist now — it solves the sick-day risk AND is the same hire needed for the 3-chair expansion.

---

## 1. Capacity Analysis — 2 Phlebotomists, 15-min vs 20-min GTT Stagger

### 1.1 Method

Same draw-timing template as the Day-49-verified Scenario B (operations-manual.md "Key Rules"), relative to each client's GTT start time X:

| Step | Time (rel. to X) | Duration |
|---|---|---|
| Draw 1 (fasting + glucose drink) | X to X+15 | 15 min, in chair |
| Service 1 | X+15 to X+60 | 45 min |
| Transition buffer | X+60 to X+70 | 10 min |
| **Draw 2** (target X+75, ±5min) | X+70-X+80 | 5 min, in chair |
| Service 2 | X+80 to X+125 | 45 min |
| **Draw 3** (target X+135, ±10min) | X+125-X+145 | 5 min, in chair |
| Departure | ~X+145-150 | — |

Each client occupies their chair for ~150 min total (Draw1 + two short draws). I wrote a Python backtracking solver that, for a given chair-spacing, places every Draw 2 / Draw 3 within its tolerance window with zero overlaps — the exact failure mode that caused the Day-49 conflict (Client 1's Draw 2 colliding with Client 5's Draw 1) was caught this way.

### 1.2 Scenario B (current launch model, 8 clients, 20-min stagger) — baseline for comparison

Already verified Day 49. Per-chair spacing 40min, ~30% chair utilisation, draws land on-target with one -5min adjustment. Service-staff utilisation 33% (720 staff-min demand / 2,160 staff-min supply across 270min span). **No changes recommended — this remains the Day 1 model.**

### 1.3 Scenario A (10 clients, 2 chairs, 15-min stagger / 30-min per-chair spacing)

operations-manual.md flagged this as "deferred — full verified timetable not yet built." Built and verified below.

**Verified per-client timetable (Chair A: odd clients, Chair B: even clients):**

| Client | Chair | Draw 1 | Service 1 | Draw 2 | Service 2 | Draw 3 | Depart |
|---|---|---|---|---|---|---|---|
| 1 | A | 07:40-07:55 | 07:55-08:40 | 08:55-09:00 | 09:00-09:45 | 10:00-10:05 | ~10:10 |
| 2 | B | 07:55-08:10 | 08:10-08:55 | 09:10-09:15 | 09:15-10:00 | 10:15-10:20 | ~10:25 |
| 3 | A | 08:10-08:25 | 08:25-09:10 | 09:25-09:30 | 09:30-10:15 | 10:15-10:20 | ~10:40 |
| 4 | B | 08:25-08:40 | 08:40-09:25 | 09:40-09:45 | 09:45-10:30 | 10:30-10:35 | ~10:55 |
| 5 | A | 08:40-08:55 | 08:55-09:40 | 09:55-10:00 | 10:00-10:45 | 10:45-10:50 | ~11:10 |
| 6 | B | 08:55-09:10 | 09:10-09:55 | 10:10-10:15 | 10:15-11:00 | 11:00-11:05 | ~11:25 |
| 7 | A | 09:10-09:25 | 09:25-10:10 | 10:20-10:25 | 10:30-11:15 | 11:15-11:20 | ~11:40 |
| 8 | B | 09:25-09:40 | 09:40-10:25 | 10:35-10:40 | 10:45-11:30 | 11:30-11:35 | ~11:55 |
| 9 | A | 09:40-09:55 | 09:55-10:40 | 10:50-10:55 | 11:00-11:45 | 11:45-11:50 | ~12:10 |
| 10 | B | 09:55-10:10 | 10:10-10:55 | 11:05-11:10 | 11:15-12:00 | 12:00-12:05 | ~12:25 |

**This timetable is mathematically feasible — no chair double-booking.** But it has a critical operational property:

> **Verified zero-slack finding:** I tested the same chair-pairs with Draw 3's tolerance artificially halved to ±5min (instead of the native ±10min). Result: **infeasible** — no valid assignment exists. The native ±10min Draw 3 window is fully required. In the table above, 8 of 10 clients land their Draw 3 at the **-10min edge** of tolerance (e.g. Client 5's Draw 3 target is 10:55 but is placed at 10:45 — the earliest the rule allows).

**What this means in practice:** the schedule is *within protocol* (±10min is an explicit, allowed tolerance — not a violation), but there is **no spare capacity to absorb real-world variance**. A client arriving 3 minutes late, a draw taking 7 minutes instead of 5, or a glucose drink running long pushes the next event outside its tolerance window — which under the existing "10-min rule" means the *next* client's slot is at risk, not just a soft delay. Scenario B has 10-20min gaps between draws (per operations-manual.md's own per-staff table) that absorb this kind of variance for free; Scenario A has none.

This is structural to 30-min spacing (the math doesn't improve by shifting the whole day's start time earlier or later — relative spacing is what creates the conflict).

### 1.4 Worst-case Package 3 (2x45min) cross-check

**Finding: the existing 45-min Service 1 / Service 2 slots in the timetable above ALREADY assume the Package 3 worst case.** Per services-master-table.md and financial-break-even-staff.md's Package Pricing Model:

- Package 1 (2x30min) and Package 2 (30+45min) clients use a 30-min service inside a 45-min slot — leaving 15min of staff downtime within that slot (covered by the Staff Downtime Protocol: room prep, restocking, cross-training, content creation).
- Package 3 (2x45min) clients use the **full** 45-min slot with zero downtime.

So a day where every client picks Package 3 is **already what Scenario A/B's chair timetables are built around** — it does not create a *new* timing conflict beyond what's already verified above. The only effect of an all-Package-3 day is **service-staff utilisation rises to its ceiling** (no 15-min downtime windows that day) — covered in 1.5 below.

### 1.5 Service-staff capacity-minutes (8 staff: 2x Massage, 2x Nail, 2x Hair, 2x Beauty)

| Scenario | Clients | Session span | Demand (slots × 45min) | Supply (8 staff × span) | Utilisation | Per-category split |
|---|---|---|---|---|---|---|
| B (current) | 8 | 270 min (07:55-12:25) | 720 staff-min | 2,160 staff-min | **33.3%** | 4 slots/category, 2 each → 33% per staff |
| A (10-client) | 10 | 245 min (07:55-12:00) | 900 staff-min | 1,960 staff-min | **45.9%** | 5 slots/category → 3+2 split → 55.1% / 36.7% per staff |
| C (12-client, see §2) | 12 | 257 min (07:55-12:12) | 1,080 staff-min | 2,056 staff-min | **52.5%** | 6 slots/category → 3+3 split → 52.5% / 52.5% per staff |

**Reference ceiling:** financial-break-even-staff.md uses "6-8 sessions per 6hr (360min) shift" as the practical per-role capacity ceiling for the PM Service Therapist — i.e. 75-100% utilisation of 45-min sessions. All three AM scenarios above (33%/46%/52.5%) sit comfortably below that ceiling, even at the worst-case Package-3-only mix (which removes the 15-min downtime cushion within each slot but doesn't change the slot count).

**Conclusion for Q1(b): yes, 8 service staff (2/category) structurally cover both 10-client and 12-client scenarios, including 100% Package 3 demand.** The unresolved item is the *specific* per-client category-rotation assignment (which staff does which client's Service 1/2) — operations-manual.md already flags this as "build and verify before activating Scenario A," and that recommendation stands. The capacity-minutes math says it's very likely to fit (Scenario A's tightest staff load, 55.1%, is far from the ceiling); the rotation itself just hasn't been hand-verified the way the chair timetable above has.

---

## 2. Future Expansion — 3-Chair / 3-Phlebotomist Sketch (Scenario C)

Per Anthony's "open to changes... sketch allocations for future expansion to 3 chairs."

### 2.1 Design

Keep the **proven-comfortable 40-min per-chair spacing from Scenario B** (don't reuse Scenario A's tight 30-min spacing). Add a 3rd chair/phlebotomist; stagger arrivals across 3 chairs at 13/14-min offsets (≈ Anthony's "15min" framing) so each individual chair still sees exactly Scenario B's per-chair pattern, just phase-shifted.

**Verified per-client timetable (12 clients, 3 chairs):**

| Client | Chair | Draw 1 | Service 1 | Draw 2 | Service 2 | Draw 3 | Depart |
|---|---|---|---|---|---|---|---|
| 1 | A | 07:40-07:55 | 07:55-08:40 | 08:50-08:55 | 09:00-09:45 | 09:55-10:00 | ~10:10 |
| 2 | B | 07:53-08:08 | 08:08-08:53 | 09:03-09:08 | 09:13-09:58 | 10:08-10:13 | ~10:23 |
| 3 | C | 08:07-08:22 | 08:22-09:07 | 09:17-09:22 | 09:27-10:12 | 10:22-10:27 | ~10:37 |
| 4 | A | 08:20-08:35 | 08:35-09:20 | 09:30-09:35 | 09:40-10:25 | 10:25-10:30 | ~10:50 |
| 5 | B | 08:33-08:48 | 08:48-09:33 | 09:43-09:48 | 09:53-10:38 | 10:38-10:43 | ~11:03 |
| 6 | C | 08:47-09:02 | 09:02-09:47 | 09:57-10:02 | 10:07-10:52 | 10:52-10:57 | ~11:17 |
| 7 | A | 09:00-09:15 | 09:15-10:00 | 10:10-10:15 | 10:20-11:05 | 11:05-11:10 | ~11:30 |
| 8 | B | 09:13-09:28 | 09:28-10:13 | 10:23-10:28 | 10:33-11:18 | 11:18-11:23 | ~11:43 |
| 9 | C | 09:27-09:42 | 09:42-10:27 | 10:37-10:42 | 10:47-11:32 | 11:32-11:37 | ~11:57 |
| 10 | A | 09:40-09:55 | 09:55-10:40 | 10:50-10:55 | 11:00-11:45 | 11:45-11:50 | ~12:10 |
| 11 | B | 09:53-10:08 | 10:08-10:53 | 11:03-11:08 | 11:13-11:58 | 11:58-12:03 | ~12:23 |
| 12 | C | 10:07-10:22 | 10:22-11:07 | 11:17-11:22 | 11:27-12:12 | 12:12-12:17 | ~12:37 |

**Verified comfortable:** I re-ran the ±5min Draw-3-tolerance tightness test (the one that broke Scenario A) against each chair's 4-client set — **all three chairs remain feasible even with Draw 3 tolerance halved to ±5min.** Each chair is running exactly Scenario B's proven 40-min pattern, just phase-shifted — there is no new chair-collision risk.

**One scheduling note:** Client 12 departs ~12:37, about 7-12min later than Scenario A/B's last departure (~12:25). If the 12:00-12:30 "Close Operations" window is hard, shift the whole day's start ~10min earlier (C1 at 07:30 instead of 07:40) to bring C12's departure back to ~12:27.

### 2.2 Service-staff and capacity implications

- 1,080 staff-min demand / 2,056 staff-min supply (8 staff) = **52.5% utilisation, evenly split 3+3 per category** — actually a *more even* load than Scenario A's lopsided 3+2 (55.1%/36.7%).
- No new service-staff hires required for 12 clients, same as Scenario A for 10.

### 2.3 Capital/payroll cost

- **+1 Phlebotomist:** A$43,068/yr (per financial-break-even-staff.md Total Annual Payroll table — same rate as the existing 2).
- **+1 Phlebotomy chair:** A$600-1,500 one-time (pathology-collection-room.md equipment list).
- **Room:** pathology-collection-room.md already recommends 12-14sqm "to allow... multiple bays" vs the 9sqm minimum for 2 chairs — likely fits without floor-area expansion, but worth confirming during the Subiaco/Nedlands site inspections (Quinn's open item).
- **Centrifuge:** currently 1 unit "serves both chairs... within the 10-min window without contention" — adding a 3rd chair's draws to the same centrifuge schedule should be re-checked once the rotation is built, but the 13/14-min stagger spreads draws similarly to B, so contention risk looks low.

### 2.4 The headline finding

**Scenario C (12 clients) is operationally MORE comfortable than Scenario A (10 clients)** — it inherits Scenario B's proven margins exactly, while Scenario A genuinely has none. Scenario C costs ~A$43-45K/yr (1 phlebotomist + 1 chair) for **+4 clients/day vs B (~+A$250K/yr revenue at A$250 blended avg × 250 days)**, vs Scenario A's "free" +2 clients/day (~+A$125K/yr) bought with zero schedule slack.

**Recommendation:** rather than treating Scenario A as the mandatory stepping-stone, start WDP/PathWest credentialing for a 3rd (initially casual/part-time) phlebotomist now. Credentialing has lead time (staff-plan.md: "must be approved collector under their NATA accreditation" — a Week 7 hiring item even for the first 2). Getting ahead of this lead time means that once Scenario B is consistently >80% booked, GTT Center Perth can go **directly to Scenario C** — bigger revenue step, better margins, better staff-load balance — instead of passing through Scenario A's zero-slack window. This same hire also closes the sick-day gap in §5.

---

## 3. Pricing & Market Position

### 3.1 MIWM (the only direct GTT+spa competitor)

| MIWM Package | Price | Includes |
|---|---|---|
| Standard GTT Experience | **A$50** | Pathology + 60min massage/facial + light snacks + bulk-billed GP consult |
| Deluxe GTT Experience | **A$380** | Pathology + TWO 60min massage treatments (2hr spa) |

vs GTT Center Perth:

| Our Package | Price | Includes |
|---|---|---|
| Package 1 | A$200 | 2x30min any service |
| Package 2 | A$250 | 30min + 45min |
| Package 3 | A$300 | 2x45min any combo |

**Deluxe comparison (favourable):** MIWM's A$380 buys 2hr of massage-only. Our Package 3 (A$300, 90min, *any 2 of 4 categories*) is cheaper AND more flexible. Good selling point.

**Standard comparison (stark gap, needs context):** MIWM's A$50 vs our A$200 Package 1 is a 4x difference. **The reason is structural, not a pricing error on our side**: MIWM's A$50 is a "gap fee" on top of a **bulk-billed Medicare GP consultation** — the GP consult itself (likely A$80-120 worth of MBS billing) subsidises most of the visit cost. GTT Center Perth has **no on-site GP and bills no Medicare item** — our packages must cover the full cost of the spa services out of pocket, with zero Medicare offset.

**Recommendation for Poppy/marketing:** never lead with a price comparison against MIWM's "Standard" headline — a prospect doing a naive Google comparison ("$50 vs $200 for basically the same thing") would be misled, and so would we if we tried to match it (we'd be giving away spa time MIWM gets subsidised by Medicare). Instead, lead with: no 3-4 week wait (MIWM is "fully booked 3-4 weeks in advance"), multi-service day-spa menu (massage/nails/hair/beauty vs MIWM's massage/facial-only), and WA-only availability (MIWM is Victoria-only — zero direct competition in WA).

### 3.2 Perth standalone service pricing (services-master-table.md vs market)

| Service | Our price/duration | Perth market | Assessment |
|---|---|---|---|
| Pregnancy massage | A$120/45min (≈A$160/60min equiv.) | A$110-205/60min (mode A$120-160) | **Mid-market — well positioned** |
| Blowdry | A$65/30min (short-med), A$80/45min (long) | A$55-90 (Chilli Couture), A$89-115 incl. cut (JT's) | **Within range — well positioned** |
| Signature facial | A$130/45min | (Crown Spa 60min massage A$230+ w/ 30min facial combo — facial-only price not isolated) | Directionally reasonable; no clean single-service comparable found |
| Gel manicure | A$75/45min | Perth multi-service packages "from A$130" (Endota), A$169+ (Keturah) | Package-vs-single-service — not apples-to-apples; **flag as open item for Reed/Poppy to get a direct single-service quote** |

### 3.3 Package-level positioning vs Perth pregnancy day-spa packages

| Provider/Package | Price | Duration | Services |
|---|---|---|---|
| Hidden Valley "Pregnancy Glow" | n/a (range A$200-700 across Mumma Spa-style packages) | 1.75hr | foot wash + massage + facial + pedicure + afternoon tea (4 services) |
| Serene Day Spa pregnancy package | A$320 | 2.5hr | massage + facial + pedicure (3 services) |
| Mumma Spa packages | A$200-700 | varies | varies |
| **Our Package 1** | **A$200** | 1hr | 2 services |
| **Our Package 2** | **A$250** | 1.25hr | 2 services |
| **Our Package 3** | **A$300** | 1.5hr | 2 services |

Our packages sit **within** the A$200-700 Perth pregnancy-spa-package band, at the lower end on absolute price but higher on a **per-minute** basis (e.g. our Pkg3 = A$300/90min = A$3.33/min vs Serene's A$320/150min = A$2.13/min). This is defensible because **our packages bundle the GTT test + free venue/lounge access** — something no Perth day spa offers — but it means the *spa component alone* is priced at a premium relative to standalone day spas. **Recommendation:** keep current pricing (it's the GTT bundling that justifies the per-minute premium, and Lever 2 in §4 already targets PM-only spa packages, where this per-minute premium is most visible to price-comparing prospects — worth Poppy/Bruno keeping an eye on PM Spa Package conversion rates specifically as a read on whether the per-minute premium is being felt).

---

## 4. Profit Reconciliation

### 4.1 Canonical figure (Day 51, current — use this one)

| Metric | Value |
|---|---|
| Month 5+ steady-state revenue | A$84,623/mo (AM A$44,000 + PM A$33,000 + cafe/retail A$7,623) |
| Month 5+ steady-state costs | A$74,391/mo |
| **Month 5+ Net P&L** | **+A$10,232/mo = +A$122,784/yr (~12.1% margin)** |
| Month 4 (marginal break-even) | +A$4,188/mo |
| Year 1 (incl. M1-3 ramp losses) | +A$37,232 net |
| Year 2 | +A$122,784 |
| Bull case (premium mix + extended PM hours) | +A$25,657/mo = +A$307,884/yr |
| Capital recovery vs A$149,500 baseline | ~Month 24 |
| If 30% trust-distribution tax enacted (not yet legislated) | Y1 → A$26,062, Y2 → A$85,949 (post-tax illustrative only) |

Source of truth: cash-flow.md (canonical month-by-month model, Day 51 reconciliation).

### 4.2 Other figures found in the doc set — all superseded

| Figure | Where it appears | Status |
|---|---|---|
| A$314,235 (Year 1), A$29,192/mo (Month 4), A$20,392/mo (Month 3), "A$900K+ 3-yr" | feasibility.md | Predates Day-50 cost-base reconciliation. feasibility.md itself carries a banner flagging this — but the numbers remain printed in the body, not just the banner. |
| A$22,192/mo at 10% no-show | review-audit.md | Derived from the same superseded feasibility.md model — retained for audit-trail only. |
| "A$12,728/month stable profit, Month 3 break-even" | business-plan.md (original) | RESOLVED Day 50 (IC-07) — replaced by A$5,646/mo, itself replaced by A$10,232/mo Day 51. |
| A$5,646/mo (12-staff/A$675,589 model) | cash-flow.md Day 50 interim | Superseded Day 51 — PM Service Therapist + relief pool added, 3D scan revenue removed. |
| "A$24,651 / 2.8%" | financial-break-even-staff.md, referenced only to say it "does not survive" | Explicitly invalidated — origin predates the current doc set. |
| **A$124,726/year "Gross margin above wages"** | financial-break-even-staff.md, PM Service Therapist section | **Not superseded, but a different metric** — this is ONE role's (PM Service Therapist) individual gross-margin contribution, not the venture's Net P&L. It's coincidentally close in magnitude to the venture-wide A$122,784/yr Net P&L figure (within A$2K) — easy to misquote as the same number. **Flagging this pairing explicitly so nobody cites A$124,726 as "the" profit figure.** |

### 4.3 Improvement levers (from financial-break-even-staff.md Sensitivity, still valid)

- **Lever 1 (price):** raise blended avg package price from A$250 toward A$289 (0% margin) / A$306 (5%) / A$317 (8%) / A$325 (10%), e.g. shifting the A$200/250/300 tiers toward A$230/290/350 → A$260/325/390. Use only as fallback.
- **Lever 2 (PM volume — primary, recommended):** grow PM Spa Packages from 3/day to 6/day (within the existing "6-8 sessions/shift" per-role ceiling). Adds ~A$187,500/yr — **alone closes the entire -A$107,194 gap** without touching Anthony's stated A$200/250/300 prices. This is already the Day-51 plan (PM ramp M1=2/day → M5+=6/day); the Month 5+ A$10,232/mo figure above already assumes this ramp completes on schedule.
- **Bull case** combines a premium package mix with extended PM hours → +A$25,657/mo.

**No new levers identified by this audit beyond what's already in financial-break-even-staff.md** — but §1-2 above add a *third* lever not previously modelled: **AM capacity growth (Scenario A or C)**, worth +A$125K-250K/yr on top of the PM-side levers above, once Scenario B is consistently booked out.

---

## 5. Sick-Day / Relief Coverage

Falls out of the phlebotomist-count question (Q1) — the Day-1 model requires **both** phlebotomists simultaneously (staff-plan.md, financial-break-even-staff.md CF-01 Day 51: "none of them is free to double as PM staff").

### 5.1 The risk

If either phlebotomist is sick on a given day:
- Only 1 chair operational → max ~4 GTT clients that day (half of Scenario B's 8), OR the other 4 pre-booked clients need same-day rebooking.
- Same-day GTT rebooking is high-friction: clients are fasted, often travelled to the venue, and the "no 3-4 week wait" differentiator (vs MIWM) is directly undermined by a forced reschedule.
- This is a **single point of failure on a 2-person clinical team** — statistically, with 2 staff each taking the AU average ~10 sick days/yr, there's a meaningful chance of at least one phlebotomist absence roughly every 1-2 months.

### 5.2 Relief pool budget math

A$15,000/yr casual relief pool covers **all 12 roles**, not phlebotomists specifically. Phlebotomist base rate A$27/hr; casual loading (~25%) ≈ A$33.75/hr; a 5hr AM shift ≈ A$169/shift.

- If ~25-30% of the pool were earmarked for phlebotomist relief (≈A$3,750-4,500/yr), that buys **~22-27 casual shifts/yr** — roughly 11-13 covered sick days per phlebotomist per year, in line with the AU average. This is *workable* but assumes a pre-credentialed casual phlebotomist is on standby and willing to work irregular call-out shifts — credentialing (WDP/PathWest NATA-approved collector status) has lead time and can't be arranged same-day.

### 5.3 Recommended layered protocol

1. **Pre-credential a casual/part-time 3rd phlebotomist now** (ties directly into §2.4's 3-chair recommendation — same hire serves both purposes). This is the only option that fully closes the gap without same-day rebooking.
2. **Cross-training (already in the Staff Downtime Protocol):** service-staff cross-train on adjacent categories during downtime — doesn't help phlebotomy (Cert III HLT37215-gated) but reduces single-point-of-failure risk for Massage/Nail/Hair/Beauty absences.
3. **Reduced-capacity-day fallback:** if a service-category staff member is out and Scenario A (10 clients, 5 slots/category) is active, the remaining staff member would face a 92% utilisation day (5×45min/245min) — likely infeasible without timing conflicts. Protocol: on a confirmed same-category absence under Scenario A, **drop that day's bookings back to Scenario B's 8-client level via Fresha** (4 slots/category = 67% for the remaining staff member — tight but feasible, similar to Scenario A's normal 3-slot load). Under Scenario B itself (4 slots/category, 2 staff), a single absence means the remaining staff member absorbs all 4 (67%) — feasible without dropping bookings.
4. **Hard "no late arrivals" policy under Scenario A specifically** (per §1.3's zero-slack finding) — operations-manual.md's existing ">10min late = forfeited slot, rebooked" rule already covers this, but Scenario A removes the margin that currently makes minor (2-5min) lateness a non-event under Scenario B.

---

## 6. Summary of Recommendations

1. **Launch as planned (Scenario B, 8 clients) — no change.**
2. **Start WDP/PathWest credentialing for a casual/part-time 3rd phlebotomist now** — lead time means this should begin well before Scenario B hits the >80%-booked trigger. Solves §5's sick-day risk AND seeds §2's 3-chair expansion.
3. **When Scenario B is consistently >80% booked, prefer Scenario C (12 clients/3 chairs/3 phlebotomists) over Scenario A (10 clients/2 chairs)** — more revenue (+A$250K/yr vs +A$125K/yr), better margins (inherits B's comfortable timing vs A's zero-slack), more even staff load (3+3 vs 3+2), for ~A$43-45K/yr incremental cost (1 phlebotomist + 1 chair).
4. **If Scenario A is used as an interim step** (e.g. while the 3rd phlebotomist is being credentialed), build and verify the per-client category-rotation timetable first (per operations-manual.md's existing flag) and institute the hard no-late-arrivals policy from §5.4.
5. **Pricing: keep A$200/250/300.** No changes needed — broadly well-positioned vs the Perth market. Marketing should avoid head-to-head price comparisons with MIWM's "Standard" A$50 package (Medicare-subsidised, not comparable) and instead lead with wait-time, service breadth, and WA exclusivity.
6. **Profit: A$10,232/mo (A$122,784/yr, 12.1% margin) is the number to use everywhere.** The PM-volume ramp (Lever 2) is the primary path there and is already the Day-51 plan — no new action needed beyond what cash-flow.md already specifies. AM capacity growth (Scenario C) is a *third*, previously unmodelled lever worth +A$250K/yr once pursued.
7. **Clean-up item (low priority):** feasibility.md and review-audit.md still print superseded dollar figures in their body text (not just banners) — worth a pass to either delete the stale numbers or make the supersession banners impossible to miss, so a future reader skimming the body doesn't pick up A$314,235 or A$29,192 as current.

---

## Sources

- [MIWM Fees](https://www.miwm.com.au/fees), [MIWM GTT Experience](https://www.miwm.com.au/gtt-package)
- [Perth pregnancy massage pricing — Perth Weekend](https://perthweekend.com.au/perth-pregnancy-massage/), [Fresha prenatal massages Perth](https://www.fresha.com/lp/en/tt/prenatal-massages/in/au-perth)
- [Serene Day Spa pregnancy packages](https://serenedayspa.com.au/pregnancy.html), [Hidden Valley Pregnancy Glow Package](https://hiddenvalleyeco.com.au/product/pregnancy-glow-day-spa-package-1-75-hours/), [Keturah Life pregnancy massage](https://www.keturah.com.au/spa-skin-treatments/massage/pregnancy-massage/), [Crown Spa Perth pregnancy treatments](https://www.crownhotels.com.au/perth/crown-spa/spa-treatments/pregnancy)
- [Chilli Couture pricing](https://chillicouture.com.au/pricing/), [JT's Hairstylists price list](https://www.jtshairstylist.com.au/price-list/)
- Internal: operations-manual.md, financial-break-even-staff.md, cash-flow.md, staff-plan.md, services-master-table.md, pathology-collection-room.md, market-research-findings.md, feasibility.md, review-audit.md
