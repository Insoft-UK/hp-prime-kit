# radius

The radius of a circle.

| | |
|---|---|
| Syntax | `radius(Circle)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("radius(circle(point(0,0),point(1,0)))")` | `1/2` | [emulator](../results.tsv) |

## Behaviour

`radius` of the circle through the origin and 1,0 answers a half (emulator),
type 8, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It settles how `circle` reads its two points** (emulator). A half is the
radius only if those points are the ends of a diameter; if the first were the
centre and the second a point on the rim, the radius would have been 1.
[center](center.md) says the same from the other side and
[area](area.md) agrees, answering a quarter of pi for the same circle.

**The answer is exact rather than decimal** (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers): `1/2` and not
0.5.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[center](center.md) · [area](area.md) · [distance](distance.md)
