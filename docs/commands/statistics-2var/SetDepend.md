# SetDepend

Points a data set's dependent column, refused on a reset calculator.

| | |
|---|---|
| Syntax | `SetDepend(Sn, Cn)` |
| Group | statistics-2var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SetDepend(S1,C1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It takes the same two kinds of argument as [SetIndep](SetIndep.md)** and
refused the same way (emulator), so this row does not separate them.

**Both name things a reset calculator leaves empty** (emulator), and
[Do2VStats](Do2VStats.md) carries the account of why the whole group is
blocked: `S1` cannot be assigned to from a batch at all.

**What it sets is the y column, where its pair sets the x** (HP help). A
two-variable data set needs both before a fit means anything.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SetIndep](SetIndep.md) · [Do2VStats](Do2VStats.md) · [Resid](Resid.md)
