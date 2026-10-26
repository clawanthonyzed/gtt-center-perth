# Round 22 overnight: how the daily free-route quota is shared

- 28 brief files queue at 22:00 AWST at priority 7. The executor claims "order by priority desc, created_at", 2 a minute, so all 28 are claimed by about 22:14 AWST, ahead of the older priority 6 GTT "Suggested" drafts and the 46 Instagram triage cards (priority 5 and 6).
- Priority orders the CLAIMS, not each call. Once claimed, the 28 and the backlog all draw on the same free-route pool of about 50 calls a day (resets 08:00 AWST). About 37 were left today, so 28 first attempts leave about 9 for rework (each task may rework once automatically). Expect 28 to 40 calls.
- If the cap runs out, the free models return 429, the draft fails at the Proof-of-Done gate, and the card goes to failed. Nothing is lost and nothing is sent.
- overnight_requeue.py puts failed or stuck overnight cards back to pending (up to 4 tries, a card must have failed 20 or more minutes ago). Its cron is 02:05, 02:25 and 02:45 (through 05:45) SERVER time. Since the clocks went back on 2026-10-25 server time is CET (UTC+1), so the first retry is 09:05 AWST (after the 08:00 reset), not 08:05, and the last is 12:45 AWST. To restore 08:05, change the cron hours from 2-5 to 1-4.
- After 08:00 the new day's pool is shared again between the requeued Round 22 cards and whatever backlog is pending; priority 7 cards are claimed first, so Round 22 finishes before the backlog resumes.
- GTT drafts end as DRAFT (needs Anthony sign-off) cards through the Publishing Shield trigger.
