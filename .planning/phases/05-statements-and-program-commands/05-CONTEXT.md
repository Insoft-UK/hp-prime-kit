---
phase: 05-statements-and-program-commands
created: 2026-09-12
requirements: [CMD-08]
---

# Phase 5 context: Statements and program commands

## What this phase is

The first phase that writes entries at scale. 112 names: 14 statements and 98
program commands, in the format Phase 1 fixed, with their examples run on the
Virtual Calculator by the path Phase 3 built and their platform facts linked
from the topic pages Phase 4 wrote.

Until now the documentation has had five entries. This is where it stops being
a sample.

## Decisions the user made

- **A group at a time, written and then verified.** One plan per block of
  related groups: the plan writes those entries, then one emulator batch runs
  their examples, then the suite has to be green before the next plan starts.
  No group is left half done, and a mistake in the format shows up after
  fifteen entries rather than after a hundred.
- **`drawing` gets entries with no runnable example.** Its 35 commands paint on
  the screen, and the emulator gives back no value that `results.tsv` could
  hold. Each entry says so in the words the criterion allows -- "or says why it
  cannot have one" -- and leans on the facts in
  `docs/topics/interface.md` for what is measured about the screen.

## Decisions taken here, and why

- **The first batch carries two probes of its own**, which the user approved
  when Phase 4 closed: one program with `IF a = 1 THEN` and one with a bare
  `END`. They settle `ppl.equality-operators` and `ppl.end-semicolon`, the two
  facts labelled `unverified` that two lint rules rely on. They cost nothing:
  the batch is already going to the emulator.
- **HP's syntax is the starting point, not the evidence.** 109 of the 112
  names carry a syntax string from HP's help in `names.tsv`. An entry begins
  from it and from the help's own example where there is one, and every
  example is labelled `HP help` until a batch moves it to `emulator`, exactly
  as the five sample entries did.
- **An entry with nothing measured is still written.** It states what HP's
  help says, labelled `HP help`, and says what has not been run. A missing
  entry is worse than one that says how little is known.
- **The group pages and the index are regenerated at the end of each plan**,
  not per entry: `hpprime docs` is one command and the tests catch a stale
  page.

## Claude's discretion

- Which groups go together in a plan, and in what order, within the rule that
  a plan is one batch's worth of keypresses.
- How many examples an entry gets. Enough to pin the edges that a model would
  guess wrong, not one per sentence of HP's help.
- The wording of a "Models get wrong" section, and whether an entry has one:
  only where there is a record.

## Deferred

- `function` (177), `app function` (179), `app variable` (172) and `variable`
  (65): Phases 6, 7 and 8.
- The audit CHECK-04 still wants -- which facts a PC could catch and no lint
  rule does -- which needs these entries in place first.
- Any new lint rule these entries suggest. Writing one is a change to the
  tool, and it goes through its own decision rather than riding along with a
  page.

## Success criteria (from the roadmap)

1. Every name the inventory files under statements and program commands has an
   entry in the fixed format
2. Every example in those entries has a Virtual Calculator result on file, or
   says why it cannot have one
3. The tests pass with the new entries included
