# PredX

Predicts an x from a y and a fitted model, refused from Home.

| | |
|---|---|
| Syntax | `PredX(mode, y, parameters)` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("PredX(1,2,3)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**`PredX(1,2,3)` is refused** (emulator), given three plain numbers where the
syntax names a mode, a value and parameters.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**The third argument is called parameters and nothing published says its
shape** (HP help). Three numbers were sent because a probe has to choose
something, and a number may well be wrong where a list or a fitted model is
wanted. This row cannot separate a bad third argument from the group-wide
refusal.

[PredY](PredY.md) is its mirror and was refused identically (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PredY](PredY.md) · [REGRS](REGRS.md) · [SUM](SUM.md)
