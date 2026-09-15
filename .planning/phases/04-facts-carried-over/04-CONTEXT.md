---
phase: 04-facts-carried-over
created: 2026-09-12
requirements: [FACT-01, FACT-02, FACT-03, FACT-04, FACT-05, CMD-06, TOOL-02, CHECK-04]
---

# Phase 4 context: Facts carried over

## What this phase is

Everything measured so far lives in seven pages of prose under
`docs/reference/`: 2,180 lines, 55 sections. Each of those pages is rewritten
as a topic page in the format Phase 1 fixed, so that every fact has an
identifier, one label saying how it is known, and exactly one place where it
is stated. The seven old pages go; a migration list says where every section
went.

## Decisions the user made

- **The reference pages become topic pages.** Each of the seven is rewritten
  into `docs/topics/<name>.md` in the new format, keeping the prose that
  explains, and the old page is removed in the same commit as its replacement.
  One fact, one place (FACT-02).
- **Three plans, by blocks.** 04-01 `ppl` and `formats`, which is where the
  entries already point; 04-02 `interface`, `apps` and `micropython`; 04-03
  `deploy` and `libraries`, plus the lint rules citing their fact identifiers.

## Decisions taken here, and why

- **The topic names stay the ones people already know**: `ppl`, `formats`,
  `interface`, `apps`, `micropython`, `deploy`, `libraries`. `docs/topics/ppl.md`
  already exists with three facts and grows into the rewritten `ppl`.
- **Prose that is not a fact goes in the page's introduction**, before the
  first anchor, which is where the format allows free text. A section that is
  advice rather than measurement (most of `libraries`, the "which level"
  guidance) stays prose. Nothing is dropped silently: the migration list says
  "became fact X", "kept as prose in Y", or "dropped, because Z".
- **`unverified` items need no new `Kind`.** `Kind` is `rule` or `refuted
  hypothesis`; how sure we are is the `Known from` label, and `unverified` is
  one of the four. A "not measured" item becomes a fact whose statement says
  what is not known, labelled `unverified`, so that a model reading only the
  rules does not invent the rest (FACT-03).
- **The migration list is a work record**, `.planning/phases/04-facts-carried-over/MIGRATION.md`,
  one row per section of the seven pages. An index of topics for readers is
  Phase 9's job (READ-03).
- **Links are repointed in the same commit as each move.** Removing
  `docs/reference/` breaks 101 links in 34 files: `README.md` (12),
  `AGENTS.md` (10), `docs/start/` (11), `docs/tools.md` (5), the entries and
  the generated pages, `SKILL.md`, the examples' READMEs, and docstrings in
  `hpkit/emulator.py`, `program.py` and `numbers.py`. `tests/test_docs.py`
  fails until every one resolves, which is the check that this was done.
  Links inside `.planning/` are history and are left alone.
- **A fact keeps its evidence, not a pointer to the old page.** Today's topic
  facts carry a `Known from` label linking into the old reference page, which will not
  survive. The evidence paragraph says what was run, on what, and what it
  showed, in the fact itself.

## Claude's discretion

- How many facts a section becomes: a section that measures four independent
  things becomes four facts, one that measures one becomes one.
- The slugs, within the rule that an identifier never changes once published.
- The order of facts inside a topic page.

## Deferred

- An index of topics and facts for readers: Phase 9 (READ-03).
- `AGENTS.md` and `SKILL.md` are repointed so they resolve, not rewritten:
  Milestone 2 replaces them.
- Entries for the commands these facts concern: Phases 5 to 8. Phase 4 links
  a fact to an entry only where the entry already exists.

## Success criteria (from the roadmap)

1. A migration list maps every fact in today's seven reference pages to its
   new home, with none left out
2. The false hypotheses and the unverified items are entries with their own
   status
3. Every lint message names the fact identifier it comes from, and a test
   checks that every rule has one
4. The deploy page explains the send from the Connectivity Kit's content
   library, marked as done once
5. The mistakes models are known to make appear in the entries they concern
