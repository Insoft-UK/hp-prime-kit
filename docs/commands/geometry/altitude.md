# altitude

The altitude of a triangle, as a line.

| | |
|---|---|
| Syntax | `altitude(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("altitude(point(0,0),point(4,0),point(0,3))")` | `line(y=4/3*x)` | [emulator](../results.tsv) |

## Behaviour

`altitude` of the origin, 4,0 and 0,3 answers `line(y=4/3*x)` (emulator), a
symbolic object of type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer says which vertex the altitude is dropped from** (emulator). The
line through the origin perpendicular to the side joining 4,0 and 0,3 has
slope four thirds, which is what came back, so the first argument is the
vertex and the other two are the opposite side.

**It answers an equation rather than a pair of points** (emulator), unlike
[segment](segment.md) and [half_line](half_line.md), which name themselves.
Three names in this batch answered in that form:
[bisector](bisector.md), [median_line](median_line.md) and
[perpen_bisector](perpen_bisector.md).

The slope is exact rather than decimal (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[median_line](median_line.md) · [bisector](bisector.md) ·
[perpendicular](perpendicular.md)
