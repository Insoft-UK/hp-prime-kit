# Zeta

The Riemann zeta function.

| | |
|---|---|
| Syntax | `Zeta(x)` |
| Group | special |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `Zeta(2)` | `π^2/6` | [emulator](../results.tsv) |

## Behaviour

**It answers the exact closed form, not a decimal.** `Zeta(2)` comes back as
pi squared over six, of type 8 (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers). That is the sum of
one over every square, and the calculator knows it rather than approximating
it.

**[Psi](Psi.md) answers the same expression from a different question**, and
the two were measured in separate batches (emulator). Two commands arriving at
one value by different routes is a check neither row could give alone.

HP's list gives this name no syntax string (HP help), so the shape above is
what the measured call shows rather than something published. It was held back
into a small batch for that reason, and it compiled.

What it answers at an odd argument, where no such closed form exists, was not
run (unverified). Three is the interesting case: the value has no known
elementary form, so either a decimal comes back or the call is handed back
unevaluated the way [Ci](Ci.md) and [Ei](Ei.md) are.

Pi comes back as U+03C0, so the Result cell was built from the stored row
rather than typed (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Psi](Psi.md) · [Gamma](Gamma.md) · [Beta](Beta.md)
