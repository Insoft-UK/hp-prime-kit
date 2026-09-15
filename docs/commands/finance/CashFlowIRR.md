# CashFlowIRR

The rate at which a list of cash flows breaks even.

| | |
|---|---|
| Syntax | `CashFlowIRR(cash_flow_data,[cashflows_per_year])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CashFlowIRR({-1000,300,400,500})")` | `8.89633946933` | [emulator](../results.tsv) |

## Behaviour

`CashFlowIRR({-1000,300,400,500})` answers 8.89633946933 (emulator), a plain
real of type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It is the rate that would make [CashFlowNPV](CashFlowNPV.md) zero**
(emulator), and the two rows check each other: at ten per cent that command
answers −21.0368144252, a negative number, so the break-even rate has to lie
below ten. It does, at 8.8963.

**The answer is a percentage, like the rate the others take** (emulator),
which is what makes the pair comparable at all.

**It takes no rate, because the rate is what it answers** (HP help). The
optional second argument is how many flows fall in a year and was not run
(unverified).

A list of flows that never changes sign has no break-even rate, and what this
command does with one was not measured (unverified). That is the case worth
guarding, since it is the one where an answer would be meaningless rather
than merely surprising.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CashFlowNPV](CashFlowNPV.md) · [CashFlowMIRR](CashFlowMIRR.md) ·
[CashFlowPB](CashFlowPB.md)
