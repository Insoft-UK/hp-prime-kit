# CashFlowTotal

Adds up a list of cash flows, without discounting them.

| | |
|---|---|
| Syntax | `CashFlowTotal(cash_flow_data)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CashFlowTotal({-1000,300,400,500})")` | `200` | [emulator](../results.tsv) |

## Behaviour

`CashFlowTotal({-1000,300,400,500})` answers 200 (emulator), a plain real of
type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes): minus a
thousand plus three hundred plus four hundred plus five hundred.

**It is the only one of the family that takes no rate, and that is the
point** (emulator). Every other `CashFlow` command discounts, so it answers
what the flows are worth at some moment; this one answers what they add up
to, which is a different question and usually a larger number.
[CashFlowNPV](CashFlowNPV.md) gives −21.0368144252 for this same list at ten
per cent.

The flows go in as a list and the first is the one at time zero (emulator),
which is what the discounted members of the family show by leaving it
undiscounted.

What it does with an empty list was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CashFlowNPV](CashFlowNPV.md) · [CashFlowIRR](CashFlowIRR.md) ·
[CashFlowPB](CashFlowPB.md)
