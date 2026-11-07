---
name: interview-me
description: The relentless interview — pin down a rule, system, spec, plan or session brief until nothing load-bearing is ambiguous, every question with a recommendation; rulings one at a time, routing questions in rounds. TRIGGER when the user says "/interview-me", "grill me", "interview me", "poke holes", "let's rule <spec>", "let's be specific", when /resume reaches its brief grill, or when any seat is about to APPROVE a spec and finds load-bearing ambiguity. SKIP when the ambiguity is a FACT a tool can look up (read the code, the spec, the docs, the repo's research; never ask the owner what the repo already knows).
user-invocable: true
allowed-tools: [Read, Grep, Glob, Bash, AskUserQuestion, Edit, Write]
---

You are running **the interview**, the method used when a rule, system, spec, plan or session
must be certain before it is captured or started. Adapted from Matt Pocock's `grill-me` and
`grilling`. The goal isn't to fill a template. It's that **nothing load-bearing can be read two
ways** when the interview ends.

Where rulings are recorded is the repo's call: its `CLAUDE.md` or `specs/README.md` names the
home (a spec's decision log, a rulings file, a decisions doc). If none is named, the spec being
ruled gets a dated decision log, and a ruling with no spec goes to `notes/journal.md` as a dated
entry. Read that before the first question.

## The five laws

1. **One decision per question; rulings one at a time, routing in rounds.** A spec sitting, and
   any question whose answer reshapes another, is asked alone: ask, wait, incorporate, then ask
   the next. Routing questions (the brief grill, `/groom`'s grooming, `/retro`'s candidates,
   `/dream`'s summary) ask their **frontier**, the questions whose prerequisites are settled, in
   rounds of up to four, each with its REC first and worded so "yes" accepts it; a question that
   depends on one still open waits for the next round (the frontier of the design tree, never a
   leaf before its branch).
2. **Facts are researched; only DECISIONS are asked.** Before any question, check whether the
   repo already knows (a spec, a decision log, the docs, the code, a research note, the journal).
   If it does, cite it. Every question carries a premise, so check it first: the owner answers
   the question you asked, and an unchecked premise slips a claim past the one person who rules.
3. **Every question carries a RECOMMENDATION.** Always "here's the choice, my REC and why, what
   the alternative costs", never an open-ended "what do you want?". "Use your REC" is a valid
   answer. When the owner overrules a REC, ask the reason in the same ask (so it costs no second
   round), **capture it verbatim**, and replay it against the rulings already made before the
   next question. A pick over the REC with no reason is re-shown once ("is this the one you
   meant?"), with every option it had; the log keeps the first click, the re-ask and the pick
   that stands.
4. **A worked example is CHECKED.** When the owner gives an example, replay it against the rule
   as you understood it (arithmetic and all) and say which general rule you extracted.
5. **The shared-understanding gate.** You're done only when you've played the whole design back
   in your own words, the owner has confirmed it, and every number, format and route has a NAMED
   HOME (a decision row, a data column, a doc section). Anything still fuzzy gets one more
   question or stays an explicit open question with a REC. Never smooth it over silently. The
   playback comes after every reason, never before.

## The flow (a spec, a rule, a plan)

1. **Frame:** what is being pinned down and what's waiting on it (which spec, which slice, which
   seat's next run). For a thing with a shape (a vision, a system's parts, an order of events),
   ask the owner's own shape of it first, before any question inside it.
2. **Research sweep:** resolve every fact-shaped ambiguity from the repo first; report what you
   resolved, with citations. "We said previously" is searched (this repo, and the sibling repos
   the owner names) before the replay, and told where it was or that it wasn't.
3. **The decision tree:** list the open decisions in dependency order (answers that reshape later
   questions go first), then walk it: one question, one REC, one answer, capture, next. For a
   spec, the tree is its open-questions section, blocking ones first. Use `AskUserQuestion` with
   the REC as the first option, marked "(Recommended)"; price every clause of every option, not
   only its headline. When a question is about order, play the causal chain back as a numbered
   sequence first. **The record rule:** each answer is logged in the brief's `## Sitting log`
   (here, in `/groom`, in a mid-lane question): the question as the owner saw it, word for word
   and decoded, never the tool call's escapes, and the **label** of the option picked (or the
   owner's own words) with its description beside it as context, never a summary.
4. **Playback:** the whole design in your words, with every number and its home. When any
   answer touches a date, play back the whole dated timeline before capturing.
5. **Capture:** each ruling goes to the repo's home for rulings (date, ruling, **why**, with the
   owner's words). The open question leaves its doc: struck through with a pointer to the ruling,
   and the doc's text updated to state the ruling as decided. Acceptance criteria become
   observables a reviewer can verify; the spec's status moves (DRAFT → IN REVIEW → APPROVED when
   no blocking question remains; only the owner's word moves it to APPROVED). Then run the repo's
   spec lint, if it has one. A ruling that lives only in the transcript doesn't exist.

## The brief grill (a session brief)

Run by `/resume` after `/groom`, and by `/orchestrator` Phase 0 for a goal-started session. The
brief is a draft until the owner has been walked through it and confirmed a playback: the grill
is how the owner stays familiar with what each session does, and how a wrong lane is caught
before an agent is briefed.

1. **Walk-through**, in plain words: the goal; what gets built or ruled, and why now; the plan,
   each agent or skill and what it does; how we'll know it's done (the Done-when lines). Then the
   last wrap's tech-debt sort as `/groom` step 4 read it (its totals and the rows it moved), any
   of which the owner can move under Other.
2. **The questions** the brief's "Owner's decisions needed" still holds (the ones `/groom` didn't
   settle, or a brief `/orchestrator` wrote from a goal), in rounds (law 1), each in the form
   `/groom` step 5 gives and logged by the record rule.
3. **Playback:** the brief as the answers left it, in one last question the owner confirms. An
   answer that changed the lane, the scope or the plan rewrites the brief first (the machine line
   judged again, `/groom` step 1), and the playback shows the rewrite.

Done when the owner has confirmed the playback, every answer is in the brief's `## Sitting log`
(one heading; a later sitting appends under it), and the brief on disk is the one the owner
confirmed. Flow step 5's capture doesn't run here: an answer that changes a spec becomes a ruling
in the lane that consumes it, checked against the log.

## House rules

- **Numbers need homes in the same breath** they're ruled.
- **Disagree before capture, not after.** If a ruling collides with another ruling, a doc or a
  verified fact, say so in the next question; a collision is checked against the old ruling's
  Why, not its headline.
- **Never invent content to fill a gap.** An unanswered number stays PROPOSED or an open question.
- **A ruling that changes another repo** gets a handoff note for the owner to file there; it
  isn't changed from here.
