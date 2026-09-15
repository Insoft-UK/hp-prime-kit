# CashFlowNPV

What a list of cash flows is worth today, at a given rate.

| | |
|---|---|
| Syntax | `CashFlowNPV(cash_flow_data, investment_rate, [cashflows_per_year])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CashFlowNPV({-1000,300,400,500},10)")` | `−21.0368144252` | [emulator](../results.tsv) |

## Behaviour

`CashFlowNPV({-1000,300,400,500},10)` answers −21.0368144252 (emulator), a
plain real of type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer says how the arguments are read** (emulator). Three hundred over
1.1, plus four hundred over 1.21, plus five hundred over 1.331, less the
thousand, is −21.04. So the rate is a percentage rather than a fraction, the
first flow sits at time zero and is not discounted, and each later one is
discounted by one more period.

**A negative answer means the flows do not clear the rate asked for**
(emulator), and [CashFlowIRR](CashFlowIRR.md) says by how much: it answers
8.89633946933, which is below the ten per cent demanded here. The two rows
agree, and a program can use one to sanity-check the other.

**The minus sign is the calculator's own, U+2212** (emulator), not the hyphen
a keyboard types:
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign). The Result cell above
was built from the stored row rather than typed.

The third argument sets how many flows fall in a year (HP help) and was not
run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CashFlowIRR](CashFlowIRR.md) · [CashFlowNFV](CashFlowNFV.md) ·
[CashFlowTotal](CashFlowTotal.md) ·
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign)
