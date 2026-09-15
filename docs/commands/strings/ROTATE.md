# ROTATE

Moves the characters of a string around by n places.

| | |
|---|---|
| Syntax | `ROTATE(String, n)` → string |
| Group | strings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ROTATE("abcdef", 2)` | `"cdefab"` | [emulator](../results.tsv) |
| `ROTATE({1,2,3,4}, 1)` | *error* | [emulator](../results.tsv) |

## Behaviour

With a positive n the string moves left: the first n characters come off the
front and go on the end, so `ROTATE("abcdef", 2)` is `"cdefab"` (emulator).
What a negative n does, and what an n larger than the string does, has not
been measured (unverified).

A list is refused (emulator). HP files `ROTATE` under strings and its syntax
says `String`, so that refusal agrees with the help; it is worth knowing
because the same word rotates lists in other languages, and a model reaching
for it here gets an error rather than a rotated list.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LEFT](LEFT.md) · [RIGHT](RIGHT.md) · [MID](MID.md)
