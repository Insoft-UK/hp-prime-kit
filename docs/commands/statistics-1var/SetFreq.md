# SetFreq

Points a data set's frequencies at a column, refused on a reset calculator.

| | |
|---|---|
| Syntax | `SetFreq(Hn, Dn)` |
| Group | statistics-1var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SetFreq(H1,D1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It takes the same two kinds of argument as [SetSample](SetSample.md)** and
refused identically (emulator), so nothing measured here separates the two
commands.

**Both name things a reset calculator leaves empty** (emulator), which is the
likeliest reason and not established (unverified).
[Do1VStats](Do1VStats.md) carries the account of the three-and-three division
in this group.

**What it sets is the count for each value** (HP help), where
[SetSample](SetSample.md) sets the values themselves. A data set needs both
before statistics mean anything, which is why the two go together.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SetSample](SetSample.md) · [Do1VStats](Do1VStats.md)
