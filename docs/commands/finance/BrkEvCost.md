# BrkEvCost

The cost per unit, from fixed cost, quantity, price and profit.

| | |
|---|---|
| Syntax | `BrkEvCost (fixed_cost, quantity, price, profit)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("BrkEvCost(1000,100,20,500)")` | `5` | [emulator](../results.tsv) |

## Behaviour

`BrkEvCost(1000,100,20,500)` answers 5 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It answers the cost of one unit, not of all of them** (emulator). The five
it returns times the hundred units is the five hundred of stock that
[BrkEvProfit](BrkEvProfit.md) subtracts, so a program holding a total has to
divide before calling this or it will be out by the quantity.

The arguments omit the cost, which is what this one answers (HP help). HP's
own list writes a space between the name and its bracket; the calculator
takes the call without it, which is how the row above was sent.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BrkEvProfit](BrkEvProfit.md) · [BrkEvQuant](BrkEvQuant.md) ·
[BrkEvFixed](BrkEvFixed.md) · [BrkEvPrice](BrkEvPrice.md)
