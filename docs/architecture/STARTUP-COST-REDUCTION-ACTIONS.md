# Startup Cost Reduction — Concrete Actions Only

**Date:** 2026-08-15 | **Status:** Execution list, not a new analysis.
**Purpose:** This document does not re-litigate `STARTUP-COST-OPTIMISATION.md` (Minimum Viable Opening scenario, A$243,912) or `MVP-OPENING-DECISION-REVIEW.md` (founder-approved A$251,198 planning figure, `docs/VERIFICATION-TRACKER.md` item 48, RESOLVED). Those documents already did the analysis. This document extracts only the concrete, actionable-now items from that existing work and from the still-open dependency (`docs/VERIFICATION-TRACKER.md` item 49), and prepares whatever can genuinely be prepared without a venue. **No new savings figure is invented anywhere below.**

---

## Action Table

| # | Action | Known financial impact | Dependency | Owner | Status |
|---|---|---|---|---|---|
| 1 | Get real insurance quotes (public liability, PI, workers' comp, property, business interruption) | Replaces the placeholder A$400/month modelled figure with a real number; itemised estimate range is A$975-1,583/month (`financial-setup.md` Step 8) — direction of change unknown until quoted | None — can happen now, no venue required for an indicative quote | Anthony (send) | **DO NOW — draft ready.** See `docs/insurance-broker-quote-request-draft.md` (Priority 3, this round). |
| 2 | Engage accountant for structure/GST/payroll-tax advice | No direct cost saving on its own, but blocks correct GST apportionment and entity-structure decisions that DO have real cost/tax consequences | None — can happen now | Anthony (send, pick a firm) | **DO NOW — draft ready.** See `docs/accountant-engagement-email-draft.md` (Priority 3, this round). |
| 3 | Call Fair Work Infoline re: MA000027 Saturday ordinary-hours question | **Upside-only.** If confirmed, reduces modelled Saturday phlebotomist labour cost below every current financial model's conservative full-penalty-rate assumption (`docs/hr-framework.md`) | None — can happen now | Anthony (call 13 13 94) | **DO NOW — script ready.** See `docs/fairwork-infoline-query-script.md` (Priority 3, this round). |
| 4 | Book a free WA Small Business Development Corporation (SBDC) advisory session | No direct dollar saving, but a free sanity check on the business plan/lease-readiness before paying a solicitor for the same review — genuinely reduces the risk of paying for advice a free session could catch first | None — can happen now, before a venue is shortlisted | Anthony (book) | **DO NOW — see Appendix A below for the concrete booking step.** |
| 5 | Request indicative pricing from AS 1530.2/3-compliant acoustic curtain suppliers | Firms up the acoustic-curtain-fabric line already funded in the adopted A$251,198 planning figure (+A$1,350, `MVP-OPENING-DECISION-REVIEW.md` §1) against a real supplier price instead of a market-research estimate | Partial — final linear-metre quantity needs confirmed room dimensions (item 49), but indicative per-linear-metre/per-panel pricing can be requested now | Anthony / Venue Manager (once hired) | **DO NOW (indicative only) — see Appendix B below.** |
| 6 | Get 3 real builder quotes for fit-out construction | The single largest cost category (A$139,678 in the adopted planning figure) — real quotes are the only way to close `VERIFICATION-TRACKER.md` item 49 | **BLOCKED — requires a confirmed venue and floor plate** | Anthony (venue search) | **WAIT FOR VENUE.** |
| 7 | Negotiate landlord fit-out contribution (A$20,000-60,000 potential offset, currently NOT netted into any headline figure per Anthony's own instruction) | Real, disclosed upside — `data/canonical/startup_costs.yml#startup_landlord_fitout_contribution` | **BLOCKED — requires a specific lease negotiation** | Anthony (lease negotiation) | **WAIT FOR VENUE.** |
| 8 | Confirm rent, bond, and landlord insurance/proof-of-funds requirements | Firms up Category A (A$19,000 in the adopted figure) against a real lease, not a benchmark | **BLOCKED — requires a shortlisted venue** | Anthony (property agent, once engaged) | **WAIT FOR VENUE.** |
| 9 | WDP collection-room spec sign-off before signing any lease | Could affect fit-out cost if a shortlisted venue needs adaptation to meet WDP's spec (`location-scouting.md`'s own rule: obtain spec BEFORE signing) | **BLOCKED — requires WDP's commercial terms and a shortlisted venue in parallel** | Reed / Anthony | **WAIT FOR WDP** (commercial figure actively progressing per Carole, `docs/reed-partnerships.md`) **and WAIT FOR VENUE** simultaneously. |
| 10 | Confirm FSS certificate renewal cadence (currently PLACEHOLDER — "renewal frequency not stated anywhere in this repo") | Small (A$100-200 range), but currently an unknown recurring-vs-one-off cost | None — a genuine research gap, not a founder decision | Whoever next has live web access to the relevant WA council/food-authority page | **OUTSOURCE** (needs a live web-fetch capability this session doesn't have — flagged, not guessed at). |
| 11 | Confirm whether AED leasing (A$40-60/month, the one leasing option found anywhere in this repo, `equipment-costs.md` §11) is genuinely cheaper than purchase over the relevant time horizon | Potentially defers a purchase cost to a smaller recurring opex line — direction and size not calculated here (would need a specific AED purchase quote to compare against) | None — can be researched now | Whoever next reviews `equipment-costs.md` | **DO NOW, low priority** — not actioned this round, flagged as a genuine open small-value item, not fabricated a number for. |

---

## Appendix A — WA SBDC Advisory Session (concrete booking step)

**What:** Free, government-funded business advisory session — business plan review, lease-obligation understanding, general startup guidance for WA small businesses.
**Where:** smallbusiness.wa.gov.au — the SBDC's own advisory service booking page.
**What to ask for:** a session covering (1) a general review of the current business-plan structure ahead of engaging a paid solicitor for lease review, and (2) general guidance on commercial lease obligations for a hybrid clinical/wellness premises, so the paid solicitor review (once a venue is shortlisted) is more efficient and targeted.
**Why now, not later:** this is free and general — it doesn't need a shortlisted venue the way the paid solicitor review does, and reviewing the business plan structure now (rather than after a lease is found) gives more time to act on any findings.
**Not sent/booked this round** — this is a booking action, not an email draft; the concrete next step is Anthony visiting the booking page directly.

---

## Appendix B — Acoustic Curtain Supplier Indicative-Pricing Request

**Status:** READY TO SEND, indicative-pricing-only — final order requires confirmed room dimensions (`docs/VERIFICATION-TRACKER.md` item 49).
**Suppliers identified** (per `docs/architecture/CURTAIN-COMPLIANCE-CLOSURE.md`, already researched and confirmed to sell AS 1530.2/3-compliant fabric with genuine acoustic performance): Imported Theatre Fabrics, Freedom's Halcyon range, Blinds Plus, Lifestyle Curtains, eSafety Supplies, Creative Systems.

**Draft enquiry:**

> Subject: Indicative pricing — AS 1530.2/3 fire-retardant, acoustic-rated curtain fabric and track
>
> Hi [Supplier name],
>
> I'm planning a small commercial fit-out in Perth (4 curtain-partitioned treatment rooms, each approximately 11-12sqm, using floor-to-ceiling curtain partitions rather than fixed walls) and I'm looking for fabric that meets AS 1530.2/AS 1530.3 fire-retardancy requirements and also offers genuine sound-absorbing/acoustic performance, not just fire compliance.
>
> At this stage I don't have final room dimensions confirmed (a lease is not yet signed), so I'd appreciate:
>
> - Indicative pricing per linear metre or per panel for your acoustic/fire-rated range
> - Confirmation of current AS 1530.2/1530.3 test certification for the products you'd recommend
> - Lead time from order to delivery
> - Whether curtain track/hardware is quoted separately or bundled
>
> I'll follow up with exact quantities once a venue is confirmed. This is a planning-stage enquiry.
>
> Regards,
> Anthony Zed

**Design notes:** no venue name, no opening date, consistent with this repo's standing outreach convention. Explicitly frames as planning-stage/indicative, since final quantities depend on the still-open venue dependency (item 49) — sending this now gets a real per-unit price range into the planning figure without waiting for a lease.

**Sending status:** Not sent. Six candidate suppliers identified — Anthony to choose which to approach first (or approach multiple in parallel for competitive pricing).

---

## What This Document Deliberately Does Not Do

- Does not recalculate the A$251,198 adopted planning figure, or any component of it.
- Does not invent a new savings estimate for any item — every dollar figure above is quoted directly from an existing canonical or architecture document, not recomputed.
- Does not attempt items 6-9 above (builder quotes, landlord negotiation, rent/bond confirmation, WDP spec sign-off) — all four are genuinely blocked on a confirmed venue or WDP's commercial terms, both explicitly outside this agent's authority per this round's own instruction (no property research, no WDP rework while Carole is awaited).

---

## Changelog

**2026-08-15** — Created as the concrete-actions-only companion to `STARTUP-COST-OPTIMISATION.md` and `MVP-OPENING-DECISION-REVIEW.md` (both unchanged, not re-analysed). Priority 4, external execution round. Cross-references the three Priority 3 outreach drafts (insurance, accountant, Fair Work) rather than duplicating them, and prepares one new supplier-pricing enquiry (Appendix B) plus one booking action (Appendix A).
