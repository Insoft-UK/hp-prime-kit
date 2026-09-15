# CopyVar

Copies one variable into another.

| | |
|---|---|
| Syntax | `CopyVar(Var1, Var2)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CopyVar(L1,L2)")` | `{}` | [emulator](../results.tsv) |

## Behaviour

`CopyVar(L1,L2)` answers `{}` (emulator), an empty list of type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**That row measures that the call is accepted, not that it copies**
(emulator). The batch runs on a calculator reset before every run, so `L1`
was empty when this was called and an empty answer is what an empty source
gives either way. The copy itself is untested.

The probe is two calls in one program (unverified): fill `L1`, copy it, and
answer `L2`. Whichever way that comes out, it separates a command that copies
from one that merely accepts the names.

Which of the two arguments is the source is stated by HP's order, first to
second (HP help), and nothing measured here confirms it.

**It names its variables rather than taking their values** (HP help), which
is why the arguments are written bare. A program that passes `L1` to an
ordinary function passes what `L1` holds; this one is given the name.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EVALLIST](EVALLIST.md) ·
[ppl.global-namespace](../../topics/ppl.md#ppl.global-namespace) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
