# DEBUG

Starts a program under the debugger.

| | |
|---|---|
| Syntax | `DEBUG(ProgramName(arguments))` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DEBUG(MYPROG())` | *no value* | unverified |

## Behaviour

**This is the one name in its group that was deliberately not run**
(unverified). Every other name here was measured in a batch; this one was
left out on purpose, and saying so is more honest than an entry that reads as
though nobody got to it.

The reason is the batch itself (emulator). A batch runs a program on an
emulator window and reads its answers back when that window closes. A command
that stops a program and waits for a person at the keyboard does not return,
so it would hold the window open with no result, waiting for somebody to press
keys.

It takes a call, not a name (HP help): the argument is the program being
started together with its arguments, which is why the syntax shows two sets
of parentheses.

What it answers, whether it answers at all, and what it does when the program
is already running were not measured (unverified). The way to measure it is
by hand, at the calculator, not in a batch.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[QUOTE](QUOTE.md) · [SUPPRESS](SUPPRESS.md)
