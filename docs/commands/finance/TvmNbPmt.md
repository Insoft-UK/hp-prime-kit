# TvmNbPmt

How many payments, from the other four.

| | |
|---|---|
| Syntax | `TvmNbPmt(IPYR, PV, PMT, FV, [PPYR], [CPYR], [BEG])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("TvmNbPmt(5,-1000,0,1051.16)")` | `11.9995657754` | [emulator](../results.tsv) |

## Behaviour

`TvmNbPmt(5,-1000,0,1051.16)` answers 11.9995657754 (emulator), a plain real
of type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It recovers the twelve periods the other commands were given** (emulator),
and the shortfall is the rounding in 1051.16 rather than a disagreement:
[TvmFV](TvmFV.md) answered 1051.16189788 from exactly twelve.

**It answers a fraction, and a program has to decide what to do with it**
(emulator). Twelve payments cannot be 11.9995657754 of anything real, so a
caller either rounds or treats the answer as the point where the balance is
reached part way through a period. Nothing here says which the calculator
intends.

The rate comes first in this one, because the count is what it answers
(HP help).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TvmFV](TvmFV.md) · [TvmPV](TvmPV.md) · [TvmPMT](TvmPMT.md) ·
[TvmIPYR](TvmIPYR.md)
