# SideB

The side opposite angle B.

| | |
|---|---|
| Syntax | `SideB` → real |
| Syntax | `SideB:=real` |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR(" SideB")` | `−1` | [emulator](../results.tsv) |
| `EXPR("SideB:=4")` | `4` | [emulator](../results.tsv) |

## Behaviour

**It reads −1 unset and accepts an assignment** (emulator), both with the
Triangle Solver active. [SideA](SideA.md) carries the account of what −1
means and why the app has to be active.

**It was not read back after being set** (emulator), where `SideA` was. The
pair is not repeated for every name in the group: one name carries the
read-assign-read-back evidence and the others carry the assignment. What
makes that honest rather than lazy is that [DoSolve](DoSolve.md) then solved
a 3-4-5 triangle, which it could only do if this assignment had taken.

**It is the second input of three** (emulator). See [SideA](SideA.md) for the
shape the app works in.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SideA](SideA.md) · [SideC](SideC.md) · [AngleB](AngleB.md) ·
[DoSolve](DoSolve.md)
