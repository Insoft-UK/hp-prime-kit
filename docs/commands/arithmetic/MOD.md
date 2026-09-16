# MOD

The remainder after dividing.

| | |
|---|---|
| Syntax | `value1 MOD value2` |
| Group | arithmetic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `9 MOD 4` | `1` | [emulator](../results.tsv) |

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

What it does with a negative left argument, where languages disagree about
the sign of the answer, was not run (unverified). The probe is `-9 MOD 4`.

**Neither spelling works on both machines.** The calculator compiles
`9 MOD 4` and refuses `MOD(9,4)` (emulator). The interpreter on the PC is the
other way round: it has `MOD` as a function and answers `MOD(9,4)` as 1,
while the infix form it does not know at all -- `9 MOD 4` comes back as 9,
and so does `9 MOD 4 + 100`, with the rest of the expression dropped and no
error raised (unverified: that is the interpreter on the PC, not a
calculator). So `hpprime run` cannot check a program that uses MOD the one
way the calculator accepts, and it will not say so.

## Related

[IP](../numbers/IP.md) · [FLOOR](../numbers/FLOOR.md) ·
[ppl.equality-operators](../../topics/ppl.md#ppl.equality-operators)
