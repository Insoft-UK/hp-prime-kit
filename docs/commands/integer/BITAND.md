# BITAND

The bitwise AND of two or more integers.

| | |
|---|---|
| Syntax | `BITAND(int1, int2, ... intn)` → integer |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `BITAND(12, 10)` | `8` | [emulator](../results.tsv) |

## Behaviour

Bit by bit: 12 is 1100 and 10 is 1010, so the bits they share are 1000, which
is 8 (emulator). The answer comes back as an ordinary number, not in the `#`
notation [SETBASE](SETBASE.md) and [SETBITS](SETBITS.md) use (emulator).

HP's syntax takes more than two (HP help); nothing here has run three or more.
What a negative or a fractional argument does has not been measured
(unverified), and neither has the width the calculator works in --
[BITNOT](BITNOT.md) is where that question shows up.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BITOR](BITOR.md) · [BITXOR](BITXOR.md) · [BITNOT](BITNOT.md)
