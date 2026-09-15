# parallelogram

A parallelogram from three of its vertices.

| | |
|---|---|
| Syntax | `parallelogram(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("parallelogram(point(0,0),point(2,0),point(3,1))")` | `polygon(point(0,0),point(2,0),point(3,1),point(1,1),point(0,0))` | [emulator](../results.tsv) |

## Behaviour

**Three points are given and the fourth is computed** (emulator). The origin,
2,0 and 3,1 come back with `point(1,1)` added before the ring closes, which
is the vertex that makes the figure a parallelogram: the same step from 2,0
to 3,1 applied from the origin.

**The answer was known before asking** (emulator), so this row shows the
command computing the missing vertex rather than echoing what it was handed.

**The fourth vertex is placed to close the figure in the order given**
(emulator). Three points admit three different parallelograms depending on
which pair is taken as a side, and the one chosen here follows the order of
the arguments.

It answers in the closed `polygon(...)` form the family shares (emulator),
[polygon](polygon.md), so the name is lost in the value.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[quadrilateral](quadrilateral.md) · [is_parallelogram](is_parallelogram.md) ·
[polygon](polygon.md)
