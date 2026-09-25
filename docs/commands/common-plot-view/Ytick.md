# Ytick

The spacing of the marks on the y axis of the active app's plot, 1 on a reset calculator.

| | |
|---|---|
| Syntax | `Ytick` → real |
| Syntax | `Ytick:=value` |
| Group | common-plot-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Ytick")` | `1` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Ytick"); IFERR EXPR("Ytick:=2"); r := EXPR("Ytick"); THEN r := "refused"; END; EXPR("Ytick:=" + STRING(o)); RETURN r;` | `2` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can set it** (emulator): set to 2, it read back 2. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Xmin](Xmin.md) · [Ymax](Ymax.md) · [interface.draw-units](../../topics/interface.md#interface.draw-units)
