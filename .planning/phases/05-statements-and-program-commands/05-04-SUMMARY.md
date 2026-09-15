---
phase: 05-statements-and-program-commands
plan: 04
status: complete
completed: 2026-09-12
key_files:
  - docs/commands/io/*.md
  - docs/commands/app/*.md
commits: ["Eleven entries for the commands that wait for a person"]
---

# Plan 04 summary: the commands that talk to a person

## What was built

- The 10 `io` entries: `CHOOSE`, `CHOOSEDATE`, `EDITLIST`, `GETKEY`, `INPUT`,
  `ISKEYDOWN`, `MOUSE`, `MSGBOX`, `PRINT`, `WAIT`.
- The 3 `app` entries: `STARTAPP`, `STARTVIEW`, `VIEW`.
- Each links to what `docs/topics/interface.md` already holds about it:
  `interface.input-fields`, `interface.input-modal`,
  `interface.dialog-touch-twice` and the rest.

## What this turned up

**Almost every entry here has `*no value*` in its Result column**, and that
is the honest answer rather than a gap. A batch has nobody to press a key, so
what `INPUT` gives back when somebody answers it -- 1 accepted, 0 cancelled --
comes from the G2 and says so, while the call itself has no answer a batch
could store.

The distinction the plan asked for holds: an entry says which of the two it
is. `EDITLIST` cannot be run at all; `MSGBOX` can be called and simply waits.
Both get `*no value*`, and the paragraph underneath says which.

## Deviations

- The plan expected 82 entries in the documentation at this point. The count
  is what the inventory gives, not what the plan estimated, and the estimate
  was not corrected as earlier plans landed.

## Results

```
hpprime docs --check      0 problems
io                        10 of 10
app                       3 of 3
```
