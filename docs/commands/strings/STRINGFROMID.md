# STRINGFROMID

The calculator's own message for a system message number.

| | |
|---|---|
| Syntax | `STRINGFROMID(Integer)` → string |
| Group | strings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `STRINGFROMID(1)` | `"La contraseña no es válida"` | [emulator](../results.tsv) |

## Behaviour

**The answer is in the calculator's own language.** The example above came
back in Spanish from a calculator set to Spanish (emulator). A program that
shows what it returns will show a different string on somebody else's
machine, which is the point of the command and also its trap: it is not a
stable string to compare against.

Which number means what has not been measured beyond that one, and HP's help
gives no table (unverified). What it answers for a number with no message has
not been measured either.

It is the call the reference prose points at for turning an error code into a
message: `IFERR` leaves the code in `Ans`, and this turns that into something
readable (unverified). Neither half of that has been measured here, and the
[IFERR](../branch/IFERR.md) entry says the same.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[IFERR](../branch/IFERR.md) · [STRING](STRING.md)
