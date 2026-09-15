# half_line

The ray from one point through another.

| | |
|---|---|
| Syntax | `half_line(Point1, Point2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("half_line(point(0,0),point(3,4))")` | `half_line(point(0,0),point(3,4))` | [emulator](../results.tsv) |

## Behaviour

`half_line` of the origin and 3,4 answers `half_line(point(0,0),point(3,4))`
(emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), handing back a written
form of itself.

**The first point is the end it starts from** (HP help), which is what makes
it different from [segment](segment.md) given the same two points; nothing
measured here shows that difference, since both answered by naming
themselves.

**It answered where [line](line.md) was refused** (emulator), from the same
two points in the same batch. Two of the three ways to join two points work
and the plainest one does not.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[segment](segment.md) · [line](line.md) · [point](point.md)
