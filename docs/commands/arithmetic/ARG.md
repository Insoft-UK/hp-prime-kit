# ARG

The angle of a complex number.

| | |
|---|---|
| Syntax | `ARG(x+yi)` |
| Group | arithmetic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ARG(3+4*i)` | `0.927295218002` | [emulator](../results.tsv) |

## Behaviour

`ARG(3+4*i)` answers 0.927295218002 (emulator), which is the angle whose
tangent is four thirds.

**That number is radians, and the calculator's angle mode is why.** The same
call in degrees would answer about 53.13. The mode the throwaway calculator
was in was not itself read back, so what this row really says is "this
machine, in whatever mode it was in, answered radians" (unverified). A
program that needs one or the other should set the mode rather than trust
this row, and the probe that would settle it reads the mode alongside the
call.

[ARC](../drawing/ARC.md) carries the same open question about its sweep
angles, and for the same reason (unverified).

With [RE](RE.md) and [IM](IM.md) this is the polar half of taking a complex
number apart: angle here, and the length from `ABS`, which has not been run
beside them (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RE](RE.md) · [IM](IM.md) · [CONJ](CONJ.md)
