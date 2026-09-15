# plotimplicit

Answered an empty list.

| | |
|---|---|
| Syntax | `plotimplicit(Expr, [XIntrvl, YIntrvl])` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("plotimplicit(X^2+Y^2-1)")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**The answer is an empty list** (emulator), type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): not an error, not a
curve, nothing at all. The expression given is the unit circle, so there was
something to plot.

**It is the third command in this group to answer that way**, after
[tangent](tangent.md) and [conic](conic.md) (emulator). All three take
something other than plain points -- a curve and a point, an expression, an
expression -- and all three answer nothing while raising nothing.

**An expression reaching a command unevaluated has gone wrong twice already
in this phase** (emulator): [arcLen](arcLen.md) answered a number a third
short, and [LineTan](../catalog/LineTan.md) collapsed its argument before
use. Whether `X` and `Y` arrived here as symbols is not measured
(unverified).

**A program looping over the answer does nothing, silently** (emulator),
which is the practical cost of an empty list where a refusal would have been
clearer.

The two optional intervals were not supplied (HP help), and whether they
change the answer was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[conic](conic.md) · [tangent](tangent.md) · [plotfunc](plotfunc.md)
