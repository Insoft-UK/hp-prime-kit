# 5. Moving to Python

The Prime has carried MicroPython since the 2021 firmware, and with it a bridge
that runs PPL and hands the result back. So the question is not which language
to use, but which half goes where.

The full detail is in [micropython.md](../topics/micropython.md).

---

## When it is worth it

| Move to Python when | Stay in PPL when |
|---|---|
| the interface is getting long | the program is small |
| you already have the logic in Python on your PC | you need a library other programs call |
| you want to test the real code on your PC | you are calling the calculator's own maths |

The reason that outweighs the others:

> The file that computes can be exactly the same on the PC and on the
> calculator. Only the module underneath it changes, the one that looks data
> up. With that, your PC tests say something real about what runs on the G2.

## Send a probe first

There are questions you cannot answer from a PC: whether the bridge responds,
whether it sees your PPL functions, what `GETKEY` returns for each key, whether
touch arrives and with what coordinates. One app answers all of them in a
single pass:

```bash
hpprime build PROBE examples/probe/main.py
```

Drag it over, open it and read what it reports. Ten minutes there saves a day
of guessing later.

## Hello, bridge

```bash
hpprime new MYAPP --python
```

That writes `MYAPP/main.py`, with two rules already applied.

The file must be called `main.py` and its code must be at module level, not
inside an `if __name__` block. That is the entry point, and it runs on import.
Without it, your app starts and nothing happens.

Everything the screen does goes through `eval`:

```python
from hpprime import eval as ev, fillrect

fillrect(0, 0, 0, 320, 240, 0xFFFFFF, 0xFFFFFF)
ev('TEXTOUT_P("hello",G0,3,10,2,RGB(0,0,0))')
n = ev('1+1')            # -> 2
ev('CX:=3.5')            # write a PPL global
x = ev('CX')             # and read it back
r = ev('AREA(2)')        # call YOUR PPL library
```

Then build and drag it over:

```bash
hpprime build MYAPP MYAPP/main.py
```

## The two traps that cost a day each

A list with a string inside closes the app. There is no exception, no message
and no trace: if your PPL function returns `{1, 2, "warning"}`, calling it raw
from Python kills the app on the spot.

The fix is never to let the raw list out. Wrap the call in PPL and let only
numbers through:

```python
def numbers_only(call):
    return ev('LOCAL zr:=' + call + '; {zr(1),zr(2),zr(3)}')
```

Design your PPL library that way from the start: a flat list of numbers, or a
number.

`time` does not exist. If `import time` fails, the bridge is fine and the
module is simply not there. What MicroPython on the Prime has is `math`,
`hpprime`, `micropython` and not much else. `hpprime build` warns about an
import it does not recognise, because on the calculator that failure looks like
the app closing at startup, silently.

## Debugging when the app closes by itself

There is no trace and the screen is gone. What works is leaving a mark in a PPL
global, which survives the close:

```python
def mark(t):
    try:
        ev('PZ:="' + t + '"')
    except Exception:
        pass

mark('before the call')
r = ev(EXPRESSION)
mark('call ok')
```

If the app dies, go to Home, type `PZ` and press `Enter`. It says how far it
got. Put the marks in order of increasing risk, and the point where it dies
identifies the cause without further experiments.

## The architecture to aim for

```
      PC                                   calculator
   ---------                            -----------------
   engine.py   \                       /   LIB (PPL)
                >   data.py (2 faces) <
                                       \   hpprime.eval
                       |
                    app.py      <-- THE SAME FILE in both places
                       |
                 main / screen         <-- pixels only here
```

- `app.py` is literally the same file in your repository and in the app.
  `hpprime build` copies it, and `hpprime verify` tells you when the two have
  drifted apart.
- `data.py` is the one piece deliberately written twice, with the same face:
  one version over your PC engine, one over the bridge.
- Whatever touches pixels and keys stays as thin as you can make it, because it
  is the only part you cannot test from the PC.

The bridge costs 0.2 ms per crossing, measured. Thirty crossings is 8 ms, so
there is nothing to optimise here. Write the clear version.

---

Next: [6. Working with an AI](06-working-with-ai.md).
