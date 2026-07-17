# Booking Rule — Per-Service Capacity Caps + Business-Assigned Service Order

**Date:** 2026-07-17 | **Status:** Specified, needs implementation (Fresha config or the planned custom booking page)

## The problem this solves

If every client could freely pick which service happens first, and enough clients independently pick the same single service, the queue backs up — tested directly this session: 10 clients all wanting Hair with only 2 Hair staff produces waits growing to 20 minutes, affecting 8 of 10 clients. Statistically unlikely under normal demand mix, but the booking system should prevent it structurally rather than rely on luck.

## The rule

**1. Client selects their 2 desired services at booking (unordered) — not which happens first.** The business assigns which is Service 1 (post-Draw-1) vs Service 2 (post-Draw-2), based on that day's actual staffing load. This is a real scheduling degree of freedom, not just a UX simplification — tested this session on the 15-client Scenario D case, and having order-flexibility was what let a fully feasible staff schedule exist.

**2. Enforce a per-service daily capacity cap at booking time**, computed from real peak-concurrent-demand analysis (not guessed):

| Service pool | Cap (10-client/day volume) | Cap (15-client/day volume, if 3rd phlebotomist active) |
|---|---|---|
| Massage + Beauty (cross-trained, 3–4 staff) | 3 concurrent | 4 concurrent |
| Nails (standalone, 2 staff) | 2 concurrent | 2 concurrent |
| Hair (standalone, 2 staff) | 2 concurrent | 2 concurrent |

Once a service's cap is reached for a given time window, it shows as unavailable in the booking widget for that slot — same mechanism as the existing GTT Overbooking Rule in `operations-manual.md`, just extended to the service level instead of only the whole-day GTT count.

## Why this works cleanly here (not a generic same-day problem)

GTT packages book weeks in advance with service selection happening at booking time (per the existing GTT Slot Pairing Rule). That means each day's actual service demand is known well ahead of the day itself — the capacity cap prevents overbooking at the point of booking, not as a same-day scramble. If a client can't get their exact combination on their preferred day, they're offered the next available day/slot at booking time, not turned away on arrival.

## Standalone-gap revenue — realistic sizing, not the theoretical max

Full gap inventory: ~22 slots/day of real ≥45min downtime across the 8-staff roster (see `multirole-CORRECTION.md`/staff profiles for the per-staff breakdown). Filling all 22 is not realistic. Even a conservative fraction converts real dead time into revenue:

| Gaps filled/day | Extra sessions/month (22 trading days) | Extra revenue/month (A$95 avg standalone) |
|---|---|---|
| 2 | 44 | **≈A$4,180** |
| 3 | 66 | **≈A$6,270** |
| 5 (stretch) | 110 | **≈A$10,450** |

Even the conservative 2–3/day case is a genuine, close-to-zero-marginal-cost revenue lever — the staff are already on-site and paid for that block regardless.

## Implementation requirements (not yet built)

1. Fresha (or the planned custom booking page) needs to expose real-time per-service capacity, not just whole-day GTT capacity — a config/build item, not a policy decision alone.
2. A process to publish that day's standalone-bookable gaps once its GTT roster locks in (weeks-ahead booking makes this knowable early, not last-minute — this significantly de-risks the implementation).
3. Assign to: whoever owns the Fresha/booking build (Grace/Ops per `operations-manual.md`'s document ownership) — flagging as the next concrete build task, not yet assigned to a person.
