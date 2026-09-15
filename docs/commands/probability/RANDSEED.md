# RANDSEED

Sets the starting point of the random sequence.

| | |
|---|---|
| Syntax | `RANDSEED([value])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `RANDSEED(1); A := RANDOM(); RANDSEED(1); RETURN A - RANDOM();` | `0` | [emulator](../results.tsv) |

## Behaviour

**Seeding with the same value makes the sequence repeat.** The example draws
a number, seeds again with 1, draws a second, and subtracts: the answer is 0
(emulator), so the two draws were identical.

That is what makes a program using randomness testable. Without it every run
differs and nothing can be compared against a previous one; with it, a test
can fix the seed and expect the same numbers (emulator).

**The example is built to answer itself**, which is why it is one call rather
than two. Two separate draws would be two rows whose equality nobody could
check later, and a stored random number is a value no second run reproduces
(emulator). Subtracting inside the call turns the question into a single
number that means the same thing every time it runs.

What it does with no argument at all, which HP's syntax allows, was not run
(unverified) -- seeding from the clock would be the usual meaning, and that
would make runs differ rather than repeat.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RANDOM](RANDOM.md) · [RANDINT](RANDINT.md) · [RANDNORM](RANDNORM.md)
