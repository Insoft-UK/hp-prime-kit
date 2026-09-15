# is_concyclic

Whether four points lie on one circle.

| | |
|---|---|
| Syntax | `is_concyclic(Point1, Point2, Point3, Point4)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("is_concyclic(point(1,0),point(0,1),point(-1,0),point(0,-1))")` | `1` | [emulator](../results.tsv) |

## Behaviour

`is_concyclic` of the four points where the unit circle meets the axes
answers 1 (emulator), type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). All four are one unit
from the origin, so the answer was known before asking.

**Four is the smallest number for which the question is not trivial**
(HP help): any three points that are not collinear lie on some circle, so a
test of three would always say yes.

**It answers 1 rather than a code** (emulator), unlike
[is_isosceles](is_isosceles.md) and
[is_parallelogram](is_parallelogram.md).

What it answers for four points that are not concyclic was not run
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[is_collinear](is_collinear.md) · [circumcircle](circumcircle.md) ·
[circle](circle.md)
