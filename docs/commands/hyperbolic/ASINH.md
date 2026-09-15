# ASINH

The inverse hyperbolic sine.

| | |
|---|---|
| Syntax | `ASINH(value)` |
| Group | hyperbolic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ASINH(1)` | `0.88137358702` | [emulator](../results.tsv) |

## Behaviour

`ASINH(1)` answers 0.88137358702 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It accepts any value**, unlike [ACOSH](ACOSH.md), which needs 1 or more,
and [ATANH](ATANH.md), which needs less than 1 in size (unverified: each was
measured only at one point inside its own range, so the limits are what the
functions are rather than what these rows show).

The round trip was not run (unverified): `SINH(0.88137358702)` should answer
1, and that would be the probe worth having, because it checks the pair
against each other rather than against arithmetic done here.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SINH](SINH.md) · [ACOSH](ACOSH.md) · [ATANH](ATANH.md)
