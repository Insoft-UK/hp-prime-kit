# RIGHT

The last n characters of a string.

| | |
|---|---|
| Syntax | `RIGHT(str, n)` → string |
| Group | strings |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `RIGHT("abcdef", 3)` | `"def"` | G2 |
| `RIGHT("abcdef", 0)` | `"abcdef"` | G2 |
| `RIGHT("abcdef", 99)` | `"abcdef"` | G2 |
| `RIGHT("abcdef", -1)` | *error* | [emulator](../results.tsv) |
| `RIGHT("MOMOGUMBO", 5)` | `"GUMBO"` | [emulator](../results.tsv) |

## Behaviour

As with `LEFT`, a count of 0 gives back the whole string, not an empty one,
and so does a count past the end (G2). HP's help does not cover either edge,
so both rest on the measurement alone.

A negative count is an error (emulator). HP's help does not cover it here;
for `LEFT` it says a count of 0 or less returns the entire string, and the
calculator refuses a negative count for both.

**Evidence.** The G2 cases come from two probe programs run on a G2 with
firmware 2.4.15515. The negative count is in [results.tsv](../results.tsv),
run on the Virtual Calculator 2.4, build 2025-09-15.

## Related

[LEFT](LEFT.md) · [MID](MID.md)
