---
phase: 09-guided-path-index-and-readme
created: 2026-09-16
requirements: [READ-01, READ-03, READ-04, READ-05, READ-06, CHECK-02]
status: approved
approved: 2026-09-16, all eight proposed decisions
---

# Phase 9 context: Guided path, index and README

## What this phase is

The way in. A person learns from zero on the guided path; a model loads one
index and finds any entry or fact from it; the README presents the
documentation before the tools; `AGENTS.md`, `SKILL.md` and the paste block
point at the documentation; and a check holds every example to having been
run, or to saying why it cannot be.

**It runs ahead of Phases 8 and 8.1, at the user's choice** (2026-09-16). The
roadmap has it depend on the finished reference, and the reference is not
finished: 42 app variables wait for Phase 8 and 66 names for Phase 8.1.
Nothing this phase builds has to wait for them. The index is generated from
the entries, so it takes in each new one as it is written, and every other
page links rather than lists. What does wait is the verification's count,
which is taken again when 8.1 closes.

Measured before planning, on 2026-09-16:

| | |
|---|---|
| entries | 598, of the 706 names that get one |
| facts | 117: 76 `G2`, 18 `emulator`, 23 `unverified`; 112 rules and 5 refuted hypotheses |
| examples | 800 |
| with a stored answer in `results.tsv` | 779 |
| `*no value*`, with the reason in the entry | 17 |
| measured by hand on the G2, with no stored answer | 4: `ROOT`, `SUM`, `SSS`, `Solve2×2` |
| with no answer and no reason | **0** |
| labelled `unverified` although a stored answer agrees | **21**, in 10 entries |
| `docs/commands/index.md` | 88 KB |
| every entry and fact as one line, with its link and summary | 69 KB, about 17,000 tokens at four bytes a token |
| suite | 12,091 passed, 0 failed |

## What is wrong today, found while measuring

**The guided path contradicts the reference in three places.**

- Step 2's table says `IF x = 1 THEN` "does not compare, or compares wrong".
  [ppl.equality-operators](../../../docs/topics/ppl.md#ppl.equality-operators)
  (emulator) measured that a single `=` in a condition compiles and compares.
- The same step says `hpprime lint` catches the first six rows of that table.
  The rule for the `=` was removed for flagging legal code, so it catches five.
- Step 6 says the linter does not know every builtin, so an invented command
  gets past it. Since Phase 2 it warns on any name that is not on the list.

**Two entries contradict what is on file.** `IF` says a single `=` is not a
comparison (unverified), against the same fact. `LOCAL` says its second and
third examples are "waiting for a batch", and both have agreeing answers
stored on 2026-09-12. One of them, `LOCAL za := 2, zb := 3; RETURN za + zb;`,
compiled on the Virtual Calculator as the body of a function, which bears on
[ppl.locals-initialised-one-line](../../../docs/topics/ppl.md#ppl.locals-initialised-one-line),
still labelled `unverified`.

**21 examples understate their evidence.** They say `unverified` while
`results.tsv` holds an agreeing answer, in `CASE`, `CONTINUE`, `DIM`, `IF`,
`IFERR`, `INSTRING`, `LOCAL`, `REPEAT`, `RETURN` and `WHILE`. By the Phase 3
decision `hpprime examples --relabel` moves only `HP help` to `emulator`, so
nothing was ever going to move these.

**Planning language reached the documentation.** 56 pages speak of a phase,
a round of work, keypresses as a cost, the throwaway `Prime_1` as the place a
batch ran, or the maintainer as "the user". 39 more say "this kit", meaning
the repository and its tools. "harness" is in 104 pages, "batch" in 139 and
"probe" in 158. A reader who did not follow the project cannot know what any
of those refer to.

**66 names have no phase.** Phase 5 deferred the 65 names of kind `variable`
to "Phases 6, 7 and 8", and none of those phases took them; `GET`, whose kind
the sources do not give, was never assigned. The README already says they
have no entries. They are Phase 8.1 now.

## Decisions the user made (2026-09-16)

- **The 66 names get their own phase inside milestone 1**: Phase 8.1, after
  Phase 8, with batches on the emulator the way Phase 8 runs. Chosen over
  documenting only the fifteen or so most used, and over leaving them out of
  the milestone.
- **The index a model loads first is one file with a link on every line**:
  every entry and every fact, one line each, in the llms.txt layout. Chosen
  over the same list without links, about 11,000 tokens but with every path
  left for the model to build, `-var`, Greek and arrow names included; and
  over a small map with one index per group, where a model has to guess the
  group and `LineTan` is filed under `catalog`.
- **The guided path keeps its six steps, in their order, rewritten**: a fact
  is linked where it is used rather than restated, the three errors go, step
  6 points at the model index rather than at `AGENTS.md` and `SKILL.md`, and
  `docs/start/` is checked like the rest of the documentation. Chosen over a
  shorter path that ends at the first program, and over a new structure.
- **Planning language comes out of the documentation, and a check keeps it
  out**, while "harness", "batch" and "probe" are explained once, in
  `format.md`. Chosen over rewriting every page into plain prose, and over
  leaving it as it is.

## Decisions proposed here, approved by the user on 2026-09-16

1. **The index is `docs/llms.txt`**, generated by `hpprime docs` beside
   `index.md` and failing the tests when stale, the same way. It lives inside
   `docs/` so the documentation can still be split out on its own. Its
   layout: a title; one paragraph on the four labels, the reference firmware,
   and `names.tsv` as the place to look up whether a name exists; a section
   per topic page, opening with that page's first sentence, with a line per
   fact giving its identifier, linked to its anchor, and its heading; then a
   section per group, with a line per entry giving its name, linked to its
   file, and its summary. Names without an entry are left out, because there
   is nothing to load. **Budget: 100,000 bytes**, enforced by the check, with
   room for the complete reference at an estimated 82,000.
2. **CHECK-02 becomes part of `hpprime docs --check`**: an example with no
   stored answer has to be `*no value*`, labelled `G2` with its evidence in
   the entry, or run through the interpreter. Today it reports nothing, and
   its job is to keep it that way: an example nobody has run cannot be
   committed.
3. **`--relabel` also moves `unverified` to `emulator`** where the stored
   answer agrees, and the 21 move; `G2` still never moves. The prose around
   them is read in the same step, `IF`'s single `=` and `LOCAL`'s "waiting for
   a batch" at least. Whether the stored `LOCAL` rows settle
   `ppl.locals-initialised-one-line` is decided from what was run rather than
   assumed: they put two initialised locals on one line, and the tutorial the
   fact cites wrote three.
4. **What a pattern catches unambiguously, the check refuses**: "phase" in
   any form, since every use in the documentation today is a planning one.
   The rest is rewritten by reading, because each word has a legitimate use
   elsewhere: a round trip, keypresses a program waits for, the user of a
   program, and `Prime_1` as the emulator's own name for its second
   calculator in `deploy.md`.
5. **"this kit" goes the same way** in the 39 pages, becoming "here" or the
   tool meant: the decoder, the interpreter, the linter. The documentation is
   meant to stand without the layer above it. This one was not in the
   question, so it is asked here.
6. **`docs/start/` joins the checked documentation**: its links, the rule
   that it does not point at the layer above it, and the planning words.
7. **The README leads with the documentation**: what it is and how a claim is
   labelled, where a person starts and where a model starts, then the tools,
   then working with an AI. **A test holds its numbers** to the documentation,
   so a batch that adds entries fails the suite until the README says so.
8. **`AGENTS.md`, `SKILL.md` and `docs/ai/prompts.md` point at `docs/llms.txt`
   first** and cite facts by identifier where they state one. §1 of the paste
   block keeps restating on purpose, since it is for a chat that cannot read
   files, but each line names its fact or entry, and anything the reference
   contradicts is corrected. Generating it is KIT-10, in milestone 2.

## Claude's discretion

- The wording of every rewritten page. The README goes to the user as a draft
  before it is committed, because it is the first page the HP forum sees.
- The number and order of plans. Proposed:
  - **09-01** the model index and the check for examples nobody ran:
    READ-03 and CHECK-02, decisions 1 to 3
  - **09-02** planning language out of the documentation, and the glossary:
    READ-04, decisions 4 and 5
  - **09-03** the guided path: READ-01, decision 6
  - **09-04** the README, and the pages above the documentation: READ-05 and
    READ-06, decisions 7 and 8

## Deferred

- The 42 app variables, to Phase 8; the 65 variables and `GET`, to Phase 8.1.
- The harness problems confirmed still open on 2026-09-16 (a batch lost to
  one infinity, a probe overwriting a stored row without a word, a row dated
  the day its batch was prepared) and the interpreter's silent answer to
  `9 MOD 4 + 100`. Each is a change to a tool, with its own decision, and
  this phase needs none of them.
- CHECK-04's open half: which facts a PC could catch and no lint rule does.
- A paste block generated from the documentation (KIT-10), and the rest of
  milestone 2.

## Success criteria (from the roadmap)

1. The guided path takes somebody from an empty folder to a program running
   on the calculator, linking to entries rather than restating them
2. One index, within its size budget, lists every entry and topic with its
   identifier and a one-line summary
3. The README presents the documentation first, and `AGENTS.md` and
   `SKILL.md` point at the new documentation until milestone 2 replaces them
4. The tests confirm that every example in the documentation has been run or
   says why not
