# SetSample

Points a data set at a column, refused on a reset calculator.

| | |
|---|---|
| Syntax | `SetSample(Hn, Dn)` |
| Group | statistics-1var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SetSample(H1,D1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Both arguments name things a reset calculator leaves empty** (emulator):
the app's first data set and its first column. So the refusal most likely
concerns what was passed rather than the command (unverified).

**It refused alongside [SetFreq](SetFreq.md) and
[Do1VStats](Do1VStats.md)** (emulator), the three names in this group that
take a data set, while the three taking a plain number answered.
[Do1VStats](Do1VStats.md) carries the account of that division.

**This is the command that would fix the others** (emulator). If anything can
put data where [Do1VStats](Do1VStats.md) can reach it, this is the name for
it, so it is the first to probe once a way to fill a column is known.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SetFreq](SetFreq.md) · [Do1VStats](Do1VStats.md) · [CHECK](CHECK.md)
