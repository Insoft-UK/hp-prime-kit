# HypZ1prop

A z test for one proportion, refused from Home.

| | |
|---|---|
| Syntax | `HypZ1prop(input_list, ["configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HypZ1prop({1,2,3,4,5})")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), given the list shape its syntax names.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator);
[SUM](SUM.md) carries the account and the probes.

**It pairs with [ConfZ1prop](ConfZ1prop.md)** (HP help), the interval beside
the test, and both concern a proportion rather than a mean.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ConfZ1prop](ConfZ1prop.md) · [HypZ2prop](HypZ2prop.md) · [SUM](SUM.md)
