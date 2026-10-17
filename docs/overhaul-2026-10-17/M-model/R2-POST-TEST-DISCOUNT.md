# R2: 10% post-test discount (workstream M2, 2026-10-17)

This is general knowledge, not your personal documents. Verify with a qualified adviser before acting. Consumer-law, GST and pathology-rule points are for the accountant, a solicitor and the pathology partner to confirm.

## 1. Policy box (adopted by Anthony 2026-10-17; details marked PROPOSAL need his sign-off)

| Term | Policy | Status |
|---|---|---|
| Who | Any expecting mother who completes a GTT test | **Adopted** (Anthony) |
| What she gets | 10% off standalone wellness treatments or multi-service packages | **Adopted** |
| When | Not limited to the afternoon. Valid immediately: a morning client who completes her test (final draw taken) can redeem the same day if a therapist is free, whether she finishes early or late | **Adopted** |
| Which test | A GTT test completed at GTT Center Perth (all three draws taken) | PROPOSAL (the directive says "a GTT test"; tests done elsewhere cannot be verified) |
| Applies to | Every service on the treatment menu booked as a standalone treatment, and the afternoon packages (PM Refresh A$185, PM Restore A$135). Menu prices from `docs/overhaul-2026-10-16/X-market/AFTERNOON-MENU.md` | PROPOSAL |
| Excludes | The GTT morning package (A$250 or A$300) and the upgrade between them; the test and any lab fee (the model charges clients no lab fee); refreshments and café items; retail; gift vouchers; deposits | PROPOSAL |
| Stacking | Never combined with another offer. It **replaces** the earlier "10% online pre-booking discount on afternoon services booked with a test reservation": one 10% only, whichever she uses first. The earlier rule "no discount on same-day upsells" is lifted for standalone treatments and packages and stays for add-ons sold inside the morning package, café and retail | PROPOSAL (needs Anthony: it changes `docs/services-pricing-locked.md`) |
| Use limit | One redemption per completed test, on one booking (one treatment or one package). A repeat test earns a new one. Not per visit | PROPOSAL |
| Expiry | 14 days from the test date (the figure X proposed on 2026-10-16) | PROPOSAL |
| Availability | Subject to availability; walk-ins only when a therapist is free (afternoon rule) | Existing rule |
| How it is recorded | When the third draw is logged in the collection log the booking system flags the client as eligible with the test date; the discount is applied at checkout and logged against the test; the Venue Manager counts redemptions weekly for Grace. Until the booking system is configured a numbered paper slip is used. Client consent is needed to message her about the offer | PROPOSAL |
| Name | Test Day Thank You (working name from X); the customer wording is for Anthony | PROPOSAL |
| Pathology and consumer-law check | The discount is on GTT's own wellness services, open to every client, not linked to any referrer, doctor or lab request. Confirm with the pathology partner and the Medicare workstream (`docs/overhaul-2026-10-17/L-medicare/`) that a post-test offer raises no issue, and with a solicitor that the terms meet Australian Consumer Law advertising rules | TO CONFIRM |

## 2. What the model does and does not already contain

The afternoon is modelled at full price and at capacity: 8.6957 bookings on a weekday and 4.3478 on a Saturday at A$117 gives **A$24,585.37 a month** (210.13 bookings). The earlier 10% pre-booking discount was never taken out of that figure (tracker item 39, ITC-38). So any redemption by a client who would have booked anyway costs 10% of a sale the model already counts in full. The model base is unchanged by this round; the discount is shown below as a separate cost and a separate, assumption-based upside, never netted into the headline.

Testing clients who could redeem: 18 a morning x 26.33 trading days = **473.94 a month** (every morning client completes a test). Prices are the repo's: A$117 average afternoon booking (the model figure), A$135 PM Restore, A$185 PM Refresh.

## 3. Cost: what the discount gives away (certain per redemption, take-up is assumed)

If a redeemer would have booked at full price anyway, the discount costs 10% of that booking. Take-up is the share of testing clients who redeem; **no take-up data exists, every rate below is an assumption**. X's 25% figure was rounded to 118 redemptions (118 x A$117 x 10% = A$1,380.60, shown as A$1,381); exact is 118.49 redemptions and A$1,386.27, a A$5 difference.

| Take-up (share of testing clients who redeem) | Redemptions a month | Cost a month: one treatment at A$117 | Cost: PM Restore at A$135 | Cost: PM Refresh at A$185 | Cost at A$117 as share of monthly net profit | Break-even added (A$117) | Break-even after adaptive roster (A$117) |
|---|---|---|---|---|---|---|---|
| 5% | 23.7 | A$277.25 | A$319.91 | A$438.39 | 0.8% | +0.042 | 7.293 |
| 10% | 47.4 | A$554.51 | A$639.82 | A$876.79 | 1.6% | +0.084 | 7.335 |
| 15% | 71.1 | A$831.76 | A$959.73 | A$1,315.18 | 2.4% | +0.126 | 7.377 |
| 25% | 118.5 | A$1,386.27 | A$1,599.55 | A$2,191.97 | 3.9% | +0.211 | 7.461 |
| 40% | 189.6 | A$2,218.04 | A$2,559.28 | A$3,507.16 | 6.3% | +0.337 | 7.587 |

Worst case reading: at 25% take-up and A$117 a booking the discount costs A$1,386.27 a month (3.9% of the A$35,186.40 monthly profit), which would raise break-even from 7.250 to 7.461 morning clients a day. At 10% take-up it costs A$554.51 (break-even 7.335). On the GST-stress basis the discount lowers GST by one eleventh of itself, so the break-even effect is the same.

## 4. Upside: extra revenue it should create (assumption-based)

The discount creates value only if redeemers include clients who would not otherwise have booked, or who book a longer service. Let R be redemptions, s the booking price, q the share of redeemers who are new bookings (assumed, no data) and m the extra cost of delivering one new booking.

- Each new booking earns 0.9 x s - m. Each redeemer who would have booked anyway costs 0.1 x s.
- **The discount pays for itself when q >= 0.1 x s / (s - m).** This does not depend on the take-up rate; take-up only scales the amount.
- m = A$0 where the therapist time is already paid (an afternoon place that would otherwise be empty, or a quiet morning inside a paid 6-hour shift). m = A$68.74 where extra hours must be paid, taken from the repo's afternoon labour (A$12,704.74 x 1.137 spread over 210.13 bookings).

| Price basis | If the extra hours are already paid (idle capacity) | If the extra hours must be paid (loaded afternoon labour A$68.74 a booking) |
|---|---|---|
| Treatment A$117 | 10.0% of redeemers must be new bookings | 24.2% of redeemers must be new bookings |
| PM Restore A$135 | 10.0% of redeemers must be new bookings | 20.4% of redeemers must be new bookings |
| PM Refresh A$185 | 10.0% of redeemers must be new bookings | 15.9% of redeemers must be new bookings |

Plain reading: on A$117 treatments the discount covers its own cost if one redeemer in ten is a new booking (idle capacity), or about one in four (24.2%) if the extra hours must be paid. Packages need fewer (15.9% for PM Refresh) because the margin per booking is larger. In absolute terms at 25% take-up (118.5 redemptions) that is about 12 new bookings a month with idle capacity, or 29 if hours must be paid, 2.5% and 6.1% of all testing clients.

Net effect on monthly profit (A$117 booking; A$35,186.40 before the discount):

| Take-up | New bookings among redeemers | Net effect a month (extra hours already paid) | Net effect a month (extra hours must be paid) | Monthly net profit after (extra hours already paid) |
|---|---|---|---|---|
| 5% | 0% | -A$277.25 | -A$277.25 | A$34,909.15 |
| 5% | 10% | A$0.00 | -A$162.90 | A$35,186.40 |
| 5% | 25% | A$415.88 | A$8.63 | A$35,602.28 |
| 5% | 50% | A$1,109.02 | A$294.51 | A$36,295.42 |
| 10% | 0% | -A$554.51 | -A$554.51 | A$34,631.89 |
| 10% | 10% | A$0.00 | -A$325.81 | A$35,186.40 |
| 10% | 25% | A$831.76 | A$17.25 | A$36,018.16 |
| 10% | 50% | A$2,218.04 | A$589.01 | A$37,404.44 |
| 25% | 0% | -A$1,386.27 | -A$1,386.27 | A$33,800.13 |
| 25% | 10% | A$0.00 | -A$814.51 | A$35,186.40 |
| 25% | 25% | A$2,079.41 | A$43.13 | A$37,265.81 |
| 25% | 50% | A$5,545.10 | A$1,472.53 | A$40,731.50 |

## 5. Separation of cost and upside

| | Cost | Upside |
|---|---|---|
| Certain? | Yes, 10% of each redeemed booking | No, depends on new bookings |
| Source | Repo prices and 473.94 testing clients; take-up assumed | Share of new bookings assumed; extra-cost case assumed |
| Size | A$277 to A$2,218 a month at 5% to 40% take-up on A$117 bookings | Zero to several thousand a month; see the table above |
| In the headline model | Not deducted (shown separately) | Not added |
| Why accepted | An empty afternoon place earns nothing against paid therapist hours, so a discounted place is worth more than an empty one (X, 2026-10-16); the discount also lifts the quiet weekdays and supports the afternoon revenue of A$24,585.37 that the model assumes will fill | |

## 6. Net effect on break-even

The discount changes break-even only through its cost. With the adaptive roster (7.250): 5% take-up 7.293, 10% 7.335, 15% 7.377, 25% 7.461, 40% 7.587. All stay far below the 18-a-day capacity and below the previous 8.266.

## 7. Wording updated (afternoon-only references)

- `docs/services-pricing-locked.md`, `docs/financial-break-even-staff.md`: discount policy lines now point to the adopted 10% post-test policy.
- `docs/overhaul-2026-10-16/X-market/REVENUE-PROFIT-STRATEGY.md` section P11b and `docs/overhaul-2026-10-16/X-market/FOR-DOCUMENTS-AGENT.md` page 11: the "afternoon only, advance booking only" proposal is replaced by the adopted policy.
- `docs/ITEMS-TO-CONFIRM.md` ITC-38 and `docs/VERIFICATION-TRACKER.md` item 39: updated to reference this cost model.
- Not edited (documents agent owns): `outputs/PRESENTATION/slides.html`, `outputs/PRESENTATION/BUSINESS-PLAN.md` (Section 4.6 step 4, Section 5.3, cross-selling row, open-decision lists), and the slide script `outputs/PRESENTATION/build/build_slides.py`. The Imara brief files under `docs/presentations/` repeat the "10% online discount when pre-booked" wording; they are presentation hand-offs and were not touched (flag).
