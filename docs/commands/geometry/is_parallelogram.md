# is_parallelogram

Answers a code for the kind of quadrilateral, not a yes or no.

| | |
|---|---|
| Syntax | `is_parallelogram(Point1, Point2, Point3, Point4)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("is_parallelogram(point(0,0),point(2,0),point(2,2),point(0,2))")` | `4` | [emulator](../results.tsv) |

## Behaviour

**The four points are a square and the answer is 4, not 1** (emulator), a
plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**A square is a parallelogram, so this is not a refusal** (emulator). The
number is most likely a classification, a square being the most particular
kind a parallelogram can be, and no scale for it is published in the data this
kit holds (HP help).

**[is_isosceles](is_isosceles.md) behaves the same way**, answering 3 for a
triangle that is isosceles (emulator). Two of the nine tests in this family
answer a code where the other seven answer 0 or 1, and nothing in HP's list
marks them apart.

**It works as a test and fails as an equality** (emulator): not zero when the
shape qualifies, but never 1 for the case measured here.

The probe is a plain parallelogram that is not a rectangle (unverified),
which would show whether the answer drops and give the scale its meaning.

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| `IF is_parallelogram(a,b,c,d) == 1 THEN` | Never fires for a square, which answers 4. Testing the answer for truth works; comparing it to 1 does not | [emulator](../results.tsv) |

## Related

[is_isosceles](is_isosceles.md) · [quadrilateral](quadrilateral.md) ·
[is_concyclic](is_concyclic.md)
