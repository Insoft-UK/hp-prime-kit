# SLOPE

The slope of a function at a value.

| | |
|---|---|
| Syntax | `SLOPE(Fn,Value)` |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SLOPE(F1,2)")` | `4` | [emulator](../results.tsv) |
| `EXPR(" SLOPE(F1,2)")` | `4` | [emulator](../results.tsv) |
| `EXPR("SLOPE(F1,1)")` | `0` | [emulator](../results.tsv) |

## Behaviour

**The first and last rows are right, and were measured under different conditions**
(emulator). In the first, `F1` held `X^2-4` with the Function app active, and
the slope at 2 is 4, which is twice x. In the last, `F1` held the constant
−4 and the slope of a constant is 0 everywhere.

**The last row is the more interesting of those two** (emulator). It was
taken when this documentation believed the whole group was unreachable, and
it is what showed otherwise: a command that computes 0 for a constant is
computing, not refusing. Together with [AREA](AREA.md) it corrected that
reading before the app rule was known.

**So this entry has a right answer from a wrong setup and a right answer from
a right one** (emulator), which is why both are kept: the pair shows the
command was never the problem.

The second argument is where the slope is taken (HP help), and the first row
confirms it: at a different value the answer changes with x.

**One row was taken by a batch that set up its own `F1`** (emulator), the one
whose call carries a leading space. It reproduces the answer that had needed
a person at the keyboard, because `F1:='X^2-4'` stores the expression where
`F1:=X^2-4` stored a number. [ROOT](ROOT.md) carries the quoting rule. The
space is incidental: it exists only so the two runs keep separate rows.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AREA](AREA.md) · [ROOT](ROOT.md) · [EXTREMUM](EXTREMUM.md)
