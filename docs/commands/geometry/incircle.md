# incircle

The circle inscribed in a triangle.

| | |
|---|---|
| Syntax | `incircle(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("incircle(point(0,0),point(3,0),point(0,4))")` | `circle(point(1,1),1)` | [emulator](../results.tsv) |

## Behaviour

**The answer is right, and it was known before asking** (emulator). For a
3-4-5 right triangle the inscribed circle has radius 1, and with the right
angle at the origin its centre sits one unit along each leg. That is
`circle(point(1,1),1)`, type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It answers in the centre-and-radius form the whole family uses**
(emulator), the same as [circle](circle.md) and
[circumcircle](circumcircle.md).

**The three circle commands taking the same triangle answer three different
circles** (emulator): this one has radius 1, [circumcircle](circumcircle.md)
has 5/2 and [excircle](excircle.md) has 6. Together they are a useful check
that a program is calling the one it means.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[circumcircle](circumcircle.md) · [excircle](excircle.md) ·
[circle](circle.md)
