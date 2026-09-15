# ConfZ2prop

A z confidence interval for two proportions, refused from Home.

| | |
|---|---|
| Syntax | `ConfZ2prop(SuccCount1, SuccCount2, SampSize1, SampSi` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ConfZ2prop(10,12,50,50)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), given four separate numbers: ten
successes of fifty and twelve of fifty.

**It was the one name in this group sent in its own published shape rather
than as a list** (emulator), precisely so that the group's refusal could not
be blamed on a wrong argument. It was refused like the rest, which is part of
what makes the finding about the group rather than about argument shapes.
[SUM](SUM.md) carries the account.

**HP's syntax row is truncated in the inventory** (HP help), ending part way
through the fourth argument's name, so the full list is not published in the
data this kit holds. Four were sent because four are visible.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ConfZ1prop](ConfZ1prop.md) · [HypZ2prop](HypZ2prop.md) · [SUM](SUM.md)
