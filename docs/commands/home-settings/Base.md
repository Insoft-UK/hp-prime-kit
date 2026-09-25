# Base

The base Home writes integers in: 3, hexadecimal, on a reset calculator.

| | |
|---|---|
| Syntax | `Base` → real |
| Syntax | `Base:=value` |
| Group | home-settings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Base")` | `3` | [emulator](../results.tsv) |
| `EXPR("STRING(R→B(255))")` | `"#FFh"` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Base"); EXPR("Base:=3"); r := EXPR("Base"); EXPR("Base:=" + STRING(o)); RETURN r;` | `3` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Base"); EXPR("Base:=0"); IFERR r := {EXPR("Base"), STRING(R→B(255))}; THEN r := "refused"; END; EXPR("Base:=" + STRING(o)); RETURN r;` | `{0,"#11111111b"}` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Base"); EXPR("Base:=1"); IFERR r := {EXPR("Base"), STRING(R→B(255))}; THEN r := "refused"; END; EXPR("Base:=" + STRING(o)); RETURN r;` | `{1,"#377o"}` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Base"); EXPR("Base:=2"); IFERR r := {EXPR("Base"), STRING(R→B(255))}; THEN r := "refused"; END; EXPR("Base:=" + STRING(o)); RETURN r;` | `{2,"#255d"}` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Base"); EXPR("Base:=3"); r := {EXPR("Base"), STRING(R→B(255))}; EXPR("Base:=" + STRING(o)); RETURN r;` | `{3,"#FFh"}` | [emulator](../results.tsv) |

## Behaviour

**0 is binary, 1 octal, 2 decimal and 3 hexadecimal** (emulator):
`STRING(R→B(255))` answered `"#11111111b"`, `"#377o"`, `"#255d"` and
`"#FFh"`, the letter at the end saying which.

**A program can set it** (emulator), and each row that did put the first
value back, so no later row saw the change.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Bits](Bits.md) · [Signed](Signed.md) · [R→B](../integer/R→B.md)
