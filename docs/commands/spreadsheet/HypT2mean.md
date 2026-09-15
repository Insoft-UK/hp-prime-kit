# HypT2mean

A t test for two means, refused from Home.

| | |
|---|---|
| Syntax | `HypT2mean(input_list, ["configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HypT2mean({1,2,3,4,5})")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), given the list shape its syntax names.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**It pairs with [ConfT2mean](ConfT2mean.md)** (HP help), the interval beside
the test, and one list was sent where two samples would be wanted.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ConfT2mean](ConfT2mean.md) · [HypT1mean](HypT1mean.md) · [SUM](SUM.md)
