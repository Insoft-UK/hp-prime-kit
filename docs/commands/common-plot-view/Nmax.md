# Nmax

The last index plotted of a plot, refused while the Function app is active.

| | |
|---|---|
| Syntax | `Nmax` → real |
| Group | common-plot-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Nmax")` | *error* | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Nmax"); IFERR EXPR("Nmax:=20"); r := EXPR("Nmax"); THEN r := "refused"; END; EXPR("Nmax:=" + STRING(o)); RETURN r;` | *error* | [emulator](../results.tsv) |

## Behaviour

**Read and set alike, it was refused with the Function app active**
(emulator), where the window's `Xmin` and `Ymax` answered. So, as with some
app functions and variables, it needs its own app active, [apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**Which app that is, the Sequence app, is read from its name** (unverified): HP's
list files it with the plot settings every app shares, and gives nothing
more. With that app active it was not tried, so no value and no form that
sets it is given here.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Xmin](Xmin.md) · [apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
