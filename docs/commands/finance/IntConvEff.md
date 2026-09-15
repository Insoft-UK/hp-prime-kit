# IntConvEff

The effective rate, from a nominal rate and how often it compounds.

| | |
|---|---|
| Syntax | `IntConvEff(nominal_rate,compounds_per_year)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("IntConvEff(12,12)")` | `12.6825030132` | [emulator](../results.tsv) |

## Behaviour

`IntConvEff(12,12)` answers 12.6825030132 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer says the arithmetic** (emulator): one plus twelve over twelve
hundred, raised to the twelfth, less one, is 0.126825, and twelve per cent
compounded monthly is worth 12.6825 per cent over the year. So both arguments
are read as percentages and the answer is a percentage too, not a fraction.

**The two arguments are easy to swap and the mistake is quiet** (emulator).
Both are 12 in the row above, which is why this entry says the order rather
than relying on the example: the rate comes first and the number of
compoundings second.

[IntConvNom](IntConvNom.md) reverses it and [IntConvCPYR](IntConvCPYR.md)
answers the third quantity, so the three together cover one relation
(emulator): each was given what the others answered and returned the value
that started the chain, short only by the figures dropped in writing it down.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[IntConvNom](IntConvNom.md) · [IntConvCPYR](IntConvCPYR.md) ·
[TvmIPYR](TvmIPYR.md)
