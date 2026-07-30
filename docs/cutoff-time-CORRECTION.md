# CORRECTION — WDP Cutoff Time Was Never Confirmed (2026-07-17)

**Anthony's direct statement, on record:** *"I have not had a reply from WDP so they have not told me 12:30."* Confirmed correct — checked the actual document trail below.

## What actually happened

The 12:30 figure has been used throughout `am-capacity-weekend.md`, `pathology-partnership-brief.md`, and every timetable/scheduler built this session as if it were a known constraint. It was not. Tracing it back:

- `am-capacity-weekend.md` repeatedly calls it "the WDP courier cutoff," each time also noting it "should still be confirmed directly with WDP" — the hedge was always there in the small print, but the number was used as the working figure regardless.
- `gtt-clinical-protocol.md` (a different, earlier document) states a **different** number for the same thing: *"Dispatch to lab at agreed time (latest: 11:30am daily — confirm with WDP)."*

**Two different unconfirmed numbers exist in the documentation (11:30 and 12:30), neither sourced from an actual WDP reply.** That inconsistency is itself proof nobody had it confirmed — if it had been, both documents would agree. The 12:30 figure most likely originated as a *designed target* (07:00 start + ~5.5hr AM window = 12:30) rather than something WDP told anyone.

## What this session found from public sources

Searched for a publicly-documented specimen transport time limit (ACSQHC/RCPA/NPAAC collection centre standards) that might independently establish a real cutoff without needing WDP's answer. Found the relevant primary documents but could not retrieve their full content (two direct fetch attempts failed — connection reset, then timeout — flagging that plainly rather than guessing at their contents).

What general chemistry sources did confirm: fluoride-oxalate (glucose) tubes are stable for hours — glycolysis inhibition holds for ~4 hours, then the sample is stable for 72 hours at room temperature. **There's no chemical reason forcing an early same-day cutoff.** This points toward 12:30 (or 11:30) being **WDP's own courier/logistics schedule — an operational, negotiable number — not a clinical or regulatory mandate.** Useful context for the WDP conversation: there's no evidence the cutoff can't move later if their courier schedule allows it.

## Standing instruction from here

- **Every document and every scheduler output that cites a specimen cutoff must say "ASSUMED / UNCONFIRMED — pending WDP reply," not state it as fact.** This includes `am-capacity-weekend.md`'s existing "12:30 WDP courier cutoff" references and the visual timelines built this session (`scenario-c-timeline.html`, `scenario-c-sync-timeline.html`) — several of these state it without the caveat and should be treated as provisional, not corrected retroactively.
- **Scenario D's hiring case (`scenario-d-investigation.md`) is entirely provisional on this number** — do not treat the P&L or staff timetable in that document as final until WDP actually replies.
- Once WDP responds with a real number, every scheduler built this session (`draw-event-scheduler.py`, `sync-treatment-solver.py`, `scenario-d-staffing.py`) takes it as a single parameter and recomputes instantly — no manual rebuild needed.

---

## Update (2026-07-28) — WDP Replied, Active Conversation

**WDP has replied as of 2026-07-28** — Carole Rivers (Customer & Commercial Manager, Country) confirmed courier/GTT collection is feasible with the correct specimen tubes, and asked for more detail on the venture's vision plus a discussion of on-site pathology staff presence. **The specific 11:30 vs 12:30 cutoff-time question has NOT yet been directly answered in what's been relayed — still open**, to be raised in Anthony's next reply (he has a draft ready to send himself). PathWest and Clinipath were emailed 2026-07-27, still awaiting reply — see `docs/05_open_questions_for_founder.md` Q6 and `lab-outreach-2026-07-28.md`.

**When the cutoff-specific exchange happens, Anthony will ask two questions:**
1. The actual specimen dispatch cutoff time (resolves the 11:30 vs 12:30 conflict directly).
2. **Whether overnight blood storage + next-day lab collection is viable** as an alternative model to the same-day courier-cutoff constraint.

**Question 2 is not answered here and should not be speculated on** — it depends entirely on WDP's clinical/logistics answer (specimen stability under their actual storage conditions, their lab's next-day intake process, and whether this fits their Licensed Collection Centre QMS). If viable, it could materially change the AM window's end-time constraint that currently drives the whole Scenario C/D capacity ceiling — but that's WDP's determination to make, not an assumption to build into any document ahead of their reply. Once received, update this file and `docs/05_open_questions_for_founder.md` with the actual answer(s) before they feed into any capacity/scheduling document.

**2026-07-27 correction note (retained for trace):** the heading and body previously said "WDP Emailed" — corrected to reflect the actual channel used (online enquiry form). PathWest/Clinipath both emailed 2026-07-27.

**2026-07-28 update:** WDP's reply logged above — this section corrected from "awaiting reply" framing to reflect the active conversation.

---

## Update (2026-07-29) — Carole Rivers Verbally Confirmed No Cutoff Within Operating Hours — SUPERSEDED 2026-07-30, see below

~~Carole Rivers (WDP, Customer & Commercial Manager, Country) verbally confirmed there is no specimen-pickup cutoff within business operating hours.~~ **This 2026-07-29 verbal readback was an oversimplification, corrected 2026-07-30 by Carole's actual written email — see below. It was never a blanket "no cutoff," and should not have been summarised that way even as a verbal-only status.** Retained here (struck through) for trace, not deleted.

---

## Update (2026-07-30) — Carole Rivers' Actual Email Reply — Real, Written, More Nuanced Than the Verbal Readback

Carole Rivers' actual email (pasted directly by Anthony in chat — genuine written correspondence, not from an attached doc) gives a real but **conditional**, not unconditional, answer:

- Overnight storage is viable **"in some circumstances"** — fluoride oxalate tubes (the type used for GTT glucose specimens) are stable for approximately 24 hours.
- **"A late booking would not necessarily prevent collection, although specimen type and storage requirements would always need to be considered."**

`[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]`

**This is NOT the same as "no cutoff within business hours."** The 2026-07-29 verbal readback (struck through above) oversimplified a conditional, case-by-case answer into a blanket confirmation — exactly the kind of overstatement this repo's own standing instruction (2026-07-17, above) exists to prevent. The real answer is: **a late booking is not automatically rejected, and overnight storage is a genuine option in at least some circumstances** — but whether a specific late booking can actually be accommodated depends on the specimen type and storage conditions being right for that day, not a standing, unconditional guarantee that any time works.

**This is now written, primary-source correspondence — a stronger evidentiary status than the 2026-07-29 verbal-only confirmation.** No further "get it in writing" action item is needed for this specific point (the original 11:30-vs-12:30 question is answered — there isn't a single fixed cutoff, there's a conditional, circumstance-dependent answer instead). What remains open: the exact conditions (which specimen handling/storage setup on GTT Center Perth's side would need to be in place to reliably use the overnight-storage option) are not yet spelled out — see `docs/VERIFICATION-TRACKER.md` for this as a still-open follow-up question, distinct from the now-answered "is there a hard cutoff" question.

**Practical effect on the AM/PM capacity model (Scenario C/D):** the courier-cutoff constraint that has driven the AM window's end-time ceiling in every scheduling document to date (`scenario-c-sync-timetables.md`, `am-capacity-weekend.md`, `draw-event-scheduler-findings.md`) is confirmed **not to be a hard, unconditional wall** — there is real flexibility (overnight storage in some circumstances, late bookings not automatically rejected). **Still not yet actioned into any scheduling document** — this is a real, written, more-favourable answer than previously assumed, but "in some circumstances" and "would always need to be considered" mean the exact operational conditions need to be nailed down with WDP (what storage setup, what specimen handling) before re-running the capacity model on the assumption that the window can simply be widened. Treat as a genuine, sourced upside for a future capacity review, not yet a basis for changing today's Scenario C/D figures.

## New Information — WDP Commercial/Rental Structure (2026-07-30)

Carole's email also describes WDP's model for a venue-based collection clinic: **an annual rental arrangement**, with terms depending on expected pathology volume, number of referring doctors on-site, location/accessibility, and the overall business opportunity. **No figure is quantified anywhere in this correspondence.** Added as a new tracked item in `docs/VERIFICATION-TRACKER.md` (owner: Anthony/WDP commercial negotiation) — do not invent a rental estimate anywhere in this repo until a real figure exists.

## Critical Open Question — Phlebotomist Employment Model (2026-07-30, NOT DECIDED)

Carole's email states that under this rental model, WDP staff's **"safety, wellbeing and employment responsibilities... would remain with Western Diagnostic Pathology."** This raises a real, high-priority, unresolved question: does GTT Center Perth still employ its own phlebotomist(s) directly (the current modelled assumption — AM Direct Labor stays at ~A$48,255/month per `docs/CURRENT-STATE.md`), or does WDP supply/employ the phlebotomist as part of the rental deal (which would replace that wage line with a to-be-negotiated rental fee instead)?

**Anthony's explicit answer: NOT DECIDED — ask Carole to clarify directly before assuming either way.** `[PLACEHOLDER — critical dependency, not yet resolved]`. **Do not change the AM Direct Labor cost line in any P&L document over this** — the current figure (in-house employment assumption) stays as the modelled baseline until this is actually answered. See `docs/CURRENT-STATE.md` §4 and §7 for the prominent flag on this dependency, and `docs/VERIFICATION-TRACKER.md` for the high-priority tracked item.
