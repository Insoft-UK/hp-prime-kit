# zoombox

Refused, with the whole zoom family.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("zoombox")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), a plain error with no type.
[zoomin](zoomin.md) carries the account of the family and its probe.

**Its name suggests it waits for a rectangle to be drawn** (HP help), which
would make it need a person at the keyboard as well as a view. A batch
supplies neither.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[zoomin](zoomin.md) · [zoomauto](zoomauto.md) · [zoomdundo](zoomdundo.md)
