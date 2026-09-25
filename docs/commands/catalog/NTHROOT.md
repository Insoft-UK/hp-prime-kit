# NTHROOT

The nth root, written between the degree and the number.

| | |
|---|---|
| Syntax | `n NTHROOT value` |
| Group | catalog |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("3 NTHROOT 8")` | `2` | [emulator](../results.tsv) |
| `EXPR("NTHROOT(3,8)")` | *error* | [emulator](../results.tsv) |
| `EXPR("3 NTHROOT 8 + 19")` | `21` | [emulator](../results.tsv) |
| `EXPR("2 * 3 NTHROOT 8")` | `4` | [emulator](../results.tsv) |
| `EXPR("2 ^ 3 NTHROOT 8")` | `4` | [emulator](../results.tsv) |
| `EXPR("-3 NTHROOT 8")` | `−2` | [emulator](../results.tsv) |
| `EXPR("2 NTHROOT 3 NTHROOT 64")` | `11.0356646359` | [emulator](../results.tsv) |
| `EXPR("3 NTHROOT (-8)")` | `−2` | [emulator](../results.tsv) |
| `EXPR("2 NTHROOT (-4)")` | *error* | [emulator](../results.tsv) |

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

**It binds tighter than anything around it** (emulator): tighter than
`+` and `*` -- `3 NTHROOT 8 + 19` is 21 and `2 * 3 NTHROOT 8` is 4 -- and
tighter than `^` and a minus sign in front: `2 ^ 3 NTHROOT 8` is 4, two
squared, and `-3 NTHROOT 8` is `−2`, the minus applied to the root. So it
does not sit with `*` the way [MOD](../arithmetic/MOD.md) does. Two in a row
go left to right: `2 NTHROOT 3 NTHROOT 64` is 11.0356646359, which is 64 to
the power of one over the square root of 3.

**An odd root of a negative number is real** (emulator): `3 NTHROOT (-8)`
answers `−2`. An even one, `2 NTHROOT (-4)`, is refused on a calculator
with [HComplex](../home-settings/HComplex.md) at 0, as a reset one has it.
With it at 1 it answers `2*i`, and the odd root stays real (emulator).

**The interpreter on the PC follows these answers** (unverified: that is the
interpreter, not a calculator). It refuses the call form as the calculator
does, and refuses what was not measured -- a degree of 0 or below, or one
that is not a whole number under a negative -- rather than choose. Until 2026-09-24 it answered 3 to `3 NTHROOT 8`, dropping the rest of
the expression.

A model writing PPL from habit reaches for the parentheses, which will not
compile at all (emulator).

## Related

[MOD](../arithmetic/MOD.md) · [NEG](NEG.md) · [INVERSE](INVERSE.md)
