# arcLen

The length of an arc, answered wrongly for the curve tried here.

| | |
|---|---|
| Syntax | `arcLen(Expr, Real1, Real2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("arcLen(X^2,0,1)")` | `1` | [emulator](../results.tsv) |

## Behaviour

**`arcLen(X^2,0,1)` answers 1, and the arc is about 1.4789** (emulator). The
length of the parabola from the origin to 1,1 is the integral of the square
root of one plus four x squared, which is 1.4789428575. The answer is a third
short.

**The call succeeded, which is what makes it dangerous** (emulator). It is a
plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), and 1 is a perfectly
plausible length for a curve between two points one apart. Nothing in the
answer says it is wrong, so a program carries the error without a sign.

**The likeliest reading is that the expression never reached it as an
expression** (unverified). One is the distance along the x axis from 0 to 1,
which is what the integral degenerates to when the curve is flattened, and
that matches what [LineTan](../catalog/LineTan.md) does in another group:
there the argument arrived already evaluated, and `QUOTE` did not stop it.

The probe is an arc whose length is a whole number by construction
(unverified), so that a right answer and a degenerate one cannot be confused.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| `arcLen(f(x), a, b)` expecting the arc length | Answers a number that is not the arc length and raises nothing. For the parabola from 0 to 1 it answers 1 where the arc is 1.4789 | [emulator](../results.tsv) |

## Related

[LineTan](../catalog/LineTan.md) · [perimeter](perimeter.md) ·
[distance](distance.md)
