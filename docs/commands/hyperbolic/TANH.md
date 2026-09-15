# TANH

The hyperbolic tangent.

| | |
|---|---|
| Syntax | `TANH(value)` |
| Group | hyperbolic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TANH(1)` | `0.761594155956` | [emulator](../results.tsv) |

## Behaviour

`TANH(1)` answers 0.761594155956 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It is [SINH](SINH.md) over [COSH](COSH.md), and the three rows agree**:
1.17520119364 divided by 1.54308063482 gives this number to every digit
brought back (emulator, and the arithmetic between them).

The answer always lies between -1 and 1, which is why this is the one of the
three a program reaches for when it needs a bounded value -- squashing a
number into a range without a conditional (unverified: one point does not
show the bound, and no row was run at a large argument).

[ATANH](ATANH.md) goes back the other way, and takes only arguments inside
that range (emulator); `ATANH(0.5)` was the value chosen for that reason.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SINH](SINH.md) · [COSH](COSH.md) · [ATANH](ATANH.md)
