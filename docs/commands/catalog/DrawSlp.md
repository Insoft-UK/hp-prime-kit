# DrawSlp

Answers the line through a point with a given slope.

| | |
|---|---|
| Syntax | `DrawSlp(a, b, m)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("DrawSlp(1,2,3)")` | `line(y=3*x-1)` | [emulator](../results.tsv) |

## Behaviour

`DrawSlp(1,2,3)` answers `line(y=3*x-1)` (emulator), a symbolic object of
type 8, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer says what the three arguments mean** (emulator). A slope of 3
through the point 1 and 2 gives `y = 3x - 1`, and putting x as 1 into that
gives 2, so the first two arguments are the point and the third is the slope,
in that order.

**It answers a line rather than drawing one** (emulator), the same as
[LineHorz](LineHorz.md) and [LineVert](LineVert.md). The name promises a
drawing and the value is an equation.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LineHorz](LineHorz.md) · [LineVert](LineVert.md) · [LineTan](LineTan.md)
