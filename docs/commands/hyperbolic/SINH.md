# SINH

The hyperbolic sine.

| | |
|---|---|
| Syntax | `SINH(value)` |
| Group | hyperbolic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SINH(1)` | `1.17520119364` | [emulator](../results.tsv) |

## Behaviour

`SINH(1)` answers 1.17520119364 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The whole group answers decimals, where the special functions beside it
answer exact forms.** `erf(1)` comes back as `erf(1)` unevaluated and
`Beta(2,3)` as the fraction `1/12`, both of type 8 (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers). These six compute.

**Three of the rows check each other.** Dividing this answer by
[COSH](COSH.md)'s gives [TANH](TANH.md)'s to every digit brought back, and
squaring the two and subtracting gives 1 (emulator, and the arithmetic
between those rows). A program can use that identity to test its own
handling without trusting any single command.

The angle mode does not apply here, because a hyperbolic argument is not an
angle (unverified: `HAngle` was read as 0 beside these rows but nothing was
run in a second mode to show these answers do not move).

[ASINH](ASINH.md) goes back the other way (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[COSH](COSH.md) · [TANH](TANH.md) · [ASINH](ASINH.md)
