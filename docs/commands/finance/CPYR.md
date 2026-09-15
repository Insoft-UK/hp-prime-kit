# CPYR

Compounding periods per year, 12 once the Finance app is active.

| | |
|---|---|
| Syntax | `CPYR` → real |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CPYR")` | *error* | [emulator](../results.tsv) |
| `EXPR(" CPYR")` | `12.00` | [emulator](../results.tsv) |

## Behaviour

**It refused with the Function app active and answered once Finance was
selected** (emulator), with nothing else changed between the two batches. It is
one of nine Finance variables that behave this way -- [NbPmt](NbPmt.md), [IPYR](IPYR.md), [PV](PV.md), [PMT](PMT.md), [FV](FV.md), [PPYR](PPYR.md), `CPYR`, [BEG](BEG.md) and [GSize](GSize.md), the
time-value-of-money names -- while 50 of their neighbours answer from any app, [apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**It holds how many times a year interest compounds** (unverified): HP's list gives this name and its app, and
nothing more. It read `12.00` once Finance was active, a default the app arrives with.

**The two decimals are the Finance app's display, not part of the value**
(emulator), [apps.finance-shows-two-decimals](../../topics/apps.md#apps.finance-shows-two-decimals).

**Whether a program can set it is untested** (unverified). [PV](PV.md) took
`PV:=1000` and kept it with the Finance app active, so a Finance variable can
be written; this one was not tried.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PV](PV.md) · [PPYR](PPYR.md) · [apps.finance-shows-two-decimals](../../topics/apps.md#apps.finance-shows-two-decimals)
