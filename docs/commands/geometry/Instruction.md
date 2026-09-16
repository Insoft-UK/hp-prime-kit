# Instruction

Refused, and nothing published says what it is for.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Instruction")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), a plain error with no type.

**It is one of three names in this group with no menu path at all** (HP help),
beside [DelInstruction](DelInstruction.md) and [Apps](Apps.md). The other two
of that three behaved differently from each other: `Apps` answered a list of
app names, `DelInstruction` refused like this one.

**Its name and its neighbour's suggest a pair** (HP help): something that
records an instruction and something that deletes one. The Geometry app keeps
a list of construction steps, which is the likeliest thing an instruction
would be, and nothing measured here supports or refutes that (unverified).

**A batch is the wrong place to find out** (emulator). If these names touch
the app's construction list, they need the app open with a construction in
it, which takes pressing keys rather than a batch.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DelInstruction](DelInstruction.md) · [Apps](Apps.md) · [zoomin](zoomin.md)
