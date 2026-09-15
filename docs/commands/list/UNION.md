# UNION

Every element that appears in either list, once each.

| | |
|---|---|
| Syntax | `UNION({list1}, {list2})` |
| Group | list |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `UNION({1,2},{2,3})` | `{1,2,3}` | [emulator](../results.tsv) |

## Behaviour

**Duplicates are dropped.** `UNION({1,2},{2,3})` answers `{1,2,3}`
(emulator), with one 2 and not two, so this is a set union rather than a
join. [CONCAT](CONCAT.md) is the one that keeps everything.

It completes the set of three with [INTERSECT](INTERSECT.md) and
[DIFFERENCE](DIFFERENCE.md), and it is the only one of the three that behaves
as its name suggests: `DIFFERENCE` is the symmetric difference rather than a
subtraction (emulator).

HP's list gives this name no syntax string (HP help), so the shape above is
what the measured call shows.

Whether more than two lists are accepted, as they are for
[INTERSECT](INTERSECT.md), was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[INTERSECT](INTERSECT.md) · [DIFFERENCE](DIFFERENCE.md) ·
[CONCAT](CONCAT.md)
