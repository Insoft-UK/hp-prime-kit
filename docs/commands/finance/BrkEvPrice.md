# BrkEvPrice

The price per unit, from fixed cost, quantity, cost and profit.

| | |
|---|---|
| Syntax | `BrkEvPrice(fixed_cost, quantity, cost, profit)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("BrkEvPrice(1000,100,5,500)")` | `20` | [emulator](../results.tsv) |

## Behaviour

`BrkEvPrice(1000,100,5,500)` answers 20 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It returns the twenty the other members were given** (emulator): the
thousand of fixed cost, the five hundred of stock and the five hundred of
profit come to two thousand, spread over a hundred units.

Like [BrkEvCost](BrkEvCost.md), the answer is per unit rather than a total,
so a program holding revenue has to divide by the quantity before comparing
(emulator).

The arguments omit the price, which is what this one answers (HP help).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BrkEvProfit](BrkEvProfit.md) · [BrkEvQuant](BrkEvQuant.md) ·
[BrkEvCost](BrkEvCost.md) · [BrkEvFixed](BrkEvFixed.md)
