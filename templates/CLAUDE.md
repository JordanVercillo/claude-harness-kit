# {{REPO_NAME}} — {{ONE_LINE_PURPOSE}}

## ⏭️ RESUME HERE (read first, every session)

**Before anything else, read [`notes/PROJECT_CONTEXT.md`](notes/PROJECT_CONTEXT.md).**
It is the living memory — current status, conventions, key files, and the exact
next step. Reading it makes you fully caught up without re-deriving anything.
`/resume` reads it automatically; `/wrap-session` updates it at session end.

## Ground rules

1. {{RULE_TOOLING}} <!-- e.g. Python runs through uv: `uv run <script>` — never bare python, never activate a venv -->
2. {{RULE_READONLY}} <!-- what is read-only: data/, generated files, synced copies — never hand-edit -->
3. {{RULE_SECRETS}} <!-- secrets by name only, live values in .env (gitignored); a hardcoded fallback IS a leak -->
4. Commit small reviewable chunks and push regularly — the repo is its own backup.

## Routing

| Want | Use |
|---|---|
| Get back up to speed & continue (start here) | `/resume` (orients, writes the session brief, hands it to `/orchestrator`) |
| Lead this session's work from its brief | `/orchestrator` + the brief path or a one-line goal |
| End a session that did meaningful work | `/wrap-session` (reviews the brief, saves memory, tidies, runs `/retro` when the harness fought back) |
| Stop mid-task and continue in a fresh session | `/handoff` |
| Something is red, throws, or a check moved | `diagnose` (model-invoked; name it to force it) |
| Prove every check passes | `/verify` (it reads the commands from this file: {{TEST_CMD}} · {{LINT_CMD}} · `uv run scripts/harness_guards.py`) |
<!-- add if installed: -->
<!-- | Design a feature before building it | `/spec` + one-line idea (`/interview-me` rules its open questions) | -->
<!-- | Open a reviewed PR | `/ship` (the `code-reviewer` seat gates it; the owner merges) | -->

The harness skills under `.claude/skills/` were pasted from the harness kit and adapted here; an
improvement every repo wants goes back to the kit as generic process, never with this repo's
specifics. A new skill or seat gets its routing row here.

## Map

| Path | What |
|---|---|
| `notes/` | PROJECT_CONTEXT (memory) · journal (numbered lessons) · roadmap (plan) |
| `.claude/` | agents · hooks · rules · settings (the hooks, the allowlist) — this repo's part of the harness |
| {{SRC_PATH}} | {{SRC_DESC}} <!-- e.g. src/ — the package you build and extend --> |
<!-- add if installed: | `specs/` | validated implementation contracts (`/spec`) | -->
