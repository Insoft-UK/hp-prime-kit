---
phase: 08-app-variables
created: 2026-09-14
requirements: [CMD-11]
---

# Phase 8 context: App variables

## What this phase is

The 172 names the inventory files as `app variable`: what a program reads or
sets to drive one of HP's apps from the outside. None of them has an entry.

Measured before planning, the way Phases 6 and 7 were:

| | |
|---|---|
| names in scope | 172, none with an entry |
| HP gives a syntax string for | 4 |
| HP gives a menu path for | 0 |
| HP gives a worked example with a result for | 0 |
| the interpreter implements | 0 |
| rows in `results.tsv` naming one | 0 |

**Every entry in this phase waits for a batch**, as in Phase 7. The list
supplies a name and an app and, for 168 of the 172, nothing else -- no
syntax, no menu, no example. That is less than Phase 7 had, where 162 of 179
came with a syntax string.

By group:

| group | names |
|---|---|
| finance | 68 |
| inference | 50 |
| statistics-1var | 16 |
| statistics-2var | 12 |
| triangle-solver | 7 |
| advanced-graphing | 6 |
| function | 5 |
| spreadsheet | 4 |
| linear-solver | 2 |
| sequence | 1 |
| solve | 1 |

**Two apps arrive that Phase 7 never touched**: `advanced-graphing` and
`sequence`. Everything known about the other nine comes with them from
Phase 7, including which of their functions answer.

## What Phase 7 hands over

**An app's functions answer only while its app is active**
([apps.function-needs-active-app](../../../docs/topics/apps.md#apps.function-needs-active-app)),
and the rule survives inside a batch program: the user selects the app, the
harness runs, and the calls answer. **Whether the same holds for reading a
variable is not known**, and the two measurements that exist disagree in an
interesting way: `EXPR("F1")` answered −4 from Home with no app active, while
`S1` refused both to be read and to be assigned. So a variable may be
readable from anywhere, or `S1` may be the exception, or the two may differ
because one had been written to. One probe separates them.

**`F1` takes the evaluated value, not the expression.** `F1:=X^2-4` leaves
`F1` holding a number. Anything in this phase that looks like it stores an
expression needs its assignment measured, not assumed.

Carried over unchanged: the `EXPR` wrapping that costs one row instead of a
whole batch when a call is doubtful; the Check button reporting the **last**
bad line rather than the first
([ppl.check-last-error](../../../docs/topics/ppl.md#ppl.check-last-error));
the 160-character answer width with its cut marker; `NEVER_STORED`, which
keeps `SERIAL` and `VERSION` out of the file in code rather than by care; and
the date on a stored row being the day the batch was **prepared**.

## What is different about a variable

**A variable has no arguments, so the probe has a different shape.** A
function is measured by calling it; a variable needs reading, setting and
reading back -- three rows a name, and 172 names is 516 rows against the 623
the whole file holds today. The batches cannot simply be Phase 7's with
different names in them. Deciding what a minimal useful row set is, per
group, is the first planning question.

**`SOLVE` is filed as an app variable and carries a function's syntax**:
`SOLVE(En,Var[,Guess])`. [Solve](../../../docs/commands/solve/Solve.md) was
refused in five forms and is the one name in Phase 7 whose group answers
nothing at all. This is the likeliest explanation on the table, and it costs
one row. Worth being the first thing measured in the phase.

**The other three with a syntax string are `CFData`, `ColWidth` and `Row`**,
and two of those three list several names in one string
(`ColWidth RowHeight Row Col Cell`), which is a menu line rather than a
syntax. Treat the four as a hint, not as documentation.

## Risks, each with what would settle it

**22 names carry non-ASCII characters** -- the subscripts U+2081, U+2082 and
U+2083, and the Greek U+03A3, U+03BC, U+03C0 and U+03C3, in names such as
`ΣXY`, `Mean₁` and `σX`. Phase 6 measured that a
private-use codepoint (U+E003) cannot be typed through the editing channel,
while U+00E1 and U+00D7 both survive. None of these 22 is private-use, so
they should behave like `Solve2×2` did, but **that is a prediction and the
phase should not be planned on it**: create one such file, read it back, and
compare bytes before writing 22 of them.

**7 names collide with an existing entry by case alone**: `Extremum`,
`Isect`, `Root` and `Slope` against the Function app's commands, `Alpha`
against `ALPHA`, `Inter` against `inter`, and `SOLVE` against `Solve`. The
scheme for this is already built and tested -- the file takes the `-var`
suffix, the title keeps the true name -- so this is a known cost, not an open
question.

**A variable that holds app state may answer nothing useful on a reset
calculator.** The harness resets `Prime_1` before every run, so every app
starts empty; `H1`, `S1` and `F1` all did in Phase 7. A read of `MeanX` on an
app with no data is a refusal or a zero, and neither says much. Whether the
user must fill an app by hand first -- as they did for `F1` -- is the second
planning question, and it decides how many rounds this phase needs.

## Constraints that do not change

The calculator's serial number is never committed. Batches run on `Prime_1`,
never on the user's own `Prime`. `results.tsv` is written by
`hpprime examples` and never edited by hand. HP's help prose is not copied,
only names and syntax. Nothing is pushed to `main` without asking.
