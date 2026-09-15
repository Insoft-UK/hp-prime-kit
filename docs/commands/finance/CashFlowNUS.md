# CashFlowNUS

The level amount per period worth the same as the flows.

| | |
|---|---|
| Syntax | `CashFlowNUS(cash_flow_data, investment_rate, [cashflows_per_year])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CashFlowNUS({-1000,300,400,500},10)")` | `−8.45921450151` | [emulator](../results.tsv) |

## Behaviour

`CashFlowNUS({-1000,300,400,500},10)` answers −8.45921450151 (emulator), a
plain real of type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It is the same value as the other two, said as a series** (emulator).
[CashFlowNPV](CashFlowNPV.md) answers −21.0368144252 today and
[CashFlowNFV](CashFlowNFV.md) answers −28 at the end; spreading that present
value evenly over three periods at ten per cent gives −8.459. Three ways of
writing one number, which is why a program should pick the one its reader
expects rather than computing all three.

**The spread is over three periods, not four** (emulator), matching the
horizon [CashFlowNFV](CashFlowNFV.md) shows: the flow at time zero is the
outlay, not one of the periods.

**The minus sign is the calculator's own, U+2212** (emulator):
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign). The Result cell was
built from the stored row rather than typed.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CashFlowNPV](CashFlowNPV.md) · [CashFlowNFV](CashFlowNFV.md) ·
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign)
