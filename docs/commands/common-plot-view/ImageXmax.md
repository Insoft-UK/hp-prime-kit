# ImageXmax

Where the picture behind the plot ends across, 30 on a reset calculator.

| | |
|---|---|
| Syntax | `ImageXmax` → real |
| Syntax | `ImageXmax:=value` |
| Group | common-plot-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ImageXmax")` | `30` | [emulator](../results.tsv) |
| `LOCAL o; o := EXPR("ImageXmax"); EXPR("ImageXmax:=" + STRING(o)); RETURN EXPR("ImageXmax");` | `30` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name, the
group, and nothing more.

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can assign it** (emulator): given its own value back, it was
accepted and read back the same. Another value was not tried.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ImageName](ImageName.md) · [ImageDisplay](ImageDisplay.md) · [ImageOpacity](ImageOpacity.md)
