# King Edward Hospital Guidance — GTT Must Start Before 10:00am

**Date:** 2026-07-17 | **Source:** General clinical guidance, source: internet research (clarified by Anthony 2026-07-19 — the "before 10am" claim originated from general internet research, not from a specific locatable KEMH document such as a referral form, fact sheet, or published patient guidance). This is not a case of a real document being unlocatable by search — there is no single specific document to find. Treat this as general clinical guidance rather than a formally sourced, citable constraint alongside ADIPS/RCPA-type references.

## Impact — checked against both current scenarios

**Scenario C (2 chairs, 10 clients, synchronized start): PASSES comfortably.** Last Draw 1 start is **09:40** — a full 20 minutes inside the "before 10:00" limit. This is a genuine bonus of the synchronized-start layout (both chairs finish their start-sequence together) versus the original staggered layout, whose last client started at 10:00 — right on the boundary, likely a violation under a strict reading of "before 10". **The synchronized model isn't just uniform, it's also safer against this constraint.**

**Scenario D (3 chairs, 15 clients): FAILS on a strict reading.** Last Draw 1 start is exactly **10:00** — not *before* 10:00. Two ways to fix this, no compromise needed on the finding itself:

| Fix | Effect | What it needs |
|---|---|---|
| **Shift the whole day ~20min earlier** (06:40 start instead of 07:00) | Last start moves to 09:40 — same as Scenario C, comfortably clears the limit, all 15 clients kept | Needs the already-open award early-start-penalty check (MA000005/MA000027 ordinary-hours span) — this was flagged as unresolved in `am-capacity-weekend.md` before this session, now becomes load-bearing rather than optional |
| **Drop to 14 clients** (remove the last slot) | No schedule change, no award risk | Reduces Scenario D's revenue/contribution — would need re-running the P&L in `scenario-d-investigation.md` |

**Recommendation: pursue the earlier-start fix first** — it preserves the full 15-client economics and only needs one already-outstanding verification (the award start-time check), not a new one.

## Standing note

This is now a second independent constraint on the AM window, alongside the (still unconfirmed) WDP courier cutoff — see `cutoff-time-CORRECTION.md`. The two are different in kind: WDP's is an end-of-day logistics constraint, King Edward's is a start-time clinical/best-practice guidance. Once both are sourced/confirmed, the real usable window is whichever is tighter.

---

## Changelog

**2026-07-19** — Reframed the sourcing status per Anthony's clarification: this is general clinical guidance from internet research, not an unlocatable specific document. Previous wording ("not yet independently verified... couldn't locate the specific document") implied a document exists somewhere and further searching might find it — that search is not a productive next step. If more certainty is wanted before relying on this for Scenario D planning, the path is a direct question to KEMH or a referring practice, not further web search.
