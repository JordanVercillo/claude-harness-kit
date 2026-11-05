# Handoff: carrying the harness kit to another machine or workplace

This folder is a way of working with Claude Code, packaged so it can be pasted into any repo: a
living memory every session starts from, a lead that briefs one expert at a time, specs before
code, a check the agent runs, a reviewer who reads the diff cold, and the owner merging. It was
authored outside any employer, on personal time, from personal projects, and it contains no
personal data and nothing machine-local: a deny-list guard runs at build time and fails the build
on any such term. What it does contain is method: skills, seats, hooks, rules, templates, docs.

## 1. Before you carry it

Three things to settle with the workplace once, in writing where that is the norm there:

1. **Is Claude Code approved** for the repos you mean to use it in, and under which account.
2. **May a personal, generic toolkit be brought in** and adapted there. Most policies allow
   generic tooling and method; what they forbid is the other direction (§2).
3. **Who owns the adaptations.** Assume the employer does: a skill edited for a work repo is
   theirs the moment it names their systems.

## 2. The boundary (one way, always)

**In:** the kit as it is. Method, not material.

**Never back:** anything that names the employer's systems, data, people, hosts, tickets, repos,
paths or commands. An adapted skill stays in the work repo. A seat that lists work files stays.
A journal entry about a work defect stays. Nothing from a work repo is pasted into a personal
repo, a personal knowledge base, a personal note or a chat on a personal account.

**The one thing that may travel home:** a *generic* improvement to the method, re-authored from
memory at home, with no work specifics in it. The test, line by line: would this line make sense
in a repo the employer has never heard of? If it names a system, a person, a dataset or a
convention that exists only at work, it stays at work. Write the lesson down at work as a note
("the `/verify` table needed a HOLD state for a gate that timed out"), and rebuild the kit at home
from that sentence, not from the file.

Keep the accounts apart too: the work repos are reached with the work account and the work
Claude Code login; the kit folder at work is a copy, never a clone that pushes anywhere personal.

## 3. What the work machine needs

| Need | Why | Without it |
|---|---|---|
| Claude Code (CLI, desktop app or IDE extension) | runs the skills | nothing works |
| git | every skill reads the branch and tree state | nothing works |
| Python 3.11+ and `uv` | the hooks, the guards, the spec validator and the audit scripts are single-file scripts with inline dependencies, run as `uv run <script>` | `python <script>` works for every script; install `pyyaml` once; `/kit-start` writes `python` into the hook commands when it finds no `uv` |
| `gh` (GitHub CLI) | `/ship` opens and watches PRs with it | `/ship` says what to open by hand; everything else runs |
| Git Bash on Windows | hook commands run through it by default | PowerShell runs them when it is absent; the hook commands work in both |

Check the managed settings before the first install (§5): a workplace may restrict what loads.

## 4. The carry route and the install

1. **Carry** the folder through a channel the workplace accepts: a zip over an approved transfer,
   or a private git repository the workplace allows you to clone. Never a personal cloud share
   mounted on the work machine without approval.
2. **Place** it somewhere stable on the work machine, beside the repos it will serve, and leave
   it untouched: it is the template; the adaptations live in each repo.
3. **Install the startup skill once at user scope:** copy `.claude/skills/kit-start/` to
   `%USERPROFILE%\.claude\skills\kit-start\` (Windows) or `~/.claude/skills/kit-start/`.
4. **In each repo:** open it in Claude Code and run `/kit-start <path to the kit>`. It shows the
   catalog, interviews for the repo's purpose and vision, rules ADOPT / ADAPT / SKIP per piece
   with you, installs only what you ruled, fills the placeholders, and proves the install (the
   guards pass, the hooks block and allow, no `{{` left, the skills load).
5. **A repo that already has a `CLAUDE.md`** is never overwritten: the skill shows what is there
   and merges piece by piece.

## 5. If loose skills are blocked

A workplace can lock Claude Code down through its managed settings file (Windows:
`C:\Program Files\ClaudeCode\managed-settings.json`; macOS:
`/Library/Application Support/ClaudeCode/managed-settings.json`; Linux and WSL:
`/etc/claude-code/managed-settings.json`; also a registry or MDM policy, or the admin console).
Keys that matter here:

| Key | Effect on the kit |
|---|---|
| `strictPluginOnlyCustomization` | project `.claude/skills/`, `.claude/agents/` and hooks do not load; only plugins from allowed marketplaces do |
| `allowManagedHooksOnly`, `disableAllHooks` | the two hooks do not run; the skills still work, the session just starts cold (`/resume` reads the memory itself) |
| `strictKnownMarketplaces`, `blockedMarketplaces` | which plugin sources may be added |

When project skills are blocked, the kit's `.claude/` can be wrapped as a plugin: a folder with
`.claude-plugin/plugin.json` (`name`, `version`, `description`), the kit's `skills/` and
`agents/` folders moved up one level, and `hooks/hooks.json` registering the SessionStart hook
by a path relative to that folder (the hooks documentation names the variable to use). It loads for one session with
`claude --plugin-dir <folder>` (unless `disableSideloadFlags` is set), or permanently through a
marketplace the admin allow-lists. Ask the admin which route is open; `/plugin` and `/skills`
inside a session show what actually loaded, which is the only proof.

## 6. The first slice at work

1. `/kit-start` in the repo; approve the review table; let it verify.
2. Fill the RESUME block's first real NEXT ACTION before closing that session (the skill asks).
3. Next session: `/resume` → it writes the session brief → `/orchestrator` → `/interview-me` the
   first spec → `/spec` → build on a branch → `/verify` → `/ship` → the owner merges →
   `/wrap-session`. The first slice is a tracer bullet, not the whole feature.
4. After the first slice, `/retro`. Anything mechanical it finds becomes a guard or a hook in
   that repo, never a sentence in `CLAUDE.md`.

## 7. What not to do

- Install every skill in every repo: each description loads into every session. Adapt the two
  or three that fill a gap.
- Let `CLAUDE.md` grow past about 120 lines: procedures go to skills, file-specific rules to
  `.claude/rules/`.
- Commit evidence or scratch; enable auto-merge; let an agent fan out subagents; hand-edit a
  generated file (the protected-paths hook exists to stop that).
- Edit the kit folder at work. An adaptation belongs in the repo; a generic lesson belongs in a
  note (§2) and reaches the kit at home.
