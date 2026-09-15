# COSH

The hyperbolic cosine.

| | |
|---|---|
| Syntax | `COSH(value)` |
| Group | hyperbolic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `COSH(1)` | `1.54308063482` | [emulator](../results.tsv) |

## Behaviour

`COSH(1)` answers 1.54308063482 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It is never below 1**, unlike the circular cosine which runs between -1 and
1 (unverified: only this one point was measured, and the claim is what the
function is rather than what these rows show). That is the difference that
catches a program written for one and handed the other.

Squaring this and subtracting [SINH](SINH.md) squared gives 1 (emulator, and
the arithmetic between the two rows), which is the identity the pair is
defined by and a cheap check on both.

[ACOSH](ACOSH.md) goes back the other way, and takes only arguments of 1 or
more (emulator); `ACOSH(2)` was the value chosen for that reason.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SINH](SINH.md) · [TANH](TANH.md) · [ACOSH](ACOSH.md)
