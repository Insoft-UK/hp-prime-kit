# l2norm

The Euclidean length of a vector.

| | |
|---|---|
| Syntax | `l2norm(Vector)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `l2norm([1,2,3])` | `√14` | [emulator](../results.tsv) |

## Behaviour

**It answers an exact value, not a number.** For `[1,2,3]` the length is
the square root of 14, and that is what comes back: the radical sign U+221A
and the 14, held as `TYPE` 8 (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers).

**Its two siblings do not.** [l1norm](l1norm.md) answers 6 and
[maxnorm](maxnorm.md) answers 3 for the same vector, both plain numbers of
`TYPE` 0 (emulator). Three commands in one family, and only this one hands
back something a program cannot print as digits without converting it first.

`TYPE` 8 is the type `CAS` answers with, and this reached it without any `CAS`
call around it (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

Whether an argument with decimals in it forces a decimal answer was not run
(unverified). That is the probe worth having, because it decides whether a
program can rely on getting digits.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[l1norm](l1norm.md) · [maxnorm](maxnorm.md) · [DOT](DOT.md)
