# ATANH

The inverse hyperbolic tangent.

| | |
|---|---|
| Syntax | `ATANH(value)` |
| Group | hyperbolic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ATANH(0.5)` | `0.549306144334` | [emulator](../results.tsv) |

## Behaviour

`ATANH(0.5)` answers 0.549306144334 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The argument is 0.5 because [TANH](TANH.md) only ever answers between -1
and 1**, so its inverse has nothing to answer outside that range, and a probe
at 1 or above would have measured an error rather than a value (unverified:
the refusal was avoided rather than measured).

What it does at exactly 1, where the answer is infinite, is the case worth
settling: the calculator has a way to write infinity, measured elsewhere in
this phase, so the interesting question is whether this returns it or refuses.
The probe is `ATANH(1)` (unverified).

[ASINH](ASINH.md) accepts anything and [ACOSH](ACOSH.md) needs 1 or more, so
all three inverses guard different ranges (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TANH](TANH.md) · [ASINH](ASINH.md) · [ACOSH](ACOSH.md)
