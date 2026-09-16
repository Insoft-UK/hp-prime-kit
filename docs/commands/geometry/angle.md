# angle

The angle at a vertex, in radians.

| | |
|---|---|
| Syntax | `angle(Vertex, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("angle(point(0,0),point(1,0),point(0,1))")` | `1/2*π` | [emulator](../results.tsv) |

## Behaviour

`angle` at the origin between 1,0 and 0,1 answers half of pi (emulator), a
symbolic object of type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**That is a right angle in radians, and it was known before asking**
(emulator). The two arms lie along the axes, so the angle is a quarter turn;
in degrees it would have been 90. The answer agrees with the mode recorded in
[ACOT](../trigonometry/ACOT.md), where `HAngle` answered 0 beside three inverse trigonometric
answers in radians.

**It is exact rather than decimal** (emulator): half of pi written as such
and not as 1.5707963268,
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers). The Result cell
above was built from the stored row rather than typed, because that pi is
U+03C0, a character the calculator writes and nobody can type.

**The first argument is the vertex** (emulator), the same arrangement
[bisector](bisector.md) and [altitude](altitude.md) take.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[bisector](bisector.md) · [slope](slope.md) ·
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers)
