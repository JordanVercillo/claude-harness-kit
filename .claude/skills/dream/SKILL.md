---
name: dream
description: Consolidate the living memory the way sleep does — a light pass at every wrap (this session's lesson against the memory) and a full pass every fifth session or when the roadmap marker moves a phase (merge duplicate lessons, retire ones a check now enforces, generalize repeats into one convention, refresh stale lines), each with a summary the owner confirms before anything is rewritten. TRIGGER when /wrap-session reaches its journal step, or when the user says "/dream", "consolidate the memory", "clean up the journal". SKIP for saving one session's facts (that is /wrap-session).
user-invocable: true
allowed-tools: [Read, Grep, Glob, Bash, PowerShell, Edit, Write, Skill, AskUserQuestion]
---

The wrap writes memory one session at a time: facts, when a cue says so. Over weeks that memory
goes stale and repeats itself. Dreaming is the background pass over the whole corpus that keeps
it a map: it re-reads many sessions' lessons together, proposes what to merge, retire,
generalize or refresh, and rewrites nothing until the owner has confirmed the summary. The
`memory_budget` guard still holds; the journal stays append-only. This copy is the repo's own: name the repo's memory corpus here as it grows.

## The corpus

`notes/PROJECT_CONTEXT.md` (the RESUME block, Conventions, Key files) · `notes/journal.md` (the
numbered lessons) · `notes/roadmap.md`'s 📍 phase · the closed briefs' `## Review` sections since
the last dream (`~/.claude/projects/<project-key>/sessions/closed/`; `/resume` §1 derives the
key) · the guard script's docstring (the checks that exist), `.claude/hooks/` and the tests ·
`.claude/rules/` and the skills (where a lesson may already be a rule) · Claude Code's
auto-memory folder for this project (`~/.claude/projects/<project-key>/memory/`), when it exists.

## The light pass (every wrap, inside the wrap commit)

Take this session's journal entry, if any, and every fact the wrap changed, and answer four
questions in the report:
1. **Is it now enforced?** A lesson a guard, hook or test now catches gets, at the end of its `>`
   takeaway line, "(enforced by `<check>` since <date>)". The entry stays; the pointer tells the
   reader a check holds it.
2. **Does it supersede or repeat an entry?** The new entry's takeaway names the older one
   ("updates #NN"), and the older entry's takeaway gains "(see #MM)". The light pass never merges.
3. **Is a RESUME or Conventions fact stale?** Fixed in place (the wrap's own rule), and listed.
4. **The auto-memory folder:** when this session wrote or changed a memory file there, run the
   memory-consolidation skill the session lists, if it lists one; otherwise do its pass by hand
   (read each memory file, merge duplicates, fix stale facts, prune the index). List the merges
   and prunes.
Done when each question has an answer in the report; "light dream: nothing to consolidate" is one.

## The full pass (every fifth session, or when the 📍 moves a phase)

The cadence is counted from the RESUME block's "How to work" line, which carries the last full
dream's date: five dated Session-log lines since it (git holds the dropped ones), or the 📍
moving to a new phase in this wrap, triggers it. No date there yet (the first wrap after this
skill lands): write today's, and count from it. Five is the default; a repo's owner may rule
another number, and its home is that line and this one.

1. **Read the corpus** by section (long files by heading; the journal by entry).
2. **Draft the consolidation**, each item with its evidence, as one of five kinds:
   - *merge*: two lessons with one takeaway; the later entry's takeaway gains "merged into #NN"
     and the surviving entry's takeaway is widened to cover both;
   - *retire*: a lesson a check now enforces; the light pass's pointer, and the lesson leaves any
     one-line index of the journal the memory keeps;
   - *generalize*: three or more entries with one shape become one Conventions line in
     PROJECT_CONTEXT, each entry pointing at it;
   - *refresh*: a Conventions or Key files line the repo has outgrown, rewritten or deleted;
   - *keep*.
   Entries are never deleted or renumbered: an entry gains a pointer, nothing more.
3. **The summary for the owner:** one table (item · kind · evidence · the change), shown and
   confirmed in rounds (`/interview-me` law 1's routing shape), each kind's items as one question
   when they fit, the REC first and worded so "yes" accepts it; an item the owner declines stays
   as it is. Nothing is rewritten before the confirm.
4. **Apply** what the owner confirmed; write today's date into the "How to work" line as the last
   full dream; run the harness guards (`memory_budget`); the changes ride the wrap commit.

## Report

For the wrap's reply: the light pass's four answers, and for a full pass the confirmed table and
the new "last full dream" date. A fact the dream could not place (a lesson with no check, a
convention nobody cites) is listed as an open question with a REC, never smoothed over.
