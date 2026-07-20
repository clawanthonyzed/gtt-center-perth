# PathWest GTT Patient Instructions — Start Time and Fasting Requirements

**Date:** 2026-07-20 (rewritten with real source — see changelog)
**Source: SOURCED, OFFICIAL, CITABLE.** Two official PathWest patient instruction documents, one hosted on King Edward Memorial Hospital's own site:

- **PathWest Patient Instructions — GTT, January 2019** (hosted on KEMH's site): https://www.kemh.health.wa.gov.au/~/media/PathWest/Documents/For-Patients/Patient-Instructions---GTT-January-2019.pdf — direct quote: *"The test should be performed in the morning, preferably started before 10.00am (particularly if you are pregnant)."*
- **PathWest Patient Instructions — GTT, 2024** (current version): https://www.pathwest.health.wa.gov.au/~/media/PathWest/Documents/For-Patients/Patient-Testing-Instructions-2024/Patient-Instructions---GTT.pdf

**This replaces the previous "general clinical guidance, source: internet research" framing — this is now a real, citable source, not an unattributed claim.**

---

## What the Sourced Documents Actually Say

**Start time (2019 document only — the "before 10am" line does not appear in the 2024 version, cite the 2019 document specifically for this claim):**
> "The test should be performed in the morning, preferably started before 10.00am (particularly if you are pregnant)."

**Important nuance — this is guidance, not an absolute mandate.** The word "preferably" matters: this is a best-practice recommendation from the pathology provider, not a hard clinical cutoff with a stated consequence for missing it (unlike, for example, a specific fasting-window requirement with a defined validity boundary). Do not upgrade this to "must" language in any patient-facing or planning material — "preferably before 10am" is the accurate framing.

**Fasting window — the two documents differ slightly, use 2024 as primary:**

| | 2019 document | 2024 document (current, use as primary) |
|---|---|---|
| Minimum fast | 10 hours | 10 hours |
| Maximum fast | 16 hours | 12 hours |
| Total procedure time | ~3 hours | 2-3 hours |

**Where the two conflict (fasting maximum: 16hrs vs 12hrs, procedure length: ~3hrs vs 2-3hrs), the 2024 document is more recent and should be treated as the current standard** — but note both are official PathWest documents, so if a specific patient's timing falls between 12 and 16 hours fasted, this is worth a direct confirmation with the pathology partner rather than assuming either figure is definitively wrong.

---

## Impact — checked against both current scenarios (unchanged from previous analysis, now on a sourced basis)

**Scenario C (2 chairs, 10 clients, synchronized start): PASSES comfortably.** Last Draw 1 start is **09:40** — a full 20 minutes inside the "before 10:00" guidance. This is a genuine bonus of the synchronized-start layout (both chairs finish their start-sequence together) versus the original staggered layout, whose last client started at 10:00 — right on the boundary, likely a violation under a strict reading of "before 10". **The synchronized model isn't just uniform, it's also safer against this guidance.**

**Scenario D (3 chairs, 15 clients): FAILS on a strict reading — but a fix exists (verified 2026-07-19), see below.** Last Draw 1 start is exactly **10:00** — not *before* 10:00, on a strict reading of the guidance.

**RECOMMENDATION (verified 2026-07-19): shift only Client 15's start from 10:00 to 09:55 — verified workable, no whole-day shift or dropped client needed.** This was verified by simulating the actual Chair C draw-event sequence (not eyeballing it) — see `am-capacity-weekend.md` "Can Client 15 Start at 09:55 Instead of 10:00?" for the full working. Result: the phlebotomist/chair side checks out with zero double-booking. **This clears the "preferably before 10am" guidance for all 15 clients without needing a whole-day shift or a dropped client.**

**One caveat carried over from the verification:** the treatment-staff side of Client 15's shifted services could not be fully verified from existing documentation (no per-client staff-assignment table exists for Scenario D). Treat the 09:55 fix as verified on the phlebotomist/chair side and pending final confirmation on the treatment-staff side — see `am-capacity-weekend.md` for detail.

---

## Standing note

This is now a second independent constraint on the AM window, alongside the (still unconfirmed) WDP courier cutoff — see `cutoff-time-CORRECTION.md`. The two are different in kind: WDP's is an end-of-day logistics constraint (still unsourced, awaiting a direct reply), King Edward/PathWest's is a start-time guidance (now sourced, but framed as "preferably," not absolute). Once both are fully confirmed, the real usable window is whichever is tighter.

---

## Changelog

**2026-07-19** — Reframed the sourcing status per Anthony's clarification: this is general clinical guidance from internet research, not an unlocatable specific document.

**2026-07-19 (Scenario D fix update)** — Updated the Scenario D recommendation: verified that shifting only Client 15's start from 10:00 to 09:55 clears the guidance for all 15 clients, without needing a whole-day shift or dropped client.

**2026-07-20 (real source found — full rewrite)** — Anthony found and provided the actual official PathWest patient instructions PDF (2019 version, hosted on KEMH's own site), which contains the exact "preferably started before 10.00am (particularly if you are pregnant)" quote. This is a real, citable, official source — not general internet research as previously framed. Also incorporated the 2024 current version's fasting-window figures (10-12hrs, vs the 2019 document's 10-16hrs) as the primary current reference, noting the discrepancy rather than silently picking one. Retitled the document from "King Edward Hospital Guidance" to "PathWest GTT Patient Instructions" since PathWest, not KEMH itself, is the author of the guidance (KEMH merely hosts a copy of the 2019 PDF). Updated `docs/05_open_questions_for_founder.md` Q3 to reflect this is now resolved/sourced, not just clarified — see that document.
