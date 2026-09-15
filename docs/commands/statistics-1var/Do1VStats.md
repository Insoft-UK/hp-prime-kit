# Do1VStats

Computes the one-variable statistics, refused with an empty data set.

| | |
|---|---|
| Syntax | `Do1VStats(Hn)` |
| Group | statistics-1var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Do1VStats(H1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The refusal is most likely about `H1` rather than about this command**
(unverified). A batch runs on a calculator reset before it, so the app's
first data set holds nothing, and there is nothing to compute statistics
from.

**Three of this group's six names answered and three refused** (emulator).
[CHECK](CHECK.md), [UNCHECK](UNCHECK.md) and [ISCHECK](ISCHECK.md) work; this
one, [SetFreq](SetFreq.md) and [SetSample](SetSample.md) do not. The three
that work take a number, and the three that refuse all name a data set.

**That division is the evidence** (emulator): it points at the empty data
sets rather than at the group, because the same batch showed the group
reachable.

**The lesson from `function` applies here** (emulator). That group was
recorded as refused until a batch measured the setup and found the variable
held the wrong thing; the same probe is owed here -- fill `H1`, read it back,
then call this.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SetSample](SetSample.md) · [SetFreq](SetFreq.md) · [CHECK](CHECK.md)
