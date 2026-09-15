# square

The square on a side given by two points.

| | |
|---|---|
| Syntax | `square(Point1, Point2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("square(point(0,0),point(2,0))")` | `polygon(point(0,0),point(2,0),point(2,2),point(0,2),point(0,0))` | [emulator](../results.tsv) |

## Behaviour

**Two points give one side and the other two vertices are computed**
(emulator). The origin and 2,0 produce the square above the x axis, and the
answer closes the ring by repeating the first point, as
[polygon](polygon.md) records for the whole family.

**The answer was known before asking** (emulator), which is what makes this
row evidence that the command computes rather than echoes.

**The square is built on one side of the segment, not the other** (emulator):
the vertices come back above the axis rather than below. Which side is
chosen for a general pair of points is not established by one row
(unverified).

**[rectangle](rectangle.md) with a ratio of 1 answered exactly this same
polygon** (emulator), character for character, so on this evidence a square
is a rectangle whose ratio is one and the two names overlap.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[rectangle](rectangle.md) · [polygon](polygon.md) · [rhombus](rhombus.md)
