# bisector

The line that halves an angle.

| | |
|---|---|
| Syntax | `bisector(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("bisector(point(0,0),point(4,0),point(0,4))")` | `line(y=x)` | [emulator](../results.tsv) |

## Behaviour

`bisector` of the origin, 4,0 and 0,4 answers `line(y=x)` (emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer was known before asking and it fixes the argument order**
(emulator). The angle at the origin between the two axes is a right angle and
its bisector is the diagonal, so the first argument is the vertex and the
other two lie on the arms.

**[perpendicular](perpendicular.md) asked for three points and this is the
shape it meant** (emulator). That name was given a point and a line, as HP's
syntax says, and replied that it expects three points -- the arrangement this
command takes.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[altitude](altitude.md) · [median_line](median_line.md) ·
[perpendicular](perpendicular.md) · [angle](angle.md)
