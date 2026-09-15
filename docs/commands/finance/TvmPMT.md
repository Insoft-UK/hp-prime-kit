# TvmPMT

The payment, from the other four.

| | |
|---|---|
| Syntax | `TvmPMT(NbPmt, IPYR, PV, FV, [PPYR], [CPYR], [BEG])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("TvmPMT(12,5,-1000,0)")` | `85.6074817885` | [emulator](../results.tsv) |

## Behaviour

`TvmPMT(12,5,-1000,0)` answers 85.6074817885 (emulator), a plain real of type
0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**That is a thousand repaid over twelve months, not twelve years**
(emulator). Twelve payments of 85.61 come to 1027.29, which is the thousand
plus the interest on a balance that falls each month, and it agrees with the
rate being divided by twelve the way [TvmFV](TvmFV.md) shows.

**The arguments are not in the same order as its siblings** (HP help). This
one takes the present value and the future value, where
[TvmFV](TvmFV.md) takes the present value and the payment. Each of the five
omits the quantity it answers, so the position of a number changes with the
name and a program cannot reuse one argument list across them.

Money paid out is negative (emulator): the thousand was given as -1000 and
the payment came back positive.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TvmFV](TvmFV.md) · [TvmPV](TvmPV.md) · [TvmIPYR](TvmIPYR.md) ·
[TvmNbPmt](TvmNbPmt.md)
