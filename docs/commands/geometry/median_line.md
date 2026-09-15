# median_line

The line from a vertex to the middle of the opposite side.

| | |
|---|---|
| Syntax | `median_line(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("median_line(point(0,0),point(4,0),point(0,3))")` | `line(y=3/4*x)` | [emulator](../results.tsv) |

## Behaviour

`median_line` of the origin, 4,0 and 0,3 answers `line(y=3/4*x)` (emulator),
type 8, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer was known before asking** (emulator). The middle of the side
joining 4,0 and 0,3 is at 2 and 1.5, and the line from the origin through it
has slope three quarters, which is what came back. So the first argument is
the vertex, as in [altitude](altitude.md) and [bisector](bisector.md).

**The same three points give a different line here and in
[altitude](altitude.md)** (emulator): four thirds there, three quarters here.
The two are easy to confuse in a program and the answers do not resemble each
other, which is the one mercy.

The slope is exact rather than decimal (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[altitude](altitude.md) · [bisector](bisector.md) · [midpoint](midpoint.md)
