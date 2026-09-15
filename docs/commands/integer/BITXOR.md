# BITXOR

The bitwise exclusive OR of two or more integers.

| | |
|---|---|
| Syntax | `BITXOR(int1, int2, ... intn)` → integer |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `BITXOR(12, 10)` | `6` | [emulator](../results.tsv) |

## Behaviour

Bit by bit, the bits that differ: 1100 against 1010 is 0110, which is 6
(emulator). The answer is an ordinary number (emulator).

HP's syntax takes more than two (HP help), and nothing here has run three or
more. Negative and fractional arguments have not been measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BITAND](BITAND.md) · [BITOR](BITOR.md) · [BITNOT](BITNOT.md)
