# Ci

The cosine integral.

| | |
|---|---|
| Syntax | `Ci(Expr)` |
| Group | special |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `Ci(1)` | `Ci(1)` | [emulator](../results.tsv) |

## Behaviour

**The answer is the call itself.** `Ci(1)` comes back as `Ci(1)`, of type 8
(emulator), [ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers). The
calculator holds it exactly rather than working out a decimal.

It shares that with [Ei](Ei.md), [Si](Si.md) and [erf](erf.md), all measured
in one batch (emulator). [erfc](erfc.md) is the one that shows the algebra,
rewriting itself into another function, and [Gamma](Gamma.md) is the one that
answers a number.

A program cannot tell from a type-8 answer alone whether the calculator
computed something exact or simply declined to compute; here the text makes it
plain, because it is the question unchanged (emulator).

What turns it into a number was not measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Si](Si.md) · [Ei](Ei.md) · [erf](erf.md)
