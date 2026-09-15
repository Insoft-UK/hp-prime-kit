# MOUSE

What the touch screen is reporting right now.

| | |
|---|---|
| Syntax | `MOUSE` → list of lists |
| Group | io |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MOUSE` | `{{},{}}` | [emulator](../results.tsv) |

## Behaviour

**With nothing touching the screen it answers two empty lists**, not an empty
list and not −1 (emulator). So a program checks `SIZE(zm(1)) == 0` rather
than comparing the whole thing, which is what the measured wrapper in
[interface.mouse-lists](../../topics/interface.md#interface.mouse-lists)
does.

With a finger down each inner list is `{x1,y1,x0,y0,type}` (G2). Two of them
come back because the screen reports two touch points; what the second holds
during a two-finger gesture has not been measured here (unverified).

From Python it has to be flattened before it crosses the bridge, because a
list that is not all numbers closes the app without a word (G2),
[micropython.list-with-string-closes-the-app](../../topics/micropython.md#micropython.list-with-string-closes-the-app).

A reading is not an event: it says what is happening now, and telling a fresh
tap from a finger that has been down for half a second is left to you
(unverified),
[interface.touch-readings](../../topics/interface.md#interface.touch-readings).

The interpreter records it rather than reading a screen, so `hpprime run`
cannot check what a program does with a real touch (unverified).

## Related

[GETKEY](GETKEY.md) · [ISKEYDOWN](ISKEYDOWN.md) ·
[interface.dialog-touch-twice](../../topics/interface.md#interface.dialog-touch-twice)
