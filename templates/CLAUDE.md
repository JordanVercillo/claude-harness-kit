# {{REPO_NAME}} — {{ONE_LINE_PURPOSE}}

## ⏭️ RESUME HERE (read first, every session)

**Before anything else, read [`notes/PROJECT_CONTEXT.md`](notes/PROJECT_CONTEXT.md).**
It is the living memory — current status, conventions, key files, and the exact
next step. Reading it makes you fully caught up without re-deriving anything.
`/resume` reads it automatically; `/wrap-session` updates it at session end.

## Ground rules

1. {{RULE_TOOLING}} <!-- e.g. Python runs through uv: `uv run <script>` — never bare python, never activate a venv -->
2. {{RULE_READONLY}} <!-- what is read-only: generated files, synced copies, vendored code — never hand-edit -->
3. {{RULE_DATA}} <!-- default: data only (extracts and pulls: inputs, screenshots, fetched data, snapshots, generated outputs, library caches in its cache/) lives in this project's folder in the machine-level data home, outside the repo, when the data home's owner admits this repo (the data home's allowlist; with none, ask the owner): code finds it through its env var with a default, e.g. $DATA_ROOT/<repo>/ (default ~/.data/<repo>/), never a path built in code without that variable. Never inside the repo, a temp dir, a session scratchpad, a library's default cache or a cloud-synced folder. Code, docs and every other file never go in the data home; the doc of the data's layout lives in the repo (e.g. docs/data-home.md). Without a data home, or with one that doesn't admit this repo, the repo's own gitignored data/. Scratch (a probe script, a check's output) stays in the scratchpad; data kept or read again (an input, a pull, an output) is local data -->
4. {{RULE_SECRETS}} <!-- secrets by name only, live values in .env (gitignored); a hardcoded fallback IS a leak -->
5. Commit small reviewable chunks and push regularly — the repo is its own backup.

## Routing

| Want | Use |
|---|---|
| Get back up to speed & continue (start here) | `/resume` (orients, grooms the backlog with you through `/groom`, writes the session brief, grills you on it, hands it to `/orchestrator`) |
| Lead this session's work from its brief | `/orchestrator` + the brief path or a one-line goal |
| End a session that did meaningful work | `/wrap-session` (reviews the brief, sorts the tech debt, saves memory, consolidates it through `/dream`, tidies, runs `/retro` when the harness fought back) |
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
| {{DATA_PATH}} | local data only, never committed (the data ground rule): inputs, fetched data, snapshots, generated outputs, `cache/`; its layout is documented in `docs/data-home.md` <!-- e.g. `$DATA_ROOT/<repo>/` (outside the repo); `data/` without a data home --> |
<!-- add if installed: | `specs/` | validated implementation contracts (`/spec`) | -->
