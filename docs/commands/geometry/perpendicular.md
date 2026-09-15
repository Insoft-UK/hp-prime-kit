# perpendicular

The perpendicular through a point, which asked for three points instead.

| | |
|---|---|
| Syntax | `perpendicular(Point, Line)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("perpendicular(point(0,1),line(point(0,0),point(1,0)))")` | `"se esperan 3 puntos Error: valor de argumento incorrecto"` | [emulator](../results.tsv) |

## Behaviour

**The calculator and HP's help disagree, and the calculator is the one that
runs** (emulator). HP publishes `perpendicular(Point, Line)`; given exactly
that, a point and a line, the machine replies that it expects three points.

**The reply is a string, not a refusal** (emulator). It is type 2,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), so a program that tests
for an error finds none and carries the message on as though it were a value.
Seven answers in this batch behaved that way; [inter](inter.md) records the
pattern.

**The text is in the calculator's language** (emulator). It is Spanish
because this machine is, so the wording is not a property of the command and
this entry quotes it only as the evidence that the call was rejected.

Three points would name a vertex and two rays, which is the shape
[bisector](bisector.md) and [altitude](altitude.md) take, and both of those
answered (emulator). That is the form worth trying next, and it is untried
here (unverified).

[perpen_bisector](perpen_bisector.md) is the neighbour that worked: given one
segment it answered `line(x=2)` (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[perpen_bisector](perpen_bisector.md) · [parallel](parallel.md) ·
[altitude](altitude.md) · [inter](inter.md)
