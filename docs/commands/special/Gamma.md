# Gamma

The gamma function: the factorial extended beyond whole numbers.

| | |
|---|---|
| Syntax | `Gamma(Real)` |
| Group | special |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `Gamma(5)` | `24` | [emulator](../results.tsv) |

## Behaviour

`Gamma(5)` answers 24 (emulator), which is four factorial: the function is
shifted by one, so `Gamma(n)` is the factorial of `n-1` rather than of `n`.

**That offset is the thing to get right** (emulator), and it is easy
to get wrong in either direction. A program wanting the factorial of 5
must call `Gamma(6)`.

It cross-checks against the factorial operator `!`, measured the same way:
`5!` answers 120, and 120 divided by 24 is 5 (emulator). Two commands
agreeing through arithmetic is worth more than either row alone.

**It is the one of this group that computes.** Seven of its neighbours answer
an exact or unevaluated expression of type 8; this answers a plain number of
type 0 (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers).

What it answers for a fraction, which is where the gamma function earns its
name, was not run (unverified). Half would give the square root of pi.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Beta](Beta.md) · [Psi](Psi.md) · [!](../probability/!.md)
