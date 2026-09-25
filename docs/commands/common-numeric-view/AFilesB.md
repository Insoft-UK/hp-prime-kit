# AFilesB

A second list of the active app's files, empty on a reset calculator.

| | |
|---|---|
| Syntax | `AFilesB` → list |
| Group | common-numeric-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AFilesB")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more. How it differs from [AFiles](AFiles.md) is not known.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AFiles](AFiles.md)
