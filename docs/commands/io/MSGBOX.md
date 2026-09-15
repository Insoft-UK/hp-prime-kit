# MSGBOX

Shows a message and waits for it to be dismissed.

| | |
|---|---|
| Syntax | `MSGBOX(expr, [OK_Cancel])` |
| Group | io |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MSGBOX("hi")` | *no value* | HP help |

## Behaviour

There is nothing to record: it waits for a person (HP help). With the second
argument it offers OK and Cancel rather than one button, and what it then
answers has not been measured here (unverified).

**Its OK button lands on the soft-key row**, in the F6 position, and a finger
still there when the dialog closes sends the same touch to the screen
underneath (G2),
[interface.dialog-touch-twice](../../topics/interface.md#interface.dialog-touch-twice).
That is measured, it is easy to mistake for a bug in your own menu, and the
fix is a debounce that counts the screen as touched when a dialog closes.

`hpprime run` records the call and answers a neutral value, so a program that
shows messages still runs end to end on the PC (unverified: that is this
kit's interpreter, not the calculator)
([interface.md](../../topics/interface.md#what-the-design-of-a-screen-comes-down-to)).

## Related

[INPUT](INPUT.md) · [CHOOSE](CHOOSE.md) ·
[interface.dialog-touch-twice](../../topics/interface.md#interface.dialog-touch-twice)
