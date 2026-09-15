# CHAR

The string built from one character code or from a list of them.

| | |
|---|---|
| Syntax | `CHAR(List)` or `CHAR(Vector)` or `CHAR(Integer)` → string |
| Group | strings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CHAR(65)` | `"A"` | [emulator](../results.tsv) |
| `CHAR({72,80})` | `"HP"` | [emulator](../results.tsv) |

## Behaviour

A single number gives a string of one character, and a list gives one
character per element, joined (emulator). HP's help also allows a vector
(HP help); nothing here has run that form.

It is the other direction from [ASC](ASC.md). What a code outside the range
the calculator can show does, and whether it refuses or draws something else,
has not been measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ASC](ASC.md) · [STRING](STRING.md)
