# EVAL

Evaluates an expression.

| | |
|---|---|
| Syntax | `EVAL(expression)` → the value |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EVAL(2+3)` | `5` | [emulator](../results.tsv) |

## Behaviour

An expression written in the source is already evaluated when it is passed,
so `EVAL(2+3)` answers 5 exactly as `2+3` would (emulator). That makes the
measured example a poor demonstration of what the command is for, and it is
here because it is what was run.

Where it earns its place is with something not yet evaluated -- a symbolic
expression, or a variable holding one -- and nothing here has measured that
(unverified). [EXPR](../strings/EXPR.md) is the measured way to evaluate
**text**, which is a different thing and the one a program usually needs.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EXPR](../strings/EXPR.md) · [TEVAL](TEVAL.md)
