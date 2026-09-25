# AVars

The names of the active app's own variables, a list, empty on a reset calculator.

| | |
|---|---|
| Syntax | `AVars` → list |
| Group | common-numeric-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AVars")` | `{}` | [emulator](../results.tsv) |
| `EXPR(" AVars")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**[DelAVars](DelAVars.md) called with nothing did not change it**
(emulator): read again after that call was refused, it was still `{}`.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DelAVars](DelAVars.md) · [HVars](../system/HVars.md)
