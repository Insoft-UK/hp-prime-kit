# center

The centre of a circle.

| | |
|---|---|
| Syntax | `center(Circle)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("center(circle(point(0,0),point(2,0)))")` | `point(1,0)` | [emulator](../results.tsv) |

## Behaviour

`center` of the circle through the origin and 2,0 answers `point(1,0)`
(emulator), a symbolic object of type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer was known before the calculator was asked, and it confirms how
`circle` reads its arguments** (emulator). Halfway between the two points is
1,0, which is the centre only if those two points are the ends of a diameter.
[radius](radius.md) says the same from the other side, answering a half for a
circle through the origin and 1,0.

**It answers a point rather than two numbers** (emulator), so a program
wanting the coordinates passes the answer to [abscissa](abscissa.md) or
[coordinates](coordinates.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[radius](radius.md) · [point](point.md) · [coordinates](coordinates.md)
