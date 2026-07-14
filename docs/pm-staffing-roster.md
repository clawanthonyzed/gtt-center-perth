# GTT Center Perth — PM Shift Staffing Roster (Product Doc)

**Version:** 1.0 | **Date:** 2026-07-14
**Status:** Draft — open questions block roster finalisation

---

## Problem Statement

The PM shift currently runs on a single dedicated therapist offering individual services only, and this staffing level is the confirmed root cause of the venture's projected -A$9,684/month loss (see diagnose output, prior session). Anthony wants to expand the PM shift to offer both standalone booked services and PM packages (bundled services excluding the blood test) across massage, hair, nail, and beauty lines. This requires new dedicated PM hires — not a stretch of AM staff hours — while AM GTT capacity remains the non-negotiable priority and leave/sick coverage must not create staffing gaps in either shift.

## Goals

- PM shift (Mon–Fri) offers standalone individual bookings across massage, hair, nail, and beauty
- PM shift also offers PM packages (bundled services, GTT blood test excluded)
- AM GTT capacity (8 clients/day, current staffing) is never reduced by PM staffing decisions
- Roster has built-in coverage for annual leave, sick leave, and public holidays with no service gap below minimum staffing
- Updated PM labor cost is reflected in financial-model.md and cash-flow.md so break-even can be recalculated

## Non-Goals

- Not expanding AM GTT capacity beyond 8 clients/day in this phase
- Not offering GTT blood collection or any pathology service during the PM shift
- Not resolving PM pricing (already locked in services-pricing-locked.md) — this doc covers staffing only

## User Stories

- As a PM walk-in client, I want to book a standalone massage, hair, nail, or beauty service so I can access services without doing a GTT.
- As a PM client, I want to book a bundled PM package (multiple services, no blood test) so I get value for booking more than one service.
- As the Manager, I want a roster showing AM and PM coverage per day per role so I can confirm minimum staffing is always met.
- As the Manager, I want built-in relief coverage so a single staff member's sick day doesn't cancel PM bookings.

## Technical Requirements

- Define minimum PM staffing per service line (massage, hair, nail, beauty) needed to run standalone + PM package bookings 5 days/week
- Confirm PM-dedicated staff are net-new hires (per Anthony's instruction), not additional hours on existing AM staff
- Calculate weekly rostered hours per PM role based on confirmed PM shift length (see Open Question 1)
- Build a leave-coverage model: relief/casual pool sized per role, or defined cross-cover arrangement
- Recalculate monthly PM labor cost and feed into financial-model.md and cash-flow.md
- Recalculate PM break-even revenue requirement against the new staffing cost
- Reconcile PM shift end time across all documents (currently inconsistent — see Open Question 1)

## Open Questions

1. **PM shift end time:** this brief states 5pm; services-pricing-locked.md and cole.md state 12:00–18:00 (6pm). Must be resolved before rostered hours can be calculated — a 1-hour difference changes weekly PM labor cost by ~20%.
2. **Headcount per service line:** 1 PM-dedicated staff member per line (massage/hair/nail/beauty), or 2 to match AM capacity? No PM demand data exists pre-launch — recommend starting at 1 per line and scaling on booking volume, but this is Anthony's call.
3. **Employment type:** are PM-dedicated hires full-time, part-time, or casual? Materially affects wage cost, leave accrual liability, and rostering flexibility.
4. **Leave coverage model:** dedicated casual/relief pool per role, or occasional AM-staff cross-cover on PM absence days? The latter would partially contradict "no stretching AM staff" — needs an explicit decision.
5. **PM package definition:** exact service combinations and pricing structure not yet defined. Needed before booking system (Fresha) can be configured.
6. **Booking priority:** if PM shift is fully booked, do PM package bookings get priority over standalone single-service bookings?
7. **Public holiday coverage:** stay closed, or open at WA public holiday penalty rates (~2.5x)? Materially affects annual PM labor cost — needs a decision before roster is finalised.

## Definition of Done

- [ ] PM shift hours confirmed and consistent across all GTT Center Perth documents
- [ ] Headcount and employment type for PM-dedicated hires confirmed by Anthony
- [ ] Weekly roster template built showing AM + PM coverage per day, per role
- [ ] Leave/sick/public holiday coverage model defined and costed
- [ ] Updated PM labor cost fed into financial-model.md and cash-flow.md
- [ ] Revised break-even point recalculated and confirmed (loss closed, or new gap size known)

---

## Assumptions Made

- PM-dedicated hires are treated as net-new headcount, separate from the existing AM team, per Anthony's explicit instruction ("we will need to hire more staff")
- AM GTT priority is fixed and non-negotiable — no roster option that reduces AM coverage was considered
- PM shift length (5pm vs 6pm) was NOT resolved — flagged as Open Question 1 rather than assumed, since it materially changes the cost calculation

## Decisions Needed Before Roster Build

1. Confirm PM shift end time: 5pm or 6pm
2. Confirm headcount per PM service line: 1 or 2
3. Confirm employment type for PM hires: full-time / part-time / casual
4. Confirm leave coverage approach: dedicated relief pool vs AM cross-cover
5. Confirm public holiday policy: closed vs staffed at penalty rates

Once these five are answered, Grace can build the actual weekly roster and cost it into financial-model.md.
