# CASE

Tries each test in turn and runs the first block whose test is true.

| | |
|---|---|
| Syntax | `CASE IF test1 THEN commands1 END; IF test2 THEN commands2 END; [DEFAULT commands] END;` |
| Group | branch |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL z; z := 0; CASE IF 1 == 2 THEN z := 1; END; IF 1 == 1 THEN z := 2; END; DEFAULT z := 3; END; RETURN z;` | `2` | unverified |
| `LOCAL z; z := 0; CASE IF 1 == 2 THEN z := 1; END; DEFAULT z := 3; END; RETURN z;` | `3` | unverified |

## Behaviour

Each branch is written as its own `IF … THEN … END;` inside the `CASE`, which
is what makes the syntax look heavier than it is (HP help). The first true
test wins and the rest are not tried (unverified).

`DEFAULT` runs when no test was true (HP help). Without a `DEFAULT` and with
no test true, nothing in the `CASE` runs, and the function still answers the
value it had (G2):
[ppl.function-always-answers](../../topics/ppl.md#ppl.function-always-answers).

The outer `END;` closes the `CASE`, and every branch closes its own (G2):
[ppl.no-end-keywords](../../topics/ppl.md#ppl.no-end-keywords).

## Related

[IF](IF.md) · [IFERR](IFERR.md)
