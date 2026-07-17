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
