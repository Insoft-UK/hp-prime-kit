# EDITLIST

Opens the list editor on a list.

| | |
|---|---|
| Syntax | `EDITLIST(listvar or list, [title], [read only])` |
| Group | io |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EDITLIST(L1)` | *no value* | HP help |

## Behaviour

There is nothing to record: it hands the screen to the calculator's own list
editor and waits (HP help). A batch cannot run it, and what it answers when
the editor closes has not been measured (unverified).

It is the list counterpart of [EDITMAT](../matrix/EDITMAT.md), and the same
reasoning applies (unverified): the editor is for a person, while a program
that has to change a list does it with the list commands and draws its own
screen if it wants one.

The third argument makes it read only (HP help), which is the interesting one
for showing data without letting anybody edit it, and it has not been run
here (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EDITMAT](../matrix/EDITMAT.md) · [CHOOSE](CHOOSE.md) · [INPUT](INPUT.md)
