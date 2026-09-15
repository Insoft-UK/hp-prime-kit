# erf

The error function.

| | |
|---|---|
| Syntax | `erf(x)` |
| Group | special |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `erf(1)` | `erf(1)` | [emulator](../results.tsv) |

## Behaviour

**The answer is the call itself, unevaluated.** `erf(1)` comes back as
`erf(1)`, of type 8 (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers). The calculator
holds it as an exact object rather than working out a number.

That is the finding, and it is a trap worth stating plainly: a program that
prints this gets the text of its own question back, and one that compares it
against a decimal finds no match. Four of this group behave the same way --
[Ci](Ci.md), [Ei](Ei.md), [Si](Si.md) and this one (emulator).

What turns it into a number was not measured (unverified). Something in the
`approx` family is the usual answer on this calculator, and no row here shows
it.

[erfc](erfc.md) is the complement, and it answers something different in kind
rather than merely in value (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[erfc](erfc.md) · [Ci](Ci.md) · [Si](Si.md)
