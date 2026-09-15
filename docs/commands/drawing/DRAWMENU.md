# DRAWMENU

Draws the row of six labels along the bottom of the screen.

| | |
|---|---|
| Syntax | `DRAWMENU(label1, ..., label6)` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DRAWMENU("a","b","c","d","e","f")` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1 (emulator) and paints the six labels in the bottom band of the
screen, y 213 to 239 (G2),
[interface.geometry](../../topics/interface.md#interface.geometry).

**The labels it draws are not keys.** Touching one reports nothing through
`GETKEY` (G2),
[interface.soft-labels-not-keys](../../topics/interface.md#interface.soft-labels-not-keys):
what published apps call "soft keys" are physical keys they chose, and touch
arrives through [MOUSE](../io/MOUSE.md) instead. So drawing the menu is half
the work; deciding what each position does, and reading it, is yours.

Six labels were passed and accepted. Whether fewer is allowed, and what an
empty string draws, has not been measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[interface.soft-labels-not-keys](../../topics/interface.md#interface.soft-labels-not-keys) ·
[MOUSE](../io/MOUSE.md) · [TEXTOUT_P](TEXTOUT_P.md)
