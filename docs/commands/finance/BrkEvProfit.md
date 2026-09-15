# BrkEvProfit

The profit, from fixed cost, quantity, cost and price.

| | |
|---|---|
| Syntax | `BrkEvProfit(fixed_cost, quantity, cost, price)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("BrkEvProfit(1000,100,5,20)")` | `500` | [emulator](../results.tsv) |

## Behaviour

`BrkEvProfit(1000,100,5,20)` answers 500 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The arithmetic is visible in the answer** (emulator): a hundred units sold
at twenty, less a hundred bought at five, less a thousand of fixed cost, is
2000 minus 500 minus 1000, which is the 500 that came back. That is what says
the third argument is the cost per unit and not the total cost.

**Five names solve one equation, and this is the one for the profit**
(emulator): [BrkEvQuant](BrkEvQuant.md), [BrkEvCost](BrkEvCost.md),
[BrkEvFixed](BrkEvFixed.md) and [BrkEvPrice](BrkEvPrice.md) each take the
other four and answer the one they are named for. The round trip is recorded
in [BrkEvQuant](BrkEvQuant.md), which is handed this answer and returns the
hundred units it started from.

Break-even is where this answers zero (HP help), which no row here measures;
the name describes the family rather than this member.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BrkEvQuant](BrkEvQuant.md) · [BrkEvCost](BrkEvCost.md) ·
[BrkEvFixed](BrkEvFixed.md) · [BrkEvPrice](BrkEvPrice.md)
