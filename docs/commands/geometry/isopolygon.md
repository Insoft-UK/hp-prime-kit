# isopolygon

A regular polygon, whose answer is long enough to be cut.

| | |
|---|---|
| Syntax | `isopolygon(Point1, Point2, Realn)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("isopolygon(point(0,0),point(1,0),5)")` | `polygon(point(0,0),point(1/2+/(2*√(5-2*√5))+(-(1/2)-/(2*√(5-2*√5)))*(√5-1)/4+*(-(1/2)-/(2*√(5-2*√5)))*√(2*√5+10)/4),point(1/2+/(2*√(5-2*√5))-(-(1/2)-/(2*√ (cut at 160 characters)` | [emulator](../results.tsv) |

## Behaviour

**The answer was cut at 160 characters, and the row says so** (emulator). It
is long enough to reach the harness's width, and
the marker in the stored row is the harness's own, not the calculator's. Only
the first two vertices and part of the third survive.

**The two points give one side and the third argument the number of sides**
(emulator): five here, so a regular pentagon built on the segment from the
origin to 1,0.

**The coordinates arrive unevaluated and exact** (emulator), written with
radicals rather than decimals -- the vertices of a pentagon involve the
square root of five, and it is there in the answer twice over. That is why
this answer is long where [square](square.md)'s is short.

**The Result cell carries the radical U+221A and the imaginary unit U+E003**
(emulator), characters nobody can type, so it was built from the stored row
rather than typed.

**A shorter call would fit** (unverified). Three or four sides give
coordinates without radicals, so the probe that would record this command
whole is `isopolygon` with 4 rather than 5.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[polygon](polygon.md) · [square](square.md) · [circumcircle](circumcircle.md)
