# PV

The present value: needs the Finance app, and a program can set it.

| | |
|---|---|
| Syntax | `PV` → real |
| Syntax | `PV:=real` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("PV")` | *error* | [emulator](../results.tsv) |
| `EXPR(" PV")` | `0.00` | [emulator](../results.tsv) |
| `EXPR("PV:=1000")` | `1000.00` | [emulator](../results.tsv) |
| `EXPR("(PV)")` | `1000.00` | [emulator](../results.tsv) |

## Behaviour

**It refused with the Function app active and answered once Finance was
selected** (emulator), with nothing else changed between the two batches. It is
one of nine Finance variables that behave this way -- [NbPmt](NbPmt.md), [IPYR](IPYR.md), `PV`, [PMT](PMT.md), [FV](FV.md), [PPYR](PPYR.md), [CPYR](CPYR.md), [BEG](BEG.md) and [GSize](GSize.md), the
time-value-of-money names -- while 50 of their neighbours answer from any app, [apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**It holds the present value** (unverified): HP's list gives this name and its app, and
nothing more. It read `0.00` once Finance was active.

**The two decimals are the Finance app's display, not part of the value**
(emulator), [apps.finance-shows-two-decimals](../../topics/apps.md#apps.finance-shows-two-decimals).

**Its twin function answers without the app** (emulator):
[TvmPV](TvmPV.md) was measured in Phase 7 from a batch nobody had touched, so
with the Function app active, and it answered. A program that cannot select
the Finance app can still compute this value by calling the function with
its arguments.

**A program can set it, and the value stays** (emulator). With the Finance app
active, `PV:=1000` answered `1000.00` and a later read in the same pass
answered `1000.00`. That is the only assignment measured in this app.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TvmPV](TvmPV.md) · [PPYR](PPYR.md) · [BEG](BEG.md) · [apps.finance-shows-two-decimals](../../topics/apps.md#apps.finance-shows-two-decimals)
