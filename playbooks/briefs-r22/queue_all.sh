#!/bin/bash
# Queue the GTT Round 22 overnight tasks (28 brief files from 25 jobs, each at most 8,000 characters), priority 7.
# Server copy: /opt/openclaw/overnight/r22/queue_all.sh   Brief files sit beside it.
# Usage: queue_all.sh [--dry-run] [--force]
#   --dry-run  checks every file and agent, prints the 28 commands (agent, priority, characters), queues nothing, writes no log line
#   --force    run again although queued.flag exists (otherwise a second run is refused)
# Scheduled by: systemd-run --unit=gtt-r22-overnight --on-calendar='2026-10-26 22:00:00 Australia/Perth' /bin/bash /opt/openclaw/overnight/r22/queue_all.sh
# Replaces the Round 21 timer (gtt-r21-overnight). /opt/openclaw/overnight/r21/queue_all.sh now only hands over to this script.
# Priority 7 runs ahead of the old backlog (priority 5 and 6): the executor claims "order by priority desc, created_at".
# Nothing is sent or published: tasks are queued as drafts (the Publishing Shield trigger holds GTT results for Anthony's approval).

DIR=/opt/openclaw/overnight/r22
LOG="$DIR/queue.log"
FLAG="$DIR/queued.flag"
QUEUE=/opt/openclaw/orchestration/queue_task.py
VENTURE="GTT Center Perth"
PRIORITY=7
MAXCHARS=8000
DRY=0
FORCE=0
for a in "$@"; do
  [ "$a" = "--dry-run" ] && DRY=1
  [ "$a" = "--force" ] && FORCE=1
done

# agent|brief file|task title
ROWS=(
"reed|R22-01.txt|R22-01 Lab questions and 3-year term sheet"
"reed|R22-02.txt|R22-02 GP survey and Path A and Path B waitlist test plan"
"grace|R22-03-p1.txt|R22-03 part 1 of 2 Midwife hiring pack: screening sheet and interview guide"
"grace|R22-03-p2.txt|R22-03 part 2 of 2 Midwife hiring pack: position description and contract outline"
"grace|R22-04.txt|R22-04 Role descriptions and weekly roster"
"grace|R22-06-p1.txt|R22-06 part 1 of 2 Booking flow, Path A and Path B"
"grace|R22-06-p2.txt|R22-06 part 2 of 2 Consent text"
"grace|R22-07.txt|R22-07 Test-morning procedure"
"grace|R22-08.txt|R22-08 Results line patch"
"grace|R22-09-p1.txt|R22-09 part 1 of 2 Architect brief: changes to the existing brief"
"grace|R22-09-p2.txt|R22-09 part 2 of 2 Architect brief: consult room needs and feel"
"grace|R22-10.txt|R22-10 Room licence, consumer guarantee wording and lease checklist"
"reed|R22-11.txt|R22-11 Payroll tax and workers compensation worksheet"
"grace|R22-12.txt|R22-12 Welcome card final copy"
"grace|R22-13.txt|R22-13 Booking terms draft"
"grace|R22-14.txt|R22-14 Waitlist email set"
"grace|R22-15.txt|R22-15 Appointment reminder set, Path A and Path B"
"grace|R22-16.txt|R22-16 Abnormal results call, voicemail, email and text"
"grace|R22-17.txt|R22-17 Venue manager day-before print checklist"
"grace|R22-18.txt|R22-18 Client FAQ page text"
"grace|R22-19.txt|R22-19 Opening and closing checklists"
"grace|R22-20.txt|R22-20 Staff induction one-pager"
"grace|R22-21.txt|R22-21 Test-morning run sheet"
"reed|R22-22.txt|R22-22 Records system vendor question list (draft, nothing sent)"
"grace|R22-23.txt|R22-23 Path B Medicare notice set"
"grace|R22-24.txt|R22-24 Venue manager late and illness decision guide"
"grace|R22-25.txt|R22-25 Midwife pre-start checklist and consult note layout"
"grace|R22-26.txt|R22-26 Staff privacy one-pager"
)

stamp() { TZ=Australia/Perth date '+%Y-%m-%d %H:%M:%S AWST'; }
logline() { echo "$(stamp) | $*" | tee -a "$LOG"; }

cd "$DIR" || { echo "no $DIR"; exit 2; }

# 1. Pre-checks on every row before anything is queued (all or nothing)
bad=0
for row in "${ROWS[@]}"; do
  IFS='|' read -r agent file title <<<"$row"
  if [ ! -f "$DIR/$file" ]; then echo "MISSING FILE $file"; bad=1; continue; fi
  n=$(wc -m < "$DIR/$file")
  if [ "$n" -gt "$MAXCHARS" ]; then echo "OVER $MAXCHARS CHARACTERS: $file ($n)"; bad=1; fi
  if ! head -1 "$DIR/$file" | grep -q '^OVERNIGHT_SLUG: '; then echo "NO OVERNIGHT_SLUG LINE: $file"; bad=1; fi
  if [ ! -f "/root/.claude/agents/$agent.md" ]; then echo "NO AGENT FILE: $agent"; bad=1; fi
done
if [ "$bad" -ne 0 ]; then
  [ "$DRY" -eq 0 ] && logline "ABORT pre-check failed, nothing queued"
  exit 1
fi

# 2. Dry run: print the commands only
if [ "$DRY" -eq 1 ]; then
  echo "DRY RUN: ${#ROWS[@]} commands, nothing queued"
  i=0
  for row in "${ROWS[@]}"; do
    i=$((i + 1))
    IFS='|' read -r agent file title <<<"$row"
    n=$(wc -m < "$DIR/$file")
    printf '%02d python3 %s --agent %s --venture "%s" --title "%s" --brief-file %s/%s --priority %s   # %s characters\n' \
      "$i" "$QUEUE" "$agent" "$VENTURE" "$title" "$DIR" "$file" "$PRIORITY" "$n"
  done
  exit 0
fi

# 3. Refuse a second run
if [ -e "$FLAG" ] && [ "$FORCE" -ne 1 ]; then
  logline "REFUSED already queued (see $FLAG); use --force to run again"
  exit 1
fi

logline "START queueing ${#ROWS[@]} Round 22 tasks at priority $PRIORITY"
ok=0
fail=0
for row in "${ROWS[@]}"; do
  IFS='|' read -r agent file title <<<"$row"
  out=$(python3 "$QUEUE" --agent "$agent" --venture "$VENTURE" --title "$title" --brief-file "$DIR/$file" --priority "$PRIORITY" 2>&1)
  rc=$?
  if [ "$rc" -eq 0 ]; then
    ok=$((ok + 1))
    logline "QUEUED $file agent=$agent priority=$PRIORITY task=$out"
  else
    fail=$((fail + 1))
    logline "FAILED $file agent=$agent rc=$rc $(echo "$out" | tr '\n' ' ' | cut -c1-200)"
  fi
  sleep 2
done
logline "END queued=$ok failed=$fail"
[ "$ok" -gt 0 ] && date -u '+%Y-%m-%dT%H:%M:%SZ' > "$FLAG"
[ "$fail" -eq 0 ]
