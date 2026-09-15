# AngleB

The angle opposite side B.

| | |
|---|---|
| Syntax | `AngleB` → real |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR(" AngleB")` | `−1` | [emulator](../results.tsv) |
| `EXPR("  AngleB")` | `53.1301023542` | [emulator](../results.tsv) |

## Behaviour

**−1 before, 53.1301023542 after** (emulator), with
[DoSolve](DoSolve.md) between them and sides of 3, 4 and 5 set by the same
batch. [AngleA](AngleA.md) carries the account of what those two readings
mean.

**The two angles sum to 90** (emulator): 36.8698976458 and 53.1301023542 add
to 90 exactly, as they must in a right triangle, and
[AngleC](AngleC.md) holds the right angle itself. That the three agree is
worth more than any one of them, because it shows the app filled all three
from one call rather than leaving stale values behind.

**Degrees again**
(emulator),
[apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AngleA](AngleA.md) · [AngleC](AngleC.md) · [SideB](SideB.md) ·
[DoSolve](DoSolve.md)
