# 2. Your first program

From an empty folder to a function running on the calculator. Seven steps, five
of them on your PC.

---

## Step 1 — write it

You do not need an editor on the calculator. A PPL program is text.

```bash
hpprime new CIRCLE
```

That writes `CIRCLE.txt`. Open it: it is a working program, not a stub.

```ppl
EXPORT AREA(zr)
BEGIN
  RETURN 3.14159265359 * zr * zr;
END;

EXPORT MAIN()
BEGIN
  LOCAL zr;
  zr := 1;
  INPUT(zr, "CIRCLE", "radius:");
  MSGBOX("area = " + STRING(AREA(zr)));
  RETURN AREA(zr);
END;
```

Five rules of the language are already in those lines: `EXPORT` so the function
is visible from outside the file, the `LOCAL`s together at the top, `:=` to
assign and `==` to compare, `END` to close any block, and the final `;` after
it.

The split between the two functions is the point of the file. `AREA` is pure
arithmetic and `MAIN` talks to the screen, so everything on the `AREA` side can
be tested on your PC. Keeping that line as the program grows is what makes this
platform workable.

## Step 2 — lint it, before compiling anything

```bash
hpprime lint CIRCLE.txt
```

This catches what the Prime's compiler will not explain. Every rule comes from
an error measured on a real calculator: too many variables in one `LOCAL`,
`ENDIF`, comparing with `=`, index 0, a `LOCAL` half way down a function. Fix
whatever it reports now. On the calculator the same mistake costs a round trip.

## Step 3 — run it, on your PC

```bash
hpprime run CIRCLE.txt --call "AREA(2)"
```

You should get `12.5663706144`. This runs the same file you are going to
install, not a reimplementation of it, so what you see here is what it will do
there.

Try the interface half too:

```bash
hpprime run CIRCLE.txt --call "MAIN()"
```

It runs, and returns the area for the default radius. `INPUT` and `MSGBOX` are
not drawn, because there is no screen here. They are recorded and return a
neutral value, so the calculation runs without an interface. See
[what can and cannot be tested](../topics/interface.md#what-the-design-of-a-screen-comes-down-to).

## Step 4 — turn it into a `.hpprgm`

```bash
hpprime write CIRCLE.txt -o CIRCLE.hpprgm
```

`.hpprgm` is a binary container, with the source inside it verbatim. The tool
builds one from the code template the kit ships, and reads it back to check
before reporting success.

## Step 5 — put it on the calculator

1. Connect the calculator, or open the Virtual Calculator, and open the
   Connectivity Kit.
2. Drag `CIRCLE.hpprgm` from your file manager onto the calculator in the CK
   window.

> Do not copy it into the mirror folder. It looks like a mailbox and it is not:
> on connecting, the CK overwrites it with whatever is on the calculator, and
> your file disappears.

If the drag shows the no-entry cursor and nothing happens, the file is not the
problem. Check whether the CK is set to run as administrator: Windows does not
allow dragging from an unelevated process into an elevated window. The detail,
and a ten-second test, are in [deploy.md](../topics/deploy.md).

## Step 6 — run it there

There is nothing to compile. A program you have just dragged over runs as it
is.

On the Home screen, type the function name and its arguments:

```
AREA(2)
```

and press `[Enter]`. You should get 12.566…

Then run the interface half, and note the missing parentheses:

```
MAIN
```

> On Home, a function with no arguments is called without parentheses. `MAIN()`
> answers *syntax error*; `MAIN` runs it. Inside your source the parentheses are
> correct, and `AREA(zr)` is called normally from `MAIN`, so this is a Home
> rule rather than a PPL rule.
> ([Detail and evidence](../topics/ppl.md#ppl.home-no-parentheses).)

It is the first failure most people meet, and it is not in your program.

## Step 7 — check that you installed what you think you did

It costs one command:

```bash
hpprime read ".../Calculators/HP Prime/CIRCLE.hpprgm" -o installed.txt
diff installed.txt CIRCLE.txt
```

The check is what catches a calculator that has been running an old version for
weeks. The only expected difference is the trailing newline: the CK stores the
editor's buffer, which has none.

---

## What will break on your first day

All of this is measured, and each one costs at least one round trip:

| What you do | What happens | The right way |
|---|---|---|
| `LOCAL a,b,c,d,e,f,g,h,i,j;` | *syntax error* on that line | 7-8 per statement at most; use groups of 6 |
| `L(0)` | run-time error | everything starts at 1, not 0 |
| `IF x = 1 THEN` | does not compare, or compares wrong | `==` to compare, `:=` to assign |
| `ENDIF`, `ENDFOR` | *syntax error* | `END` for everything |
| `n := SIZE(M)(1);` | *syntax error* | `d := DIM(M);` then `d(1)` |
| declaring a `LOCAL` half way down | *syntax error* | all of them at the top, together |
| `MYFUNC()` on Home | *syntax error* | no parentheses on Home when there are no arguments |
| a program that draws, then returns | you see Home and the result, not the drawing | wait for a key before returning |
| copying the file into the mirror | nothing gets installed | drag it in the CK window |
| passing a big matrix to a function | it crawls | matrices are copied by value: use a global |

One ordering rule surprises people: a program only sees another's functions if
it was compiled afterwards. If you have data, engine and app, install them in
that order.

`hpprime lint` catches the first six before you open the CK. The last four
cannot be seen from a file.

## When something does not add up

The method matters more than the tools:

> Do not reason about the syntax. Measure programs that already work on that
> same calculator, and compare.

The limit on variables per `LOCAL` cost five compile-and-look rounds, because
the error did not move and every hypothesis looked reasonable. What settled it
was tabulating the programs that did compile and counting their locals.

Two consequences:

- An error that does not move after a fix means your hypothesis is false, not
  that the fix was too small.
- Download somebody else's program and read it.
  [hpcalc.org](https://www.hpcalc.org/prime/) is full of code that runs on real
  calculators. The event loop, the key codes and the menu geometry in this kit
  all come from there.

---

Next: [3. Asking for data and drawing](03-input-screen.md).
