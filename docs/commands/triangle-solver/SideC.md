# SideC

The side opposite angle C.

| | |
|---|---|
| Syntax | `SideC` → real |
| Syntax | `SideC:=real` |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR(" SideC")` | `−1` | [emulator](../results.tsv) |
| `EXPR("SideC:=5")` | `5` | [emulator](../results.tsv) |

## Behaviour

**It reads −1 unset and accepts an assignment** (emulator), both with the
Triangle Solver active, exactly as its two siblings do.
[SideA](SideA.md) carries the account.

**Its value was the hypotenuse of the triangle that was solved** (emulator).
Set to 5 beside sides of 3 and 4, it produced a right angle in
[AngleC](AngleC.md) -- 90 exactly -- which is the arithmetic anyone can check
and the reason these three numbers were chosen.

**Nothing here shows the app rejects an impossible triangle** (unverified).
Three sides that cannot close were never tried, and this group's commands
refuse in ways worth knowing: see [SSA](SSA.md), which refused one set of
arguments and answered another.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SideA](SideA.md) · [SideB](SideB.md) · [AngleC](AngleC.md) ·
[DoSolve](DoSolve.md)
