# VIEW

Declares one of an app's own views, with the name it shows in the View menu.

| | |
|---|---|
| Syntax | `VIEW "Text" Function()` |
| Group | app |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `VIEW "Text" Function()` | *no value* | HP help |

## Behaviour

**It is a declaration, not a call** (HP help): it sits in an app's program
beside the function it names, the way [KEY](../function/KEY.md) does, and
there is nothing to record because nothing is answered.

The text is what the calculator shows in the `[View]` menu, and the function
is what it runs when that entry is chosen (HP help). Nothing here has
declared one and pressed it, so what happens when the function returns, and
whether the menu entry can be changed while the app runs, are unmeasured
(unverified).

**In an app built with no base view it is likely moot**, because the hooks
never fire there: `START()` holds the keyboard and `[View]` arrives as an
ordinary key code, 9, instead (G2),
[apps.blank-app-hooks](../../topics/apps.md#apps.blank-app-hooks) and
[apps.blank-app-keys](../../topics/apps.md#apps.blank-app-keys). Whether a
`VIEW` declaration behaves any differently in that kind of app has not been
measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[STARTVIEW](STARTVIEW.md) · [KEY](../function/KEY.md) ·
[apps.blank-app-hooks](../../topics/apps.md#apps.blank-app-hooks)
