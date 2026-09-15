# ordinate

The y coordinate of a point.

| | |
|---|---|
| Syntax | `ordinate(Point)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ordinate(point(3,4))")` | `4` | [emulator](../results.tsv) |

## Behaviour

`ordinate(point(3,4))` answers 4 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It is the pair of [abscissa](abscissa.md)** (emulator), which answered 3
for the same point in the same batch. Together they take a point apart, and
[coordinates](coordinates.md) does both at once.

**The answer was known before asking** (emulator).

HP's syntax names only a point for this one, where
[abscissa](abscissa.md) also allows a vector (HP help). Whether that
difference is real was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[abscissa](abscissa.md) · [coordinates](coordinates.md) · [point](point.md)
