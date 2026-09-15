# SETBITS

Turns a number into the calculator's `#` integer.

| | |
|---|---|
| Syntax | `SETBITS(#integer[m] [,bits])` → integer |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SETBITS(12)` | `#Ch` | [emulator](../results.tsv) |

## Behaviour

Twelve comes back as `#Ch`: C in hexadecimal, which is what the trailing `h`
says (emulator). So the default display of a `#` integer is hexadecimal, and
the `TYPE` of the answer is 1 rather than 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

What the optional `bits` argument does has not been measured (unverified),
and it is the interesting one: [BITNOT](BITNOT.md) showed the calculator
complementing across 39 bits, and whether `SETBITS(12, 8)` narrows that is
exactly the question. `GETBITS(SETBITS(12))` would say what width an integer
carries by default.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[GETBITS](GETBITS.md) · [SETBASE](SETBASE.md) · [BITNOT](BITNOT.md)
