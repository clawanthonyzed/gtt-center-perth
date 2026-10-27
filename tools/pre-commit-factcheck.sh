#!/bin/sh
# GTT pre-commit hook: blocks a commit that adds stale or conflicting facts.
# Install:  cp tools/pre-commit-factcheck.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
# Runs tools/factcheck_locked_facts.py over staged docs/*.md and playbooks files, looking only at the
# LINES YOU ADD in this commit (old history lines are not your fault). A line carrying the marker
# factcheck:ok is allowed. Bypass is not offered; fix the line or add the marker if it is a benign quote.
ROOT=$(git rev-parse --show-toplevel) || exit 0
cd "$ROOT" || exit 0
PY=python3; command -v python3 >/dev/null 2>&1 || PY=python
export PYTHONIOENCODING=utf-8
FILES=$(git diff --cached --name-only --diff-filter=AM | grep -E '^(docs/.*\.md|playbooks/.*)$' | grep -v -E '^docs/archive/')
[ -z "$FILES" ] && exit 0
BAD=0
TMP=$(mktemp -d 2>/dev/null || echo "${TMPDIR:-/tmp}/gttfc.$$"); mkdir -p "$TMP"
for f in $FILES; do
  # Added line numbers for this file in the staged diff
  ADDED=$(git diff --cached -U0 -- "$f" | sed -n 's/^@@ -[0-9,]* +\([0-9]*\),\{0,1\}\([0-9]*\) @@.*/\1 \2/p' | while read s n; do
    [ -z "$n" ] && n=1; i=0; while [ "$i" -lt "$n" ]; do echo $((s+i)); i=$((i+1)); done; done)
  [ -z "$ADDED" ] && continue
  mkdir -p "$TMP/$(dirname "$f")"
  git show ":$f" > "$TMP/$f"
  OUT=$(cd "$TMP" && "$PY" "$ROOT/tools/factcheck_locked_facts.py" "$f" 2>&1)
  [ $? -eq 2 ] && { echo "factcheck setup problem: $OUT"; continue; }
  HITS=$(echo "$OUT" | tr -d '\r' | sed -n "s#^$f:\([0-9]*\): \([^|]*\)|.*#\1|\2#p")
  echo "$HITS" | while IFS='|' read ln why; do
    [ -z "$ln" ] && continue
    echo "$ADDED" | grep -qx "$ln" && echo "$f:$ln: $why"
  done > "$TMP/hits.txt"
  if [ -s "$TMP/hits.txt" ]; then cat "$TMP/hits.txt"; BAD=1; fi
done
rm -rf "$TMP"
if [ "$BAD" -ne 0 ]; then
  echo ""
  echo "COMMIT BLOCKED: the lines above contradict docs/GTT-READ-FIRST.md or the Center of Truth."
  echo "Fix them, or if a line only quotes a banned value on purpose add the marker: factcheck:ok"
  exit 1
fi
exit 0
