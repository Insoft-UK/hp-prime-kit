# KEY

Declares a handler the calculator calls when a key is pressed.

| | |
|---|---|
| Syntax | `KEY name` |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `KEY name` | *no value* | HP help |

## Behaviour

A declaration rather than a call, so there is nothing to record (HP help).
HP's help gives the form above and no example, and what a real handler name
looks like on this firmware has not been measured here: one program declaring
one, installed and pressed, would settle it (unverified).

What is measured is the other way of reading keys, which is what the example
apps here use: a program polls `GETKEY`, and a code is a position rather than a
character (G2),
[interface.getkey-position](../../topics/interface.md#interface.getkey-position),
with the 51 codes in
[interface.key-codes](../../topics/interface.md#interface.key-codes).

An app's program has hooks of its own -- `START`, `Num`, `Info`, `RESET` (G2),
[apps.hooks](../../topics/apps.md#apps.hooks) -- and in an app built with no
base view they never fire (G2),
[apps.blank-app-hooks](../../topics/apps.md#apps.blank-app-hooks). There the
view keys arrive as ordinary key codes instead (G2),
[apps.blank-app-keys](../../topics/apps.md#apps.blank-app-keys). Whether `KEY`
is subject to the same trap has not been measured (unverified).

## Related

[interface.key-codes](../../topics/interface.md#interface.key-codes) ·
[apps.hooks](../../topics/apps.md#apps.hooks)
