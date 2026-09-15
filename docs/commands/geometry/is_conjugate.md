# is_conjugate

Whether points are conjugate with respect to a circle.

| | |
|---|---|
| Syntax | `is_conjugate(Circle, Point1, Point2, [Point3])` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("is_conjugate(circle(point(0,0),point(2,0)),point(1,0),point(3,0))")` | `0` | [emulator](../results.tsv) |

## Behaviour

`is_conjugate` answers 0 for the circle through the origin and 2,0 with the
points 1,0 and 3,0 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer is a no, and this row does not prove the command works**
(emulator). Zero is the family's no, as
[is_equilateral](is_equilateral.md) shows, but a command that never worked
would answer 0 as well and nothing measured here separates those.

**The first point given is the centre of that circle** (emulator), as
[center](center.md) showed, which may be why the answer is no rather than a
refusal. A pair chosen to be conjugate is the probe (unverified).

The fourth argument is optional and was not used (HP help).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[circle](circle.md) · [center](center.md) · [is_concyclic](is_concyclic.md)
