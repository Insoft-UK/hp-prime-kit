# Psi

The polygamma function.

| | |
|---|---|
| Syntax | `Psi(Real(a), Intg(n))` |
| Group | special |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `Psi(1,1)` | `π^2/6` | [emulator](../results.tsv) |

## Behaviour

**It answers an exact expression, not a decimal.** The result is pi squared
over six, written with the calculator's own pi, and its type is 8 (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers).

That value is the sum of one over every square, which is the closed form the
first polygamma takes at 1 (unverified). The row shows the calculator holding
it rather than approximating it.

Pi comes back as U+03C0, a character nobody types (emulator). It joins the
minus sign, the imaginary unit, the exponent glyph and the radical as
something the calculator writes and a keyboard does not,
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign). The Result cell above
was built from the stored row rather than typed, for that reason.

The second argument is the order, and HP writes the two as a real and an
integer (HP help). What a different order answers was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Gamma](Gamma.md) · [Beta](Beta.md) · [Ci](Ci.md)
