# BSPut

The Black-Scholes value of a put, refused while its twin BSCall answers.

| | |
|---|---|
| Syntax | `BSPut` → real |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("BSPut")` | *error* | [emulator](../results.tsv) |
| `EXPR(" BSPut")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It refused with the Function app active and again with Finance's**
(emulator). So this is not the app rule, which freed nine of its neighbours
the moment Finance was selected -- see [PV](PV.md). Something other than the
active app keeps it from answering.

**It holds the value of a put option by Black-Scholes** (unverified): HP's list gives this name and its app, and
nothing more.

**Its twin [BSCall](BSCall.md) answered 0 under both conditions** (emulator),
with every Black-Scholes input at 0. Both values are computed from nothing,
and only this one refuses. Why is untested, and a call with real inputs --
a stock price, a strike, a volatility -- is the probe (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BSCall](BSCall.md) · [StockPrice](StockPrice.md)
