# BITNOT

The bitwise NOT of an integer.

| | |
|---|---|
| Syntax | `BITNOT(int)` → integer |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `BITNOT(12)` | `549755813875` | [emulator](../results.tsv) |

## Behaviour

The answer says how wide the calculator's integers are, and it is not 32 or
64 bits: 549,755,813,875 is 2^39 − 13, so flipping the bits of 12 filled
**39 bits** (emulator). A model that assumes a 32-bit or 64-bit complement
gets a different number, and so does anyone who expects −13.

Why 39, and whether the width changes with [SETBITS](SETBITS.md) or with the
calculator's integer settings, has not been measured (unverified). That is
the first thing to probe before relying on this command for a mask.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| `BITNOT(12)` expecting `-13`, the two's complement | the calculator answers 549755813875, a 39-bit complement | measured on the Virtual Calculator 2.4, build 2025-09-15, when this entry was written ([results.tsv](../results.tsv)) |

## Related

[BITAND](BITAND.md) · [BITOR](BITOR.md) · [SETBITS](SETBITS.md)
