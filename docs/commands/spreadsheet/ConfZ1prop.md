# ConfZ1prop

A z confidence interval for one proportion, refused from Home.

| | |
|---|---|
| Syntax | `ConfZ1prop(input_list, ["configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ConfZ1prop({1,2,3,4,5})")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), given the list shape its syntax names.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**A proportion wants successes and a sample size rather than a column of
values** (HP help), so the list sent here may be the wrong shape as well as
reaching a command that refuses everything. [ConfZ2prop](ConfZ2prop.md) was
sent four separate numbers for that reason and was refused too, which is what
says the shape is not what decides it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ConfZ2prop](ConfZ2prop.md) · [HypZ1prop](HypZ1prop.md) · [SUM](SUM.md)
