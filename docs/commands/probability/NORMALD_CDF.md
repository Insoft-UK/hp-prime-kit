# NORMALD_CDF

The probability that a normal value is at or below a point.

| | |
|---|---|
| Syntax | `NORMALD_CDF([μ, σ,] x, [x2])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `NORMALD_CDF(0)` | `0.5` | [emulator](../results.tsv) |

## Behaviour

`NORMALD_CDF(0)` answers exactly 0.5 (emulator): half the standard normal
lies at or below its mean, which is the value that says the call was read as
the standard form.

**It is the inverse of [NORMALD_ICDF](NORMALD_ICDF.md)**, and the pair was
measured round-tripping: 0 goes to 0.5 here and 0.5 goes back to 0 there
(emulator).

Like [NORMALD](NORMALD.md) it takes μ and σ before the point, and both are
optional (emulator: measured on `NORMALD`, and the syntax is the same).

HP's syntax allows a second point (HP help), which would give the probability
of falling between two values rather than below one. That form was not run
(unverified), and it is the one worth having for a program asking about an
interval.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NORMALD](NORMALD.md) · [NORMALD_ICDF](NORMALD_ICDF.md)
