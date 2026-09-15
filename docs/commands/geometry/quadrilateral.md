# quadrilateral

A four-sided figure through four points.

| | |
|---|---|
| Syntax | `quadrilateral(Point1, Point2, Point3, Point4)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("quadrilateral(point(0,0),point(2,0),point(2,2),point(0,2))")` | `polygon(point(0,0),point(2,0),point(2,2),point(0,2),point(0,0))` | [emulator](../results.tsv) |

## Behaviour

**It computes nothing: the four points come back as given, with the ring
closed** (emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). That makes it the
four-point case of [polygon](polygon.md) rather than a constructor with a
rule of its own.

**The answer is identical to what [square](square.md) gave for the same
shape** (emulator), because both normalise to `polygon(...)`. A program
receiving the value cannot tell which of the two built it.

**It does not check that the figure is a quadrilateral in any particular
sense** (unverified). Four points in an order that crosses itself were not
tried, and that is the row that would say whether it validates or simply
records.

[is_parallelogram](is_parallelogram.md) answered 4 for exactly these four
points (emulator), so this square is recognised as the most particular kind
of parallelogram by that test.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[polygon](polygon.md) · [parallelogram](parallelogram.md) ·
[is_parallelogram](is_parallelogram.md)
