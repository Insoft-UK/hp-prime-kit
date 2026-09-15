# FirstAsset

The first year of a depreciation, 1 as the app arrives.

| | |
|---|---|
| Syntax | `FirstAsset` → real |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("FirstAsset")` | `1` | [emulator](../results.tsv) |

## Behaviour

**It answered `1` with the Function app active, not its own** (emulator),
on a calculator the harness had just reset. Finance is the app where this is
common: 50 of its 68 variables answered from outside it, which is not what the
Triangle Solver's or the Function app's did,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**It holds which year of an asset’s life a depreciation is taken for** (unverified): HP’s list gives this name and its app,
and nothing more.

**Whether a program can set it is untested** (unverified). [PV](PV.md) took
`PV:=1000` and kept it with the Finance app active, so a Finance variable can
be written; this one was not tried.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LifeAsset](LifeAsset.md) · [FirstDateAsset](FirstDateAsset.md) · [CostAsset](CostAsset.md)
