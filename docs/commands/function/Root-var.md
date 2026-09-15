# Root

The Function app's stored root, which its own command does not write.

| | |
|---|---|
| Syntax | `Root` → real |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Root")` | `0` | [emulator](../results.tsv) |
| `EXPR("  Root")` | `0` | [emulator](../results.tsv) |
| `EXPR(" Root")` | *error* | [emulator](../results.tsv) |

## Behaviour

**[ROOT](ROOT.md) answered 2 and this still read 0** (emulator). The two calls
were consecutive in one batch: `ROOT(F1,1)` returned 2 for `F1` holding
`X^2-4`, and the very next call read this variable and got 0. So a Function
app command called from Home does **not** leave its answer here.

**That kills the pattern the Triangle Solver had suggested** (emulator).
There, [DoSolve](../triangle-solver/DoSolve.md) wrote its answers into
[AngleA](../triangle-solver/AngleA.md) and its neighbours, and reading the
variables afterwards was a second way to collect the result. This app does
not work that way, and an entry that assumed the shape generalised would have
been wrong. A program wanting a root has to take the return value.

**What does write it is untested** (unverified). The likely answer is the
app's own plot view, where the Fcn menu computes a root and displays it;
whether that fills this variable is a keypress probe, not a batch one.

**The first two rows are the same read before and after the command**
(emulator), which is why both are kept: one value would have been a reading,
the pair is evidence that nothing moved.

**The refusal is what proved the app rule for variables** (emulator). It was
measured with the Triangle Solver active, where the other two rows were taken
with the Function app active -- which a reset calculator has already,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active).
[AngleA](../triangle-solver/AngleA.md) carries that account.

**Its file carries a suffix its title does not** (HP help). This name and
[ROOT](ROOT.md) differ only in case, which no filesystem this documentation
runs on can tell apart, so the file is `Root-var.md` and the entry is still
`Root`. Three of its four neighbours do the same.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ROOT](ROOT.md) · [Slope](Slope-var.md) · [SignedArea](SignedArea.md) ·
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active)
