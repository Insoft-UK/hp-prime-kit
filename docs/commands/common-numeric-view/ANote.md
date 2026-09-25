# ANote

The active app's note, a string, empty on a reset calculator.

| | |
|---|---|
| Syntax | `ANote` → string |
| Syntax | `ANote:=value` |
| Group | common-numeric-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ANote")` | `""` | [emulator](../results.tsv) |
| `LOCAL o; o := EXPR("ANote"); EXPR("ANote:=" + STRING(o)); RETURN EXPR("ANote");` | `""` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can assign it** (emulator): given its own value back, the empty
string, it was accepted. Text of its own was not tried.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AProgram](AProgram.md)
