# AREA

The signed area under a function between two values.

| | |
|---|---|
| Syntax | `AREA(Fn, [Fm], Lower, Upper)` |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AREA(F1,0,2)")` | `−5.33333333333` | [emulator](../results.tsv) |
| `EXPR(" AREA(F1,0,2)")` | `−5.33333333333` | [emulator](../results.tsv) |
| `EXPR("AREA(F1,0,1)")` | `−4` | [emulator](../results.tsv) |

## Behaviour

**The first and last rows are right, and they come from different setups**
(emulator). In the first, `F1` held `X^2-4` with the Function app active, and the integral
from 0 to 2 is eight thirds less eight, which is minus sixteen thirds:
−5.33333333333. In the last, `F1` held the constant −4 -- see
[ROOT](ROOT.md) for why -- and the area under it over one unit is −4.
Both are plain reals of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The area is signed** (emulator). A function below the axis gives a negative
answer rather than a magnitude, which every row shows, and a program adding
areas across a crossing has to expect cancellation rather than a sum of
magnitudes.

**The last row is what first showed this group computes** (emulator). Its
answer depends on the function and on both bounds, so a command ignoring its
arguments could not have produced it. Together with [SLOPE](SLOPE.md) it
corrected an earlier batch that had recorded the whole group as refused.

**The first row is the one taken under both conditions** (emulator): a real
function in `F1` and the Function app active,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).
It is the row that shows the command integrating something other than a
constant. It was first taken with `F1` filled by hand in the app's editor,
and a later batch reproduced the same answer with `F1:='X^2-4'` written by
the program itself -- see [ROOT](ROOT.md) for the quoting rule.

**The optional second function was never supplied** (HP help), so the area
*between* two curves -- the likeliest meaning -- is untested (unverified).
`F2` now holds a function, so that is one row away.

The minus signs are the calculator's own, U+2212 (emulator),
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign): both Result cells were
built from the stored rows rather than typed.

**One row was taken by a batch that set up its own `F1`** (emulator), the one
whose call carries a leading space. It reproduces the answer that had needed
a person at the keyboard, because `F1:='X^2-4'` stores the expression where
`F1:=X^2-4` stored a number. [ROOT](ROOT.md) carries the quoting rule. The
space is incidental: it exists only so the two runs keep separate rows.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SLOPE](SLOPE.md) · [ROOT](ROOT.md) · [ISECT](ISECT.md) ·
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign)
