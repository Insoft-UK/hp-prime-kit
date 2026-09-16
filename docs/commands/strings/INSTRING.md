# INSTRING

Where one string first appears inside another.

| | |
|---|---|
| Syntax | `INSTRING(String1, String2)` → number |
| Group | strings |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `INSTRING("banana", "na")` | `3` | [emulator](../results.tsv) |
| `INSTRING("ab", "abc")` | `0` | [emulator](../results.tsv) |
| `INSTRING("abcdef", "cd")` | `3` | [emulator](../results.tsv) |
| `INSTRING("abcdef", "f")` | `6` | [emulator](../results.tsv) |
| `INSTRING("abcdef", "zz")` | `0` | G2 |
| `INSTRING("abcdef", "")` | `1` | G2 |

## Behaviour

The position counts from 1, like every index in PPL (G2):
[ppl.one-based](../../topics/ppl.md#ppl.one-based). The first example is HP's
own: `na` starts at the third character of `banana`, not at the fifth, so it
answers the **first** match (HP help).

A needle longer than the haystack is simply not found (HP help), which is the
second example.

Not found is **0**, not −1 and not an error (G2). Since 0 is also the answer
no position ever has, `IF INSTRING(s, t) THEN` reads as "if it is there",
which is the idiom the measured programs use.

An empty second argument answers **1** (G2). That is the trap: a needle built
from a field the user left blank reports a match at the start rather than
nothing, so the guard is on the needle, before the call.

**Evidence.** The two edges were measured on a G2 with firmware 2.4.15515.
The two ordinary cases ran on the Virtual Calculator 2.4, build 2025-09-15, in
the batch stored on 2026-09-12, and agree.

## Related

[MID](MID.md) · [LEFT](LEFT.md) · [RIGHT](RIGHT.md) ·
[ppl.one-based](../../topics/ppl.md#ppl.one-based)
