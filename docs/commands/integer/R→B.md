# R→B

An ordinary number as a `#` integer.

| | |
|---|---|
| Syntax | `R→B(Real [, bits [,base]])` → integer |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `R→B(12)` | `#Ch` | [emulator](../results.tsv) |

## Behaviour

Twelve becomes `#Ch`: C in hexadecimal, of `TYPE` 1 rather than 0 (emulator).
That is the same answer [SETBITS](SETBITS.md) gives for the same number, so
the two reach the `#` kind by different names, and what separates them has
not been measured (unverified).

[B→R](B→R.md) goes back the other way, measured on this value (emulator).

HP's syntax offers a width and a base as optional arguments (HP help), and
neither has been run here. The width is the interesting one:
[BITNOT](BITNOT.md) showed the calculator complementing across 39 bits, and
whether `R→B(12, 8)` narrows that is the probe that would connect these two
commands to that number.

The name carries an arrow, `→`, which most keyboards do not have (HP help);
it is on the list of names, so `hpprime lint` knows it (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[B→R](B→R.md) · [SETBITS](SETBITS.md) · [BITNOT](BITNOT.md)
