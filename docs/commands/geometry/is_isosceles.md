# is_isosceles

Answers which pair of sides is equal, not whether any is.

| | |
|---|---|
| Syntax | `is_isosceles(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("is_isosceles(point(0,0),point(2,0),point(1,2))")` | `3` | [emulator](../results.tsv) |

## Behaviour

**The triangle is isosceles and the answer is 3, not 1** (emulator). Two of
its sides are equal, the two running from the base to the apex, and what came
back is a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), carrying a 3.

**So the answer names something rather than asserting something** (emulator).
Three is most likely the vertex or the side the equality concerns, the apex
being the third point given. One row cannot choose between those readings and
this entry does not.

**It is still usable as a test** (emulator), because 3 is not zero and
[is_equilateral](is_equilateral.md) answered 0 for a triangle that is not
equilateral. A condition asking whether the answer holds behaves correctly; a
comparison against 1 does not.

The probe is a triangle that is not isosceles at all (unverified), which
would show whether the false answer is 0 and fix the shape of the scale.

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| `IF is_isosceles(a,b,c) == 1 THEN` | Never fires. The command answers 3 for an isosceles triangle, so the comparison is false exactly when the triangle qualifies | [emulator](../results.tsv) |

## Related

[is_equilateral](is_equilateral.md) · [is_parallelogram](is_parallelogram.md)
