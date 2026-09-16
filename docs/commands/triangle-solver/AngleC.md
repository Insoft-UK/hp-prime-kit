# AngleC

The angle opposite side C.

| | |
|---|---|
| Syntax | `AngleC` → real |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR(" AngleC")` | `−1` | [emulator](../results.tsv) |
| `EXPR("  AngleC")` | `90` | [emulator](../results.tsv) |

## Behaviour

**It answered 90, which is the one number in this batch that needed no
calculator** (emulator). Sides of 3, 4 and 5 make a right triangle, and the
right angle is opposite the longest side. An answer of exactly 90 -- not
89.9999999 -- also says the app is not returning a rounded numerical solution
where an exact one exists.

**−1 before, 90 after** (emulator), with [DoSolve](DoSolve.md) between
them. [AngleA](AngleA.md) carries the account.

**90 is degrees, and here that is unmistakable**
(emulator). A right angle in radians is 1.5707963268, so this single row is
enough to establish the mode on its own, which is why it is worth stating
beside
[apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees)
rather than only pointing at it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AngleA](AngleA.md) · [AngleB](AngleB.md) · [SideC](SideC.md) ·
[DoSolve](DoSolve.md)
