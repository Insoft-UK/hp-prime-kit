# →HMS

Turns a decimal number into hours, minutes and seconds.

| | |
|---|---|
| Syntax | `→HMS(value)` → number |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `→HMS(1.5)` | `1°30′00″` | [emulator](../results.tsv) |

## Behaviour

`1.5` becomes one hour, thirty minutes and no seconds (emulator), which is
the conversion the name promises.

**What comes back is a number, not text.** Its `TYPE` is 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), even though it shows as
`1°30′00″`: the degree sign U+00B0, the prime U+2032 and the double prime
U+2033 are how the calculator *displays* the value, not characters in a
string. A program can go on calculating with it, and a program that expects
text from it will be wrong.

Its twin did not convert the other way: [HMS→](HMS→.md) answered `1.3`
unchanged (emulator), and the round trip that would explain the difference has
not been run (unverified).

The name carries an arrow, U+2192, and the arrow is part of the name rather
than an operator (emulator: the call ran with it). This is also where a
linter that splits names on the arrow goes wrong, which is why the rules in
this kit read the whole name.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[HMS→](HMS→.md) · [ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
