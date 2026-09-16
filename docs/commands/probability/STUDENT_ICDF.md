# STUDENT_ICDF

The point a Student's t distribution reaches a probability at.

| | |
|---|---|
| Syntax | `STUDENT_ICDF(d, p)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `STUDENT_ICDF(3,0.5)` | `0` | [emulator](../results.tsv) |

## Behaviour

`STUDENT_ICDF(3,0.5)` answers exactly 0 (emulator), because Student's t is
symmetric about zero: half of it lies on each side whatever the degrees of
freedom.

**That exact zero is the useful part of this row.** A value that comes back
as a clean 0 rather than as a rounding of it says the command is doing the
symmetric thing rather than approximating its way there
(emulator). [NORMALD_ICDF](NORMALD_ICDF.md) answers the same 0 at the same
probability for the same reason.

It takes the degrees of freedom first and the probability second (HP help),
mirroring [STUDENT_CDF](STUDENT_CDF.md), which takes a point where this takes
a probability. Confusing the two gives a number rather than an error.

What it answers for a probability of 0 or 1, where the point is infinite, was
not run (unverified); the calculator does have a way to write infinity,
measured in [Dirac](../catalog/Dirac.md).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[STUDENT](STUDENT.md) · [STUDENT_CDF](STUDENT_CDF.md) ·
[NORMALD_ICDF](NORMALD_ICDF.md)
