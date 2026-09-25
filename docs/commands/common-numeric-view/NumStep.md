# NumStep

The step between the rows of the active app's numeric view, 0.1 on a reset calculator.

| | |
|---|---|
| Syntax | `NumStep` → real |
| Syntax | `NumStep:=value` |
| Group | common-numeric-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("NumStep")` | `0.1` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("NumStep"); EXPR("NumStep:=0.5"); r := EXPR("NumStep"); EXPR("NumStep:=" + STRING(o)); RETURN r;` | `0.5` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can set it** (emulator): set to 0.5, it read back 0.5. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NumStart](NumStart.md) · [NumZoom](NumZoom.md)
