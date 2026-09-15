# Screen, keyboard and touch

Facts about the machine a program draws on and reads from, rather than about
one command. Each has an identifier, says how it is known, and is stated here
once.

320 × 240 pixels, a keyboard whose codes are not ASCII, a touch screen and no
window manager. HP's documentation describes the commands one by one and says
nothing about how they combine, so nearly everything here comes from measuring
it on a G2 with firmware 2.4.15515, or from reading apps that run on one --
and which of the two is the label on each fact.

It applies to both languages: from PPL you call these directly, and from
Python you call the same things across the `hpprime.eval` bridge
([micropython.md](micropython.md)).

## The building blocks

| What you need | Command |
|---|---|
| Clear the screen | `RECT()` · from Python, `fillrect(0,0,0,320,240,col,col)` |
| Rectangle | `fillrect(gr, x, y, w, h, edge, fill)` |
| Text | `TEXTOUT_P(txt, G0, x, y, font, colour [, width])` |
| A row of six buttons | `DRAWMENU("a","b","c","d","e","f")` |
| Form | `INPUT(fields, title, labels, help)` |
| Pop-up menu | `CHOOSE(var, title, "opt1", "opt2", …)` |
| Modal notice | `MSGBOX("message")` |
| Pending key | `GETKEY` |
| Touch | `MOUSE` |
| Flicker-free drawing | `DIMGROB_P` to an off-screen grob, then `BLIT_P` to `G0` |

`TEXTOUT_P` fonts: 1 small, 2 normal, 3 large, up to 7. Colours with
`RGB(r,g,b)` in PPL, and `0xRRGGBB` integers from Python. From Python the two
grob calls are `dimgrob(1, 320, 240, 0)` and `blit(0, 0, 0, 1)`, read from a
published toolkit that creates the grob once when it loads and blits every
frame.

## What the design of a screen comes down to

The part of this page that is judgement rather than measurement, kept because
it is what the facts are for.

**Update, then draw.** Every app that feels responsive reads the inputs, moves
the state, and draws the result, rather than drawing where the input is
handled. What a loop keeps: the touch (`x`, `y`, the event type, `dx`/`dy` for
a drag, whether it is down, whether this is a fresh tap), the keyboard (the
key, plus the shift and alpha layers, since one code means different things in
each), and time (milliseconds from `ticks`, and the gap since the last
update). The third matters more than it looks: MicroPython on the Prime has no
`time` module, so anything that animates or times out has to ask PPL.

**One widget covers nearly every screen**: a list with seven visible rows, a
top index, a scrollbar, arrows, touch and digit jump. The data, the parts, the
results and the diagnosis are all one row per record. Since it is pure logic --
selection, window, bar, what each key means -- it can be tested entirely on the
PC, and the pixel module is left drawing rows. Behaviour worth copying, all of
it from apps that work: digits jump to a row; selection wraps; left and right
change column when there are several and page when there are not, which is
what the calculator's own Numeric view does; touching a row selects it and
touching it again enters; `Cancel` and `OK` in positions 5 and 6; partial
redraw; automatic exit on inactivity; `IFERR` around the event loop; a
two-page soft menu rather than six unreadable labels; and theme colours. What
is not worth copying is a full event framework with drags, long press and
eight handlers.

**A table needs no sentinels; a form does.** `Enter` on a record opening an
`INPUT` with four fields is fast and wrong, because a form cannot say "I do not
know this one": you end up inventing `0` for empty and then `-1` because `0` is
a legitimate value. An editable table has no such problem -- an empty cell is
empty -- and two details only come out of typing a real problem into one: after
editing, the cursor moves down on its own, because data arrives by column; and
defaults are proposed, so a four-part chain is typed without entering a single
connecting number.

**Units are stated, not asked for.** Asking at startup is worse than saying
nothing: it lets somebody enter `25` where the table expects `298`, and the
result comes out solved and wrong, which is the worst way to fail. Derive the
unit from the data and show it -- in the `INPUT` label, in the help line, and
in the column title when a whole column shares one.

**What can be tested on the PC**: selection, window, bar and what each key
does; what text goes in each row; that each string fits its column, against a
geometry module with no imports. What cannot: drawing, reading keys, reading
touch, whether a dialog closes where you think, how long a real data entry
takes, and whether the calculation behind it is fast enough
([ppl.md](ppl.md#ppl.speed-anchor)). This is why the pixel module should be as
thin as you can make it. The kit's interpreter follows the same rule:
`TEXTOUT_P`, `INPUT`, `CHOOSE`, `MSGBOX` and `WAIT` are recorded in
`machine.io` and return a neutral value, so a calculation runs with no
interface.

Before building a scrolling list or a menu with pages, see
[libraries.md](libraries.md): which of the three levels a screen
needs, and what `CHOOSE_R`, `LibMenu` and `SkeletonApp` already give you.

## Where this comes from

Third-party apps read from [hpcalc.org](https://www.hpcalc.org/prime/), all of
them running on real calculators:

| Program | What it contributed |
|---|---|
| **SkeletonApp** (Andreas Möller) | the event loop and the soft-menu geometry |
| **CHOOSE_R 1.0** (Jacob Wall) | the windowed list, partial redraw, inactivity exit |
| **LibMenu 3.0** | the two-page soft menu |
| **ktest** / **WaitLab** | what each input method returns, exactly |
| **CAC** | the "choose what you are solving and only be asked for what it needs" pattern |
| **Markdown Viewer** | the `keyboard()` + `GETKEY()` loop from Python, and measuring text with a grob |
| **PrimeEdit** | proof that a full interface fits in Python: widgets, menus, icons, syntax highlighting |

The rest is measured on a G2 with firmware 2.4 revision 15515.

---

<a name="interface.geometry"></a>
## The screen is 320x240, and the soft-key row is the bottom 27 pixels

| | |
|---|---|
| Identifier | `interface.geometry` |
| Kind | rule |
| Known from | G2 |

| | |
|---|---|
| Screen | 320 × 240 |
| App area | y from 0 to 212 |
| Soft-key row | y from 213 to 239 |
| Width of one soft key | ~53 px (320 / 6) |

That is what turns a touch into a button: below y 213, the key is
`int(x / 53) + 1` when that lands in 1..6. A layout that works well for a
list: a 20 px header, seven 24 px rows, and the help line underneath.

**Evidence.** The app area and the soft-key row were measured on a G2 with
firmware 2.4.15515; the key width is the arithmetic that follows from six
across 320 pixels.

---

<a name="interface.draw-units"></a>
## A drawing unit is ten pixels, and the origin is the middle of the screen

| | |
|---|---|
| Identifier | `interface.draw-units` |
| Kind | rule |
| Known from | emulator |

The commands that come in two forms -- `LINE` and `LINE_P`, `DIMGROB` and
`DIMGROB_P`, `GROBW` and `GROBW_P` -- do not differ in what they draw but in
what their numbers mean. The `_P` forms count pixels from the top-left corner.
The forms without `_P` count the current view's units from the middle of the
screen, and in the view a program starts with, one unit is ten pixels.

The conversion in that view is `px = 160 + 10x` and `py = 109 - 10y`, with y
running upwards while pixels run down. The screen is 32 units across, x from
-16 to 16.

This is why a picture sized with the wrong form comes out ten times too big,
and why `GROBW` and `GROBW_P` disagree by a factor of ten on the same grob.
When you mean pixels, use the `_P` form.

What has not been measured is whether the factor follows a view the program
sets itself; everything here is the view before anything changes it.

**Evidence.** On the Virtual Calculator 2.4, build 2025-09-15:
`C→PX(0,0)` answers `{160,109}` and `C→PX(1,1)` answers `{170,99}`;
`PX→C(0,0)` answers `{-16,10.9}` and `PX→C(100,50)` answers `{-6,5.9}`;
a grob made `DIMGROB(G4,10,5,0)` measures 100 through `GROBW_P`
([results.tsv](../commands/results.tsv)).

<a name="interface.offscreen-grob"></a>
## Drawing straight onto the screen shows the work

| | |
|---|---|
| Identifier | `interface.offscreen-grob` |
| Kind | rule |
| Known from | G2 |

Rows appear one at a time and a redraw blinks. Draw into an off-screen grob
and copy the finished picture across in one go:

```ppl
DIMGROB_P(G1, 320, 240, 0);     // a canvas the size of the screen
// ... draw into G1 ...
BLIT_P(G0, G1);                 // one copy, one visible change
```

`G0` is the screen; `G1` through `G9` are yours.

**Evidence.** Measured on a G2 with firmware 2.4.15515. The Python equivalent,
`dimgrob` and `blit`, is read from a published toolkit rather than measured
here.

<a name="interface.two-themes"></a>
## There are two themes, and black on white is broken in one of them

| | |
|---|---|
| Identifier | `interface.two-themes` |
| Kind | rule |
| Known from | unverified |

The calculator has a light theme and a dark one. Published apps keep two sets
of colours -- background, foreground, selection, and one per state -- and pick
a set at startup.

**Evidence.** Read from published apps, not measured here. What would settle
it is one program drawing a fixed palette, looked at in both themes.

<a name="interface.textout-width"></a>
## TEXTOUT_P overflows unless you pass the width

| | |
|---|---|
| Identifier | `interface.textout-width` |
| Kind | rule |
| Known from | G2 |

The last argument is the maximum width in pixels. Without it, a long string is
written over the neighbouring column and keeps going until it runs off the
screen, and nothing raises an error: the calculator cuts the text or paints it
over something else, and you never learn what it said.

```ppl
TEXTOUT_P(txt, x, y, font, colour, width)          // clips at width
TEXTOUT_P(txt, G0, x, y, font, colour, width)      // clips at width
TEXTOUT_P(txt, x, y, font, colour)                 // runs off the screen
```

Three things close the hole: always pass the width; put long help text on its
own line with all 320 pixels; and keep a geometry module with no imports at
all, holding every column's `x`, so a PC test can check screen by screen that
each string fits. Character widths in such a test should be deliberate
over-estimates -- take the widest character -- so that when the test says it
fits, it fits.

**Evidence.** Measured on a G2 with firmware 2.4.15515 by drawing one long
string in the three forms above. `hpprime lint` catches the missing argument
in both forms, as `textout-width`.

<a name="interface.text-measure"></a>
## TEXTOUT_P returns the x where it finished, which is how text is measured

| | |
|---|---|
| Identifier | `interface.text-measure` |
| Kind | rule |
| Known from | unverified |

Drawing onto an off-screen grob and reading the return value gives the exact
width of a string, which no other call reports.

```python
def text_width(txt, fnt=2):
    dimgrob(9, 512, 22, 0)
    return eval('textout_p("' + txt + '",G9,0,0,0,0)')
```

**Evidence.** Read from the Markdown Viewer's source, which uses it that way.
Not measured here: one program drawing a known string and printing the return
value would settle it.

<a name="interface.input-fields"></a>
## What INPUT's field descriptions mean

| | |
|---|---|
| Identifier | `interface.input-fields` |
| Kind | rule |
| Known from | G2 |

`INPUT` returns 1 if accepted and 0 if cancelled. What is measured about its
fields:

| | |
|---|---|
| Field position | `{x%, width%, row}`, as a percentage of the screen |
| The label sits to the left of the field | at `x=5` labels came out clipped to a dot; at `x=22` they fit |
| Field type | `[0]` is real: the number is typed as it is, with no quotes |
| A text field demands quotes | typing `"0.2"` under exam pressure is a tax on every value |
| The variables must already exist, with the right type | |

The quotes detail decides whole interfaces. Given a choice between a form with
blank cells, which needs text fields and therefore quotes, and two drop-downs
plus two numeric fields, the drop-downs win: they say what you know, the
numeric fields say how much, and the label can show the unit.

**Evidence.** Measured on a G2 with firmware 2.4.15515, in an app in daily
use whose form has one drop-down and four fields over two rows.

<a name="interface.input-modal"></a>
## INPUT is modal and builds its labels once

| | |
|---|---|
| Identifier | `interface.input-modal` |
| Kind | rule |
| Known from | G2 |

A label that depends on another field of the same form cannot be refreshed
while the form is open. Offer fixed variants instead, or ask one field at a
time: a one-field `INPUT` can label itself with the unit for that particular
row, and lets somebody correct one value without walking through the other
nine.

**Evidence.** Measured on a G2 with firmware 2.4.15515.

<a name="interface.getkey-position"></a>
## GETKEY returns a position, not a character

| | |
|---|---|
| Identifier | `interface.getkey-position` |
| Kind | rule |
| Known from | G2 |

The code for `[Enter]` is 30, not 13. A code is a position, counted along the
keyboard from the top left, and the same code means different things in
different modes: 42 is `1` in normal mode and `y` in alpha mode.

**Evidence.** Measured on a G2 with firmware 2.4.15515, key by key.

<a name="interface.key-codes"></a>
## The 51 key codes, 0 to 50

| | |
|---|---|
| Identifier | `interface.key-codes` |
| Kind | rule |
| Known from | G2 |

| Where | Codes |
|---|---|
| top block | `Apps` 0, `Symb` 1, ▲ 2, `Help` 3, `Esc` 4 |
| | `Home` 5, `Plot` 6, ◄ 7, ► 8, `View` 9 |
| | `CAS` 10, `Num` 11, ▼ 12, `Menu` 13 |
| keypad, six wide | `Vars` 14, Mem 15, Units 16, `x t θ n` 17, `a b/c` 18, `Del` 19 |
| keypad, six wide | `x^y` 20, `SIN` 21, `COS` 22, `TAN` 23, `LN` 24, `LOG` 25 |
| keypad, five wide | `x²` 26, `+/-` 27, `( )` 28, `Eval` 29, `Enter` 30 |
| | `EEX` 31, `7` 32, `8` 33, `9` 34, `÷` 35 |
| | `ALPHA` 36, `4` 37, `5` 38, `6` 39, `×` 40 |
| | `Shift` 41, `1` 42, `2` 43, `3` 44, `−` 45 |
| | `On` 46, `0` 47, `.` 48, space 49, `+` 50 |

The rows are not all the same width: the two top rows of the white keypad have
six keys and the five below them have five, which is what puts `Del` at 19,
`Enter` at 30 and `+` last at 50. Design to fail quietly: send an unknown code
to the default case, and make that case harmless.

**Evidence.** Measured on a G2 with firmware 2.4.15515, key by key, 51 keys.
To read a code you did not expect, press the key:
`examples/keymap/` prints it.

<a name="interface.soft-labels-not-keys"></a>
## The six labels along the bottom are not keys

| | |
|---|---|
| Identifier | `interface.soft-labels-not-keys` |
| Kind | rule |
| Known from | G2 |

Touching them reports nothing through `GETKEY`: they are touch targets, and
touch arrives through `MOUSE`. What published apps call "soft keys 1..6" are
physical keys -- codes 0, 5, 10, 1, 6, 11, which is `Apps`, `Home`, `CAS`,
`Symb`, `Plot`, `Num`: the top-left 3×2 block, taken column by column. If your
program wants those labels driven from the keyboard as well as by finger, you
pick the physical keys yourself, and that block is what other people picked.

**Evidence.** Measured on a G2 with firmware 2.4.15515: touching the labels
produced no key code. The mapping is read from two published apps.

<a name="interface.draw-then-return"></a>
## A program that draws and returns loses its screen

| | |
|---|---|
| Identifier | `interface.draw-then-return` |
| Kind | rule |
| Known from | G2 |

Run a program from Home, have it draw with `TEXTOUT_P` and then `RETURN`, and
what you are left looking at is Home, with the return value. The drawing does
not survive the program ending, so anything meant to be read has to wait
before it returns. This is the first thing that goes wrong with a diagnostic
program, and it looks like the program did nothing at all.

What you are left with is a framed line in the Home history -- the program's
name and the value it returned -- or, when it was started from the Program
Catalog, a modal pop-up saying the same. It is not a message: it is the return
value, shown the way Home shows the value of anything you type.

Nothing suppresses it, because
[ppl.function-always-answers](ppl.md#ppl.function-always-answers): every
ending produces a number, so every one leaves a line. What you choose is what
the number says, not whether it appears.

**Evidence.** Measured on a G2 with firmware 2.4.15515, with five endings: an
assignment, a loop, an `IF` that does not run, a call, and a bare `RETURN;`.

<a name="interface.drain-then-wait"></a>
## Waiting for a key means draining the buffer first

| | |
|---|---|
| Identifier | `interface.drain-then-wait` |
| Kind | rule |
| Known from | G2 |

```ppl
EXPORT TPAUSE()
BEGIN
  LOCAL zk;
  REPEAT zk := GETKEY; UNTIL zk < 0;    // drain what is pending
  REPEAT zk := GETKEY; UNTIL zk >= 0;   // and only now wait
  RETURN zk;
END;
```

From Python the same principle, with `keyboard()` and `GETKEY()`.

**Evidence.** Measured on a G2 with firmware 2.4.15515: this waits where
`WAIT(-1)` did not, in a program called from another one.

<a name="interface.wait-minus-one"></a>
## Whether WAIT(-1) waits is contradicted by two measurements

| | |
|---|---|
| Identifier | `interface.wait-minus-one` |
| Kind | rule |
| Known from | unverified |

In one program `WAIT(-1)` did not wait: a results screen flashed past and the
form came straight back. In two published apps `WAIT(-1)` is the event loop,
returning a number for a key, a list for a touch, and −1 every 60 s. The
likeliest explanation is a key still pending in the buffer -- the one that had
just accepted an `INPUT` -- but that is a hypothesis. `WAIT(-1)` would use
less battery than
[interface.drain-then-wait](#interface.drain-then-wait) and delivers touches
in the same place; if you use it, check it yourself.

**Evidence.** The two readings above, which disagree. What would settle it:
the same program run with and without a key pressed just before the call.

<a name="interface.mouse-lists"></a>
## MOUSE returns lists inside lists

| | |
|---|---|
| Identifier | `interface.mouse-lists` |
| Kind | rule |
| Known from | G2 |

`{{x1,y1,x0,y0,type}, …}`. From Python it has to be flattened before it
crosses the bridge, because a list that is not all numbers closes the app
([micropython.md](micropython.md)):

```python
_MOUSE = ('LOCAL zm:=MOUSE; LOCAL zp:=zm(1);'
          ' IFTE(SIZE(zp)==0,{-1,-1,-1},{zp(1),zp(2),zp(5)})')
```

**Evidence.** Measured on a G2 with firmware 2.4.15515, in an app that reads
touch from Python.

<a name="interface.touch-readings"></a>
## A touch reading is not an event

| | |
|---|---|
| Identifier | `interface.touch-readings` |
| Kind | rule |
| Known from | unverified |

Three jobs raw readings leave to you. The coordinates need their sign fixed,
with `(c + 2**63) % 2**64 - 2**63`, which is an unsigned 64-bit value turned
signed; without it you get astronomically large numbers instead of a position
off the edge. `MOUSE` tells you what is happening now and cannot tell a finger
that has just landed from one that has been there half a second, so a layer
keeps the previous reading and derives `down`, a fresh `tap`, and `dx`/`dy`
for a drag. And a tap is reported once, on release: `tap and not down`, true
in exactly one update.

**Evidence.** Read from a published Python library's source, not measured
here. Its debounce was arrived at independently by another author, which is
a fair sign it is not optional.

<a name="interface.dialog-touch-twice"></a>
## The touch that closes a dialog arrives again underneath

| | |
|---|---|
| Identifier | `interface.dialog-touch-twice` |
| Kind | rule |
| Known from | G2 |

The Prime's dialogs, `INPUT` and notices, are accepted with an OK button that
falls on top of the soft-key row, in the F6 position. If your finger is still
there when the dialog closes, the same touch arrives at the screen underneath,
as though you had pressed its F6.

The fix is a debounce with memory, and it belongs in the pure-logic module
rather than the pixel one, precisely so that it can be tested on the PC: count
the screen as touched when a dialog closes, and pass only on the first contact
of a new touch. Call that purge on closing any dialog and on returning from
any screen, so that no single place can forget. It solves two things at once:
the screen is read dozens of times a second while a finger stays down, and the
touch that closes a dialog outlives the dialog.

**Evidence.** Measured on a G2 with firmware 2.4.15515, in an app whose menu
acted on the touch that had just dismissed a notice.

<a name="interface.screen-capacity"></a>
## About 20 rows of 40 characters fit in the small font

| | |
|---|---|
| Identifier | `interface.screen-capacity` |
| Kind | rule |
| Known from | unverified |

Use it to rule a design out before drawing it, not to call one good.

**Evidence.** An estimate from the font sizes, not a measurement.
[interface.text-measure](#interface.text-measure) is how it would be measured
for real.
