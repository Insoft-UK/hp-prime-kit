# RANDOM

A random number.

| | |
|---|---|
| Syntax | `RANDOM([a], [b], [c])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TYPE(RANDOM())` | `0` | [emulator](../results.tsv) |

## Behaviour

**The example asks what kind of thing comes back, not what number**, and that
is deliberate: a random value is different every run, so a stored answer would
be a number no later run reproduces and the checker would report a
disagreement every time the batch was repeated (emulator).

What can be measured and repeated is the type, and it is 0, an ordinary real
(emulator), [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It can be made repeatable.** Seeding with [RANDSEED](RANDSEED.md) and the
same value gives the same draw again, measured end to end (emulator). A
program that needs to be testable seeds first.

What range the number falls in with no arguments, and what the three optional
ones choose, was not measured (unverified). Zero to one is the usual meaning
of a bare `RANDOM`, and that is an expectation rather than a reading.

[RANDMAT](../matrix/RANDMAT.md) is documented the same way and for the same
reason: by its shape rather than its contents (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RANDSEED](RANDSEED.md) · [RANDINT](RANDINT.md) ·
[RANDMAT](../matrix/RANDMAT.md)
