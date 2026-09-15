# point

Builds a point from two coordinates.

| | |
|---|---|
| Syntax | `point(Real1, Real2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("point(3,4)")` | `point(3,4)` | [emulator](../results.tsv) |

## Behaviour

`point(3,4)` answers `point(3,4)` (emulator), a symbolic object of type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): it hands back a written
form of itself rather than a pair of numbers.

**This is the foundation of the group and the row that proved it reachable**
(emulator). It was the first call of the probe, on a calculator reset before
the run with no Geometry app open, and almost every other name here takes its
answer as an argument.

**Answering itself is not the same as doing nothing** (emulator).
[distance](distance.md) of two of these is 5 for the origin and 3,4, and
[abscissa](abscissa.md) of this one is 3, so the object carries its
coordinates where later calls can reach them.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[abscissa](abscissa.md) · [coordinates](coordinates.md) ·
[distance](distance.md) · [midpoint](midpoint.md)
