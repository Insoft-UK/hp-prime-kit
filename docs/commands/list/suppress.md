# suppress

Removes the element at a position from a list.

| | |
|---|---|
| Syntax | `suppress(List, Integer)` |
| Group | list |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `suppress({1,2,3},2)` | `{1,3}` | [emulator](../results.tsv) |

## Behaviour

`suppress({1,2,3},2)` answers `{1,3}` (emulator): the second element is gone
and the rest close up.

**HP writes this name in lower case and the inventory keeps it that way**
(HP help). There is a separate `SUPPRESS` on HP's list, filed under a
different group, so the two are not the same name written carelessly. This
kit's linter compares names without regard to case and cannot tell them
apart, which it already documents as a limitation.

The position counts from 1 (emulator),
[ppl.one-based](../../topics/ppl.md#ppl.one-based), so 2 is the middle
element of three and not the last.

It answers a new list rather than changing the one given (emulator), which is
the same shape [INSERT](INSERT.md) has.

What it does with a position past the end was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[INSERT](INSERT.md) · [POS](POS.md) · [REVERSE](REVERSE.md)
