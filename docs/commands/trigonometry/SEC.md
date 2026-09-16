# SEC

The secant: one over the cosine.

| | |
|---|---|
| Syntax | `SEC(value)` |
| Group | trigonometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SEC(1)` | `1.85081571768` | [emulator](../results.tsv) |

## Behaviour

`SEC(1)` answers 1.85081571768 (emulator): one over the cosine of one radian.

**The argument is an angle, so the answer depends on the mode**, which was
read in the same batch and is recorded once in [ACOT](ACOT.md) (emulator). A
program that sets a different mode gets a different number from the same call,
and nothing here measures that (unverified).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The calculator offers no `COS` in this group because `COS` is filed under
`catalog` (HP help). These three -- secant, [CSC](CSC.md) and [COT](COT.md) --
are the reciprocals it keeps separate.

What it answers where the cosine is zero, and the secant infinite, was not run
(unverified). The calculator has a way to write infinity, measured in
[Dirac](../catalog/Dirac.md), so whether it returns that or refuses is the question.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ASEC](ASEC.md) · [CSC](CSC.md) · [COT](COT.md)
