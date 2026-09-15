# similarity

Scales and turns an object about a centre.

| | |
|---|---|
| Syntax | `similarity(Point, Realk, Angle, Object)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("similarity(point(0,0),2,0,point(1,1))")` | `point(2,2)` | [emulator](../results.tsv) |

## Behaviour

**With an angle of zero it is exactly [homothety](homothety.md)** (emulator):
both answered `point(2,2)` for doubling `point(1,1)` about the origin, type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**So this row measures the scaling and says nothing about the turn**
(emulator). The angle was zero precisely so the two commands could be
compared, and the probe that would measure the rest is the same call with a
quarter turn, where the answer should move to `point(-2,2)`.

The angle is in radians (unverified here, emulator elsewhere): every angle
this documentation has measured is, including
[rotation](rotation.md) in this same batch and [angle](angle.md) in the one
before.

The arguments go centre, factor, angle, object (HP help), which the row is
consistent with.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[homothety](homothety.md) · [rotation](rotation.md) ·
[reflection](reflection.md)
