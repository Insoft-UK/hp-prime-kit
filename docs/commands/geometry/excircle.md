# excircle

A circle touching one side of a triangle and the other two extended.

| | |
|---|---|
| Syntax | `excircle(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("excircle(point(0,0),point(3,0),point(0,4))")` | `circle(point(6,6),6)` | [emulator](../results.tsv) |

## Behaviour

`excircle` of the 3-4-5 right triangle answers `circle(point(6,6),6)`
(emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): centre outside the
triangle, radius 6.

**A triangle has three excircles and this answers one of them** (HP help).
Which one is decided by the order of the points, and nothing measured here
says which order gives which; one row cannot show it.

**The centre lies outside the triangle, which is what distinguishes it from
[incircle](incircle.md)** (emulator): that one answered `point(1,1)` with
radius 1 for the same three points, well inside.

The probe is the same three points in a different order (unverified), which
would show whether the answer moves to another of the three.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[incircle](incircle.md) · [circumcircle](circumcircle.md) ·
[circle](circle.md)
