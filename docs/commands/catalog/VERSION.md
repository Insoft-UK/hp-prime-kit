# VERSION

Answers the software version, and the serial number with it.

| | |
|---|---|
| Syntax | `VERSION([n])` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("VERSION")` | `"(not stored)"` | [emulator](../results.tsv) |

## Behaviour

**That result is not what the calculator answered** (emulator). The reply is
several lines of text, a string of type 2,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), and one of those lines
carries the calculator's serial number. The harness replaced the whole answer
before the row was built.

**This is the command that caused the rule** (emulator). An early batch
stored what it answered, serial number included, into a file that is
committed and published. The fix was not to be careful next time: the name
went on a short list in `hpkit/examples.py` whose answers are never kept, the
same list [SERIAL](SERIAL.md) is on.

**What survives is the version number and the build date** (emulator). Every
row in `results.tsv` is stamped with those two, pulled out of this answer by
a function that skips the line naming the serial. That is how a measurement
records which firmware produced it without carrying anything of the machine.

HP's list gives it an optional argument (HP help). What a number selects from
the answer was not run (unverified), and it is the one form that might return
a single line worth storing.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SERIAL](SERIAL.md) · [MEMORY](MEMORY.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
