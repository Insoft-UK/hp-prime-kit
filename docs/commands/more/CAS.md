# CAS

Evaluates an expression with the CAS, from a program.

| | |
|---|---|
| Syntax | `CAS(expression)` |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CAS("1/2+1/3")` | `5/6` | [emulator](../results.tsv) |
| `CAS(1/2+1/3)` | `5/6` | [emulator](../results.tsv) |

## Behaviour

**It answers exactly, not approximately.** `1/2+1/3` comes back as `5/6`
(emulator), where ordinary evaluation would give a decimal that is not quite
a third. That is the whole reason to send something to the CAS from a
program: a fraction stays a fraction.

**Both forms of the argument work and answer the same thing.** HP's syntax
says `CAS(expression)` without saying whether the expression is quoted; the
quoted `"1/2+1/3"` and the bare `1/2+1/3` were both run and both answer `5/6`
(emulator). So a program may write it either way, and nothing here depends on
which.

**What comes back has `TYPE` 8** (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). HP's help calls 8 a
function and keeps 14.x for a CAS object, so what the CAS hands back arrives
as 8 rather than 14.x. Which of the two namings is right is not something two
rows settle (unverified), and a program that branches on `TYPE` should be
written against the 8 that is measured rather than the 14.x that is
documented.

**This ran in a batch of its own, on purpose.** It was held out of every
earlier batch because evaluating with the CAS may change the mode the calls
after it are read in, and a batch is one program: a row that quietly changed
the rules for the rows below it would be worse than no row at all (emulator:
the batch carried nothing but this command and [EXECON](EXECON.md), with
`EXECON` first). Whether it changes anything was therefore not measured, and
that is the cost of measuring it safely (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EVAL](EVAL.md) · [EXECON](EXECON.md) · [TYPE](TYPE.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
