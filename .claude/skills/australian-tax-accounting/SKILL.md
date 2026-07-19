---
name: australian-tax-accounting
description: Australian tax law, GST, income tax, CGT, digital product income, trust accounting, crypto tax, BAS, and ATO compliance for online businesses and AI ventures
type: skill
consultant: Eleanor
created: 2026-04-24
---

# Australian Tax and Accounting — Skill

## When to Activate
- Any Australian tax question across the 33 empire ventures
- GST registration, BAS preparation, income tax queries
- Digital product income treatment (Gumroad, Etsy, LemonSqueezy)
- Crypto and prediction market tax
- Business expense deductibility
- "Is this income?", "Can I claim this?", "Do I need to register for GST?"

## Core Tax Knowledge

### Income Tax — Australian Residents

**Tax Rates 2025-26**
| Taxable Income | Rate |
|---------------|------|
| $0 - $18,200 | 0% (tax-free threshold) |
| $18,201 - $45,000 | 16% |
| $45,001 - $120,000 | 30% |
| $120,001 - $180,000 | 37% |
| $180,001+ | 45% |

Plus Medicare Levy: 2% on all taxable income above $26,000.

**Empire Income — Tax Treatment**
| Income Type | Platform | Treatment |
|-------------|---------|-----------|
| Digital product sales (AU buyers) | Etsy, Gumroad | Assessable income + GST if registered |
| Digital product sales (overseas buyers) | Etsy, Gumroad | Assessable income, GST-free export |
| Subscription revenue | LemonSqueezy | Assessable income, GST-free export (overseas) |
| Affiliate commissions | Amazon, ShareASale | Assessable income when received |
| YouTube AdSense | Google | Assessable income, foreign source |
| Streaming royalties | Spotify, Apple Music | Assessable income, withholding tax may apply |
| Platform creator revenue | Character.ai | Assessable income, foreign source |
| Prediction market winnings | Polymarket | Complex — see crypto/gambling section below |
| Domain flipping profits | Sedo, Flippa | Capital gains (if held as investment) or income (if trading) |

### GST — Goods and Services Tax

**Key Rules**
- Registration threshold: $75,000 AUD annual turnover
- Rate: 10% on taxable supplies in Australia
- Registered businesses charge GST to Australian customers
- Exports are GST-free (zero-rated)

**Digital Products Exported Overseas — GST-Free**
All Gumroad, Etsy, LemonSqueezy sales to overseas customers: GST-free. The platforms collect and remit overseas GST under their own obligations. Anthony's obligation is only for Australian sales.

**BAS Lodgement**
- Quarterly: 28 Oct, 28 Feb, 28 Apr, 28 Jul
- Monthly (if turnover >$20M — not applicable yet)
- Annual (if turnover <$75K — pre-registration)

**Input Tax Credits**
Claim GST on business expenses:
- Server costs (VPS hosting)
- Anthropic API credits
- Software subscriptions (n8n, tools)
- Domain registration
- Home office proportion of internet, electricity
- Business equipment

### Platform Income — Specific Rules

**Gumroad**
- US-based platform. Gumroad pays to your bank account (USD or AUD).
- ATO requires reporting all income including USD converted at RBA daily exchange rate.
- Gumroad issues 1099 for US tax — irrelevant for Australian resident, report in Australian return.
- No W-8BEN needed for Australian businesses (not US persons).

**Etsy**
- US marketplace. Income assessable in Australia.
- Etsy collects and remits GST for Australian sales (since July 2017 marketplace rules).
- Anthony only responsible for GST on sales made outside the marketplace (own website).
- Keep records of all Etsy income and fees (deductible).

**LemonSqueezy**
- US payment processor. SaaS/subscription revenue.
- Australian source rules: income has Australian source because Anthony performs the service in Australia.
- LemonSqueezy handles EU VAT and other indirect taxes — not Anthony's concern.

**Amazon Associates / Affiliate Programs**
- Commission income: assessable when received.
- US withholding tax: Amazon may withhold 30% if no tax form submitted. Submit W-8BEN to claim treaty rate of 0% (Australia-US DTA).
- File W-8BEN with each US affiliate program to avoid withholding.

**YouTube AdSense**
- Google pays to Australian bank account.
- Submit W-8BEN to Google to claim 0% US withholding under Australia-US DTA.
- Income assessable in Australia at marginal rate.

### Capital Gains Tax (CGT)

**50% CGT Discount**
Assets held >12 months: only 50% of net capital gain included in taxable income.

**Domain Names**
- Held as investment asset: CGT applies on sale.
- Held as trading stock (regular buying/selling): ordinary income treatment.
- domain-flipping venture: likely trading — income treatment, no 50% discount.

**Crypto (Bitcoin, Ethereum)**
- Every disposal is a CGT event (including trading crypto-to-crypto).
- 50% discount applies if held >12 months.
- DeFi staking income: ordinary income when received (ATO TD 2014/26 principles).
- Records required: date acquired, cost base, date disposed, proceeds — every transaction.

**Polymarket**
- If domiciled as a wagering platform: winnings may be non-assessable (gambling winnings not income).
- If domiciled as a financial product: gains are CGT events.
- ATO has not issued definitive guidance. Conservative approach: treat as assessable income.
- Consult Eleanor per-trade for advice above $5,000.

### Business Expenses — Deductibility

**Fully Deductible (empire operations)**
- VPS server hosting: 100%
- Anthropic API costs: 100%
- n8n, domain purchases for business: 100%
- Gumroad, Etsy, LemonSqueezy platform fees: 100%
- Business bank account fees: 100%
- Accounting and legal fees for business: 100%
- Skill/training costs directly related to empire: 100%

**Partially Deductible**
- Home office: calculate work area % of total home area × electricity, internet, rent
- Phone: work use % (log 4 consecutive weeks to establish pattern)
- Car: cents-per-km or logbook method if visiting clients/suppliers

**Not Deductible**
- Personal living expenses
- Capital assets (depreciate instead)
- Fines and penalties

### Trust Accounting

**Discretionary Family Trust — Tax Rules**
- Trust itself pays no tax if income is distributed to beneficiaries each year
- Trustee resolution required before 30 June each year — distribute income
- Beneficiary pays tax at their marginal rate
- $18,200 tax-free threshold per beneficiary — useful for splitting income
- Franked dividends can flow through trust with full imputation credit benefit
- Losses do NOT flow out to beneficiaries — stay trapped in trust

**Trust Income Streaming**
- Can stream capital gains to specific beneficiaries (to use their CGT discounts)
- Can stream franked income to beneficiaries who can best use franking credits
- Must comply with trust deed and streaming provisions of ITAA 1997

## Compliance Calendar

| Date | Action |
|------|--------|
| 28 October | Q1 BAS (Jul-Sep) |
| 28 February | Q2 BAS (Oct-Dec) |
| 28 April | Q3 BAS (Jan-Mar) |
| 28 July | Q4 BAS (Apr-Jun) |
| 31 October | Income tax return (individual) |
| 21 May | FBT return (if applicable) |
| 30 June | Trust income distribution resolutions |
| 30 June | Super concessional contributions deadline |

## Output Format for Consultations

Eleanor delivers tax advice in this structure:
```
TAX ASSESSMENT — [Question/Topic]
Date: [date]
Requested by: [Manager/Anthony]

1. QUESTION
   [Exact question being answered]

2. RULING
   [Clear statement of correct tax treatment]

3. LEGISLATIVE BASIS
   [ATO reference, section of ITAA, or ATO ruling]

4. RECORD-KEEPING REQUIRED
   [What Anthony needs to keep]

5. ACTION REQUIRED
   Anthony: [Yes/No — specific action if yes]
   Eleanor follow-up: [Yes/No]

6. CONFIDENCE LEVEL: High / Medium / Low
   [Note if Low: recommend professional tax advice]
```
