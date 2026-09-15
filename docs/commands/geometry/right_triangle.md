# right_triangle

A right triangle on a leg, with the other leg given as a ratio.

| | |
|---|---|
| Syntax | `right_triangle(Point1, Point2, Realk)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("right_triangle(point(0,0),point(3,0),1)")` | `polygon(point(0,0),point(3,0),point(0,3),point(0,0))` | [emulator](../results.tsv) |

## Behaviour

**The two points give one leg and the third argument scales the other**
(emulator). A leg of 3 with a ratio of 1 gives a second leg of 3, so the
answer is the isosceles right triangle with vertices at the origin, 3,0 and
0,3.

**The right angle sits at the first point** (emulator), which the answer
shows: the two legs run from the origin along each axis.

**The third argument is a ratio, as in [rectangle](rectangle.md), and not an
angle as in [rhombus](rhombus.md)** (emulator). Three commands in this family
take a third number and it means something different in each, with nothing in
the answer's shape to warn a reader.

**It is one of the two ways to build a triangle today** (emulator), since
[triangle](triangle.md) is refused; the other is
[polygon](polygon.md) with three points.

It answers in the closed `polygon(...)` form the family shares (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[triangle](triangle.md) · [polygon](polygon.md) · [rectangle](rectangle.md)
