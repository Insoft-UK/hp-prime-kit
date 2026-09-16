# REGRS

A regression over a range, refused from Home.

| | |
|---|---|
| Syntax | `REGRS(Input_range, [model], ["configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("REGRS(A1:A5)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**`REGRS(A1:A5)` is refused** (emulator), given a range and no model, where
the model is optional.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**Its second argument names a model** (HP help), which is a shape nothing in
this documentation has sent successfully yet: HP publishes no list of the
values it takes. [Depreciate](../finance/Depreciate.md) has the same
difficulty in another group and was refused too, though for reasons that are
its own.

**It is one of the four that would have answered something long** (emulator),
with [STAT1](STAT1.md), [STAT2](STAT2.md) and [AMORT](AMORT.md). All four
refused, so none of the four tested a long answer against the
harness's width.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[STAT1](STAT1.md) · [PredY](PredY.md) · [SUM](SUM.md)
