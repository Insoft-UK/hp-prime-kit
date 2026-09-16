# Do2VStats

Computes the two-variable statistics, and its data set could not be filled.

| | |
|---|---|
| Syntax | `Do2VStats(Sn)` |
| Group | statistics-2var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("S1:=[[1,2],[2,4],[3,6]]")` | *error* | [emulator](../results.tsv) |
| `EXPR("Do2VStats(S1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The first row is why the second one cannot mean much** (emulator).
Assigning a matrix to `S1` is itself refused, and reading `S1` back afterwards
is refused too, so the app's first data set was never filled and this command
was asked about nothing.

**That was measured on purpose** (emulator). An earlier batch called this
command after an assignment without checking whether the assignment worked,
and drew a conclusion from the refusal. The same mistake in the `function`
group produced a wrong reading that had to be corrected, so the setup is now
a row of its own.

**`F1` and `S1` behave differently** (emulator). The function app's variable
accepted an assignment -- storing a number rather than a function, which is
its own problem -- while this one refuses assignment outright.

**So this group is still unresolved** (unverified), and honestly so: three of
its five names refuse on data sets that could not be filled,
[residue](residue.md) answers because it needs no data set, and nothing here
says whether the commands work.

The probe is a way to put data into `S1` at all (unverified), which is
pressing keys in the Statistics app rather than a batch.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Resid](Resid.md) · [SetIndep](SetIndep.md) · [residue](residue.md)
