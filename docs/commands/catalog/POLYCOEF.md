# POLYCOEF

The coefficients of the polynomial with the given roots.

| | |
|---|---|
| Syntax | `POLYCOEF(Vector)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `POLYCOEF([1,2])` | `[1,-3,2]` | [emulator](../results.tsv) |

## Behaviour

**It takes roots and answers coefficients**, which is the opposite direction
from what the name suggests to a reader expecting it to read a polynomial
apart. `POLYCOEF([1,2])` answers `[1,-3,2]` (emulator): the polynomial whose
roots are 1 and 2 is x squared minus three x plus two.

[POLYROOT](POLYROOT.md) is the command that goes the other way, and the two
together round-trip (unverified: that round trip was not run, and it is the
probe worth having).

The argument and the answer are both vectors, written with single brackets and
of type 4 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes) -- not lists, which is
the shape [POLYEVAL](POLYEVAL.md) also takes.

The coefficients run from the highest power down, which is what makes the
leading 1 first (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[POLYROOT](POLYROOT.md) · [POLYEVAL](POLYEVAL.md)
