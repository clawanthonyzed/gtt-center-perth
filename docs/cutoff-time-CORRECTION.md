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

## Update (2026-07-29) — Carole Rivers Verbally Confirmed No Cutoff Within Operating Hours — NOT Yet in Writing

**Carole Rivers (WDP, Customer & Commercial Manager, Country) verbally confirmed there is no specimen-pickup cutoff within business operating hours.** This directly answers the standing 11:30-vs-12:30 question — but it is a **verbal confirmation only**, not yet in writing/email.

`[VERIFIED — Carole Rivers, WDP, verbal confirmation, 2026-07-29]`

**This is real and should be relied on for planning purposes — it is not the same status as the two previously-unconfirmed 11:30/12:30 figures, which had no source at all.** But it is **not fully closed out** either: a verbal confirmation from one contact is a real but weaker form of evidence than a written reply, and this repo's own standing instruction (above, 2026-07-17) explicitly required documenting anything short of an actual WDP reply as unconfirmed. Treating this as identically strong as a written confirmation would repeat the same class of error this file was created to catch.

**Standing action item — do not close until done:** get this specific confirmation ("no specimen-pickup cutoff within business operating hours") in writing/email from WDP, for the permanent record. Anthony has an existing draft reply in progress to WDP (see the 2026-07-28 update above) — this confirmation should be explicitly referenced/requested in that reply, or in a short separate follow-up, so there is a written record to point to rather than relying on a verbal exchange indefinitely. Added to `docs/VERIFICATION-TRACKER.md` item 1 and `docs/CURRENT-STATE.md` §1.

**Practical effect on the AM/PM capacity model (Scenario C/D):** if no cutoff exists within operating hours, the courier-cutoff constraint that has driven the AM window's end-time ceiling in every scheduling document to date (`scenario-c-sync-timetables.md`, `am-capacity-weekend.md`, `draw-event-scheduler-findings.md`) may no longer be the binding constraint — this could open room for later start times or a wider window than currently modelled. **Not yet actioned in any scheduling document** — the verbal-only status means this should be treated as directionally encouraging, not yet a basis for re-running the capacity model. Re-verify once the written confirmation exists, then update the schedulers.
