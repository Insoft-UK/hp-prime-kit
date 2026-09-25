# Notes

The names of the notes on the calculator, as a list.

| | |
|---|---|
| Syntax | `Notes` → list |
| Group | system |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Notes")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**It answered `{}` on a reset calculator, which holds no notes** (emulator).
That the list holds names, like [Programs](Programs.md), is inferred from
that neighbour (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Programs](Programs.md) · [HVars](HVars.md)
