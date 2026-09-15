# CashFlowNFV

What a list of cash flows is worth at the end, at a given rate.

| | |
|---|---|
| Syntax | `CashFlowNFV(cash_flow_data, investment_rate, [cashflows_per_year])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CashFlowNFV({-1000,300,400,500},10)")` | `−28` | [emulator](../results.tsv) |

## Behaviour

`CashFlowNFV({-1000,300,400,500},10)` answers −28 (emulator), a plain real of
type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It is the present value carried forward, and the arithmetic is exact**
(emulator). [CashFlowNPV](CashFlowNPV.md) answers −21.0368144252 for the same
list and rate, and that times 1.1 cubed is −28 to every figure the calculator
printed. Three periods of growth, one for each flow after the first, which is
what says the horizon is the last flow rather than the count of them.

**A round number out of an untidy one is worth trusting rather than
suspecting** (emulator): it falls out of the list chosen here and is not a
sign that the command rounds.

**The minus sign is the calculator's own, U+2212** (emulator):
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign). The Result cell was
built from the stored row rather than typed.

The third argument sets how many flows fall in a year (HP help) and was not
run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CashFlowNPV](CashFlowNPV.md) · [CashFlowNUS](CashFlowNUS.md) ·
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign)
