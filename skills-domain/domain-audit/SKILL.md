---
name: {{DOMAIN}}-audit
description: Internal skill — deterministic {{DOMAIN}} audit. Called by {{DOMAIN}}-partner at session start and after any <relevant change>; also usable directly when the owner asks to "audit the <thing>" or "is <X> healthy".
user-invocable: true
allowed-tools: [Bash, Read]
---

You are an audit agent. Run the validator, then report; no design opinions.

## Steps

1. From the repo root run:

   ```bash
   <runner> .claude/skills/{{DOMAIN}}-audit/audit_{{DOMAIN}}.py
   ```

2. Parse the JSON output and return exactly this block:

   ```
   === <DOMAIN> AUDIT ===
   <Inventory line: counts of the units that matter>
   Errors:   <one line each, or "none">
   Warnings: <one line each, or "none">
   Flags:    <true flags with [WARNING], or "Normal">
   ```

3. Flag meanings (one line per flag the script can emit):
   - `NO_DATA` — nothing to audit yet (informational, but blocks downstream work: say which)
   - `<INTEGRITY_FLAG>` [WARNING] — <what broke and what it blocks>

If the script itself errors, report the raw error and stop; do not guess. Return only the
formatted block, no commentary.

<!-- The paired script (audit_<domain>.py) starts from audit_TEMPLATE.py beside this file and
     follows the pattern card docs/deterministic-audit-scripts.md in the kit:
     PEP 723 header · facts → JSON · errors / warnings / flags · exit 0 with findings ·
     graceful when data is absent. An audit with no checks is a defect: write the first flag
     from the thing someone keeps checking by eye. -->
