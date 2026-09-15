# ACOSH

The inverse hyperbolic cosine.

| | |
|---|---|
| Syntax | `ACOSH(value)` |
| Group | hyperbolic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ACOSH(2)` | `1.31695789692` | [emulator](../results.tsv) |

## Behaviour

`ACOSH(2)` answers 1.31695789692 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The argument is 2 rather than the 1 used elsewhere in this group, and that
is not arbitrary.** [COSH](COSH.md) never goes below 1, so its inverse has
nothing to answer for anything smaller, and a probe at 0.5 would have measured
an error instead of a value (unverified: the refusal was avoided rather than
measured).

What it answers below 1 is therefore still open, and it is the case worth
knowing: a program feeding it computed data cannot always promise the value is
large enough (unverified). The probe is `ACOSH(0.5)`.

[ASINH](ASINH.md) has no such limit, which makes the two easy to confuse in
code that handles both (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[COSH](COSH.md) · [ASINH](ASINH.md) · [ATANH](ATANH.md)
