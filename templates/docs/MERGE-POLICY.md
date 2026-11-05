# Merge & collaboration policy

*Two people now work out of this repo. This is how conflicts get handled.*

**The one rule that matters: a conflict is always reported to a human and never
silently resolved.** Everything below is detail.

---

## 1. How conflicts actually happen here

There is **one shared `main`** and both of us commit straight to it — no pull
requests. So a conflict shows up like this:

1. You work, commit, push → **rejected** (the other person pushed first)
2. You pull → **conflict**

Not a feature-branch merge. A pull conflict. That shapes everything below.

**The high-risk files are not code.** They're the ones *every* session writes:

- `notes/PROJECT_CONTEXT.md` — session log gets a new line every wrap
- `notes/journal.md` · `career/context/career-log.md` — append-only
- `INDEX.md`, `docs/environment/*` — regenerated on every wrap

Two sessions wrapping on the same day will collide in exactly these places.

---

## 2. Prevention (cheaper than any resolution)

| Habit | Why |
|---|---|
| **`git pull --rebase` before starting work** | Replays your commits on top of theirs — linear history, far simpler conflicts |
| **Push immediately after `/wrap-session`** | An unpushed commit is a future conflict sitting on your disk |
| **Small, frequent commits** | A 1-file conflict is a 2-minute fix; a 20-file one is an evening |
| **Stay in your lane** | {{OWNER}}: `{{OWNER_LANES}}`. {{COLLABORATOR}}: `{{COLLABORATOR_LANES}}`. Overlap is the memory files. |
| **Say when you're in it** | "I'm working in the repo tonight" prevents most of this entirely |

**Recommended one-time setting** (not applied — your call):

```bash
git config pull.rebase true
```

Currently `false`, meaning plain merge. Rebase is better for append-heavy files
and keeps history readable.

---

## 3. The absolute rules

**Always:**
- **Report every conflict** in the format below, *before* touching it
- **Stop and wait** for a human decision — a conflict is a question, not a task
- **Preserve both sides** until told otherwise

**Never — no exceptions:**
- `git push --force` / `--force-with-lease` on `main`
- `git reset --hard` when it would discard someone else's commits
- Blanket `git checkout --ours` / `--theirs` to "make it go away"
- Resolve by deleting the other person's work because yours looks more complete
- Commit a file still containing `<<<<<<<` markers

---

## 4. Resolution by file type

**The type determines the answer. Classify first, then resolve.**

| Class | Files | Correct resolution |
|---|---|---|
| **Generated** | `INDEX.md`, `docs/environment/PYTHON_ENVS.md`, `OLLAMA_MODELS.md` | **Never hand-merge.** Take either side to clear it, then **regenerate** (`/repo-index`). The file is an output, not a source. |
| **Append-only log** | `notes/journal.md`, `career/context/career-log.md`, session-log section of `PROJECT_CONTEXT.md`, `inbox.md` Done | **Keep BOTH sides**, ordered by date. Dropping either loses a real event or lesson. This is almost never a "pick one". |
| **Current state** | `PROJECT_CONTEXT.md` Status / ➡️ NEXT ACTION, `roadmap.md` ticks | **Human decides.** Usually the newer wins — but read the older side first; it may assert a fact still true that the newer one didn't know. |
| **Authored prose** | `resume.md`, career profile, specs, skills, docs | Semantic merge, reviewed by whoever wrote it. Never machine-blend two versions of a résumé bullet. |
| **Code** | `pipelines/ platform/ src/ tools/ scripts/` | Normal review; consult the lane expert (sql/python/llm/…). **Run the audit after** — a merge that compiles can still be wrong. |
| **Seeds & gold data** | `*/seeds/*.csv`, gold sets | **Highest care.** These carry semantics (`locked`, `review_status`, provenance). Never blind-merge; re-run validation after, and never let a merge flip a human review flag. |

---

## 5. The report format

When a conflict appears, produce exactly this, then **stop**:

```
=== MERGE CONFLICT ===
Pulling:   origin/main -> local main
Conflicts: <N> file(s)   |   Auto-merged cleanly: <M> file(s)

| File | Class | Your side | Their side | Recommendation |
|---|---|---|---|---|
| notes/journal.md | append-only | added #25 | added #25 | keep both, renumber |
| INDEX.md | generated | regen 07-19 | regen 07-20 | take either, then /repo-index |

Their commits being pulled in:
  <sha> <subject> (<author>, <date>)

RECOMMENDED COURSE OF ACTION
  1. <specific step>
  2. <specific step>
  Risk if wrong: <what gets lost>

Nothing has been resolved. Waiting on your decision.
```

Rules for the report: name **every** conflicted file, say what *each* side did
(not just yours), and give a recommendation **per file** — not one blanket
verdict. If a file is in the "seeds & gold" or "current state" class, say so
loudly; those are where a bad merge does invisible damage.

---

## 6. Procedure

1. `git pull --rebase` → conflict appears
2. **Report** (section 5). Stop.
3. On approval, resolve file-by-file per section 4
4. Verify before continuing:
   - `grep -rn "<<<<<<<" .` → must be empty
   - generated files regenerated, not hand-edited
   - if code or seeds changed: `/warehouse-audit`
5. `git rebase --continue`, then push
6. Report what was kept, what was dropped, and why

**Escape hatch:** `git rebase --abort` (or `git merge --abort`) puts everything
back exactly as it was. Nothing is lost by stopping. When unsure — abort, report,
ask.

**Recovery:** `git reflog` finds any commit that appears "lost". Committed work
is essentially never gone; say so before anyone panics.

---

## 7. For the person who isn't deep in git

You do not need to understand any of this. If a conflict appears, Claude will
tell you plainly:

> *"You and {{OWNER}} both changed the same file. Here's what each of you wrote —
> which should we keep, or should I keep both?"*

Answering that question is the whole job. Nothing is deleted while you decide,
and anything can be undone.
