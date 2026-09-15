# Beta

The beta function.

| | |
|---|---|
| Syntax | `Beta(x, y)` |
| Group | special |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `Beta(2,3)` | `1/12` | [emulator](../results.tsv) |

## Behaviour

**It answers an exact fraction, not a decimal.** `Beta(2,3)` comes back as
`1/12` with type 8 (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers). A program
expecting 0.0833 will not find it, and comparing the answer against a number
will not work until it is converted.

The value follows from [Gamma](Gamma.md): the beta of two and three is the
gammas of each over the gamma of their sum, which is 1 times 2 over 24
(unverified). `Gamma` was measured in the same batch and answers plainly
rather than exactly, so the two commands of one family behave differently.

It is symmetric in its two arguments (unverified): `Beta(3,2)` should answer
the same fraction, and that was not run.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Gamma](Gamma.md) · [Psi](Psi.md) · [Zeta](Zeta.md)
