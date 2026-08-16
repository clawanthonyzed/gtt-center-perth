# Scenario D — Growth Capacity Decision: 3rd Phlebotomist/Chair vs. Second Location

**Status:** REFRAMED 2026-08-16, per F4/Anthony's direct instruction — the original 2026-07-17 investigation below (a 15-client/day, 3rd-chair scheduling exercise against the then-committed 10-client model) is now historical and stale — it predates the 2026-08-05 Table 1/Table 2 rebase, the superannuation correction, and the current 18-client/day committed planning model. **Retained below for trace, per this repo's disclose-don't-delete convention, but do not use its figures — see the reframed strategic treatment immediately below instead.**

---

## The Real Strategic Question, Reframed

Once GTT Center Perth is trading at or near its Table 1 planning ceiling (18 clients/day), the next growth decision is not "add one more chair" in the abstract — it is a genuine choice between two structurally different paths:

1. **Add a 3rd phlebotomist/chair at the existing venue** — marginal capacity expansion, same fixed costs (rent, lounge, reception, most treatment staff), incremental revenue on top of an already-profitable base.
2. **Open a second venue** — full replication of the entire cost structure (new rent, new fit-out, new full staff roster, new phlebotomist relationship), but also full replication of the entire revenue ceiling, not just an incremental slice.

These are genuinely different shapes of growth, not the same decision at different sizes — this document frames the choice qualitatively using the venture's own existing financial-model architecture, without inventing new precision this session's tools can't support (a real 3-chair schedule solve is a computational task requiring `tools/sync-treatment-solver.py`/`tools/draw-event-scheduler.py` to be re-run against the current Table 1 cadence specifically — not attempted this round, flagged as the genuine next step in §3).

## 1. Option A — 3rd Phlebotomist/Chair at the Existing Venue

**What's known, from the existing (historical, pre-rebase) investigation below:** adding a 3rd chair to reach 15 clients/day (against the old, now-superseded 10-client/12:30-cutoff model) required a 3rd phlebotomist and pushed peak treatment-line concurrency up, historically estimated at an incremental +A$18,776/month AM contribution (§3-4 below) — but that figure is built on a superseded schedule shape, superseded headcount assumptions, and pre-superannuation labour costs, and should not be quoted.

**What's structurally still true, even without a fresh recompute:**
- A 3rd chair adds phlebotomist labour cost (one more wage line) and, per the venture's own established finding, may or may not add treatment-staff cost depending on whether peak treatment-line concurrency actually rises at the new volume — this is exactly the kind of question `docs/CURRENT-STATE.md` §1's dual-verification method (sweep-line + greedy first-fit) is built to answer precisely, once re-run against Table 1's 25-minute cadence at a higher client count.
- It does **not** require new rent, a new lease, new reception, or a new Venue Manager — the existing venue's fixed-cost base absorbs it.
- WDP's collection-room specification and the ~10:30am start-time guidance (`docs/CURRENT-STATE.md` §1) would need re-checking against a 3-chair draw pattern — a real, not yet resolved dependency, separate from WDP's still-outstanding commercial rental figure.

**What a real answer requires (not done this session):** a fresh solver run (3 chairs, Table 1's 25-min cadence, testing 20-24+ clients/day) to establish the true chair/phlebotomist ceiling and the true treatment-headcount requirement at that ceiling — the same two-independent-method verification already used for every other capacity finding in this repo. This is a scheduling-computation task, not a financial-modelling one, and should be scoped as its own dedicated follow-up phase.

## 2. Option B — A Second Venue

**What the existing financial-model architecture already tells us, without new computation:** a second venue does not share fixed costs with the first — it replicates the entire cost structure in `docs/CURRENT-STATE.md` §5 (Non-Wage Overhead A$13,980/month, the full 8-treatment/2-phlebotomist headcount, a new Venue Manager) against a fresh, unproven local referral pipeline and a fresh market (per `docs/business-plan.md`'s own confirmed framing: "an acknowledged future possibility, not yet committed or scheduled," Month 9+ revenue trigger deliberately removed, no fixed timeline).

**Why this is structurally different from Option A, not just "the same decision at a bigger scale":**
- Full revenue ceiling replication (a second full 18-client/day, or Table 2 12-client/day, model), not an incremental slice on top of an already-derisked base.
- Full startup-capital requirement replication — a second venue needs its own A$251,198-594,900 range (per `docs/CURRENT-STATE.md` §6), not a marginal addition.
- A second, independent pathology-partner relationship and a second, independent referral pipeline (midwife/OB network) — the single largest source of AM revenue risk in the current model, doubled, not incrementally added to.
- Genuinely lower execution risk in one specific sense: it reuses a fully proven, already-operating playbook (staffing model, brand, booking system, supplier relationships) rather than pushing an unproven schedule variant at the existing site.

## 3. What This Comparison Cannot Yet Answer

Both options are currently unquantified at the level of precision this repo's own established convention requires (a real solver-verified schedule, a real recomputed P&L) — deliberately not fabricated here. **The genuine next step, not attempted this round:**
1. Re-run the scheduling solver for a 3-chair variant of Table 1's 25-minute cadence, establishing a real chair/phlebotomist ceiling and treatment-headcount requirement via the same dual-method verification used elsewhere in this repo.
2. Once that exists, compute a real incremental P&L for Option A (marginal revenue minus marginal cost) directly comparable to a real full-replication P&L for Option B (using `data/models/master_financial_model.yml`'s existing Table 1 architecture as the template for "what a second venue's own P&L would look like").
3. Neither of these has been done this session — both are flagged as open, scoped follow-up work, not guessed at.

## 4. Bottom Line

**Neither Option A nor Option B is committed or recommended here.** This is not a decision that can be made yet — it depends on (a) the still-outstanding WDP commercial terms, (b) a confirmed first venue actually opening and trading, and (c) real operating data on referral-pipeline fill rate, none of which exist today. This document exists to frame the choice correctly (two structurally different growth shapes, not one decision at two sizes) so that when the venture is ready to have this conversation, it's asking the right question rather than defaulting to "just add a chair" without considering the alternative.

---

---

## HISTORICAL — Original 2026-07-17 Investigation (STALE, do not use these figures)

**Date:** 2026-07-17
**Status: PROVISIONAL, HISTORICAL.** Every figure below assumes the 12:30 last-departure cutoff, the old 10-client committed model, and pre-superannuation, pre-2026-08-05-rebase labour costs. **Superseded in full by the reframed treatment above.**

### 1. Client / Chair Timetable

Already verified (`am-capacity-weekend.md`, Scenario D): 15 clients, 3 chairs (offsets 0/+10/+20min), zero collisions, last client departs ~12:25 — only a 5-minute buffer before the assumed cutoff. That tightness is itself a reason to want the real WDP number before committing.

### 2. Staff Timetable (corrected 8-person cross-trained pool, historical)

Uses the corrected multi-role model: 4× Massage/Beauty dual-qualified (Staff 1–4), 2× Nails (Staff 5–6), 2× Hair (Staff 7–8). Verified with a real constraint solver — zero double-bookings, every client placed, "client picks 2 services / business picks the order" flexibility used where needed.

| Staff | Bookings |
|---|---|
| Staff 1 | 07:15–08:00 C1 (Massage), 08:35–09:20 C7 (Massage), 09:25–10:10 C11 (Massage), 10:15–11:00 C15 (Massage) |
| Staff 2 | 07:35–08:20 C3 (Massage), 08:40–09:25 C3 (Beauty), 09:40–10:25 C7 (Beauty), 10:30–11:15 C11 (Beauty) |
| Staff 3 | 08:05–08:50 C5 (Massage), 08:55–09:40 C9 (Massage), 09:55–10:40 C13 (Massage), 11:00–11:45 C13 (Beauty) |
| Staff 4 | 08:20–09:05 C1 (Beauty), 09:10–09:55 C5 (Beauty), 10:00–10:45 C9 (Beauty), 11:20–12:05 C15 (Beauty) |
| Staff 5 | 07:25–08:10 C2 (Nails), 08:15–09:00 C6 (Nails), 09:15–10:00 C10 (Nails), 10:05–10:50 C14 (Nails) |
| Staff 6 | 07:55–08:40 C4 (Nails), 08:45–09:30 C8 (Nails), 09:35–10:20 C12 (Nails) |
| Staff 7 | 08:30–09:15 C2 (Hair), 09:20–10:05 C6 (Hair), 10:20–11:05 C10 (Hair), 11:10–11:55 C14 (Hair) |
| Staff 8 | 09:00–09:45 C4 (Hair), 09:50–10:35 C8 (Hair), 10:40–11:25 C12 (Hair) |
| Phlebotomist A/B/C | 15 draws each across their 5 chair-assigned clients (see am-capacity-weekend.md Scenario D per-chair breakdown) |

### 3. P&L — Historical Current (7-staff, 2 phlebotomists) vs Historical Scenario D (8-staff, 3 phlebotomists)

Both use the conservative safe price (A$250/client) and 22 trading days/month — **pre-superannuation, pre-rebase figures, do not use.**

| | Historical then-current (10 clients/day) | Historical Scenario D (15 clients/day) |
|---|---|---|
| Revenue | 10×22×$250 = **$55,000** | 15×22×$250 = **$82,500** |
| Phlebotomist labor | 2× ≈ **$7,178** | 3× ≈ **$10,767** |
| Treatment labor | 7-staff ≈ **$35,942** | 8-staff ≈ **$41,077** |
| Opening cost (07:00 start) | **$980** | **$980** |
| **AM Direct Contribution** | **≈+$10,900/month** | **≈+$29,676/month** |
| **Incremental gain from 3rd phlebotomist** | | **≈+$18,776/month** |

### 4. What Was Still Missing (historical, unresolved when this section was written)

1. The WDP cutoff itself was not confirmed at the time.
2. One-off costs (3rd phlebotomist recruitment, WDP credentialing) were not included.
3. Treatment labor figures were approximate, not a full payroll recalculation.

---

## Changelog

**2026-08-16 (F4 reframe)** — Replaced the outdated, stale 15-client/3rd-chair scheduling exercise (built against the now-superseded 10-client model) with a real strategic capacity decision: 3rd phlebotomist/chair at the existing venue vs. a second location, using the existing financial-model architecture qualitatively. Original content retained below as HISTORICAL, not deleted, per this repo's disclose-don't-delete convention. No new scheduling-solver computation was performed this round — flagged as the genuine next step (§3 of the reframed treatment).

**2026-07-17 (original)** — Created as a provisional 3rd-phlebotomist investigation, pending WDP cutoff confirmation.
