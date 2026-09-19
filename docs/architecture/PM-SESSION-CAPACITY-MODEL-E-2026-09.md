# PM Session Capacity — Model E (Session-Count Method), Locked at 10 Sessions/Day

**Date:** 2026-09-19 | **Purpose:** Resolve PM package session-consumption "properly this time, not as an open caveat," per Anthony's direct instruction, and recompute PM revenue/labour at his directly-specified planning input of exactly 10 PM sessions/day (was 16). Supersedes `docs/architecture/PM-CAPACITY-RECONCILIATION.md`'s Model C (staff-minutes method) for revenue purposes — Model C's own staffing research (which package needs how many specialists) is NOT re-litigated, only the counting method built on top of it changes.

---

## 1. Why Model C Is Replaced, Not Just Rescaled

Model C (2026-08-18) converted PM capacity into client transactions using a **minutes-weighted-average** method: total staff-minutes ÷ weighted average minutes-per-transaction. That method is mathematically sound but does not match Anthony's own framing of the fix he wants: *"a package that takes 2 sessions must be counted as 2 sessions, not 1, when computing capacity and revenue."* That is a literal **session-count** rule, not a minutes-weighted one. Model E below implements the literal rule.

A genuine, disclosed finding from testing Model C's own formula at the new 10-session target first: because the 3-hour casual-minimum-engagement floor already dominated PM labour costing at 16 sessions/day (3.08hrs/role, barely above the 3.0hr floor), simply lowering the "sessions" input to 10 inside Model C's own minutes-based formula produces a transaction capacity (12.48/day) that is *barely lower* than the old 12.8128/day figure — because the floor absorbs almost all of the reduction on the labour side, and the minutes-weighted revenue conversion doesn't cleanly reflect a directly-specified session cap. This is not a defensible way to honour a direct "10 sessions" instruction. Model E (below) instead treats 10 as the literal session-capacity ceiling and works out transaction capacity from the actual session cost of each transaction type.

---

## 2. Model E — The Method

**A "session" is one treatment-staff appointment-slot.** Total daily PM session capacity is a directly-specified planning input (Anthony's instruction: 10/day weekday). Each transaction type consumes a whole number of sessions, using the SAME staffing-pattern research already established and not reopened here (`docs/architecture/PM-CAPACITY-RECONCILIATION.md` §2):

| Transaction type | Sessions consumed | Why |
|---|---|---|
| Individual a-la-carte | 1 | One therapist, one continuous booking |
| PM Refresh (Massage 45min + Mini facial 30min) | 1 | ONE dual-qualified Massage+Beauty-pool therapist delivers both components sequentially — the venue's own established common-pool design, not two people |
| PM Restore (Gel manicure 45min + Blow-dry 30min) | 2 | TWO different specialists (Nail Technician + Hairdresser) — no confirmed dual Nails+Hair qualification anywhere in this repo |

Using the same disclosed 60% individual / 25% Refresh / 15% Restore transaction-mix assumption (`docs/architecture/PM-PACKAGES.md` §5, unchanged — still a planning estimate, not real booking data):

**Weighted sessions/transaction** = 0.60(1) + 0.25(1) + 0.15(2) = **1.15**

**Weekday transaction capacity** = 10 sessions ÷ 1.15 = **8.6957 transactions/day** (was 12.8128 under Model C, a genuine 32.1% reduction — a direct, disclosed consequence of the lower session target, not an error).

**Saturday:** preserved at the existing 50%-of-weekday convention (5 sessions, half of the new weekday 10) — same reasoning as Model C: Saturday's own PAID labour hours are already floor-inflated and are not evidence that Saturday demand doubles. Saturday transaction capacity = 8.6957 × 0.5 = **4.3478 transactions/day** (was 6.4064).

---

## 3. Revenue

Using the same, unaffected blended average transaction value (A$116.97 ≈ A$117, `data/canonical/pricing.yml#pm_alacarte_average` — the 60/25/15 mix % is unchanged, only the total transaction count changes):

| | Transactions/day | Revenue/day | Days/month | Revenue/month |
|---|---|---|---|---|
| Weekday | 8.6957 | A$1,017.40 | 22 | **A$22,382.73** |
| Saturday | 4.3478 | A$508.69 | 4.33 | **A$2,202.64** |
| **TOTAL** | | | | **A$24,585.37** |

**PM revenue: was A$36,225.69/month (Model C) → now A$24,585.37/month (Model E), a decrease of A$11,640.32/month (-32.1%).** This is Anthony's own directly-specified planning input working through the same, already-established staffing-pattern research — not a re-guess, and not framed as "may be X% high": it is the resolved planning figure, labelled `[MODELED — estimate]`, per Anthony's explicit instruction not to present it as unresolved.

---

## 4. Labour Cost

PM labour costing (`tools/cost_ramp_model.py`) reuses its own pre-existing formula unchanged (`hours/role/day = sessions ÷ 4 roles ÷ 1.3 throughput`, floored at the 3-hour casual minimum) — only the session-count input changes, from the `PM_SESSION_RAMP` constant:

| Month | Old sessions (16-target ramp) | New sessions (10-target ramp) | Hours/role/day |
|---|---|---|---|
| M1 | 4 | 3 | 3.0 (floor) |
| M2 | 8 | 5 | 3.0 (floor) |
| M3 | 12 | 8 | 3.0 (floor) |
| M4 | 15 | 9 | 3.0 (floor) |
| M5plus | 16 | 10 | 3.0 (floor) |

**Genuine, disclosed finding:** at the new 10-session M5plus target, `10 ÷ 4 ÷ 1.3 = 1.923hrs/role`, which is BELOW the 3.0hr floor — unlike the old 16-session target, which cleared the floor at 3.08hrs/role. This means PM weekday labour is now **flat at A$9,808.92/month for every one of the 5 ramp months, including M5plus** (was ramping from a floored M1-M4 rate up to a higher, floor-clearing M5plus rate of A$10,070.50/month). PM Saturday labour is unaffected (A$668.78/day, already floor-bound before this change).

**PM labour total: was A$12,966.32/month (M5plus) → now A$12,704.78/month, a decrease of A$261.54/month** (small — the floor was already absorbing most of the labour-cost effect of a lower session target; the revenue effect above is far larger).

---

## 5. What This Changes and What It Doesn't

**Changes:** `data/canonical/revenue_assumptions.yml` (`rev_pm_weekday_transactions`/`rev_pm_saturday_transactions`, `rev_reconstruction_table1_monthly`/`rev_reconstruction_table2_monthly`), `data/canonical/revenue_ramp.yml` (all 10 records), `data/canonical/cost_ramp.yml` (all 10 records, PM weekday labour line), `data/canonical/client_assumptions.yml` (`pm_steady_state_capacity`, 16→10), `tools/cost_ramp_model.py` (`PM_SESSION_RAMP`, removal of the now-unneeded M5plus anchor).

**Does not change:** PM Saturday labour cost, the PM package prices themselves (A$185 PM Refresh / A$135 PM Restore, see §6 below), the 60/25/15 transaction-mix assumption, AM revenue/costs (independent of this change), or the underlying staffing-pattern research (Refresh = 1 therapist, Restore = 2 specialists) from `PM-CAPACITY-RECONCILIATION.md`.

---

## 6. PM Package Pricing — Locked as the Best Current Defensible Planning Figure

Per Anthony's explicit instruction not to leave this "unresolved": **PM Refresh = A$185, PM Restore = A$135** (both 75 minutes) are used as the resolved planning prices for every figure in this document and in the reconciled content brief this feeds. Anthony's own final sign-off on these two exact numbers has not been separately re-confirmed this round — they are the same figures `docs/architecture/PM-PACKAGES.md` already proposed, carried forward as the best current defensible planning figures, labelled `[MODELED — estimate, real Perth-comparable bundle pricing research, not yet independently re-confirmed by Anthony this round]`. This is a plain estimate label, not a claim the numbers are unresolved or "may be X% high."

---

## Changelog

**2026-09-19** — Created per Anthony's direct instruction to lock PM capacity at exactly 10 sessions/day and reconcile package session-consumption properly (session-count method, not the prior minutes-weighted Model C). Full recompute of PM revenue (A$36,225.69 → A$24,585.37/month) and PM weekday labour (flat A$9,808.92/month across the entire ramp, no more M5plus anchor) propagated through the canonical layer in the same commit.
