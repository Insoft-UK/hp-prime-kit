# ΔLIST

The differences between neighbouring elements of a list.

| | |
|---|---|
| Syntax | `ΔLIST(list)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ΔLIST({1,4,9})` | `{3,5}` | [emulator](../results.tsv) |

## Behaviour

`ΔLIST({1,4,9})` answers `{3,5}` (emulator): four minus one, then nine minus
four.

**The answer is one element shorter than the argument**, which is what a
program indexing it in step with the original has to allow for (emulator).

**The first character is U+0394, and it is part of the name.** Typing
`DELTALIST` finds nothing. It is one of three list commands HP names with a
Greek letter, and all three print identically on a Windows console although
they are different commands, which is why every probe for them goes through a
file rather than a command line (emulator: this one ran, sent that way).

The other two are [ΣLIST](ΣLIST.md), which adds, and `ΠLIST`, which
multiplies and which HP files under `list` rather than here (HP help).

What it answers for a list of one element, where there is no difference to
take, was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ΣLIST](ΣLIST.md) · [ΠLIST](../list/ΠLIST.md)
