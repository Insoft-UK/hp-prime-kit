# circumcircle

The circle through three points.

| | |
|---|---|
| Syntax | `circumcircle(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("circumcircle(point(0,0),point(3,0),point(0,4))")` | `circle(point(3/2,2),5/2)` | [emulator](../results.tsv) |

## Behaviour

**The answer is right, and it was known before asking** (emulator). The three
points form a 3-4-5 right triangle, whose circumcircle has the hypotenuse as
its diameter: centre at 1.5 and 2, radius 2.5. That is what came back, type
8, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The numbers are exact rather than decimal** (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers): three halves and
five halves, not 1.5 and 2.5.

**It answers in the same centre-and-radius form as
[circle](circle.md)** (emulator), so a program can pass the result to
[center](center.md) or [radius](radius.md) without knowing which command
built it.

[incircle](incircle.md) and [excircle](excircle.md) take the same three
points and answer different circles (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[incircle](incircle.md) · [excircle](excircle.md) · [circle](circle.md) ·
[is_concyclic](is_concyclic.md)
