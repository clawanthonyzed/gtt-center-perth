> SUPERSEDED on Path B wording (Round 24, Anthony 2026-10-27): Path B is NOT limited. Ignore any cap, limit or roster-shrink wording below. See docs/GTT-READ-FIRST.md.

# Theodore R22, Part 3: Anthony as venue manager (sensitivity only), health lawyer line, questions

Date: 2026-10-26. Source: [theodore_r22.py](theodore_r22.py), [theodore_r22_results.json](theodore_r22_results.json). Tags: R repo, E estimate, U unverified. General knowledge and desk research, not your personal documents. Verify before acting.

## READ-FIRST CHECK

- Venue manager: starts 06:30, Mon to Fri 06:30 to 15:00. 07:00 is the first draw.
- Path A = consult package (PREFERRED). Path B = outside referral (NOT preferred).
- Prices: Path A A$320 / A$370 shown, GTT charged A$292.15 / A$342.15. Path B A$300 / A$350 all in, GTT charged A$272.15 / A$322.15.
- Rebates: consult A$32.95 + lab A$22.05 = A$55.00; client cost on Path A A$265 / A$315.
- Midwives 08:00 to 16:00; first consult 08:15; 25 minute blocks to 10:30.
- Late: from the appointment time onwards; a consult may allow 5 to 10 minutes if the midwife can finish in the time left.

## 1. Job 5: what if the venue manager line were zero (SENSITIVITY ONLY)

Anthony has said he is administrator and venue manager. The model still carries a paid venue manager at A$8,504.76 a month loaded (repo base A$8,004.48 + extra half hour A$500.28, R). **This table is NOT applied and is NOT the headline. The headline stays A$26,631.97 before tax and A$19,973.98 after.**

| Case (Path A, Package 1) | Before company tax | After company tax | Change after tax vs headline |
|---|---|---|---|
| Headline (paid venue manager) | A$26,631.97 | A$19,973.98 | 0 |
| Venue manager line = zero, payroll tax left as is | A$35,136.73 | A$26,352.55 | +A$6,378.57 |
| Venue manager line = zero, payroll tax also falls (E) | A$35,668.39 | A$26,751.29 | +A$6,777.31 |

The payroll tax saving of A$531.66 a month (E) assumes the group stays above the A$1m threshold and the wage drops out of the grouped wage bill. Super and workers comp are inside the A$8,504.76.

### Open issues for Catherine (I do not decide these)

1. **MRCA work hours.** Anthony's Special Rate Disability Pension work test is 10 hours a week of remunerative work. A venue manager role of Mon to Fri 06:30 to 15:00 is far above that if it counts as work. Whether unpaid, paid, or director duties count is a legal question.
2. **Route B means no wage.** The locked income route is franked dividends with no wage. Paying Anthony a venue manager wage conflicts with Route B. Doing the job unpaid is a separate question for Catherine (and for the unpaid-work rules).
3. **Roster cover.** If Anthony is on site 06:30 to 15:00, who covers when he is away? The A$8,504.76 may still be needed for a paid venue manager on those days.
4. **Dividends are not work hours** (per the locked MRCA note); that part is settled.

Nearest compliant alternative to a dead end: keep the paid venue manager in all financials until Catherine rules; show the zero case only as the upper bound above.

## 2. Job 6: health lawyer cost

Health lawyer cost (general knowledge, about A$2,500 to A$8,000 fixed fee, not a quote) is excluded from all financials.

## 3. Checks run

- Headline asserts in the script: A$26,631.97 before tax and A$19,973.98 after, both unchanged (stops if either moves).
- Venue manager figures asserted: A$8,004.48 + A$500.28 = A$8,504.76.
- Shared block asserted: forms total A$50,415.21 less shared A$23,783.23 = A$26,631.98 before rounding noise; the script allows 5 cents.
- `python tools/factcheck_locked_facts.py` run on GTT-READ-FIRST.md, the regenerated Center of Truth and all three parts (result at the end of the final reply).

## QUESTIONS FOR ANTHONY

1. Path B price. A$300 clears the break-even only if the midwife roster shrinks; it falls A$26.66 short a client if the roster stays fixed. (a) keep A$300 / A$350 as decided; (b) raise to about A$330 / A$380 so Path B never loses money; (c) cap Path B at 10 percent of bookings. Recommendation: (a) now, since you decided it and the loss is A$947.65 a month at 10 percent; revisit with real take-up.
2. Path B receipt. (a) Option 3 (same layout, honest zero consult line); (b) Option 1 (one line); (c) Option 2 (two lines, only if the second line is real work). Recommendation: (a), after Catherine confirms.
3. Venue manager. (a) keep the paid line in all numbers until Catherine rules; (b) switch the headline to zero. Recommendation: (a).

Regards.
