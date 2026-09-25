# HAngle

The angle mode of Home: 0 is radians and 1 is degrees.

| | |
|---|---|
| Syntax | `HAngle` → real |
| Syntax | `HAngle:=value` |
| Group | home-settings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HAngle")` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("HAngle"); EXPR("HAngle:=1"); r := EXPR("HAngle"); EXPR("HAngle:=" + STRING(o)); RETURN r;` | `1` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("HAngle"); EXPR("HAngle:=1"); r := {EXPR("HAngle"), SIN(90)}; EXPR("HAngle:=" + STRING(o)); RETURN r;` | `{1,1}` | [emulator](../results.tsv) |

| `LOCAL o, r; o := EXPR("HAngle"); EXPR("HAngle:=2"); IFERR r := {EXPR("HAngle"), SIN(100)}; THEN r := "refused"; END; EXPR("HAngle:=" + STRING(o)); RETURN r;` | `{2,1}` | [emulator](../results.tsv) |

## Behaviour

**It reads 0 on a reset calculator, and 0 is radians** (emulator). The
trigonometric entries answered in radians with it at 0, as
[ACOT](../trigonometry/ACOT.md) records.

**A program can set it, and `SIN` follows at once** (emulator). Set to 1, it
read back 1, and in the same row `SIN(90)` answered 1: degrees. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

**The active app's angle mode overrides it once that is not 0**
(emulator): with the Function app's [AAngle](../common-app-mode/AAngle.md)
at 2, `SIN(90)` answered 1 while this stayed 0,
[apps.app-mode-overrides-home](../../topics/apps.md#apps.app-mode-overrides-home).
So this alone does not say what angle a program computes in.

**2 is gradians** (emulator): set to 2, `SIN(100)` answered 1, a right
angle being 100 gradians.

Whether a value a program sets outlasts the program was not tried
(unverified).

**The Triangle Solver answers in degrees whatever this holds** (emulator), a
fact of that app: [apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[HComplex](HComplex.md) · [ACOT](../trigonometry/ACOT.md) · [SIN](../catalog/SIN.md)
