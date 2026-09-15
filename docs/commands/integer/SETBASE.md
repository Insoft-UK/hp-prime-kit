# SETBASE

Shows an integer in another base.

| | |
|---|---|
| Syntax | `SETBASE(#integer[m] [,c])` → integer |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SETBASE(12, 2)` | `#14o` | [emulator](../results.tsv) |

## Behaviour

The answer comes back in the calculator's `#` notation, with a letter for the
base: `#14o` is octal, and 14 octal is 12 (emulator). What it does **not** do
is what the call looks like it asks for: a second argument of 2 did not give
binary.

So what that second argument means has not been established (unverified).
HP writes it as `c` with no explanation in the syntax, and one probe --
`SETBASE(12, 16)` beside `SETBASE(12, 8)` -- would say whether it is a base
at all, and if so why 2 answered octal.

The `TYPE` of the answer is 1, the integer kind, not 0 (emulator):
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SETBITS](SETBITS.md) · [GETBITS](GETBITS.md) · [BITNOT](BITNOT.md)
