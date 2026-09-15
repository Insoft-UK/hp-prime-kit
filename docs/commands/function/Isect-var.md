# Isect

The Function app's stored intersection, 0 while ISECT answered 2.56155281281.

| | |
|---|---|
| Syntax | `Isect` → real |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Isect")` | `0` | [emulator](../results.tsv) |
| `EXPR("  Isect")` | `0` | [emulator](../results.tsv) |

## Behaviour

**This is the clearest of the five** (emulator). [ISECT](ISECT.md) answered
2.56155281281 for `F1` and `F2` holding `X^2-4` and `X`, and the very next
call read this variable and got 0. No rounding, no coincidence, no reading
under which 0 is that answer: the command did not write here.

**It was 0 before as well** (emulator), read at the start of the same batch
before `F1` had been given anything. So the pair brackets the command and
neither end moved.

**Its file carries the `-var` suffix** (HP help), because this name and
[ISECT](ISECT.md) differ only in case. [Root](Root-var.md) carries the rule.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ISECT](ISECT.md) · [Root](Root-var.md) · [Extremum](Extremum-var.md)
