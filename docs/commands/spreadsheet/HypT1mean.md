# HypT1mean

A t test for one mean, refused from Home.

| | |
|---|---|
| Syntax | `HypT1mean(input_list, ["configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HypT1mean({1,2,3,4,5})")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), given the list shape its syntax names.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**It is the test beside the interval** (HP help):
[ConfT1mean](ConfT1mean.md) gives a range for the mean where this one asks
whether a claimed mean stands. The six `Conf` names and the six `Hyp` names
pair off that way.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ConfT1mean](ConfT1mean.md) · [HypT2mean](HypT2mean.md) · [SUM](SUM.md)
