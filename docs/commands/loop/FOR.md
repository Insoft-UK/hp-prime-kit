# FOR

Repeats a block for each value of a counter, counting up or down.

| | |
|---|---|
| Syntax | `FOR var FROM start TO finish [STEP increment] DO commands END;` |
| Syntax | `FOR var FROM start DOWNTO finish [STEP increment] DO commands END;` |
| Group | loop |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL zi, zs; zs := {}; FOR zi FROM 1 TO 10 STEP 2 DO zs := CONCAT(zs, {zi}); END; RETURN zs;` | `{1,3,5,7,9}` | [emulator](../results.tsv) |
| `LOCAL zi, zs; zs := {}; FOR zi FROM 10 DOWNTO 1 STEP 2 DO zs := CONCAT(zs, {zi}); END; RETURN zs;` | `{10,8,6,4,2}` | [emulator](../results.tsv) |
| `LOCAL zi, z; FOR zi FROM 1 TO 2 DO z := zi; END;` | `2` | [G2](../../topics/ppl.md#ppl.function-always-answers) |

## Behaviour

The counter starts at `start`, and the block runs until the counter passes
`finish`. Each pass adds 1 to it, or `increment`, and `DOWNTO` subtracts
instead (HP help). HP's own examples print the values; the first two above
collect them in a list, which is the same loop.

One `END` closes the loop, as it closes every block: `ENDFOR` does not exist
(G2). `RETURN` inside the loop is allowed, and leaves the function from there
(G2): the fact is [ppl.return-in-loop](../../topics/ppl.md#ppl.return-in-loop).

A function whose last statement is a loop, with no `RETURN`, answers the last
value the loop's body produced (G2).

## Related

[ppl.return-in-loop](../../topics/ppl.md#ppl.return-in-loop) · [SIZE](../list/SIZE.md)
