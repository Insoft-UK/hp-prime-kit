# ASA

Two angles and the side between them.

| | |
|---|---|
| Syntax | `ASA(angle,side,angle)` |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ASA(40,10,60)")` | `{6.52703644666,8.79385241572,80}` | [emulator](../results.tsv) |
| `EXPR("ASA(30,10,60)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It answers the two missing sides and the missing angle** (emulator), type
6, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes): angles of 40 and 60
leave 80, and the sides are 6.527 and 8.794.

**The arithmetic confirms that the side lies between the two angles**
(emulator). A side of 10 opposite the 80-degree angle gives ten over the sine
of 80, which is 10.154, and that times the sines of 40 and 60 gives exactly
the two numbers returned.

**That is the difference from [AAS](AAS.md), measured rather than assumed**
(emulator). The same three numbers given to that command answer 13.473 and
15.321, because there the side of 10 lies opposite the first angle instead.
Both entries once said that nothing measured separated them; these two rows
do.

**The two rows differ only in whether the Triangle Solver was active**
(emulator); [SSS](SSS.md) carries that account.

**Writing the angles as degrees was correct** (G2), which this entry once
doubted: the app has its own mode,
[apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AAS](AAS.md) · [SSS](SSS.md) · [SAS](SAS.md)
