# THEODORE R23 PART 3: the revenue ramp, where it lives, and the timeline without it

Theodore, financial consultant, 2026-10-27. Numbers from [theodore_r23_cashflow.py](theodore_r23_cashflow.py). General knowledge and repo figures, not your personal documents. Nothing sent. Tags: R repo, E estimate.

## READ-FIRST CHECK

- Venue manager starts 06:30 (Mon to Fri 06:30 to 15:00). 07:00 is the first draw. Anthony is Owner and Director, not the venue manager.
- Path A = PREFERRED: package with the GTT midwife consult. Path B = NOT preferred: outside referral, no GTT consult.
- Prices: Path A A$320 / A$370, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350 all in, GTT charges A$272.15 / A$322.15.  <!-- factcheck:ok -->
- Rebates: consult A$32.95 + lab A$22.05 = A$55.00 (shown as about).
- Midwives 08:00 to 16:00, first consult 08:15, 25 minute blocks to 10:30.
- Late rule: clients arrive 10 minutes early; late means from the appointment time onwards.

## 1. What the ramp is

The repo's ramp says the business earns **43, 64, 79 and 93 percent** of full revenue in months 1 to 4, and **100 percent** from month 5.

**What it was based on: nothing measured.** The repo says so itself: it is a "reused historical planning convention", status MODELLED, not VERIFIED. No document gives a reason for those five numbers: no booking curve, no referral pipeline, no outside benchmark (R, REVENUE-RAMP-METHODOLOGY.md section 2; revenue_ramp_model.py comment on RAMP_CURVE). It was first used in three old documents built for 10 and 12 clients a day, before the 18-client model existed.

## 2. Where each ramp lives

| Place | What is there | Status today |
|---|---|---|
| tools/revenue_ramp_model.py | RAMP_CURVE = 43/64/79/93/100, applied to AM and PM revenue | Calculator kept (GTT rule: never rewrite repo calculators). Not used by the locked case |  <!-- factcheck:ok -->
| data/canonical/revenue_ramp.yml | Month 1 to 5 revenue built from that curve | Reference only |
| data/canonical/revenue_assumptions.yml | rev_ramp_pct_curve_historical (marked SUPERSEDED) and rev_pm_session_ramp_historical | Reference only |
| tools/cost_ramp_model.py, data/canonical/cost_ramp.yml | PM sessions 3/5/8/9/10 a day in months 1 to 5. AM staff are fixed from month 1 | Reference only. The locked case uses the full roster from month 1 |
| docs/cash-flow.md, docs/profit-loss-tables.md, docs/investor-memorandum.md | The original 43/64/79/93/100 tables (10 and 12 client models) | Historical, out of date |  <!-- factcheck:ok -->
| **My R22C timeline** (THEODORE-R22C-PART-1, theodore_r22c.py) | Read the ramp from revenue_ramp.yml | **My error.** See below |

**Own goal, stated plainly:** you already removed the ramp on 2026-10-16 (DECISION-LOG, item (c): "The 43% / 64% / 79% / 93% ramp is removed from every model"). The 3-way model v0.6 and CASHFLOW-FORECAST.md were rebuilt with no ramp. My Round 22 loan timeline pulled the old curve back in from revenue_ramp.yml. That is why it showed month 20 and a A$96,663.78 top-up. Both figures are withdrawn.

## 3. What I fixed today

| File | Line | Change |
|---|---|---|
| docs/FINANCIAL-CENTER-OF-TRUTH.md | Morning clients source | Was "revenue_ramp.yml, 22 + 4.33 days". Now: 18 a day x 26.33 trading days (22 weekdays + 4.33 Saturdays). **That day count is a calendar count, not a ramp.** No ramp, full volume from month 1 |
| same | Venue manager line | Was out of date ("Anthony says he is administrator and venue manager"). Now: a hired venue manager; Anthony is Owner and Director. GTT-READ-FIRST.md wins |  <!-- factcheck:ok -->
| same | Company tax line, change log | Three companies, no trust; Round 23 row added |
| center_of_truth.yml | volumes, venue_manager | Added "ramp: none"; replaced the old open-issue line |

Both files regenerate from theodore_r22.py (I edited its writer only, re-ran it, and checked that the headline is unchanged: A$26,631.97 before tax, A$19,973.98 after).

## 4. Loan timeline with NO ramp (flat 100 percent from month 1)

Same method as R22C (start-up spend A$251,198 at month 0, every spare dollar after tax repays the shareholder loan, R and E), ramp set to 100 percent:

| | A$250,000 put in | A$336,000 put in |
|---|---|---|
| Cash left after start-up spend | -A$1,198 | A$84,802 |
| Extra owner cash needed early | **A$1,198** at opening (month 1 profit covers it) | **A$0** |
| Monthly repayment from month 1 | about A$19,973.98 | about A$19,973.98 (plus A$84,802 in month 1) |
| **Loan cleared** | **Month 13** | **Month 13** |
| **First dividend** | **Month 14** | **Month 14** |

With tax, GST and working-capital timing added (Part 4, THEODORE-R23-CASHFLOW.md) the answer is the same: **loan cleared month 13, first dividend month 14**, or month 15 / 16 if you keep a A$50,000 cash floor. Compared with my R22C: 7 months sooner, and no A$96,663.78 top-up.

All of this rests on your decision that the waitlist and marketing fill 18 mornings from day one. If they do not, the repo's own warning still applies: at 70 percent fill (12.6 a morning) the company loses about A$8,871.51 a month after GST (R, CASHFLOW-FORECAST.md section 3, earlier price basis).

**Second location (option only):** if a second venue opens within a reasonable time, part of the cash could go to it first and the owner repayments would pause. Not modelled; no data in the repo.

Regards.
Theodore
