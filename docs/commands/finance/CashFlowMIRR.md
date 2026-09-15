# CashFlowMIRR

A break-even rate that separates the borrowing rate from the reinvestment one.

| | |
|---|---|
| Syntax | `CashFlowMIRR(cash_flow_data, investment_rate, safe_investment_rate, [cashflows_per_year])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CashFlowMIRR({-1000,300,400,500},10,5)")` | `9.22317710801` | [emulator](../results.tsv) |

## Behaviour

`CashFlowMIRR({-1000,300,400,500},10,5)` answers 9.22317710801 (emulator), a
plain real of type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It sits above the plain break-even rate** (emulator).
[CashFlowIRR](CashFlowIRR.md) answers 8.89633946933 for the same list, and
the difference is what the two extra rates buy: the returns here are taken as
reinvested at ten per cent rather than at the answer itself.

**[CashFlowFMRR](CashFlowFMRR.md) answered exactly the same number, to every
figure** (emulator). The two commands cannot be told apart by this row, so
this entry does not describe a difference it has not seen. Separating them
wants a list where the rates matter more -- a flow that turns negative again
after the outlay, which is the case the two are said to treat differently.

The two rates go in investment first, safe second (HP help), and nothing
measured here confirms which the answer leaned on.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CashFlowFMRR](CashFlowFMRR.md) · [CashFlowIRR](CashFlowIRR.md) ·
[CashFlowNPV](CashFlowNPV.md)
