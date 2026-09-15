# Phase 1: Entry format and checks — Context

**Gathered:** 2026-09-11
**Status:** Ready for planning

## Phase Boundary

This phase delivers the format of a command entry, a fact and an example; one
page that explains it; a handful of real entries and facts in that format; and
the tests that hold every entry to it.

It does not build the list of names (Phase 2), run anything on the emulator
(Phase 3), or carry over the current reference (Phase 4). The sample entries
and facts are the only content it writes.

Requirements: CMD-03, CMD-04, CMD-07, READ-02, CHECK-01, CHECK-03, CHECK-05.

## Decisions

Locked by the user on 2026-09-11.

### One file per command, with generated group pages

- Every command has its own Markdown file. That file is the source, and the
  only place its content is written.
- A page per group is generated from those files, with the group's entries in
  full, for reading straight through.
- An index is generated from them: every name with its one-line summary.
- A test fails when a generated page differs from what the generator would
  produce now.

### The mixed entry

In this order:

1. The name, as the title.
2. One sentence saying what it does.
3. Fixed fields: the syntax (every form, with what it returns), the group, and
   whether `hpprime run` implements it.
4. The examples, each with its result and how that result is known.
5. Behaviour: a short paragraph for the edges and the errors, each statement
   with its source.
6. What models get wrong, when that is known, and where it was seen.
7. Related entries.

The mockup the user chose (layout only; its status labels were illustrative):

```
# LEFT
The first n characters of a string.

Syntax     LEFT(str, n) -> string
Group      strings
Runs on PC yes (hpprime run)

LEFT("HP Prime",2)  -> "HP"        emulator
LEFT("HP Prime",0)  -> "HP Prime"  G2

Behaviour
A count of 0 or less, or past the end,
gives the whole string, not "" (G2
2.4.15515; HP's help agrees for n <= 0).
MID with a length of 0 does the opposite.

Models get wrong  LEFT(s,0) is not ""
Related           RIGHT, MID
```

## Claude's Discretion

Decided here, open to the user's review.

### How an entry states how it is known

- Four labels, always the same words:
  - `G2`: measured on a physical G2, firmware stated
  - `emulator`: run on the Virtual Calculator, firmware stated
  - `HP help`: stated in HP's built-in help, dump version stated
  - `unverified`: none of these, and it says where it came from
- Every example carries exactly one label. Every sentence in Behaviour that
  states a fact ends with its label, or with more than one when sources agree
  ("G2; HP help agrees").
- A label points at its evidence: a G2 label at the record of what was run, an
  emulator label at the stored result, an HP help label at the topic in the
  dump, an unverified label at its source.
- Nobody writes an entry-level label by hand. The index and the group pages
  show each entry's weakest label, computed, in the order G2, emulator, HP
  help, unverified.

### How it renders

- Fields and examples are Markdown tables. Aligned plain text collapses into
  one line when GitHub renders it, and a table is also the easiest thing for a
  test to parse.
- The examples table has three columns: call, result, known from. The call and
  the result are PPL in backticks, the result written the way the calculator
  displays it.

### Identifiers

- A command's identifier is its name as PPL spells it: `LEFT`, `TEXTOUT_P`,
  `FOR`. A statement is named by its first keyword (`FOR`, `IF`, `IFERR`), with
  the full form in its syntax field.
- App functions and app variables are qualified by their app, as in
  `Function.AREA` and `Function.Xmin`, because several apps share names. That
  applies from Phase 7.
- A fact's identifier is its topic plus a short slug, as in `ppl.local-limit`
  or `deploy.ck-mirror`. A hypothesis found false is a fact like any other,
  phrased as what is true and marked "not a rule".
- An identifier never changes once published. A rename leaves the old one
  pointing at the new.

### Folders

| Path | What it holds |
|---|---|
| `docs/commands/<group>/<NAME>.md` | the source entries |
| `docs/commands/<group>.md` | generated: the whole group on one page |
| `docs/commands/index.md` | generated: every name, one line each |
| `docs/topics/<topic>.md` | platform facts, each with its identifier. Phase 4 fills them; Phase 1 creates only the one its sample facts need |
| `docs/format.md` | the page that explains the format |

- The current `docs/reference/`, `docs/start/` and `docs/tools.md` stay as they
  are until Phases 4 and 9 replace them. The kit layer, when it comes, goes in
  `kit/`.
- Group names follow HP's help, in lower case (`strings`, `loops` and so on).
  Phase 2 fixes the full list; Phase 1 uses only the groups its samples need.

### Tests and the generator

- New tests in `tests/`, standard library only, run by `tests/run_all.py`:
  - the format: fields present and in order, a label on every example
  - identifiers: unique, and every reference resolves
  - direction: nothing under `docs/` mentions the kit
  - links: the existing link check, extended to the new folders
  - generated pages up to date
  - for a command the interpreter implements, its examples run through the
    interpreter and give the stated result
- The generator is a small standard-library script. It is run by hand, and the
  test compares its output with what is committed.

## Specific Ideas

- Sample commands: `LEFT` and `SIZE`, which the interpreter implements and
  which carry measured edges; and `FOR`, a statement.
- Sample facts: the `LOCAL` limit (`ppl.local-limit`) and one hypothesis found
  false (`RETURN` inside `FOR` is allowed).

## Existing Code Insights

- `tests/test_docs.py` already checks that every relative link resolves:
  extend it rather than add a second link check.
- `hpkit/compare.py` evaluates a single call through the interpreter
  (`interp.Parser(interp.lex(expr)).expr()` and `Machine().evaluate`); the
  example runner can do the same.
- `tests/test_hpdocs.py` already runs HP's examples through the interpreter and
  judges a result as the same number or a refusal; its comparison is the
  starting point for checking an entry's examples.

## Deferred Ideas

- Emulator results as evidence: Phase 3.
- The full list of names, and the linter reading it: Phase 2.
- Carrying over the current reference: Phase 4.
- A converter for agents other than Claude Code: after milestone 2.

---
*Phase: 01-entry-format-and-checks*
*Context gathered: 2026-09-11*
