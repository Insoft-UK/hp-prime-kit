# CellHasData

Says whether the current cell holds anything, and answers 0 on an empty sheet.

| | |
|---|---|
| Syntax | `CellHasData()` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CellHasData( )")` | `0` | [emulator](../results.tsv) |
| `EXPR("CellHasData()")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The two rows differ in whether the Spreadsheet was the active app when the
program ran** (emulator), not in the space inside the brackets. That space is
incidental: `results.tsv` keys a row by the exact text of its call, so the
second run needed a different spelling to keep both answers instead of
replacing one.

**With the app active it answers 0** (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). A calculator reset
before the run has an empty sheet, so 0 is the honest answer to the question
rather than a failure -- and that is what makes this row useful: the command
works and reports no data, where before there was no current cell to ask
about at all.

**It takes no arguments, which makes it the cleanest test of the rule**
(emulator). Nothing about the call could have been written wrongly, so the
difference between the two rows is the app and nothing else:
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**What it answers with data in the cell was not run** (unverified). That is
the row that would show 0 and 1 are its two answers rather than 0 being all
it ever says.

[ClearCell](ClearCell.md) is its pair and behaved identically in both runs
(emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ClearCell](ClearCell.md) · [SUM](SUM.md) · [AVERAGE](AVERAGE.md)
