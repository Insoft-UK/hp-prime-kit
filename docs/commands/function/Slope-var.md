# Slope

The Function app's stored slope, 0 before and after SLOPE answered 4.

| | |
|---|---|
| Syntax | `Slope` → real |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Slope")` | `0` | [emulator](../results.tsv) |
| `EXPR("  Slope")` | `0` | [emulator](../results.tsv) |

## Behaviour

**[SLOPE](SLOPE.md) answered 4 and this stayed at 0** (emulator), in the same
batch and with one call between them. [Root](Root-var.md) carries the account
of what that means for the whole group: these commands return their answers
and do not store them.

**0 is not a marker for "not computed" here, or if it is, nothing says so**
(emulator). The Triangle Solver marks an unknown side with −1,
[SideA](../triangle-solver/SideA.md), which makes the absence visible. A
slope of 0 is a perfectly ordinary slope, so a program cannot tell a stored
zero from a variable nobody has touched.

**Its file carries the `-var` suffix** (HP help), because this name and
[SLOPE](SLOPE.md) differ only in case. [Root](Root-var.md) carries the rule.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SLOPE](SLOPE.md) · [Root](Root-var.md) · [SignedArea](SignedArea.md)
