# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""audit_<domain> — facts about <the thing>, as one JSON object. Judgment stays in the skill.

Rename this file audit_<domain>.py beside the <domain>-audit SKILL.md, replace the two example
checks with the first real ones (the thing someone keeps checking by eye), and keep the contract:

  {"inventory": {...}, "errors": [...], "warnings": [...], "flags": {"NO_DATA": bool, ...}}

- errors   block the work they touch (the partner skill fixes or descopes first)
- warnings resize the work
- flags    are branch points the partner skill reads; every flag the script can emit is listed
           in the skill's "Flag meanings"
- exit 0 even with findings (the report IS the result); exit 1 only when the audit itself can't run
- absent data is a flag (NO_DATA), never a crash

Usage:  <runner> .claude/skills/<domain>-audit/audit_<domain>.py [--root DIR] [--json-indent N]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def check_exists(root: Path, report: dict) -> None:
    """Example check 1: the thing to audit exists (replace with the real location)."""
    target = root / "data"  # <- the warehouse file, the content folder, the build output
    report["inventory"]["target"] = str(target)
    if not target.exists():
        report["flags"]["NO_DATA"] = True
        report["warnings"].append(f"nothing to audit yet: {target} is absent")


def check_integrity(root: Path, report: dict) -> None:
    """Example check 2: an invariant that must hold (replace with the real one)."""
    if report["flags"].get("NO_DATA"):
        return
    # e.g. a row count that must match across two layers, a sum that must be conserved,
    # a column list that must equal the contract. Set a flag AND an error line when it fails.
    observed, expected = 0, 0
    report["inventory"]["observed"] = observed
    if observed != expected:
        report["flags"]["INTEGRITY"] = True
        report["errors"].append(f"integrity: observed {observed} != expected {expected}")


CHECKS = [check_exists, check_integrity]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", type=Path, default=Path.cwd())
    ap.add_argument("--json-indent", type=int, default=2)
    a = ap.parse_args()
    report = {"inventory": {}, "errors": [], "warnings": [], "flags": {"NO_DATA": False}}
    try:
        for check in CHECKS:
            check(a.root.resolve(), report)
    except Exception as exc:  # the audit itself failed: say so, exit 1
        print(json.dumps({"audit_error": f"{type(exc).__name__}: {exc}"}))
        return 1
    print(json.dumps(report, indent=a.json_indent, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
