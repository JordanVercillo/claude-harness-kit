# {{REPO_NAME}}

{{ONE_PARAGRAPH_WHAT_AND_WHY}}

## Quick start

```bash
{{SETUP_CMD}}   # e.g. uv sync
{{RUN_CMD}}     # e.g. uv run python -m {{package}}
```

## Working with Claude Code

This repo carries a Claude Code harness (skills, seats, hooks and rules under `.claude/`,
plus the living memory under `notes/`). Start a session with **`/resume`** —
it reads `notes/PROJECT_CONTEXT.md` (the living memory) and continues from the exact
next step. End meaningful sessions with **`/wrap-session`** to save context.

- `CLAUDE.md` — ground rules + routing (read by every session).
- `notes/PROJECT_CONTEXT.md` — status, conventions, key files, next step.
- `notes/journal.md` — lessons learned. `notes/roadmap.md` — the plan.

## Prerequisites

- {{PREREQ}} <!-- e.g. Python 3.11+, uv, ... -->
