# AMORT

An amortisation table into a range, refused from Home.

| | |
|---|---|
| Syntax | `AMORT(Range, n, i, pv, pmt[, ppyr=12, cpyr=ppyr, GroupSize=12])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AMORT(A1:A5,12,5,-1000,85.61)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), with a range and the five required
numbers: twelve periods, five per cent, a thousand borrowed and the payment
of 85.61.

**Those numbers are not arbitrary** (emulator). They are the ones
[TvmPMT](../finance/TvmPMT.md) answered for the same loan, so if this command
had run, its table could have been checked against a measured payment rather
than against an assumption. That check is still available once the command
can be reached.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**It writes into a range rather than answering** (HP help), which makes it
the one name here whose real behaviour a batch could not capture even if the
call were accepted: the result would be cells, not a value.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TvmPMT](../finance/TvmPMT.md) · [STAT1](STAT1.md) · [SUM](SUM.md)
