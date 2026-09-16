# SERIAL

Answers this calculator's serial number, which is never stored here.

| | |
|---|---|
| Syntax | `SERIAL` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SERIAL")` | `"(not stored)"` | [emulator](../results.tsv) |

## Behaviour

**That result is not what the calculator answered** (emulator). The call ran
and the machine replied with its own serial number; the harness replaced the
answer before anything was written or printed, and the row says so in its
place. The answer is a string, type 2,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The reason is that this file is committed and published** (emulator).
`results.tsv` travels with the repository, so an answer that identifies a
particular machine would be published along with it, permanently and by
accident.

The guard is a short list of names in `hpkit/examples.py`, applied where the
row is built (emulator). It is code rather than a rule someone has to
remember, which is the answer this project gave after `VERSION` put the same
number into the same file once. `VERSION` is on that list too, for the same
reason.

It takes no parentheses (HP help), the shape a name with no arguments has,
like [MEMORY](MEMORY.md).

**What the serial number looks like is not documented here** (emulator), and
that is deliberate: this entry exists to say the command works and that its
answer is the one thing this documentation will not show you.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[VERSION](VERSION.md) · [MEMORY](MEMORY.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
