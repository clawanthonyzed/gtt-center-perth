# Category S glucose lab: costing against Route 1

General knowledge and desk research, not personal documents. Verify before acting. Prepared 2026-10-20 by Theodore (CFO role). Script: [theodore_categoryS.py](theodore_categoryS.py). Output: [theodore_categoryS_results.json](theodore_categoryS_results.json). All amounts are Australian dollars. Foreign prices converted at the RBA rate 1.4337 AUD per USD (fx_aud.json, 2026-10-19) and labelled.

## 1. The answer in one table

The lab does not pay for itself on glucose alone in any case. Medicare income at 18 clients a day is A$104,782 a year. The two people the rules require (a full-time specialist and an on-site clinical scientist) cost more than that before any equipment.

| | Low | Base | High |
|---|---|---|---|
| Set-up cost (capex plus pre-opening staff) | A$141,680 | A$262,156 | A$634,303 |
| Running cost, 12 months, 18 clients a day | A$350,862 | A$556,140 | A$906,970 |
| Medicare income, 12 months (A$22.05 x 18 x 264 days) | A$104,782 | A$104,782 | A$104,782 |
| Net result, 12 months | -A$246,080 | -A$451,359 | -A$802,188 |
| Break-even clients a day (running cost only) | 70.6 | 131.9 | 294.7 |
| Break-even with set-up cost spread over 5 years | 76.7 | 145.1 | 338.5 |
| Most fixed cost the lab can carry at 18 a day | A$84,134 | A$71,351 | A$52,177 |
| Months to recover set-up cost | never | never | never |

The repo caps GTT at 18 AM clients a day, so break-even at 71 to 339 a day is out of reach.

## 2. Route 1 against Category S (repo figures not altered)

Route 1: the partner lab runs the collection centre inside GTT. The repo model has no Medicare line for GTT, so GTT earns A$23,442.58 a month (A$281,310.96 a year) real profit after GST and before company tax. The partner lab keeps the A$22.05.

| GTT profit a year, before company tax | Low | Base | High |
|---|---|---|---|
| Route 1 (repo) | A$281,311 | A$281,311 | A$281,311 |
| Category S (repo profit plus lab net) | A$35,231 | -A$170,048 | -A$520,877 |
| Difference | -A$246,080 | -A$451,359 | -A$802,188 |

Extra funding needed on top of the repo peak of A$251,198 equals the set-up cost above. A lab loss reduces company tax by 25%, which softens the loss but does not remove it (company tax relief is not modelled in the table).

## 3. What the rules force GTT to buy

| Requirement | Source (from R9 file) | Cost line |
|---|---|---|
| Full-time designated person who is a specialist, not a pathologist | Supervision Requirements 8th ed S4.1 | Specialist retainer or salary |
| On-site Clinical Scientist in all normal working hours | C4.1(i) | Scientist plus leave cover |
| NATA assessment; report must name the same category and services | Services Australia APL page | NATA fees |
| APL application, Category S | ABLIS, 2025-26 | A$750 (verified) |
| ACC tax unless co-located with a GX or GY lab (S does not waive it) | HW035 | A$2,000 (verified) |
| APA application | HW011 | none found |
| Approved pathology practitioner must be a recognised specialist with a Medicare provider number | Services Australia APP page | Included in specialist cost |

## 4. Prices found, with sources

Label key: VERIFIED = government or published fee. ESTIMATE = a named source or my judgement, not a quote. QUOTE NEEDED = nothing usable published, my placeholder.

| Item | Low / Base / High | Status and source |
|---|---|---|
| (a) NATA application and first assessment | A$5,000 / 12,000 / 25,000 | QUOTE NEEDED. [NATA fees page](https://nata.com.au/accreditation/fees/) publishes no dollar amounts; contact annualfee@nata.com.au. My placeholders |
| NATA annual fee | A$3,500 / 6,000 / 12,000 | QUOTE NEEDED. Since 1 July 2024: per-site membership by size plus grouped service fee ([NATA fee model](https://nata.com.au/news/natas-new-fee-model-explained/)). Amount on member portal only |
| (b) APL application, Category S | A$750 | VERIFIED, [ABLIS](https://ablis.business.gov.au/service/ag/accredited-pathology-laboratories/86), 2025-26. 2026-27 not found |
| APA application fee | none found | No fee on HW011 or the APA page |
| ACC tax (HW035) | A$2,000 per 2-year approval | VERIFIED, form HW035 |
| (c) Analyser | A$10,055 / 25,000 / 57,348 | Low: refurbished YSI 2950D-1, resale listing about USD 6,985, converted (R9). Base: ESTIMATE, refurbished benchtop; a used cobas c 111 is listed at EUR 7,200 ex VAT ([Labexchange](https://shop.labexchange.com/en/roche-cobas-c-111.html)) before Australian freight, install and service. High: new mid-range benchtop, general price guide USD 30,000 to 80,000 ([medindexer](https://medindexer.com/knowledge/biochemistry-analyzers-price-estimate)), USD 40,000 converted. Refurbished Beckman AU480 listings range USD 7,000 to 45,095 ([Relink](https://relinkonline.com/products/beckman-coulter-au480-clinical-chemistry-analyzer)). No Australian list price found for Roche, Beckman, Abbott, Siemens, Mindray, Randox or Horiba. QUOTE NEEDED from each local distributor |
| Backup glucose meter | A$2,000 / 3,000 / 4,000 | ESTIMATE, Theodore |
| Centrifuge | A$2,000 / 3,500 / 6,000 | QUOTE NEEDED, my estimate |
| Pathology fridge and freezer | A$3,000 / 6,000 / 10,000 | QUOTE NEEDED, my estimate |
| Pipettes, loggers, small kit | A$2,000 / 3,000 / 5,000 | ESTIMATE |
| LIS software | Set-up A$3,000 / 8,000 / 25,000; yearly A$2,400 / 6,000 / 15,000 | QUOTE NEEDED. No price found |
| Analyser service contract | 5% / 8% / 10% of analyser price a year | ESTIMATE, Theodore |
| QC materials | A$1,500 / 2,500 / 4,000 a year | ESTIMATE |
| RCPAQAP proficiency program | A$2,500 / 4,000 / 7,000 a year | QUOTE NEEDED. [RCPAQAP chemical pathology](https://rcpaqap.com.au/products/chemical) shows no fee; phone +61 2 9045 6000 |
| Reagent per glucose test | A$0.10 / 0.30 / 0.60 | ESTIMATE. Listed hexokinase kits work out at about 0.05 to 0.30 a test, currency often unstated ([Horiba kit via Relink](https://relinkonline.com/products/horiba-instruments-inc-1220001667-reagent-general-chemistry)); not Australian. Three draws a client, plus 15% for calibration and QC |
| Tubes, glucose drink, other consumables per client | A$4 / 6 / 9 | ESTIMATE, Theodore |
| Biohazard waste | A$1,800 / 3,000 / 5,000 a year | QUOTE NEEDED |
| (d) Specialist (obstetrician) | A$150,000 / 250,000 / 450,000 a year | ESTIMATE. O&G permanent A$250,000 to 450,000, locum A$2,000 to 2,500 a day ([HCA Doctors via search](https://healthcareaustralia.com.au/?p=31070)); survey rate about A$179 an hour ([AusDoc, MABEL](https://www.ausdoc.com.au/specialist-update/how-do-ogs-earnings-stack-against-other-specialists)). The A$150,000 low case assumes a part-time arrangement the rules may not accept. No published lab medical director retainer found |
| Clinical scientist | A$100,000 / 135,000 / 158,894 salary | ESTIMATE. PathWest advertised Medical Scientist A$88,411 to 119,660; Scientist in Charge A$148,216 to 158,894 ([WA Health jobs](https://search.jobs.wa.gov.au/jobs/medical-scientist-perth-metropolitan-western-australia-australia-f53e0dcc-b4ef-40b8-95a4-82f16952b17b)). Plus 25% on-costs and 5 to 15% leave cover (my estimate) |
| Lab assistant | A$60,523 / 68,780 / 81,776 at 0.4 / 0.6 / 1.0 of a full-time job | ESTIMATE. Award entry rate about A$60,523 (Health Professionals Award, third-party pay site); PathWest collector A$68,780 to 81,776 (WA Health listing). Plus 25% on-costs. Collectors are already in the repo cost under both routes, so this is the bench assistant only |
| (e) Fit-out, 20 m2 | A$3,000 / 4,000 / 7,000 per m2 = A$60,000 / 80,000 / 140,000 | ESTIMATE. Medical fit-out A$1,500 to 3,500 per m2; lab fit-out A$4,000 to 7,000 per m2 ([Amicus Labline](https://www.amicus.com.au/insights/misconception-of-laboratory-construction-costs), vendor figure, 2023). No NPAAC-specific price found. QUOTE NEEDED |
| Compliance advice and NATA preparation | A$5,000 / 10,000 / 20,000 | ESTIMATE |
| (f) Insurance (professional indemnity, public liability, property) | A$4,000 / 8,000 / 18,000 a year | QUOTE NEEDED. Only a general small business public liability band of A$400 to 1,500 found ([Upcover](https://www.upcover.com/blog/public-liability-insurance-cost-australia)); a lab with diagnostic error risk sits well above it |
| Other fixed (calibration, courier, CPD, admin) | A$2,500 / 4,000 / 7,000 | ESTIMATE |

## 5. Base case running cost, 12 months

| Line | A$ |
|---|---|
| Specialist | 250,000 |
| Clinical scientist (with on-costs and leave cover) | 185,625 |
| Lab assistant | 51,585 |
| Staff total | 487,210 |
| Other fixed (NATA, RCPAQAP, QC, LIS, service, waste, insurance, other) | 35,500 |
| Fixed total | 522,710 |
| Variable A$7.04 a client x 4,752 clients | 33,430 |
| Running cost | 556,140 |

Base set-up: analyser 25,000; backup meter 3,000; centrifuge 3,500; fridge and freezer 6,000; small kit 3,000; LIS set-up 8,000; fit-out 80,000; compliance 10,000; NATA initial 12,000; APL 750; ACC tax 2,000; pre-opening staff 108,906 (specialist and scientist for 3 months before income, because Medicare is not backdated). Total A$262,156.

## 6. What would have to change for the lab to work

| Lever | Effect |
|---|---|
| Client gap A$3.80 collected on top of the benefit (A$25.85 a client, repo) | Base net improves to -A$433,301. Not enough |
| More clients through the same lab (non-pregnant item 66542 stream, not modelled in the repo) | Base net: 36 a day -A$380,007; 90 a day -A$165,954; 120 a day -A$47,035. Still negative, and the lounge cannot hold that volume |
| Specialist cost near zero | Only if the rules accept a salaried doctor already paid for other work. Even then the base ceiling of A$71,351 cannot cover scientist and assistant (A$237,210) |

## 7. Big unknowns, stated honestly

1. **Specialist retainer.** No published figure for a lab designated person. The rules say "full time" (S4.1). A part-time or shared specialist may be refused. This one line is 46% of base running cost and decides the result.
2. **Whether a glucose-only lab is Category S at all.** The Department and NATA view is not found (R9 unknown 5). The words fit, but nobody has confirmed it.
3. **Whether Category S can claim item 66548.** The MBS group heading for 66548 was not captured (R9 unknown 16, assumed general chemistry). If NATA scope or the Department does not cover it, Medicare income is zero.
4. **NATA time and cost.** Fee amounts are not published. R9 estimates 12 to 24 months to approval. Income cannot be backdated, so pre-opening carrying cost is real. This model counts only 2 to 6 months; at 12 to 24 months the loss is larger.
5. **Space.** The 20 m2 lab room comes out of the GTT lease. No rent is charged here. It is a real cost if that room could earn spa revenue.
6. **Scope risk.** NATA names the services in scope. Adding services later costs more.
7. **Medicare rate.** A$22.05 is the 85% benefit. Small changes cannot close a gap of A$250,000 or more.
8. **Depreciation and company tax** are not modelled.

## 8. Verdict

Route 1 stays the answer. Category S makes sense only as a later option if (a) a full-time specialist already employed elsewhere in the business accepts the designated-person role at little extra cost, (b) the Department confirms 66548 and the glucose-only scope in writing, and (c) volumes well beyond the repo figure of 18 a day appear. None of those is in the repo. To keep the option alive: ask NATA for a new-accreditation quote, ask two local distributors for analyser quotes, and ask the Department the Category S and 66548 questions (R9 draft letter question 8).

CORRECTION 2026-10-20 (Theodore): Services Australia APL application fees were abolished from 1 July 2025 (Catherine R10), so the A$750 line is A$0. Medicare income uses the repo day count (396 visits a month, 4,752 a year), not the 5,688 in Catherine's blueprint.
