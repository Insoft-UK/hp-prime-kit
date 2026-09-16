# translation

Moves an object by a vector, and says so when given a point instead.

| | |
|---|---|
| Syntax | `translation(Vector, Object)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("translation(point(1,1),point(2,2))")` | `"El primer arg. de la traducción no debe ser un punto Error: valor de argumento incorrecto"` | [emulator](../results.tsv) |

## Behaviour

**The calculator explains the mistake in words** (emulator): the first
argument of a translation must not be a point. It is a string of type 2,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), carrying the complaint
and then an error message.

**A vector is not a point on this machine** (emulator), which is the finding.
Most of this group takes points wherever it can, and several commands accept
a segment where the syntax says Line, so a reader could reasonably expect a
point to serve as a displacement. It does not.

**This is the second command in this group to correct its own published
syntax** (emulator), after [perpendicular](perpendicular.md) replied that it
expects three points. Both times the machine was more precise than HP's list.

**The message is in the calculator's language** (emulator), so it is evidence
of rejection rather than a property of the command.

The probe is a real vector (unverified). Nothing in this group has built one
yet, and finding how is the next step for this entry.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[homothety](homothety.md) · [perpendicular](perpendicular.md) ·
[reflection](reflection.md)
