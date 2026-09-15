---
phase: 06-home-functions
created: 2026-09-12
requirements: [CMD-09]
---

# Phase 6 context: Home functions

## What this phase is

The 177 names the inventory files as `function`: what a person types on Home
and a program calls to compute something. 176 of them have no entry. `SIZE`
has one, with 7 measured rows, from the sample entries of Phase 1.

It is the largest phase of the milestone and the most uniform. Unlike
`drawing`, where the result was a screen and 15 entries had nothing an answer
could hold, **almost every name here returns a value**, so almost everything
is measurable. The work is volume, not invention.

Measured before planning, because Phase 5 learned this the hard way:

| | |
|---|---|
| names in scope | 177, of which 176 have no entry |
| the interpreter implements | 21 |
| HP's help gives an example with a result for | 19 |
| HP gives a syntax string for | 159 |

Five groups have **no** interpreter coverage at all: `probability` (28),
`special` (9), `hyperbolic` (6), `trigonometry` (6) and `units` (6). For
those, an entry cannot be written before the batch without inventing its
Result column, which is the order every plan here starts in.

## Decisions the user made

- **Six plans, by HP's own groups**, with the two large ones split so a batch
  stays near the size that worked in Phase 5, about thirty calls. Fewer and
  larger batches would cost fewer keypresses but a single syntax error has
  the whole program refused, which happened in Phase 5 and cost a round trip
  to isolate.
- **`SERIAL` gets a guard in the harness, not a note in a plan.** A short
  list of names whose answer is never stored, applied where the row is built.
  The entry says what the command returns and why there is no row. This is
  the same answer the project gave when `VERSION` put the calculator's serial
  number into `results.tsv`: code, not discipline.

## Decisions taken here, and why

- **The guard covers two paths, because there are two.** `collect()` builds a
  row for every case without exception, and it also hands the answer to
  `_report`, which prints it. A guard on the stored file alone would still
  put the serial on screen and into a session transcript. It goes where the
  row is built, and the report shows the same placeholder.
- **`SERIAL` still gets an entry.** It is on the inventory, so criterion 1
  wants it. It states what the command answers and that this kit does not
  store it, which is a fact about the documentation's own rules and worth
  reading.
- **The order inside a plan is: batch first, then write.** For the five
  groups with no interpreter coverage this is forced. For the rest it is
  still right, and Phase 5 arrived at it after two plans tried the other way.
- **Four names are Greek, not arrows.** `ΔLIST` is U+0394, `ΠLIST` is U+03A0,
  `ΣLIST` and `Σ` are U+03A3. They print identically on a Windows console,
  which is a display problem and not a data one, and they are three different
  commands. `ΠLIST` is filed under `list` while `ΔLIST` and `ΣLIST` are under
  `catalog`: one family, two homes, and the inventory is followed rather than
  corrected.
- **No two entries of this phase collide as filenames.** `SUPPRESS` is in
  `catalog` and `suppress` in `list`, so they land in different folders. The
  linter compares names without regard to case and cannot tell those two
  apart, which is a limitation it already documents.

## Claude's discretion

- Which names go in which of the six plans, within the split the user chose,
  and the order of the plans.
- How many examples an entry gets: enough to pin the edges a model would
  guess wrong, not one per sentence of HP's help.
- Whether a probability or a random function gets an example at all, given
  that `RANDOM`, `RANDINT`, `RANDNORM`, `RANDMAT` and `RANDSEED` answer
  something different every time. An answer that cannot repeat is not an
  example, and the entry says that rather than storing one run.

## Deferred

- `app function` (179) and `app variable` (172): Phases 7 and 8.
- **A name clash those phases have to solve before writing files.** Same
  group, same name but for case: `EXTREMUM`/`Extremum`, `ISECT`/`Isect`,
  `ROOT`/`Root`, `SLOPE`/`Slope` in `function`, and `Solve`/`SOLVE` in
  `solve`. On this filesystem they cannot both be `NAME.md` in one folder.
  `statistics-1var` and `statistics-2var` hold one such pair each, and this
  note used to call them the same name outright, which was wrong: they are
  `ΣX` against `σX` and `ΣY` against `σY`, the sum and the standard
  deviation, two different variables that collide only because U+03A3 lowers
  to U+03C3. Corrected 2026-09-13 by reading the codepoints. Found here while
  checking this phase; recorded so it is not discovered halfway through
  writing 179 entries.
- CHECK-04's audit, which still wants the entries of Phases 6 to 8 first.
- `cas` (436), which Phase 2 decided is on the list, known to the linter and
  not documented.

## Success criteria (from the roadmap)

1. Every name the inventory files under the Home functions has an entry in
   the fixed format
2. Every example in those entries has a Virtual Calculator result on file, or
   says why it cannot have one
3. Where HP's stated result and the emulator's answer differ, the entry says
   so

Criterion 3 is new: Phase 5 did not have it. With HP giving a result for only
19 of the 177, most entries will have nothing of HP's to disagree with, and
the criterion is met by the 19 that do plus whatever the batches contradict.
