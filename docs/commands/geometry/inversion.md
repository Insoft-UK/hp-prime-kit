# inversion

Inverts a point in a circle.

| | |
|---|---|
| Syntax | `inversion(Point1, Realk, Point2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("inversion(point(0,0),1,point(2,0))")` | `point(1/2,0)` | [emulator](../results.tsv) |

## Behaviour

**The answer was known before asking** (emulator). Inversion in the unit
circle sends a point at distance 2 to one at distance a half along the same
ray, which is `point(1/2,0)`, type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The arguments are centre, power, point** (emulator). The middle number is
the power of the inversion rather than a radius or a scale, and the answer
fixes that: with power 1 the product of the two distances is 1.

**The answer is exact rather than decimal** (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers): a half written as
a fraction, not 0.5.

What it does to the centre itself, where the inverse is undefined, was not run
(unverified). That is the case a program must guard.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[homothety](homothety.md) · [reciprocation](reciprocation.md) ·
[circle](circle.md)
