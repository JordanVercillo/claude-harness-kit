---
name: kit-start
description: Start a repo on the harness kit — show what the kit holds, interview for the repo's purpose and vision, rule ADOPT / ADAPT / SKIP per piece, install the chosen pieces with their placeholders filled, verify. TRIGGER when the user says "/kit-start", "set this repo up from the kit", "what's in the kit", "which skills does this project need", or opens a repo with no CLAUDE.md. SKIP for a repo already on the harness that wants one more piece (copy it from the kit's CATALOG row and fill it by hand) and for resuming work (/resume).
user-invocable: true
allowed-tools: [Read, Glob, Grep, Write, Edit, Bash, PowerShell, AskUserQuestion]
---

You make a repo "Claude Code native" from the harness kit, a folder of skills, seats, hooks, rules
and templates pasted into a repo and adapted to its workflow: show what is available, learn what
the repo is for, recommend what it needs, install only that, prove the install. **The owner rules
every verdict**; you recommend. Operate on the current repo (CWD) unless the invocation names a
target folder.

## Phase 0 — Locate the kit and detect the repo (don't ask what you can see)

1. **Find the kit**, in this order, and say which: the path in the invocation's arguments; the
   `HARNESS_KIT` environment variable; a folder named `claude-harness-kit` beside this repo or in
   the home folder; the current folder itself when it holds `CATALOG.md` and `.claude/skills/kit-start/`
   (then the target repo must be named in the arguments). Read the kit's `CATALOG.md` in full (the
   inventory, the install order, the placeholder table) and `HANDOFF.md` §"The boundary" once.
2. **Detect the repo:** `git rev-parse --is-inside-work-tree`, `git log -1` (new or has history);
   the stack from its manifest (`pyproject.toml`, `package.json`, `go.mod`, `Cargo.toml`, `*.sln`,
   `dbt_project.yml`, `requirements.txt`: language, setup, run, test and lint commands); generated,
   vendored or synced paths (an index, a catalog, `vendor/`, `dist/`, `target/`): candidates for the
   protected-paths hook; a knowledge-base folder; CI config; how work is merged (branches, PRs, a
   protected `main`); who commits (`git shortlog -sn | head`); a tracked `data/` (`git ls-files data`).
3. **Detect the tooling** the kit's scripts need: `uv --version`, else `python --version` plus
   `python -c "import yaml"`; the runner the install writes into hook commands and routing rows is
   `uv run <script>` when uv exists, else `python <script>` (name `pyyaml` as a prerequisite). Record
   whether `gh` exists (`/ship` uses it; without it `/ship` opens PRs through the web).
4. **Already harnessed?** If `CLAUDE.md`, `notes/PROJECT_CONTEXT.md` or `.claude/skills/` exists,
   never clobber: show the owner what is there and offer to merge or add specific pieces. An
   existing skill of the same name as a kit piece is the repo's own and wins; leave it.
5. **Enterprise settings:** read the managed settings file, when one exists (`HANDOFF.md` §"If loose
   skills are blocked" names the path per OS and the keys): a key that stops loose project skills,
   agents or hooks from loading is said now, before installing; where you can't read the file, say that.

**Done when:** you can state, in one block, the kit path, the stack, the runner, the merge model,
the committers, the protected-path candidates, a tracked `data/`, and whether it is already harnessed.

## Phase 1 — Showcase (what is available)

Present the catalog as one table per tier from `CATALOG.md`, each row in the owner's terms (the
piece, what it gives a session, when a repo wants it); drop nothing. Then one paragraph on the loop
(`/resume` → `/groom` → brief → grill → build → `/verify` → review → `/ship` → the owner merges →
`/wrap-session` with `/dream` → `/retro`), so the owner sees how the pieces connect. No verdicts yet.

## Phase 2 — Interview: the purpose and the vision (one question at a time)

Ask with `AskUserQuestion`, one question per turn, each with a recommendation drawn from Phase 0;
never ask what Phase 0 detected, confirm it in the premise. Six at most; stop once the review is settled.

1. **Purpose.** The repo's one-line purpose, and what it is NOT (the adjacent thing elsewhere).
2. **Vision.** What "done" looks like in a quarter, in one sentence, and the first milestone on
   the way. (These become the roadmap's one-sentence goal and Phase 1.)
3. **Who works here.** Solo, a pair, a team; who rules decisions (the owner); whether work merges
   through reviewed PRs or lands on a trunk. (Gates and MERGE-POLICY hang on this.)
4. **The domain.** What the repo mostly is: a data platform or warehouse, a pipeline, an app or
   service, a library, infrastructure, docs or research, a course. (The domain pieces hang on this.)
5. **The ground rules.** The four a session must never break: the runner; what is read-only or
   generated; where local data lives (default: the repo's own gitignored `data/`, library caches in
   `data/cache/`, never a temp dir, a scratchpad, a home cache or a synced folder; another home when
   Phase 0 found a tracked `data/`, which ignoring would hide new files from); the secrets policy.
6. **What recurs.** The check someone keeps running by eye ("is X healthy?", a count, a parity):
   the candidate for the first deterministic audit. "Nothing yet" is a fine answer.

**Done when:** every placeholder in `CATALOG.md` §Placeholders marked "(interview)" has a value or
an explicit "delete the line", and the owner has named who rules.

## Phase 3 — Review: ADOPT / ADAPT / SKIP per piece (the owner rules)

Build one table over every catalog piece except `docs/` and the kit's own start pieces:

| Piece | Verdict | Why (one line, grounded in an answer) | Adapt by |
|---|---|---|---|

Rules for the verdict:
- **core is ADOPT** in every repo (memory, the two hooks, rules, guards, `/resume`, `/groom`,
  `/wrap-session`, `/dream`, `/handoff`, `/retro`); ADAPT, with the merge named, where it has its own.
- **gates:** ADOPT when work merges through PRs; ADAPT when the repo has a trunk flow (`/ship`
  commits and pushes, the reviewer still gates); the PR template only with PRs.
- **specs:** ADOPT for anything non-trivial; SKIP for a repo of scripts or docs only.
- **lead:** `/orchestrator` ADOPT when work spans domains or seats will exist; `kb-librarian`
  only with a knowledge-base folder; `MERGE-POLICY` only with two or more people.
- **domain templates:** one seat per domain the answers named, as ADAPT (a template is never
  installed unfilled); `domain-partner` + `domain-audit` ADAPT when question 6 named a recurring
  check or the repo has one dominant domain; else SKIP, with the trigger that would change it.
- Every SKIP names what would change the verdict, so the owner can revisit it without the kit.

Present the table with a one-line summary of what will be written and ask the owner to rule it
(approve, or name the rows to change). **Done when:** the owner has approved the table as it stands.

## Phase 4 — Install (write only what was ruled)

1. **Memory core, always:** copy from `templates/` into the repo, filling every `{{…}}` token from
   the interview and Phase 0 per the placeholder table: `CLAUDE.md` (prune routing rows for tiers
   not installed; the runner's spelling in every command), `notes/PROJECT_CONTEXT.md`,
   `notes/journal.md`, `notes/roadmap.md`, `README.md` (only if absent), `.gitignore` (merge the
   kit's lines, the root-anchored `/data/` among them; uncomment the language block), `data/` (and
   `data/cache/` when the code has a library cache; a home the data rule named instead replaces
   `data/` in `.gitignore` and the map), `.claude/settings.json` (merge: keep the repo's permissions
   and hooks; the two hook commands with the runner's spelling and an absolute `$CLAUDE_PROJECT_DIR`
   path), `.claude/hooks/block_protected_paths.py` (fill `PROTECTED` with the Phase 0 candidates),
   `.claude/hooks/session_start.py`, `.claude/rules/harness.md`, `scripts/harness_guards.py`.
2. **Skills and seats ruled ADOPT:** copy the kit's `.claude/skills/<name>/` folder (with its
   scripts) and `.claude/agents/<name>.md` as they are. ADAPT: copy, then make the named edit
   (the bench in `/orchestrator`, the regenerate list in `/wrap-session`, the domain standard in
   `code-reviewer`), nothing else. Each installed skill and seat gets its routing row in
   `CLAUDE.md`; each seat is in the roster and lists `## Your files` that exist.
3. **Domain templates ruled ADAPT:** copy `seats/<x>.TEMPLATE.md` to `.claude/agents/<x>.md` and
   `skills-domain/<x>/` to `.claude/skills/<domain>-<x>/`, fill every `{{…}}` and `<angle>`
   placeholder from the answers, rename per the catalog's "adapt by", and write the audit script's
   first flags from question 6 (an empty flag list is a defect: the script must check something).
4. **Gates ruled ADOPT:** `.github/pull_request_template.md`; when CI exists, add the guards and
   the test command to it, or list the two lines for the owner when the CI format is unknown.
5. **The first NEXT ACTION** in PROJECT_CONTEXT's RESUME block is the first real step from the
   vision, never "start using the harness". The session-log line records the kit's plugin version
   (from `CATALOG.md`'s header) and the tiers installed, so a later upgrade knows where it started.

Never copy `docs/`, `HANDOFF.md`, `CATALOG.md` or this skill into the repo. Never edit the kit.
`git init` only when the folder is not a repo, and ask first. Do not commit unless asked.

**Done when:** every ADOPT or ADAPT row has its files and its routing row; no SKIP file exists.

## Phase 5 — Verify (an install nobody tested is a draft)

Run and show, one table, PASS / FAIL per line:
- `<runner> scripts/harness_guards.py` passes all six checks;
- `git check-ignore -q <data home>/probe` exits 0 (`data/probe` by default); a home outside the
  repo, or a folder that is not a git repo, is "not applicable", said so;
- the protected-paths hook blocks a protected path and allows a normal one: pipe
  `{"tool_name":"Edit","tool_input":{"file_path":"<path>"}}` to it; exit 2 blocks, 0 allows;
- the SessionStart hook prints a JSON object with `additionalContext` holding the RESUME block
  when run from the repo root with an empty stdin;
- no `{{` remains under the repo (`grep -rn "{{" CLAUDE.md notes/ .claude/ scripts/`), excluding
  files the repo had before;
- the spec validator runs, when `/spec` was installed: `<runner> .claude/skills/spec/validate_spec.py --help`
  or on an empty file returns its JSON;
- the skills load: at the next session start in this folder, `/skills` lists each installed
  name (discovery is not the same as the file existing; say so if you cannot restart here).

A FAIL is fixed now, not reported for later. **Done when:** every line is PASS, or a line says
exactly what the owner must do on their machine (a restart, a tool install).

## Phase 6 — Close

Tell the owner, in a few lines: what was installed per tier, the runner written into the commands,
the one line to begin (`/resume`), and that this is a STARTING harness whose first `/retro` says
what the repo needs more of; an adaptation belongs in this repo's copy, and only a generic
improvement, with none of this repo's specifics, goes back to the kit (`HANDOFF.md` §"The boundary").
