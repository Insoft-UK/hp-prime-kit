# SetIndep

Points a data set's independent column, refused on a reset calculator.

| | |
|---|---|
| Syntax | `SetIndep(Sn, Cn)` |
| Group | statistics-2var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SetIndep(S1,C1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Both arguments name things a reset calculator leaves empty** (emulator):
the app's first two-variable data set and its first column.
[Do2VStats](Do2VStats.md) records that `S1` cannot even be assigned to from a
batch.

**It refused identically to [SetDepend](SetDepend.md)** (emulator), its pair,
so nothing measured here separates the two commands.

**This is one of the two names that would unblock the group** (emulator). If
anything can attach data to `S1`, it is this and its pair, so they are the
first to probe once a way to fill a column is known.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SetDepend](SetDepend.md) · [Do2VStats](Do2VStats.md)
