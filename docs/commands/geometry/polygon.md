# polygon

A closed figure through any number of points.

| | |
|---|---|
| Syntax | `polygon(Point1, Point2, …, Pointn)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("polygon(point(0,0),point(1,0),point(0,1))")` | `polygon(point(0,0),point(1,0),point(0,1),point(0,0))` | [emulator](../results.tsv) |

## Behaviour

**Three points come back as four: the first is repeated at the end**
(emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). The figure is closed
explicitly rather than left for the reader to close.

**Every polygon command in this group answers in this form** (emulator).
[square](square.md), [rectangle](rectangle.md), [rhombus](rhombus.md),
[parallelogram](parallelogram.md), [quadrilateral](quadrilateral.md),
[right_triangle](right_triangle.md) and [isopolygon](isopolygon.md) all
answer `polygon(...)` with the ring closed, whatever they were asked for. So
the name of the constructor is lost in the answer, and a program cannot tell
from the value which command built it.

**A program counting vertices has to allow for the repeat** (emulator). A
triangle answers four points, a square five. Counting them as given
overstates every figure by one.

**It is the way to build a triangle today** (emulator), since
[triangle](triangle.md) is refused: three points here answer the closed
three-sided figure that command would not.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[triangle](triangle.md) · [quadrilateral](quadrilateral.md) ·
[isopolygon](isopolygon.md)
