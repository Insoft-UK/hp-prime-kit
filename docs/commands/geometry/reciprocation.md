# reciprocation

The polar line of a point with respect to a circle.

| | |
|---|---|
| Syntax | `reciprocation(Circle, [Obj1, Obj2,...Objn])` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("reciprocation(circle(point(0,0),point(2,0)),point(3,0))")` | `line(x=3/2)` | [emulator](../results.tsv) |

## Behaviour

`reciprocation` of the circle through the origin and 2,0 with the point 3,0
answers `line(x=3/2)` (emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It turns a point into a line** (emulator), which is what distinguishes it
from the other transforms here: [homothety](homothety.md),
[inversion](inversion.md) and [projection](projection.md) all answer points.

**The circle is the one [circle](circle.md) built from a diameter**
(emulator), so its centre is at 1,0 and its radius 1, and the answer is
vertical at three halves. Whether that is the classical polar of the point is
consistent with those numbers but not verified here (unverified).

**The answer is exact** (emulator), three halves rather than 1.5,
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers).

HP's syntax allows several objects after the circle (HP help); only one was
run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[inversion](inversion.md) · [circle](circle.md) · [is_conjugate](is_conjugate.md)
