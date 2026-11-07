---
name: retro
description: Retrospective on a session's friction with the harness. Produces ranked candidates (a check, a hook, a seat line, a deletion, an issue), asks the owner each one with its evidence, why and cost, and applies what they OK. TRIGGER when the user says "/retro", "retro", "what should the harness learn from this session", or when /wrap-session finds friction (a check that failed twice on one class, a reverted edit, a question the repo could have answered, a skipped step).
user-invocable: true
allowed-tools: [Read, Grep, Glob, Bash, PowerShell, Edit, Write, Skill, AskUserQuestion]
---

The session is the evidence. You read where the harness cost more than it returned, or failed to
catch what it should have, and you propose the smallest fix in the right home. Adapted from Matt
Pocock's `retro`; the homes and the cost cap are ours: process must cost less than the work it
guards.

## 1 — Read the session

This conversation, or the transcript the user names. For each moment of friction, note the turn
and what it cost: tokens, a retry, a wrong edit, a question the user answered that the repo already
knew. Also read the last five entries of `notes/journal.md` and the checks the repo already runs
(the guard script and test command its `CLAUDE.md` names; the guard script's docstring is the one
list of its checks; CI), so you don't propose a check that exists.

## 2 — Classify each moment

| Category | The question | The usual home |
|---|---|---|
| Navigation | Was a file hard to find, or a dependency hidden? | a Map row in `CLAUDE.md`, a Key files row in `notes/PROJECT_CONTEXT.md`, a `.claude/rules/` pointer |
| Missing check | Could a lint, guard, test, build invariant or hook have caught it before a human did? | the guard script, a hook, a test |
| Standard missed | Did the reviewer miss something mechanical? A class found twice is closed by a check. | a guard; prose only for judgement calls |
| Steering bloat | Was an instruction ignored because the file around it is long? Would deleting it change anything? | delete it, or move it to a path-scoped rule or a skill |
| Tool economy | A call that cost more than it returned: a huge output, a parse failure, a blocking call, a slow tool, a permission prompt every session. | an allowlist entry in `.claude/settings.json`, a narrower command, an async pattern, a helper script |
| Information access | Did the agent lack something it needed: a log, a verdict, a build report, a service's state? | `/resume`'s health check, the SessionStart hook, a CLI |
| Memory | Did `PROJECT_CONTEXT` or the roadmap mislead, or go stale? | `/wrap-session`'s protocol, `/dream`, the `memory_budget` guard |
| Process cost | Did a gate cost more than the slice it guarded? | remove or shrink the gate |

## 3 — Rank and write

At most seven candidates, most severe first, each in this shape:

- **Category · severity** (BLOCKER: it caused a wrong result · MAJOR: it cost a round · MINOR).
- **Evidence:** the moment, quoted or paraphrased, with its cost.
- **Fix and home:** the smallest change, in the file that owns it. A deterministic check beats a
  sentence; a deletion beats an addition; a new sentence comes last.
- **Why it helps,** in one line the owner can weigh.
- **Cost:** what the fix adds to every session (tokens, seconds, a step for the owner). A fix that
  costs more than the friction it removes is listed as rejected, with the reason.

A rule nobody broke all session is a deletion candidate, not a success. A candidate that belongs to the harness kit the skills were pasted from, rather than to this repo, says so (its home is the kit, carried back as generic process, never with this repo's specifics).

## 4 — Ask the owner, then apply what they OK

Put the candidates to the owner in rounds (`/interview-me` law 1's routing shape), each as one
question with its evidence, the fix and its home, why it helps and its cost every session, the
REC first ("Apply it (Recommended)" or "Reject it (Recommended)" with the reason) and "Not now"
among the options; the answers are recorded by `/interview-me`'s record rule, in the brief's
`## Sitting log`. Then, in this session:
- a candidate the owner OKs that is **prose** (a skill, a `.claude/rules/` line, a seat line, a
  `CLAUDE.md` row), a **deletion** or an **allowlist** line is applied now and rides the open
  batch PR through `/ship` step 0 (opened if none is; a small PR of its own where that tier isn't
  installed), reviewed whole before it leaves draft;
- a **guard, hook or test** becomes an issue (with the repo's labels, if it uses them; the
  tech-debt label unless a slice owes it) carrying the deliberate-failure proof requirement: the
  check is seen failing on purpose before it counts; built in a HARNESS lane or the next debt
  batch, never inside the wrap;
- a **lesson** becomes the `notes/journal.md` entry the wrap commits;
- a candidate the owner declines, or answers "Not now", is listed in the report with their words
  and not filed.
Run from `/wrap-session`, the wrap's reply carries the list: each candidate, what the owner said,
and where it landed (a commit on the batch PR, an issue, the journal entry). Run alone, report
the same list and stop.
