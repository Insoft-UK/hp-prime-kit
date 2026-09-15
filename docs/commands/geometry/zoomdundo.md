# zoomdundo

Refused, with the whole zoom family.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("zoomdundo")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), a plain error with no type.
[zoomin](zoomin.md) carries the account of the family and its probe.

**Its name suggests undoing the last zoom** (HP help), which would need a
previous zoom to undo. A batch performs none, so even a working command might
have nothing to do here -- and this row cannot tell that apart from a command
that does not work at all (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[zoomin](zoomin.md) · [zoombox](zoombox.md) · [zoomout](zoomout.md)
