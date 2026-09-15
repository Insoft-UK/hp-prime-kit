# MKSA

Rewrites a value in the base SI units.

| | |
|---|---|
| Syntax | `MKSA(Value_Unit)` |
| Group | units |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MKSA(2_m)` | `2_m` | [emulator](../results.tsv) |

## Behaviour

`MKSA(2_m)` answers `2_m` (emulator), unchanged.

**That is the example's weakness and it is worth saying so.** A metre is
already a base unit, so there was nothing to rewrite, and this row shows the
shape of the answer rather than the work. The probe that would show the work
is a value in feet or in a compound unit, and it was not run (unverified).

The answer carries its unit and is type 9 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The name is the initials of metre, kilogram, second and ampere, which are the
base units it reduces to (HP help).

[USIMPLIFY](USIMPLIFY.md) answered the same unchanged value for the same
argument, and it has the same weakness for the same reason (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[USIMPLIFY](USIMPLIFY.md) · [CONVERT](CONVERT.md) · [UPART](UPART.md)
