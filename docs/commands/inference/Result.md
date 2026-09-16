# Result

A code DoInference wrote 1 into, and nothing says what 1 means.

| | |
|---|---|
| Syntax | `Result` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Result")` | `0` | [emulator](../results.tsv) |
| `EXPR(" Result")` | `1` | [emulator](../results.tsv) |

## Behaviour

**0 before [DoInference](DoInference.md), 1 after** (emulator), in the pass
that also filled [TestScore](TestScore.md) and [Prob](Prob.md).

**What 1 means is not measured** (unverified). It could be "the test ran", it
could be "do not reject", it could be an index into a list of outcomes.
`DoInference` itself also returned 1, which makes "it ran" the likeliest
reading and leaves it a reading. A second run on data that rejects would
separate them, and this documentation does not have one.

**A program should not compare it against 1 on the strength of this entry**
(emulator). Two geometry tests answered codes rather than truths --
`is_isosceles` answered 3 and `is_parallelogram` 4 -- so a code that happens
to be 1 here is exactly the shape of trap this documentation exists to
name.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Prob](Prob.md) · [TestScore](TestScore.md) · [DoInference](DoInference.md)
