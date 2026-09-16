# BlackScholes

Answers a list of two, for an option on a stock.

| | |
|---|---|
| Syntax | `BlackScholes(stock_price,strike_price,time_to_maturity,risk_free_interest_rate,stock_volatility,stock_divi` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("BlackScholes(100,95,1,5,0.2,0)")` | `{9.63320467243,0}` | [emulator](../results.tsv) |

## Behaviour

`BlackScholes(100,95,1,5,0.2,0)` answers `{9.63320467243,0}` (emulator), a
list of type 6, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes), where
every other command in this group answers a single number.

**Two values come back and this entry does not say which is which**
(emulator). An option has a call price and a put price, and a list of two is
what a command answering both would give, but nothing measured here labels
the elements. The probe is a second call with the strike above the stock
price rather than below, which should move the two in opposite directions and
name them.

**The second element is exactly zero, which is worth suspicion rather than
belief** (emulator). A put on these terms should be worth something, so the
zero may mean the element is not a put at all, or that an argument the call
did not supply is needed before it computes.

**HP's own list is truncated** (HP help): the syntax row ends part way
through the sixth argument's name, so the full argument list is not published
in the list of names here. Six were sent because six are visible, and the
call was accepted, which says the visible six are enough to get an answer and
not that they are all of them.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CashFlowNPV](CashFlowNPV.md) · [TvmFV](TvmFV.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
