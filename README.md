# hp-prime-kit

Write programs and apps for the HP Prime on a PC, check them there, and only
then put them on the calculator. It works the same whether you write the code
yourself or with an AI assistant.

The Prime is programmable and thinly documented. Its compiler reports `syntax
error` and a line number and nothing else; a Python app that does something it
dislikes closes with no message. The usual way round that is to paste code into
the Connectivity Kit, compile, look at the calculator and repeat. An assistant
does not shorten it: there is little PPL in public code for a model to have
learned from, so it invents syntax that reads well and does not compile.

This kit replaces that loop. You write the code on the PC, lint it, run it and
build the binary there, and the platform facts you both work from are ones that
were measured on a calculator.

Python 3.7 or newer. No dependencies, nothing to install.

---

## Start

```bash
git clone https://github.com/JordiRigau/hp-prime-kit
cd hp-prime-kit
python hpprime.py doctor          # is this machine ready?
```

The whole cycle is five commands, run from that folder. They are written here
the short way: `.\hpprime` in PowerShell, `./hpprime` on macOS and Linux, or
`python hpprime.py` anywhere.

```bash
hpprime new CIRCLE                     # a starter that already runs
hpprime lint CIRCLE.txt                # what the compiler will not explain
hpprime run  CIRCLE.txt --call "AREA(2)"   # run the real file, here
hpprime write CIRCLE.txt -o CIRCLE.hpprgm  # build the binary
hpprime install CIRCLE.hpprgm --restart    # into the emulator, and open it
```

The last line installs into the emulator and opens it, with nothing to drag. On
a physical calculator that step is still a drag onto it in the Connectivity Kit
window. [deploy.md](docs/topics/deploy.md) covers both.

New to the Prime: start at [the guided path](docs/start/01-setup.md), six steps
from an empty folder to a program running on the calculator.

Working with an AI: point it at [`AGENTS.md`](AGENTS.md) for Cursor, Copilot or
Codex, or at [`SKILL.md`](SKILL.md) for Claude Code. Both load the same rules.
If your assistant cannot read files, paste
[`docs/ai/prompts.md`](docs/ai/prompts.md) §1 instead.

## What is here

The guided path, in order:

| | |
|---|---|
| [1. What you are getting into](docs/start/01-setup.md) | the machine, the two languages, program against app, what to install |
| [2. Your first program](docs/start/02-first-program.md) | empty file to running on the calculator, and what breaks on the way |
| [3. Asking for data and drawing](docs/start/03-input-screen.md) | `INPUT`, keys, text that fits |
| [4. Wrapping it as an app](docs/start/04-first-app.md) | the icon, and the byte that decides which screen opens |
| [5. Moving to Python](docs/start/05-python.md) | the bridge to PPL, and two traps that cost a day each |
| [6. Working with an AI](docs/start/06-working-with-ai.md) | the loop, and what not to accept from a model |

The reference. Every claim in it says how it is known: measured on a G2, run
on HP's Virtual Calculator, taken from HP's help, or marked `unverified`. The
labels and the format are in [format.md](docs/format.md).

| | |
|---|---|
| [commands](docs/commands/index.md) | one entry per PPL name, 598 of them: syntax, examples with the calculator's own answers, and what models get wrong. 741 of the 800 examples were run on the Virtual Calculator, and its answers are kept in [results.tsv](docs/commands/results.tsv) |
| [ppl.md](docs/topics/ppl.md) | the language: the limits that break compilation, the hypotheses that look reasonable and are false, and what each one is known from |
| [interface.md](docs/topics/interface.md) | screen, keyboard and touch: `INPUT`, the key map, the touch that arrives twice |
| [libraries.md](docs/topics/libraries.md) | building an interface: which level a screen needs, and what the published libraries provide |
| [apps.md](docs/topics/apps.md) | the `.hpappdir`, the hooks, the startup-view byte |
| [micropython.md](docs/topics/micropython.md) | Python on the calculator, the bridge to PPL, and the call that closes the app |
| [formats.md](docs/topics/formats.md) | the binary container and the internal number format, both decoded, and what is still not |
| [deploy.md](docs/topics/deploy.md) | getting it onto the calculator: the emulator folder you can write into, and the two traps of the one you cannot |

The tools. One command, `hpprime`, [documented here](docs/tools.md):

| | |
|---|---|
| `hpprime doctor` | what works on this machine, and what to do about what does not |
| `hpprime new` | a starter that already compiles and runs |
| `hpprime lint` | twelve rules, each naming the fact it comes from, or saying what it comes from instead |
| `hpprime run` | runs PPL on your PC: the file you install, not a copy of it |
| `hpprime write` / `read` | the `.hpprgm` binary, both directions |
| `hpprime build` / `verify` | apps: build the folder, and catch it drifting |
| `hpprime install` / `pull` | into the emulator, and back out of it |
| `hpprime emu` | calculators to experiment on, and put back |
| `hpprime compare` | the same call here and on the calculator, side by side |
| `hpprime matrix` | `.hpmat` files: a whole matrix as a file, nothing pasted |
| `hpprime docs` / `examples` | the documentation held to its format, and its examples run on the Virtual Calculator |

## Running PPL on the PC

If the same calculation exists twice, in PPL for the calculator and in Python
to develop against, no ordinary test will tell you the two have drifted apart:
each is consistent with itself and both pass their own tests. Running the real
PPL and comparing the answers is what surfaces the difference, and the failures
cluster where one side forgot a case.

There is a runnable example, with a mode that introduces a divergence so you
can see what one looks like:

```bash
python examples/conformance/conformance.py --break
```

## What it does not do

- **Draw the interface.** `INPUT`, `CHOOSE`, `TEXTOUT_P` and the rest are
  recorded rather than painted, so a program with a screen runs end to end
  here, but seeing it needs the emulator.
- **Run MicroPython.** The `hpprime.eval` bridge exists only on the
  calculator. What you can do is write the engine so that the file which
  computes is the same file in both places; see
  [micropython.md](docs/topics/micropython.md).
- **Generate a program's compiled block**, which it does not need to. That
  block is a cache the calculator rebuilds from the source, measured by
  changing one number in it and watching the calculator put it back, so a
  program carrying data is generated like any other. How long a large one
  takes to compile on arrival has not been measured.
- **Install on a physical calculator.** That step is a drag onto the
  calculator in the Connectivity Kit window, and the CK's mirror folder is not
  a mailbox. The emulator is different: its folder is a real one, so
  `hpprime install` does the whole job
  ([evidence](docs/topics/deploy.md#deploy.emulator-folder)).
- **Replace testing on the calculator.** It cuts the number of round trips;
  the last one is still a real Prime. It can compare itself against one:
  `hpprime compare` runs the same calls in both places and brings the
  calculator's numbers back as a file.

## Status

Reference firmware: G2, 2.4 revision 15515 (2025-09-15). The examples run on
the Virtual Calculator 2.4, build 2025-09-15.

The command reference covers every statement, command and Home function, all
179 app functions, and 130 of the 172 app variables. The other 42 belong to six
apps and are next. The 65 Home variables, such as `HAngle`, have no entries
yet.

Both paths have been run on a real G2: a program built from the template this
repository ships
([evidence](docs/topics/deploy.md#deploy.writer-on-hardware)),
and an app built end to end by `hpprime build --ppl`
([evidence](docs/topics/apps.md#apps.generated-and-verified)).

```bash
python tests/run_all.py     # thirteen suites, none of them needs a calculator
```

Open, and listed here so that nobody relies on them:

| | |
|---|---|
| G1 | everything here is a G2. Same firmware, different hardware |
| MicroPython speed, and an app's memory limit | not measured. The bridge crossing is 0.2 ms |
| `.hplist` | lists as files are neither read nor written. Same family as `.hpmat`, with the type byte in the same slot, `0x16` against `0x14`, but every `.hplist` seen here is empty, and the format will not be guessed from those |

If you measure something new, or build something with this, see
[CONTRIBUTING.md](CONTRIBUTING.md). A fact with its evidence is welcome even if
the prose needs work.

## Licence

MIT. See [LICENSE](LICENSE).
