# MID

Part of a string: from a start position, a given number of characters or up
to the end.

| | |
|---|---|
| Syntax | `MID(str, start, length)` → string |
| Syntax | `MID(str, start)` → string |
| Group | strings |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MID("abcdef", 2, 3)` | `"bcd"` | G2 |
| `MID("abcdef", 4, 99)` | `"def"` | G2 |
| `MID("abcdef", 2)` | `"bcdef"` | G2 |
| `MID("abcdef", 2, 0)` | `""` | G2 |
| `MID("abcdef", 7, 2)` | `""` | G2 |
| `MID("abcdef", 0, 2)` | *error* | G2 |
| `MID("MOMOGUMBO", 3, 5)` | `"MOGUM"` | [emulator](../results.tsv) |
| `MID("PUDGE", 4)` | `"GE"` | [emulator](../results.tsv) |

## Behaviour

The third argument is a length, not an end position, and a length that runs
past the end stops at the end (G2). With two arguments it runs to the end
(G2; HP help agrees).

A length of 0 gives `""`, the opposite of what `LEFT` and `RIGHT` do with a
count of 0 (G2). A start past the end gives `""` as well, and a start below 1
is an error (G2).

**Evidence.** The G2 cases come from two probe programs run on a G2 with
firmware 2.4.15515.

## Related

[LEFT](LEFT.md) · [RIGHT](RIGHT.md)
