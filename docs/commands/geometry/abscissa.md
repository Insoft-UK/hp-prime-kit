# abscissa

The x coordinate of a point.

| | |
|---|---|
| Syntax | `abscissa(Point) or abscissa(Vector)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("abscissa(point(3,4))")` | `3` | [emulator](../results.tsv) |

## Behaviour

`abscissa(point(3,4))` answers 3 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**This is how a program gets a number out of a point** (emulator). The
objects this group builds answer as themselves, so a caller needing
coordinates reaches for this, [ordinate](ordinate.md), or
[coordinates](coordinates.md) for both at once.

**The answer was known before asking** (emulator), which is what says it
reads the point rather than echoing it.

HP's syntax also allows a vector (HP help), and that form was not run
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ordinate](ordinate.md) · [coordinates](coordinates.md) · [point](point.md)
