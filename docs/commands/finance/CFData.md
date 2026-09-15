# CFData

The cash flows, an empty list until a program puts some in.

| | |
|---|---|
| Syntax | `CFData` → list |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CFData")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**It answered `{}` with the Function app active, not its own** (emulator),
on a calculator the harness had just reset. Finance is the app where this is
common: 50 of its 68 variables answered from outside it, which is not what the
Triangle Solver's or the Function app's did,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**It holds the cash flows the app analyses** (unverified): HP’s list gives this name and its app,
and nothing more.

**Empty, with every cash-flow result refusing** (emulator). [NPV](NPV.md),
[IRR](IRR.md) and six more refused under both app conditions, and a list with
nothing in it is the likeliest reason: there is nothing to discount. Filling
this and reading `NPV` again is the probe (unverified).

**Whether a program can set it is untested** (unverified). [PV](PV.md) took
`PV:=1000` and kept it with the Finance app active, so a Finance variable can
be written; this one was not tried.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CFPYR](CFPYR.md) · [TotalCF](TotalCF.md) · [NPV](NPV.md)
