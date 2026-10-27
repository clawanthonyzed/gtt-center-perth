> SUPERSEDED where it disagrees with docs/GTT-READ-FIRST.md (Round 25 integrity banner, 2026-10-27). Read that file first.

> SUPERSEDED on Path B wording (Round 24, Anthony 2026-10-27): Path B is NOT limited. Ignore any cap, limit or roster-shrink wording below. See docs/GTT-READ-FIRST.md.

# Theodore R22, Part 1: Center of Truth regenerated, and Path B (outside referral) economics

Date: 2026-10-26. Numbers come from [theodore_r22.py](theodore_r22.py) and [theodore_r22_results.json](theodore_r22_results.json) (it extends the R21 calculator, which runs the repo's own model). Tags: R repo, V verified, E estimate, U unverified. General knowledge and desk research, not your personal documents. Verify before acting.

## READ-FIRST CHECK

- Venue manager: starts 06:30, Mon to Fri 06:30 to 15:00. 07:00 is the first draw.
- Path A = consult package (PREFERRED). Path B = outside referral (NOT preferred).
- Prices: Path A A$320 / A$370 shown, GTT charged A$292.15 / A$342.15. Path B A$300 / A$350 all in, GTT charged A$272.15 / A$322.15.
- Rebates: consult A$32.95 + lab A$22.05 = A$55.00; client cost on Path A A$265 / A$315.
- Midwives 08:00 to 16:00; first consult 08:15; 25 minute blocks to 10:30.
- Late: from the appointment time onwards; a consult may allow 5 to 10 minutes if the midwife can finish in the time left.
- Files checked: the old Center of Truth had the Path labels the wrong way round and banned A$300/A$350. GTT-READ-FIRST.md wins; the Center of Truth is now regenerated to match.

## 1. Job 1: the Center of Truth is regenerated

Files written by the script: [FINANCIAL-CENTER-OF-TRUTH.md](../../FINANCIAL-CENTER-OF-TRUTH.md) and [center_of_truth.yml](center_of_truth.yml).

| Check | Result |
|---|---|
| Profit before company tax | **A$26,631.97 (unchanged, R)** |
| Profit after company tax | **A$19,973.98 (unchanged, R)** |
| Script has an assert on both numbers | Yes, it stops if either moves |
| Venue manager label fixed | Waterfall and P&L now say 06:30 to 15:00 |
| Venue manager combined cost | Repo base (07:00 start) A$8,004.48 + extra half hour A$500.28 = **A$8,504.76 a month** loaded (R, checked in the script) = A$17.94 a client |
| Rebate lock table | Added (Section 1A of the Center of Truth) |
| Paths renamed | Path A = consult package, Path B = outside referral, everywhere |
| Banned table | A$300/A$350/A$272.15/A$322.15 removed as plain bans (valid Path B figures). Added rows: one for the old venue manager start wording and four reversed-label rows |
| Checker tool | Two patterns added to [factcheck_locked_facts.py](../../../tools/factcheck_locked_facts.py): those four figures are flagged only when they sit beside the words 'Path A', and reversed path labels are flagged. It passes on the Center of Truth and on GTT-READ-FIRST.md |
| 'Not in any financial' list | Added (Section 6): interest, standalone consults, Package 2 take-up, retail, food and drink, gap-filling, card quotes, post-test discount, health lawyer cost |

### Rebate lock (every figure used for planning)

| Item | MBS item | Fee | Rebate | Status |
|---|---|---|---|---|
| Consult | 82105 | A$38.75 | A$32.95 | Confirmed (V) |
| Lab test | 66548 | A$19.90 | A$16.95 | Confirmed (V) |
| Collection | 73928 | A$5.95 | A$5.10 | Unresolved. 73938 is A$6.80 benefit, A$7.95 fee. AskMBS later |
| Lab rebate | | | A$22.05 | Locked for planning |
| **Total** | | | **A$55.00** | Locked, shown as 'about' |
| Client cost, Path A | | | A$265 / A$315 | Package 1 / Package 2 |

GTT's own money does not change either way, so this is closed.

## 2. Job 2: Path B economics (A$300 Package 1, A$350 Package 2, lab A$27.85 inside)

Whole GTT amount is taxable (no consult line), 1/11 is GST. Card fee 1.7 percent + A$0.30 (E).

| Per client | Path B P1 | Path B P2 |
|---|---|---|
| Client pays all in | A$300.00 | A$350.00 |
| Lab fee, paid to the lab | A$27.85 | A$27.85 |
| **GTT receives** | **A$272.15** | **A$322.15** |
| GST (1/11) | A$24.74 | A$29.29 |
| Card fee | A$4.93 | A$5.78 |
| **GTT keeps (ex GST, after card)** | **A$242.48** | **A$287.08** |

### Versus Path A, per client (Package 1; Package 2 gives the same gaps)

| | Path A keeps | Path B keeps | Path B minus Path A |
|---|---|---|---|
| Before any midwife cost | A$272.14 | A$242.48 | -A$29.66 |
| Midwife cost saved (roster flexes, A$31.31 a client) | A$240.83 | A$242.48 | **+A$1.65** |
| Midwife cost NOT saved (fixed roster, only A$3.00 consumables) | A$269.14 | A$242.48 | **-A$26.66** |

Plain reading: on Path B, GTT receives A$20.00 less than Path A, and the GST bill is higher by A$10.00 because the whole amount is taxable. Path B only breaks even if the midwife roster really shrinks when clients choose Path B. The A$31.31 includes room costs that do not shrink in practice, so treat the flex row as the best case (E).

### Break-even Path B price (all in, lab fee included)

| Compared with | Package 1 | Package 2 | Do A$300 / A$350 clear it? |
|---|---|---|---|
| Path A, midwife cost saved | A$298.15 | A$348.14 | **Yes**, by about A$1.85 |
| Path A, midwife cost NOT saved | A$329.88 | A$379.88 | **No**, short by about A$29.88 |
| Path A, if midwife cost were zero | A$333.24 | A$383.24 | No |

### Whole month if some clients are on Path B (ILLUSTRATION, Package 1, not a forecast)

| Share on Path B | Roster flexes: net after tax | vs headline | Roster fixed: net after tax | vs headline |
|---|---|---|---|---|
| 0 percent | A$19,973.98 | 0 | A$19,973.98 | 0 |
| 10 percent (47 clients) | A$20,032.63 | +A$58.65 | A$19,026.33 | -A$947.65 |
| 20 percent (95 clients) | A$20,091.28 | +A$117.30 | A$18,078.69 | -A$1,895.29 |

NOT IN REPO: what Medicare benefit a Path B client can claim herself (GTT-READ-FIRST.md says no benefit at GTT). It affects her cost, not GTT's money.

Regards.
