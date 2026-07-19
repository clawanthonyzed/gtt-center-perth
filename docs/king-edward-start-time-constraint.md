# King Edward Hospital Guidance — GTT Must Start Before 10:00am

**Date:** 2026-07-17 | **Source:** General clinical guidance, source: internet research (clarified by Anthony 2026-07-19 — the "before 10am" claim originated from general internet research, not from a specific locatable KEMH document such as a referral form, fact sheet, or published patient guidance). This is not a case of a real document being unlocatable by search — there is no single specific document to find. Treat this as general clinical guidance rather than a formally sourced, citable constraint alongside ADIPS/RCPA-type references.

## Impact — checked against both current scenarios

**Scenario C (2 chairs, 10 clients, synchronized start): PASSES comfortably.** Last Draw 1 start is **09:40** — a full 20 minutes inside the "before 10:00" limit. This is a genuine bonus of the synchronized-start layout (both chairs finish their start-sequence together) versus the original staggered layout, whose last client started at 10:00 — right on the boundary, likely a violation under a strict reading of "before 10". **The synchronized model isn't just uniform, it's also safer against this constraint.**

**Scenario D (3 chairs, 15 clients): FAILS on a strict reading — but a third, better fix exists (verified 2026-07-19), see below.** Last Draw 1 start is exactly **10:00** — not *before* 10:00.

**RECOMMENDATION UPDATED 2026-07-19: shift only Client 15's start from 10:00 to 09:55 — verified workable, no whole-day shift or dropped client needed.** Anthony asked whether the 10:00 appointment (Client 15, Chair C) could start at 09:55 instead. This was verified by simulating the actual Chair C draw-event sequence (not eyeballing it) — see `am-capacity-weekend.md` "Can Client 15 Start at 09:55 Instead of 10:00?" for the full working. Result: the phlebotomist/chair side checks out with zero double-booking (the resulting zero-minute gap is structurally identical to two zero-gap handoffs the same timetable already contains elsewhere). **This clears the King Edward "before 10am" limit for all 15 clients without needing the whole-day shift or the dropped-client option below.**

**One caveat carried over from the verification:** the treatment-staff side of Client 15's shifted services could not be fully verified from existing documentation (no per-client staff-assignment table exists for Scenario D). Treat the 09:55 fix as verified on the phlebotomist/chair side and pending final confirmation on the treatment-staff side — see `am-capacity-weekend.md` for detail.

**Original two fixes, now superseded by the option above but retained for reference:**

| Fix | Effect | What it needs |
|---|---|---|
| ~~Shift the whole day ~20min earlier~~ (06:40 start instead of 07:00) | ~~Last start moves to 09:40 — same as Scenario C, comfortably clears the limit, all 15 clients kept~~ | **No longer the recommended path — the single-client 09:55 shift achieves the same result without moving the whole day or needing the award early-start-penalty check below** |
| ~~Drop to 14 clients~~ (remove the last slot) | ~~No schedule change, no award risk~~ | **No longer needed — the 09:55 fix keeps all 15 clients** |

**Updated recommendation: pursue the single-client 09:55 shift first** — it preserves the full 15-client economics, requires no whole-day timing change, and does not depend on the still-open award early-start-penalty question (MA000005/MA000027 ordinary-hours span at a 06:40 start) that the whole-day-shift option would have required. Close out the treatment-staff-side caveat above before treating this as fully final.

## Standing note

This is now a second independent constraint on the AM window, alongside the (still unconfirmed) WDP courier cutoff — see `cutoff-time-CORRECTION.md`. The two are different in kind: WDP's is an end-of-day logistics constraint, King Edward's is a start-time clinical/best-practice guidance. Once both are sourced/confirmed, the real usable window is whichever is tighter.

---

## Changelog

**2026-07-19** — Reframed the sourcing status per Anthony's clarification: this is general clinical guidance from internet research, not an unlocatable specific document. Previous wording ("not yet independently verified... couldn't locate the specific document") implied a document exists somewhere and further searching might find it — that search is not a productive next step. If more certainty is wanted before relying on this for Scenario D planning, the path is a direct question to KEMH or a referring practice, not further web search.

**2026-07-19 (Scenario D fix update)** — Updated the Scenario D recommendation: verified (via `am-capacity-weekend.md`) that shifting only Client 15's start from 10:00 to 09:55 clears the "before 10am" limit for all 15 clients, without needing the whole-day-shift or dropped-client options previously recommended. Phlebotomist/chair side verified; treatment-staff side flagged as an open caveat, not yet closed out.
