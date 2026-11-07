# The harness kit

A folder of Claude Code skills, seats (subagents), hooks, rules and templates that turn any repo
into one that works well with an agent: every session starts warm from a living memory, nothing is
built without a spec, nothing merges without a check the agent ran and a reviewer who read the
diff cold, and the owner merges. Paste the pieces a repo needs, adapt them to its workflow, keep
the rest in the kit.

Generated from one canonical copy; nothing here is hand-edited. `CATALOG.md` is the inventory,
`HANDOFF.md` is how to carry the kit to another machine and what may and may not flow back.

## Sixty-second start

1. Put this folder somewhere stable (beside your repos, or `~/claude-harness-kit`).
2. Install the startup skill once, at user scope, so it works in every repo:
   copy `.claude/skills/kit-start/` to `~/.claude/skills/kit-start/`
   (Windows: `%USERPROFILE%\.claude\skills\kit-start\`).
3. Open the target repo in Claude Code and run:

   ```
   /kit-start <path to this folder>
   ```

   It shows the catalog, asks six questions about the repo's purpose and vision, recommends
   ADOPT / ADAPT / SKIP per piece, installs what you rule, and proves the install.
4. Begin with `/resume` (it grooms the backlog with you and grills you on the session brief before
   any work starts); end every working session with `/wrap-session` (it sorts the tech debt and
   consolidates the memory).

Prerequisites: Claude Code, git, Python 3.11+ with `uv` (or `python` plus `pyyaml`; the startup
skill writes whichever it finds into the hook commands). `gh` is optional (`/ship` uses it).

## What is in here

| Folder | Holds |
|---|---|
| `.claude/skills/` | the shared skills, ready to paste: `kit-start`, `resume`, `groom`, `wrap-session`, `dream`, `orchestrator`, `handoff`, `retro`, `diagnose`, `verify`, `spec` (+ validator), `interview-me`, `ship` |
| `.claude/agents/` | the shared seats, ready to paste: `code-reviewer` (the review gate), `kb-librarian` |
| `templates/` | the repo-shaped pieces with `{{…}}` placeholders: `CLAUDE.md`, `notes/`, `.claude/settings.json`, the two hooks, the rule, the guards, the PR template, `MERGE-POLICY.md` |
| `seats/` | domain-seat templates: the generic shape, plus SQL, data-modeling, Python and testing seats |
| `skills-domain/` | the domain-partner orchestrator and the deterministic audit worker with its script skeleton |
| `docs/` | the workflow, the skill patterns, the audit pattern card: read, never installed |

`CATALOG.md` has every piece with what it gives, when a repo wants it, and how to adapt it.
