# IFERR

Runs a block, and runs a second one instead if the first raises an error.

| | |
|---|---|
| Syntax | `IFERR commands1 THEN commands2 END;` |
| Syntax | `IFERR commands1 THEN commands2 ELSE commands3 END;` |
| Group | branch |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL z; z := 0; IFERR z := MID("abcdef", 0, 2); THEN z := -1; END; RETURN z;` | `-1` | [emulator](../results.tsv) |
| `LOCAL z; z := 0; IFERR z := MID("abcdef", 2, 3); THEN z := -1; END; RETURN z;` | `"bcd"` | [emulator](../results.tsv) |

## Behaviour

It traps a system error: the calculator's own refusal, such as the start below
1 that [MID](../strings/MID.md) rejects (G2), which is what the first example
catches (emulator). What it does not give you is a
way to raise an error of your own with a value inside, so a library that has
to report a reason still needs a convention of its own, such as a region code
of `-1` (unverified).

The error's code is left in `Ans`, and `STRINGFROMID` turns that into a
message (unverified). Neither has been measured here, and the entry for
`STRINGFROMID` will say what it answers once a batch has run it.

`IFERR` hardens one call. Wrapping a whole program in it hides where the
failure was, and the recorded practice is to wrap the call that can fail
(unverified).

## Related

[IF](IF.md) · [CASE](CASE.md) · [MID](../strings/MID.md)
