# MAX

The largest of the values given, or the larger of each pair of two lists.

| | |
|---|---|
| Syntax | `MAX(value1,[value2],[..value16])` |
| Group | arithmetic |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MAX(210,25)` | `210` | [emulator](../results.tsv) |
| `MAX(8/3,11/4)` | `2.75` | [emulator](../results.tsv) |
| `MAX({1,8,2})` | `8` | [emulator](../results.tsv) |
| `MAX({1,8,2},{2,4,6})` | `{2,8,6}` | [emulator](../results.tsv) |

## Behaviour

**One list answers one number, two lists answer a list.** `MAX({1,8,2})` is
8, the largest element; `MAX({1,8,2},{2,4,6})` is `{2,8,6}`, the larger of
each pair taken by position (HP help). Both run through the interpreter and
agree with what HP states.

Up to sixteen values are accepted (HP help), which is the same limit
[MIN](MIN.md) carries.

The arguments may be arithmetic rather than plain numbers: `MAX(8/3,11/4)` is
2.75 (HP help), so the expression is worked out first and the comparison
happens on the result.

Every row above was run on the calculator and answered what HP's help
states (emulator).

## Related

[MIN](MIN.md) · [SIGN](SIGN.md) · [SORT](../list/SORT.md)
