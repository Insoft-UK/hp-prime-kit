# ΠLIST

The product of every element of a list.

| | |
|---|---|
| Syntax | `ΠLIST(list)` |
| Group | list |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ΠLIST({1,2,3,4})` | `24` | [emulator](../results.tsv) |

## Behaviour

`ΠLIST({1,2,3,4})` answers 24 (emulator): one times two times three times
four. The Greek capital pi is the mathematician's product sign, which is
where the name comes from.

**The first character is U+03A0 and it is part of the name.** Typing `PILIST`
or `PLIST` finds nothing. It is one of three list functions HP names with a
Greek letter, and they print identically on a Windows console although they
are three different commands, which is why every probe for them goes through
a file rather than a command line (emulator: this one ran, sent that way).

The other two are `ΣLIST`, U+03A3, and `ΔLIST`, U+0394, both of which HP
files under a different group and neither of which has an entry yet
(HP help).

What it answers for an empty list was not run (unverified); one is the
mathematical answer and zero is the one a careless implementation gives.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CONCAT](CONCAT.md) · [SIZE](SIZE.md) · [MAKELIST](MAKELIST.md)
