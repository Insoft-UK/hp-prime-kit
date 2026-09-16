# zoomdecimal

Refused, with the whole zoom family.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("zoomdecimal")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), a plain error with no type.
[zoomin](zoomin.md) carries the account of the family and its probe.

**Its name suggests a view where one pixel is a round decimal step**
(HP help), which would tie it to the screen's own units. This documentation
measured those units and recorded them under
[interface.draw-units](../../topics/interface.md#interface.draw-units), but
nothing connects that measurement to this command (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[zoomin](zoomin.md) · [zoominteger](zoominteger.md) · [zoomout](zoomout.md)
