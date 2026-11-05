# The agentic workflow: how a harnessed repo works with Claude Code

The one description of the workflow the kit installs. `/kit-start` installs the pieces; this
page says what each is for and why, so a new repo starts from the whole kit instead of
rediscovering it one painful session at a time.

## 1. The loop

```
/resume ──► /orchestrator ──► interview ──► spec ──► build ──► /verify ──► review ──► /ship ──► the owner merges ──► /wrap-session ──► /retro
 writes the   reads it,     (/interview-me)  (/spec)  (a branch,            (code-reviewer)  (PR)                     reviews the       when the
 session      one lane,                               one agent                                                       brief, closes it  harness fought
 brief        one agent                               at a time)                                                                        │
   ▲          at a time                                                                                                                 │
   └──────────── the next /resume lists the retro's issues among the open items, for the owner to slot ◄────────────────────────────────┘

side loops: diagnose (a defect)  ·  /handoff (stop mid-task; the next /resume continues it)
```

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
- **The loop closes through `/retro`.** When the wrap finds the session fought the harness (a
  check that failed twice on one class, a reverted edit, a question the repo could have answered,
  a skipped step), it runs `/retro`, which files an issue per check or hook; the next `/resume`
  lists it among the open items for the owner to slot. Nothing else from a retro is applied in
  the wrap.

## 2. The tiers (what `/kit-start` installs)

| Tier | Pieces | Why | Install when |
|---|---|---|---|
| **Memory core** | `CLAUDE.md` bootloader · `notes/PROJECT_CONTEXT.md` (RESUME HERE ≤ 20 lines, file ≤ 150, session log ≤ 10) · `notes/roadmap.md` with a 📍 · `notes/journal.md` (numbered, append-only) · `/resume` · `/wrap-session` · `/handoff` · `/retro` · the session brief (outside the repo) · the SessionStart hook · `block_protected_paths.py` · `.claude/rules/harness.md` · `harness_guards.py` | A session that re-derives state from code spends its context before it works. Budgets keep the memory a map, not a transcript. A rule in prose is advisory; a hook is a gate. | every repo |
| **Gates** | `/verify` (the check commands `CLAUDE.md` names, one table) · `/ship` (a PR sized to the change; the owner merges) · the `code-reviewer` seat (CONFIRMED / PLAUSIBLE, HOLD on a partial pass) · `diagnose` · the PR template (acceptance evidence, merge risk) · the guards in CI | "Looks done" is the only signal an agent has unless a check returns pass / fail. A reviewer with a fresh context catches what the author's context hides. | any repo with code |
| **Specs** | `/spec` (+ its validator) · `/interview-me` · `specs/` with a README | The spec is the frozen contract the build reads; the interview is how it stops being ambiguous. Numbers are PROPOSED until the owner rules them. | anything non-trivial |
| **Lead and seats** | `/orchestrator` · `.claude/agents/` seats with `## Your files` and `## Creates at first task` · the roster in `CLAUDE.md` · `kb-librarian` where a knowledge base exists · `MERGE-POLICY.md` where two or more people commit | One lead that briefs one expert at a time keeps the main context clean and the reports verifiable. File ownership keeps two writers off one file. | work that spans domains |
| **Domain extras** | a `<domain>-partner` orchestrator over a `<domain>-audit` worker and its script; domain seats (SQL, modeling, Python, testing) | Each domain has one or two things only a check keeps honest: rows that carry `status` + `source`, a generated view with a drift guard, a read-only knowledge base. | as the domain needs |

## 3. The principles, each paid for once

1. **One home per fact.** Status, counts and baselines each live in one file; everything else
   links to it. Views are generated, and a drift guard fails CI when a twin is stale.
2. **Memory is budgeted and guarded.** A context file that grows past its budget fails a check;
   history lives in git, not in the file.
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
9. **Evidence in the PR, scratch outside the repo.** Verdict lines and test counts are pasted
   into the PR; proof folders and screenshots nobody references are never committed.
10. **Write for agents the way the research says works.** A skill's description is a pointer with
    its trigger words first; every step has a completion criterion; state the target behaviour,
    not the prohibition; delete instructions the model already follows; link, never paste.

## 4. Starting a new repo (the playbook)

1. **Create it private** where the workplace's convention allows a choice. Vendor assets,
   personal data and anything with a key never go public.
2. **Bootstrap.** In a Claude Code session in that folder, `/kit-start <kit path>`. It detects
   the stack, asks only for the gaps (purpose, vision, who rules, the domain, three ground rules,
   what recurs), rules the pieces with you, and writes them with their placeholders filled.
3. **Start warm.** Fill the RESUME HERE block with the first real NEXT ACTION before closing the
   session; the next `/resume` must be productive.
4. **First slice.** `/resume` (writes the brief) → `/orchestrator` → `/interview-me` the first
   spec → `/spec` → build on a branch → `/verify` → `/ship` → the owner merges → `/wrap-session`.
   A tracer bullet, not the whole feature.
5. **First retro.** After the first slice, `/retro`. Anything mechanical it finds becomes a guard
   or a hook, never a sentence in `CLAUDE.md`.
6. **Keep the kit upstream.** An adaptation lives in the repo's copy and wins by name. A generic
   improvement goes back to the kit (`HANDOFF.md` §2 says how, and what never travels).

**What not to do:** install a skill mega-pack (every description loads into every session; adapt
the two or three skills that fill a gap instead); let `CLAUDE.md` grow past about 120 lines
(procedures to skills, file-specific rules to `.claude/rules/`); commit evidence or scratch;
enable auto-merge; let an agent fan out subagents.
