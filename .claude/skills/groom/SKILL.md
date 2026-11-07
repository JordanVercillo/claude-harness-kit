---
name: groom
description: Groom the backlog with the owner before a session's lane starts — what their machine must be ready for, what needs them (checked live), which spec sittings the next slices need, the tech-debt lane, the untriaged intakes; ask the blocking and important questions in rounds and return the lane their answers pick. TRIGGER when /resume reaches its groom step, when /orchestrator opens a session from a goal, or when the user says "/groom", "groom the backlog", "what needs me", "what's outstanding". SKIP for a question about one item (answer it), for ruling a spec (/interview-me).
user-invocable: true
allowed-tools: [Read, Glob, Grep, Bash, PowerShell, Edit, AskUserQuestion]
---

Backlog grooming is where the owner unblocks the session before it starts: everything that waits
on them is walked through once, in plain words, and asked where it is due, so a session never
idles on a decision the owner would have made in a minute, and the owner stays familiar with what
each session does. Every item is derived live from the issue tracker, the repo's deterministic
checks and the RESUME block, never stored. Nothing is ruled here: a spec question is routed to a
sitting, where `/interview-me` rules it one question at a time. This copy is the repo's own: name its labels and its machine instruments here as the repo earns them.

## 1 — The machine, first

Judged from the lane the session would take (a continuation, else the ➡️ NEXT ACTION's first
unblocked item): what the owner's machine must be ready for. The repo's `CLAUDE.md` or memory
names its instruments (an editor or app that must be open or closed, a service or runner that
must be up, a device plugged in, a long build that wants the machine idle); for each, say its
state now, what the lane needs, and what the owner does (nothing, open it, close it, start it),
with the reason. A repo with no such instrument says "nothing to do". When nothing else follows
a machine line of "nothing to do", say "Nothing needs you right now".

## 2 — What needs the owner, soonest-blocking first

From the ledger and the RESUME block, each item checked where it lives (one already done is a
stale fact for the wrap, never a question): the block's items in the owner's hands; the issues
carrying the repo's label for decisions waiting on the owner; open PRs ready for their merge (out
of draft, CI green, reviewed through their head); blocking open questions with the slice each
gates; the next manual step in the owner's hands (an install, a setup screen, a look at a
result); stragglers left in a finished phase's milestone. An item the block names as the owner's
decision that lacks the label gets it now, so the list and the block agree. Each item gets four
parts in plain words: **what** it is (an id always with its meaning), **why it needs the owner**
(a ruling, a merge, their hands), the **REC** with its reason, and what it **blocks** and when, in
the roadmap's order. An item that blocks nothing yet goes last and says so. An item the owner has
marked as their own lane (a `dnd` label or its equivalent) is listed as DND and never offered,
triaged or counted.

## 3 — The sitting schedule

Which spec sittings the roadmap needs, and when. For each spec with blocking open questions,
find the first roadmap slice (the 📍 phase first) that reads it. Show one table: spec · blocking
questions · the slice that waits · REC, where the REC is "rule it this session, as the lane or
its first step" when it gates the lane the session would take or the ➡️ NEXT ACTION's named
fallback, "its own sitting session before <slice>" when a slice in the 📍 phase waits on it, or
"Not now: due at <slice>". This is where new sessions get named. A repo without specs skips the
table and says so.

## 4 — The debt lane

The last wrap's tech-debt sort is the newest closed brief's `## Review` (`/wrap-session` step 0
writes it); when there is none, the live list under the repo's tech-debt label is the truth.
When the list isn't empty, one question: this session's lane is the ➡️ NEXT ACTION's, or a
tech-debt batch (its top items named, each with its cost), or the lane folds the debt items its
own files would touch anyway. A batch is one lane on one batch PR, each item by the agent that
owns it, one at a time. The owner can move any sorted item here, under Other.

## 5 — Choose the questions

- **Blocking:** it gates the lane the session would take or the ➡️ NEXT ACTION's named fallback,
  or it is owed before a slice in the 📍 phase; a straggler in a finished phase's milestone
  counts as the 📍 phase's.
- **Important:** an untriaged intake, or a decision waiting on the owner that is due in the 📍
  phase.
- **Not asked**, each listed with why: the machine (an instruction, step 1); a PR ready for the
  owner's merge and a manual step in their hands (actions, each named with what it unblocks); an
  item for another repo's session; an item due after the 📍 phase ("not asked: due at <slice or
  phase>"); a DND item, never; and **a "Not now" that named a slice** ("before <slice>", "due at
  <slice>"), wherever it was given (a `/resume`, a goal-started session, mid-lane), which waits
  until the `/resume` before that slice, listed with the deadline the RESUME block carries
  ("(Not now, <date>)"; `/wrap-session` step 0 writes it). This outranks Blocking and Important.
- **The form:** a decision whose REC and research already sit on its issue (a yes on a plan, a
  reading of a ruling, a pick between lanes the roadmap doesn't order) is asked directly. A spec
  question, or an intake whose `/spec` research hasn't run, is asked as a routing question ("Rule
  it this session, in a sitting / triage lane" or "Not now: due at <slice>"; REC "rule it this
  session" only when it gates the lane); a yes makes that sitting or triage the lane or its first
  step, and the ruling itself runs through `/interview-me` or `/spec` in that lane, never here.

## 6 — Ask them, in rounds

`AskUserQuestion`, up to four questions per round, the frontier first (the questions whose
prerequisites are settled; one whose answer depends on another waits for the next round:
`/interview-me` law 1). Each question is one decision and carries step 2's what, why and blocks
in its own text, since a click on an option the owner hasn't read isn't their pick. Options: the
REC first, marked "(Recommended)" and worded so "yes" accepts it, each with its description in
plain words and every clause priced; the realistic alternatives; and **Not now**, which leaves
the item waiting and the lane routing around it. An id named in an option resolves in the repo
(`grep -rnw '<id>'`) or the option says it in words. A pick over the REC follows law 3 (the reason
in the same question; a pick with no reason re-shown once). Record each answer by `/interview-me`'s
record rule: the question as shown, the pick, its description and any typed words, verbatim and
decoded; typed words are a second answer, replayed before they're used. A "Not now" goes in the
log only; an answer with an issue or PR also goes there as a comment.

## 7 — Hand back

Return to `/resume` (or report, when run alone): the lane the answers pick, the sitting schedule,
the debt decision, every answer for the brief's `## Sitting log` (run alone: the open brief's log,
else a comment on each item's issue), and the stale facts for the wrap. Done when every source in
steps 1–4 has been read, each item it holds is listed, the machine line states its calls with
their reasons, and every chosen question is answered or listed as not asked with why.
