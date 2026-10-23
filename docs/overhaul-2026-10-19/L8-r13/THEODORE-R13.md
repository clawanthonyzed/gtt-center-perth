# Round 13 (Theodore): lowest-category lab refresh and midwife revenue model

General knowledge and desk research, not personal documents. Verify before acting. Prepared 2026-10-23 by Theodore. The model is a plan, not a forecast. Script: [theodore_r13.py](theodore_r13.py). Output: [theodore_r13_results.json](theodore_r13_results.json). All amounts are Australian dollars.

Labels: VERIFIED = read from an official page this round. ESTIMATE = my judgement or a named general source. QUOTE NEEDED = no published price, my placeholder.

Basis (repo, unchanged): 07:00 start, 2 chairs, 25 minute pair cadence, 18 clients a day, 22 days a month = 396 visits a month, 4,752 a year. Repo net A$35,186.40 a month (no GST line). After GST the repo figure is A$23,442.58. Fee 66548 A$19.90, benefit A$16.95. Collection 73928 A$5.95, benefit A$5.10. Rent uses the repo rate A$40 per sqm per month.

Catherine's file r13/catherine-r13.md did not exist when I finished, so I assumed Category S as Round 10 did. If her file names a lower category, the lab table needs one more pass.

## Part 1. Category S lab, refreshed

### 1.1 The answer in one table

The lab still cannot pay for itself on glucose alone. Medicare income at 18 a day is A$104,782 a year (A$22.05 x 4,752).

| | Low | Base | High |
|---|---|---|---|
| Set-up cost, including staff paid before income | A$140,367 | A$370,312 | A$838,156 |
| Running cost, 12 months | A$357,822 | A$568,140 | A$923,770 |
| Medicare income, 12 months | A$104,782 | A$104,782 | A$104,782 |
| Net, 12 months | -A$253,040 | -A$463,359 | -A$818,988 |
| Break-even clients a day, running cost only | 72.1 | 134.9 | 300.5 |
| Break-even clients a day, set-up spread over 5 years | 78.1 | 153.6 | 358.4 |
| Most fixed cost the lab can carry at 18 a day | A$84,134 | A$71,351 | A$52,177 |
| Months to NATA approval (ESTIMATE, R9 says 12 to 24) | 12 | 18 | 24 |
| Net a year if the specialist cost were zero | -A$103,040 | -A$213,359 | -A$368,988 |

Against paying a partner lab: the partner lab keeps the A$22.05, so GTT earns A$0 from Medicare and carries none of these costs. Owning the lab costs GTT A$253,040 to A$818,988 a year more than the partner route, plus A$140,367 to A$838,156 up front. The repo cap of 18 a day makes break-even at 72 to 358 a day unreachable. Volume sensitivity (base): 36 a day -A$392,007; 60 -A$296,872; 90 -A$177,954; 120 -A$59,035. Still negative.

### 1.2 What changed since Round 10

| Change | Effect |
|---|---|
| APL application fee is now A$0. Fees for APA, APP and APL approvals were abolished from 1 July 2025 (Act repealed, commenced 5 Sep 2025; old fees A$500 to 2,500) | VERIFIED, [Department of Health update](https://www.health.gov.au/sites/default/files/2025-09/budget-2024-25-reforming-pathology-application-charging-arrangements-implementation-update.pdf). Saves A$750 |
| Lab room now carries rent at the repo rate (12 / 20 / 25 sqm x A$40 x 12) | A$5,760 / 9,600 / 12,000 a year. Round 10 charged none. The repo itself says its rent line may be understated |
| Fit-out space 12 / 20 / 25 sqm (was 20 in all cases) | ESTIMATE |
| Time to approval 12 / 18 / 24 months, with specialist and scientist carried 3 / 6 / 9 months before income (was 2 / 3 / 6) | ESTIMATE. Medicare is not backdated. Main reason set-up rose |
| Courier added A$1,200 / 2,400 / 4,800 a year | ESTIMATE |
| Consultancy and NATA preparation | A$5,000 / 10,000 / 20,000, ESTIMATE |

### 1.3 Set-up and running lines

| Line | Low / Base / High | Label and source |
|---|---|---|
| Analyser, refurbished to new | A$10,055 / 25,000 / 57,348 | ESTIMATE. Used cobas c 111 listed EUR 7,200 ex VAT on [Labexchange](https://shop.labexchange.com/en/roche-cobas-c-111.html); new mid-range USD 30,000 to 80,000 on [medindexer](https://medindexer.com/knowledge/biochemistry-analyzers-price-estimate), USD 40,000 converted at RBA 1.4337. QUOTE NEEDED from local distributors |
| Centrifuge | A$2,000 / 3,500 / 6,000 | QUOTE NEEDED |
| Fridge and freezer with temperature logging | A$3,000 / 6,000 / 10,000 | QUOTE NEEDED |
| Backup meter, pipettes, loggers, small kit | A$4,000 / 6,000 / 9,000 | ESTIMATE |
| Bench fit-out | A$36,000 / 80,000 / 175,000 | ESTIMATE. A$3,000 / 4,000 / 7,000 per sqm; lab fit-out A$4,000 to 7,000 per sqm on [Amicus](https://www.amicus.com.au/insights/misconception-of-laboratory-construction-costs) (vendor figure, 2023) |
| LIS software | Set-up A$3,000 / 8,000 / 25,000; yearly A$2,400 / 6,000 / 15,000 | QUOTE NEEDED |
| NATA application and first assessment | A$5,000 / 12,000 / 25,000 | QUOTE NEEDED. [NATA fees page](https://nata.com.au/accreditation/fees/) gives no amounts |
| NATA annual fee | A$3,500 / 6,000 / 12,000 | QUOTE NEEDED. [NATA fee model](https://nata.com.au/news/natas-new-fee-model-explained/): per-site membership plus grouped service fee |
| ACC tax (HW035) | A$2,000 per 2 years | VERIFIED in R10 |
| QC materials / proficiency (RCPAQAP) | A$1,500 / 2,500 / 4,000 and A$2,500 / 4,000 / 7,000 a year | ESTIMATE / QUOTE NEEDED |
| Analyser service contract | 5% / 8% / 10% of analyser price a year | ESTIMATE |
| Reagent per glucose test | A$0.10 / 0.30 / 0.60 (x 3 draws x 1.15) | ESTIMATE |
| Tubes, drink, other per client | A$4 / 6 / 9 | ESTIMATE |
| Waste, insurance, other fixed | A$1,800 / 3,000 / 5,000; A$4,000 / 8,000 / 18,000; A$2,500 / 4,000 / 7,000 a year | QUOTE NEEDED / ESTIMATE |
| Supervising specialist retainer | A$150,000 / 250,000 / 450,000 a year | ESTIMATE. Obstetrician pay ranges from a recruiter page; low case may fail the "full time" rule. No published lab-director retainer found |
| Scientist | A$100,000 / 135,000 / 158,894 salary, x1.25 on-costs, plus 5 / 10 / 15% leave cover | ESTIMATE. PathWest advertised A$88,411 to 158,894 (R10) |
| Bench assistant | A$60,523 / 68,780 / 81,776 at 0.4 / 0.6 / 1.0 FTE | ESTIMATE |

Staff cost a year: A$311,512 / 487,210 / 780,630. That one block is 87% to 85% of running cost and is why the lab fails.

### 1.4 Verdict on Part 1

Stay with the partner lab. A GTT-owned lab loses at least A$253,040 a year even on the cheapest settings, and A$103,040 even if the specialist cost nothing. Unknowns that could change this: whether a glucose-only lab is Category S at all, whether Category S can claim 66548, the specialist retainer, and NATA quotes. All are listed in the Round 10 file.

## Part 2. Midwife revenue model

### 2.1 MBS items for participating midwives (VERIFIED on [MBS Online](https://www9.health.gov.au/mbs/), item pages read 2026-10-23)

I read these through a page summariser. The item text was returned verbatim, but 82110 and 82100 both showing A$89.00 and the postnatal fees being higher than the antenatal ones look odd, so re-check each fee on MBS Online before relying on it. The 85% arithmetic checks out for every item.

| Item | Service | Fee | Benefit 85% | Limits |
|---|---|---|---|---|
| 82100 | Initial antenatal, at least 60 min | A$89.00 | A$75.65 | Once per pregnancy. No telehealth version |
| 82105 | Short antenatal, at least 10 min | A$38.75 | A$32.95 | Video version exists |
| 82110 | Routine antenatal, at least 40 min | A$89.00 | A$75.65 | No cap on number, clinically relevant only. Video 91212 same fee, phone 91219 |
| 82115 | Maternity care plan, at least 90 min, past 28 weeks | A$381.75 | A$324.50 | Once per pregnancy. Needs 2 antenatal visits with this midwife in the past 6 months. Midwife intends to stay primary carer. Not payable if 16590 or 16591 was claimed |
| 82130 | Short postnatal, at least 20 min, within 6 weeks | A$63.90 | A$54.35 | No cap, clinically relevant only |
| 82135 | Routine postnatal, at least 40 min, within 6 weeks | A$130.80 | A$111.20 | Same |
| 82120, 82125 | Labour management in hospital, 6 to 12 hours | A$1,803.35 | 75%: A$1,352.55 | Hospital only. Out of scope for GTT |

Rules common to all: the midwife must do the service personally; no group sessions; no lactation consultant services; no goods in the fee; not payable where a government already funds the service; one patient at a time. Settings allowed: home, midwifery group practice, the midwife's rooms, or a medical practice.

Who counts as a participating midwife (VERIFIED, [Services Australia](https://www.servicesaustralia.gov.au/mbs-billing-rules-for-eligible-midwife-items)): a registered midwife with the scheduled medicines endorsement, working in private practice (or an exempt public facility), with a Medicare provider number for each practice location (form HW088). The Australian College of Midwives describes the endorsement as a postgraduate prescribing program plus 5,000 hours of practice (ESTIMATE, secondary source; the college itself wants the hours removed, so check the current standard).

Collaborative arrangement: Catherine's R12 file lists it as needed. The Department of Health says the legal requirement was removed from 1 November 2024 ([Collaborative arrangements](https://www.health.gov.au/our-work/collaborative-arrangements)). I flag this to Catherine to correct. VERIFIED on the Department page, not re-read in the Act.

### 2.2 Prices

| Item | Finding | Label |
|---|---|---|
| Perth private midwife fee | No published Perth price found. A 2023 [Medical Forum article](https://www.mforum.com.au/posts/more-pain-for-maternity-services) says Perth bulk-billing midwife practices were moving off bulk billing because rebates were too low | NOT VERIFIED. The private cases below assume fee = schedule fee, or 130% of it (the 130% is my placeholder, not a benchmark) |
| Medicare patient rebate | 85% of the schedule fee, so a private client at schedule fee gets A$60.72 back on the base mix | VERIFIED arithmetic |

### 2.3 Award wages (VERIFIED: [Fair Work Pay Guide, Nurses Award 2020 MA000034, from 1 Jul 2026](https://calculate.fairwork.gov.au/payguides/pact/MA000034/20260701))

| Classification | Ordinary hour | Saturday (150%) | Casual ordinary | Casual Saturday |
|---|---|---|---|---|
| Registered nurse L1 pay point 1 | A$32.09 | A$48.14 | A$40.11 | A$60.17 |
| Registered nurse L2 pay point 1 | A$39.59 | A$59.39 | A$49.49 | A$74.24 |
| Registered nurse L2 pay point 4 | A$41.59 | A$62.39 | A$51.99 | A$77.99 |
| Registered nurse L3 pay point 1 | A$42.93 | A$64.40 | A$53.66 | A$80.49 |
| Nurse practitioner, 1st year | A$49.39 | A$74.09 | A$61.74 | A$92.61 |
| Nurse practitioner, 2nd year | A$50.86 | A$76.29 | A$63.58 | A$95.37 |

The Award does not name "endorsed midwife". I mapped her to RN level 2 or 3 (ESTIMATE). Super 12% (VERIFIED, current guarantee rate). Workers compensation 1.7% (repo figure). Base on-cost x1.20 includes leave (ESTIMATE). Cost per paid hour including Saturday mix and on-costs: low A$45.01, base A$54.07, high A$71.18 (casual L3). A registered nurse who is not a participating midwife or nurse practitioner cannot bill these items or request pathology (general knowledge, Catherine to confirm).

Cost ranking per hour, ordinary rate: RN A$41.59 < NP A$49.39. The midwife costs about 16% less than the NP at the same experience.

### 2.4 Midwife cost lines (a month unless stated)

| Line | Low / Base / High | Label |
|---|---|---|
| AHPRA registration | A$193 a year | VERIFIED, [NMBA 2026/27](https://www.nursingmidwiferyboard.gov.au/News/2026-04-07-Registration-renewal-opens). One fee covers dual nurse and midwife |
| Professional indemnity | A$1,200 / 2,500 / 4,500 a year | QUOTE NEEDED. Commonwealth-subsidised MIGA Midwifery Practice Insurance Scheme exists for endorsed midwives; no premium published ([MIGA wording](https://www.miga.com.au/MIGA/media/MIGA/Policy%20Documents/2024-midwives-policy-wording.pdf)) |
| Medicare provider number | No fee found | ESTIMATE. Form HW088 shows none; not confirmed |
| CPD | A$300 / 600 / 1,200 a year | ESTIMATE |
| Billing and records software | A$80 / 120 / 200 | ESTIMATE |
| Consult equipment (fetal doppler, BP, scales, couch, tape, urine tests) | A$2,500 / 4,500 / 8,000, spread over 5 years | ESTIMATE |
| Consumables per consult | A$1.50 / 3 / 5 | ESTIMATE |
| Clinical room, 12 sqm at repo A$40 | A$0 / 240 / 480 | Repo rate. Low assumes an existing room is free outside peak |
| Idle time (utilisation) | 80% / 70% / 60% billable | ESTIMATE |

Fixed cost a month: A$262.75 / 709.42 / 1,304.42 (these include the room share).

### 2.5 Weekly and monthly P&L, base cost case

Revenue per consult (base mix: 12% initial, 25% short, 43% routine, 20% short postnatal; average 30.9 minutes): bulk billed A$60.72; private at schedule fee A$71.42; private with 30% gap A$92.84; mixed 50/50 bulk and gap A$76.78. Paid hours a week include the idle time.

| Consults a week | Paid hours a week | Bulk billed, net a week / month | Private at schedule, net a week / month | Private + 30% gap, net a week / month | Mixed, net a week / month |
|---|---|---|---|---|---|
| 10 | 7.4 | A$15.65 / A$67.83 | A$122.68 / A$531.60 | A$336.93 / A$1,460.03 | A$176.29 / A$763.93 |
| 15 | 11.0 | A$105.33 / A$456.45 | A$265.87 / A$1,152.11 | A$587.25 / A$2,544.75 | A$346.29 / A$1,500.60 |
| 20 | 14.7 | A$195.02 / A$845.07 | A$409.07 / A$1,772.62 | A$837.57 / A$3,629.48 | A$516.29 / A$2,237.27 |

Low and high cost cases, monthly net, mixed pricing:

| Consults a week | Low cost | Base cost | High cost |
|---|---|---|---|
| 10 | A$1,743.64 | A$763.93 | -A$841.50 |
| 15 | A$2,746.83 | A$1,500.60 | -A$610.04 |
| 20 | A$3,750.02 | A$2,237.27 | -A$378.58 |

Low / base / high monthly net at 15 consults a week, by pricing:

| Pricing | Low | Base | High |
|---|---|---|---|
| Bulk billed | A$1,702.68 | A$456.45 | -A$1,654.19 |
| Private at schedule fee | A$2,398.34 | A$1,152.11 | -A$958.53 |
| Private + 30% gap | A$3,790.98 | A$2,544.75 | A$434.11 |

Break-even consults a week (base cost): bulk billed 10; private at schedule 6; private + gap 4; mixed 5. High cost case bulk billed never breaks even (A$71.18 an hour against A$60.72 a consult).

Effect on GTT total monthly net, repo basis A$35,186.40, base cost, mixed pricing: 10 a week A$35,950.33; 15 a week A$36,687.00; 20 a week A$37,423.67. The midwife adds roughly A$0.8k to A$2.2k a month, 2% to 6% of the baseline. It is not a profit engine. Its value is Medicare ordering authority.

### 2.6 Midwife as requester only (the Catherine R12 "B3" route)

The midwife genuinely assesses each client who has no usable request and issues the 66548 request. GTT's own collectors collect on her behalf. She bills the short antenatal 82105 (10 minutes) bulk billed at A$32.95, which pays for her time. Share of clients needing a GTT request is my assumption: 25% / 50% / 100% of 396 visits. Paid time per request 15 / 20 / 30 minutes (consult plus notes plus result follow up).

| | Low (25%) | Base (50%) | High (100%) |
|---|---|---|---|
| Requests a month | 99 | 198 | 396 |
| Paid hours a week (genuine minimum) | 5.7 | 15.2 | 45.7 |
| Clinical minutes in each morning (10 min each) | 45 | 90 | 180 |
| Net a month if she bills 82105 bulk billed | A$1,643.84 | A$1,652.20 | -A$3,323.17 |
| GTT total net a month (repo A$35,186.40 plus this) | A$36,830.24 | A$36,838.60 | A$31,863.23 |
| Net a month if she does not bill (cost only) | -A$1,618.21 | -A$4,871.90 | -A$16,371.37 |
| GTT total net a month, cost only | A$33,568.19 | A$30,314.50 | A$18,815.03 |

Reading it: about 6 to 15 paid hours a week is a believable genuine load for a quarter to half of clients, and it pays for itself when billed. At 100% it is a full-time job (46 hours) and 180 clinical minutes in a 210-minute morning, which is not workable in the window. Do not run it unbilled: it is a cost with no income and looks hollow to Medicare. Genuineness and the s 23DNL warning problem are Catherine's.

### 2.7 Collection benefit 73938 against 73928

| Item | Amount | Who earns it |
|---|---|---|
| 73928 collection at an approved collection centre | A$5.95 fee, A$5.10 benefit | The lab |
| 73938 collection on behalf of the treating practitioner | A$7.95 fee, A$6.80 benefit (VERIFIED by Catherine R12) | The lab claims it. GTT earns none |
| Client rebate with 66548 | A$22.05 on the ACC route; A$23.75 on the practitioner route | The client |
| Extra over 73928 if the lab passed it to GTT | A$1.70 a client = A$673.20 a month = A$8,078.40 a year | Excluded from every figure above. Pass-through is doubtful under Part IIBA |

### 2.8 GST in plain words

Health services such as midwife consults are GST-free, so GTT adds no GST to the consult fee and can still claim back GST on what it buys for that service (general knowledge, GST Act s 38-10; Catherine to confirm midwives are on the list). Hospitality (lounge, treatments) stays taxable as the repo already treats it. Pathology is GST-free. So the midwife net adds to both the repo basis and the after-GST basis without a GST line.

### 2.9 Lowest-cost qualification that satisfies Medicare ordering authority

| Route | What I can verify | Cost view |
|---|---|---|
| Hire an existing participating (endorsed) midwife | Services Australia: registered midwife with scheduled medicines endorsement, private practice, provider number. Catherine R12 verified that participating midwives may request 66548 | Cheapest in wages: A$41.59 an hour Award rate. Training one yourself is not priced (no fee found) |
| Hire a nurse practitioner | On Catherine's list of requesters | A$49.39 an hour, about 19% above the midwife |
| Doctor (GP or obstetrician) | General knowledge only | No Award rate; market rate not priced |
| Registered nurse | Cannot bill these items or request pathology (general knowledge) | Not an option alone |

Legal points deferred to Catherine: the corrected collaborative arrangement rule, whether GTT may employ the midwife and receive her Medicare payments, genuine treating relationship, s 23DNL, Part IIBA.

## Assumptions list

1. Category S assumed (no r13 file from Catherine). 2. Repo basis: 396 visits a month, 18 a day, A$35,186.40 a month, rent A$40 per sqm. 3. All lab prices are R10 estimates unless marked VERIFIED. 4. Time to approval 12 / 18 / 24 months. 5. Midwife awarded RN L2 or L3; on-cost 1.14 / 1.20 / 1.14 (casual). 6. Consult mix as stated, average 30.9 minutes. 7. Private fee at 100% or 130% of schedule fee (no Perth benchmark found). 8. 73938 stays with the lab. 9. No company tax, payroll tax or depreciation modelled. 10. MBS fees read via a page summariser, re-check on MBS Online.

## Open items for others

1. Catherine: collaborative arrangement was removed 1 Nov 2024, her R12 text says it is needed. 2. Quotes still needed: NATA, analysers, LIS, fridge, indemnity premium. 3. Perth midwife fee benchmark: ring two Perth practices.
