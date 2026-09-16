# ICON

On HP's list of names, and refused as a call.

| | |
|---|---|
| Syntax | not published |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ICON")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Evaluating the bare name is an error** (emulator), the same answer
[ALPHA](ALPHA.md) and [EEX](EEX.md) give.

HP's list carries the name with no syntax string (HP help).

What the name is for is not measured here (unverified). An app can carry an
icon, and `hpprime build` gives apps one, so the likeliest reading is that the
name belongs to an app's source rather than to an expression a program
evaluates. That would explain a refusal at the point where it was tried,
which was a value asked for on Home.

Where an app built here gets its icon is documented under
[apps](../../topics/apps.md), and none of that goes through this name
(unverified).

This entry records a refusal, not a working form (unverified).

The interpreter does not know the name at all (unverified), so `hpprime run`
cannot check a program that uses it.

## Related

[ALPHA](ALPHA.md) · [EEX](EEX.md) · [COLOR](COLOR.md)
