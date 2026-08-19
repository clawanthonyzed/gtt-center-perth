# AM→PM Data Capture Specification

**Status:** Current, name-agnostic. Companion to `RETURN-LOOP.md` and `CUSTOMER-JOURNEY.md` (this document's entire reason to exist is to eventually measure whether the loop those two documents describe is actually working) and `docs/ivy-booking-system.md` (the booking-system evaluation this spec extends, not replaces).
**Purpose:** `RETURN-LOOP.md` makes the strategic case that converting one-off AM/GTT guests into self-directed, repeat PM guests is this venture's highest-leverage growth mechanism, since AM volume is capped by referral behaviour the business doesn't control while PM demand is not. That argument is currently unmeasurable — no field, tag, or report anywhere in this repo's booking-system design captures whether it's actually happening. This specification defines exactly what data needs to be captured, where, and by whom, so the loop can eventually be measured rather than assumed.

**What this document is not:** it does not change the booking flow, pricing, or operating model. It does not require new software — every field below is either a native Fresha field, a Fresha custom field, or a manual log a receptionist/Venue Manager can keep with no new tooling. It is a data-architecture addition to the existing `ivy-booking-system.md` spec, not a rebuild of it.

---

## 1. The Three Questions This Spec Exists to Answer

Per the prior audit round's own framing, restated here as the concrete measurement targets:

1. **Which AM service (if any) preceded a given PM booking?** — tests whether trying a wellness service during the AM visit (Massage/Nails/Hair/Brows, alongside the GTT draw) makes a guest more likely to book that same category again standalone, or whether PM bookings mostly come from guests who had no wellness service at all during their AM visit.
2. **Time-to-first-booking** — the gap between a guest's AM/GTT visit date and her first self-directed PM booking date (if any). A short gap suggests the departure/follow-up mechanism (`RETURN-LOOP.md`'s Experience→Discovery→Follow-up→Visit 2 stages) is working; a long gap or no PM booking at all suggests it isn't.
3. **Second-booking rate** — of all AM/GTT guests, what percentage ever make a second booking of any kind (PM standalone, or a later pregnancy's AM visit)? This is the single top-line number that tells the business whether the loop is real or aspirational.

---

## 2. What Needs To Be Captured, By Stage

Mapped directly to `CUSTOMER-JOURNEY.md`'s stages and `RETURN-LOOP.md`'s six-stage loop — no new stage invented, only the data layer added underneath the existing experience design.

### 2.1 At AM/GTT Booking (Visit 1)

| Field | Type | Purpose | Where it lives |
|---|---|---|---|
| Client record (name, mobile, email) | Native Fresha client field | Already captured per `ivy-booking-system.md` Step 5 | Fresha |
| Referral source | Native Fresha field ("how did you hear about us?") | Already specified in `ivy-booking-system.md` Step 5 — links AM acquisition channel to eventual PM conversion, not just to AM booking volume | Fresha |
| Due date / pregnancy stage | Native Fresha field | Already captured — also lets a later report distinguish "second AM visit, same or later pregnancy" from "first PM standalone booking," which are different loop outcomes | Fresha |
| **Visit type tag: "AM-GTT-Visit-1"** | **NEW — Fresha client tag** | Marks this client's first-ever AM visit, distinct from any repeat AM or PM visit later. Without this, a client's Nth visit looks identical to her 1st in any later report. | Fresha (client tag) |
| AM wellness service booked alongside GTT (if any): Massage / Nails / Hair / Brows / None | Derived from the booked service line items already in Fresha (Step 3 of `ivy-booking-system.md`) — no new field needed, just needs to be reportable, see §3 | Fresha (existing service line) |

### 2.2 At Departure (per `CUSTOMER-JOURNEY.md`'s "Departure Experience" stage — the specific gift/parcel mechanism previously described in that stage is REMOVED, not approved; the PM-mention data capture below is unaffected, since it tracks a verbal mention only, not any physical item)

| Field | Type | Purpose | Where it lives |
|---|---|---|---|
| PM mention delivered: Yes/No | **NEW — manual checkbox on the daily roster sheet the Venue Manager already distributes** (per `ivy-booking-system.md`'s Staff Management section — no new system, just a column added to the existing printed/shared roster) | Confirms the Discovery-stage mechanism (`RETURN-LOOP.md` Experience→Discovery) actually happened for this guest, not assumed | Manual roster sheet, transcribed to Fresha notes weekly by the Venue Manager |
| Specific PM category mentioned (if any) | Free-text note on the same sheet | Lets a later report test whether guests who were told about a *specific* category ("you might like a facial next time") convert at a different rate than a generic mention — directly tests `RETURN-LOOP.md`'s own claim that specificity outperforms genericness | Manual roster sheet → Fresha client notes |

### 2.3 At Follow-Up (per `RETURN-LOOP.md`'s Discovery→Follow-up stage)

| Field | Type | Purpose | Where it lives |
|---|---|---|---|
| Follow-up message sent date | **NEW — Fresha automated-message log** (Fresha logs sent SMS/email automatically; this is a reporting requirement, not a new send) | Establishes the actual date the "genuinely useful" results-timing message went out, so time-to-first-booking (§1, Question 2) can be measured from a real anchor date, not the visit date alone | Fresha (message log, already exists — needs to be included in the weekly report, see §3) |
| PM mention included in follow-up: Yes/No | Confirmed by the message template used (a single approved template, not client-by-client customisation) | Same measurement purpose as §2.2 — confirms the mechanism fired | Fresha (message template ID) |

### 2.4 At Any PM Booking (Visit 2+)

| Field | Type | Purpose | Where it lives |
|---|---|---|---|
| **Visit type tag: "PM-Standalone" or "AM-Repeat"** | **NEW — Fresha client tag, applied at booking** | Distinguishes a self-directed PM wellness booking from a second AM/GTT visit (a later pregnancy) — both are loop success, but they're different outcomes and should be reportable separately | Fresha (client tag) |
| Prior AM visit date (if any) | Looked up from the existing client record (already in Fresha, since the same client profile persists across visits) — no new field, just a lookup | This is the raw material for time-to-first-booking (§1, Question 2) | Fresha (existing client history) |
| Booking channel for this PM visit (self-booked online / phoned in / walk-in) | **NEW — Fresha field, if not already default-captured** | Tests whether AM guests convert via the same self-service flow PM-first guests use, or need more hand-holding | Fresha |

---

## 3. Reporting — What Gets Produced, How Often, By Whom

This is the piece that closes the loop between "data is captured" and "someone can actually answer the three questions in §1." Per `financial-setup.md`'s existing reporting rhythm (Bruno owns the Friday weekly P&L), this reuses the same cadence rather than inventing a new one.

| Report | Frequency | Owner | Method |
|---|---|---|---|
| AM Visit-1 cohort list (every guest tagged "AM-GTT-Visit-1" this week) | Weekly | Venue Manager | Fresha client list, filtered by tag, exported |
| PM conversion check (of guests tagged "AM-GTT-Visit-1" more than 30 days ago, how many now also carry a "PM-Standalone" or "AM-Repeat" tag) | Monthly, once enough visit-1 history exists (not meaningful in Month 1) | Venue Manager, reviewed by Bruno alongside the monthly management accounts | Fresha client list, cross-referenced by tag and visit date |
| Second-booking rate (top-line %, per §1 Question 3) | Monthly, same cadence as above | Venue Manager → Anthony | Simple ratio: (clients with 2+ tagged visits) / (all clients tagged "AM-GTT-Visit-1" more than 60 days ago, to give a fair conversion window) |
| AM-service-to-PM-category correlation (§1 Question 1) | Quarterly, once volume is large enough to be meaningful (not a Month 1-3 report) | Venue Manager, or Bruno if a simple spreadsheet cross-tab is easier than a Fresha report | Manual cross-tab: AM wellness service booked (§2.1) vs. first PM category booked (§2.4) |

**Why quarterly, not monthly, for the AM-service-to-PM-category correlation specifically:** at Month 1-4 volumes (per `docs/architecture/AM-STAFFING-RAMP-OPTIMISATION.md`'s own 190-221 AM clients/month figure), a monthly cross-tab across 4 AM service categories and 4+ PM categories would have too few data points per cell to mean anything — this is a genuine statistical-power judgment, not an arbitrary delay.

---

## 4. What This Spec Deliberately Does Not Require

- **No new software purchase.** Every field above is either a native Fresha field, a Fresha custom tag (Fresha supports client tagging natively), or a manual note on the roster sheet the Venue Manager already produces daily per `ivy-booking-system.md`'s Staff Management section.
- **No change to the booking flow itself.** The 11-step flow in `ivy-booking-system.md` §4 is unchanged — this spec only asks that two tags be applied at the points that flow already passes through (booking, and any later booking).
- **No client-facing change.** None of this data capture is visible to the guest — it does not add a question to her booking form, a step to her visit, or a line to her follow-up message beyond what `RETURN-LOOP.md` already specifies should be there for experience reasons.

---

## 5. Implementation Sequencing (Not Yet Actioned — Depends on the Venue Manager Being Hired)

1. **Before opening:** Venue Manager (once hired) sets up the two Fresha client tags ("AM-GTT-Visit-1" / "PM-Standalone" / "AM-Repeat") and confirms whether Fresha's client-tag filtering supports the export needed for §3's weekly/monthly reports (a genuine platform-capability check, not assumed — `ivy-booking-system.md` itself already flags that Fresha "is not designed for medical/clinical workflows" and needed a workaround for GTT pairing; the same caution applies here, this has not been verified against Fresha's actual current tag-reporting feature set).
2. **Week 1 of trading:** roster sheet gets the "PM mention delivered" column added (§2.2) — a one-line change to an existing document, not a new system.
3. **Month 2 onward:** first meaningful weekly/monthly reports become possible once enough Visit-1 history exists to report on.
4. **Quarter 2 onward:** first meaningful AM-service-to-PM-category correlation report becomes possible, per the statistical-power reasoning in §3.

---

## 6. Open Item, Flagged Not Guessed At

Whether Fresha's actual tag-filtering and export functionality supports the exact reports in §3 as described has not been verified against Fresha's live product — this session has no Fresha account access to confirm directly. `ivy-booking-system.md`'s own established practice (documenting the GTT-pairing workaround as a "not natively supported, needs configuration" gap) is the model followed here: this spec is written as the target design, with the Fresha-capability confirmation step explicitly listed in §5 item 1 as unverified, not assumed to work exactly as described.

---

## Changelog

**2026-08-15** — Created as the AM→PM data-capture specification identified as a gap in the prior audit round. Grounds every field in the existing `RETURN-LOOP.md`/`CUSTOMER-JOURNEY.md` experience design and `ivy-booking-system.md`'s existing Fresha/roster-sheet architecture — no new operating-model assumption introduced. Priority 5, external execution round.
