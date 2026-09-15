# BITSR

Shifts an integer's bits to the right.

| | |
|---|---|
| Syntax | `BITSR(int1 [, int2])` → integer |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `BITSR(8)` | `4` | [emulator](../results.tsv) |
| `BITSR(8, 2)` | `2` | [emulator](../results.tsv) |

## Behaviour

Without a second argument it shifts by one place, so 8 becomes 4 (emulator).
With one, it shifts by that many: 8 shifted twice is 2 (emulator). Each place
is a halving, and the bits pushed off the right-hand end are lost, which is
what makes it a division that throws the remainder away rather than a
division.

What it does with a negative number, where the sign bit would decide between
an arithmetic and a logical shift, has not been measured (unverified). Given
the width [BITNOT](BITNOT.md) showed, that is worth probing before trusting
it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BITSL](BITSL.md) · [BITAND](BITAND.md) · [BITNOT](BITNOT.md)
