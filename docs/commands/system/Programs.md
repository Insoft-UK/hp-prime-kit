# Programs

The names of the programs on the calculator, as a list of strings.

| | |
|---|---|
| Syntax | `Programs` → list |
| Group | system |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Programs")` | `{"HPKDOC"}` | [emulator](../results.tsv) |

## Behaviour

**It lists the programs by name** (emulator): on the calculator the batch
ran on, reset and holding only the batch's own program, it answered
`{"HPKDOC"}`.

**A program can find out whether another is installed** by looking for its
name here (emulator, for the list; that such a test works end to end was not
tried).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Notes](Notes.md) · [HVars](HVars.md)
