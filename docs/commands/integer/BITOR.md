# BITOR

The bitwise OR of two or more integers.

| | |
|---|---|
| Syntax | `BITOR(int1, int2, ... intn)` → integer |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `BITOR(12, 10)` | `14` | [emulator](../results.tsv) |

## Behaviour

Bit by bit: 1100 or 1010 is 1110, which is 14 (emulator). The answer is an
ordinary number (emulator).

HP's syntax takes more than two (HP help), and nothing here has run three or
more. Negative and fractional arguments have not been measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BITAND](BITAND.md) · [BITXOR](BITXOR.md) · [BITNOT](BITNOT.md)
