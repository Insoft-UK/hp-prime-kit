# PIXOFF

Clears one point, in the drawing units of the current view.

| | |
|---|---|
| Syntax | `PIXOFF([grob,] x, y)` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,10,5,RGB(255,0,0)); PIXOFF(G1,1,1); RETURN GETPIX(G1,1,1);` | `#FF000000h` | [emulator](../results.tsv) |

## Behaviour

The grob was created filled red and the point read back `#FF000000h`
(emulator). That is the same answer [GETPIX](GETPIX.md) gives on a grob
created with colour 0, so the read did not see the red fill either before or
after the clearing.

**That makes this row a measurement of the read, not of the clearing**
(emulator): nothing here says whether the point was cleared, because the
answer is the one that comes back whatever the picture holds.
[GETPIX](GETPIX.md) records the three probes together and the hypothesis
behind them.

Its `_P` twin carries a warning worth repeating: [PIXOFF_P](PIXOFF_P.md) does
not do what its name suggests (emulator), so neither form should be assumed
to paint the background colour until somebody measures which colour it
leaves.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PIXOFF_P](PIXOFF_P.md) · [PIXON](PIXON.md) · [GETPIX](GETPIX.md)
