# AFiles

The names of the files the active app holds, a list, empty on a reset calculator.

| | |
|---|---|
| Syntax | `AFiles` → list |
| Group | common-numeric-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AFiles")` | `{}` | [emulator](../results.tsv) |
| `EXPR(" AFiles")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**[DelAFiles](DelAFiles.md) called with nothing did not change it**
(emulator): the second row read it after that call was refused, and it was
still `{}`. There was nothing in it to delete.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AFilesB](AFilesB.md) · [DelAFiles](DelAFiles.md)
