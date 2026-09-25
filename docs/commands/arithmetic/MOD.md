# MOD

The remainder after dividing.

| | |
|---|---|
| Syntax | `value1 MOD value2` |
| Group | arithmetic |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `9 MOD 4` | `1` | [emulator](../results.tsv) |
| `EXPR("9 MOD 4 + 100")` | `101` | [emulator](../results.tsv) |
| `EXPR("100 + 9 MOD 4")` | `101` | [emulator](../results.tsv) |
| `EXPR("2 * 7 MOD 4")` | `2` | [emulator](../results.tsv) |
| `EXPR("9 MOD 4 * 2")` | `2` | [emulator](../results.tsv) |
| `EXPR("2^3 MOD 5")` | `3` | [emulator](../results.tsv) |
| `EXPR("9 MOD 4 == 1")` | `1` | [emulator](../results.tsv) |
| `EXPR("-9 MOD 4")` | `3` | [emulator](../results.tsv) |
| `EXPR("(-9) MOD 4")` | `3` | [emulator](../results.tsv) |
| `EXPR("8 / 2 MOD 3")` | `1` | [emulator](../results.tsv) |
| `EXPR("9 MOD 4 / 2")` | `0.5` | [emulator](../results.tsv) |
| `EXPR("9 MOD (-4)")` | `−3` | [emulator](../results.tsv) |

## Behaviour

**It is an operator written between its arguments, not a function.**
`9 MOD 4` answers 1 (emulator), while `MOD(9,4)` is refused by the compiler:
a batch carrying it was rejected at that line and never ran (emulator). So
the parentheses form does not merely fail at run time, it fails to compile.

That is why HP's list gives this name no syntax string (HP help), where it
gives one to almost every other name: there is no call shape to write down.

A model writing PPL from habit reaches for `MOD(a,b)` because that is the
spelling in most languages, and the program will not compile (emulator). It
is worth knowing before the first Check rather than after.

**It binds like `*` and `/`, before `+`** (emulator). `9 MOD 4 + 100`
and `100 + 9 MOD 4` both answer 101. Beside `*` and `/` it goes left to
right: `2 * 7 MOD 4` is 2, fourteen's remainder, `9 MOD 4 * 2` is 2 as well,
`8 / 2 MOD 3` is 1 and `9 MOD 4 / 2` is 0.5, where the other grouping would
give 6, 1, 4 and 1. A power binds tighter, `2^3 MOD 5` being 3, and a
comparison looser, so `n MOD 2 == 0` tests evenness.

**A minus sign in front belongs to the number** (emulator): `-9 MOD 4` and
`(-9) MOD 4` both answer 3, where `-(9 MOD 4)` would be `−1`.

**The remainder takes the sign of the divisor** (emulator). `9 MOD (-4)`
answers `−3`, the remainder of a division rounded down, and `(-9) MOD 4`
answers 3. HP's help calls it the remainder of the Euclidean division
(HP help), which is never negative and would give 1 for the first: the
calculator does not do what its help says for a negative divisor.

**The interpreter on the PC follows these answers** (unverified: that is the
interpreter, not a calculator). `hpprime run` answers `9 MOD 4` with 1 and
the rows above as the emulator did, and refuses `MOD(9,4)` with the
calculator's reason. Until 2026-09-24 it answered `MOD(9,4)`, read
`9 MOD 4 + 100` as 9 with no error, and gave 1 for `9 MOD (-4)`.

## Related

[IP](../numbers/IP.md) · [FLOOR](../numbers/FLOOR.md) ·
[ppl.equality-operators](../../topics/ppl.md#ppl.equality-operators)
