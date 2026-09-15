# ConfZ1mean

A z confidence interval for one mean, refused from Home.

| | |
|---|---|
| Syntax | `ConfZ1mean(input_list, ["configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ConfZ1mean({1,2,3,4,5})")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), given the list shape its syntax names.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**It differs from [ConfT1mean](ConfT1mean.md) in the distribution it
assumes** (HP help), z where that one uses t, which matters when the sample
is small. Nothing measured here shows the difference, because neither ran.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ConfT1mean](ConfT1mean.md) · [ConfZ2mean](ConfZ2mean.md) · [SUM](SUM.md)
