# Xmin

The left edge of the active app's plot window, −15.9 on a reset calculator.

| | |
|---|---|
| Syntax | `Xmin` → real |
| Syntax | `Xmin:=value` |
| Group | common-plot-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Xmin")` | `−15.9` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Xmin"); IFERR EXPR("Xmin:=-5"); r := EXPR("Xmin"); THEN r := "refused"; END; EXPR("Xmin:=" + STRING(o)); RETURN r;` | `−5` | [emulator](../results.tsv) |
| `EXPR("C→PX(0,0)")` | `{160,109}` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Xmin"); EXPR("Xmin:=0"); IFERR r := {EXPR("Xmin"), C→PX(0,0)}; THEN r := "refused"; END; EXPR("Xmin:=" + STRING(o)); RETURN r;` | `{0,{1,109}}` | [emulator](../results.tsv) |
| `EXPR("Function.Xmin")` | `−15.9` | [emulator](../results.tsv) |

## Behaviour

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**`Function.Xmin` reads the same** (emulator): −15.9, with the Function app
active, [apps.qualified-names](../../topics/apps.md#apps.qualified-names). Whether another app's window reads differently through its own
name was not tried (unverified).

**A program can set it** (emulator): set to −5, it read back −5. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

**The drawing commands follow it** (emulator), because the forms without
`_P` count the plot window's own units, [interface.draw-units](../../topics/interface.md#interface.draw-units). With the window a reset
calculator has, `C→PX(0,0)` answers `{160,109}`; with `Xmin` at 0 it answered
`{1,109}`, and with `Ymax` at 0, `{160,0}`: the point moved to the window's
edge. So a program drawing in units draws somewhere else once anything has
changed the window.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Xmax](Xmax.md) · [Ymin](Ymin.md) · [interface.draw-units](../../topics/interface.md#interface.draw-units)
