# GTT Center Perth — Financial Infrastructure Setup
## Pre-Launch Checklist
### Version 1.0 | June 2026 | Owner: Bruno (Finance Agent) + Imara

---

## OVERVIEW

All financial infrastructure must be operational before the first patient pays. This document is a sequential checklist. Complete in order — each step depends on the previous.

**Target completion:** Week 12 (4 weeks before soft open)  
**Accountant brief required:** Week 1 (before any other financial steps)

---

## STEP 1 — ENGAGE ACCOUNTANT (Week 1 — BLOCKING)

Before any financial setup: brief a Perth-based accountant with experience in:
- Discretionary trust taxation
- Mixed supply GST (GST-free + taxable in same business)
- Health services businesses

**Brief the accountant on:**
1. YETI Holding Trust structure (trust + corporate trustee YETI Tipi Holdings PTY LTD)
2. GTT Center Perth trading as the trust
3. Mixed supply GST issue (pathology = GST-free, wellness = taxable, rental income = taxable)
4. Imara salary vs trust distribution decision (must be resolved before first pay run)
5. TPI pension implications (flag to DVA-qualified advisor — accountant must know this constraint)
6. 2028 trust distribution tax risk — should we add an operating PTY LTD under the trust now?

**Deliverables from accountant (get in writing):**
- [ ] Confirmed entity structure (trust trades directly vs add operating PTY LTD)
- [ ] Imara remuneration structure (salary amount vs distribution amount)
- [ ] GST registration advice (must register before first booking)
- [ ] BAS lodgement frequency (monthly vs quarterly — recommend monthly given cash flow tightness in Month 1–3)
- [ ] Default super fund selection for employee contributions
- [ ] Payroll tax threshold advice (WA: A$1M/year threshold — not triggered at launch but confirm)

**Accountant cost:** A$500–1,500 for initial brief and structure confirmation.

---

## STEP 2 — ABN AND BUSINESS NAME REGISTRATION (Week 1)

| Action | How | Cost | Timeline |
|---|---|---|---|
| Confirm existing trust ABN covers GTT Center Perth trading activity | Accountant confirms | Nil | Week 1 |
| Register business name "GTT Center Perth" with ASIC | business.gov.au | A$39/year | Week 1 — takes 1 business day |
| GST registration | ATO Online via business.gov.au | Nil | Week 1 (must be before first taxable transaction) |
| BAS agent authorisation | Give accountant ATO agent access to lodge BAS | Nil | Week 2 |

**ABN note:** The YETI Holding Trust already has an ABN. Confirm with accountant whether GTT Center Perth trading activity requires a separate registration or operates under the existing trust ABN. Most discretionary trusts can trade under one ABN with multiple business names.

---

## STEP 3 — TRUST BANK ACCOUNTS (Week 2)

**Required accounts:**

| Account | Purpose | Bank |
|---|---|---|
| GTT Center Perth Operating Account | All revenue in, all expenses out | NAB / ANZ / Westpac business account |
| GST Holding Account | Set aside GST collected before quarterly/monthly lodgement | Sub-account of same bank |
| Staff Wages Account | Weekly payroll transfers | Sub-account or same account (Xero manages) |

**Setup requirements:**
- Business bank account in trust name: "YETI Holding Trust t/as GTT Center Perth"
- Authorised signatories: Anthony (trustee) + Imara (operational authority)
- Internet banking access for Imara (payment approvals up to A$2,000 per transaction — see Financial Gates in grace-startup-plan.md)
- Payments > A$2,000: require Anthony's approval

**GST discipline:** On the 28th of each month, transfer that month's net GST liability to the GST Holding Account. Never spend GST collected — it belongs to the ATO.

---

## STEP 4 — XERO SETUP (Week 2–3)

### Account configuration

- [ ] Create Xero account under YETI Holding Trust ABN
- [ ] Connect to ATO (STP Phase 2 — mandatory for payroll reporting)
- [ ] Configure chart of accounts — must separate:
  - GST-free revenue (pathology GTT component)
  - GST-taxable revenue (wellness services, room rental)
  - GST-taxable expenses
  - GST-free expenses
- [ ] Connect bank feeds (NAB/ANZ Open Banking connection to Xero)
- [ ] Set BAS period: monthly (lodged by 21st of following month)
- [ ] Set financial year start: 1 July

### GST coding — CRITICAL

GTT Center Perth is a mixed supply business. Every transaction must be coded correctly.

| Transaction type | GST code in Xero |
|---|---|
| GTT package revenue — pathology component | GST-free (BAS1 = G1, Input = N/A) |
| GTT package revenue — wellness component | Standard-rated (GST 10%) |
| Afternoon wellness revenue | Standard-rated (GST 10%) |
| Room rental income (scan, dietitian) | Standard-rated (GST 10%) |
| Retail product sales | Standard-rated (GST 10%) |
| Staff wages | No GST (wages exempt) |
| Superannuation contributions | No GST |
| Rent expense | Standard-rated (GST 10% — claim input tax credit) |
| Medical/pathology supplies (glucose, vacutainers) | GST-free (medical supplies) |
| Professional services (accountant, solicitor) | Standard-rated (GST 10%) |

**Note on package apportionment:** When a patient pays A$285 for a Restore package (GTT + massage + nails), the pathology component is GST-free and the wellness component is taxable. Accountant must advise on the apportionment method (fair market value approach or formula-based).

### Payroll setup (Week 3–4)

- [ ] Add all employees with full details (name, DOB, TFN, address, bank account, super fund)
- [ ] Set classification and award rate for each employee
- [ ] Configure leave accrual (annual leave, personal/carer's leave, FDV leave from Day 1)
- [ ] Set pay calendar: weekly, Friday pay date, Monday run
- [ ] Enable STP: connect to ATO, test with a dummy pay run before going live
- [ ] First real payroll: reviewed by accountant before processing
- [ ] Configure super payments: monthly, due 28th of following month, via clearing house (ATO Small Business Superannuation Clearing House — free for <20 employees)

---

## STEP 5 — EFTPOS AND PAYMENT PROCESSING (Week 8–10)

### In-venue EFTPOS

**Recommended:** Square Terminal or Tyro terminal  
- Square Terminal: A$299 one-off, 1.6% transaction fee (cards present), no monthly fee
- Tyro: A$0 terminal (leased), 1.4% transaction fee, A$35/month software
- Bank EFTPOS (NAB/ANZ): slower approval, higher monthly fees — avoid for launch

**Setup requirements:**
- [ ] EFTPOS terminal ordered and arrives before staff training (Week 12)
- [ ] Connected to venue internet (ethernet preferred — not WiFi for reliability)
- [ ] Test: process A$1 transaction, verify bank receipt, reverse transaction
- [ ] Receipt printing: paper and emailed receipt both operational

### Fresha Pay (online deposits)

- [ ] Fresha Pay connected to trust bank account
- [ ] A$30 deposit configured for all GTT bookings
- [ ] Card-on-file enabled for no-show charges
- [ ] Test: make a test booking, pay A$30 deposit, verify it appears in bank account within 3 business days
- [ ] Refund test: refund the A$30, confirm it returns to test card

### Payment flow

| Stage | Payment | Method |
|---|---|---|
| Booking | A$30 deposit | Fresha Pay (card online) |
| End of visit | Balance of package | EFTPOS terminal (in venue) |
| No-show | Full session charge | Fresha Pay card-on-file |
| Cancellation ≥24hrs | Deposit refunded | Fresha Pay refund |

---

## STEP 6 — WORKCOVER WA REGISTRATION (Week 10 — before first hire)

- [ ] Register at workcover.wa.gov.au as an employer
- [ ] Confirm industry classification (health and beauty services — approximate rate 1.5–2.0% of wages)
- [ ] Calculate estimated annual premium based on projected wages (A$22,575 gross wages × ~1.7% = ~A$384/month)
- [ ] Payment: annual premium, can pay by monthly instalment
- [ ] Certificate of registration: keep on file and make available to employees

---

## STEP 7 — SUPERANNUATION SETUP (Week 10)

- [ ] Default super fund selected (confirm with accountant — industry fund e.g., HESTA for health workers or AustralianSuper as general default)
- [ ] Each employee offered super choice form within 28 days of start
- [ ] If employee nominates their own fund: record stapled super fund (ATO lookup required)
- [ ] Super contribution schedule: monthly, 28th of following month
- [ ] ATO Small Business Super Clearing House: register at ato.gov.au (free for <20 employees)
- [ ] Xero: super payment reminders configured for 21st of each month (pay 7 days early to allow clearinghouse processing)

---

## STEP 8 — INSURANCE (Week 10)

All policies must be active before first patient enters venue.

| Policy | Provider options | Min coverage | Annual cost est. |
|---|---|---|---|
| Public liability | BizCover, Aon, Gallagher | A$20M (NATA requirement) | A$2,500–4,500 |
| Professional indemnity | Same broker | A$5M | A$2,000–4,000 |
| Workers compensation | WorkCover WA mandatory | As per WC Act | A$4,500–6,000 |
| Commercial property contents | Building insurer (landlord) + contents | Fit-out + equipment value | A$1,500–2,500 |
| Business interruption | Optional | 6 months revenue | A$1,200–2,000 |
| **TOTAL ANNUAL** | | | **A$11,700–19,000** |

**Get 3 quotes.** BizCover (online, instant quotes) is the fastest for public liability and PI for small health businesses.

**Certificate of currency:** Get a certificate of currency for each policy. Required by:
- Landlord (public liability, before lease signing)
- WDP (public liability, before accreditation inspection)
- All subtenants (before they sign Room Licence Agreements)

---

## STEP 9 — FOOD BUSINESS NOTIFICATION (Week 14)

GTT Center Perth serves food (packaged snacks, coconut water, herbal teas). This is classified as a **low-risk food business** in WA.

- [ ] Notify the local council (not State Health — councils handle food business notifications in WA)
- [ ] Required: Food Safety Supervisor certificate (FSS) — Imara or receptionist completes online course (~4 hours, A$100–200)
- [ ] Document the FSS certificate holder's details for the council notification
- [ ] Post food safety poster in snack preparation area (free from council)
- [ ] Note: pre-packaged snacks with intact packaging have minimal requirements. No hot food preparation = no council inspection required.

---

## STEP 10 — MONTHLY FINANCIAL RHYTHM (from Month 1)

| Week | Action | Who |
|---|---|---|
| Monday | Weekly payroll run (pay Friday) | Bruno (Xero) → Imara approves |
| Wednesday | Reconcile bank feed in Xero | Bruno |
| Friday | Weekly P&L report to Anthony | Bruno |
| Month end | Reconcile all accounts, prepare management accounts | Bruno + accountant |
| 21st of month | Pay super contributions via clearing house | Bruno |
| 28th of month | Transfer GST liability to holding account | Bruno |
| Following month 21st | Lodge BAS with ATO | Accountant |

---

## KEY FINANCIAL GATES

| Decision | Threshold | Approval required |
|---|---|---|
| Individual expense | < A$500 | Imara |
| Individual expense | A$500–A$2,000 | Imara + notify Bruno |
| Individual expense | > A$2,000 | Anthony explicit approval |
| New supplier contract | Any amount | Anthony reviews |
| Lease or property commitment | Any amount | Anthony explicit approval + solicitor |
| Trust distribution | Any | Anthony (as trustee) + accountant advice |

---

## FINANCIAL REPORTING SCHEDULE

| Report | Frequency | Owner | Audience |
|---|---|---|---|
| Daily revenue summary | Daily | Fresha auto-report → Imara | Imara |
| Weekly P&L | Weekly (Friday) | Bruno | Anthony + Imara |
| Monthly management accounts | Monthly | Bruno + accountant | Anthony |
| Quarterly BAS | Monthly (not quarterly — given tight early cash) | Accountant | ATO |
| Annual financial statements | Annual | Accountant | Trust beneficiaries, bank |
| Annual super compliance check | Annual (July) | Bruno + accountant | ATO |

---

*Owner: Bruno (Finance Agent) | Imara (operational execution)*  
*Accountant brief: Week 1 — this document is the briefing agenda*
