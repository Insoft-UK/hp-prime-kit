# BITSL

Shifts an integer's bits to the left.

| | |
|---|---|
| Syntax | `BITSL(int1 [, int2])` → integer |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `BITSL(1)` | `2` | [emulator](../results.tsv) |
| `BITSL(1, 3)` | `8` | [emulator](../results.tsv) |

## Behaviour

Without a second argument it shifts by one place, so 1 becomes 2 (emulator).
With one, it shifts by that many: 1 shifted three places is 8 (emulator). Each
place is a doubling, which is the useful way to remember it.

What happens when a bit is pushed past the width the calculator works in --
39 bits, as far as [BITNOT](BITNOT.md) shows -- has not been measured
(unverified), and neither has a negative shift.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BITSR](BITSR.md) · [BITAND](BITAND.md) · [BITNOT](BITNOT.md)
