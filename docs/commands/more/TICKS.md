# TICKS

Milliseconds since the calculator started.

| | |
|---|---|
| Syntax | `TICKS` → number |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TICKS` | `120274` | [emulator](../results.tsv) |

## Behaviour

**No parentheses in PPL**: it is written `zt := TICKS;`, like `GETKEY` (G2),
[ppl.getkey-no-parentheses](../../topics/ppl.md#ppl.getkey-no-parentheses).
From Python, across the bridge, a published library writes `eval('ticks')`
bare and this kit's examples write `ticks()`; which form that side needs has
not been measured (unverified),
[micropython.eval-parentheses](../../topics/micropython.md#micropython.eval-parentheses).

The number above is the one that batch happened to see, about two minutes
after that emulator started (emulator). It is only useful as a difference:
read it before and after, and subtract. What it does when the calculator has
been on for a long time, and whether it wraps, has not been measured
(unverified).

It is the whole reason MicroPython on the Prime can time anything at all,
since that has no `time` module (G2),
[micropython.modules](../../topics/micropython.md#micropython.modules).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TEVAL](TEVAL.md) · [ppl.speed-anchor](../../topics/ppl.md#ppl.speed-anchor)
