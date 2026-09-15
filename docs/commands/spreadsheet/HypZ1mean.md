# HypZ1mean

A z test for one mean, refused from Home.

| | |
|---|---|
| Syntax | `HypZ1mean(input_list, ["configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HypZ1mean({1,2,3,4,5})")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), given the list shape its syntax names.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**It pairs with [ConfZ1mean](ConfZ1mean.md)** (HP help) and differs from
[HypT1mean](HypT1mean.md) in the distribution it assumes.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ConfZ1mean](ConfZ1mean.md) · [HypZ2mean](HypZ2mean.md) · [SUM](SUM.md)
