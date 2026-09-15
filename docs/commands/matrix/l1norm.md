# l1norm

The sum of the absolute values of a vector's elements.

| | |
|---|---|
| Syntax | `l1norm(Vector)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `l1norm([1,2,3])` | `6` | [emulator](../results.tsv) |

## Behaviour

`l1norm([1,2,3])` answers 6 (emulator): one plus two plus three, with no
squaring and no root.

**Its sibling `l2norm` does not answer a number at all.** For the same vector
it answers a square root left in exact form, of `TYPE` 8, while this one
answers a plain `TYPE` 0 number (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers). Two commands one
letter apart, and a program cannot assume from one what it will get from the
other.

[maxnorm](maxnorm.md) is the third of the family and answers 3 for this
vector, also a plain number (emulator).

Whether the absolute value is taken before summing was not settled here,
because every element is positive (unverified). The probe is
`l1norm([1,-2,3])`, which answers 6 if it is and 2 if it is not.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[maxnorm](maxnorm.md) · [COLNORM](COLNORM.md) · [DOT](DOT.md)
