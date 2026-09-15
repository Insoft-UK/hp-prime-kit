# BrkEvQuant

The quantity, from fixed cost, cost, price and profit.

| | |
|---|---|
| Syntax | `BrkEvQuant(fixed_cost,cost,price,profit)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("BrkEvQuant(1000,5,20,500)")` | `100` | [emulator](../results.tsv) |
| `EXPR("BrkEvQuant(1000,5,20,BrkEvProfit(1000,100,5,20))")` | `100` | [emulator](../results.tsv) |

## Behaviour

`BrkEvQuant(1000,5,20,500)` answers 100 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The second row is the check that matters** (emulator). It hands this
command exactly what [BrkEvProfit](BrkEvProfit.md) answered for a hundred
units, and gets a hundred back, exactly rather than to a few figures. That is
the calculator agreeing with itself across two names, and it is what says the
five `BrkEv` commands invert one equation rather than computing five
unrelated things.

**The exactness is worth noticing** (emulator). The `Tvm` family's round trip
comes back two billionths away from where it started, because it solves for a
rate by iteration; this one is a straight rearrangement, so it returns the
whole number.

The arguments omit the quantity, which is what this one answers (HP help), so
the positions differ from its siblings' and a program cannot reuse one
argument list across the family.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BrkEvProfit](BrkEvProfit.md) · [BrkEvCost](BrkEvCost.md) ·
[BrkEvFixed](BrkEvFixed.md) · [BrkEvPrice](BrkEvPrice.md)
