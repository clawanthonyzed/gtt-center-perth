# GTT Center Perth — Capacity, Pricing & Profit Audit

> **2026-07-20 SUPERSEDED — 12-CLIENT MODEL RESTS ON A LATER-REVERSED ASSUMPTION (CONFLICT-08 resolution).** §1 below ("Capacity — The 12-Client / 2-Chair Model") depends on a relaxed Draw 3 rule ("no upper bound... placed at the earliest 5-min chair-free slot ≥X+125"). **This relaxed rule was not carried forward** — the current standing clinical rule, confirmed in `operations-manual.md`'s "Key Rules" table and used by every subsequent verified scheduling document (`scenario-c-sync-timetables.md`, `draw-event-scheduler-findings.md`, `docs/scenario-e-floating-chair-investigation.md`), is **Draw 3 tolerance ±10min of target X+135** — the same bounded-tolerance rule this document's v1.0 originally used before this relaxation. **The current, actively verified AM capacity ceiling is 10 clients/day (Scenario C, 2 chairs) or 15 clients/day (Scenario D, 3 chairs) — not 12.** Do not cite the 12-client figure as a current capacity option. Retained below for historical reference and methodology only — see `docs/01_conflicts_log.md` CONFLICT-08 for full detail.

> **2026-07-14 SUPERSEDED — PM MODEL CORRECTED.** References below to a single "PM Service Therapist" delivering "PM Spa Packages" (Package 1/2/3 pricing) are superseded. The confirmed PM model is: **4 dedicated casual hires** (1 massage, 1 hair, 1 nail, 1 beauty), cross-shift qualified with AM staff, delivering **individual standalone services** (not packages) at ~A$95/session average, staffed on actual hours worked — not a blanket shift. Corrected Month 5+ steady state: **see `profit-loss-tables.md` v2.0 for the current figures (+A$25,087.07/month at Month 5+ steady state) — the figures immediately below this banner are also stale, both due to the PM model change AND the Draw-3-rule reversal noted above.** See `pm-staffing-roster.md` for the PM staffing structure (still valid) and `profit-loss-tables.md` v2.0 for current financial figures.

**Version:** 2.0 | **Date:** 2026-06-11 (Day 51)
**Author:** Idea Lobster (internal review, requested by Anthony for Phase 1 confidence before lease/hire commitments)
**Status:** Internal working document — not yet linked from reading-order.md pending Anthony's review
**Supersedes:** v1.0 (same date). v1.0 is retained in git history for the audit trail — its headline finding ("Scenario A has zero scheduling slack") is corrected in §1.4 below following Anthony's clarification that Draw 3 has no fixed upper bound. Nothing else from v1.0 is silently dropped; superseded items are marked explicitly throughout.

---

## 0. Purpose & Scope (v2.0)

Anthony reviewed v1.0 and raised 10 points. This revision answers all of them:

1. Draw 3 can run "as long as needed" — it's the end of the booking and the test, not a fixed ±10min window.
2. What time can the last test be conducted — we need to fill the whole AM window.
3. There is no hard cut-off time to the AM shift.
4. What's the max client count Scenario C (3 chairs) can handle?
5. Should prices go up a little, accounting for GST?
6. Should we only have 2 packages?
7. Can we get a Medicare rebate?
8. Using Perth standalone (a la carte) service pricing vs market, what should the package prices be?
9. Can we line up a pathology clinic for short-notice phlebotomist relief?
10. Aim high — 12 clients/day.

**Bottom line up front (v2.0):**

- **HEADLINE: 12 clients/day is achievable TODAY with the existing 2 chairs / 2 phlebotomists, at $0 incremental cost.** Same proven 40-min per-chair spacing as Scenario B — just 6 cycles per chair instead of 4 — using Draw 3's corrected flexible-late placement (point 1). Verified table in §1.3. This directly delivers point 10, and it **strictly dominates** v1.0's Scenario A (10 clients) and removes Scenario C (3 chairs) as a *prerequisite* for reaching 12.
- The AM shift is **07:00-13:00 (360 minutes)** per staff-plan.md, not the shorter window implied by operations-manual.md's "12:00-12:30 Close Operations" (point 3 — that section is now flagged stale, §1.6). The latest a chair's Draw 1 can start and still finish Service 2 inside the 360-min window is **~10:55am**; the verified 12-client model's last Draw 1 is **10:50am** — i.e. the schedule already fills essentially the whole available time (point 2).
- **Scenario C (3 chairs) is reframed as a lever for >12 clients/day, or for sick-day redundancy** — not a step needed to reach 12. Max is **18 clients (strict, zero overrun)** or **21 clients (with the same ~5-min tolerance already accepted for the 12-client model's last client)** (point 4).
- **Recommend collapsing 3 packages to 2** — "Standard" (merging old Pkg 1 + Pkg 2) and "Premium" (old Pkg 3) — at **A$250 / A$330 (GST-inclusive)**. This folds in GST-safety margin (point 5) and is cross-checked against services-master-table.md a la carte pricing (point 8), answering points 5, 6 and 8 together.
- **GTT Center Perth cannot bill Medicare directly** under Option A — but the patient's pathology test itself is typically Medicare-bulk-billed/$0 out-of-pocket via PathWest/WDP, independent of our package fee. That's a marketing point, not a new revenue line (point 7, §4).
- **"Relief Pathology Collector" is an established Perth job category at PathWest/WDP** — calling a pathology provider for short-notice locum phlebotomist cover is realistic and should be added to Reed's negotiation scope (point 9, §6.4).
- **New "Lever 0" (AM capacity 8→12/day):** at unchanged costs, Month 5+ Net P&L could rise from the canonical **+A$10,232/mo** to roughly **+A$32,000–34,000/mo (+A$386,000–407,000/yr, ~30-31% margin)** — by far the largest lever identified across v1.0 and v2.0, contingent on a booking-demand ramp (§5.2).

---

## 1. Capacity — The 12-Client / 2-Chair Model — SUPERSEDED, see banner at top of document

> **Reminder: this entire section is superseded (2026-07-20).** The current standing capacity ceiling is 10 clients/day (Scenario C) or 15/day (Scenario D, 3 chairs) — both using the bounded Draw 3 tolerance rule (±10min), not this section's relaxed "no upper bound" assumption. Read on for historical/methodology interest only.

### 1.1 Method — Draw 3 corrected (point 1)

v1.0 modelled Draw 3 as a fixed window, X+125 to X+145 (target X+135, ±10min). **Anthony's correction: Draw 3 has no upper bound** — it is the final blood draw of the test and the end of the booking, so it can run as long as the chair needs it to. The only real constraint is clinical: Draw 3 is the 2-hour-post-glucose-load sample, so it cannot start *before* X+125.

**Revised draw-timing template** (relative to each client's GTT start time X):

| Step | Time (rel. to X) | Duration |
|---|---|---|
| Draw 1 (fasting + glucose drink) | X to X+15 | 15 min, in chair |
| Service 1 | X+15 to X+60 | 45 min |
| Transition buffer | X+60 to X+70 | 10 min |
| Draw 2 (target X+75) | X+70 to X+80 | 5 min, in chair |
| Service 2 | X+80 to X+125 | 45 min |
| **Draw 3 (NEW: flexible-late, ≥X+125, no upper bound)** | placed at the earliest 5-min chair-free slot ≥X+125 | 5 min, in chair |
| Departure | immediately after Draw 3 | — |

The practical effect: Draw 3 no longer creates scheduling pressure on the *next* client's Draw 1. It simply waits for the chair to be free. The chair's true bottleneck is the **125-minute fixed block** (Draw 1 → Service 1 → buffer → Draw 2 → Service 2); Draw 3 absorbs whatever gap remains before the next client arrives — exactly what's needed to "fill the whole time available" (point 2).

I re-verified this with a Python model (relaxed Draw-3 rule + 360-min AM window) — same backtracking method used to verify Scenario B on Day 49.

### 1.2 What time can the last test start? (points 2, 3, 10)

Per staff-plan.md Section 2A, the AM shift for service staff and phlebotomists is **07:00-13:00 (360 minutes)** — confirmed for Massage/Nail/Hair/Beauty therapists and phlebotomists alike ("Both — GTT clients (07:00–13:00)"). This is the real constraint, not operations-manual.md's "12:00-12:30 Close Operations" (§1.6).

A chair's critical path from Draw 1 start to Service 2 end is fixed at 125 minutes. For Service 2 to finish inside the 360-min window, Draw 1 must start by **360 − 125 = 235 minutes after 07:00 = 10:55am**.

**Fasting check:** gtt-clinical-protocol.md requires fasting "from midnight the night before." A 10:55am Draw 1 is **10.9 hours** post-midnight — comfortably inside ADIPS' 8-14hr guideline.

So **10:55am is the absolute latest a chair's Draw 1 can start** while finishing Service 2 inside the 360-min shift (Draw 3 then runs past 13:00, which is fine — point 3, no hard cutoff). The verified 12-client model below has its last Draw 1 at **10:50am** — within 5 minutes of this ceiling, i.e. the AM window is essentially fully utilised already.

### 1.3 Verified 12-client / 2-chair model — THE HEADLINE

Same per-chair pattern as the proven Scenario B (40-min spacing per chair), just **6 cycles per chair instead of 4**, with chairs staggered 20 minutes apart (Chair A starts 07:10, Chair B starts 07:30):

| Client | Chair | Draw 1 | Service 1 | Draw 2 | Service 2 | Draw 3 | Depart |
|---|---|---|---|---|---|---|---|
| C1 | A | 07:10-07:25 | 07:25-08:10 | 08:25-08:30 | 08:30-09:15 | 09:25-09:30 | ~09:35 |
| C2 | B | 07:30-07:45 | 07:45-08:30 | 08:45-08:50 | 08:50-09:35 | 09:45-09:50 | ~09:55 |
| C3 | A | 07:50-08:05 | 08:05-08:50 | 09:05-09:10 | 09:10-09:55 | 10:05-10:10 | ~10:15 |
| C4 | B | 08:10-08:25 | 08:25-09:10 | 09:25-09:30 | 09:30-10:15 | 10:25-10:30 | ~10:35 |
| C5 | A | 08:30-08:45 | 08:45-09:30 | 09:45-09:50 | 09:50-10:35 | 10:45-10:50 | ~10:55 |
| C6 | B | 08:50-09:05 | 09:05-09:50 | 10:05-10:10 | 10:10-10:55 | 11:05-11:10 | ~11:15 |
| C7 | A | 09:10-09:25 | 09:25-10:10 | 10:25-10:30 | 10:30-11:15 | 11:15-11:20 | ~11:25 |
| C8 | B | 09:30-09:45 | 09:45-10:30 | 10:45-10:50 | 10:50-11:35 | 11:35-11:40 | ~11:45 |
| C9 | A | 09:50-10:05 | 10:05-10:50 | 11:05-11:10 | 11:10-11:55 | 11:55-12:00 | ~12:05 |
| C10 | B | 10:10-10:25 | 10:25-11:10 | 11:25-11:30 | 11:30-12:15 | 12:15-12:20 | ~12:25 |
| C11 | A | 10:30-10:45 | 10:45-11:30 | 11:45-11:50 | 11:50-12:35 | 12:35-12:40 | ~12:45 |
| C12 | B | 10:50-11:05 | 11:05-11:50 | 12:05-12:10 | 12:10-12:55 | 12:55-13:00 | ~13:05 |

**Verified — no chair double-booking, no Draw collisions.** C12 (the last client) departs ~13:05, just 5 minutes past the nominal 13:00 AM-shift end — within the "no hard cutoff" allowance (point 3). Every other client departs comfortably inside the window.

**Why this beats v1.0's Scenario A:** same 2 chairs, same 2 phlebotomists, same staff — but **2 more clients/day** (12 vs 10) with **comfortable margins** instead of zero slack. There is no reason to consider the old 10-client/30-min-spacing model as a step; this 12-client/40-min-spacing model is strictly better in every dimension.

### 1.4 v1.0's Scenario A finding — corrected/superseded

v1.0 found that Scenario A (10 clients, 2 chairs, 30-min spacing) had "zero scheduling slack" — under the *old* fixed ±10min Draw 3 window, 8 of 10 clients required the full -10min edge of tolerance.

**This finding is corrected, not just dropped.** Under Anthony's relaxed Draw 3 rule (§1.1), I re-ran Scenario A's 30-min spacing — it becomes comfortable, with natural slack before each chair's next Draw 1. However, **Scenario A is now strictly dominated** by §1.3's 12-client model: same chairs, same phlebotomists, but 12 > 10 clients with equal or better margins. There is no scenario where Scenario A is preferable to §1.3. **v1.0's Scenario A recommendation is withdrawn in favour of §1.3.**

### 1.5 Worst-case "all-Premium" cross-check

Under the 2-package redesign in §3, every client's Service 1 and Service 2 slots remain sized at their existing maximum — 45 minutes each — regardless of which package (Standard or Premium) the client selects (Standard clients use 30-of-45 or 45-of-45 minutes; Premium clients use the full 45 minutes both times). So a day where **every client picks Premium (2x45min)** is **already what the §1.3 timetable assumes** — it creates no new timing conflict. The only effect of an all-Premium day is that service-staff utilisation rises to the figures in §1.6 below (no 15-min downtime windows that day, covered by the Staff Downtime Protocol on lighter-mix days).

### 1.6 Service-staff capacity-minutes (8 staff: 2x Massage, 2x Nail, 2x Hair, 2x Beauty)

**Methodology refinement vs v1.0:** v1.0 used the *session span* (the elapsed clock time of GTT activity, ~245-270min) as the supply denominator. v2.0 uses the **full 360-min AM shift** (staff-plan.md's confirmed 07:00-13:00 commitment), which is what staff are actually rostered and paid for regardless of client count. This is also the same 360-min basis financial-break-even-staff.md uses for its "6-8 sessions per shift = 75-100%" reference ceiling, so the numbers below compare directly against that ceiling. This refinement doesn't change any conclusion — all scenarios remain comfortably below ceiling — but gives a cleaner read.

| Scenario | Clients | Demand (slots × 45min) | Supply (8 staff × 360min) | Utilisation | Per-category split |
|---|---|---|---|---|---|
| B (current, 8 clients) | 8 | 720 staff-min | 2,880 staff-min | **25.0%** | 4 slots/category → 2 each → 25% per staff |
| **§1.3 (NEW, 12 clients/2 chairs)** | 12 | 1,080 staff-min | 2,880 staff-min | **37.5%** | 6 slots/category → 3 each → 37.5% per staff |
| Scenario C, strict max (18 clients/3 chairs, §2) | 18 | 1,620 staff-min | 2,880 staff-min | **56.25%** | 9 slots/category → 4+5 split → 50% / 62.5% |
| Scenario C, max w/ overrun (21 clients/3 chairs, §2) | 21 | 1,890 staff-min | 2,880 staff-min | **65.6%** | 10.5 slots/category → 5+6 split → 62.5% / **75%** |

**21 clients lands one staff member at exactly 75%** — the floor of the 75-100% reference ceiling — a natural "soft max" signal that 21 is genuinely the practical upper bound for this 8-staff configuration, consistent with §2's finding.

**Conclusion: 8 service staff (2/category) structurally cover the 12-client model with 37.5% utilisation — comfortable headroom for both normal operations and an all-Premium day.** No new service-staff hires required. The per-client category-rotation timetable still needs to be hand-verified before activation (operations-manual.md's existing flag stands), but the capacity-minutes math says it fits easily.

### 1.7 Open follow-up — operations-manual.md is now stale (not fixed in this audit)

operations-manual.md currently has "11:00am-12:00pm Wind-Down" / "12:00pm-12:30pm Close Operations — All patients have departed" / "12:30pm EOD Wrap" sections. These conflict with **both** staff-plan.md's confirmed 07:00-13:00 AM shift **and** the §1.3 model (last departure ~13:05). Per reading-order.md's Cross-Document Consistency Rule, fixing this requires a coordinated pass across operations-manual.md, gtt-clinical-protocol.md and gtt-test-reference.md (all of which reference the launch timetable) — **flagged here as a Day 52+ open item, not silently fixed in this audit.**

---

## 2. Beyond 12/Day — 3-Chair Growth Lever (Scenario C reframed) (point 4)

### 2.1 Per-chair maximum under the 360-min window

Using the same relaxed Draw-3 model at 40-min per-chair spacing: a single chair can run **6 clients with zero overrun** (Service 2 of the 6th client ends inside 360min). A **7th client** pushes that chair's Service 2 end to ~13:05 — the *same* ~5-minute overrun already accepted for §1.3's C12. An 8th client would overrun further and is not recommended.

### 2.2 Scenario C's true maximum

- **18 clients (strict, zero overrun):** 3 chairs × 6 clients, all departures inside 13:00-13:05.
- **21 clients (with the same minor-overrun tolerance already accepted in §1.3):** 3 chairs × 7 clients — not a new risk category, just the same ~5-min-per-chair overrun already baked into the 12-client recommendation, applied across all 3 chairs.

**Answer to point 4: Scenario C's max is 18 (strict) to 21 (with accepted tolerance).** §1.6 shows 21 clients lands one staff category at exactly 75% utilisation — the practical ceiling.

### 2.3 When to pursue Scenario C

Scenario C is **no longer required to reach 12/day** — §1.3 does that with $0 incremental cost using the existing 2 chairs. Scenario C remains valuable for two later purposes:

1. **Growth beyond 12/day** (13-21 clients), once the 12-client model in §1.3 is consistently booked out.
2. **Sick-day redundancy** (§6) — a 3rd phlebotomist/chair means the clinic can keep running 2 active chairs even if one phlebotomist is rostered off, instead of collapsing to a single-chair day.

Cost (unchanged from v1.0): +1 phlebotomist (~A$43,068/yr per financial-break-even-staff.md) + 1 phlebotomy chair (A$600-1,500 one-time, per pathology-collection-room.md).

---

## 3. Pricing, GST & Package Redesign (points 5, 6, 8)

### 3.1 The GST question (point 5)

cash-flow.md's GST table classifies "GTT (pathology collection)" as **GST-free** (medical service, GSTD 2004/6) and the standalone PM Spa Packages (Pkg 1/2/3, no testing) as **taxable (10%)**. It does **not** explicitly classify the AM-bundled package fee — the one that includes both the pathology collection *and* the spa services together. This is the gap behind Anthony's question.

Two possible readings, per ATO guidance (GSTR 2001/8 — apportioning the consideration for a mixed supply; ATO "Medical services" GST guidance):

- **(a) Mixed-supply reading:** the AM package fee is apportioned between a GST-free component (pathology collection) and a taxable component (spa services), with GST paid only on the spa portion.
- **(b) Fully-taxable reading:** under Option A, **GTT Center Perth itself doesn't supply the pathology collection to the customer at all** — PathWest/WDP perform and bill for that separately under their own arrangement (option-b-collection-centre.md, line 53). GTT Center Perth's package fee may therefore be **100% taxable** (venue/lounge access + spa services, no GST-free component on our invoice).

Either reading points the same direction: **some or all of the package fee carries 10% GST.** reading-order.md's note that "CF-06 GST treatment clarified (BAS item, not P&L line)" suggests the existing A$200/250/300 figures may be **net-of-GST planning numbers** — i.e. the customer-facing (GST-inclusive) price needs to be ~10% higher to deliver the same net revenue.

**This audit cannot resolve which reading applies — that's an accountant decision.** *This is general guidance from training, not your personal documents — verify before acting (CLAUDE.md Rule 14).* What this audit does is fold a GST-safety margin into the new prices below (§3.3) so that, under either reading, net revenue doesn't end up worse than the old A$200/250/300 net figures — and recommends Reed/Theodore get cash-flow.md's GST table updated with an explicit row for the AM package fee before go-live.

### 3.2 Should we have only 2 packages? (point 6)

**Yes — recommend collapsing 3 → 2.** Reasoning:

- All three existing packages (Pkg 1: 2x30min, Pkg 2: 30+45min, Pkg 3: 2x45min) sit inside the **same** chair/phlebotomist timing template (§1.1) — the clinical/chair cost is identical no matter which package a client picks. There's no cost-side reason for 3 tiers.
- Per v1.0 §1.4 (still valid): Pkg 1/Pkg 2 clients use a 30-min service inside a 45-min slot (15min covered by the Staff Downtime Protocol) — operationally, Pkg 1 and Pkg 2 are the same slot, differing only in *which services* the client picks.
- Three price points only A$50 apart (A$200/250/300) add menu complexity without a clear differentiator. Two tiers — "Standard" and "Premium" — is simpler to market, book, and explain at reception.

**Recommended structure:**

- **Standard** (merges old Pkg 1 + Pkg 2): any combination of GTT-window services totalling up to 75 minutes (30+30 or 30+45min).
- **Premium** (= old Pkg 3): two 45-minute services (90 minutes total), any combination.

### 3.3 New price points — a la carte cross-check (point 8)

services-master-table.md Part A standalone prices for the relevant 30/45-min services: Express massage 30min A$75, Standard massage 45min A$120, Express facial 30min A$95, Signature facial 45min A$130, Classic mani 30min A$55, Gel mani 45min A$75, Express pedicure 30min A$55, Spa pedicure 45min A$65, Lash lift+tint 45min A$95, Blowdry short 30min A$65, Hair mask+blowdry 45min A$85.

| Tier | A la carte combo range | A la carte midpoint |
|---|---|---|
| Standard (30+30 or 30+45) | A$110 (Classic mani + Express pedicure) – A$215 (Express facial + Standard massage) | ~A$160 |
| Premium (45+45) | A$140 (Gel mani + Spa pedicure) – A$250 (Standard massage + Signature facial) | ~A$195 |

**Recommended package prices (GST-inclusive, customer-facing):**

| Tier | Price (incl. GST) | Net of 10% GST | A la carte range | Premium-over-a-la-carte |
|---|---|---|---|---|
| **Standard** | **A$250** | ~A$227.27 | A$110-215 | +16% to +127% |
| **Premium** | **A$330** | A$300.00 | A$140-250 | +32% to +136% |

Both tiers sit comfortably above their a la carte ranges — consistent with v1.0's "GTT convenience premium" framing (the package bundles the GTT pathology collection and free venue/lounge access on top of the spa service, neither of which a la carte customers get). Premium's net price (A$300) equals the **old Pkg 3 GST-inclusive price** — if cash-flow.md's A$300 was already a GST-inclusive figure, this reframing keeps Premium's net revenue roughly flat while resolving the ambiguity (A$330 becomes the unambiguous gross price, A$300 the net). Standard's net (A$227.27) sits between the old Pkg 1 (A$200) and Pkg 2 (A$250) — a sensible merged midpoint.

**Blended-average impact:** the old 30/40/30 mix (Pkg1/Pkg2/Pkg3) blended to A$250 GST-incl. If Standard absorbs the old Pkg1+Pkg2 share (70%) and Premium the old Pkg3 share (30%): new blended = 0.7×A$250 + 0.3×A$330 = **A$274 GST-incl ≈ A$256.36 net** — about +A$6/visit net vs the old A$250 blended average. **The pricing change itself is a modest (~2-3%) net uplift; its real purpose is GST-safety and menu simplification.** The big revenue lever is the capacity move in §5.2, not the price change.

Both new prices remain within the Perth pregnancy-spa-package band (A$200-700, v1.0 §3.3) and well below MIWM's Deluxe (A$380/2hr massage-only) — see §3.4.

### 3.4 Market position — refreshed package table

| Our Package | Price (incl. GST) | Net of GST | Duration | Services |
|---|---|---|---|---|
| **Standard** | A$250 | ~A$227.27 | up to 1.25hr | 2 services, 30+30 or 30+45min |
| **Premium** | A$330 | A$300.00 | 1.5hr | 2x45min, any combo of 4 categories |

vs MIWM Deluxe A$380/2hr massage-only — Premium (A$330/1.5hr) remains cheaper *and* more flexible. MIWM's "Standard" A$50 (Medicare-GP-subsidised gap fee) remains not directly comparable — v1.0's marketing guidance (lead with no wait time, multi-service menu, WA exclusivity; never head-to-head price-match MIWM's A$50) is unchanged.

---

## 4. Medicare Rebate (point 7)

Per option-b-collection-centre.md (line 53), under Option A, **GTT Center Perth (acting as a collection point) cannot bill Medicare directly** — only PathWest or WDP (the Approved Pathology Authority that performs the actual lab analysis) can bill Medicare for the pathology test itself. This is unchanged.

**However**, per PathWest's own patient billing pages, pathology tests referred by a GP with a valid Medicare card are typically **bulk-billed / $0 out-of-pocket** when the test is Medicare-rebateable and referral criteria are met — and an OGTT for GDM screening is a standard Medicare-rebateable referral. WDP similarly bulk-bills concession-card holders for all Medicare-rebateable items.

**What this means for GTT Center Perth:**

- **No new Medicare revenue line for us** — confirmed, no change from option-b-collection-centre.md.
- **But it's a real marketing point**: prospective clients can be told, truthfully, *"your GTT pathology test itself is typically bulk-billed by PathWest/WDP at $0 out-of-pocket (with a valid Medicare card and GP referral) — our package fee covers your spa experience and venue access on top of that."* This pre-empts the objection "am I paying twice for my blood test?" — recommend adding to Poppy's marketing copy and patient-intake-form.md's FAQ.
- **Add to Reed's PathWest/WDP negotiation scope** (alongside the already-flagged pathology-fee item): (a) confirm bulk-billing eligibility criteria for OGTT referrals so reception sets expectations correctly, and (b) ask whether any revenue-share arrangement is available even under Option A's collection-only model (option-b-collection-centre.md notes "revenue sharing is negotiated between ACC and APA" in the context of Option B, but it costs nothing to ask whether any variant applies to Option A too).

---

## 5. Profit Reconciliation

### 5.1 Canonical figure — baseline (pre-Lever-0), unchanged

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

Source of truth: cash-flow.md (canonical month-by-month model, Day 51 reconciliation). The "other figures found in the doc set — all superseded" table from v1.0 §4.2 still stands and is not reproduced here to avoid duplication; nothing in v2.0 changes its conclusions.

### 5.2 NEW — Lever 0: AM capacity 8→12 clients/day (§1.3)

- **Current AM revenue** (8 clients/day, A$250 blended avg, ~22 working days/mo): A$44,000/mo — matches cash-flow.md.
- **New AM revenue at 12 clients/day**, ~22 working days/mo:
  - At *old* A$250 blended avg: 12 × A$250 × 22 = **A$66,000/mo** (+A$22,000/mo)
  - At the *new* §3.3 blended net average (A$256.36): 12 × A$256.36 × 22 ≈ **A$67,680/mo** (+A$23,680/mo)
- **Costs unchanged**: §1.6 shows 12 clients = 37.5% staff utilisation with the existing 8 service staff + 2 phlebotomists — no new hires. Fixed cost base remains A$74,391/mo.
- **Resulting Month 5+ Net P&L:**
  - At old pricing: A$66,000 + A$33,000 (PM) + A$7,623 (cafe/retail) − A$74,391 = **+A$32,232/mo (+A$386,784/yr, ~30.2% margin)**
  - At new 2-tier pricing: A$67,680 + A$33,000 + A$7,623 − A$74,391 = **+A$33,912/mo (+A$406,944/yr, ~31.4% margin)**

**Either way, roughly 3x the canonical +A$10,232/mo baseline — the largest single lever identified across v1.0 and v2.0.**

**Caveat (same as Lever 2's existing open item):** this is a *supply-side* finding — the chairs, staff and timing can handle 12/day. It assumes booking demand fills all 12 slots. Recommend adding an AM 8→12 booking ramp to Bruno's existing PM-ramp validation scope (reading-order.md Open Decisions), tracked over Months 1-5 alongside the PM ramp, before assuming the full +A$22-24K/mo as committed revenue.

### 5.3 GST sensitivity (point 5)

- If §3.1 "Reading (a)" applies (mixed supply, partial GST-free apportionment): effective GST on the package fee is *less* than 10% of the gross price → §3.3's A$250/A$330 prices carry slight extra buffer beyond what's needed.
- If §3.1 "Reading (b)" applies (100% taxable): 10% GST on the full A$250/A$330 → net A$227.27/A$300.00, as used throughout §3.3 and §5.2.

**§5.2's "new pricing" figure (+A$33,912/mo) already uses the conservative Reading-(b) net values — it's a floor, not an optimistic case.** Action: confirm GST treatment with the venture's accountant before go-live (CLAUDE.md Rule 14), and update cash-flow.md's GST table with an explicit row for the AM package fee.

### 5.4 Updated levers summary

| Lever | Type | Impact | Status |
|---|---|---|---|
| **Lever 0 (NEW)** — AM capacity 8→12/day, $0 incremental cost | Supply + demand | Net P&L +A$32,232 to +A$33,912/mo (vs +A$10,232 baseline) | New this audit. Needs booking-demand ramp, like Lever 2. |
| Lever 1 (price) | Price | Superseded by §3's 2-tier A$250/A$330 redesign — folds in a small (~2-3%) net uplift on top of Lever 0 | Updated this audit |
| Lever 2 (PM volume — primary per v1.0) | Demand | +A$187,500/yr, already the Day-51 plan | Unchanged |
| Scenario C (3-chair growth, was "Scenario C" in v1.0) | Supply | +1 to +9 clients/day beyond 12 (13-21 total), ~A$43-45K/yr cost | Reframed §2 |

---

## 6. Sick-Day / Relief Coverage

(v1.0 §5.1-5.3 unchanged and retained below; §6.4 is new.)

### 6.1 The risk

If either phlebotomist is sick on a given day:
- Only 1 chair operational → max ~4 GTT clients that day (half of Scenario B's 8), or the other clients need same-day rebooking.
- Same-day GTT rebooking is high-friction: clients are fasted, often travelled to the venue, and the "no 3-4 week wait" differentiator (vs MIWM) is directly undermined by a forced reschedule.
- This is a single point of failure on a 2-person clinical team — with 2 staff each taking the AU average ~10 sick days/yr, there's a meaningful chance of at least one phlebotomist absence roughly every 1-2 months.

### 6.2 Relief pool budget math

A$15,000/yr casual relief pool covers all 12 roles, not phlebotomists specifically. Phlebotomist base rate A$27/hr; casual loading (~25%) ≈ A$33.75/hr; a 5hr AM shift ≈ A$169/shift.

If ~25-30% of the pool were earmarked for phlebotomist relief (≈A$3,750-4,500/yr), that buys ~22-27 casual shifts/yr — roughly 11-13 covered sick days per phlebotomist per year, in line with the AU average. This assumes a pre-credentialed casual phlebotomist is on standby — credentialing (WDP/PathWest NATA-approved collector status) has lead time and can't be arranged same-day.

### 6.3 Recommended layered protocol (1-3 unchanged, 4 updated for §1.3's model)

1. **Pre-credential a casual/part-time 3rd phlebotomist now** — ties into §2.3's 3-chair growth lever (same hire serves both purposes).
2. **Cross-training** (already in the Staff Downtime Protocol): service-staff cross-train on adjacent categories during downtime — doesn't help phlebotomy (Cert III HLT37215-gated) but reduces single-point-of-failure risk for Massage/Nail/Hair/Beauty absences.
3. **Reduced-capacity-day fallback:** if a service-category staff member is out, drop that day's bookings back to Scenario B's 8-client level via Fresha (4 slots/category = 50% of the new 360-min basis for the remaining staff member — comfortable).
4. **Updated "no late arrivals" note:** §1.4 confirms the §1.3 model has comfortable margins (unlike v1.0's Scenario A), so minor (2-5min) lateness remains a non-event, as under Scenario B. operations-manual.md's existing ">10min late = forfeited slot, rebooked" rule is unaffected.

### 6.4 NEW — Pathology-clinic short-notice relief (point 9)

Both PathWest and WDP (Healius) maintain "Relief Pathology Collector" / "Pathology Collector Reliever" as an established, separately-advertised job category across the Perth metro area — staff who provide coverage across multiple clinic sites on a relief roster basis (confirmed via PathWest's Education/Vacancies pages and WDP's site).

**This supports Anthony's idea directly: calling PathWest or WDP to ask about short-notice locum/relief phlebotomist cover for a sick day is realistic**, as a complement to §6.3's "pre-credential a casual 3rd phlebotomist."

**Recommended addition to Reed's WDP/PathWest negotiation scope** (alongside the Medicare-billing questions in §4): ask whether WDP/PathWest can supply a relief collector to GTT Center Perth's site on short notice (same-day or next-day) under their existing relief-pool arrangements, and at what cost. **If available, this could downgrade §6.3 item 1 (in-house casual 3rd phlebotomist) from "sick-day-critical" to "nice-to-have, primarily for the §2 growth lever"** — likely the faster of the two options since it carries no in-house credentialing lead time.

---

## 7. Summary of Recommendations (v2.0)

1. **(points 2, 3, 10) Adopt the verified §1.3 model as the next step beyond Scenario B** — 12 clients/day, same 2 chairs, same 2 phlebotomists, same staff, $0 incremental cost, comfortably inside the 07:00-13:00 AM shift (last departure ~13:05). This supersedes v1.0's Scenario A *and* its "Scenario C needed for 12" framing.
2. **(point 1) Adopt the corrected Draw 3 rule** (flexible-late, ≥X+125, no upper bound) in operations-manual.md and gtt-clinical-protocol.md going forward — v1.0's fixed ±10min Draw 3 window is superseded.
3. **(point 4) Treat Scenario C (3 chairs) as a growth lever for 13-21 clients/day**, and/or sick-day redundancy (§6.4) — pursue once the §1.3 model is consistently booked out. Max = 18 (strict) to 21 (with the same minor-overrun tolerance already accepted for §1.3's last client).
4. **(points 5, 6, 8) Adopt the 2-tier "Standard" (A$250) / "Premium" (A$330) package structure**, GST-inclusive, replacing Pkg1/2/3 — confirm GST treatment with the accountant before go-live (§3.1, §5.3) and update cash-flow.md's GST table with an explicit row for the AM package fee.
5. **(point 7) No Medicare revenue line for GTT Center Perth itself** — but add "$0 out-of-pocket pathology test via PathWest/WDP" to Poppy's marketing copy and patient-intake-form.md's FAQ; Reed to confirm OGTT bulk-billing eligibility criteria with PathWest/WDP.
6. **(point 9) Add "short-notice relief pathology collector" to Reed's WDP/PathWest negotiation scope** — likely a faster sick-day fix than in-house casual credentialing alone.
7. **NEW — Lever 0 (AM capacity 8→12) is the single highest-impact item identified across v1.0 and v2.0** (~3x the canonical Net P&L). Recommend Bruno's PM-ramp validation scope (reading-order.md Open Decisions) be expanded to include an AM 8→12 booking ramp over Months 1-5.
8. **FOLLOW-UP (not done in this audit):** operations-manual.md's "Wind-Down / Close Operations / EOD Wrap" sections are stale vs staff-plan.md's confirmed 07:00-13:00 AM shift and the §1.3 model (ends ~13:05) — needs a Day 52+ cross-doc consistency pass per reading-order.md's Cross-Document Consistency Rule (touches operations-manual.md, gtt-clinical-protocol.md, gtt-test-reference.md at minimum).
9. **Carryover from v1.0 (still open, low priority):** feasibility.md and review-audit.md still print superseded dollar figures in body text (A$314,235, A$29,192/mo etc.) — worth a cleanup pass.

---

## Sources

- [MIWM Fees](https://www.miwm.com.au/fees), [MIWM GTT Experience](https://www.miwm.com.au/gtt-package)
- [Perth pregnancy massage pricing — Perth Weekend](https://perthweekend.com.au/perth-pregnancy-massage/), [Fresha prenatal massages Perth](https://www.fresha.com/lp/en/tt/prenatal-massages/in/au-perth)
- [Serene Day Spa pregnancy packages](https://serenedayspa.com.au/pregnancy.html), [Hidden Valley Pregnancy Glow Package](https://hiddenvalleyeco.com.au/product/pregnancy-glow-day-spa-package-1-75-hours/), [Keturah Life pregnancy massage](https://www.keturah.com.au/spa-skin-treatments/massage/pregnancy-massage/), [Crown Spa Perth pregnancy treatments](https://www.crownhotels.com.au/perth/crown-spa/spa-treatments/pregnancy)
- [Chilli Couture pricing](https://chillicouture.com.au/pricing/), [JT's Hairstylists price list](https://www.jtshairstylist.com.au/price-list/)
- **(NEW v2.0)** Medicare/pathology billing: [PathWest — Pay a Bill](https://www.pathwest.health.wa.gov.au/For-Patients/Pay-a-Bill), [PathWest — Understanding Medicare Rebates](https://pathwest.health.wa.gov.au/For-Patients/Pay-a-Bill/Medicare-Rebates), [WDP — Billing Policy](https://www.wdp.com.au/patients/billing-policy), [WDP — Oral Glucose Tolerance Test](https://www.wdp.com.au/tests/oral-glucose-tolerance-test)
- **(NEW v2.0)** GST/mixed supply: [ATO — GSTR 2001/8 Apportioning the consideration for a supply](https://www.ato.gov.au/law/view/document?docid=GST%2FGSTR20018%2FNAT%2FATO%2F00001), [ATO — GST and medical services](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-health/medical-services), [ATO — Supply of services through a third party](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-health/supply-of-services-through-a-third-party)
- **(NEW v2.0)** Relief phlebotomist roles: [PathWest — Certificate III in Pathology Collection](https://pathwest.health.wa.gov.au/ResearchAndEducation/Pages/Certificate-III-in-Pathology-Collection.aspx), [PathWest — Vacancies](https://pathwest.health.wa.gov.au/About-Us/Work-With-Us/Vacancies)
- Internal: operations-manual.md, financial-break-even-staff.md, cash-flow.md, staff-plan.md, services-master-table.md, gtt-clinical-protocol.md, option-b-collection-centre.md, pathology-collection-room.md, market-research-findings.md, feasibility.md, review-audit.md, reading-order.md

---

## Changelog

**2026-07-20 (CONFLICT-08 resolution)** — Flagged the entire §1 "12-Client / 2-Chair Model" as superseded — it depends on a relaxed Draw 3 rule ("no upper bound") that was not carried forward into subsequent scheduling documents, which all use the bounded ±10min tolerance rule. The current standing capacity ceiling is 10 clients/day (Scenario C) or 15/day (Scenario D), not 12. See `docs/01_conflicts_log.md` CONFLICT-08 and `docs/scenario-e-floating-chair-investigation.md` (which independently confirms the ±10min rule is the one used in current verified scheduling analysis).
