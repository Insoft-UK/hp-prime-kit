# CROSS

The cross product of two vectors.

| | |
|---|---|
| Syntax | `CROSS(Vector1, Vector2)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CROSS([1,2,3],[4,5,6])` | `[-3,6,-3]` | [emulator](../results.tsv) |

## Behaviour

`CROSS([1,2,3],[4,5,6])` answers `[-3,6,-3]` (emulator): a vector
perpendicular to both, where [DOT](DOT.md) answers the single number 32 for
the same pair.

The answer is `TYPE` 4, a matrix, written with single brackets (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes) -- the same shape the
arguments have.

The negatives come back with the calculator's own minus sign (emulator),
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign), which is why the stored
row and the cell above are not the same characters even though they are the
same number.

**The order matters**: swapping the arguments negates the answer, which is
what a cross product does and what was not run here (unverified). The probe
is `CROSS([4,5,6],[1,2,3])`, and it should answer `[3,-6,3]`.

What it does with vectors that are not three long was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DOT](DOT.md) · [TRN](TRN.md)
