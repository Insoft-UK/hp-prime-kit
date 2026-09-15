# Phase 2: Command inventory — Context

**Gathered:** 2026-09-11
**Status:** Ready for planning

## Phase Boundary

This phase delivers the list of every PPL name as data in the repository,
reconciled up to firmware 2.4.15515, with every name saying where it came
from; the index by name and by HP's grouping, generated from that list; and
`hpprime lint` flagging a call to a name that is neither on the list nor
defined in the program.

It writes no entries: those are Phases 5 to 8.

Requirements: CMD-01, CMD-02, CMD-05, TOOL-01.

## Decisions

Locked by the user on 2026-09-11.

### The sources

- HP's Command Tree 13217, already read, is the base.
- `commandslist.zip` from hpcalc.org (84,059 bytes, 2019-03-24, by Frank P):
  the command tree of firmware 2.1.14181, exported as a spreadsheet and as
  text. It covers what was added between 13217 and 2.1.14181.
- The G2 firmware package 2.4.15515 from hpcalc.org (10,074,224 bytes,
  2025-09-15). Only its release notes are read, for what changed between
  2.1.14181 and 2.4.15515. Nothing in it is installed or run.
- All three stay outside the repository. The repository keeps names, syntax,
  categories and where each name came from.

### A name the linter does not know

- Files linted together (`--set`): a call to a name that is neither on the
  list nor defined in any of the files is an ERROR.
- A single file: it is a WARNING, because the file may be calling a function
  that another program exports.

## Claude's Discretion

Decided here, open to the user's review.

- **CAS names are on the list** as known but not documented, so the linter
  does not flag them. They get no entry: CAS is out of scope.
- **The list is a plain text table**, one name per line, tab-separated: the
  name, its kind (statement, command, function, app function, app variable,
  CAS), HP's group, its syntax as HP writes it, and its source (13217,
  2.1.14181, or the 2.4.15515 release notes). Plain text keeps a change to the
  list readable in a diff.
- **App functions and app variables** are listed qualified by their app,
  `Function.AREA`, and the linter accepts them with or without the app.
- **The generated index covers the whole list**, not only the entries written
  so far: a name with an entry links to it, a name without one says so. The
  index then shows how much of PPL is documented at any moment.
- **What a program defines**, for the linter: its functions, exported or not,
  their parameters, its `LOCAL` and `EXPORT` variables, and the calculator's
  own variables (`A` to `Z`, `L0` to `L9`, `M0` to `M9`, `G0` to `G9` and the
  rest the list names).
- **The rule is called `unknown-name`**, and the hand-kept `BUILTINS` set in
  `hpkit/lint.py` is replaced by the list.

## Existing Code Insights

- `hpkit/lint.py` judges one line at a time with regular expressions, over a
  copy of the source with string contents and comments emptied
  (`_strip_noise`). It already collects exported names for `--set`. The new
  rule fits that shape: collect what each file defines, then check its calls,
  and with `--set` collect across all the files first.
- `lint.BUILTINS` is kept by hand and used by the `one-based` rule, so that
  `RGB(0, …)` is not read as an index. The list replaces it.
- `tests/hp_examples_extract.py` documents how HP's help dump is read; the
  inventory's extraction belongs next to it, as a maintainer's step, not a
  dependency of the kit.

## Deferred Ideas

- Documenting the CAS commands.
- Checking the number of arguments of a call against the syntax.

---
*Phase: 02-command-inventory*
*Context gathered: 2026-09-11*
