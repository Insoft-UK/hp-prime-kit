# TvmIPYR

The interest rate a year, from the other four.

| | |
|---|---|
| Syntax | `TvmIPYR(NbPmt, PV, PMT, FV, [PPYR], [CPYR], [BEG])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("TvmIPYR(12,-1000,0,1051.16)")` | `4.9998186967` | [emulator](../results.tsv) |

## Behaviour

`TvmIPYR(12,-1000,0,1051.16)` answers 4.9998186967 (emulator), a plain real
of type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It recovers the five per cent the other commands were given** (emulator).
[TvmFV](TvmFV.md) turned five per cent into 1051.16189788, and handing the
printed 1051.16 back to this command returns 4.9998186967. The gap is the two
figures dropped when that number was written down, not a disagreement between
the commands.

**The answer is a rate a year, not a rate a period** (emulator). The twelve
periods are months, as [TvmFV](TvmFV.md) shows, and the answer is still about
five rather than about 0.4166.

The arguments omit the rate, which is what this one answers (HP help), so the
list is one shorter in the middle than its siblings' and the positions move.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TvmFV](TvmFV.md) · [TvmPV](TvmPV.md) · [TvmPMT](TvmPMT.md) ·
[TvmNbPmt](TvmNbPmt.md)
