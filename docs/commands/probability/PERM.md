# PERM

How many ways to arrange r things out of n, order counting.

| | |
|---|---|
| Syntax | `PERM(n, r)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `PERM(5,2)` | `20` | [emulator](../results.tsv) |

## Behaviour

`PERM(5,2)` answers 20 (emulator): five choices for the first place and four
for the second.

**It is [COMB](COMB.md) times `r` factorial.** The same arguments give 10
there and 20 here (emulator), and the two commands differ only in whether the
order of what you drew counts as a different result.

It answers a plain number, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

A program reaching for the wrong one of the pair gets a plausible number
rather than an error, which is the reason this entry states the relation
rather than describing each in isolation (unverified).

What it does when `r` is larger than `n` was not run (unverified); zero is the
mathematical answer and an error is the other possibility.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[COMB](COMB.md) · [BINOMIAL](BINOMIAL.md)
