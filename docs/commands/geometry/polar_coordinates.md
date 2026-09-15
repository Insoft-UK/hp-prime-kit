# polar_coordinates

A point's radius and angle, as a vector.

| | |
|---|---|
| Syntax | `polar_coordinates(Point)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("polar_coordinates(point(3,4))")` | `[5,0.927295218002]` | [emulator](../results.tsv) |

## Behaviour

`polar_coordinates(point(3,4))` answers `[5,0.927295218002]` (emulator), type
4, a matrix, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**Both numbers were known before asking** (emulator). The radius is the
distance from the origin, 5, which [distance](distance.md) answers for the
same point; the angle is the arc tangent of four thirds, 0.9272952180, which
is what came back to twelve figures.

**The angle is in radians** (emulator), agreeing with
[angle](angle.md), which answered half of pi for a right angle, and with the
mode Phase 6 measured.

**The radius is exact and the angle is not** (emulator). Five arrives whole
while the angle is a decimal, because one is a whole number and the other is
not; this is the same exactness [radius](radius.md) and
[slope](slope.md) show, [ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[coordinates](coordinates.md) · [distance](distance.md) · [angle](angle.md)
