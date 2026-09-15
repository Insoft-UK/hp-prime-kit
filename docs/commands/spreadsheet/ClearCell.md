# ClearCell

Empties the current cell, and answers 0 with the app active.

| | |
|---|---|
| Syntax | `ClearCell()` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ClearCell( )")` | `0` | [emulator](../results.tsv) |
| `EXPR("ClearCell()")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The two rows differ in whether the Spreadsheet was the active app**
(emulator), not in the space inside the brackets, which exists only so that
both answers could be kept: `results.tsv` keys a row by the exact text of its
call. [CellHasData](CellHasData.md) carries the account of the pair.

**With the app active it answers 0** (emulator), type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), the same as its pair.
What that 0 reports is not established: it may be the command's own success,
or the state of a cell that was already empty (unverified).

**It changes the calculator rather than only reporting on it** (HP help),
which is why it ran on the throwaway `Prime_1` and never on the user's own
machine. On a sheet reset before the run there was nothing to clear, so
nothing was lost either way.

**The probe is a cell with something in it** (unverified): run
[CellHasData](CellHasData.md), then this, then `CellHasData` again. Three
rows would show whether this command does anything and whether either answer
means what it seems to.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CellHasData](CellHasData.md) · [SUM](SUM.md)
