# CashFlowFMRR

A break-even rate of the same family, which this example cannot tell from MIRR.

| | |
|---|---|
| Syntax | `CashFlowFMRR(cash_flow_data, investment_rate, safe_investment_rate, [cashflows_per_year])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CashFlowFMRR({-1000,300,400,500},10,5)")` | `9.22317710801` | [emulator](../results.tsv) |

## Behaviour

`CashFlowFMRR({-1000,300,400,500},10,5)` answers 9.22317710801 (emulator), a
plain real of type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**[CashFlowMIRR](CashFlowMIRR.md) answered the same number, character for
character** (emulator), from the same list and the same two rates. One
example cannot separate the two commands, and this entry says so rather than
describing a difference nobody here has measured.

**The probe is a list where the rates have something to do** (emulator). The
flows used here go out once and come back three times, so the safe rate has
nothing to apply to. A list that turns negative again part way through is the
case the two names are said to treat differently, and it is one row away.

The same happened in Phase 6 with two unit commands that agreed on the pair
they were given (emulator), and the answer then was the same: record the
agreement, name the probe, and do not invent the difference.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CashFlowMIRR](CashFlowMIRR.md) · [CashFlowIRR](CashFlowIRR.md)
