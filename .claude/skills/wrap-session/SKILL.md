---
name: wrap-session
description: Close the session — review the brief, sort the tech debt, save the repo's durable memory, dream (consolidate it), tidy, run /retro when the harness fought back, commit, push, report. TRIGGER when the user says "/wrap-session", "wrap up", "end session", "save context", or meaningful work is done. SKIP if nothing durable changed.
user-invocable: true
allowed-tools: [Read, Edit, Write, Bash, PowerShell, Skill, AskUserQuestion]
---

Distil THIS conversation into the repo's memory: a map, not a transcript. `/resume` reads what
you write here, so write for a cold reader, and write the ➡️ NEXT ACTION as its instructions.
This copy is the repo's own: list what the repo regenerates before a commit here. The memory's shape and budgets are the repo's
(`CLAUDE.md`, the protocol paragraph in `notes/PROJECT_CONTEXT.md`); read them before editing.

0. **Session review.** Read the session brief: the newest open file in
   `~/.claude/projects/<project-key>/sessions/` (`/resume` §1 derives the key). A session
   started without `/resume` has none: write its Goal and Done-when now from the conversation,
   so the review has something to check against. Then, for each **Done when** line: ✅ with its
   evidence (a PR number and state, a check's result, a commit hash, a verdict, a file) or ⬜
   with why. Every ⬜ is carried or slotted, never dropped: into the ➡️ NEXT ACTION when it's the
   next lane's first step, otherwise into an issue or a spec question with its facts. For each
   decision made: who made it and where it's recorded (a spec row, an issue comment, a PR); one
   recorded nowhere is recorded now or flagged. A question for the owner the session raised and
   hasn't asked is asked now, under `/orchestrator` Phase 2's rule, before `## Review` is
   appended. Decisions still waiting on the owner go to the RESUME block, and each one's issue
   gets the repo's label for decisions waiting on the owner, so `/groom` asks it when it's due;
   a "Not now" that named a slice goes into the block with that slice, marked "(Not now,
   <date>)", the deadline `/groom` step 5 reads. Append the review to the brief as `## Review`.
   **The tech-debt sort:** this session's new issues, and every open chore in the 📍 phase's
   milestone not yet sorted, each go to one of three homes: the lead's next tech-debt batch (the
   repo's tech-debt label), the owner (the label above), or the slice or sitting it's owed to
   (named in its body). A chore already labelled, or already owed to a slice, keeps its home.
   The `## Review` always carries the sort's rows and one line of totals (tech-debt / the
   owner's / owed to slices), "no new chores" included, since `/groom` step 4 reads it there;
   the step 10 reply repeats them. A repo without an issue tracker sorts the roadmap's unticked
   chores the same way.
1. **Re-read the conversation.** Identify decisions made (with who made them), work completed
   (with evidence: verify verdict, test counts, PR/commit hashes, CI run), surprises, and the
   agreed next step.
2. **`notes/PROJECT_CONTEXT.md`:** rewrite **Status** and **➡️ NEXT ACTION** in place (the
   RESUME block stays short, ≤ 20 lines); add new key files/conventions; append one dated
   **Session log** line ending "**Left off:** …"; fix any fact this session proved stale.
   The ➡️ NEXT ACTION is `/resume`'s instruction: the next lane, what blocks it and whose hand
   that's in, and the first unblocked alternative. The open-items ledger itself lives in the
   issue tracker and the checks, derived at resume; don't copy it here. Stay inside the budgets
   the `memory_budget` guard enforces: the file ≤ 150 lines and the Session log ≤ 10 entries.
   Condense or drop the oldest entries to fit (a fact that lives nowhere else moves to the
   roadmap, the journal or an area README first); history lives in git.
3. **`notes/roadmap.md`:** tick what landed; move the **📍 we are here** marker if the position
   changed; keep "Immediate next step" identical to the ➡️ NEXT ACTION.
4. **`notes/journal.md`, then the dream.** A genuine surprise gets a numbered entry (situation →
   **The realization:** → `>` takeaway). Routine progress doesn't. Number it against the journal
   on `origin/main`, not the branch's copy (two sessions numbering against their own branches
   both claim the same number), and land it in the same PR as anything that cites it. Then run
   `/dream` (through the Skill tool): it decides whether this wrap gets the light pass alone or
   the full pass too (every fifth session, or when the 📍 moves a phase; the owner
   confirms its summary before anything is rewritten), and its changes ride this wrap commit.
5. **Retro, when the session fought the harness.** Run `/retro` (through the Skill tool) when any
   of these happened: a gate or check failed twice on the same class; an edit was reverted, or a
   commit carried a file nobody meant to stage; the owner answered a question the repo already
   knew; a tool call cost a round (a blocking call, a reload race, an output too big to read); a
   skill step was skipped or a rule misread; a session's memory had to be recovered from a
   branch or a transcript; an agent lacked a tool its brief assumed. When none did, the report
   says "no retro: no friction logged". It ranks the candidates, asks the owner each one with its
   evidence, the fix and its home, why it helps and its cost, in rounds, and applies what they
   OK: prose, a deletion or an allowlist line lands now and rides the open batch PR through
   `/ship` step 0 (where that tier is installed; otherwise a small PR of its own); a guard, hook
   or test becomes an issue carrying the deliberate-failure proof requirement; a lesson becomes
   the journal entry this wrap commits; a declined candidate is listed, not filed.
6. **Regenerate anything generated** (an index, a catalog, a view, a dashboard) with the
   generator `CLAUDE.md` or `PROJECT_CONTEXT.md` names, so the committed copy can't drift; never
   hand-edit it. A generated page that is published somewhere (an artifact, a site) is
   republished in place, and its URL stays in PROJECT_CONTEXT's Key files.
7. **Checks before commit:** the harness guards where the repo has them
   (`uv run scripts/harness_guards.py`, or the equivalent its `CLAUDE.md` names) must pass, plus
   any lint `CLAUDE.md` names. A wrap may commit straight to `main`, and the guards check exactly
   what it edits (`memory_budget`), so a red guard is fixed here, never pushed.
8. **Tidy**, inside named bounds. Outside them the default is report-only: an instruction to a
   future agent is an action, just a delayed one, so anything beyond these bounds is listed for
   the owner, never done. Everything done here is listed in the report:
   - **Inside the repo:** `git status --short` shows only the memory files you're about to
     commit. A file it lists that this session's own tools wrote (a guard's JSON output, a
     verdict file, a screenshot no doc references) is moved to the scratchpad, unless it is kept or
     read again: that is local data, and it moves to the data home `CLAUDE.md`'s ground rules
     name (listed for the owner where they name none), never into the scratchpad this step clears.
     A file whose origin you don't know is listed for the owner and left alone. This session's
     unfinished work reaches a branch through `/ship`, never the wrap commit. `git stash list` is
     empty and `git worktree list` shows one worktree; anything else is reported.
   - **Branches:** a local or remote branch that `origin/main` already contains
     (`git log origin/main..<ref>` prints nothing) is deleted with `git push origin --delete`
     and `git branch -d`. That containment check is the authority: `-d` tests against the
     upstream, which the push just removed, so when it refuses a branch the check passed,
     `-D` is allowed in the same step, right after the empty `git log`. A branch with commits
     past `main` is listed with its PR, never deleted, whatever its PR's state says. A `wrap/*`
     branch another session left is deleted only after its memory is folded into a commit that
     is pushed.
   - **Session files:** the brief, with its `## Review`, moves to `sessions/closed/`; a handoff
     whose task this session finished moves to `handoffs/closed/`; the scratchpad is cleared (it
     sits outside every repo, and nothing in it is a source of truth).
   - **Any other repo this session touched:** the same checks, with its changes on a pushed
     branch. Report the result.
9. **Commit and push the memory.** On `main`, a memory-only commit goes straight in:
   `git add notes/ <regenerated files> && git commit -m "wrap-session: <one line>" && git push`.
   **A wrap off `main` rides a PR:** a session on another branch puts the wrap commit on its open
   PR; with none open, the commit rides the batch PR through `/ship` step 0, or a PR opened for
   it where that tier isn't installed. A wrap that lives only on an unmerged branch is memory
   nobody has: never leave a `wrap/*` branch without a PR.
10. **Reply with:** the session review (each Done-when with ✅/⬜ and its evidence), the
    session-log line, the ➡️ NEXT ACTION, any journal entry, the dream's summary (or "light
    dream: nothing to consolidate"), the retro line (its candidates, what the owner OK'd and
    where each landed, or "no retro"), the tidy result, the tech-debt sort (step 0's rows and
    totals), and the roadmap with the 📍 marker (phases as a compact list, ✅ done / 📍 here / ⬜
    next). Then three short parts for the owner:
    - **What changed:** in the work's own terms (for harness work, in how-we-work terms), not
      file names.
    - **What you can try:** something concrete to open, run or look at right now, with the one
      command or click. If nothing is new to try, say so.
    - **For next session:** what the owner's machine should be ready for, so they can prepare:
      the ➡️ NEXT ACTION's lane and what it needs open, closed or running, each with its reason
      (`/groom` step 1's machine item).
