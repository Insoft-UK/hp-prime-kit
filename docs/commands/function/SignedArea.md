# SignedArea

The Function app's stored area, and the only one of the five whose name is free.

| | |
|---|---|
| Syntax | `SignedArea` → real |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SignedArea")` | `0` | [emulator](../results.tsv) |
| `EXPR("  SignedArea")` | `0` | [emulator](../results.tsv) |

## Behaviour

**[AREA](AREA.md) answered −5.33333333333 and this stayed at 0** (emulator),
one call apart in the same batch. [Root](Root-var.md) carries the account for
all five.

**Its name says what the command's does not** (HP help). The command is
`AREA` and this is `SignedArea`, and the sign is the thing a caller most
often gets wrong: the area under a curve below the axis comes back negative
rather than as a magnitude, which [AREA](AREA.md) records with two rows. HP
named the variable more carefully than the command.

**It is the only one of the five that needs no suffix** (HP help). `AREA` and
`SignedArea` are different words, where `Root`, `Slope`, `Extremum` and
`Isect` each collide with their command by case alone and take `-var` in the
file name. [Root](Root-var.md) carries the rule.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AREA](AREA.md) · [Root](Root-var.md) · [Slope](Slope-var.md)
