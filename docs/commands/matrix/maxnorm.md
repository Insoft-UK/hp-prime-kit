# maxnorm

The largest absolute value among a vector's elements.

| | |
|---|---|
| Syntax | `maxnorm(Vector)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `maxnorm([1,2,3])` | `3` | [emulator](../results.tsv) |

## Behaviour

`maxnorm([1,2,3])` answers 3 (emulator): the largest element, and nothing is
summed.

It answers a plain number, `TYPE` 0, as [l1norm](l1norm.md) does and unlike
`l2norm`, which answers an exact square root of `TYPE` 8 for the same vector
(emulator), [ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers).

Whether it takes the absolute value first was not settled, because every
element here is positive (unverified). The probe is `maxnorm([1,-5,3])`,
which answers 5 if it does and 3 if it does not -- and that is the case where
the name would otherwise mislead.

This is the vector counterpart of what [ROWNORM](ROWNORM.md) and
[COLNORM](COLNORM.md) do for a matrix, which answer 7 and 6 for a matrix
measured in the same batch (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[l1norm](l1norm.md) · [ROWNORM](ROWNORM.md) · [COLNORM](COLNORM.md)
