# TvmPV

The present value, from the other four.

| | |
|---|---|
| Syntax | `TvmPV(NbPmt, IPYR, PMT, FV, [PPYR], [CPYR], [BEG])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("TvmPV(12,5,0,1051.16)")` | `−999.998194492` | [emulator](../results.tsv) |
| `EXPR("TvmPV(12,5,0,TvmFV(12,5,-1000,0))")` | `−999.999999998` | [emulator](../results.tsv) |

## Behaviour

`TvmPV(12,5,0,1051.16)` answers −999.998194492 (emulator), a plain real of
type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The second row is the check that matters** (emulator). It hands this
command exactly what [TvmFV](TvmFV.md) answered, rather than a rounded copy
of it, and gets back −999.999999998: the thousand the other command started
from, to nine figures. That is the calculator agreeing with itself across two
names, which is worth more than either row alone, and it is what says the
five `Tvm` commands invert one equation rather than computing five unrelated
things.

**The difference between the two rows is the rounding, not the command**
(emulator). The first was given 1051.16, the printed value, and came back
1.8 thousandths away; the second was given the full answer and came back two
billionths away.

**The minus sign is the calculator's own, U+2212** (emulator), not the
hyphen a keyboard types:
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign). Both Result cells above
were built from the stored row rather than typed.

Money paid out is negative here as everywhere in this family (emulator): a
future value of about 1051 taken as positive makes the present value come
back negative.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TvmFV](TvmFV.md) · [TvmPMT](TvmPMT.md) · [TvmIPYR](TvmIPYR.md) ·
[TvmNbPmt](TvmNbPmt.md) ·
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign)
