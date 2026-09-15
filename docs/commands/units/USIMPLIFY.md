# USIMPLIFY

Simplifies the units of a value.

| | |
|---|---|
| Syntax | `USIMPLIFY(Value_Unit)` |
| Group | units |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `USIMPLIFY(2_m)` | `2_m` | [emulator](../results.tsv) |

## Behaviour

`USIMPLIFY(2_m)` answers `2_m` (emulator), unchanged, because a single metre
has nothing to simplify.

**So this row measures that the call is accepted, not what it does.** The work
happens on a compound unit -- something that reduces to a named one -- and no
such probe was run (unverified). That is the gap worth filling next in this
group.

[MKSA](MKSA.md) answered the same unchanged value for the same argument
(emulator), so these two are in the same position: both measured, neither
demonstrated.

The answer carries its unit and is type 9 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[MKSA](MKSA.md) · [UFACTOR](UFACTOR.md) · [CONVERT](CONVERT.md)
