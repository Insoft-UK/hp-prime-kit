# segment

The segment between two points.

| | |
|---|---|
| Syntax | `segment(Point1, Point2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("segment(point(0,0),point(3,4))")` | `segment(point(0,0),point(3,4))` | [emulator](../results.tsv) |

## Behaviour

`segment` of the origin and 3,4 answers `segment(point(0,0),point(3,4))`
(emulator), a symbolic object of type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): it hands back a written
form of itself, the way [point](point.md) does.

**It answered where [line](line.md) was refused** (emulator), given the same
two points in the same batch. That makes it the working way to join two
points today, and it is why [midpoint](midpoint.md),
[element](element.md) and [perpen_bisector](perpen_bisector.md) were all
probed through a segment rather than a line.

**The object can be passed on** (emulator): [midpoint](midpoint.md) of one
answers a point and [perpen_bisector](perpen_bisector.md) of one answers a
line, so these are values a program can carry, not just text.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[line](line.md) · [half_line](half_line.md) · [midpoint](midpoint.md)
