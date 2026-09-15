# COMB

How many ways to choose r things from n, order not counting.

| | |
|---|---|
| Syntax | `COMB(n, r)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `COMB(5,2)` | `10` | [emulator](../results.tsv) |

## Behaviour

`COMB(5,2)` answers 10 (emulator): the ten pairs that can be drawn from five
things when `{a,b}` and `{b,a}` count as the same pair.

**[PERM](PERM.md) answers 20 for the same arguments** (emulator), exactly
twice as many, because it counts the two orders of each pair separately. The
factor is `r` factorial, and choosing between the two commands is choosing
whether order matters.

It answers a plain number, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

This is the coefficient that appears in [BINOMIAL](BINOMIAL.md): the
probability of five heads in ten tosses is `COMB(10,5)` over 1024, and both
were measured in the same batch (emulator).

What it does when `r` is larger than `n`, or when either is not whole, was not
run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PERM](PERM.md) · [BINOMIAL](BINOMIAL.md)
