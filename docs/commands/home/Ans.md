# Ans

The last answer on Home, which a program's EXPR does not change.

| | |
|---|---|
| Syntax | `Ans` → value |
| Group | home |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Ans")` | `0` | [emulator](../results.tsv) |
| `EXPR("2+3")` | `5` | [emulator](../results.tsv) |
| `EXPR(" Ans")` | `0` | [emulator](../results.tsv) |

## Behaviour

**Evaluating something with `EXPR` inside a program does not move it**
(emulator). In one batch `Ans` read 0, `EXPR("2+3")` answered 5, and `Ans`
read 0 again.

**What it holds after a calculation typed on Home, and whether a program's
own return value becomes it, was not measured** (unverified). A program that
reads it gets whatever Home last answered, which is not something the
program controls.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EXPR](../strings/EXPR.md)
