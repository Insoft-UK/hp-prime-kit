# DelInstruction

Refused, and nothing published says what it is for.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("DelInstruction")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), a plain error with no type, exactly as
[Instruction](Instruction.md) was in the same batch.

**Being refused is the safe outcome here** (emulator). Of all the names in
this group this is the one whose name promises to delete something, and a
batch runs on a throwaway calculator without asking. A command that worked
would have changed state silently.

[Instruction](Instruction.md) carries what little can be said about the pair
and the reason a batch cannot settle it (unverified): neither name has a
published syntax and neither answered anything but an error.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Instruction](Instruction.md) · [Apps](Apps.md)
