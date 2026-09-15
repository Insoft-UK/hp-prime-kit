# NTHROOT

The nth root, written between the degree and the number.

| | |
|---|---|
| Syntax | `n NTHROOT value` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("3 NTHROOT 8")` | `2` | [emulator](../results.tsv) |
| `EXPR("NTHROOT(3,8)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It is an operator written between its arguments, not a function**
(emulator). `3 NTHROOT 8` answers 2, the cube root of 8, and `NTHROOT(3,8)`
with the same two numbers in the same order is refused.

The left operand is the degree and the right one is the number (emulator).
The answer settles which way round they go, since 2 is the cube root of 8
while the other reading would give the eighth root of 3.

That is why HP's list gives this name no syntax string (HP help), where it
gives one to almost every other name: there is no call shape to write down.
`MOD` sits in exactly the same position and was settled the same way.

**The interpreter answers 3 to the form the calculator answers 2 to**
(unverified). It does not know `NTHROOT` as an operator, so it evaluates the
left operand and drops the rest of the expression without raising, which is
the defect [MOD](../arithmetic/MOD.md) records. Here the contrast is sharper,
because the calculator's answer is known: a program checked on the PC gets a
plausible number that is simply not what the calculator will compute.

So `hpprime run` cannot check a program that uses this name, and it will not
say so (unverified). A model writing PPL from habit reaches for the
parentheses, which will not compile at all.

## Related

[MOD](../arithmetic/MOD.md) · [NEG](NEG.md) · [INVERSE](INVERSE.md)
