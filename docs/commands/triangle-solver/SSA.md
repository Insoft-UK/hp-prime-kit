# SSA

Two sides and an angle not between them, the ambiguous case.

| | |
|---|---|
| Syntax | `SSA(side,side,angle)` |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SSA(3,5,30)")` | `{5.9884394141,56.4426902381,93.5573097619}` | [emulator](../results.tsv) |
| `EXPR("SSA(3,4,30)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It answers one triangle: the missing side and the two missing angles**
(emulator), type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). The two angles and the
30 that was given sum to 180.

**This is the ambiguous case, and the answer does not say so** (emulator).
Two sides with an angle not between them can describe two different
triangles, and the command returns a single list with no hint that another
solution exists. A program taking the answer at face value may be using the
wrong one of two.

**Which of the two it chose is not established** (unverified). The probe is a
pair of sides and an angle where both triangles are clearly different, run
twice against a hand solution -- one row would show whether it always picks
the acute answer or the obtuse.

**The two rows differ only in whether the Triangle Solver was active**
(emulator); [SSS](SSS.md) carries that account.

Angles are in degrees (G2),
[apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SAS](SAS.md) · [SSS](SSS.md) · [AAS](AAS.md)
