# CONCAT

Joins values and lists into one list.

| | |
|---|---|
| Syntax | `CONCAT(value1, value2, [..value16])` |
| Group | list |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CONCAT(1,2,3,4)` | `{1,2,3,4}` | [emulator](../results.tsv) |
| `CONCAT({1,2,3},4)` | `{1,2,3,4}` | [emulator](../results.tsv) |
| `CONCAT({1,2},3,{{4,5},6,{7,8}})` | `{1,2,3,{4,5},6,{7,8}}` | [emulator](../results.tsv) |

## Behaviour

**Plain values and lists mix freely, and only the top level is opened.**
`CONCAT({1,2},3,{{4,5},6,{7,8}})` answers `{1,2,3,{4,5},6,{7,8}}` (HP help):
the outer lists are unwrapped and their elements joined, while `{4,5}` and
`{7,8}` stay whole because they were elements rather than arguments. That is
the difference a program gets wrong when it expects a flat result.

Numbers alone still answer a list: `CONCAT(1,2,3,4)` is `{1,2,3,4}` and not a
number (HP help), so this is also the way to build a list out of loose values.

**The interpreter does not cover any of these three forms** (unverified: that
is this kit's interpreter on the PC, not a calculator). `hpprime run` stops on
them rather than answering, so the checker records a note instead of running
them, and what is written above is HP's statement rather than something
verified on a machine.

Up to sixteen arguments are accepted (HP help).

## Related

[SIZE](SIZE.md) · [SORT](SORT.md) ·
[ppl.one-based](../../topics/ppl.md#ppl.one-based)
