# BrkEvFixed

The fixed cost, from quantity, cost, price and profit.

| | |
|---|---|
| Syntax | `BrkEvFixed(quantity, cost, price, profit)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("BrkEvFixed(100,5,20,500)")` | `1000` | [emulator](../results.tsv) |

## Behaviour

`BrkEvFixed(100,5,20,500)` answers 1000 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It returns the thousand the other four members were given** (emulator).
A hundred units at twenty, less a hundred at five, less the five hundred of
profit, leaves the thousand of fixed cost, which is the same equation
[BrkEvProfit](BrkEvProfit.md) reads in the other direction.

This is the only member whose argument list starts with the quantity
(HP help), because it is the only one that does not need the fixed cost as an
input.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BrkEvProfit](BrkEvProfit.md) · [BrkEvQuant](BrkEvQuant.md) ·
[BrkEvCost](BrkEvCost.md) · [BrkEvPrice](BrkEvPrice.md)
