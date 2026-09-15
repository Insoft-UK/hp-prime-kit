# DIFFERENCE

The elements that are in one list or the other, but not in both.

| | |
|---|---|
| Syntax | `DIFFERENCE({list1}, ...{listN})` |
| Group | list |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIFFERENCE({1,2,3},{2,3,4})` | `{1,4}` | [emulator](../results.tsv) |

## Behaviour

**This is the symmetric difference, not a subtraction.**
`DIFFERENCE({1,2,3},{2,3,4})` answers `{1,4}` (emulator): the 1 from the left
list and the 4 from the right. A program expecting "the first list minus the
second" would want `{1}` and gets an extra element it never asked for.

That is the single most useful thing this entry records (emulator), because
the name reads like subtraction in every other library.

It answers a list, `TYPE` 6 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

HP's syntax shows more than two lists (HP help), and what it does with three
has not been run here (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[INTERSECT](INTERSECT.md) · [UNION](UNION.md) · [POS](POS.md)
