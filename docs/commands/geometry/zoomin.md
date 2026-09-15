# zoomin

Refused, with the whole zoom family.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("zoomin")` | *error* | [emulator](../results.tsv) |

## Behaviour

**All seven zoom commands are refused** (emulator): this one,
[zoomout](zoomout.md), [zoomauto](zoomauto.md), [zoombox](zoombox.md),
[zoomdecimal](zoomdecimal.md), [zoomdundo](zoomdundo.md) and
[zoominteger](zoominteger.md). Seven names, seven plain errors, no type at
all. This entry carries the account and the others point at it.

**They change a view rather than answer a value** (HP help), which is the
likeliest reason. A batch evaluates a string from Home on a calculator reset
before the run, with no Geometry app open and no plot on screen, so there is
no view for them to change.

**That separates them cleanly from the rest of the group** (emulator). Every
family here that takes arguments answers something -- points, lines,
polygons, even error messages carried as data. The zoom family answers
nothing at all.

**The refusal is a plain error, not a message** (emulator), unlike
[locus](locus.md) or [translation](translation.md), which explain themselves
in text. Nothing here says what these commands would want.

The probe is keypresses rather than a batch (unverified): the same names
called from inside the Geometry app with a plot on screen.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[zoomout](zoomout.md) · [zoomauto](zoomauto.md) · [zoombox](zoombox.md) ·
[Apps](Apps.md)
