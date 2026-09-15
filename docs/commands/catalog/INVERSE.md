# INVERSE

The inverse, refused everything tried here.

| | |
|---|---|
| Syntax | not published |
| Group | catalog |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("INVERSE(4)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**`INVERSE(4)` is refused** (emulator). Written directly into a program
rather than inside a string, it is the line the editor's Check flagged, so
the refusal is at compile time and not only at run time.

HP's list gives this name no syntax string (HP help), the same gap that
`MOD` and `NTHROOT` have, and for both of those the working form turned out
to be an operator written between its arguments rather than a call.

**The interpreter points somewhere else, and it is the better lead**
(unverified). It implements the name and refuses this call with a reason
rather than a shrug: the argument has to be a matrix. That makes a number
the mistake here, not the parentheses, and it is the one hypothesis in this
entry that has a clear probe: `INVERSE([[1,2],[3,4]])` on the calculator.

Until that runs, this entry records a refusal and not a working form
(unverified). A reader who needs the inverse of a matrix today should reach
for the matrix group's own commands, which are measured.

Because the two machines disagree about what is wrong with the same call,
`hpprime run` will not reproduce the calculator's refusal (unverified): the
PC raises about the argument's kind, the calculator refuses the line.

## Related

[NEG](NEG.md) · [NTHROOT](NTHROOT.md) · [MOD](../arithmetic/MOD.md)
