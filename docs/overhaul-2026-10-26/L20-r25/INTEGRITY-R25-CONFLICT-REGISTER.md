# INTEGRITY R25 CONFLICT REGISTER (part 1 of 2): repo files

## READ-FIRST CHECK
- Venue manager starts 06:30. The first draw is 07:00. Anthony is owner and director, 0 operational hours.
- Path A = package WITH the GTT midwife consult (preferred, A$320 / A$370 shown, GTT charge A$292.15 / A$342.15). Path B = outside referral, no GTT consult (not preferred, A$300 / A$350, GTT charge A$272.15 / A$322.15). Path B is not limited.
- Rebates used: consult A$32.95 + lab A$22.05 = A$55.00. Midwives 08:00 to 16:00, first consult 08:15.
- Late: draws no wiggle room, consults 10 minute grace. GTT-READ-FIRST.md wins over every file below.

## How the scan was done
`factcheck_locked_facts.py` over docs/*.md, docs subfolders (not archive, not overhaul-2026-10-1x), playbooks, outputs, CLAUDE.md and every round folder L15 to L19, plus my own greps for trust, Path B limits, Draft D, Lounge phlebotomists, recalled midwives, 5 hour shift, grace 5 to 10, separate groups, rebates, 12 minute, the word mother. Em dash hits (thousands, all old) are not counted as conflicts. Result: 336 line-level hits in 77 files from the tool, plus 10 more found by hand. Legend: FIXED = line edited; BANNER = one-line "SUPERSEDED" banner added at the top, body left as history; OTHERS = file another window is changing, listed for you.

## Fixed (line edited)
| File | Stale value | Truth | Action |
|---|---|---|---|
| CLAUDE.md lines 9, 11 | Imara salary vs trust split; YETI Holding Trust income splitting | Three companies, no trust, Route B | FIXED |
| CLAUDE.md Standing Facts AM model | Packages A$250/A$300, 12 client Table 2 as a live option | Path A A$320/A$370, Path B A$300/A$350, 18 clients | FIXED (marked HISTORICAL) |
| CLAUDE.md Governance | CURRENT-STATE.md is "the single canonical source" | GTT-READ-FIRST.md then Center of Truth | FIXED |
| CLAUDE.md line 17 | dva-navigator-skill name | skill name only, not DVA content | factcheck:ok marker |
| outputs/GTT-CENTER-PERTH-VENTURE-OVERVIEW.md lines 19 to 23, 87 | YETI Holding Trust operating entity, corporate trustee, Anthony as trustee, revenue through trust | Holdings, Medical, Lounge; Anthony owner and director; Route B dividends | FIXED |
| outputs/FINANCIALS/ROUTE-B-CAPITAL-RETURN-MEMO.md line 12 | consult may allow 5 to 10 minutes (OPEN) | 10 minute grace, locked R24 | FIXED |
| same memo, paragraph (g) | MRCA / SRDP 10 hour analysis | DVA closed for GTT | FIXED | <!-- factcheck:ok -->
| docs/ITEMS-TO-CONFIRM.md ITC-06 | "Anthony, Venue Manager" | Anthony is owner; a hired venue manager | FIXED | <!-- factcheck:ok -->

## Banner added (body left as history), by type of stale content
| Stale content | Files |
|---|---|
| DVA / SRDP / MRCA content | docs/dva-tpi-research, review-audit, 00_document_inventory, research, venture-timeline, revenue-extraction-options, reading-order, executive-summary, 02_issues_and_risks, team-startup, financial-setup, 01_conflicts_log, CURRENT-STATE, VERIFICATION-TRACKER; outputs/PRESENTATION and FINANCIALS/ROUTE-B memo; architecture/ENTITY-STRUCTURE-INVESTIGATION, REPOSITORY-AUDIT, TARGET-ARCHITECTURE; reviews/ANTHONY-DIRECTIVE-2026-10-17; L17-r22 Catherine R22B parts 1, 2, 7, R22C-3, Grace R22-6, Theodore R22-3, R22C-2 | <!-- factcheck:ok -->
| Bulk billing talk | docs/pricing-billing-strategy, market-research-findings, capacity-pricing-audit, referral-partnership-plan, research, financial-break-even-staff, onboarding, website-spec, team-startup, reading-order, 00_document_inventory, VERIFICATION-TRACKER; outputs/PRESENTATION BUSINESS-PLAN and EXECUTIVE-PITCH-DECK, FINANCIALS/PROFIT-AND-LOSS and 3-WAY model; research/PATHOLOGY-OPERATIONS-DEEP-DIVE and four more | <!-- factcheck:ok -->
| Old profit A$35,186.40, old prices A$245/A$295/A$110/A$251 | docs/CURRENT-STATE, unit-economics, property-links, investor-memorandum, review-audit, feasibility; outputs/FINANCIALS (3 files), PRESENTATION (2), OPERATIONS/GTT-LAUNCH-READINESS-TRACKER; research/RENT-ECONOMICS-FORENSICS, STAFFING-FORENSICS, MODEL-BREAKPOINTS; presentations/imara-brief-content-brief-v2 | <!-- factcheck:ok -->
| Revenue ramp (43/64/79/93/100) | docs/VERIFICATION-TRACKER; outputs/FINANCIALS 3-WAY model; architecture/REVENUE-RAMP-METHODOLOGY, COST-RAMP-METHODOLOGY, FINANCIAL-MODEL-DECISION-REVIEW, COMMERCIAL-VALIDATION-FRAMEWORK, REVENUE-ASSUMPTION-AUDIT, MVP-OPENING-DECISION-REVIEW, CANONICAL-DATA-POC, AM-OPERATIONS-SENSITIVITY-MODEL; L17-r22 Theodore R22C-1 | <!-- factcheck:ok -->
| "hosts" (staff or venue wording, benign for most) | docs/reed-partnerships, workflow, pathology-partnership-brief, king-edward-start-time-constraint, gtt-test-reference, fairwork-infoline-query-script, pathwest-clinipath-outreach; architecture/WDP-PARTNERSHIP-ACTIVATION-PLAN and 3 more. Mostly the verb "hosts", so low risk. | <!-- factcheck:ok -->
| Reversed Path labels | L16-r21 Grace Booking Flow part 2, Grace Playbook Hooks |
| Venue manager 07:00 | L16-r21 Theodore R21 part 2 |
| Anthony as venue manager | L17-r22 Catherine R22B parts 1 and 2, R22C-3, Theodore R22-3 | <!-- factcheck:ok -->
| Whole round folders before the R23 locks | every .md in L15-r20, L16-r21, L17-r22 (45 files) |
Total files bannered in the repo: 120.

## Checked and found no conflict
Lounge employing phlebotomists (none), Path B limited (only the lock itself and the neutral A$26.66 line), Draft D (none outside the retired note), midwife recalled (only the R24 timesheet code rules, correct), 12 minute cadence (none), the bare parent word (only "expecting" plus the word, which is correct; two harmless family phrases in afternoon-marketing-plan, left), "PathWest/Clinipath not contacted" in docs/risk-register, scenario-d-demand-analysis, external-resources-and-advisors, team-meeting (these are about labs, not the four government bodies, so true). 5 hour phlebotomist shift: no phlebotomist 5 hour statement found (the 5 hour figures are for massage, nail, hair and beauty therapist sessions in financial-break-even-staff and pm-staffing-roster). Flag only: being re-derived. <!-- factcheck:ok -->
