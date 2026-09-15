# ISECT

Where two functions cross.

| | |
|---|---|
| Syntax | `ISECT(Fn, Fm, [Guess])` |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ISECT(F1,F2,2)")` | `2.56155281281` | [emulator](../results.tsv) |
| `EXPR(" ISECT(F1,F2,2)")` | `2.56155281281` | [emulator](../results.tsv) |
| `EXPR("ISECT(F1,F1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The answer is right, and it is not the obvious number** (emulator). With
`F1` holding `X^2-4` and `F2` holding `X`, the curves meet where x squared
less four equals x, which is one plus the square root of seventeen, over two:
2.56155281281 to every figure returned. A plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**This documentation predicted 2 before the row arrived, and was wrong**
(emulator). Two is where `F1` crosses the axis, not where it crosses `F2`;
at x equal to 2 the two functions are worth 0 and 2. The calculator was
right. That is recorded because a prediction is only worth making if a miss
is admitted.

**It answers one crossing and there are two** (emulator). The other is at one
less the square root of seventeen, over two, about −1.56. The guess of 2
chose this one, the same way the guess works in [ROOT](ROOT.md).

**The last row asked where a function crosses itself** (emulator), which
has no answer, and was taken before either condition of this group held.
[ROOT](ROOT.md) carries that account.

**One row was taken by a batch that set up its own `F1`** (emulator), the one
whose call carries a leading space. It reproduces the answer that had needed
a person at the keyboard, because `F1:='X^2-4'` stores the expression where
`F1:=X^2-4` stored a number. [ROOT](ROOT.md) carries the quoting rule. The
space is incidental: it exists only so the two runs keep separate rows.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ROOT](ROOT.md) · [EXTREMUM](EXTREMUM.md) · [AREA](AREA.md)
