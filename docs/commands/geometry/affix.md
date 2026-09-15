# affix

A point as a complex number.

| | |
|---|---|
| Syntax | `affix(Point) or affix(Vector)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("affix(point(3,4))")` | `3+4*` | [emulator](../results.tsv) |

## Behaviour

`affix(point(3,4))` answers three plus four times the imaginary unit
(emulator), and the type is 3, a complex number,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The Result cell above ends in a character nobody can type** (emulator):
U+E003, the imaginary unit, which the calculator writes and no keyboard
produces. The cell was built from the stored row rather than typed,
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit).

**It is the third way this group hands back a point's coordinates**
(emulator), after [coordinates](coordinates.md) as a vector and
[abscissa](abscissa.md) with [ordinate](ordinate.md) as two reals. This one
gives a single number a program can do arithmetic with.

The same character appeared in `plotfunc`'s answer in the probe (emulator),
which rewrote a function as a parametric one using it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[coordinates](coordinates.md) · [point](point.md) ·
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit)
