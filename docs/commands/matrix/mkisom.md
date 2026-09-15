# mkisom

Builds the matrix of an isometry.

| | |
|---|---|
| Syntax | `mkisom(Vector, sign)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `mkisom([1,2],1)` | `[[0.540302305868,−0.841470984808],[0.841470984808,0.540302305868]]` | [emulator](../results.tsv) |

## Behaviour

`mkisom([1,2],1)` answers a two by two matrix whose entries are the
cosine and sine of 1 (emulator): a rotation by one radian.

**HP's published syntax for this name is ambiguous**, written as
`mkisom(Vect,(Sign(1) or -1))` (HP help), which is why it was held back into a
smaller batch rather than risked among forty calls. It compiled and ran
(emulator).

The angle is taken in radians here (emulator), as
[ARG](../arithmetic/ARG.md) answers in radians. Neither row read the
calculator's angle mode back, so what a different mode would do is unmeasured
(unverified).

What the second argument does, and what -1 gives instead of 1, was not run
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ARG](../arithmetic/ARG.md) · [IDENMAT](IDENMAT.md) · [TRN](TRN.md)
