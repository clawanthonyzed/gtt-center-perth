#!/bin/bash
# Queue the GTT Round 21 overnight tasks (10 jobs = 13 brief files, each at most 8,000 characters).
# Server copy: /opt/openclaw/overnight/r21/queue_all.sh   Brief files sit beside it.
# Usage: queue_all.sh [--dry-run] [--force]
#   --dry-run  checks every file and agent, prints the 13 commands, queues nothing, writes no log line
#   --force    run again although queued.flag exists (otherwise a second run is refused)
# Scheduled by: systemd-run --unit=gtt-r21-overnight --on-calendar='2026-10-26 22:00:00 Australia/Perth' /bin/bash /opt/openclaw/overnight/r21/queue_all.sh
# Nothing is sent or published: tasks are queued as drafts (the Publishing Shield trigger holds GTT results for Anthony's approval).

DIR=/opt/openclaw/overnight/r21
LOG="$DIR/queue.log"
FLAG="$DIR/queued.flag"
QUEUE=/opt/openclaw/orchestration/queue_task.py
VENTURE="GTT Center Perth"
MAXCHARS=8000
DRY=0
FORCE=0
for a in "$@"; do
  [ "$a" = "--dry-run" ] && DRY=1
  [ "$a" = "--force" ] && FORCE=1
done

# agent|brief file|task title
ROWS=(
"reed|R21-01.txt|R21-01 Lab questions and 3-year term sheet"
"reed|R21-02.txt|R21-02 GP survey and Path A and Path B waitlist test plan"
"grace|R21-03-p1.txt|R21-03 part 1 of 2 Midwife hiring pack: screening sheet and interview guide"
"grace|R21-03-p2.txt|R21-03 part 2 of 2 Midwife hiring pack: position description and contract outline"
"grace|R21-04.txt|R21-04 Role descriptions and weekly roster"
"grace|R21-06-p1.txt|R21-06 part 1 of 2 Booking flow, Path A and Path B"
"grace|R21-06-p2.txt|R21-06 part 2 of 2 Consent text"
"grace|R21-07.txt|R21-07 Test-morning procedure"
"grace|R21-08.txt|R21-08 Results line patch"
"grace|R21-09-p1.txt|R21-09 part 1 of 2 Architect brief: changes to the existing brief"
"grace|R21-09-p2.txt|R21-09 part 2 of 2 Architect brief: consult room needs and feel"
"grace|R21-10.txt|R21-10 Room licence, consumer guarantee wording and lease checklist"
"reed|R21-11.txt|R21-11 Payroll tax and workers compensation worksheet"
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
  for row in "${ROWS[@]}"; do
    IFS='|' read -r agent file title <<<"$row"
    n=$(wc -m < "$DIR/$file")
    printf 'python3 %s --agent %s --venture "%s" --title "%s" --brief-file %s/%s   # %s characters\n' \
      "$QUEUE" "$agent" "$VENTURE" "$title" "$DIR" "$file" "$n"
  done
  exit 0
fi

# 3. Refuse a second run
if [ -e "$FLAG" ] && [ "$FORCE" -ne 1 ]; then
  logline "REFUSED already queued (see $FLAG); use --force to run again"
  exit 1
fi

logline "START queueing ${#ROWS[@]} Round 21 tasks"
ok=0
fail=0
for row in "${ROWS[@]}"; do
  IFS='|' read -r agent file title <<<"$row"
  out=$(python3 "$QUEUE" --agent "$agent" --venture "$VENTURE" --title "$title" --brief-file "$DIR/$file" 2>&1)
  rc=$?
  if [ "$rc" -eq 0 ]; then
    ok=$((ok + 1))
    logline "QUEUED $file agent=$agent task=$out"
  else
    fail=$((fail + 1))
    logline "FAILED $file agent=$agent rc=$rc $(echo "$out" | tr '\n' ' ' | cut -c1-200)"
  fi
  sleep 2
done
logline "END queued=$ok failed=$fail"
[ "$ok" -gt 0 ] && date -u '+%Y-%m-%dT%H:%M:%SZ' > "$FLAG"
[ "$fail" -eq 0 ]
