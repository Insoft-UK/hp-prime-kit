# coordinates

Both coordinates of a point, as a vector.

| | |
|---|---|
| Syntax | `coordinates(Point) or coordinates(Vector)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("coordinates(point(3,4))")` | `[3,4]` | [emulator](../results.tsv) |

## Behaviour

`coordinates(point(3,4))` answers `[3,4]` (emulator), and the type is 4, a
matrix, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**Type 4 is the finding, not the pair of numbers** (emulator). Square
brackets on this calculator are a matrix or a vector, and a list would have
been type 6 written with braces. A program indexing the answer as a list is
indexing the wrong kind of object.

**It does in one call what [abscissa](abscissa.md) and
[ordinate](ordinate.md) do in two** (emulator), and both of those answer
plain reals of type 0, so the three names differ in what a caller gets back
as much as in how much.

[polar_coordinates](polar_coordinates.md) answers the same type for the same
point, in the other system (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[abscissa](abscissa.md) · [ordinate](ordinate.md) ·
[polar_coordinates](polar_coordinates.md)
