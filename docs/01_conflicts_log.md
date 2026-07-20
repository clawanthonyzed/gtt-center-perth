# GTT Center Perth — Conflicts Log

**Compiled:** 2026-07-19 | **Compiled by:** Grace (Operations Manager, audit pass)
**Purpose:** Every detected conflict, duplicate, or inconsistency across the docs corpus, with resolution status. Companion to `00_document_inventory.md` and `review-audit.md` (which already logs many historical conflicts — this log adds newly found ones and cross-references the historical ones still open).

---

## CONFLICT-01 | `research-supplement-day48.md` — Stale Duplicate

**Status: RESOLVED 2026-07-19**

**Finding:** `docs/research-supplement-day48.md` and `docs/research-supplement-day48-ARCHIVED.md` are byte-identical (confirmed via `diff` — zero output). `reading-order.md` already correctly lists `research-supplement-day48-ARCHIVED.md` as "ARCHIVED. Merged into research.md v3.0." The non-archived copy (`research-supplement-day48.md`) was never renamed or removed when the Day 48 supplement was merged into `research.md` v3.0 (confirmed via `research.md`'s own header: "Supersedes: v2.0 + research-supplement-day48.md").

**Root cause:** When the merge into research.md v3.0 happened (2026-06-09), one copy was renamed to `-ARCHIVED` and the original filename copy was left in place instead of being deleted or also renamed.

**Resolution:**
- Added a superseded banner to `research-supplement-day48.md` pointing to `research.md` as canonical.
- Added an entry for `research-supplement-day48.md` in `reading-order.md`'s Reference Only table, marked ARCHIVED with the same status as its sibling.
- File retained (not deleted) to preserve history per repo convention (other archived docs are kept, not removed).

---

## CONFLICT-02 | `floor-plan-v3.*` vs `floor-plan-visual.*` — Version Mismatch, No Supersession Marker

**Status: RESOLVED 2026-07-19 (partial — see note on PDF)**

**Finding:** Two floor plan concept renders exist with different layouts and no cross-reference:
- `floor-plan-visual.html` / `floor-plan-visual.pdf` — git history confirms this is v2 (commit d85c56c, 2026-07-01), box-fill room layout.
- `floor-plan-v3.svg` / `floor-plan-v3.pdf` — git history confirms this is v3 (commit 25bdc5d, 2026-07-10), open-plan lounge with furniture and accessible door swing arcs — described in its own commit message as a deliberate revision of the earlier version.

`HANDOFF.md` (2026-07-17, most recent session summary) lists `floor-plan-v3.svg`/`.pdf` as current with no mention of the v2 files, implying the v2 files are stale but this was never stated explicitly anywhere in the docs themselves, and neither file was flagged as superseded.

**Resolution:**
- Added a red, bold superseded banner directly into `floor-plan-visual.html`'s visible subtitle, pointing to `floor-plan-v3.svg`/`.pdf` as current.
- Added entries for all four floor-plan files (plus `floor-plan-concept.md`) to `reading-order.md`'s Reference Only table with accurate status.
- **`floor-plan-visual.pdf` (binary) could not be text-edited** with available tools — its superseded status is recorded in `reading-order.md` and `00_document_inventory.md` instead. If Anthony wants the PDF itself visually marked, it needs to be re-exported from the (now-updated) HTML or regenerated.

---

## CONFLICT-03 | Scenario B (8 clients/day) vs Scenario C Sync (10 clients/day) — Operational Model Mismatch

**Status: PARTIALLY RESOLVED 2026-07-19 — flagged, not fully rewritten**

**Finding:** This is the most significant conflict found this session. Per `HANDOFF.md` (2026-07-17, the most recent and most authoritative session summary), **the current committed operational model is Scenario C, synchronized-chair-start: 10 clients/day, 07:00 first draw** — fully verified in `docs/scenario-c-sync-timetables.md` (programmatic double-booking check, zero conflicts across 2 phlebotomists and 8 treatment staff).

However, `docs/operations-manual.md` — the primary day-to-day operations reference, read by all staff — still contains an entire "GTT SCHEDULING TIMETABLES" section built around **Scenario B (8 clients/day, 07:40 first draw)**, labelled "LAUNCH MODEL," with full per-client and per-staff tables. This is the document staff-plan.md, gtt-clinical-protocol.md, and patient-facing materials point to as authoritative.

`docs/gtt-clinical-protocol.md` also stated "8 GTT patients per day" and pointed to operations-manual.md for the verified timetable — doubly wrong (wrong number, and pointing to a now-also-wrong source).

**Why this matters:** If a Venue Manager or new staff member reads `operations-manual.md` cover-to-cover (as instructed by `reading-order.md`), they will train on an 8-client/07:40-start model that does not match the actual committed 10-client/07:00-start model. This could cause real scheduling errors at launch — under- or over-booking the day, wrong arrival-time communications to patients, wrong phlebotomist load expectations.

**Secondary finding:** Even within the "Scenario C" family, there are two versions:
1. Staggered Scenario C (20-min offset between chairs) — in `am-capacity-weekend.md`, dated 2026-07-16.
2. Synchronized Scenario C (both chairs start together) — in `scenario-c-sync-timetables.md`, dated 2026-07-17, one day newer, described as adding a treatment-staff concurrency check "previously only asserted, not built."

The synchronized version is the more recent and more rigorously verified of the two, and `am-capacity-weekend.md` itself (line ~405) confirms the sync variant is consistent with the original Scenario C finding. **`scenario-c-sync-timetables.md` should be treated as the single canonical timetable.**

**Resolution so far:**
- Added a clear superseded banner to `operations-manual.md`'s GTT Scheduling Timetables section, pointing to `scenario-c-sync-timetables.md` as canonical. **The Scenario B tables were NOT deleted or rewritten** — only flagged — because a full rewrite of the per-client/per-staff tables, the "Notes" analysis, and the Scenario A/D cross-references in that section is a substantial editorial task warranting its own dedicated pass (recommended as a priority action — see `04_roadmap_next_steps.md`).
- Updated `gtt-clinical-protocol.md`'s client count from 8 to 10 and repointed its reference to `scenario-c-sync-timetables.md`.
- Added a clarifying note to `staff-plan.md` confirming the headcount conclusions (2 phlebotomists + 8 treatment staff, 2 per category) are unaffected by the Scenario B->C change — Scenario C explicitly runs on the same staff numbers, just a tighter schedule.

**Not yet resolved — recommended follow-up (see roadmap):**
- Full rewrite of `operations-manual.md`'s GTT Scheduling Timetables section to replace the Scenario B tables with the Scenario C sync tables (or a direct pointer + brief summary, if a full table duplication isn't desired).
- Flag/update `scenario-c-timeline.html` (the visual companion to the staggered, non-sync Scenario C) — likely also superseded by `scenario-c-sync-timeline.html`, not confirmed or flagged this session due to time.
- Confirm whether any patient-facing materials (SMS templates, confirmation emails, website copy) reference "8 clients" or 07:40-based times anywhere — not checked this session.

---

## Cross-Reference: Historical Conflicts Already Logged in `review-audit.md`

`review-audit.md` (the pre-existing full business audit) already documents a substantial set of conflicts, most now resolved. Listed here for completeness — do not re-litigate:

| ID | Conflict | Status per review-audit.md |
|---|---|---|
| IC-01 | Ramp-up assumptions (financial-model.md vs cash-flow.md) | RESOLVED Day 50 — cash-flow.md canonical |
| IC-02 | Staff hours (staff-plan.md vs cash-flow.md/gtt-test-reference) | RESOLVED Day 51 — AM-only confirmed, PM via dedicated hire |
| IC-03 | Package pricing (multiple conflicting price lists) | RESOLVED Day 50 — standardised, later further resolved to Package 2/3 only |
| IC-04 | Operating days | RESOLVED — no change needed |
| IC-05 | GTT capacity (6-9 vs 5 slots) | RESOLVED Day 49 — 8 clients/2 phlebotomists (**now itself superseded by Scenario C, 10 clients — see CONFLICT-03 above**) |
| IC-06 | Startup capital | RESOLVED Day 50 — cash-flow.md figures canonical |
| CF-07 | TPI pension interaction (Imara/Anthony) | DEFERRED, not blocking — still requires DVA-adviser sign-off. Clarified 2026-07-19 that this is separate from the new Venue Manager payroll role. |
| OG-03 | Emergency response plan | RESOLVED Day 48 — emergency-plan.md exists. Wording refreshed 2026-07-19 (Imara -> Venue Manager). |

**Note:** IC-05's "RESOLVED Day 49" status is now itself stale per CONFLICT-03 above — the audit trail shows scheduling conflicts have been resolved and re-opened multiple times as the model evolved (8 -> 10 clients). This is a natural consequence of active iteration, not a process failure, but reinforces the recommendation in the roadmap to designate one single "current operational model" document that everything else points to, rather than letting the most-recently-edited file become accidentally authoritative.

---

## Other Consistency Checks Performed (No Conflict Found)

- **Package pricing:** `services-pricing-locked.md`, `HANDOFF.md`, and `financial-break-even-staff.md` all agree: 2 packages only, at A$250 and A$300 (renamed to Package 1/Package 2 respectively, 2026-07-20 — see `services-pricing-locked.md` changelog). Consistent.
- **Saturday/Sunday model:** `HANDOFF.md`, `am-capacity-weekend.md` agree: Saturday reuses AM model + PM standalone (hours-based costing), Sunday closed. Consistent.
- **PM staffing model:** `pm-staffing-roster.md` is consistently cited as canonical by `business-plan.md`, `staff-plan.md`, and `operations-manual.md` banners. Consistent (all three defer to it correctly).
- **Superannuation rate (12%):** Consistent across `staff-plan.md`, `hr-framework.md`, `financial-setup.md`.
- **No subtenants:** Consistent across `staff-plan.md`, `operations-manual.md` (Day 51 update explicitly removes subtenant-rent references). **Exception: `workflow.md` still describes a sublet model (massage/nails/hair/scan) — flagged below.**

**2026-07-20 (package renumbering)** — Updated the package-pricing consistency-check line above to reflect the renaming of the 2 surviving packages to Package 1 (A$250)/Package 2 (A$300) — see `services-pricing-locked.md` changelog. Historical CONFLICT/IC entries elsewhere in this log describing the earlier Package 1/2/3 (A$200/250/300) naming are left as-is, since they are a historical record of past resolutions, not a statement of current fact.

---

## CONFLICT-04 | `workflow.md` — Stale Subtenant/Sublet Staffing Model

**Status: FLAGGED 2026-07-19 — not rewritten**

**Finding:** `docs/workflow.md`'s "Staffing Model (Launch)" table describes massage therapist, nail technician, hairdresser, and keepsake scan operator as **"Sublet"** roles, with phlebotomist as PathWest/WDP staff. This entirely contradicts the current, canonical model in `staff-plan.md`, `financial-break-even-staff.md`, and the Day 51 updates elsewhere: **all service delivery staff are employed** by GTT Center Perth (wage-based, not room rental), **there are no subtenants**, and the phlebotomists are **employed directly** by GTT Center Perth (not PathWest/WDP staff) — WDP/PathWest only provides the NATA accreditation umbrella and credentialing.

**Likely cause:** `workflow.md` appears to be an early draft (no version/date banner, no supersession markers anywhere in the file) that predates the Day 51 "no subtenants, employed model confirmed" decision and was never updated or flagged.

**Resolution:** Added a note in this session's changelog entry within `workflow.md` flagging the staffing table as stale, pointing to `staff-plan.md` as the current model. **The table itself was not rewritten** — recommended as a follow-up action (see roadmap) since it requires re-deriving the "keepsake scan operator" row too, which no longer exists in current scope (3D scan removed entirely per Day 51).

---

## CONFLICT-05 | `hire-purchase-china.md` — 3D Scanner Section Timing

**Status: RESOLVED 2026-07-19 (reframed twice, same day — see below)**

**Finding:** §1C "3D Keepsake Ultrasound Scanner" described purchasing a 3D scanner or using Bloom Baby Ultrasound as a subtenant as live startup options, including specific model/pricing tables.

**Resolution history:** First pass (same day) incorrectly flagged this as "contradicts Day 51 — 3D scan removed entirely" and struck through the content. **Corrected same day per direct founder clarification: the 3D scanner is a future income stream, not part of startup/launch scope — this is a timing correction, not a full removal.** §1C was rewritten (not struck through) to keep the equipment/pricing research as reference material for a later revisit, explicitly labelled "not a current purchase decision or startup budget line." Budget Summary rows restored with "future/Phase 2, not startup capital" labelling instead of strikethrough. The Bloom Baby subtenant framing remains correctly noted as inapplicable (no subtenants under the current employed-staff model) regardless of when 3D scan might be revisited.

---

## CONFLICT-06 | `market-research-findings.md` — 3D Scan Positioned as Core Differentiator

**Status: RESOLVED 2026-07-19 (reframed, same day)**

**Finding:** §1 (MIWM competitor comparison table) and §8 (Key Market Insights Summary) both positioned "in-house 3D keepsake scanning" as GTT Center Perth's core competitive differentiator, including the claim "GTT Center Perth = first and only GTT + full day spa + 3D scan in Australia." This is a more consequential instance than most other 3D-scan stragglers because it's framed as *the* marketing differentiator — if used to brief Poppy (marketing) or any external marketing material, it would actively misrepresent the venture's launch-day offering.

**Resolution:** Rewrote §1 and §8 to reframe the core launch differentiator around the GTT wait-time experience itself (multi-client concurrent model), with 3D scan moved to a clearly-labelled "Future / Phase 2 consideration" note — not deleted from the plan, correctly reflecting Anthony's clarification that 3D scan is a future income stream, not removed entirely.

---

## CONFLICT-07 | `ivy-booking-system.md` — Subtenant/Room-Rental Booking Model

**Status: RESOLVED 2026-07-19 (fully rewritten, same day — see below)**

**Finding:** The "Practitioner Management," "Admin View," and "Subtenant Rent Billing" sections described a subtenant/room-rental practitioner model — individual practitioner calendar logins as independent subtenants, weekly subtenant rent invoicing via Xero, direct debit for rent collection. This entirely contradicted the confirmed employed-staff, no-subtenant model. Also contained a stale "8-client/morning" reference (same root issue as CONFLICT-03) and listed 3D Keepsake Scan / Dietitian consultation as current bookable services in the Step 3 booking flow.

**Resolution history:** First pass (same day) flagged each affected section with superseded banners/strikethrough but did not rewrite. **Fully rewritten same day per direct founder instruction:** "Practitioner Management" retitled "Staff Management" (employed-staff calendar logins, Venue Manager-set rosters), subtenant rent billing/invoicing replaced with a payroll reference (Xero, weekly pay run), "4-5 subtenants" corrected to "12 employed staff," and the booking-flow service list corrected to remove 3D Keepsake Scan and Dietitian consultation as current options and fix service durations to match the current package structure. Core platform comparison and Fresha recommendation were never affected by this issue and remain valid throughout.

---

## Minor Findings (Contradiction Scan, 2026-07-19)

- **`extended-wellness-services.md`:** stale cross-reference link to the now-archived `bloom-baby-case-study.md` in its "Related Documents" list. Fixed with a strikethrough/archived note — no other issues found in this file. **RESOLVED.**
- **`onboarding.md`:** used generic "Manager" throughout (19 instances) rather than "Venue Manager" — not a factual contradiction (unambiguous same role), but a naming-consistency gap versus the rest of the post-rename corpus. **RESOLVED 2026-07-19 (same day) per direct founder instruction** — all 19 instances corrected to "Venue Manager." Also corrected one self-conditioning "subtenants only" insurance checklist line that was inapplicable (not wrong) under the no-subtenant model.
- **`business-plan.md`, `brand-guide.md`:** found via the same-day 3D scanner scope check — `business-plan.md`'s Day 51 banner incorrectly said 3D scan was "removed from scope entirely" rather than "future income stream, not launch scope"; `brand-guide.md`'s Instagram bio and highlight-cover-icon list both advertised "Scan" and "Dietitian" as current launch services. **RESOLVED** — both corrected.
- **`equipment-costs.md`, `privacy-policy.md`, `staff-profiles/*.md`:** reviewed in full — no contradictions found. `staff-profiles/*.md` all correctly reference the current Scenario C (10-client) volume already.

---

## Summary

| Conflict | Severity | Status |
|---|---|---|
| CONFLICT-01: research-supplement-day48.md duplicate | Low (no operational impact, just clutter/confusion risk) | RESOLVED |
| CONFLICT-02: floor-plan v2/v3 mismatch | Low-Medium (fit-out brief risk if wrong version used) | RESOLVED (HTML); PDF flagged, not edited |
| CONFLICT-03: Scenario B vs Scenario C sync | **HIGH** (training/scheduling risk if operations-manual.md read as-is) | FLAGGED, partially resolved — full rewrite recommended as priority action |
| CONFLICT-04: workflow.md stale subtenant model | Medium (could mislead a new reader on employment structure) | FLAGGED, not rewritten — recommended as follow-up action |
| CONFLICT-05: hire-purchase-china.md 3D scanner timing | Medium (equipment budget/planning risk) | RESOLVED — reframed as future/Phase 2, not removed |
| CONFLICT-06: market-research-findings.md 3D scan as differentiator | **Medium-High** (marketing/positioning risk if used to brief external material) | RESOLVED — reframed to future/Phase 2 addon |
| CONFLICT-07: ivy-booking-system.md subtenant booking model | Medium (booking-system spec risk if built as-is) | RESOLVED — fully rewritten to employed-staff model |
| CONFLICT-08: multi-way PM-profitability and AM-capacity-figure discrepancies (Phase 6/7) | **Medium-High** (affects headline financial figures in business-plan.md/executive-summary.md) | **RESOLVED 2026-07-20** — see resolution detail below. Fixed in `pm-staffing-roster.md`, `feasibility.md`, `capacity-pricing-audit.md`, `business-plan.md`, `executive-summary.md`, `profit-loss-tables.md`, `cash-flow.md` |
| CONFLICT-09: payment-timing policy inconsistency (full prepayment vs A$30 deposit) | Medium (customer-facing billing/booking policy — must be resolved before any booking flow goes live) | **RESOLVED 2026-07-20** — Anthony confirmed full payment at booking. Fixed in `financial-setup.md`, `operations-manual.md`, `ivy-booking-system.md`, `website-spec.md`, `docs/pricing-billing-strategy.md` |

**Note on CONFLICT-03 (Scenario B vs C):** Anthony's Scenario D single-client 09:55 timing question was verified 2026-07-19 (see `am-capacity-weekend.md` "Can Client 15 Start at 09:55 Instead of 10:00?" and the updated recommendation in `king-edward-start-time-constraint.md`) — this is a scheduling verification, not a documentation contradiction, so it isn't numbered as its own conflict here, but it's directly related to CONFLICT-03's root issue (the AM capacity model evolving faster than some documents track) and resolves the King Edward "before 10am" question for Scenario D specifically.

**CONFLICT-08 detail — RESOLVED 2026-07-20:** Three separate discrepancies surfaced while verifying `business-plan.md`, `executive-summary.md`, `profit-loss-tables.md`, `cash-flow.md`, and `break-even-sensitivity-analysis.md` against Phase 6/7 spec, all now resolved:

1. **PM-shift profitability — RESOLVED.** `pm-staffing-roster.md` (2026-07-14) reported the PM shift alone as a loss (-A$4,384/month) at Month 5+ steady state under the pre-Scenario-C (8-client) AM model. Verified this was an artifact of the stale 8-client AM revenue figure (A$44,000/month) rather than a genuine standalone loss — substituting the current 10-client Scenario C AM revenue (A$55,000/month) alone flips the reported figure to a positive contribution (~+A$6,616/month using `pm-staffing-roster.md`'s own PM/ancillary/cost figures). `profit-loss-tables.md` v2.0 (2026-07-17, more recent, matches `HANDOFF.md` exactly) is confirmed as the current authoritative figure: **+A$25,087.07/month at Month 5+ steady state.** Fixed in: `pm-staffing-roster.md` (banner + table flagged), `profit-loss-tables.md` (PM/ancillary ramp figures filled in, Years 1-3 corrected), `cash-flow.md` (pointer updated), `business-plan.md` (§4/§6/§9/§13 corrected), `executive-summary.md` (Financial Snapshot corrected).

2. **Market-sizing figures — RESOLVED.** WA births cited as ~18,000 in `research.md` v3.0 vs ~35,000 in `feasibility.md` (with a screening rate of ~78% in one place vs "95%+, universal" in another). `research.md` v3.0 is the authoritative source — it is the explicitly-merged, most heavily cross-checked research document in this corpus, with a clear ABS/AIHW derivation chain that is internally consistent against national-level figures. `feasibility.md`'s ~35,000/~28,000/95%+ figures could not be traced to a specific AIHW table this session and are corrected to match `research.md`: ~18,000 WA births/year, ~14,400 Perth metro, ~277 GTT tests/week, ~100% universal screening, ~18% GDM diagnosis rate. Fixed in `feasibility.md` (§1.1 corrected, §1.4 catchment figure flagged as needing its own recalculation since it wasn't a simple substitution) and `business-plan.md` (§4 corrected to match). **Note:** `research.md` itself is explicitly out of scope for editing per the original task instruction (covers trust/ownership structure among other things, left untouched throughout this engagement) — its own capacity-vs-market comparison (§"GTT Center Perth Capacity vs Market," citing 30-40 bookings/week) also predates the current 10-client/50-per-week model, but this was not corrected since `research.md` is a protected file; flagged here for visibility only.

3. **A fifth AM-capacity-figure variant — RESOLVED.** `capacity-pricing-audit.md` (2026-06-11) referenced a "12-client/2-chair model" as its own headline finding. Traced the root cause: this model depends on a relaxed Draw 3 rule ("no upper bound on the final draw") that was not carried forward into subsequent scheduling documents — every verified scheduling document since (`operations-manual.md`, `scenario-c-sync-timetables.md`, `draw-event-scheduler-findings.md`, and this session's own `docs/scenario-e-floating-chair-investigation.md`) uses the bounded ±10min Draw 3 tolerance rule instead. The current standing capacity ceiling is confirmed as 10 clients/day (Scenario C, 2 chairs) or 15 clients/day (Scenario D, 3 chairs) — not 12. Fixed in `capacity-pricing-audit.md` (§1 flagged as superseded throughout).

**Recommended follow-up (not urgent, process improvement only):** consider a single "current operational model" pointer document (already suggested in `03_improvements.md` P1) so future model changes don't require this kind of multi-document reconciliation sweep again.

**CONFLICT-09 detail — RESOLVED 2026-07-20:** `onboarding.md`'s draft patient-facing confirmation email copy stated "full payment is required at time of booking. No deposit option." while `financial-setup.md` (Step 5, Payment flow table), `operations-manual.md` (Deposit Policy), `ivy-booking-system.md` (Step 6 Payment), and `website-spec.md` (Step 3) all described an A$30 deposit-at-booking + balance-on-day model. **Anthony confirmed the correct policy: full payment is collected at time of booking, no deposit** — `onboarding.md`'s draft copy was the one document that already had it right. Corrected the other four documents to match, and updated `docs/pricing-billing-strategy.md`'s own open-item note.

See `04_roadmap_next_steps.md` for prioritised follow-up actions on the items not fully resolved this session.
