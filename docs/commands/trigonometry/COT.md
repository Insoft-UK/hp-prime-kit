# COT

The cotangent: one over the tangent.

| | |
|---|---|
| Syntax | `COT(value)` |
| Group | trigonometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `COT(1)` | `0.642092615934` | [emulator](../results.tsv) |

## Behaviour

`COT(1)` answers 0.642092615934 (emulator): one over the tangent of one
radian.

The argument is an angle and the answer depends on the mode, recorded once in
[ACOT](ACOT.md) (emulator).

**Unlike its two neighbours it can be any size.** [SEC](SEC.md) and
[CSC](CSC.md) never answer between -1 and 1, which is why their inverses
refuse fractions; a cotangent has no such gap, and [ACOT](ACOT.md) accordingly
took 1 as its argument where the other two needed 2 (emulator).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

What it answers where the tangent is zero, and the cotangent infinite, was not
run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ACOT](ACOT.md) · [SEC](SEC.md) · [CSC](CSC.md)
