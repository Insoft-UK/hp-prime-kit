# SideA

The side opposite angle A, and a program can both read it and set it.

| | |
|---|---|
| Syntax | `SideA` → real |
| Syntax | `SideA:=real` |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR(" SideA")` | `−1` | [emulator](../results.tsv) |
| `EXPR("SideA:=3")` | `3` | [emulator](../results.tsv) |
| `EXPR("  SideA")` | `3` | [emulator](../results.tsv) |

## Behaviour

**A program can set it, and the value stays set** (emulator). These three
rows are one pass of one batch: read, assign, read back. The assignment
answers the number it stored, and the later read answers the same number. So
an entry in this app can say what few in this documentation can -- that a
program writes here and the app keeps it.

**All three rows were taken with the Triangle Solver selected by hand**
(emulator). This name was never read with another app active. Its neighbour
[AngleA](AngleA.md) was, and refused, which makes it likely this one would
too -- and likely is not measured, now that the Finance app has shown
variables of one app behaving differently from each other,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
(unverified).

**An unset side reads −1, not 0** (emulator). The first row was taken on a
calculator reset before the run, and −1 is what the app uses for "not
given". A program testing for 0 to find out whether a side is known will be
wrong on every fresh app, and a program that stores −1 deliberately is
storing "unknown". The minus sign is the calculator's own, U+2212,
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign).

**This is one third of the input to [DoSolve](DoSolve.md)** (emulator). With
`SideA`, `SideB` and `SideC` set to 3, 4 and 5 by the same batch, `DoSolve`
answered the triangle's three angles and wrote them into
[AngleA](AngleA.md), [AngleB](AngleB.md) and [AngleC](AngleC.md). That is the
whole working shape of this app from a program: variables in, `DoSolve`,
variables out.

**Whether a bad value is refused is untested** (unverified). Only 3 was ever
stored. What happens to a negative side, a zero, or a set of three sides that
cannot make a triangle is not known, and each costs one row.

The leading spaces in two of the calls are incidental (emulator): they exist
only so repeated reads keep separate rows, since `results.tsv` keys a row by
the exact text of its call.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SideB](SideB.md) · [SideC](SideC.md) · [AngleA](AngleA.md) ·
[DoSolve](DoSolve.md)
