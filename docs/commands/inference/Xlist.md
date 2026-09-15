# Xlist

The one variable measured that answers with the wrong app active.

| | |
|---|---|
| Syntax | `Xlist` → list |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Xlist")` | `{}` | [emulator](../results.tsv) |
| `EXPR(" Xlist")` | `{}` | [emulator](../results.tsv) |
| `EXPR("  Xlist")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**Three reads under three different active apps, all `{}`** (emulator): the
Function app, the Triangle Solver, and its own.

**It is not alone, and this entry said it was** (emulator). It claimed to be
the single variable on file that answers with a foreign app active. A later
batch read the other five lists of this app -- [Ylist](Ylist.md),
[ObsList](ObsList.md), [ExpList](ExpList.md), [ProbList](ProbList.md) and
[ContribList](ContribList.md) -- with the Function app active, and all five
answered `{}`. In the same batch 50 of the Finance app's 68 variables
answered from outside their app too. Whether a variable needs its app is a
fact about that variable,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app),
and this app's lists do not.

**Empty is a real value here, not a refusal** (emulator). Type 6, a list, and
the app's own worked example fills its summary statistics rather than its
lists -- see [Mean₁](Mean₁.md). So the app is loaded and these are
genuinely empty.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Ylist](Ylist.md) · [ObsList](ObsList.md) · [Xval](Xval.md) ·
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
