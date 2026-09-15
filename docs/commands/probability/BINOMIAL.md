# BINOMIAL

The probability of exactly k successes in n tries.

| | |
|---|---|
| Syntax | `BINOMIAL(n, p, k)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `BINOMIAL(10,0.5,5)` | `0.24609375` | [emulator](../results.tsv) |

## Behaviour

`BINOMIAL(10,0.5,5)` answers 0.24609375 (emulator): the chance of exactly
five heads in ten fair tosses.

**That number is [COMB](COMB.md) of 10 and 5, divided by 1024** -- 252 over
two to the tenth, which is 0.24609375 exactly (emulator, and the arithmetic
that follows from it). The two commands were measured in the same batch, so a
program can check one against the other.

It is exact rather than rounded here because the answer happens to be a
fraction with a power of two underneath (emulator). Nothing about the command
promises that in general.

The three arguments go n, p, k: how many tries, the chance of each, and how
many successes (HP help). Getting p and k the wrong way round gives a number
rather than an error.

For "five or fewer" rather than "exactly five", the command is
[BINOMIAL_CDF](BINOMIAL_CDF.md), which answers 0.623046875 for these same
arguments (emulator).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BINOMIAL_CDF](BINOMIAL_CDF.md) · [BINOMIAL_ICDF](BINOMIAL_ICDF.md) ·
[COMB](COMB.md)
