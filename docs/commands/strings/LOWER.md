# LOWER

The string in lower case.

| | |
|---|---|
| Syntax | `LOWER(string)` → string |
| Group | strings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOWER("ABC")` | `"abc"` | [emulator](../results.tsv) |

## Behaviour

Measured on the letters A to C (emulator). What it does with accented letters,
with digits and punctuation, and with a string that is already lower case, has
not been measured (unverified), and the same questions are open for
[UPPER](UPPER.md).

This matters more than it looks when a program compares what somebody typed:
the calculator's own names are compared without regard to case by
`hpprime lint`, and whether the calculator itself does has not been measured
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[UPPER](UPPER.md) · [INSTRING](INSTRING.md)
