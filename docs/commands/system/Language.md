# Language

The calculator's language, as a number.

| | |
|---|---|
| Syntax | `Language` → real |
| Syntax | `Language:=value` |
| Group | system |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Language")` | `5` | [emulator](../results.tsv) |
| `LOCAL o; o := EXPR("Language"); EXPR("Language:=" + STRING(o)); RETURN EXPR("Language");` | `5` | [emulator](../results.tsv) |

## Behaviour

**It reads 5 on this Virtual Calculator, whose messages are in Spanish**
(emulator). Which number is which language, beyond that one, was not
measured (unverified).

**A program can assign it** (emulator): given its own value back, it was
accepted. Setting another language was not tried.

**Error messages come back in this language** (emulator), which is why no
entry quotes one as if it were fixed: [STRINGFROMID](../strings/STRINGFROMID.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Theme](Theme.md) · [STRINGFROMID](../strings/STRINGFROMID.md)
