# AnovaOneWay

One-way analysis of variance over any number of samples.

| | |
|---|---|
| Syntax | `AnovaOneWay({list1},{list2},[{list3}] ... [{List14}])` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AnovaOneWay({1,2,3},{4,5,6})")` | `{13.5,0.021311641129,1,13.5,13.5,4,4,1}` | [emulator](../results.tsv) |
| `EXPR("AnovaOneWay({1,2,3},{4,5,6},{7,8,9},{10,11,12})")` | `{45,0.000023559647,3,135,45,8,8,1}` | [emulator](../results.tsv) |

## Behaviour

**It answers a list of eight numbers whatever the input** (emulator), type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). Two samples give eight
and four samples give eight, so the length is fixed by the statistic and not
by how much data went in.

**That is worth knowing before planning a batch** (emulator). This command
was chosen once to force an answer long enough to test the harness's
160-character width, and it cannot: more samples make the numbers different,
not more numerous.

**The first two entries are the F statistic and its p value** (emulator). The
second row's F of 45 with a p of two hundred-thousandths is what four
well-separated samples should give, and the third entry rises from 1 to 3
with the degrees of freedom, which is what three more samples adds.

**It was the first row that showed `inference` reachable** (emulator),
answered in the probe that surveyed seven small groups at once.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Chi2TwoWay](Chi2TwoWay.md) · [LinRegrTConfInt](LinRegrTConfInt.md) ·
[DoInference](DoInference.md)
