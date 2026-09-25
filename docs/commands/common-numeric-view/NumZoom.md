# NumZoom

The zoom factor of the active app's numeric view, 2 on a reset calculator.

| | |
|---|---|
| Syntax | `NumZoom` → real |
| Syntax | `NumZoom:=value` |
| Group | common-numeric-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("NumZoom")` | `2` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("NumZoom"); EXPR("NumZoom:=2"); r := EXPR("NumZoom"); EXPR("NumZoom:=" + STRING(o)); RETURN r;` | `2` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("NumZoom"); IFERR EXPR("NumZoom:=4"); r := EXPR("NumZoom"); THEN r := "refused"; END; EXPR("NumZoom:=" + STRING(o)); RETURN r;` | `4` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can set it** (emulator): set to 4, it read back 4. The first
row set it to 2, the value it already held. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NumStep](NumStep.md)
