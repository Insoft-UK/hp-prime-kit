# hp-prime-kit

## What This Is

Two layers in one repository, built in this order:

1. **The documentation.** A reference for programming the HP Prime in PPL,
   command by command, plus the platform topics a program runs into: the
   limits that break compilation, the screen and keyboard, apps, Python, the
   file formats, and getting code onto the calculator. Every entry says how it
   is known: measured on a calculator, run on the Virtual Calculator, taken
   from HP's own help, or not verified. It is written for models and people
   alike. Each entry stands on its own and has an identifier, so a model can
   load only what it needs, and the whole still reads well from start to
   finish.
2. **The agent kit**, built on that documentation. It is installed into Claude
   Code and gives the agent one procedure per job, specialised roles, and
   checks it cannot skip. It cites the documentation by identifier instead of
   restating it. The Python tools (lint, run, write, install, compare) sit
   between the two layers: they make the documentation checkable, and they are
   the gates the agent works through.

In the user's words: "documentación para LLMs", "para quien no sabe, pero
también para los que saben".

## Core Value

Everything the documentation says about the Prime states how it is known, and
the agents built on it never claim more than it does.

**Done when:**

- **Milestone 1, the documentation:** every PPL command has an entry with its
  syntax, its behaviour, an example and its status; every fact measured so far
  is there with an identifier; and `hpprime lint` flags a command that does
  not exist.
- **Milestone 2, the agent kit:** with a fresh Claude Code session on the
  installed kit, somebody who has never programmed a Prime has their program
  working on the calculator without reading any PPL, and an app the size of
  TermoHP (an engine, several screens, a large data set) is built from
  scratch.

## Requirements

### Validated

Inferred from the existing repository, and added phase by phase.

- ✓ `hpprime lint`: twelve rules, each from an error measured on a G2 — existing
- ✓ `hpprime run`: runs the real PPL file on the PC, and raises instead of inventing a result — existing
- ✓ `hpprime write` / `read` / `verify`: the `.hpprgm` container in both directions — existing
- ✓ `hpprime build` / `verify`: `.hpappdir` apps, PPL and Python — existing
- ✓ `hpprime install` / `pull` / `emu`: the Virtual Calculator's folder as a real mailbox, and throwaway calculators — existing
- ✓ `hpprime compare`: the same calls on the PC and on the calculator, side by side — existing
- ✓ `hpprime matrix`, `doctor`, `new`, `templates` — existing
- ✓ Measured reference for PPL, interface, libraries, apps, MicroPython, formats and deploy, every fact with its evidence or marked Unverified — existing
- ✓ HP's own help examples as test data for the interpreter (`tests/hp_examples.txt`) — existing
- ✓ Run on a real G2: a program built from the shipped template, and a PPL app built by `hpprime build --ppl` — existing
- ✓ One documented format for command entries, facts and examples, held by `hpprime docs` and `tests/test_reference.py` in both directions — Phase 1
- ✓ Examples of the commands the interpreter implements run through it in the tests; a different answer fails, an uncovered one is a note — Phase 1
- ✓ The group pages and the index are generated from the entries, and a stale one fails the tests — Phase 1
- ✓ The documentation does not refer to the kit, and a test checks it — Phase 1
- ✓ The list of every PPL name as data: 1,173 names from HP's help of 13217, the 2.1.14181 export and the release notes to 2.4.15515, each saying where it came from — Phase 2
- ✓ An index by name and one by HP's grouping, over every name that gets an entry, generated from the list — Phase 2
- ✓ `hpprime lint` flags a call to a name that is neither PPL's nor the program's (`unknown-name`): a warning alone, an error with `--set` — Phase 2
- ✓ The tools find a Connectivity Kit and a Virtual Calculator whose folders are localised, and say which folder they used — Phase 3
- ✓ The examples of a batch of entries run on the Virtual Calculator in one pass, every kind of answer comes back, and each is stored with its firmware — Phase 3
- ✓ The container reader's wrong pick between two source records ending at the same offset, reproduced in a test and fixed — Phase 3
- ✓ The platform topics carried over in the fixed format, none lost: every fact with an identifier, one statement, how it is known and its evidence, the refuted hypotheses and the unverified items included — Phase 4
- ✓ Every lint message names the fact it comes from, and the deploy page explains the send from the Connectivity Kit by hand, marked as done once — Phase 4
- ✓ An entry for every statement and program command, every Home function and every app function, each example with a Virtual Calculator result or a reason — Phases 5 to 7

### Active: Milestone 1, the documentation

Numbered in `REQUIREMENTS.md`.

- [ ] An entry for every PPL statement, command, Home function, app function, app variable and variable, and for `GET`: syntax, what it does, its arguments and what it returns, an example, the known edge cases, and its status. Done through the app functions; the app variables are Phase 8, the variables and `GET` Phase 8.1
- [ ] Every example is run on the Virtual Calculator 2.4.15515, or says why it cannot be
- [ ] A person can learn from zero with a guided path and look anything up in the reference
- [ ] A model can load one entry or one topic without the rest, from an index

### Active: Milestone 2, the agent kit, built on the documentation

Deferred in `REQUIREMENTS.md`; planned when milestone 1 is done.

- [ ] One command installs the kit into Claude Code, and the agent picks it up without being told
- [ ] One entry point per job (new program, port, debug, screen, app, deploy, measure), each a short procedure that loads only the entries that job needs
- [ ] Specialised agents: one writes, another verifies and assumes nothing works until a command shows it does
- [ ] Agent reports and lint messages cite the documentation's identifiers instead of paraphrasing, and a test checks that every citation resolves
- [ ] The checks run by themselves through Claude Code hooks, not only when the agent remembers them
- [ ] A fixed hand-over for what only the human can do: what was built, the exact keys to press, the values to expect, and what to report back
- [ ] A beginner can start from an idea, and the agent asks what it needs before writing any PPL
- [ ] A project too big for one session, TermoHP's size, can be built across sessions: the plan and the state live in files, and each step is checked before the next one starts
- [ ] An expert can use the tools and the documentation directly, without going through the agent's procedures
- [ ] A block to paste into a chat with no file access, generated from the documentation
- [ ] The interpreter grows to cover what the kit's programs use, each builtin measured first

### Out of Scope

- CAS commands — the choice was PPL command by command, not the whole platform. They are on the list for the linter, and can be a later milestone
- How-to guides, explanation pages and a Spanish version — not chosen for milestone 1; the guided path and the reference cover what a person needs, and a second language doubles the maintenance of every page
- Growing the interpreter in milestone 1 — the user's choice: it only learns the list of names; it grows in milestone 2
- Automating the keypresses on the emulator — the user's choice for Phase 3: the user presses them, a few batches in all
- Two repositories — one repository with two layers. The documentation can be split out later with `git subtree split`, history included, if it gains contributors of its own
- Rewriting the Python tools — they are validated; they change only where the new structure needs them to
- Other agents (Codex, Cursor, Copilot and the rest) — the kit targets Claude Code only. The content stays in one source so a converter can be added later
- Automating the send to a physical calculator — the user's decision: explain it, do not automate it. It has worked once, after five attempts
- A Node.js installer or dependency — the kit is Python 3.7+ standard library only, and this machine has no Node
- Becoming a GSD capability — it would need Node and GSD installed; the kit learns from GSD instead of depending on it. Can be revisited
- Drawing the interface on the PC, and running MicroPython on the PC — unchanged from today
- Project-specific content such as TermoHP — house rule: examples stay generic. A TermoHP-sized app is a test of the kit, built outside it

## Context

- **Origin.** The kit came out of building TermoHP, a thermodynamic-tables app
  for the G2, with an AI agent doing the coding.
- **The problem it answers.** There is little public PPL for a model to learn
  from, what exists contradicts itself across firmware versions and older HP
  calculators, and the compiler says only "syntax error" and a line number.
  Models answer with `ENDIF`, 0-based indexing and commands that do not exist.
- **The shape before the redo.** A human-oriented tutorial (a six-step guided
  path in plain prose) plus a Python CLI, with `AGENTS.md`, `SKILL.md` and
  `docs/ai/prompts.md` as the AI layer. It documented only what was measured
  and the traps, not the command set. The user's judgement on 2026-09-11: that
  shape did not capture what the kit is for, and the documentation has to come
  first.
- **The size of the command set.** `docs/commands/names.tsv` holds 1,173
  names: 706 get an entry (14 statements, 98 commands, 177 functions, 179 app
  functions, 172 app variables, 65 variables, and `GET`, of unknown kind); the
  436 CAS names, 7 keywords and 24 operators are on it for the linter and are
  not documented one by one. 1,116 come from HP's help of 13217, 50 only from
  the 2.1.14181 export, and 7 only from the release notes up to 2.4.15515.
- **Sources for the command reference.** HP's built-in help (the `[Help]` key)
  and its Command Tree dump; the 2.1.14181 export of the command tree; the
  release notes of every firmware to 2.4.15515; HP's Programming Reference and
  User Guide; and programs that already run. The help covers edges unevenly
  (`RIGHT` and `MID` say nothing about theirs) and says nothing about the
  limits that break compilation, which is why the kit measures.
- **This machine.** Connectivity Kit 2.4 with a Spanish interface: its folders
  are `Calculadoras`, `Contenido` and so on, and `hpprime doctor` has found
  them since Phase 3 taught the tools the localised names. The Virtual Calculator
  2.4 r15515, the same build as the reference G2, has been installed since
  2026-09-11; its calculators folder is `Calculators`, in English, although its
  other folders are Spanish, and the kit finds it. A program copied into that
  folder has to be compiled once, with the editor's Check, before its name
  works on Home (measured on 2026-09-06).
- **What to learn from.** GSD Core (open-gsd/gsd-core): documentation split
  into tutorials, how-to guides, reference and explanation; facts as one-line
  predicates that are cited, not paraphrased; thin entry points that load
  references only when a step needs them; specialised agents with a fresh
  context each; claim provenance tags; gates decided by external signals
  rather than the model's confidence; formal human checkpoints; questioning
  before building; state kept in files so work survives across sessions.
- **Findings not yet written into the documentation.**
  - The container reader could pick the wrong source record when two
    candidates end at the same offset (`program._source_record`), seen in
    TermoHP with a 65,515-character source. Already fixed on 2026-09-10
    (cd14080), with a test over the five sizes that used to trip it; this
    document said otherwise until Phase 3 looked.
  - The kit's starter program exports a function called `AREA`, which is also
    the name of a Function app function. What the calculator does with that
    has not been measured.
- **Reference firmware.** G2, 2.4 revision 15515. There are no G1 measurements.

## Constraints

- **Direction**: the documentation never depends on the kit; the kit depends on the documentation — so the documentation stands on its own and can be split out
- **Evidence**: every entry states how it is known: measured on a G2 (what was run, on which firmware, what was seen), run on the Virtual Calculator, taken from HP's help, or unverified — the whole value is that it can be trusted
- **Own words**: entries are written in the kit's words, and HP's help is cited, not copied, with at most a short quotation — it is HP's text and the repository is MIT. HP's sources are read outside the repository
- **Tech stack**: Python 3.7+, standard library only, no install step for the tools — anybody with a fresh clone and a stock Python has to be able to run everything
- **Agent**: Claude Code for the kit — skills, agents and hooks in its native format
- **Language**: English in the repository (code, docs, commits); the agent answers the user in the user's language
- **Platforms**: Windows first, because that is where the emulator and the Connectivity Kit run; macOS and Linux for everything that does not need them
- **One fact, one home**: each fact is stated once and cited everywhere else
- **Git**: `main` is the published branch, and nothing is pushed to it without asking. The redo was built on a local branch, `redo`, which became `main` on 2026-09-14

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Documentation first, then the agent kit built on it | The user's correction on 2026-09-11 | — Pending |
| One repository, two layers | Chosen on 2026-09-11: a fact, its lint rule and its test change together; one clone gives everything; the documentation can be split out later | ✓ Good (Phases 1-2) |
| The documentation covers every PPL command, plus the platform topics | The user's choice on 2026-09-11; with the full list, the linter can flag invented commands | ✓ Good: the list exists and lint reads it (Phase 2) |
| The documentation is written for models and people alike | The user's choice on 2026-09-11 | — Pending |
| One Markdown file per command, with the group pages and the index generated | The user's choice for Phase 1 | ✓ Good (Phase 1) |
| The mixed entry: a summary, fixed fields, labelled examples, a short behaviour section | The user's choice for Phase 1, from three mockups | ✓ Good (Phase 1) |
| Examples are verified on the Virtual Calculator 2.4.15515 | The user's choice on 2026-09-11: closer to the hardware than the kit's own interpreter. Installed on 2026-09-11 | — Pending |
| The user presses the keys on the emulator; the kit prints them, waits and collects | The user's choice for Phase 3: the measured path, a few batches in all | — Pending |
| Examples run on a throwaway calculator, Prime_1, reset before each batch | The user's choice for Phase 3: a known state for every result, and the user's own calculator untouched. The name is the emulator's, not ours: the second window it opens is always Prime_1, and never a calculator called anything else | — Pending |
| An example the emulator confirms goes from `HP help` to `emulator`; a disagreement is flagged, never replaced | The user's choice for Phase 3 | — Pending |
| The interpreter does not grow in milestone 1; it only learns the list of names | The user's choice on 2026-09-11 | ✓ Good: lint reads the list (Phase 2) |
| For people, milestone 1 has the guided path and the reference, nothing more | The user's choice on 2026-09-11 | — Pending |
| App variables get entries, in their own phase after the app functions | The user's choice on 2026-09-11 | — Pending |
| The list of names comes from HP's own sources, rebuilt by a maintainer's script; the sources stay outside the repository | Downloaded on 2026-09-11 with the user's permission | ✓ Good (Phase 2) |
| CAS names are on the list, known to the linter, not documented | CAS is out of scope, but a program may call it | ✓ Good (Phase 2) |
| `unknown-name` is a warning for a file alone and an error with `--set` | The user's choice for Phase 2: a file may call another program's export | ✓ Good (Phase 2) |
| The linter compares the calculator's names without regard to case | Never flag a spelling the calculator might accept; the calculator's own behaviour is not measured | — Pending |
| Keep the measured facts and the Python tools; redo the structure, the docs and the entry points | They are validated on hardware; the problem is the shape, not the content | ✓ Good so far |
| The redo happens on a local branch `redo` | The user's choice on 2026-09-11: `main` stays intact until the redo is ready | ✓ Good: `main` moved to it by fast-forward on 2026-09-14 |
| The kit targets Claude Code only, with the content kept in one source | The user's choice on 2026-09-11; Claude Code has skills, agents and hooks natively | — Pending |
| The send to a physical calculator is explained, not automated | The user's choice on 2026-09-11; one run, five attempts | — Pending |
| Done means: every PPL command documented; then a beginner succeeds end to end and a TermoHP-sized app is built from scratch | The user's choices on 2026-09-11 | — Pending |
| Learn from GSD, do not depend on it | No Node on this machine, and the kit stays standard-library only | ✓ Good so far |
| Build the redo with GSD's method: `.planning/` with PROJECT, REQUIREMENTS, ROADMAP and STATE, one phase at a time | The user asked to use GSD to capture what they want | ✓ Good: it surfaced the "documentation first" correction |
| The 65 variables and `GET` get their own phase, 8.1, inside milestone 1 | The user's choice on 2026-09-16, when Phase 9's questioning found that no phase had taken them | — Pending |
| Phase 9 runs ahead of Phases 8 and 8.1 | The user's choice on 2026-09-16: what it builds is generated from the entries or links to them | — Pending |
| The index a model loads first is one file with a link on every line | The user's choice on 2026-09-16, over the same list without links and over a map with an index per group | — Pending |
| The guided path keeps its six steps, rewritten to link rather than restate | The user's choice on 2026-09-16, over a shorter path and over a new structure | — Pending |
| Planning language comes out of the documentation, and a check keeps it out | The user's choice on 2026-09-16; harness, batch and probe are explained once instead | ✓ Good: 132 rewrites, and the check refuses "phase" and "this kit" (09-02) |
| The model index is `docs/llms.txt`, generated, with a budget of 100,000 bytes the check enforces | Approved with Phase 9's context on 2026-09-16: inside `docs/` so the documentation can still be split out, and loaded whole, so its size is watched | ✓ Good: 74,939 bytes for 598 entries and 117 facts (09-01) |
| An example nobody has run fails the check | Approved on 2026-09-16 (CHECK-02): no stored answer is allowed only for *no value*, a G2 measurement, or the interpreter | ✓ Good: it reports nothing today, and holds that (09-01) |
| `--relabel` moves `unverified` to `emulator` too, never `G2` | Approved on 2026-09-16: a label weaker than the measurement understates it as surely as a stronger one overstates it | ✓ Good: 21 examples moved, and a fact measured in Phase 5 and never written down was settled with them (09-01) |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition:**
1. Requirements invalidated? → Move to Out of Scope with the reason
2. Requirements validated? → Move to Validated with a phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update it if it has drifted

**After each milestone:**
1. Full review of all sections
2. Core Value check: still the right priority?
3. Audit Out of Scope: are the reasons still valid?
4. Update Context with the current state

---
*Last updated: 2026-09-16, when Phase 9 was questioned and Phase 8.1 inserted*
