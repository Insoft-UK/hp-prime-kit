# MAXREAL

The largest real the calculator holds.

| | |
|---|---|
| Syntax | `MAXREAL` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MAXREAL` | `9.99999999999ᴇ499` | [emulator](../results.tsv) |

## Behaviour

**It is a bare name, not a call** (emulator), as [PI](PI.md) and
[MINREAL](MINREAL.md) are. HP's list gives it no syntax string for that
reason.

The answer is written with the calculator's own exponent glyph rather than an
`E` (emulator), [ppl.exponent-glyph](../../topics/ppl.md#ppl.exponent-glyph),
so the Result cell above was built from the stored row rather than typed.

**This row settled something unrelated, and that is worth recording.** Its
mantissa of nines and its exponent of 499 are the same pattern a value that
broke the harness's decoder carried, and this one decodes without trouble
because its sign nibble is ordinary. That is what says the two odd nibbles
seen elsewhere mark infinity itself rather than sheer magnitude (emulator).

It answers type 0, an ordinary real (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[MINREAL](MINREAL.md) · [PI](PI.md)
