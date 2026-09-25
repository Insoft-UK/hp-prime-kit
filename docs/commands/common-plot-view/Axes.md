# Axes

A setting of the active app's plot view, 0 on a reset calculator.

| | |
|---|---|
| Syntax | `Axes` → real |
| Syntax | `Axes:=value` |
| Group | common-plot-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Axes")` | `0` | [emulator](../results.tsv) |
| `LOCAL o; o := EXPR("Axes"); EXPR("Axes:=" + STRING(o)); RETURN EXPR("Axes");` | `0` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more. Whether 0 means on or off is not known.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can assign it** (emulator): given its own value back, it was
accepted and read back the same. Another value was not tried.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Cursor](Cursor.md) · [GridDots](GridDots.md) · [GridLines](GridLines.md) · [Labels](Labels.md)
