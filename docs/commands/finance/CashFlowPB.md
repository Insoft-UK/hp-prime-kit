# CashFlowPB

How many periods it takes to get the money back.

| | |
|---|---|
| Syntax | `CashFlowPB(cash_flow_data, [investment_rate])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CashFlowPB({-1000,300,400,500})")` | `2.6` | [emulator](../results.tsv) |

## Behaviour

`CashFlowPB({-1000,300,400,500})` answers 2.6 (emulator), a plain real of
type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer shows the flows are counted undiscounted here** (emulator).
Three hundred and four hundred recover seven hundred of the thousand in two
periods, and three hundred of the third period's five hundred finishes it:
two periods plus three fifths, which is the 2.6 that came back. No
discounting is applied, because the rate was not given.

**It answers a fraction of a period, not a whole one** (emulator). The money
does not arrive part way through in most real schedules, so a caller that
needs a whole number has to round, and rounding down would claim the money
back before it is.

The rate is optional (HP help) and was not run (unverified). What it does to
the answer -- whether the recovery is then measured against discounted flows
-- is the probe worth one row.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CashFlowTotal](CashFlowTotal.md) · [CashFlowNPV](CashFlowNPV.md) ·
[CashFlowIRR](CashFlowIRR.md)
