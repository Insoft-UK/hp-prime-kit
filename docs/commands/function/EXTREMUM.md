# EXTREMUM

Where a function turns, given a guess.

| | |
|---|---|
| Syntax | `EXTREMUM(Fn, [Guess])` |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("EXTREMUM(F1,0)")` | `0` | [emulator](../results.tsv) |
| `EXPR(" EXTREMUM(F1,0)")` | `0` | [emulator](../results.tsv) |
| `EXPR("EXTREMUM(F1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It answers 0, which is right** (emulator). With `F1` holding `X^2-4`, the
parabola turns at x equal to 0, and the answer is a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It answers where the turn is, not what the function is worth there**
(emulator). The minimum value is −4; the answer is 0, the place. A program
wanting the value has to evaluate the function at the answer.

**The last row is the same command before either condition held**
(emulator): the app was not active and `F1` held a constant rather than a
function. [ROOT](ROOT.md) carries the account of both.

**The guess was supplied this time and omitted before** (emulator), so this
pair does not show whether the guess is required. HP marks it optional
(HP help) and the working row gave one, so that is untested (unverified).

**One row was taken by a batch that set up its own `F1`** (emulator), the one
whose call carries a leading space. It reproduces the answer that had needed
a person at the keyboard, because `F1:='X^2-4'` stores the expression where
`F1:=X^2-4` stored a number. [ROOT](ROOT.md) carries the quoting rule. The
space is incidental: it exists only so the two runs keep separate rows.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ROOT](ROOT.md) · [SLOPE](SLOPE.md) · [ISECT](ISECT.md)
