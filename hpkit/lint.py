# -*- coding: utf-8 -*-
"""HP PPL linter: catches, before you compile, what the Prime's compiler
refuses to explain.

The Prime's compiler prints `syntax error` and points at a line. It does not
say what is wrong with it, so a mistake as small as one variable too many in
a LOCAL statement costs several compile-and-look rounds. Every rule here
comes from an error measured on a real calculator, not from reading a manual.

    hpprime lint FILE.hpprgm [more files or folders...]
    hpprime lint ppl/ --quiet      # errors only, no warnings
    hpprime lint A.txt B.txt --set # the files go onto the calculator
                                   # together: exported names that would
                                   # clash, and calls none of them defines

Output is compiler-shaped:  file:line: level: rule: message
Exit code 1 if there is any ERROR.

A call to a name that is not a PPL name, from the documentation's list in
docs/commands/names.tsv, and that the program does not define is flagged as
unknown-name: a warning for a file on its own, because it may be calling a
function another program exports, and an error with --set, where all the
files that go together are in view.

What this deliberately does NOT flag, because each was checked on hardware
and found legal:

  - RETURN inside a FOR or a REPEAT.
  - locals made of letter + digit (r2, y1, L12).
  - several locals given initial values on one line.

They are listed so nobody "fixes" them back in.
"""
from __future__ import unicode_literals
import io, os, re, sys

# Variables per LOCAL statement. Measured on a G2, firmware 2.4.15515,
# against programs that compile on that same calculator: 8 declared in one
# statement compiles; the functions that failed declared 13, 16 and 18.
# Above 8 is an error; 7-8 is the risky band.
LOCAL_SAFE = 6
LOCAL_MAX = 8

BAD_BLOCK_ENDS = ('ENDIF', 'ENDFOR', 'ENDWHILE', 'ENDCASE', 'ENDPROC',
                  'ENDFUNC')
KEYWORDS = set("""IF THEN ELSE END FOR FROM TO DOWNTO STEP DO WHILE REPEAT
UNTIL CASE DEFAULT BREAK CONTINUE RETURN LOCAL EXPORT BEGIN AND OR NOT
IFTE""".split())

# The calculator's own variables: A to Z, θ, and the numbered lists,
# matrices, graphics and complex variables.
CALC_VARIABLE = re.compile(r'^([A-Z]|θ|[LMGZ][0-9])$')

# A name as the calculator writes it. Some of its own names carry an arrow --
# C→PX, PX→C, →HMS, B→R -- and the arrow is part of the name, not an operator
# (PPL assigns with :=). A rule that matches a name has to admit it: with
# [A-Za-z_]\w* the match starts after the arrow, so C→PX(0,0) reads as an
# index 0 into a variable PX and the rule fires on correct code.
NAME = r'[A-Za-z_→][\w→]*'
NOT_NAME = r'(?<![\w→])'

_KNOWN = None


def known_names():
    """Every name on the documentation's list, lower case, or an empty set
    if the list is not there. Compared without regard to case, so that no
    spelling the calculator might accept is flagged; whether the calculator
    itself ignores case in its names has not been measured."""
    global _KNOWN
    if _KNOWN is None:
        try:
            from hpkit import names
        except ImportError:                      # run as hpkit/lint.py
            sys.path.insert(0, os.path.dirname(os.path.dirname(
                os.path.abspath(__file__))))
            from hpkit import names
        _KNOWN = names.known()
    return _KNOWN


def is_known(name, defined):
    """Is `name` something a call may use: the program's own, a keyword, a
    calculator variable, or a name on the list?"""
    return (name in defined or name.upper() in KEYWORDS
            or CALC_VARIABLE.match(name) is not None
            or name.lower() in known_names())


# Every rule says which fact in docs/topics/ it comes from, so that a message
# can be checked rather than believed. A rule that comes from something else
# says what, rather than borrowing a fact that does not fit.
# tests/test_lint.py holds both halves to the topic pages.
FACTS = {
    'single-end': 'ppl.no-end-keywords',
    'index-call': 'ppl.index-call',
    'one-based': 'ppl.one-based',
    'local-limit': 'ppl.local-limit',
    'local-first': 'ppl.locals-at-top',
    'export-multiple': 'ppl.export-initialised',
    'expr-empty': 'ppl.expr-empty',
    'textout-width': 'interface.textout-width',
    'end-semicolon': 'ppl.end-semicolon',
    'export-clash': 'ppl.global-namespace',
}

NO_FACT = {
    'unbalanced': 'a block left open, which the compiler reports itself: no '
                  'fact about the platform is involved',
    'unknown-name': 'the list of names in docs/commands/names.tsv, which is '
                    'an inventory and not a fact about the platform',
}


class Finding(object):
    def __init__(self, path, line, level, rule, msg):
        self.path, self.line = path, line
        self.level, self.rule, self.msg = level, rule, msg

    @property
    def fact(self):
        """The identifier of the fact the rule comes from, or '' when the
        rule comes from something else: NO_FACT says what."""
        return FACTS.get(self.rule, '')

    def __str__(self):
        fact = ' [%s]' % self.fact if self.fact else ''
        return '%s:%d: %s: %s: %s%s' % (self.path, self.line, self.level,
                                        self.rule, self.msg, fact)


def _strip_noise(line):
    """Drop comments and string contents, keeping the quotes.

    This stops rules from firing on text that is only a message for the user.
    Returns the line with its string literals emptied."""
    out, i, n, in_str = [], 0, len(line), False
    while i < n:
        c = line[i]
        if in_str:
            if c == '"':
                in_str = False
                out.append('"')
            i += 1
            continue
        if c == '"':
            in_str = True
            out.append('"')
            i += 1
            continue
        if c == '/' and i + 1 < n and line[i + 1] == '/':
            break
        out.append(c)
        i += 1
    return ''.join(out)


def _strip_block_comments(text):
    """Blank out /* ... */ comments, keeping their line breaks so that line
    numbers stay right."""
    out, i, n, in_str = [], 0, len(text), False
    while i < n:
        c = text[i]
        if not in_str and text.startswith('/*', i):
            j = text.find('*/', i + 2)
            j = n if j < 0 else j + 2
            out.append(''.join('\n' if ch == '\n' else ' '
                               for ch in text[i:j]))
            i = j
            continue
        if c == '"':
            in_str = not in_str
        elif c == '\n':
            in_str = False
        out.append(c)
        i += 1
    return ''.join(out)


def _split_top_level(s):
    """Split on commas that are not inside (), {} or [].

    Brackets and braces matter: EXPORT NAMES:={"a","b","c"}; is ONE variable,
    not three, and counting its commas used to raise a false alarm."""
    parts, depth, cur = [], 0, []
    for c in s:
        if c in '({[':
            depth += 1
        elif c in ')}]':
            depth -= 1
        if c == ',' and depth == 0:
            parts.append(''.join(cur))
            cur = []
        else:
            cur.append(c)
    parts.append(''.join(cur))
    return [p.strip() for p in parts if p.strip()]


def _call_args(line, open_idx):
    """The text between a call's parentheses, or None if they do not close on
    this line.

    Lines are judged one at a time, so a call spanning several of them is
    left alone rather than guessed at: a false alarm teaches people to
    ignore the linter."""
    depth = 0
    for i in range(open_idx, len(line)):
        c = line[i]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return line[open_idx + 1:i]
    return None


def _block_delta(up):
    """How much a line opens blocks (BEGIN THEN DO CASE) against END."""
    opens = len(re.findall(r'\b(BEGIN|THEN|DO|CASE)\b', up))
    return opens - len(re.findall(r'\bEND\b', up))


def scan_names(text):
    """-> (the names a program defines, [(name, line) for every call]).

    Defined: its functions, exported or not, with their parameters; its
    LOCAL and EXPORT variables; any other global it declares at the top.
    A call is NAME( in code, outside strings, comments and #pragma lines."""
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    lines = [_strip_noise(l) for l in _strip_block_comments(text).split('\n')]
    defined, calls, depth = set(), [], 0
    for k, raw in enumerate(lines):
        s = raw.strip()
        if not s or s.startswith('#'):
            continue
        up = s.upper()
        header = None
        if depth <= 0:
            m = re.match(r'^(?:EXPORT\s+|KEY\s+)?([A-Za-z_]\w*)\s*\(([^()]*)\)',
                         s, re.I)
            if m and m.group(1).upper() not in KEYWORDS:
                header = m.group(1)
                defined.add(header)
                for p in _split_top_level(m.group(2)):
                    pm = re.match(r'^([A-Za-z_]\w*)', p)
                    if pm:
                        defined.add(pm.group(1))
            elif not re.match(r'^(BEGIN|LOCAL)\b', up):
                body = re.sub(r'^EXPORT\s+', '', s, flags=re.I).split(';')[0]
                for part in _split_top_level(body):
                    pm = re.match(r'^([A-Za-z_]\w*)\s*(:=|$)', part)
                    if pm:
                        defined.add(pm.group(1))
        if re.match(r'^LOCAL\b', up):
            for part in _split_top_level(s[5:].split(';')[0]):
                pm = re.match(r'^([A-Za-z_]\w*)', part)
                if pm:
                    defined.add(pm.group(1))
        for m in re.finditer(NOT_NAME + r'(%s)\s*\(' % NAME, raw):
            if m.group(1) == header and m.start() == raw.find(header):
                continue                     # the definition, not a call
            calls.append((m.group(1), k + 1))
        depth += _block_delta(up)
    return defined, calls


def check_source(path, text):
    """-> (list of Finding, list of (exported name, line))."""
    found = []
    lines = text.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    clean = [_strip_noise(l) for l in lines]

    exports = []
    in_body = False         # inside a function's BEGIN ... END
    seen_code = False
    depth = 0

    for k, raw in enumerate(clean):
        num = k + 1
        s = raw.strip()
        if not s:
            continue
        up = s.upper()

        # ---- ENDIF and friends -------------------------------------------
        for bad in BAD_BLOCK_ENDS:
            if re.search(r'\b%s\b' % bad, up):
                found.append(Finding(path, num, 'ERROR', 'single-end',
                                     '%s does not exist in PPL: every block '
                                     'closes with END' % bad))

        # ---- indexing the result of a call --------------------------------
        for m in re.finditer(NOT_NAME + r'(%s)\s*\([^()]*\)\s*\(' % NAME, raw):
            if m.group(1).upper() not in KEYWORDS:
                found.append(Finding(path, num, 'ERROR', 'index-call',
                                     'cannot index the result of a call '
                                     '(%s(...)(...)): store it first, '
                                     'd := DIM(M); d(1)' % m.group(1)))

        # ---- index 0 into a list or matrix --------------------------------
        # A 0 passed to one of the calculator's own names (RGB(0, ...)) is
        # an argument, not an index: those names come from the list. That is
        # also why the name has to be read with the arrow in it (NAME): a
        # screen point is counted from 0, and C→PX(0,0) is correct code.
        for m in re.finditer(NOT_NAME + r'(%s)\s*\(\s*0\s*[,)]' % NAME, raw):
            name = m.group(1)
            if name.upper() not in KEYWORDS \
                    and name.lower() not in known_names():
                found.append(Finding(path, num, 'ERROR', 'one-based',
                                     'index 0 into %s: PPL lists and matrices '
                                     'start at 1' % name))

        # ---- LOCAL: how many variables, and where -------------------------
        if re.match(r'^LOCAL\b', up):
            body = s[5:].split(';')[0]
            nv = len(_split_top_level(body))
            if nv > LOCAL_MAX:
                found.append(Finding(path, num, 'ERROR', 'local-limit',
                                     '%d variables in one LOCAL; the most '
                                     'seen to compile is %d. Split it into '
                                     'several LOCAL statements of %d'
                                     % (nv, LOCAL_MAX, LOCAL_SAFE)))
            elif nv > LOCAL_SAFE:
                found.append(Finding(path, num, 'WARN', 'local-limit',
                                     '%d variables in one LOCAL: this is the '
                                     'limit (7-8 depending on firmware). '
                                     'Groups of %d are safe'
                                     % (nv, LOCAL_SAFE)))
            if in_body and seen_code:
                found.append(Finding(path, num, 'ERROR', 'local-first',
                                     'LOCAL after code: every local goes '
                                     'together at the top of the BEGIN'))
        elif in_body and not up.startswith('BEGIN'):
            seen_code = True

        # ---- EXPORT with several initialised variables --------------------
        if re.match(r'^EXPORT\b', up) and ':=' in s \
                and '(' not in s.split(':=')[0]:
            chunks = _split_top_level(s[6:].split(';')[0])
            valued = [t for t in chunks if ':=' in t]
            if len(chunks) > 1 and valued:
                found.append(Finding(path, num, 'ERROR', 'export-multiple',
                                     'several variables with initial values '
                                     'in one EXPORT: one declaration per '
                                     'line'))

        # ---- exported names, to cross-check between files -----------------
        m = re.match(r'^EXPORT\s+([A-Za-z_]\w*)', s, re.I)
        if m:
            exports.append((m.group(1), num))

        # A rule called `equality` used to sit here, flagging a single = in
        # an IF, WHILE or UNTIL condition as an error. It was measured on
        # 2026-09-12 and it was wrong: IF a = 2 THEN compiles and compares,
        # exactly as == does, on the Virtual Calculator 2.4 build 2025-09-15
        # (ppl.equality-operators). A linter that flags legal, correct code
        # is worse than one rule short, so it went. What nobody has measured
        # is a bare = as a STATEMENT -- a = 2; where a := 2; was meant -- and
        # a rule for that has to wait for the measurement, not the other way
        # round.

        # ---- EXPR on a variable without checking it is not empty ----------
        for m in re.finditer(r'\bEXPR\s*\(\s*([A-Za-z_]\w*)\s*\)', raw, re.I):
            window = ' '.join(clean[max(0, k - 6):k]).upper()
            if 'SIZE(%s)' % m.group(1).upper() not in window.replace(' ', ''):
                found.append(Finding(path, num, 'WARN', 'expr-empty',
                                     'EXPR(%s) without checking SIZE(%s) > 0 '
                                     'first: EXPR("") fails at run time'
                                     % (m.group(1), m.group(1))))

        # ---- TEXTOUT_P without its width argument -------------------------
        # The trap it guards: text that does not fit raises no error. It is
        # painted over the next column and you never learn what it said.
        #
        # Both forms are judged. Measured on a G2, drawing one long string
        # three times: with no width it runs off the screen, and these two
        # clip it identically --
        #     TEXTOUT_P(txt, x, y, font, colour, width)        6 arguments
        #     TEXTOUT_P(txt, G0, x, y, font, colour, width)    7 arguments
        # so the width is the last argument of whichever form is in use.
        for m in re.finditer(r'\bTEXTOUT_P\s*\(', raw, re.I):
            args = _call_args(raw, m.end() - 1)
            if args is None:
                continue
            parts = _split_top_level(args)
            grob = len(parts) > 1 and re.match(r'^G\d$', parts[1].strip(),
                                               re.I)
            if len(parts) < (7 if grob else 6):
                found.append(Finding(path, num, 'WARN', 'textout-width',
                                     'TEXTOUT_P without its width argument: '
                                     'text that does not fit is painted over '
                                     'the next column, and raises no error'))

        # ---- block balance -------------------------------------------------
        if re.match(r'^BEGIN\b', up):
            in_body, seen_code = True, False
        depth += _block_delta(up)
        if in_body and depth <= 0:
            in_body = False
        # a function's END without its semicolon
        if re.match(r'^END\s*$', s):
            found.append(Finding(path, num, 'ERROR', 'end-semicolon',
                                 'END without ; at the end: in PPL it is '
                                 'END;'))

    if depth != 0:
        found.append(Finding(path, len(lines), 'ERROR', 'unbalanced',
                             'unclosed blocks: %d openings too many '
                             '(BEGIN/THEN/DO/CASE against END)' % depth))

    # ---- names that are neither PPL's nor this file's ----------------------
    # Only when the list is there to say what PPL's names are.
    if known_names():
        defined, calls = scan_names(text)
        for name, num in calls:
            if not is_known(name, defined):
                found.append(Finding(path, num, 'WARN', 'unknown-name',
                                     '%s is not a PPL name, and this file '
                                     'does not define it. If another program '
                                     'exports it, lint them together with '
                                     '--set' % name))

    return found, exports


def lint_files(paths, as_set=False):
    """-> (the files read, every Finding), printing nothing."""
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, fs in os.walk(p):
                for f in sorted(fs):
                    if f.endswith(('.hpprgm', '.ppl', '.txt')):
                        files.append(os.path.join(root, f))
        else:
            files.append(p)

    everything, all_exports, texts = [], {}, []
    for f in files:
        try:
            txt = io.open(f, encoding='utf-8').read()
        except (IOError, UnicodeDecodeError) as e:
            print('%s: cannot read (%s)' % (f, e))
            continue
        found, exports = check_source(os.path.relpath(f), txt)
        if as_set:
            # With every file in view, a stranger is decided below, for the
            # whole set at once.
            found = [a for a in found if a.rule != 'unknown-name']
        everything.extend(found)
        texts.append((os.path.relpath(f), txt))
        for name, line in exports:
            all_exports.setdefault(name, []).append((os.path.relpath(f), line))

    # The same exported name in two files: they clash as globals. Only with
    # --set, because it is normal to keep variants of the same code that are
    # never installed together. --set is how you say "these do go together".
    for name, places in sorted(all_exports.items()) if as_set else []:
        others = set(s[0] for s in places)
        if len(others) > 1:
            f, l = places[0]
            everything.append(Finding(f, l, 'ERROR', 'export-clash',
                                      '%s is also exported by %s: exported '
                                      'names are global and collide'
                                      % (name,
                                         ', '.join(sorted(others - {f})))))

    # A call none of the files defines, and that is not a PPL name: with the
    # whole set in view, nothing else could supply it.
    if as_set and known_names():
        scans = [(f, scan_names(t)) for f, t in texts]
        defined = set()
        for _, (d, _) in scans:
            defined |= d
        for f, (_, calls) in scans:
            for name, line in calls:
                if not is_known(name, defined):
                    everything.append(Finding(f, line, 'ERROR',
                                              'unknown-name',
                                              '%s is not a PPL name, and none '
                                              'of these files defines it'
                                              % name))

    return files, everything


def check_files(paths, quiet=False, as_set=False):
    """Lint, print compiler-shaped findings, and -> 1 if any is an error."""
    files, everything = lint_files(paths, as_set)
    errors = [a for a in everything if a.level == 'ERROR']
    warnings = [a for a in everything if a.level != 'ERROR']
    for a in sorted(everything, key=lambda a: (a.path, a.line)):
        if quiet and a.level != 'ERROR':
            continue
        print(str(a))
    print('\n%d file(s): %d error(s), %d warning(s)'
          % (len(files), len(errors), len(warnings)))
    return 1 if errors else 0


def cli(argv):
    args = [a for a in argv if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 2
    return check_files(args, quiet='--quiet' in argv, as_set='--set' in argv)


if __name__ == '__main__':
    sys.exit(cli(sys.argv[1:]))
