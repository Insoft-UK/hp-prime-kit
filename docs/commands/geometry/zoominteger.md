# zoominteger

Refused, with the whole zoom family.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("zoominteger")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), a plain error with no type.
[zoomin](zoomin.md) carries the account of the family and its probe.

**Its name suggests a view where one pixel is a whole unit** (HP help),
making it the neighbour of [zoomdecimal](zoomdecimal.md); nothing measured
separates the two, since both refused identically.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[zoomin](zoomin.md) · [zoomdecimal](zoomdecimal.md) · [zoomauto](zoomauto.md)
