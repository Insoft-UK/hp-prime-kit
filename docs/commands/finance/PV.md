# PV

The present value: refused bare unless the Finance app is active, and a program can set it.

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
| `EXPR("Finance.PV")` | `0` | [emulator](../results.tsv) |

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
[TvmPV](TvmPV.md) was measured from a batch nobody had touched, so
with the Function app active, and it answered. A program that cannot select
the Finance app can still compute this value by calling the function with
its arguments, or read it as `Finance.PV`, below.

**A program can set it, and the value stays** (emulator). With the Finance app
active, `PV:=1000` answered `1000.00` and a later read in the same pass
answered `1000.00`. That is the only assignment measured in this app.

**With the app's name in front it answers from another app** (emulator):
`Finance.PV` read `0` with the Function app active, where `PV` alone was
refused, [apps.qualified-names](../../topics/apps.md#apps.qualified-names). It came back as `0`, not `0.00`: the two decimals follow the
app that is active, not the app the variable belongs to.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TvmPV](TvmPV.md) · [PPYR](PPYR.md) · [BEG](BEG.md) · [apps.finance-shows-two-decimals](../../topics/apps.md#apps.finance-shows-two-decimals)
