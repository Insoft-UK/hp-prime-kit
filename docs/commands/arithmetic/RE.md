# RE

The real part of a complex number.

| | |
|---|---|
| Syntax | `RE(x+yi)` |
| Group | arithmetic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `RE(3+4*i)` | `3` | [emulator](../results.tsv) |
| `RE((3,4))` | `3` | [emulator](../results.tsv) |

## Behaviour

**Both ways of writing a complex number are accepted.** `3+4*i` and `(3,4)`
answer the same 3 (emulator), so a program may use the arithmetic form or the
pair, and neither is the one true spelling.

The ASCII letter `i` works as the imaginary unit on input (emulator). What
comes back carries a different character, which [CONJ](CONJ.md) shows and
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit) records.

The answer is a plain number, `TYPE` 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): taking the real part
leaves the complex behind rather than giving a complex with zero imaginary
part.

Whether `i` also works as an ordinary variable name is a different question
and still open (unverified),
[ppl.i-e-as-locals](../../topics/ppl.md#ppl.i-e-as-locals).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[IM](IM.md) · [ARG](ARG.md) · [CONJ](CONJ.md)
