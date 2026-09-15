# HypZ2prop

A z test for two proportions, refused from Home.

| | |
|---|---|
| Syntax | `HypZ2prop(Input_List, ["configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HypZ2prop({1,2,3,4,5})")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), given the list shape its syntax names.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**It pairs with [ConfZ2prop](ConfZ2prop.md)** (HP help), which was sent four
separate numbers in its own published shape and was refused as well. Two
shapes, one answer, which is what makes the finding about the group.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ConfZ2prop](ConfZ2prop.md) · [HypZ1prop](HypZ1prop.md) · [SUM](SUM.md)
