# GETBITS

How many bits an integer of the calculator's `#` kind carries.

| | |
|---|---|
| Syntax | `GETBITS(#integer)` → integer |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `GETBITS(12)` | *error* | [emulator](../results.tsv) |

## Behaviour

An ordinary number is refused (emulator). HP's syntax writes the argument as
`#integer`, and that `#` is not decoration: it is the calculator's own
notation for an integer of a stated width and base, the kind
[SETBITS](SETBITS.md) and [SETBASE](SETBASE.md) answer with, such as `#Ch` or
`#14o`.

So this is the one command of the group whose argument cannot be typed as a
plain number, and what it answers for a real `#` integer has not been measured
here (unverified): the probe that would settle it is
`GETBITS(SETBITS(12))`, which nobody has run.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SETBITS](SETBITS.md) · [SETBASE](SETBASE.md) · [BITNOT](BITNOT.md)
