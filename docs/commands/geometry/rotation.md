# rotation

Turns an object about a centre, answering a complex exponential.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("rotation(point(0,0),1,point(1,0))")` | `point(e^())` | [emulator](../results.tsv) |

## Behaviour

**The answer is e to the imaginary unit, not a pair of coordinates**
(emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). Turning `point(1,0)`
about the origin by 1 gives the point at angle 1 on the unit circle, and the
calculator writes that as an exponential rather than evaluating it.

**So the angle is in radians** (emulator). The exponential form says it
plainly: e to the i times one radian. Every angle this documentation has
measured is in radians, and [angle](angle.md) recorded the mode directly.

**The Result cell carries U+E003, the imaginary unit** (emulator), a
character nobody can type, so it was built from the stored row,
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit).

**A program comparing coordinates has to evaluate it first** (emulator), the
same difficulty [rhombus](rhombus.md) presents with its `COS` and `SIN`.

HP's list gives this name no syntax string (HP help); the argument order above
is what the answer supports, centre then angle then object.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[similarity](similarity.md) · [angle](angle.md) · [rhombus](rhombus.md) ·
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit)
