# ImageOpacity

How opaque the picture behind the active app's plot is, 75 on a reset calculator.

| | |
|---|---|
| Syntax | `ImageOpacity` → real |
| Syntax | `ImageOpacity:=value` |
| Group | common-plot-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ImageOpacity")` | `75` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("ImageOpacity"); IFERR EXPR("ImageOpacity:=50"); r := EXPR("ImageOpacity"); THEN r := "refused"; END; EXPR("ImageOpacity:=" + STRING(o)); RETURN r;` | `50` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can set it** (emulator): set to 50, it read back 50. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

That 75 is a percentage is read from the value (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ImageName](ImageName.md) · [ImageDisplay](ImageDisplay.md)
