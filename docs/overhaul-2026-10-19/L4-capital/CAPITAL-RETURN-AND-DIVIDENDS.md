# Capital return first, then franked dividends (one GST journey)

General knowledge, not personal documents. Verify with a registered tax agent before acting. Prepared 2026-10-19 by Theodore (CFO role, run by Idea Lobster). Model script: [theodore_model.py](theodore_model.py). Inputs come only from the repo: GST-SPLIT-MODEL.md and MODEL-WORKINGS.md (A$250 package is GST-inclusive; steady state profit A$35,186.40 a month before the ATO's share).

## 1. One GST journey (replaces the old before/after pair)
The GST in the A$250 price is the ATO's money, never GTT's. So the only real profit is the after-GST one.

| Step | Per year |
|---|---|
| Customers pay (GST-inclusive revenue) | A$1,716,844.44 |
| Costs paid (GST-inclusive) | A$1,294,607.64 |
| Old "before GST" profit (retire this number) | A$422,236.80 |
| Net GST sent to ATO (collected A$156,076.80 less credits A$15,150.96) | A$140,925.84 |
| **Real profit before company tax** | **A$281,310.96** (A$23,442.58 a month) |
| Company tax 25% (base rate entity) | A$70,327.74 |
| **Profit after company tax** | **A$210,983.22** |

## 2. Loan back first (tax-free)
Owners lend to the company (written loan agreement, signed before the money moves). Repaying loan principal is giving back the owners' own money, so it is not income and not a dividend. Interest-free keeps it simple. Rules in the model: A$85,000 cash stays in the company, 25% of profit is parked for company tax, one month of GST is held for the BAS.

| Case | Loan A$251,198 | Loan A$336,000 |
|---|---|---|
| Steady state (repo, no ramp-up) | fully repaid in month 15 | month 15 (A$84,802 surplus comes back in month 1) |
| Cautious ramp (older repo ramp 43/64/79/93% in months 1-4) | month 19 | month 19 |
| Stress: AM volume 15% under plan | about month 47 | about month 47 |

Repayment per month at steady state: A$17,581.94 (A$23,442.58 less 25% tax set aside).

## 3. Dividends after the loan is cleared (2026-27 resident rates; Anthony 0% Medicare levy; partner A$100,000 other income + 2% levy, ASSUMED until her real figure is known)
| Cash dividend a year | Anthony | Partner | Family cash after personal tax | Kept in company |
|---|---|---|---|---|
| A$50,000 | A$50,000 | A$0 | A$56,147 | A$160,983 |
| A$100,000 | A$100,000 | A$0 | A$102,813 | A$110,983 |
| **A$127,500** | A$101,500 | A$26,000 | **A$127,763** | **A$83,483** |
| A$150,000 | A$123,500 | A$26,500 | A$146,673 | A$60,983 |
| A$210,983 (pay everything) | A$143,500 | A$67,483 | A$196,700 | A$0 |

Total tax on the slice of profit that is distributed: 24.9% at A$127,500, 30.1% when everything is paid out.

## 4. Clinic #2 from retained cash (A$300,000 to A$350,000)
| Cash dividend kept | Retained a year | Years to A$300k | Years to A$350k |
|---|---|---|---|
| A$127,500 | A$83,483 | 3.6 | 4.2 |
| A$100,000 | A$110,983 | 2.7 | 3.2 |
| A$50,000 | A$160,983 | 1.9 | 2.2 |
| A$0 | A$210,983 | 1.4 | 1.7 |
Retained profit has only paid the 25% company rate; no personal tax until it is paid out.

## 5. Practical checks (flagged, confirm with the accountant)
1. Franking credits only exist once the company has paid tax, which is after the first tax return. Dividends declared before that cannot be fully franked. The loan-first order fits this.
2. Company must stay solvent after any repayment; BAS and PAYG come before owners.
3. Partner's real income this year is not on file; the split changes if it is lower (she is on maternity leave).
4. Depreciation of the fit-out and equipment is NOT deducted here; it would lower company tax (upside).
