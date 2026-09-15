# Chi2GOF

The chi-square goodness-of-fit test, refused for the arguments given.

| | |
|---|---|
| Syntax | `Chi2GOF(List1, List2, Value)` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Chi2GOF(1,2,3)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Three plain numbers were sent where two lists are wanted** (HP help), so
this refusal most likely measures the call rather than the command
(unverified).

**The group answers** (emulator): [Chi2TwoWay](Chi2TwoWay.md),
[AnovaOneWay](AnovaOneWay.md) and the four `LinRegrT` names all returned
lists in the same batches. So a refusal here is about what was passed.

**It was sent deliberately in that wrong shape** (emulator), as part of a
probe asking whether commands report failure as text or as a refusal. This
one refuses outright, where `residue` in another group answers a string
carrying its own error message.

The probe is two lists of observed and expected counts (unverified), which is
what the published syntax asks for.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Chi2TwoWay](Chi2TwoWay.md) · [LinRegrTTest](LinRegrTTest.md)
