# LineTan

The tangent to a curve, which needs its expression kept back.

| | |
|---|---|
| Syntax | `LineTan(f(x), [Var], Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LineTan(X^2,X,1)")` | `line(y=diff(0,0)*x-diff(0,0))` | [emulator](../results.tsv) |

## Behaviour

**That answer is not a tangent, and the reason is worth more than the row**
(emulator). It is a symbolic object of type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), and it names `diff(0,0)`
where it should name the derivative of x squared.

**The expression was evaluated before the command saw it** (unverified).
`diff(0,0)` is what a differentiation is left with once both its arguments
have already become 0, which is what `X^2` and `X` come to if `X` holds 0.
So the row measures that the call is accepted and does not measure what the
tangent is.

The probe is the same call with the expression kept back (unverified): either
[QUOTE](QUOTE.md) around it, or a variable that holds nothing on a calculator
reset before the run. Both are one batch away.

**This is a trap a program falls into silently** (emulator). The call did not
fail: it answered a line, and a line is what the caller expects, so nothing
signals that the expression arrived already collapsed. The three neighbours
[DrawSlp](DrawSlp.md), [LineHorz](LineHorz.md) and [LineVert](LineVert.md)
take numbers and do not have this problem.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DrawSlp](DrawSlp.md) · [QUOTE](QUOTE.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
