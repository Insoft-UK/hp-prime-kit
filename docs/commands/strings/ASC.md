# ASC

The character codes of a string, as a list.

| | |
|---|---|
| Syntax | `ASC(String)` → list |
| Group | strings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ASC("abc")` | `{97,98,99}` | [emulator](../results.tsv) |
| `ASC("A")` | `{65}` | [emulator](../results.tsv) |

## Behaviour

One code per character, always as a list, even for a string of one character
(emulator). The codes are the ones you would expect of ASCII for the letters
measured; what a character outside ASCII answers has not been measured
(unverified).

It is the other direction from [CHAR](CHAR.md), which turns codes back into
text. The pair is how a program takes a string apart and puts it together
again, and it is how `hpprime examples` carries any answer back from the
calculator: the harness sends `ASC(STRING(value))` and rebuilds the text on
the PC (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CHAR](CHAR.md) · [STRING](STRING.md) · [DIM](DIM.md)
