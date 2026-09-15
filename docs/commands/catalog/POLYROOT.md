# POLYROOT

The roots of a polynomial.

| | |
|---|---|
| Syntax | `POLYROOT(Poly)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `POLYROOT([1,0,-4])` | `{−2.82353141256,−0.552220307199-1.1052954935*,−0.552220307199+1.1052954935*,0.927972026959}` | [emulator](../results.tsv) |

## Behaviour

**It answered four roots for a polynomial of degree two**, and two of them
are complex (emulator). The vector `[1,0,-4]` read as x squared minus four has
roots 2 and -2, so this answer is not that, and the entry does not pretend to
explain it: what the call was understood to mean is unmeasured (unverified).

That makes this row a record of one measured answer rather than a description
of the command (unverified), in the same way `C→PX` once recorded a call made
with the wrong shape of argument.

The complex roots carry the calculator's own imaginary unit (emulator),
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit), so the Result
cell was built from the stored row rather than typed.

The probe worth running next gives the polynomial the way
[POLYEVAL](POLYEVAL.md) and [POLYCOEF](POLYCOEF.md) take one, whose ordering
those two agree about, and checks whether the roots then come back as 2 and
-2 (unverified).

It answers a list of type 6 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[POLYCOEF](POLYCOEF.md) · [POLYEVAL](POLYEVAL.md)
