# NumType

How the active app's numeric view is built, 0 on a reset calculator.

| | |
|---|---|
| Syntax | `NumType` → real |
| Syntax | `NumType:=value` |
| Group | common-numeric-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("NumType")` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("NumType"); EXPR("NumType:=1"); r := EXPR("NumType"); EXPR("NumType:=" + STRING(o)); RETURN r;` | `1` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can set it** (emulator): set to 1, it read back 1. What 1 changes
in the view was not looked at. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NumIndep](NumIndep.md) · [NumStart](NumStart.md)
