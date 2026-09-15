# LEFT

The first n characters of a string.

| | |
|---|---|
| Syntax | `LEFT(str, n)` → string |
| Group | strings |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LEFT("abcdef", 3)` | `"abc"` | G2 |
| `LEFT("abcdef", 0)` | `"abcdef"` | G2 |
| `LEFT("abcdef", 99)` | `"abcdef"` | G2 |
| `LEFT("abcdef", -1)` | *error* | [emulator](../results.tsv) |
| `LEFT(42, 2)` | *error* | [emulator](../results.tsv) |
| `LEFT("MOMOGUMBO", 3)` | `"MOM"` | [emulator](../results.tsv) |

## Behaviour

A count of 0 gives back the whole string, not an empty one, and so does a
count past the end (G2). A count that computes to zero therefore hands over
everything, and nothing warns about it.

A negative count is not the same thing: it is an error (emulator). HP's help
says that any count of 0 or less returns the entire string (HP help), and the
calculator refuses `LEFT("abcdef", -1)`. Where the two disagree, this page
follows the calculator and leaves HP's wording on the record. `RIGHT` refuses
a negative count in the same way.

A first argument that is not a string is an error too (emulator).

`MID` with a length of 0 does the opposite and gives `""`, so the two are easy
to mix up (G2).

**Evidence.** The G2 cases come from two probe programs run on a G2 with
firmware 2.4.15515. The emulator cases are in
[results.tsv](../results.tsv), run on the Virtual Calculator 2.4, build
2025-09-15.

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| `LEFT(s, -1)` expecting the whole string, because HP's help says a count of 0 or less returns it | the calculator refuses the call | this repository's own interpreter, written with an AI model, answered `"abcdef"` until the Virtual Calculator refused it on 2026-09-12 ([results.tsv](../results.tsv)) |

## Related

[RIGHT](RIGHT.md) · [MID](MID.md)
