# single_inter

One intersection of two curves, which came back as an error message.

| | |
|---|---|
| Syntax | `single_inter(Curve1, Curve2, [Point])` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("single_inter(line(point(0,0),point(4,0)),line(point(2,-1),point(2,1)))")` | `"Error: entrada no válida"` | [emulator](../results.tsv) |

## Behaviour

**The answer is a string carrying an error message** (emulator), type 2,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), where the two lines
given cross at 2,0 and a working call would have answered that point.

**[inter](inter.md) failed the same way and carries the account** (emulator):
seven answers in this batch reported a failure as data rather than raising
it, so a program testing only for an error takes the message as a value. The
difference between the two names is that this one answers a single point
where `inter` answers a list of them.

**The lines were built by [line](line.md), which was itself refused**
(emulator), so what reached this command may never have been a line. That is
the probe for both names: build them with [segment](segment.md), which
answered.

The optional third argument chooses which intersection is wanted (HP help)
and was not reached.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[inter](inter.md) · [line](line.md) · [segment](segment.md)
