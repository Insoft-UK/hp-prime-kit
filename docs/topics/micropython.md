# Python on the Prime

Facts about MicroPython on the calculator and the bridge to PPL, rather than
about one command. Each has an identifier, says how it is known, and is stated
here once.

The Prime has carried MicroPython since the 2021 firmware, and with it a
module of its own, `hpprime`, which gives direct drawing and an `eval()` that
runs arbitrary PPL and returns the result. That makes Python a practical way
to write an app's interface and logic, leaning on PPL for what the calculator
does not otherwise expose. One consequence is worth more than the rest:

> The file that computes can be exactly the same on the PC and on the
> calculator. The only thing that changes underneath is the module that looks
> data up. With that, PC tests say something real about what runs on the G2.

There is no official HP documentation for any of this. What follows was
measured on a G2 with firmware 2.4 revision 15515, or read from apps that run
on one, and each fact says which.

## The architecture that makes this useful

The bridge on its own is not much. What turns it into a way of working is the
split:

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

`app.py` is the same file in the repository and in the app, copied with a
command, and `hpprime verify` confirms that the two have not drifted apart.
`data.py` has two versions with the same face: one calls the PC engine, the
other crosses the bridge, and it is the one piece deliberately duplicated.
Whatever touches pixels and keys is isolated in a module as thin as you can
make it, because it is the only part that cannot be tested from the PC.

The discipline pays off in a specific way: a synchronisation test of this kind
is what catches a serialised form that silently drops a field. On the Python
side a round trip can pass because the defaults happen to match; the PPL side,
which has no defaults, gives it away at once.

---

<a name="micropython.modules"></a>
## What is there and what is not

| | |
|---|---|
| Identifier | `micropython.modules` |
| Kind | rule |
| Known from | G2 |

| | |
|---|---|
| `math` | yes, and it is the whole library dependency a calculation engine needs |
| `hpprime` | yes: the bridge and the drawing |
| `micropython` (`const`) | yes |
| `time` | does not exist. Apps that need it bring their own `time.py`, built on `eval('ticks()')` |
| `__future__` | no |
| `os`, `sys` | not in the CPython sense: do not count on them |
| NumPy | no |

The missing `time` is worth knowing about because of how it fails: `import
time` raises, and it is easy to conclude that the Python bridge does not work
at all. It does. The way to find out is to read code that already runs on that
same calculator -- the Markdown Viewer starts with `from hpprime import eval,
fillrect` -- and the method generalises: on a thinly documented platform, find
working code before concluding anything.

**Evidence.** Run on a G2 with firmware 2.4.15515.

<a name="micropython.community-modules"></a>
## The modules the community documents and nobody here has run

| | |
|---|---|
| Identifier | `micropython.community-modules` |
| Kind | rule |
| Known from | unverified |

`cmath`, `array`, `gc`, `sys`, `ucollections`, `uerrno`, `uhashlib`, `uio`,
`urandom`, `ure`, `ustruct`, `utimeq`, and the `graphic` and `cas`
(`cas.caseval`) modules. For linear algebra the community route is the Prime's
own `linalg`.

**Evidence.** [HP Prime Python
Libraries](https://udel.edu/~mm/hp/primePython/upython.html), which warns that
the Prime implements a subset of MicroPython and that more routines are
documented than exist. Nothing here has been run on a calculator.

<a name="micropython.hpprime-module"></a>
## The hpprime calls in use

| | |
|---|---|
| Identifier | `micropython.hpprime-module` |
| Kind | rule |
| Known from | G2 |

```python
from hpprime import eval, fillrect, keyboard
```

| Call | What it does |
|---|---|
| `eval(ppl_string)` | runs PPL and returns the result |
| `fillrect(gr, x, y, w, h, edge, fill)` | filled rectangle. `gr=0` is the screen |
| `keyboard()` | true if any key is down |
| `dimgrob(n, w, h, colour)` | creates an off-screen grob, used to measure text |

Colours are 24-bit integers, `0xRRGGBB`.

**Evidence.** In use and working in apps that run on a G2 with firmware
2.4.15515.

<a name="micropython.hpprime-undocumented"></a>
## The rest of the hpprime module is not exercised here

| | |
|---|---|
| Identifier | `micropython.hpprime-undocumented` |
| Kind | rule |
| Known from | unverified |

`arc`, `blit`, `circle`, `grob`, `grobh`, `grobw`, `line`, `mouse`, `pixon`,
`rect`, `strblit`, `textout`, `get_cartesian`, `set_cartesian`, and a `_c`
variant of each. For nearly all of them there is a PPL equivalent reachable
through `eval`, which is what the apps read here do.

**Evidence.** The community's list, not run on a calculator here.

<a name="micropython.eval"></a>
## eval() runs PPL and returns numbers and lists of numbers

| | |
|---|---|
| Identifier | `micropython.eval` |
| Kind | rule |
| Known from | G2 |

```python
from hpprime import eval as ev

ev('TEXTOUT_P("hello",G0,10,20,2,RGB(0,0,0))')   # draws
n = ev('1+1')                                     # -> 2
t = ev('ticks()')                                 # milliseconds
ev('CX:=3.5')                                     # writes a PPL global
x = ev('CX')                                      # and reads it back
r = ev('MYFUNC(1.0)')                             # calls YOUR PPL library
```

That is all you need to call a well-written PPL library.

**Evidence.** Measured on a G2 with firmware 2.4.15515, in apps that use every
form above.

<a name="micropython.eval-parentheses"></a>
## Whether the parentheses matter on the Python side is not known

| | |
|---|---|
| Identifier | `micropython.eval-parentheses` |
| Kind | rule |
| Known from | unverified |

The examples here write `ticks()` and `GETKEY()`, and a published library
writes `eval('ticks')` bare. In PPL source `GETKEY` compiles and answers
with and without them
([ppl.getkey-no-parentheses](ppl.md#ppl.getkey-no-parentheses)), so on the
Python side too one form may be tolerated rather than required.

**Evidence.** None: nobody has run the two side by side.

<a name="micropython.list-with-string-closes-the-app"></a>
## A list with a string inside closes the app

| | |
|---|---|
| Identifier | `micropython.list-with-string-closes-the-app` |
| Kind | rule |
| Known from | G2 |

No exception, no message, no trace. A PPL function returning
`{T,P,v,u,h,s,x,region,WARNING}` -- eight numbers and a text warning at the
end -- called raw from Python, closes the app; everything that had worked
until then returned plain numbers.

The fix is never to let the raw list out. Wrap the call in PPL and let only
numbers through:

```python
def _eight(call):
    """Run a PPL call and take ONLY the eight numbers."""
    return ev('LOCAL zr:=' + call + '; {zr(1),zr(2),zr(3),zr(4),zr(5),'
              'zr(6),zr(7),zr(8)}')
```

The same pattern covers `MOUSE`, which returns lists inside lists
([interface.mouse-lists](interface.md#interface.mouse-lists)). The general
rule: have the PPL wrapper return a flat list of numbers, or a number. If your
PPL library will be called from Python, design it that way from the start.

**Evidence.** Measured on a G2 with firmware 2.4.15515, and identified in one
pass by [micropython.mark-debugging](#micropython.mark-debugging).

<a name="micropython.string-quotes"></a>
## A quote inside a built string breaks the PPL expression

| | |
|---|---|
| Identifier | `micropython.string-quotes` |
| Kind | rule |
| Known from | G2 |

Clean them before concatenating: `s = str(s).replace('"', "'")`.

**Evidence.** Measured on a G2 with firmware 2.4.15515, while building `eval`
strings from user data.

<a name="micropython.number-notation"></a>
## Pass numbers through repr(float(x)), not scientific notation

| | |
|---|---|
| Identifier | `micropython.number-notation` |
| Kind | rule |
| Known from | unverified |

A number Python writes as `1e+20`, with the `+` sign, is reported to be
misread by the Prime's HOME environment. What is in use and works is
`repr(float(x))`, which in the normal working range gives a form the PPL
parser understands. If you are going to move very large or very small
magnitudes, check it with a probe before trusting it.

**Evidence.** The failure is reported by the community, whose workaround is
`cas.caseval`; it has not been reproduced here. That `repr(float(x))` works in
the normal range is measured, on a G2 with firmware 2.4.15515.

<a name="micropython.bridge-cost"></a>
## A bridge crossing costs 0.2 ms

| | |
|---|---|
| Identifier | `micropython.bridge-cost` |
| Kind | rule |
| Known from | G2 |

A calculation making 30 to 40 lookups spends about 8 ms on the bridge. There
is nothing to optimise there: write the clear code and cross as often as you
need. Next to PPL's own speed
([ppl.speed-anchor](ppl.md#ppl.speed-anchor)) it is nothing, which is what
makes moving heavy computation into Python a real option.

**Evidence.** Timed on a G2 with firmware 2.4.15515.

<a name="micropython.imports"></a>
## A shared module can only import what MicroPython has

| | |
|---|---|
| Identifier | `micropython.imports` |
| Kind | rule |
| Known from | G2 |

The symptom on the calculator is that the app closes without a word, so it is
worth a test on the PC:

```python
ALLOWED = ('math', 'engine', 'data', 'list', 'views', 'screen', 'hpprime')
```

Imports inside a function do not count; only top-level ones. `hpprime build`
checks it. Delete `__pycache__` before packaging as well: those are CPython
`.pyc` files, which MicroPython would not read and which only add bulk.

**Evidence.** Measured on a G2 with firmware 2.4.15515: an app importing a
module MicroPython does not have closes on startup.

<a name="micropython.mark-debugging"></a>
## When the app closes by itself, leave marks in a PPL global

| | |
|---|---|
| Identifier | `micropython.mark-debugging` |
| Kind | rule |
| Known from | G2 |

No trace, no message, and the screen is gone. What survives the close is a PPL
global:

```python
def mark(t):
    try:
        ev('PZ:="' + t + '"')
    except Exception:
        pass

mark('before the wrapper')
r = ev(EXPRESSION)
mark('wrapper ok')
```

If the app closes, go to Home, type `PZ` and press `Enter`: it says how far it
got. Package the probe as an app rather than as a loose script, so that it
runs by the same path the real app will. There is one ready to adapt in
`examples/probe/`, which answers in one pass what
cannot be answered from the PC: whether the bridge responds, whether it sees
your PPL functions, what `GETKEY` returns for each key, and whether touch
arrives and with what coordinates.

**Evidence.** Measured on a G2 with firmware 2.4.15515. It is how
[micropython.list-with-string-closes-the-app](#micropython.list-with-string-closes-the-app)
was found in a single pass: the probe tried things in order of increasing risk
-- `{1,2,3}`, then `{1,"a"}`, then a real list of ten numbers, then the
trimmed call, and the raw one last -- so the point where it died identified
the cause with no further experiments.

<a name="micropython.ppl-calls-python"></a>
## PPL can call Python, and it has not been measured here

| | |
|---|---|
| Identifier | `micropython.ppl-calls-python` |
| Kind | rule |
| Known from | unverified |

`PYTHON("script_name", parameters);` runs a Python script from PPL, and the
program editor accepts `#PYTHON … #END` blocks inside PPL source. For a
calculation engine the useful direction is the other one, so this is here to
put the door on record rather than because it was tried.

**Evidence.** [HP Prime
Programming](https://udel.edu/~mm/hp/primePython/), not run here.

<a name="micropython.not-measured"></a>
## What is still not measured about Python on the Prime

| | |
|---|---|
| Identifier | `micropython.not-measured` |
| Kind | rule |
| Known from | unverified |

Pure computation speed in Python against PPL: the bridge crossing is measured
([micropython.bridge-cost](#micropython.bridge-cost)), how long a long numeric
loop takes inside MicroPython is not. The memory limit of a Python app: how
many modules, and how large, before it runs out of room. And the `_c` variants
and the rest of the `hpprime` module
([micropython.hpprime-undocumented](#micropython.hpprime-undocumented)).

**Evidence.** None. Each would take one probe app and a stopwatch.
