# TOff

The time before the calculator turns itself off, 300000 on a reset calculator.

| | |
|---|---|
| Syntax | `TOff` → integer |
| Group | system |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("TOff")` | `#493E0:30h` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("TOff"); EXPR("TOff:=300"); r := EXPR("TOff"); EXPR("TOff:=" + STRING(o)); RETURN r;` | *error* | [emulator](../results.tsv) |

## Behaviour

**It is a based integer, not a real** (emulator): `#493E0:30h`, which is
300000, of type 1.

**300000 would be five minutes in milliseconds** (unverified): that reading
is arithmetic on the default, not a measurement of what it counts.

**Setting it to 300 was refused** (emulator). Whether another value is
accepted -- a based integer, or one large enough to be milliseconds -- was
not tried, so this entry gives no form that sets it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Theme](Theme.md)
