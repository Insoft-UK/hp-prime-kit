# IntConvNom

The nominal rate, from an effective rate and how often it compounds.

| | |
|---|---|
| Syntax | `IntConvNom(effective_rate,compounds_per_year)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("IntConvNom(12.6825,12)")` | `11.9999972992` | [emulator](../results.tsv) |

## Behaviour

`IntConvNom(12.6825,12)` answers 11.9999972992 (emulator), a plain real of
type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It recovers the twelve per cent [IntConvEff](IntConvEff.md) started from**
(emulator), and the three millionths missing are the four figures dropped
when 12.6825030132 was written down as 12.6825, not a disagreement between
the two commands.

That makes the pair a round trip in the same sense as the `Tvm` and `BrkEv`
families (emulator): each undoes the other, so a program can check its own
handling by going out and back.

The effective rate comes first, the compoundings second (HP help), the same
order [IntConvEff](IntConvEff.md) takes with the nominal rate in front.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[IntConvEff](IntConvEff.md) · [IntConvCPYR](IntConvCPYR.md)
