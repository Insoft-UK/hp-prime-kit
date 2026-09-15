# CSC

The cosecant: one over the sine.

| | |
|---|---|
| Syntax | `CSC(value)` |
| Group | trigonometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CSC(1)` | `1.18839510578` | [emulator](../results.tsv) |

## Behaviour

`CSC(1)` answers 1.18839510578 (emulator): one over the sine of one radian.

The argument is an angle and the answer depends on the mode, recorded once in
[ACOT](ACOT.md) (emulator).

**It is not the inverse sine.** A reader meeting `CSC` for the first time may
read the C as "arc", and the two are different functions: this is a
reciprocal, while [ACSC](ACSC.md) is the inverse. Both were measured and
answer different numbers (emulator).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

What it answers where the sine is zero, and the cosecant infinite, was not run
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ACSC](ACSC.md) · [SEC](SEC.md) · [COT](COT.md)
