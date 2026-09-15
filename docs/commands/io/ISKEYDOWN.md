# ISKEYDOWN

Whether a given key is being held down right now.

| | |
|---|---|
| Syntax | `ISKEYDOWN(key)` → 1 or 0 |
| Group | io |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ISKEYDOWN(30)` | `1` | [emulator](../results.tsv) |

## Behaviour

**The measured answer is a warning, not a demonstration.** `ISKEYDOWN(30)`
asks about `[Enter]`, code 30
([interface.key-codes](../../topics/interface.md#interface.key-codes)), and
it answered 1 in a batch where the program had just been started by pressing
`[Enter]` on Home. Nobody was holding the key down by then, so what 1 means
here is not settled: it may report a key still in the buffer rather than a
finger on the key (unverified).

That is exactly the shape of the trap
[interface.drain-then-wait](../../topics/interface.md#interface.drain-then-wait)
describes for `WAIT(-1)` (G2), and the fix is likely the same: drain what is
pending before believing what you are told (unverified).

Asking about a key that is certainly not pressed, in a program that has been
running for a while, is the probe that would settle it, and nobody has run it
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[GETKEY](GETKEY.md) ·
[interface.key-codes](../../topics/interface.md#interface.key-codes) ·
[interface.drain-then-wait](../../topics/interface.md#interface.drain-then-wait)
