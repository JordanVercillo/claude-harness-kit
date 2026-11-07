# Skill patterns: how `.claude` skills are shaped, composed and used

A skill is a markdown file that packages a repeatable workflow so Claude runs it consistently on
demand. This page: the file format, the seven design patterns, how sessions use skills, and how
to instantiate one for a new domain.

## 1. Anatomy of a SKILL.md

Location: `<repo>/.claude/skills/<skill-name>/SKILL.md` (+ optional helper scripts and a
`references/` folder beside it). Skills load only when the repo folder itself is the project
root: the number-one cause of "unknown command".

```markdown
---
name: <kebab-name>                     # what you type: /<name>; equals the folder name
description: <one sentence>. TRIGGER when: <concrete user phrasings>.
  SKIP if: <the adjacent-but-wrong case, and which skill handles it>.
user-invocable: true                   # or "Internal skill — use ONLY when called by X"
allowed-tools: [Glob, Grep, Read, Skill, Edit, Write, Bash]   # least privilege
---

<The workflow, written as instructions to Claude — numbered phases,
exact commands in fenced blocks, report formats spelled out verbatim.>
```

The `description` is the routing layer: TRIGGER phrases make it fire at the right moment; the
SKIP clause routes adjacent traffic to the right sibling. Adjacent skills that don't disambiguate
each other misfire on each other's traffic. A skill only the owner should start gets
`disable-model-invocation: true`; anything another skill calls stays model-invocable.

## 2. The seven patterns

1. **Orchestrator + internal workers.** One user-facing skill runs phases and delegates
   mechanical steps to internal skills that return structured blocks (not prose) with state
   FLAGS the orchestrator branches on.
2. **The Phase 0/5 memory sandwich.** Every orchestrator BEGINS by reading the project's
   PROJECT_CONTEXT and ENDS by updating it (status, next action, session log, journal). This wires
   the living memory into the workflow so it maintains itself.
3. **Determinism in scripts, judgment in prompts.** Facts come from a script (JSON out); the LLM
   formats, flags, decides. Generation gets bracketed: script-collect before, script-validate
   after, loop until valid. (Card: `deterministic-audit-scripts.md`.)
4. **Progressive disclosure, with a budget.** SKILL.md stays at or under 150 lines (the default; the
   `skill_budget` guard holds it); bulky detail lives in `references/` files beside it or in a
   script the skill names, read only when needed. A skill with no budget doubles in weeks with
   nothing watching, while the memory files, which have one, never drift.
5. **Draft/lock separation.** Content-authoring skills write `status: draft` and present for
   review; only the human flips to locked/approved. Spec-scale changes get a written spec with
   exit criteria before implementation.
6. **Runbooks with error playbooks.** Ops skills: silent pass-through on the happy path, lettered
   recovery options per failure, a symptom → fix table, secrets referenced by NAME only.
7. **Same-turn continuation.** Skills state explicitly: never end the turn on a bare audit or
   orientation report, and don't re-confirm a goal the invocation already stated. (Learned live:
   a partner skill "stalled" after its audit until this line was added.)

## 3. How sessions use them (the interaction model)

```
1. Open the repo folder as project root  → CLAUDE.md bootloader auto-loads
2. /resume: memory → health → the ledger → /groom (the owner unblocks the lane) → the draft
   brief → the grill (/interview-me walks the owner through it; a playback is confirmed)
3. /orchestrator runs the lane from the brief, one agent at a time (or /<domain>-partner for a
   one-domain session: Phase 0 reads PROJECT_CONTEXT, Phase 1 runs the audit worker)
4. Work happens in reviewable slices; audits/tests after each; /verify → review → /ship
5. /wrap-session writes the memory back (the review, the tech-debt sort, the journal, /dream,
   /retro when the harness fought back) — next session starts warm
```

The prompt stays tiny BY DESIGN: the repo carries the context. If a session needs a long opening
prompt, the context file is missing something: add it there once. Utility invocations
(`/<domain>-audit`, `/verify`) work standalone anytime; "continue with the session goal"
un-sticks a turn that stopped early.

## 4. Instantiating skills for a new domain

Copy `skills-domain/domain-partner/SKILL.md` and `skills-domain/domain-audit/SKILL.md` from the
kit; rename for the domain (`<x>-partner`, `<x>-audit`); point Phase 0 at the project's memory
file; write the domain's audit script from `audit_TEMPLATE.py` and the pattern card. Add the
two routing rows to `CLAUDE.md`, and `"Skill"` plus the runner to the allowlist in
`.claude/settings.json`.

## 5. Distribution: one template, adapted copies

The shared skills live once, in the kit. A repo gets a copy, and the copy is the repo's own: it
is adapted to that repo's workflow and wins by name. A diff against the kit cannot tell drift
from adaptation (every adapted copy carries its repo's own terms), so a copy is never retired
for being different. An improvement every repo wants is made in the kit, generically, and
reaches a repo when its owner re-copies it into the adaptation.
