# ROOT

The root of a function in F1, and the guess chooses which one.

| | |
|---|---|
| Syntax | `ROOT(Fn, [Guess])` |
| Group | function |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ROOT(F1,1)` | `2` | G2 |
| `EXPR(" ROOT(F1,1)")` | `2` | [emulator](../results.tsv) |
| `EXPR("ROOT(F1,-1)")` | `−2` | [emulator](../results.tsv) |
| `EXPR("F1:=X^2-4")` | `−4` | [emulator](../results.tsv) |
| `EXPR("ROOT(F1,1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The guess picks between the two roots** (emulator and G2). With `F1` set to
`X^2-4` in the Function app, a guess of 1 answers 2 and a guess of −1 answers
the other root. The first and third rows were taken differently -- one by hand, one by a
batch with the app selected first -- and they agree on the behaviour.

**The fourth row shows why this took three attempts to measure** (emulator).
Assigning through [EXPR](../strings/EXPR.md) evaluates before storing, so
`F1:=X^2-4` put the **number** −4 into `F1`, not the function. A constant has
no root, which is what the fifth row records.

**Two conditions have to hold at once, and a batch can arrange both**
(emulator): `F1` must hold a real function, and the Function app must be
active,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).
The second is free -- a reset calculator has that app active already,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active).
The first is one line: `F1:='X^2-4'` stores the expression itself, type 8,
where `F1:=X^2-4` stored the number −4. The quote is the whole difference.

**This entry said the opposite for a day** (emulator). It said a person had to
fill `F1` in the app's own editor and that a batch could arrange neither
condition. A later batch did both unaided and `ROOT(F1,1)` answered 2 from
it, matching the reading taken by hand. What had been missing was a quoting
rule, not an ability.

**This entry recorded two wrong readings before these rows existed**
(emulator). First the group was called unreachable, from a probe that never
checked its own setup. Then the setup was measured and the group shown to
compute, but with a constant, so `ROOT` still looked broken. Neither was
true.

The minus signs are the calculator's own, U+2212 (emulator),
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign): those cells were built
from the stored rows rather than typed.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EXTREMUM](EXTREMUM.md) · [ISECT](ISECT.md) · [SLOPE](SLOPE.md) ·
[AREA](AREA.md)
