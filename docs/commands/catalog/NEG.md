# NEG

Negation, refused when it is written as a call.

| | |
|---|---|
| Syntax | not published |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("NEG(5)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**`NEG(5)` is refused** (emulator). Written directly into a program rather
than inside a string, it is the line the editor's Check flagged, so it fails
to compile and not merely to run.

HP's list gives this name no syntax string (HP help). Two other names in that
same position have been settled since, and both turned out to be operators
written between their arguments: `MOD` and `NTHROOT`.

**Negation takes one argument, so the infix answer cannot be the answer
here** (unverified). That leaves a prefix operator, `NEG 5`, or a name that
is not typed at all but entered from a menu, the way the imaginary unit and
the exponent glyph are. Neither has been run.

The probe is `NEG 5`, and it belongs in a string until it is known
(emulator): a bad line refuses the whole batch it travels in, which is what
made this name cost several rounds.

The interpreter does not know the name at all (unverified), so `hpprime run`
cannot check a program that uses it either way.

## Related

[NTHROOT](NTHROOT.md) · [INVERSE](INVERSE.md) · [MOD](../arithmetic/MOD.md)
