# PercentMarkup

The difference between cost and price, over the price.

| | |
|---|---|
| Syntax | `PercentMarkup(cost,price)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("PercentMarkup(60,100)")` | `40` | [emulator](../results.tsv) |

## Behaviour

`PercentMarkup(60,100)` answers 40 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**That is the difference over the price** (emulator). With a cost of 60 and a
price of 100 the difference is 40, and 40 over 100 is 40. Dividing by the
cost instead would give 66.6666666667, which is what
[PercentMargin](PercentMargin.md) answers for the same two arguments.

**Which means it does not compute what a markup usually means** (emulator).
In ordinary accounting a markup is the difference over the *cost*, and what
this answers is the figure usually called the margin. The two names on this
calculator hold each other's usual meanings.

The arguments go in cost first, price second (HP help).

What it does when the price is below the cost was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| `PercentMarkup(cost,price)` for a markup on cost | Answers the difference over the *price*, which is the smaller number and is never flagged. The markup over the cost is [PercentMargin](PercentMargin.md) | [emulator](../results.tsv) |

## Related

[PercentMargin](PercentMargin.md) · [PercentChange](PercentChange.md) ·
[PercentTotal](PercentTotal.md)
