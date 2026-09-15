# CHECK

Turns on one of the statistics app's analyses.

| | |
|---|---|
| Syntax | `CHECK(n)` |
| Group | statistics-1var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("CHECK(1)")` | `1` | [emulator](../results.tsv) |

## Behaviour

`CHECK(1)` answers 1 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It answered from Home without its own app being selected** (emulator),
which is what says this group is reachable at all: three of its six names
work that way and three do not. The app that was active is the Function one,
which a reset calculator always has,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active);
"no app open" is not a condition the Prime has.

**The answer is not the same question as [ISCHECK](ISCHECK.md)'s**
(emulator). That one answered 0 for the same analysis before this ran, so 1
here most likely reports the new state or the success of setting it. One row
cannot tell those apart, and this entry does not choose.

**It changes the calculator rather than only reporting on it** (HP help),
which is why it was sent to the throwaway `Prime_1` and never to the user's
own machine. [UNCHECK](UNCHECK.md) is its opposite and also answered 1.

The probe worth one row is `ISCHECK` after `CHECK` (unverified), which would
show whether the change took.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[UNCHECK](UNCHECK.md) · [ISCHECK](ISCHECK.md) · [Do1VStats](Do1VStats.md)
