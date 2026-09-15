---
phase: 07-app-functions
created: 2026-09-13
requirements: [CMD-10]
---

# Phase 7 context: App functions

## What this phase is

The 179 names the inventory files as `app function`: what a program calls to
drive one of HP's apps. None of them has an entry.

Measured before planning, the way Phase 6 was:

| | |
|---|---|
| names in scope | 179, none with an entry |
| HP gives a syntax string for | 162 |
| HP gives a worked example with a result for | 0 |
| the interpreter implements | 0 |

**Every entry in this phase waits for a batch.** Phase 6 could draft 21 of its
names against the interpreter first; here that number is zero, so no Result
column can be written before the calculator has answered. The order inside
every plan is forced: batch first, then write.

The 17 names HP gives no syntax string for are `Apps`, `DelInstruction`,
`Instruction`, `equation`, `randNorm`, `rectangle`, `rotation` and the seven
`zoom` commands, all in `geometry`, plus `Solve2×2` and `Solve3×3` in
`linear-solver` and `Solve` itself.

By group:

| group | names | with syntax |
|---|---|---|
| geometry | 84 | 70 |
| finance | 34 | 34 |
| spreadsheet | 22 | 22 |
| inference | 9 | 9 |
| statistics-1var | 6 | 6 |
| triangle-solver | 6 | 6 |
| function | 5 | 5 |
| statistics-2var | 5 | 5 |
| explorer | 4 | 4 |
| linear-solver | 3 | 1 |
| solve | 1 | 0 |

## Decisions the user made

- **A file name may add a suffix where two names differ only in case.** The
  entry keeps its real name in its title and the file becomes `Root-var.md`.
  Chosen over deferring it to Phase 8, over a subfolder for variables, and
  over one entry documenting both names. Already built: `docs.NAME_SUFFIX` is
  `-var`, the rule that a title equals its file name allows exactly that
  suffix, and the suite gained a break it must catch -- a title *wearing* the
  suffix, which would name a command nobody has.

## Decisions taken here, and why

- **The clash is measured, not assumed.** This filesystem is case-insensitive:
  writing `ROOT.md` makes `root.md` report as existing. That is what makes the
  suffix necessary rather than tidy.
- **Five pairs need it, and this phase writes the upper-case half of each**:
  `EXTREMUM`, `ISECT`, `ROOT`, `SLOPE` in `function` and `Solve` in `solve`.
  Their partners are app variables and belong to Phase 8, which is where the
  suffixed file gets written. Nothing in this phase is renamed later.
- **Two more pairs are not covered by that decision and must not be treated as
  though they were.** `ΣX` against `σX` in `statistics-1var` and `ΣY` against
  `σY` in `statistics-2var` are both app variables -- the sum and the standard
  deviation -- so a suffix meaning "the variable" separates nothing. They are
  Phase 8's problem entirely and Phase 8 has to choose again.
- **No row on the list is a true duplicate.** An earlier note in
  `06-CONTEXT.md` said those statistics groups held the same name twice. It
  was wrong, and reading the codepoints is what showed it: U+03A3 lowers to
  U+03C3, and a scan that compared names in lower case reported a collision
  that a scan comparing them as written does not.
- **Two names hold a character outside ASCII**: `Solve2×2` and `Solve3×3`,
  where the middle character is U+00D7. A file carrying it was created and
  read back identical, name and title, before anything was planned around it.
  Everything that writes them goes through a script with the encoding pinned,
  never a command line.

## Claude's discretion

- How many plans, and which groups travel together in a batch.
- **Whether a geometry command can be measured at all from a batch.**
  `geometry` is 84 of the 179, and its commands act on an app's own state --
  points, curves and a plot view. The harness runs a program on Home on a
  calculator reset before every run, so a command needing the Geometry app
  open with objects in it may answer nothing useful, or refuse. This is the
  phase's main risk and it is worth one small probe batch before a large one
  is planned.
- Whether a command that changes an app rather than answering a value gets an
  example at all, or the `*no value*` form Phase 5 added for exactly that.

## Deferred

- `app variable` (172): Phase 8, including the two Greek pairs above.
- `cas` (436), which Phase 2 decided is on the list, known to the linter and
  not documented.
- Phase 6 left probes that cost one round each and are worth folding into the
  first batch here: `NEG 5` and `INVERSE` are both refused and their working
  forms are unknown; the four upper-tail commands are refused through `EXPR`
  and want one direct call inside a program; `LineTan` wants its expression
  held back with `QUOTE`; and `ppl.check-last-error` wants one program
  carrying two deliberate errors far apart.

## Success criteria (from the roadmap)

1. Every app function on the list has an entry in the fixed format, with the
   app it belongs to
2. Every example in those entries has a Virtual Calculator result on file, or
   says why it cannot have one

Phase 6's third criterion has no counterpart here, and with no worked example
from HP for any of these names there would be nothing to compare against.
