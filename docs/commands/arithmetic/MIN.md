# MIN

The smallest of the values given, or the smaller of each pair of two lists.

| | |
|---|---|
| Syntax | `MIN(value1,[value2],[..value16])` |
| Group | arithmetic |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MIN(210,25)` | `25` | [emulator](../results.tsv) |
| `MIN(8/3,11/4)` | `2.66666666667` | [emulator](../results.tsv) |
| `MIN({1,8,2})` | `1` | [emulator](../results.tsv) |
| `MIN({1,8,2},{2,4,6})` | `{1,4,2}` | [emulator](../results.tsv) |

## Behaviour

It mirrors [MAX](MAX.md) exactly: one list gives the smallest element, two
lists give the smaller of each pair by position (HP help).

**HP prints this one rounded and the calculator does not.** Eight thirds
is 2.666666..., HP's help shows `2.6667`, and the calculator answered
`2.66666666667` (emulator). The entry states what the calculator said, and
the checker compares numbers within a small tolerance so that the two
readings are not treated as a disagreement. It is worth knowing before
writing a test that expects HP's printed digits.

Up to sixteen values are accepted (HP help).

Every row above was run on the calculator (emulator); only the rounding
above differed from what HP prints.

## Related

[MAX](MAX.md) · [SIGN](SIGN.md)
