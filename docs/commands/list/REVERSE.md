# REVERSE

The list, back to front.

| | |
|---|---|
| Syntax | `REVERSE(list)` |
| Group | list |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `REVERSE({1,2,3})` | `{3,2,1}` | [emulator](../results.tsv) |

## Behaviour

`REVERSE({1,2,3})` answers `{3,2,1}` (emulator), which is all this command
does.

It answers a list rather than changing the one given (emulator), so the
result has to be stored somewhere if a program wants to keep it.

Paired with [SORT](SORT.md) this is how a descending order is built, since
`SORT` has no direction argument -- its second argument chooses which part to
sort by instead (emulator), [SORT](SORT.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SORT](SORT.md) · [INSERT](INSERT.md) · [CONCAT](CONCAT.md)
