# BSCall

The Black-Scholes value of a call, 0 while its twin BSPut refuses.

| | |
|---|---|
| Syntax | `BSCall` → real |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("BSCall")` | `0` | [emulator](../results.tsv) |
| `EXPR(" BSCall")` | `0.00` | [emulator](../results.tsv) |

## Behaviour

**It answered `0` with the Function app active, not its own** (emulator),
on a calculator the harness had just reset. Finance is the app where this is
common: 50 of its 68 variables answered from outside it, which is not what the
Triangle Solver's or the Function app's did,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**It holds the value of a call option by Black-Scholes** (unverified): HP’s list gives this name and its app,
and nothing more.

**Its twin [BSPut](BSPut.md) refused under both conditions, and this did not**
(emulator). Every Black-Scholes input read 0 -- [StockPrice](StockPrice.md),
[StrikePrice](StrikePrice.md), [Volatility](Volatility.md) -- so both values
are computed from nothing. That one answers 0 and the other refuses is the
difference this entry cannot explain, and a call with real inputs is the
probe (unverified).

**With the Finance app active it reads `0.00`, the same value with two decimals**
(emulator), [apps.finance-shows-two-decimals](../../topics/apps.md#apps.finance-shows-two-decimals). The decimals are the app's display, not part of the
value.

**Whether a program can set it is untested** (unverified). [PV](PV.md) took
`PV:=1000` and kept it with the Finance app active, so a Finance variable can
be written; this one was not tried.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BSPut](BSPut.md) · [StockPrice](StockPrice.md) · [Volatility](Volatility.md)
