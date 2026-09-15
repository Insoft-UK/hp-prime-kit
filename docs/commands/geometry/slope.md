# slope

The slope of a line, or of the line through two points.

| | |
|---|---|
| Syntax | `slope(Line) or slope(Point1, Point2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("slope(point(0,0),point(2,1))")` | `1/2` | [emulator](../results.tsv) |

## Behaviour

`slope` of the origin and 2,1 answers a half (emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): one up over two along.

**It is exact rather than decimal** (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers). A program
expecting 0.5 and comparing against a decimal will not match what this
answers, even though the two are the same number.

**The two-point form is the one measured** (emulator). HP's syntax also
allows a line, and that form was not run (unverified) -- which matters here
because [line](line.md) itself was refused, so the only lines available come
from [altitude](altitude.md) and its neighbours.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[distance](distance.md) · [angle](angle.md) · [altitude](altitude.md) ·
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers)
