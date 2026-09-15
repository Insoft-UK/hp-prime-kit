# ConfT2mean

A t confidence interval for two means, refused from Home.

| | |
|---|---|
| Syntax | `ConfT2mean(input_list, ["configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ConfT2mean({1,2,3,4,5})")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), given the list shape its syntax names.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**It is the two-sample form of [ConfT1mean](ConfT1mean.md)** (HP help), and
one list was sent where two samples would be wanted, so this row cannot
separate a wrong argument from the group-wide refusal.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ConfT1mean](ConfT1mean.md) · [HypT2mean](HypT2mean.md) · [SUM](SUM.md)
