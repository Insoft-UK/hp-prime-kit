# SeqPlot

A Sequence app setting, 0 on a reset calculator; assigning 1 raised nothing and left it at 0.

| | |
|---|---|
| Syntax | `Sequence.SeqPlot` → real |
| Group | sequence |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SeqPlot")` | *error* | [emulator](../results.tsv) |
| `EXPR("Sequence.SeqPlot")` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Sequence.SeqPlot"); IFERR EXPR("Sequence.SeqPlot:=1"); r := EXPR("Sequence.SeqPlot"); THEN r := "refused"; END; IFERR EXPR("Sequence.SeqPlot:=" + STRING(o)); THEN r := r; END; RETURN r;` | `0` | [emulator](../results.tsv) |

## Behaviour

**It is on HP's list from the release notes of firmware 14730** (HP help),
with its app and nothing more. What it holds is read from its name, the kind
of plot the Sequence app draws (unverified).

**A program reaches it with its app's name in front** (emulator):
`Sequence.SeqPlot` answered `0` with the Function app active, where `SeqPlot`
alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**Assigning it raised no error and changed nothing** (emulator): set to 1, it
read back 0. Whether 1 is out of range or the assignment is ignored was not
separated: no other value was tried (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[apps.qualified-names](../../topics/apps.md#apps.qualified-names)
