# ALPHA

On HP's list of names, and refused as a call.

| | |
|---|---|
| Syntax | not published |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ALPHA")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Evaluating the bare name is an error** (emulator). It was sent inside
`EXPR`, so the refusal is the calculator's answer to the name rather than a
compiler complaint about the program around it.

HP's list carries the name with no syntax string (HP help), which is the same
silence `NEG` and `INVERSE` have, and those two are refused as well. Three
other names in this group share it: [COLOR](COLOR.md), [EEX](EEX.md) and
[ICON](ICON.md).

What the name is for is not measured here (unverified). The Prime has an
alpha shift on its keyboard and a mode that goes with it, so the likeliest
reading is that this is a key or a mode rather than anything a program calls,
but nothing run here shows that.

This entry records a refusal, not a working form (unverified). A reader
looking for it in a program is looking in the wrong place until someone
measures what it does.

The interpreter does not know the name at all (unverified), so `hpprime run`
cannot check a program that uses it.

## Related

[COLOR](COLOR.md) · [EEX](EEX.md) · [ICON](ICON.md)
