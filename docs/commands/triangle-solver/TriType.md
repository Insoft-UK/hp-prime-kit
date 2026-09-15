# TriType

The one variable of this app that DoSolve left alone.

| | |
|---|---|
| Syntax | `TriType` → real |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR(" TriType")` | `0` | [emulator](../results.tsv) |
| `EXPR("  TriType")` | `0` | [emulator](../results.tsv) |

## Behaviour

**It read 0 before [DoSolve](DoSolve.md) and 0 after** (emulator), in the
same pass where the six other variables of this app all changed. That makes
it the only one the command does not write, and it is why both rows are kept:
a pair that does not move is evidence, where one row would only have been a
value.

**It starts at 0 where the sides and angles start at −1** (emulator). The
others use −1 for "not given"; this one does not, which suggests 0 is a
real setting rather than an absence -- a code for which kind of triangle the
app is set to solve. Which codes exist is not measured, and HP's list gives
this name no syntax string (HP help).

**Nothing here says whether a program can set it** (unverified). No
assignment was tried. Since it did not change when a triangle was solved, the
likely reading is that it is an input chosen before solving rather than an
output, and the likely reading is not the measured one. One assignment and
one read-back would settle it.

**A right triangle was solved while this held 0** (emulator), so whatever 0
means, it does not stop the app solving a right triangle from three sides.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DoSolve](DoSolve.md) · [SideA](SideA.md) · [AngleA](AngleA.md)
