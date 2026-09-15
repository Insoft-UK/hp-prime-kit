# WAIT

Pauses for a number of seconds, or until a key is pressed.

| | |
|---|---|
| Syntax | `WAIT(n)` |
| Group | io |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `WAIT(1)` | *no value* | HP help |

## Behaviour

There is nothing to record: what it produces is a pause, and a batch that ran
it would only be slower (HP help). `hpprime run` answers 30 for this call,
which is the interpreter's own stand-in for a keypress and **not** evidence
about the calculator (unverified): the entry states no result rather than
that number.

**`WAIT(-1)` is contradicted by two measurements**, and that is the part
worth knowing before designing around it (unverified),
[interface.wait-minus-one](../../topics/interface.md#interface.wait-minus-one):
in one program it did not wait at all -- a results screen flashed past -- and
in two published apps it is the event loop, answering a number for a key, a
list for a touch, and −1 every 60 seconds. The likeliest explanation is a key
still pending in the buffer, and that is a hypothesis.

What does work, measured, is to drain and then wait with
[GETKEY](GETKEY.md) (G2),
[interface.drain-then-wait](../../topics/interface.md#interface.drain-then-wait).
`WAIT(-1)` would use less battery and deliver touches in the same place; if
you use it, check it yourself.

## Related

[GETKEY](GETKEY.md) · [FREEZE](../drawing/FREEZE.md) ·
[interface.wait-minus-one](../../topics/interface.md#interface.wait-minus-one)
