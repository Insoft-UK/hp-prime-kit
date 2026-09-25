# SUM

Adds up a list; refused unless the Spreadsheet app is active or named in front of it.

| | |
|---|---|
| Syntax | `SUM([Input])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SUM({1,2,3})` | `6` | G2 |
| `EXPR("SUM({1,2,3})")` | *error* | [emulator](../results.tsv) |
| `EXPR("Spreadsheet.SUM({1,2,3})")` | `6` | [emulator](../results.tsv) |

## Behaviour

**The first two rows are the same call and differ in one thing: whether the
Spreadsheet was the active app** (G2). With it active, typing this on Home
answers 6; from a batch with another app active, it is refused. The command
does not have to be typed in a cell -- selecting the app is enough.

**That answered the question this entry used to leave open** (G2). All
twenty-two names of the group were refused from a batch, and this entry once
said the cause was not established, having ruled out the obvious one: HP
files these under the Spreadsheet menu, but it files the four `explorer`
names under their own menu too and those answered. The rule is about the
**active** app, not the menu:
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**The rule holds inside a program too, which a second batch showed**
(emulator). With the app selected before `HPKDOC` was run,
[AVERAGE](AVERAGE.md) answered 4, and [CellHasData](CellHasData.md) and
[ClearCell](ClearCell.md) answered 0 where all three had been refused. So the
harness can measure these names, provided somebody selects the app first --
which it cannot do on its own, because it resets the calculator before every
run.

**Or the call carries the app's name** (emulator): the last row,
`Spreadsheet.SUM({1,2,3})` from a batch with the Function app active,
answered 6, [apps.qualified-names](../../topics/apps.md#apps.qualified-names). The other names of the group were not tried that way
(unverified).

**Only four of the twenty-two answer even then, and the other eighteen split
into two kinds** (emulator). `STAT1`, `STAT2`, `REGRS` and `AMORT` want a
range with data in it, and a calculator reset before the run has an empty
sheet. The twelve `Conf` and `Hyp` names sit in two menus on HP's list, the
Spreadsheet's and the Inference app's, so they may belong to the other one;
that is untested (unverified) and is the next probe for this group.

A program wanting to add a list without depending on an app has `ΣLIST`,
which is measured and answers 10 for the first four whole numbers
(emulator): [ΣLIST](../catalog/ΣLIST.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AVERAGE](AVERAGE.md) · [CellHasData](CellHasData.md) · [STAT1](STAT1.md) ·
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
