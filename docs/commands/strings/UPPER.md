# UPPER

The string in upper case.

| | |
|---|---|
| Syntax | `UPPER(string)` → string |
| Group | strings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `UPPER("abc")` | `"ABC"` | [emulator](../results.tsv) |

## Behaviour

Measured on the letters a to c (emulator). Accented letters, digits and
punctuation have not been measured, and neither has a string that is already
upper case (unverified): the same gaps as [LOWER](LOWER.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LOWER](LOWER.md) · [INSTRING](INSTRING.md)
