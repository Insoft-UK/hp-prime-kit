# AAS

Two angles and the side not between them.

| | |
|---|---|
| Syntax | `AAS(angle,angle,side)` |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AAS(40,60,10)")` | `{13.4729635533,15.3208888624,80}` | [emulator](../results.tsv) |
| `EXPR("AAS(30,60,10)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It answers the two missing sides and the missing angle** (emulator), a list
of type 6, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes). With angles
of 40 and 60 the third is 80, which is the last number, and the two before it
are sides.

**The arithmetic confirms where the given side sits** (emulator). The side of
10 lies opposite the **first** angle: ten over the sine of 40 degrees is
15.557, and that times the sines of 60 and 80 gives 13.473 and 15.321, which
is what came back. Had the side been opposite another angle the numbers would
differ, so this row fixes the argument order rather than assuming it.

**That also separates it from [ASA](ASA.md), which this documentation could
not tell apart before** (emulator). Given the same three numbers rearranged,
`ASA` answers 6.527 and 8.794 because its side lies **between** the two
angles rather than opposite the first. Two entries that once said nothing
measured separated them now have the numbers that do.

**The two rows differ only in whether the Triangle Solver was active**
(emulator); [SSS](SSS.md) carries that account.

Angles are in degrees (G2),
[apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ASA](ASA.md) · [SSS](SSS.md) · [SSA](SSA.md)
