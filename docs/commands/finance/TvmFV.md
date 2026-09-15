# TvmFV

The future value, from the other four.

| | |
|---|---|
| Syntax | `TvmFV(NbPmt, IPYR, PV, PMT, [PPYR], [CPYR], [BEG])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("TvmFV(12,5,-1000,0)")` | `1051.16189788` | [emulator](../results.tsv) |

## Behaviour

`TvmFV(12,5,-1000,0)` answers 1051.16189788 (emulator), a plain real of type
0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer says what the defaults are** (emulator). Twelve payments at five
per cent a year, starting from a thousand, come to 1051.16189788, and a
thousand times one plus five over twelve hundred, raised to the twelfth, is
1051.162. So the rate is divided by twelve: payments a year defaults to
twelve, and the twelve periods here are months rather than years.

**Money paid out is negative** (emulator). The present value was given as
-1000 and the future value came back positive. A program that makes both
positive is describing a different situation and gets a different number, not
an error.

**Five names solve one equation, and this is the one for the future value**
(emulator): [TvmPV](TvmPV.md), [TvmPMT](TvmPMT.md), [TvmIPYR](TvmIPYR.md) and
[TvmNbPmt](TvmNbPmt.md) each take the other four and answer the one they are
named for. The round trip is recorded in [TvmPV](TvmPV.md), which is handed
this answer and returns the thousand it started from.

The three optional arguments are payments a year, compounds a year and
whether payments fall at the beginning (HP help). None was run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TvmPV](TvmPV.md) · [TvmPMT](TvmPMT.md) · [TvmIPYR](TvmIPYR.md) ·
[TvmNbPmt](TvmNbPmt.md)
