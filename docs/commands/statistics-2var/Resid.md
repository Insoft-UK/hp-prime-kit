# Resid

The residuals of a fit, refused on an empty data set.

| | |
|---|---|
| Syntax | `Resid(Sn)` |
| Group | statistics-2var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Resid(S1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**`S1` could not be filled** (emulator), as [Do2VStats](Do2VStats.md)
records: assigning to it is refused and reading it back is refused, so this
command was asked about an empty data set.

**The refusal therefore says nothing about this command** (emulator), and
this entry does not pretend otherwise.

**Residuals need a fit, which needs data** (HP help), so even a working
command would have nothing to answer here.

[Do2VStats](Do2VStats.md) carries the account of the group and the probe that
would unblock all three of its data-set commands (emulator): assigning to
`S1` is refused, so none of them has been asked a question it could answer.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Do2VStats](Do2VStats.md) · [SetDepend](SetDepend.md)
