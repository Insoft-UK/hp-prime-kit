# is_equilateral

Whether a triangle has three equal sides.

| | |
|---|---|
| Syntax | `is_equilateral(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("is_equilateral(point(0,0),point(3,0),point(0,4))")` | `0` | [emulator](../results.tsv) |

## Behaviour

`is_equilateral` of the 3-4-5 triangle answers 0 (emulator), a plain real of
type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes). Its sides are
3, 4 and 5, so it is not equilateral and the answer was known before asking.

**This is the row that fixes the scale for the family** (emulator). A false
answer here is 0, so the codes
[is_isosceles](is_isosceles.md) and [is_parallelogram](is_parallelogram.md)
return, 3 and 4, sit on a scale where 0 still means no rather than being
arbitrary numbers.

What it answers for a triangle that is equilateral was not run (unverified),
and that is the row that would say whether the true answer is 1 or another
code.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[is_isosceles](is_isosceles.md) · [triangle](triangle.md)
