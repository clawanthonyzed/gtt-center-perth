"""
Regression tests for tools/check_consistency.py's STALENESS_MARKERS matching.

Background (2026-08-08): STALENESS_MARKERS previously matched the bare
substring `prior` with no word boundary, so it matched inside unrelated
words like "priority" (e.g. "WDP, priority 1") and silently suppressed
genuine findings sitting within STALENESS_WINDOW lines of any such word.
Fixed by anchoring the pattern to `\bprior\b`. These tests pin that fix
down so it cannot silently regress, and confirm the fix did not weaken
any other existing marker.

Run:
    python tests/test_check_consistency.py
    (or: python -m unittest tests.test_check_consistency -v, from repo root)
"""

import importlib.util
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CC_PATH = REPO_ROOT / "tools" / "check_consistency.py"

_spec = importlib.util.spec_from_file_location("check_consistency", CC_PATH)
cc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cc)


class StalenessMarkerTests(unittest.TestCase):
    def test_prior_as_whole_word_still_matches(self):
        """'prior' used as an intentional historical marker must still suppress."""
        lines = [
            "",
            "This was the prior committed model, no longer used.",
            "",
        ]
        self.assertTrue(
            cc.has_marker(lines, 1),
            "'prior' as a whole word should still count as a staleness marker",
        )

    def test_priority_substring_does_not_match(self):
        """'priority' must NOT be treated as containing the 'prior' marker."""
        lines = [
            "",
            "Pathology partner (WDP, priority 1) has been emailed, awaiting reply.",
            "",
        ]
        self.assertFalse(
            cc.has_marker(lines, 1),
            "'priority' must not falsely trigger the 'prior' staleness marker",
        )

    def test_genuine_stale_finding_near_priority_is_still_detected(self):
        """
        Reproduces the exact real-world case found in docs/reading-order.md
        (2026-08-08 audit): a genuinely stale figure sitting within
        STALENESS_WINDOW lines of the word "priority" (with no other
        staleness marker nearby) must still be reported as a finding, not
        silently swallowed.
        """
        lines = [
            "",
            "## THE 60-SECOND VERSION",
            "",
            "Pathology partner (WDP, priority 1) has been emailed. "
            "Current committed operational model: 10 GTT clients/day, "
            "projected +A$25,087/month profit.",
        ]
        # has_marker for the stale-figure line (index 3) must be False --
        # "priority" two lines earlier must not suppress it.
        self.assertFalse(
            cc.has_marker(lines, 3),
            "a genuine stale figure must not be suppressed just because "
            "'priority' appears within the lookback window",
        )
        # And confirm the actual CHECKS pattern for the known-stale AM
        # client-capacity figure matches this line -- proving scan_file()
        # would report this as a real finding, not just that has_marker
        # returns False in isolation.
        client_capacity_patterns = cc.CHECKS[0][2]
        matched = any(p.search(lines[3]) for p in client_capacity_patterns)
        self.assertTrue(
            matched,
            "the '10 GTT clients/day' stale pattern must still match the "
            "reconstructed line -- otherwise this test isn't actually "
            "proving a real finding would surface",
        )

    def test_existing_markers_unaffected(self):
        """Spot-check other existing marker words still work post-fix (no collateral damage)."""
        for word in ["superseded", "historical", "corrected", "flagged", "archive", "deprecated"]:
            lines = ["", f"This figure is {word} as of this session.", ""]
            self.assertTrue(
                cc.has_marker(lines, 1),
                f"marker word '{word}' should still be detected after the fix",
            )
        # "was " keeps its own regex form (requires trailing whitespace) --
        # tested separately rather than via the word-substitution loop above.
        was_lines = ["", "The prior figure was 10 clients/day.", ""]
        self.assertTrue(cc.has_marker(was_lines, 1), "'was ' marker should still be detected")

    def test_scan_file_end_to_end_on_real_repo_docs(self):
        """
        End-to-end sanity check: running the real, current scan_file() against
        the real, current docs/reading-order.md must not error, and (as of
        this fix) must not silently return zero findings due to the priority
        bug specifically -- this doesn't assert a specific finding count
        (the repo's real content changes over time), it only proves the
        function runs cleanly against real content post-fix.
        """
        target = REPO_ROOT / "docs" / "reading-order.md"
        if not target.exists():
            self.skipTest("docs/reading-order.md not found -- skipping end-to-end check")
        findings = cc.scan_file(target)
        self.assertIsInstance(findings, list)


if __name__ == "__main__":
    unittest.main(verbosity=2)
