# CritVal1

The first critical value, 0 until DoInference put 0.432843347747 in it.

| | |
|---|---|
| Syntax | `CritVal1` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CritVal1")` | `0` | [emulator](../results.tsv) |
| `EXPR(" CritVal1")` | `0.432843347747` | [emulator](../results.tsv) |

## Behaviour

**0 before [DoInference](DoInference.md), 0.432843347747 after**
(emulator). [TestScore](TestScore.md) carries the account.

**[CritVal2](CritVal2.md) was not read after the run** (emulator), so whether
the pair is filled together is untested. The two names suggest a two-sided
interval with a bound in each, which would make the second the negative of
this one for a symmetric test -- and that is arithmetic about a test nobody
has identified (unverified).

**It is not a critical value in the textbook sense of a cut-off for the
statistic** (emulator). [TestScore](TestScore.md) came out at
−0.946 and this at 0.433, and 0.433 is neither a z nor a t threshold for
[Alpha](Alpha.md)'s 0.05. The likelier reading is that it bounds an interval
for the difference of means rather than for the statistic, which the numbers
fit; what the app actually computed is untested (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CritVal2](CritVal2.md) · [TestScore](TestScore.md) · [Conf](Conf.md)
