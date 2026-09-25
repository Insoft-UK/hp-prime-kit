# AProgram

The active app's program, a string, empty on a reset calculator.

| | |
|---|---|
| Syntax | `AProgram` → string |
| Syntax | `AProgram:=value` |
| Group | common-numeric-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AProgram")` | `""` | [emulator](../results.tsv) |
| `LOCAL o; o := EXPR("AProgram"); EXPR("AProgram:=" + STRING(o)); RETURN EXPR("AProgram");` | `""` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more. That it is the source of the app's program is inferred from the name and from an empty string on an app that has none.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can assign it** (emulator): given its own value back, the empty
string, it was accepted. Assigning source to it, and whether the app then
runs that source, was not tried.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ANote](ANote.md) · [apps.hooks](../../topics/apps.md#apps.hooks)
