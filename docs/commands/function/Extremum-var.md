# Extremum

The Function app's stored extremum, and a 0 that agrees by coincidence.

| | |
|---|---|
| Syntax | `Extremum` → real |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Extremum")` | `0` | [emulator](../results.tsv) |
| `EXPR("  Extremum")` | `0` | [emulator](../results.tsv) |

## Behaviour

**Both rows are 0, and [EXTREMUM](EXTREMUM.md) answered 0 between them**
(emulator). That makes this the one variable of the five where the command's
answer and the variable's value agree -- and it agrees by coincidence, since
`X^2-4` turns at x equal to 0 and the variable was already 0 before anything
ran. [Root](Root-var.md) is the entry that shows what is really happening:
the commands do not write these variables at all.

**A coincidence that looks like a result is worth naming** (emulator). Read
on its own, the second row would say "EXTREMUM stored its answer here". Read
beside the first, it says nothing of the kind. This is why the format asks
for the call as well as the result: one row without its pair would have
misled.

**Its file carries the `-var` suffix** (HP help), because this name and
[EXTREMUM](EXTREMUM.md) differ only in case. [Root](Root-var.md) carries the
rule.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EXTREMUM](EXTREMUM.md) · [Root](Root-var.md) · [Isect](Isect-var.md)
