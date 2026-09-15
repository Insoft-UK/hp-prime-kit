# PRINT

Writes a line to the program's own output screen.

| | |
|---|---|
| Syntax | `PRINT(expr)` |
| Group | io |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `PRINT("hi")` | *no value* | HP help |

## Behaviour

There is nothing to record: what it produces is a line on a screen, not a
value (HP help). Called with no argument it clears that screen, which HP
documents and nobody here has run (unverified).

It is the one output an app's `Info` hook accepts (G2),
[apps.hooks](../../topics/apps.md#apps.hooks), which is the only place this
kit has needed it.

`hpprime run` records the call and answers a neutral value, so a program that
prints still runs end to end on the PC, and `machine.io` holds what it would
have written (unverified: that is this kit's interpreter, not the calculator)
([interface.md](../../topics/interface.md#what-the-design-of-a-screen-comes-down-to)).

## Related

[MSGBOX](MSGBOX.md) · [TEXTOUT_P](../drawing/TEXTOUT_P.md) ·
[apps.hooks](../../topics/apps.md#apps.hooks)
