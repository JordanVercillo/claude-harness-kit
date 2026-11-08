# The agentic workflow: how a harnessed repo works with Claude Code

The one description of the workflow the kit installs. `/kit-start` installs the pieces; this
page says what each is for and why, so a new repo starts from the whole kit instead of
rediscovering it one painful session at a time.

## 1. The loop

```
/resume ──► /groom ──► brief ──► grill ──► build ──► /verify ──► review ──► /ship ──► the owner merges ──► /wrap-session ──► /retro
                                                                                                              (with the dream)   (asks, applies)
   ▲                                                                                                                                  │
   └───────── the next /resume grooms what the wrap's tech-debt sort and the retro left, for the owner to rule ◄──────────────────────┘

side loops: diagnose (a defect)  ·  /handoff (stop mid-task; the next /resume continues it)
```

- **`/resume`** syncs, reads the memory, proves the state and derives the open-items ledger live.
- **`/groom`** walks the owner through what waits on them (the machine first, then each item
  checked live, the sitting schedule, the debt lane, the intakes) and asks every blocking or
  important question in rounds; the lane is picked from the answers, never before them.
- **brief**: `/resume` drafts the session brief (§1.1) for that lane.
- **grill**: `/interview-me`'s brief grill walks the owner through the draft (the goal, what gets
  built and why, the plan per agent, the Done-when lines, the last wrap's tech-debt sort) and the
  owner confirms a playback; the brief is a draft until then.
- **build**: `/orchestrator` runs the lane, one agent at a time (`/interview-me` and `/spec` first
  when the lane needs a ruling or a contract; a branch); a question for the owner that comes up
  mid-lane is asked then, under the interview's laws, and only a "Not now" or an item due in a
  later phase becomes an issue carrying the label `/resume` reads.
- **`/verify`** (every check the repo names) → **review** (`code-reviewer`, cold) → **`/ship`** (a
  PR with the evidence) → **the owner merges**.
- **`/wrap-session`** reviews the brief against its Done-when lines, sorts the tech debt (each new
  or unsorted chore to the lead's next debt batch, the owner, or the slice it is owed to), saves
  the memory within its budgets, writes the journal, and runs **`/dream`**: a light pass every
  wrap, a full consolidation every fifth session (the default) or when the 📍 moves a phase, the
  owner confirming the summary before anything is rewritten; the journal stays append-only.
- **`/retro`**, when the harness fought back: it asks the owner each candidate (evidence, the fix
  and its home, why it helps, its cost every session) in rounds and applies what they OK on the
  open batch PR; a new guard, hook or test becomes an issue carrying the deliberate-failure proof.

Every session starts warm from the living memory and ends by writing back to it. Nothing is built
without a spec, nothing merges without a check the agent ran and a reviewer who read the diff
cold, and the owner merges.

### 1.1 The session brief (the loop's contract)

One file per session: written by `/resume` before any work starts, read by `/orchestrator` as its
plan, closed by `/wrap-session` against its own **Done when** list.

- **What it holds.** The goal in one line; the lane (build, research, design, harness, triage,
  sitting); why now; scope in and out, so a discovery is slotted rather than absorbed; the open
  items, each with its home and whose hand it is in; the plan, one agent or skill per step;
  **Done when**, each line observable by a cold reader; the decisions the owner must make, each
  with a recommendation.
- **Where it lives.** Outside the repo, in Claude Code's project-data folder for the repo
  (`~/.claude/projects/<project-key>/sessions/`, next to `handoffs/`). Never committed. One brief
  open at a time; a closed one moves to `sessions/closed/` with its `## Review`.
- **A draft until the grill.** `/resume` writes it after `/groom`, and `/interview-me`'s brief
  grill walks the owner through it and ends in a playback the owner confirms; an answer that
  changes the lane, the scope or the plan rewrites the brief first. `/orchestrator` does the same
  when a session starts from a goal instead of `/resume`.
- **The loop closes through the sort and `/retro`.** The wrap sorts every new or unsorted chore
  into one of three homes (the lead's next debt batch, the owner, the slice or sitting it is owed
  to) and writes the rows and one line of totals into the brief's `## Review`, which the next
  `/groom` reads; the debt lane is offered as a question whenever the list isn't empty. When the
  wrap finds the session fought the harness (a check that failed twice on one class, a reverted
  edit, a question the repo could have answered, a skipped step), it runs `/retro`, which asks the
  owner each candidate in rounds and applies what they OK on the open batch PR (prose, deletions,
  allowlist lines); a guard, hook or test becomes an issue carrying the deliberate-failure proof
  requirement; a declined candidate is listed, not filed.

## 2. The tiers (what `/kit-start` installs)

| Tier | Pieces | Why | Install when |
|---|---|---|---|
| **Memory core** | `CLAUDE.md` bootloader · `notes/PROJECT_CONTEXT.md` (RESUME HERE ≤ 20 lines, file ≤ 150, session log ≤ 10) · `notes/roadmap.md` with a 📍 · `notes/journal.md` (numbered, append-only) · `/resume` · `/groom` · `/wrap-session` · `/dream` · `/handoff` · `/retro` · the session brief (outside the repo) · the SessionStart hook · `block_protected_paths.py` · `.claude/rules/harness.md` · `harness_guards.py` (six checks; a skill stays at or under 150 lines by default) | A session that re-derives state from code spends its context before it works. Budgets keep the memory a map, not a transcript. The owner unblocks the lane before it starts and confirms the brief before an agent is briefed. A rule in prose is advisory; a hook is a gate. | every repo |
| **Gates** | `/verify` (the check commands `CLAUDE.md` names, one table) · `/ship` (a PR sized to the change; the owner merges) · the `code-reviewer` seat (CONFIRMED / PLAUSIBLE, HOLD on a partial pass) · `diagnose` · the PR template (acceptance evidence, merge risk) · the guards in CI | "Looks done" is the only signal an agent has unless a check returns pass / fail. A reviewer with a fresh context catches what the author's context hides. | any repo with code |
| **Specs** | `/spec` (+ its validator) · `/interview-me` · `specs/` with a README | The spec is the frozen contract the build reads; the interview is how it stops being ambiguous. Numbers are PROPOSED until the owner rules them. | anything non-trivial |
| **Lead and seats** | `/orchestrator` · `.claude/agents/` seats with `## Your files` and `## Creates at first task` · the roster in `CLAUDE.md` · `kb-librarian` where a knowledge base exists · `MERGE-POLICY.md` where two or more people commit | One lead that briefs one expert at a time keeps the main context clean and the reports verifiable. File ownership keeps two writers off one file. | work that spans domains |
| **Domain extras** | a `<domain>-partner` orchestrator over a `<domain>-audit` worker and its script; domain seats (SQL, modeling, Python, testing) | Each domain has one or two things only a check keeps honest: rows that carry `status` + `source`, a generated view with a drift guard, a read-only knowledge base. | as the domain needs |

## 3. The principles, each paid for once

1. **One home per fact.** Status, counts and baselines each live in one file; everything else
   links to it. Views are generated, and a drift guard fails CI when a twin is stale.
2. **Memory is budgeted, guarded and dreamed.** A context file or a skill that grows past its
   budget fails a check; history lives in git, not in the file; a full consolidation pass every
   fifth session (the default) keeps the lessons a map, and the journal stays append-only.
3. **Spec before code, and the owner rules.** Seats draft and recommend; an unruled number is
   labelled PROPOSED; a placeholder is a decision nobody made.
4. **A check you haven't seen fail isn't a check.** A new guard or test is broken on purpose
   before it counts; absence is proven by a caller list or a counterfactual test, never inferred
   from a green run; a reviewer's careful CONFIRMED is still a hypothesis until a test asserts it.
5. **A defect class found twice is closed by a check, not a third careful pass.**
6. **Gates cost less than the slice they guard.** PRs are sized to the change; a small fix rides
   the open batch PR; process that crowds out the work is a bug.
7. **Agents run one at a time, one lane per session.** A discovery mid-session is named and
   slotted (an issue, a spec open question), not absorbed into the current work.
8. **Deterministic over prose.** Must-happen behaviour is a hook; conventions a script can check
   are guards in CI; rules that matter only for some files are path-scoped in `.claude/rules/`.
9. **Evidence in the PR, scratch outside the repo, data in its home.** Verdict lines and test
   counts are pasted into the PR; proof folders and screenshots nobody references are never
   committed. Scratch (a probe script, a check's output) stays in the session scratchpad; data kept
   or read again (an input, a pull, an output) is local data and lives where the data ground rule
   says; a doc, note or script worth keeping stays in the repo.
10. **Write for agents the way the research says works.** A skill's description is a pointer with
    its trigger words first; every step has a completion criterion; state the target behaviour,
    not the prohibition; delete instructions the model already follows; link, never paste.

## 4. Starting a new repo (the playbook)

1. **Create it private** where the workplace's convention allows a choice. Vendor assets,
   personal data and anything with a key never go public.
2. **Bootstrap.** In a Claude Code session in that folder, `/kit-start <kit path>`. It detects
   the stack, asks only for the gaps (purpose, vision, who rules, the domain, four ground rules,
   what recurs), rules the pieces with you, and writes them with their placeholders filled. One
   default it offers: data only (inputs, fetched data, snapshots, generated outputs, library
   caches) lives in this project's folder in a machine-level data home outside the repo, which an
   env var names, one folder per project; code, docs and every other file never go there, and the
   doc of the data's layout lives in the repo. The repo's gitignored `data/` is the fallback without a data
   home and a safety net with one. So a temp dir, a session scratchpad or a synced folder never
   holds the only copy, one project never edits another's data (the protected-paths hook), and
   nothing is committed by accident.
3. **Start warm.** Fill the RESUME HERE block with the first real NEXT ACTION before closing the
   session; the next `/resume` must be productive.
4. **First slice.** `/resume` → `/groom` → the draft brief → the grill → `/orchestrator` →
   `/interview-me` the first spec → `/spec` → build on a branch → `/verify` → `/ship` → the owner
   merges → `/wrap-session` (with the dream). A tracer bullet, not the whole feature.
5. **First retro.** After the first slice, `/retro`. It asks the owner each candidate and applies
   what they OK; anything mechanical becomes a guard or a hook, never a sentence in `CLAUDE.md`.
6. **Keep the kit upstream.** An adaptation lives in the repo's copy and wins by name. A generic
   improvement goes back to the kit (`HANDOFF.md` §2 says how, and what never travels).

**What not to do:** install a skill mega-pack (every description loads into every session; adapt
the two or three skills that fill a gap instead); let `CLAUDE.md` grow past about 120 lines
(procedures to skills, file-specific rules to `.claude/rules/`); commit evidence or scratch;
keep local data outside the home the data ground rule names (a temp dir or a scratchpad is
cleared, a home cache is invisible, a synced folder leaks); enable auto-merge; let an agent fan out
subagents.
