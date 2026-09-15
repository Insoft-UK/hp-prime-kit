# SSS

Solves a triangle from three sides, and answers in degrees.

| | |
|---|---|
| Syntax | `SSS(side,side,side)` |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SSS(6,8,10)")` | `{36.8698976458,53.1301023542,90}` | [emulator](../results.tsv) |
| `SSS(3,4,5)` | `{36.8698976458,53.1301023542,90}` | G2 |
| `EXPR("SSS(3,4,5)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Three rows, and together they settle the group** (emulator and G2). The
last is a batch with another app active and is refused. The middle is the
same call typed by hand with the Triangle Solver selected, and it answers.
The first is a batch **with the app selected before the program ran**, and it
answers too -- so the rule reaches inside a program and the harness can
measure this group after all:
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**The first two rows check each other** (emulator and G2). A 6-8-10 triangle
is a 3-4-5 scaled, so its angles must be identical, and they are to every
digit. One was read off the screen by hand and the other was decoded from the
calculator's memory by the harness; agreeing to ten figures is what makes
both trustworthy.

**The answer is in degrees, and that is a trap** (G2). The three numbers are
the angles of that triangle in degrees and they sum to 180. Everything else
this documentation has measured is in radians:
[angle](../geometry/angle.md) answers half of pi for a right angle,
[apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees).

**The angles come back smallest first, matching the sides in the order
given** (emulator): 36.87 opposite the shortest side, the right angle
opposite the longest.

**The sides are not returned** (emulator), only the angles, so a program
needing the whole solved triangle must keep what it passed in. Its four
siblings do return sides, because they were given fewer.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| Feeding an angle from here straight into `SIN` or `COS` | The angle is in degrees and those take radians, so the result is wrong by a factor near 57 and nothing raises | G2 |

## Related

[SAS](SAS.md) · [ASA](ASA.md) · [AAS](AAS.md) · [SSA](SSA.md) ·
[apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees)
