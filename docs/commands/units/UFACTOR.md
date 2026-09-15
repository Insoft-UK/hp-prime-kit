# UFACTOR

Factors a unit out of a value.

| | |
|---|---|
| Syntax | `UFACTOR(Value_Unit1, 1_Unit2)` |
| Group | units |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `UFACTOR(2_m, 1_ft)` | `6.56167979003_ft` | [emulator](../results.tsv) |

## Behaviour

`UFACTOR(2_m, 1_ft)` answers 6.56167979003 feet (emulator).

**That is the same answer [CONVERT](CONVERT.md) gives for the same pair**, to
every digit (emulator). So these two rows do not tell the commands apart, and
this entry does not pretend otherwise: with a simple unit on both sides they
behave alike.

What distinguishes them was not measured (unverified). Factoring is the
operation that pulls a named unit out of a compound one and leaves the rest,
so a value like metres per second against `1_ft` is the probe that would show
the difference, and it has not been run.

The answer carries its unit and is type 9 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

Two commands that agree on every example measured are worth documenting as
exactly that, rather than describing each as though the difference were known
(emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CONVERT](CONVERT.md) · [USIMPLIFY](USIMPLIFY.md) · [MKSA](MKSA.md)
