> SUPERSEDED where it disagrees with docs/GTT-READ-FIRST.md (Round 25 integrity banner, 2026-10-27). Read that file first.

# Theodore R21, Part 1: Medicare figures checked against the official schedule

Date: 2026-10-26. Numbers come from [theodore_r21.py](theodore_r21.py) and [theodore_r21_results.json](theodore_r21_results.json). Tags: R repo, V official source opened today, E estimate, U unverified. General knowledge and desk research, not your personal documents. Verify before acting.

## 1. Answer first

| Figure | Status |
|---|---|
| Item 82105 fee A$38.75, benefit A$32.95 | **CONFIRMED** (V) |
| Item 66548 fee A$19.90, benefit A$16.95 | **CONFIRMED** (V) |
| Item 73928 fee A$5.95, benefit A$5.10 | **CONFIRMED as an item** (V) |
| Item 73938 fee A$7.95, benefit A$6.80 | **CONFIRMED as an item** (V) |
| Which collection item applies to GTT's phlebotomists | **NOT CONFIRMED** |
| That the lab fee of A$27.85 matches the collection item used for the A$55 rebate | **NOT CONFIRMED, and the repo is inconsistent** (section 4) |

## 2. The official pages (all opened 2026-10-26, Medicare Benefits Schedule Online on health.gov.au)

| Item | What it is | Schedule fee | 85% benefit | Fee last changed | URL |
|---|---|---|---|---|---|
| 82105 | Short antenatal attendance by a participating midwife, at least 10 minutes | A$38.75 | A$32.95 | **01-Jul-2026** | [page](https://www9.health.gov.au/mbs/fullDisplay.cfm?type=item&q=82105&qt=item) |
| 66548 | Oral glucose tolerance test in pregnancy (glucose given, at least 3 blood glucose readings) | A$19.90 | A$16.95 | 01-Jan-2013 | [page](https://www9.health.gov.au/mbs/fullDisplay.cfm?type=item&q=66548&qt=item) |
| 73928 | Patient episode initiation, specimen collected **in an approved collection centre** | A$5.95 | A$5.10 | 01-Jan-2013 | [page](https://www9.health.gov.au/mbs/fullDisplay.cfm?type=item&q=73928&qt=item) |
| 73938 | Patient episode initiation, specimen collected **by or on behalf of the treating practitioner** | A$7.95 | A$6.80 | 01-Jan-2013 | [page](https://www9.health.gov.au/mbs/fullDisplay.cfm?type=item&q=73938&qt=item) |

Current after the 1 July 2026 indexation: yes for 82105, the page shows the fee was updated on 01-Jul-2026 and A$38.75 is the new fee. The pathology fees show no 2026 change on their pages, so they are the current ones. The 82105 page also lists an Extended Medicare Safety Net cap of A$20.40, which is a different thing and is not used here.

Limit of this check: I read the pages through a web tool that summarises them, not by eye. Every benefit below was recomputed independently and matched, but Anthony should open the four links once.

## 3. The 85 percent working and the rounding rule

Rule (matches all four pages): take 85 percent of the schedule fee, and if it is not a multiple of 5 cents, round UP to the next 5 cents.

| Item | Fee x 0.85 | Rounded up to 5 cents | Page says |
|---|---|---|---|
| 82105 | A$32.9375 | A$32.95 | A$32.95 |
| 66548 | A$16.915 | A$16.95 | A$16.95 |
| 73928 | A$5.0575 | A$5.10 | A$5.10 |
| 73938 | A$6.7575 | A$6.80 | A$6.80 |

So the consult rebate of A$32.95 and the test rebate of A$16.95 are right.

## 4. The collection item problem

The lab fee line of A$27.85 equals A$19.90 (66548) plus **A$7.95 (73938)**. With 73928 it would be A$25.85. But the A$55.00 rebate uses 73928 (A$5.10). The repo mixes the two.

| Case | Lab fee | Lab rebate | Total rebate | Client cost, P1 / P2 | Lab fee line |
|---|---|---|---|---|---|
| Repo today (73928 benefit, A$27.85 fee) | A$27.85 | A$22.05 | A$55.00 | A$265.00 / A$315.00 | only valid if the lab simply charges A$27.85 |
| 73938 applies | A$27.85 | A$23.75 | **A$56.70** | **A$263.30 / A$313.30** | A$27.85 holds |
| 73928 applies, lab charges schedule fees | **A$25.85** | A$22.05 | A$55.00 | A$263.00 / A$313.00 (all-in A$318 / A$368) | A$27.85 falls to A$25.85 |

GTT's own money does not change in any case: GTT receives A$292.15 / A$342.15 and the lab is paid by the client. Only the client's rebate, her cost and the lab line move.

Which one applies: 73928 needs the collection to happen in an approved collection centre, which is a premises approval the lab holds under the Health Insurance Act. 73938 covers collection by or on behalf of the treating practitioner. GTT's lounge is not an approved collection centre unless the lab gets it approved. NOT CONFIRMED: the MBS pages do not say who may collect, and I found no official page that settles it for a lounge-based phlebotomist.

Also not confirmed: the 82105 item says "participating midwife". GTT's midwives must hold the Medicare participating status for the A$32.95 to be payable. Ask Catherine.

## 5. Exact question to put to AskMBS (do not email; Anthony sends it)

"A private pathology provider will run an oral glucose tolerance test in pregnancy (item 66548) at a wellness lounge in Perth that is not a hospital. The specimens are collected by phlebotomists employed by the lounge, with the request written by a participating midwife. The client pays the pathology provider and claims her own benefit. (1) Is the patient episode initiation item 73928 or 73938? (2) Must the lounge be an approved collection centre for 73928? (3) Can a participating midwife request item 66548? (4) For an outside request from the client's own doctor, is the benefit the same?"

## 6. What must change in the checkout wording

1. Keep "about" on every rebate. Show "about A$55 to A$57 back" until AskMBS answers, not a fixed A$55.00.
2. Show the client cost as "about A$265 or a little less", never "exactly".
3. Show the lab line as "lab fee about A$27.85, paid to the lab" and drop the exact figure if the lab sets its own price.
4. The collection part of the rebate reads "A$5.10 to A$6.80".
5. No change to the A$292.15 / A$342.15 GTT charge.

## QUESTIONS FOR ANTHONY

1. Do you want the checkout to say "about A$55 to A$57" until AskMBS replies? (a) yes, recommended; (b) keep "about A$55" because it is the safer low number; (c) wait.
2. Will the lab (PathWest or the other partner) treat the lounge as an approved collection centre? (a) ask the lab, recommended; (b) assume not; (c) skip.
3. Do you accept sending the AskMBS question yourself? (a) yes; (b) ask Catherine to word it more formally, recommended.

Regards.
