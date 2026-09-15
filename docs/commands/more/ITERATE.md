# ITERATE

Applies an expression to itself a number of times.

| | |
|---|---|
| Syntax | `ITERATE(expression, variable, start, times)` → the value |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ITERATE(X*2,X,1,3)` | `8` | [emulator](../results.tsv) |

## Behaviour

Doubling from 1, three times, is 8 (emulator): 1 → 2 → 4 → 8. So the count is
how many times the expression is applied, not how many values you get, and
the starting value is not one of them.

The variable named in the second argument is the one the expression uses; the
measured call uses `X`, which is also one of the calculator's own variables
(G2), [ppl.global-namespace](../../topics/ppl.md#ppl.global-namespace).
Whether the call leaves that variable changed afterwards has not been
measured (unverified), and it matters, because `X` belongs to the Function
app as well.

A count of zero, and an expression that raises, have not been measured
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EVAL](EVAL.md) · [TEVAL](TEVAL.md)
