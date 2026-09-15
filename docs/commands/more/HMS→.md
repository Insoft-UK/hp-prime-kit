# HMS→

Turns hours, minutes and seconds into a plain decimal number.

| | |
|---|---|
| Syntax | `HMS→(value)` → number |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `HMS→(1.3)` | `1.3` | [emulator](../results.tsv) |

## Behaviour

**It answered its argument unchanged** (emulator). Read as hours, minutes and
seconds, `1.3` is one hour and thirty minutes, which is `1.5` as a decimal;
`1.3` came back instead, so this call did not convert anything.

That is a measurement of the call, not of the command: the reading of the
syntax behind it may be wrong, in the same way one argument was wrong for
[C→PX](../drawing/C→PX.md) (unverified). Its twin does convert --
[→HMS](→HMS.md) turns `1.5` into `1°30′00″` (emulator) -- so the pair is not
symmetric in what it accepts.

The probe that would settle it is the round trip `HMS→(→HMS(1.5))`, which
feeds this command the value its twin produces rather than a number typed to
look like one, and it has not been run (unverified).

The name carries an arrow, U+2192, and the arrow is part of the name rather
than an operator (emulator: the call ran with it). Typing `HMS->` is a
different name and will not be found.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[→HMS](→HMS.md) · [ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
