# Migration list: the seven reference pages

Every section of `docs/reference/` and where it went. A row is finished when
its destination says a fact identifier, a page and section that holds it as
prose, or why it was dropped. No row may stay blank: that is what FACT-01
asks for.

53 sections across seven pages: `ppl` 6, `formats` 7, `deploy` 8,
`interface` 12, `apps` 9, `micropython` 7, `libraries` 4.

Plan 04-01 fills `ppl` and `formats`; 04-02 `interface`, `apps` and
`micropython`; 04-03 `deploy` and `libraries`.

## ppl.md — plan 04-01

| Section | Went to |
|---|---|
| (page head) Reference firmware, and "start with the guided path" | prose, the introduction of `docs/topics/ppl.md` |
| 1. The limits that actually break | `ppl.local-limit`, `ppl.index-call`, `ppl.export-initialised`, `ppl.locals-at-top`, `ppl.no-end-keywords` |
| 1.x Indexing a global from another program: not a rule | `ppl.global-index-other-program`, with the two hypotheses and the four programs that would settle it |
| 2. Hypotheses that turned out FALSE | `ppl.return-in-loop`, `ppl.letter-digit-names`, `ppl.local-m-matrices`, `ppl.locals-initialised-one-line`, `ppl.i-e-as-locals` |
| 3. The syntax, briefly | prose, "The shape of a program", plus `ppl.type-codes` for the TYPE table |
| 4. Run-time traps, the language ones | `ppl.matrices-by-value`, `ppl.expr-empty`, `ppl.expr-dynamic-access`, `ppl.global-namespace`, `ppl.decimal-point`, `ppl.compilation-order`, `ppl.getkey-no-parentheses` |
| 4. Run-time traps, the ones about a command that has an entry | already stated in the entry: `LEFT(s,0)` and `RIGHT(s,0)` in `docs/commands/strings/`, `MID`'s length of 0 in `MID.md`, `SIZE` of a matrix in `list/SIZE.md` |
| 4. Run-time traps, `INSTRING` | to `INSTRING`'s entry, Phase 6. Recorded here so it cannot be lost: `INSTRING` answers 0 when it finds nothing, and 1 when the second argument is empty (G2, firmware 2.4.15515) |
| 4. Run-time traps, `INPUT` builds its labels once, and `WAIT(-1)` answers a key position | to the `interface` topic, plan 04-02 |
| 4. Run-time traps, a blank app and what an app's program exports | to the `apps` topic, plan 04-02 |
| 4. Run-time traps, global state in a library | to the `libraries` topic, plan 04-03 |
| 4.x A function always answers something | `ppl.function-always-answers` |
| 4.y Calling a function from Home | `ppl.home-no-parentheses` |
| 5. Speed: the one anchor there is | `ppl.speed-anchor`; the 0.2 ms bridge crossing and MicroPython's own unmeasured speed go to the `micropython` topic, plan 04-02 |
| 6. Where to look things up | prose, "Where to look things up" in the introduction, the AI-agent note included |

## formats.md — plan 04-01

| Section | Went to |
|---|---|
| (page head) What this page is, and that HP documents none of it | prose, the introduction of `docs/topics/formats.md` |
| 1. The `.hpprgm` container | `formats.container`, `formats.source-record`, `formats.wrapper-trap`, `formats.trailer-varies`, `formats.header-words`, `formats.line-endings` |
| 2. The compiled block | `formats.source-offset-152`, `formats.two-producers`, `formats.block-is-a-cache`, `formats.block-not-byte-stable`. The unverified parts -- when the rebuild happens, how long a large one takes -- are inside `formats.block-is-a-cache`, which says so |
| 3. The internal number | `formats.number`, with the Rosetta stone counts as its evidence |
| 4. What that opens: `.hpmat` | `formats.hpmat`, `formats.hpmat-vector`; the command lines are prose in the introduction |
| 5. Inside the block: the symbol entries | `formats.symbol-table`, `formats.matrix-type-byte`, `formats.value-types-undecoded`, `formats.matrix-flag`, `formats.entry-splice`. The u32 at offset 44 is folded into `formats.header-words`, which is the same word from the other end; the size of a generated data program into `formats.block-is-a-cache` |
| 6. Other files on the calculator | `formats.other-files` |
| 7. How this is verified | prose, "How this is verified" in the introduction, with the six round-trip results |

## deploy.md — plan 04-03

| Section | Went to |
|---|---|
| 1. The emulator: a folder that really is a mailbox | `deploy.emulator-folder`, `deploy.compile-once-after-a-file-copy`, `deploy.results-come-back-on-exit`, `deploy.which-window-opens`, `deploy.calc-hpsettings-moves`; the macOS and Linux note is inside the first one's evidence |
| 2. The folder that looks like a mailbox and is not | `deploy.ck-mirror`, `deploy.usb-without-the-ck`; the three-step procedure is prose in the introduction |
| 3. If the drag is refused with the no-entry cursor | `deploy.drag-refused-when-elevated` |
| 4. You do not have to compile it | `deploy.no-manual-compile`, with the reported large-program exception inside it |
| 5. Do not trust that you installed it: read it back | `deploy.read-it-back` |
| 6. The writer, validated against hardware | `deploy.writer-on-hardware` |
| 7. Getting a template, which is not as easy as it sounds | `deploy.template-from-the-ck` |
| 8. Which calculator is which | `deploy.which-calculator-is-which` |

## interface.md — plan 04-02

| Section | Went to |
|---|---|
| 1. The geometry | `interface.geometry` |
| 2. The building blocks | prose, "The building blocks"; `interface.offscreen-grob` for the flicker, `interface.two-themes` for the themes; the update-then-draw loop is prose under "What the design of a screen comes down to" |
| 3. `TEXTOUT_P` overflows unless you pass the width | `interface.textout-width`, `interface.text-measure`. To `TEXTOUT_P`'s entry in Phase 6, which will link here rather than restate it |
| 4. `INPUT`: what to know before designing around it | `interface.input-fields`, `interface.input-modal`; the one-field form is prose |
| 5. The keyboard | `interface.getkey-position`, `interface.key-codes`, `interface.soft-labels-not-keys`, `interface.draw-then-return`, `interface.drain-then-wait`, `interface.wait-minus-one`. The blank-app paragraph went to `apps.blank-app-keys`, where it belongs |
| 6. Touch, and the touch that arrives twice | `interface.mouse-lists`, `interface.touch-readings`, `interface.dialog-touch-twice` |
| 7. One widget for everything: the windowed list | prose, "What the design of a screen comes down to": it is judgement, and the behaviours are copied from named apps |
| 8. A table needs no sentinels; a form does | prose, same section |
| 9. Units are not asked for; they are stated | prose, same section |
| 10. What can be tested on the PC, and what cannot | prose, same section; the row-capacity estimate is `interface.screen-capacity` |
| 11. Somebody may have written it already | prose, the pointer to libraries at the end of that section |
| 12. Where this comes from | prose, "Where this comes from", with the seven apps named |

## apps.md — plan 04-02

| Section | Went to |
|---|---|
| 1. What is inside a `.hpappdir` | `apps.hpappdir-contents` |
| 2. The startup-view byte | `apps.startup-view-byte` |
| 3. The icon | `apps.icon` |
| 4. The two kinds of app | `apps.two-kinds` |
| 5. PPL apps: the hooks, and the blank-app trap | `apps.hooks`, `apps.blank-app-hooks`, `apps.blank-app-keys`, `apps.exports-tied`; the launcher pattern is prose |
| 6. Python apps: how one is put together | `apps.wrappers-are-portable`, `apps.main-py`; the file-by-file structure is prose in `micropython`'s "The architecture that makes this useful", and the imports and `__pycache__` rules are `micropython.imports` |
| 7. Installing | `apps.install` |
| 8. Generating and checking it from the PC | `apps.generated-and-verified`; the command lines are prose |
| 9. What is not solved | `apps.hpapp-not-generated`, `apps.empty-hpappprgm-not-a-template`; the compiled-block part points at `formats.source-offset-152` |

## micropython.md — plan 04-02

| Section | Went to |
|---|---|
| 1. What is there and what is not | `micropython.modules`, `micropython.community-modules` |
| 2. The `hpprime` module | `micropython.hpprime-module`, `micropython.hpprime-undocumented` |
| 3. The bridge: `eval()` | `micropython.eval`, `micropython.eval-parentheses`, `micropython.list-with-string-closes-the-app`, `micropython.string-quotes`, `micropython.number-notation`, `micropython.bridge-cost` |
| 4. The architecture that makes this useful | prose, "The architecture that makes this useful"; the imports rule is `micropython.imports` |
| 5. Debugging when the app closes by itself | `micropython.mark-debugging` |
| 6. From PPL into Python | `micropython.ppl-calls-python` |
| 7. Still not measured | `micropython.not-measured` |

## libraries.md — plan 04-03

| Section | Went to |
|---|---|
| 1. Which level | prose, "Which level"; the two rows worth expanding link to `interface.input-fields` and `interface.input-modal` instead of restating them |
| 2. Using somebody else's library | prose, "Using somebody else's library"; the two rules it rests on are `ppl.global-namespace` and `ppl.compilation-order`, linked rather than repeated |
| 3. What the published ones give you | `libraries.published`, `libraries.skeletonapp-container`, `libraries.usb-keyboard` |
| 4. When to write your own | prose, "When to write your own" |
