# WDP Commercial Alignment Review — Client-Volume Mismatch

**Phase:** Commercial Assumption Alignment & External Readiness — documentation only. This document reviews the full WDP/Carole Rivers correspondence history, identifies exactly what has been communicated vs. what the current committed model requires, and drafts (but does not send) a clarification. **No communication is sent by this phase.** No startup cost assumption, financial model calculation, or revenue/cost methodology is touched.

**Date:** 2026-08-10
**Version used as source of truth:** commit `a2defba` (Canonical Startup Cost Adoption) and everything it built on.

**Source documents reviewed in full:** `docs/wdp-reply-carole-2026-07-30.md`, `docs/wdp-reply-carole-2026-08-03.md`, `docs/wdp-reply-carole-2026-08-07.md`, `docs/cutoff-time-CORRECTION.md`, `docs/lab-outreach-2026-07-28.md`, `docs/wdp-staffing-comparison-2026-07-28.md`, `docs/reed-partnerships.md`, `docs/VERIFICATION-TRACKER.md` items 1, 1b, 1c, 1d, 1d-be, 1j, 1k, 1l, 1m, 29, 29b, 29c, 29d, 30.

---

## 1. Exactly What WDP Has Been Told — Quoted, Not Paraphrased

Two emails to Carole Rivers (WDP, Customer & Commercial Manager, Country) are confirmed **SENT**. One further reply exists only as an unsent draft. Each is treated separately below — the send status of each is the single most important fact for this review.

### 1.1 SENT 2026-07-31 (`docs/wdp-reply-carole-2026-07-30.md`) — the volume-mismatch source

> "we're aiming to run at the maximum volume our two phlebotomist chairs can support within your 10:30am guidance — currently landing at **12 clients each morning, Monday to Saturday**, using a slightly extended operating morning to fit comfortably inside that window."

**This is the only place in any confirmed-sent WDP communication where a specific daily client volume is stated in the email body text.** It states 12 clients/day — Table 2, the SECONDARY reference model — not Table 1 (18 clients/day), the PRIMARY committed model since the 2026-08-05 rebase (`CLAUDE.md` standing fact, `docs/VERIFICATION-TRACKER.md` item 1m).

### 1.2 SENT 2026-08-07 (`docs/wdp-reply-carole-2026-08-07.md`) — no volume mentioned

This reply covers three topics only: the "remain in our waiting room" seated/no-walking question, the still-outstanding WDP-supplied staffing cost/term questions, and the site-assessment criteria (GPs/FTE doctors/referral volumes). **It does not restate, correct, or reference client volume anywhere.** The 12-client figure from the 2026-07-31 email was neither corrected nor reconfirmed here.

### 1.3 DRAFT, NEVER CONFIRMED SENT (`docs/wdp-reply-carole-2026-08-03.md`) — the correction that never went out

This draft's own changelog explicitly updated its framing to the two-table model: "the attached schedule reference updated from '12 and 14 clients a morning' to the two new start-time variants (07:00-start **18-client** table, 08:00-start **12-client** table, both 25-minute cadence)." The email body itself references an attachment ("GTT-Center-Perth-Clinic-Operations-Overview.html") showing "one table starting at 07:00 and one starting at 08:00" without restating the exact numbers in prose.

**Confirmed multiple times across this repo's own status tracking that this draft was never independently sent:** `docs/reed-partnerships.md`'s own tracker row states "`wdp-reply-carole-2026-08-03.md` remains DRAFT, NOT YET SENT — superseded in practice by the 08-07 reply, not independently actioned... no confirmation exists that it was ever sent independently." The document itself carries no "CONFIRMED SENT" changelog entry, unlike both the 07-31 and 08-07 replies, which each explicitly do.

**This is the central finding of this review: the correction that would have fixed the volume mismatch was drafted, but never sent.** WDP has never received, via any confirmed channel, a communication stating 18 clients/day as this venture's committed daily volume.

### 1.4 A genuine visibility gap — the attachment itself

`docs/VERIFICATION-TRACKER.md` item 1k references "the client-facing clinic-operations overview sent to Carole," built from the pre-rebase 12/14-client, 23-minute-cadence tables — implying an even earlier attachment, separate from the email body text, may have shown different (also-stale) numbers at some point. **The attachment file itself (`GTT-Center-Perth-Clinic-Operations-Overview.html`) does not exist anywhere in this repository** — confirmed by direct file search, zero results. This review cannot independently verify exactly what numbers any attachment actually showed Carole, only what the email body text itself states (quoted above). **Flagged as a genuine capability/visibility gap, not glossed over:** if an attachment was sent separately from the reviewed email bodies, its content is unknown to this repo and therefore to this review.

---

## 2. What the Current Model Actually Requires

Per the 2026-08-05 rebase (`CLAUDE.md` standing fact, `docs/CURRENT-STATE.md` §1): the **PRIMARY committed daily model is Table 1 — 18 clients/day, 07:00 start, 25-minute pair cadence.** Table 2 (12 clients/day, 08:00 start, same cadence) remains a **SECONDARY reference** — numerically identical to the pre-rebase committed model, still fully supported by the same staffing structure.

**One open nuance, not glossed over:** `docs/VERIFICATION-TRACKER.md` item 1m itself carries a "framing flag OPEN for Anthony to confirm/override" — Table 1 was adopted as the daily target because it strictly dominates Table 2 (same 8-staff + 2-phlebotomist headcount, materially higher revenue), but this repo's own tracker does not treat that adoption as a fully closed founder decision. Both scenarios remain live throughout the financial model (`data/models/master_financial_model.yml` explicitly treats neither as primary for modelling purposes). This review does not resolve that open question — it only establishes that 18/day is the current, standing-fact PRIMARY figure, and 12/day the standing SECONDARY one, which is the correct pairing for external communication regardless of which eventually becomes the sole committed target.

---

## 3. Whether WDP Pricing/Commercial Terms May Be Affected

**Yes — this is a real, not hypothetical, commercial risk.** Carole's own stated model (`docs/VERIFICATION-TRACKER.md` item 1c) is that WDP's annual rental arrangement for a venue-based collection clinic depends explicitly on **"expected pathology volume,"** among other factors. Since 18 clients/day is a 50% increase over the 12/day figure WDP has actually been told, any commercial figure WDP eventually quotes — the indicative rental range Carole is currently chasing with WDP's own State Business Manager (item 1c, actively progressing) — risks being calibrated against the wrong, lower volume. A quote genuinely appropriate for 12/day (less phlebotomist workload, potentially less courier/specimen-handling volume) could understate what WDP would actually charge for 18/day, requiring renegotiation once the correction is made — a real, avoidable friction point in an otherwise actively-progressing commercial conversation.

**One reassuring, already-consistent finding:** this venture's own internal break-even analysis (`docs/VERIFICATION-TRACKER.md` item 1d-be, "Break-even analysis, 2026-08-07 — what WDP-supplied rental figure would make it the cheaper option vs in-house, **at the committed 18-client model**?") was already computed against the correct, current 18-client Table 1 volume — the A$104,800–106,600/yr in-house break-even threshold that any future WDP quote should be compared against is already volume-correct. **Only the external communication to WDP itself is stale, not this venture's own internal analysis.**

---

## 4. Draft Clarification Substance — Not Sent, Not a Finished Email

Per instruction, this is the substance to communicate, not a ready-to-send email. If/when Anthony chooses to send a clarification, it should cover:

1. **State plainly that planning has moved to a higher committed volume since the 12-client figure was last mentioned.** Something to the effect of: "Since our last update, our planning has settled on 18 clients each weekday morning as our primary committed model (still Monday to Saturday, same two phlebotomist chairs, same 10:30am window) — a higher volume than the 12/day figure I mentioned earlier. We do also have a lower-volume version at 12/day as a fallback reference, but 18/day is what we're currently building toward."
2. **Ask explicitly whether this changes anything already discussed** — specifically, whether the indicative commercial range Carole is preparing (item 1c) should be scoped against 18/day rather than 12/day, and whether the operational logistics already discussed (courier/specimen handling, staff continuity, placement-model threshold — the three questions from the 07-31 email that remain unanswered, see item 1d/1c) are volume-sensitive in a way that needs revisiting.
3. **Do not withdraw or contradict anything already sent** — the 07-31 and 08-07 emails' other content (schedule structure, waiting-room/observation clarification, room-spec compliance) remains accurate and should not be re-litigated; only the volume figure itself needs correcting.
4. **Confirm what, if anything, was actually attached and sent** as part of the 08-03 draft or any earlier overview document — since this repo cannot independently verify attachment content (§1.4), Anthony is the only party who can confirm what Carole has actually seen visually, as distinct from what the email body text states.

---

## Validation — Confirmed No Model Changes Occurred

- `git status --short` before this phase: clean.
- Full pytest suite, canonical validator, and consistency checker results: see the combined validation summary in this phase's report-back (run once, covering all three deliverables of this phase).
- No canonical YAML, financial model, or revenue/cost methodology was touched by this document.
- No email or communication was sent by this phase — every quoted passage above is reproduced from already-existing, already-filed repository documents.
