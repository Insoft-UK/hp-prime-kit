# LN

The natural logarithm.

| | |
|---|---|
| Syntax | `LN(value)` |
| Group | catalog |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LN(1)` | `0` | [emulator](../results.tsv) |
| `LN({0.1,1})` | `{-2.30258509299,0}` | [emulator](../results.tsv) |

## Behaviour

`LN(1)` is 0 (HP help), and the interpreter agrees (unverified: that is this
kit's interpreter on the PC, not a calculator).

**This is the natural logarithm and [LOG](LOG.md) is the base-ten one**
(HP help), which is the opposite of the convention in several languages
where `log` is natural and `log10` is spelled out. Getting them the wrong
way round gives a number rather than an error.

A list is taken element by element (emulator). The interpreter does not
cover that form and stops on it, so that row is the calculator's word alone
(unverified).

[EXP](EXP.md) undoes it (HP help), and [LNP1](../arithmetic/LNP1.md) is the
variant that keeps precision for an argument close to zero, where adding
one first would lose it.

## Related

[EXP](EXP.md) · [LOG](LOG.md) · [LNP1](../arithmetic/LNP1.md)
