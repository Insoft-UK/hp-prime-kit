# PercentMargin

The difference between cost and price, over the cost.

| | |
|---|---|
| Syntax | `PercentMargin(cost,price)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("PercentMargin(60,100)")` | `66.6666666667` | [emulator](../results.tsv) |

## Behaviour

`PercentMargin(60,100)` answers 66.6666666667 (emulator), a plain real of
type 0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**That is the difference over the cost, not over the price** (emulator). With
a cost of 60 and a price of 100 the difference is 40; 40 over 60 is
66.6666666667 and 40 over 100 is 40. The answer is the first of those, so
this name divides by the cost.

**Which means it does not compute what a margin usually means** (emulator).
In ordinary accounting a margin is the difference over the *price* -- 40 here
-- and what this answers is the figure usually called the markup on cost.
[PercentMarkup](PercentMarkup.md) answers 40 for the same two arguments, so
the two names hold each other's usual meanings.

The arguments go in cost first, price second (HP help), and the answer above
is consistent with that order: reading them the other way would give a
negative number.

What it does when the price is below the cost was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| `PercentMargin(cost,price)` for a profit margin | Answers the difference over the *cost*, which is larger than the margin and never flagged. The margin over the price is [PercentMarkup](PercentMarkup.md) | [emulator](../results.tsv) |

## Related

[PercentMarkup](PercentMarkup.md) · [PercentChange](PercentChange.md) ·
[PercentTotal](PercentTotal.md)
