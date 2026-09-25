# HVars

The names of the variables created on Home, as a list.

| | |
|---|---|
| Syntax | `HVars` → list |
| Group | system |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HVars")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**It answered `{}` on a reset calculator** (emulator). That it lists
variables created on Home is read from its name (unverified): the row that
would have created one and listed it again was refused before it said
anything, as [DelHVars](DelHVars.md) records.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DelHVars](DelHVars.md) · [Programs](Programs.md)
