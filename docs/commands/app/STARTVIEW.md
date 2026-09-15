# STARTVIEW

Opens one of the current app's views.

| | |
|---|---|
| Syntax | `STARTVIEW(ViewNumber[, Redraw])` |
| Group | app |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `STARTVIEW(1)` | *no value* | HP help |

## Behaviour

There is nothing to record: it changes what is on the screen and leaves the
program's own flow (HP help).

The view numbers matter more than they look. The byte that decides which view
an app opens in is measured: `01` is the app's own view and `03` is the
Numeric view, which in a Python app is the console -- and an app that opens
in the console instead of its screen is the most baffling failure a Python
app has (G2),
[apps.startup-view-byte](../../topics/apps.md#apps.startup-view-byte).

Whether the numbers this command takes are the same ones that byte holds has
**not** been measured (unverified), and it is a one-call probe worth running
before trusting either.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[STARTAPP](STARTAPP.md) ·
[apps.startup-view-byte](../../topics/apps.md#apps.startup-view-byte)
