# IF

Runs a block when a test is true, and another block when it is not.

| | |
|---|---|
| Syntax | `IF test THEN commands END;` |
| Syntax | `IF test THEN commands1 ELSE commands2 END;` |
| Group | branch |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL z; z := 0; IF 1 == 1 THEN z := 5; END; RETURN z;` | `5` | unverified |
| `LOCAL z; z := 0; IF 1 == 2 THEN z := 5; ELSE z := 7; END; RETURN z;` | `7` | unverified |
| `LOCAL z; z := 3; IF 1 == 2 THEN z := 5; END; RETURN z;` | `3` | unverified |

## Behaviour

The test compares with `==`; a single `=` is not a comparison in PPL
(unverified), and the rule is
[ppl.equality-operators](../../topics/ppl.md#ppl.equality-operators). One
`END;` closes the statement, because `ENDIF` does not exist (G2):
[ppl.no-end-keywords](../../topics/ppl.md#ppl.no-end-keywords).

A function whose last statement is an `IF` that does not run still answers
something: the value from before it (G2). That is
[ppl.function-always-answers](../../topics/ppl.md#ppl.function-always-answers),
and it is why the third example gives 3 rather than nothing.

## Related

[CASE](CASE.md) · [IFERR](IFERR.md) ·
[ppl.equality-operators](../../topics/ppl.md#ppl.equality-operators)
