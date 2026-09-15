# DoSolve

Solves the triangle the app holds, once something has put one there.

| | |
|---|---|
| Syntax | `DoSolve()` |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("DoSolve")` | `{36.8698976458,53.1301023542,90}` | [emulator](../results.tsv) |
| `EXPR(" DoSolve( )")` | `{}` | [emulator](../results.tsv) |
| `EXPR("DoSolve( )")` | *error* | [emulator](../results.tsv) |
| `EXPR("DoSolve()")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It answers once the app has a triangle, and the program can put one there**
(emulator). The first row was taken after the same batch had run
`SideA:=3`, `SideB:=4` and `SideC:=5` with the Triangle Solver active; each
assignment answered its own number, and reading `SideA` back gave 3. So the
inputs are reachable from a program, and this command then solves them.

**The answer is the three angles, and they are in degrees** (emulator),
which is
[apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees)
again: `{36.8698976458,53.1301023542,90}` for the 3-4-5 triangle, a list of
type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). [SSS](SSS.md) answers
the same three numbers when handed the same three sides.

**It also writes its answers into the app's variables** (emulator). Before it
ran, `AngleA`, `AngleB` and `AngleC` each read −1. After it ran they read
36.8698976458, 53.1301023542 and 90. So the command is not only a function
returning a list; it leaves the app holding the solved triangle. A program
can take its results from the return value or from the variables, and both
were measured in one pass.

**The two refusals are the same command before the app had anything**
(emulator). They were taken when the app was open but empty, because the
harness resets the calculator before every run. The entry then said being
active was necessary and not sufficient, and named the probe that would
settle it -- put a triangle in first. That probe has now run and this is its
result.

**What the bracketed form does is not settled** (emulator). `DoSolve( )`
answered `{}` on a solved triangle, but it ran *after* the bare name in the
same program, so an empty list may mean "the brackets are wrong" or "there is
nothing left to solve". The two readings are not separated, and the order of
the calls is the reason. One call in a fresh batch, brackets first, would
settle it.

**Its two siblings across other apps are still untested this way**
(emulator): [DoInference](../inference/DoInference.md) and
[Do1VStats](../statistics-1var/Do1VStats.md) refuse, and neither has been
given data by a program the way this one was. This row makes it likely they
behave the same, and likely is not measured.

**The space inside the brackets is incidental** (emulator), and so is the
leading space in the second row. Both exist only so repeated runs keep
separate rows, since `results.tsv` keys a row by the exact text of its call.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SSS](SSS.md) · [DoInference](../inference/DoInference.md) ·
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
