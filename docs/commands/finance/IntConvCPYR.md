# IntConvCPYR

How often a rate compounds, from the nominal and effective rates.

| | |
|---|---|
| Syntax | `IntConvCPYR(nominal_rate,effective_rate)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("IntConvCPYR(12,12.6825)")` | `11.9994580668` | [emulator](../results.tsv) |

## Behaviour

`IntConvCPYR(12,12.6825)` answers 11.9994580668 (emulator), a plain real of
type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It recovers the twelve compoundings the pair was built from** (emulator),
short by half a thousandth for the same reason
[IntConvNom](IntConvNom.md) is: the effective rate was handed over rounded to
12.6825 rather than 12.6825030132.

**It answers a fraction where the quantity is a count** (emulator). Nothing
compounds 11.9994580668 times a year, so a caller either rounds or reads the
answer as evidence that the two rates do not quite belong to a whole number
of periods. Which the calculator intends is not measured here (unverified).

The nominal rate comes first and the effective second (HP help), which is the
order the row above used.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[IntConvEff](IntConvEff.md) · [IntConvNom](IntConvNom.md)
