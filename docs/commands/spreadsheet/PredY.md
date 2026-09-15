# PredY

Predicts a y from an x and a fitted model, refused from Home.

| | |
|---|---|
| Syntax | `PredY(mode, x, parameters)` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("PredY(1,2,3)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**`PredY(1,2,3)` is refused** (emulator), the same three numbers its mirror
[PredX](PredX.md) was given, with the same answer.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**The pair would check each other if either worked** (emulator): predicting a
y from an x and then an x back from that y should return the value it started
from, which is the round trip that settled two families in
[finance](../finance.md). It is the first thing to run once these can be
reached.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PredX](PredX.md) · [REGRS](REGRS.md) · [SUM](SUM.md)
