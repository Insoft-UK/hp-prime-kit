# COLOR

Answers its own name back, unevaluated.

| | |
|---|---|
| Syntax | not published |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("COLOR")` | `COLOR` | [emulator](../results.tsv) |

## Behaviour

**It answers the text `COLOR`, which is its own name** (emulator). The type
is 8, the symbolic code,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). That is what a name the
CAS cannot resolve does: it hands the name back as an expression rather than
refusing it.

**So this row does not say the name is a function** (emulator). It separates
it from [ALPHA](ALPHA.md), [EEX](EEX.md) and [ICON](ICON.md), which are
errors outright, but answering yourself is what an unknown symbol does as
well as what a constant would do, and those two readings are not told apart
by anything measured here.

HP's list carries the name with no syntax string (HP help), so there is no
call shape to try against it.

The probe that would settle it is the name with an argument (unverified).
If it is a command that sets a colour, a call with one should answer
something other than itself.

The interpreter does not know the name at all (unverified), so `hpprime run`
cannot check a program that uses it.

## Related

[ALPHA](ALPHA.md) · [EEX](EEX.md) · [ICON](ICON.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
