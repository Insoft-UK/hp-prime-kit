# CFPYR

Cash flows per year, 12 as the app arrives.

| | |
|---|---|
| Syntax | `CFPYR` → real |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CFPYR")` | `12` | [emulator](../results.tsv) |
| `EXPR(" CFPYR")` | `12.00` | [emulator](../results.tsv) |

## Behaviour

**It answered `12` with the Function app active, not its own** (emulator),
on a calculator the harness had just reset. Finance is the app where this is
common: 50 of its 68 variables answered from outside it, which is not what the
Triangle Solver's or the Function app's did,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**It holds how many cash flows fall in a year** (unverified): HP’s list gives this name and its app,
and nothing more.

**With the Finance app active it reads `12.00`, the same value with two decimals**
(emulator), [apps.finance-shows-two-decimals](../../topics/apps.md#apps.finance-shows-two-decimals). The decimals are the app's display, not part of the
value.

**Whether a program can set it is untested** (unverified). [PV](PV.md) took
`PV:=1000` and kept it with the Finance app active, so a Finance variable can
be written; this one was not tried.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CFData](CFData.md) · [PPYR](PPYR.md) · [IRR](IRR.md)
