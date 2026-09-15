# ContribList

Empty, and holds each cell’s contribution to the chi-square statistic.

| | |
|---|---|
| Syntax | `ContribList` → list |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ContribList")` | `{}` | [emulator](../results.tsv) |
| `EXPR(" ContribList")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**It read `{}` with the Inference app active and nothing assigned**
(emulator), type 6, and `{}` again with the Function app active -- the second
row. Like every list of this app it answers from a foreign app,
[Xlist](Xlist.md). Empty is a value here rather than a refusal: the app's
loaded example fills its summary statistics and leaves its lists alone, which
[Mean₁](Mean₁.md) records.

**It holds each cell’s contribution to the chi-square statistic** (unverified), and nothing measured says so -- no test of
that kind was run. [DoInference](DoInference.md) ran once, on the loaded
example, and the four variables watched across it were
[TestScore](TestScore.md), [Prob](Prob.md), [CritVal1](CritVal1.md) and
[Result](Result.md). Whether it writes this one is untested (unverified).

**Whether a program can set it is untested here and answered next door**
(emulator). [Ylist](Ylist.md) took `{1,2,3}` and kept it, so a list variable
of this app can be written; that this particular one can is expected rather
than measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ContribMat](ContribMat.md) · [ObsList](ObsList.md) · [TestScore](TestScore.md)
