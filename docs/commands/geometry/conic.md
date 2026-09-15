# conic

The conic of an equation, which answered an empty list.

| | |
|---|---|
| Syntax | `conic(Expr)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("conic(X^2+Y^2-1)")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**The answer is an empty list** (emulator), type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): not an error, not a
curve, nothing at all. The expression given is the unit circle, so there was
a conic to find.

**[tangent](tangent.md) answered the same way in the first geometry batch**
(emulator). Two commands, two empty lists, and in both cases a program
looping over the answer does nothing and reports nothing.

**It is the only name in this family that takes an expression rather than
points** (HP help), and expressions have gone wrong twice in this phase
already: [arcLen](arcLen.md) answered a number a third short and
[LineTan](../catalog/LineTan.md) collapsed its argument before use. Whether
`X` and `Y` reached this command as symbols or as values is not measured here
(unverified).

The probe is the same call with the expression held back by
[QUOTE](../catalog/QUOTE.md) (unverified), which did not help `LineTan` but
has not been tried here.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[tangent](tangent.md) · [arcLen](arcLen.md) · [ellipse](ellipse.md)
