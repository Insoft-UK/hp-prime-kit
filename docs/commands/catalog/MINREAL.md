# MINREAL

The smallest positive real the calculator holds.

| | |
|---|---|
| Syntax | `MINREAL` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MINREAL` | `1ᴇ−499` | [emulator](../results.tsv) |

## Behaviour

**It is the smallest positive value, not the most negative one** (emulator).
A program looking for a lower bound to compare against will not find it here:
this is the closest the machine gets to zero from above.

Like [MAXREAL](MAXREAL.md) it is a bare name with no syntax string on HP's
list (HP help), and its answer carries both the exponent glyph and the
calculator's minus sign (emulator),
[ppl.exponent-glyph](../../topics/ppl.md#ppl.exponent-glyph). The Result cell
was built from the stored row for that reason.

Its exponent is the mirror of [MAXREAL](MAXREAL.md)'s, so the two mark the
range the machine can represent at all (emulator).

It answers type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[MAXREAL](MAXREAL.md) · [PI](PI.md)
