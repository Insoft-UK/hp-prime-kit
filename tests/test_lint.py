# -*- coding: utf-8 -*-
"""Linter tests: that it catches what it must, and stays quiet on good code.

The bad cases are real errors that cost compile rounds on the calculator.
The controls are code that DOES compile on a G2 and that was wrongly
suspected at some point: if the linter flags them, the linter is wrong.

    python tests/test_lint.py
"""
from __future__ import unicode_literals
import io, os, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from hpkit import lint as L                                   # noqa: E402

# ------------------------------------------------------------- bad cases
BAD = [
    ('local-limit', """
EXPORT F(a)
BEGIN
  LOCAL zm, zn, zi, zj, zk, zp, zq, zr, zs, zt, zu, zv, zw;
  RETURN a;
END;
"""),
    ('index-call', """
EXPORT F(M)
BEGIN
  LOCAL n;
  n := SIZE(M)(1);
  RETURN n;
END;
"""),
    ('export-multiple', """
EXPORT A:=1, B:=2, C:=3, D:=4, E:=5, F:=6, G:=7;
"""),
    ('single-end', """
EXPORT F(a)
BEGIN
  IF a > 0 THEN a := 1; ENDIF;
  RETURN a;
END;
"""),
    ('one-based', """
EXPORT F(M)
BEGIN
  RETURN M(0,1);
END;
"""),
    ('local-first', """
EXPORT F(a)
BEGIN
  LOCAL x;
  x := a + 1;
  LOCAL y;
  RETURN x;
END;
"""),
    ('unbalanced', """
EXPORT F(a)
BEGIN
  IF a > 0 THEN
    a := 1;
  RETURN a;
END;
"""),
    ('expr-empty', """
EXPORT F()
BEGIN
  LOCAL zs;
  zs := "";
  RETURN EXPR(zs);
END;
"""),
    ('textout-width', """
EXPORT F()
BEGIN
  TEXTOUT_P("a label that may not fit", G0, 4, 24, 2, RGB(0,0,0));
  RETURN 1;
END;
"""),
    ('textout-width', """
EXPORT F()
BEGIN
  TEXTOUT_P("a label that may not fit", 4, 24, 2, RGB(0,0,0));
  RETURN 1;
END;
"""),
    # The command a model invents: there is no STRLEN in PPL.
    ('unknown-name', """
EXPORT F(zs)
BEGIN
  RETURN STRLEN(zs);
END;
"""),
]

# -------------------------------------------------------------- controls
# Code that compiles on a real G2. No rule may fire on any of these.
GOOD = [
    ('RETURN inside a FOR', """
EXPORT F(n)
BEGIN
  LOCAL zi;
  FOR zi FROM 1 TO n DO
    IF zi > 3 THEN RETURN zi; END;
  END;
  RETURN 0;
END;
"""),
    ('locals of letter + digit', """
EXPORT F()
BEGIN
  LOCAL L12, L13, L14, r2, y1;
  L12 := 1;
  RETURN L12;
END;
"""),
    ('several locals with initial values', """
EXPORT F()
BEGIN
  LOCAL x1:=160, x2:=299, x3:=21;
  RETURN x1;
END;
"""),
    ('builtin called with a 0 argument', """
EXPORT F()
BEGIN
  TEXTOUT_P("hello", 4, 24, 3, RGB(0,0,180));
  RETURN 1;
END;
"""),
    # The arrow is part of the name. Read without it, C→PX(0,0) looks like an
    # index 0 into a variable PX, and one-based fired on correct code.
    ('a name with an arrow in it, called with 0', """
EXPORT F()
BEGIN
  LOCAL zp;
  zp := C→PX(0,0);
  RETURN zp;
END;
"""),
    ('exported list with commas in it', """
EXPORT LABELS:={"one","two","three","four","five","six","seven","eight"};
"""),
    ('EXPR behind a size guard', """
EXPORT F(zs)
BEGIN
  IF SIZE(zs) > 0 THEN
    RETURN EXPR(zs);
  END;
  RETURN 0;
END;
"""),
    ('TEXTOUT_P with its width argument', """
EXPORT F()
BEGIN
  TEXTOUT_P("a label", G0, 4, 24, 2, RGB(0,0,0), 70);
  RETURN 1;
END;
"""),
    ('TEXTOUT_P in the short form, with its width', """
EXPORT F()
BEGIN
  TEXTOUT_P("a label", 4, 24, 2, RGB(0,0,0), 70);
  RETURN 1;
END;
"""),
    ('a TEXTOUT_P call spanning two lines', """
EXPORT F()
BEGIN
  TEXTOUT_P("a label", G0, 4,
            24, 2, RGB(0,0,0), 70);
  RETURN 1;
END;
"""),
    ('8 locals, the most seen to compile', """
EXPORT F()
BEGIN
  LOCAL a, b, c, d, e2, f, g, h;
  RETURN 1;
END;
"""),
]

# ------------------------------------------------ names that are not strangers
# Every call in these is to a name PPL has or the program defines, so
# unknown-name must not appear at all, not even as a warning.
KNOWN_NAMES = [
    ('its own functions, exported or not, defined before or after', """
F2(za)
BEGIN
  RETURN za;
END;

EXPORT F(za)
BEGIN
  RETURN F2(za) + F3(za);
END;

F3(zb)
BEGIN
  RETURN zb;
END;
"""),
    ('a parameter and a local, indexed', """
EXPORT F(zl)
BEGIN
  LOCAL zm;
  zm := {1,2};
  RETURN zl(1) + zm(2);
END;
"""),
    ('an exported variable, indexed', """
EXPORT ZDATA:={1,2,3};
EXPORT F()
BEGIN
  RETURN ZDATA(2);
END;
"""),
    ("the calculator's own variables", """
EXPORT F()
BEGIN
  L1 := {1,2};
  M1 := [[1,2],[3,4]];
  RETURN L1(2) + M1(1,2) + A;
END;
"""),
    ('an app function, with and without its app', """
EXPORT F()
BEGIN
  RETURN AREA(1,2) + Function.AREA(1,2);
END;
"""),
    ('a CAS name', """
EXPORT F(zx)
BEGIN
  RETURN simplify(zx) + expand(zx);
END;
"""),
    ("the calculator's names in lower case", """
EXPORT F(zx)
BEGIN
  RETURN sin(zx) + size({1,2});
END;
"""),
    ('a forward declaration', """
F2();
EXPORT F()
BEGIN
  RETURN F2();
END;
F2()
BEGIN
  RETURN 1;
END;
"""),
    ('a #pragma line', """
#pragma mode( separator(.,;) integer(h32) )
EXPORT F()
BEGIN
  RETURN 1;
END;
"""),
    ('a call inside a block comment', """
/* STRLEN(s) would be wrong,
   but this is a comment */
EXPORT F()
BEGIN
  RETURN 1;
END;
"""),
    ('a call inside a string', """
EXPORT F()
BEGIN
  MSGBOX("STRLEN(s) is not a command");
  RETURN 1;
END;
"""),
]

# ------------------------------------------------------------ files together
LIBRARY = """
EXPORT ZLIB(zx)
BEGIN
  RETURN zx * 2;
END;
"""
CALLER = """
EXPORT F()
BEGIN
  RETURN ZLIB(21);
END;
"""
STRANGER = """
EXPORT F(zs)
BEGIN
  RETURN STRLEN(zs);
END;
"""


def lint_files(sources, as_set):
    """Lint (name, source) pairs as files. -> every Finding."""
    tmp = tempfile.mkdtemp(prefix='hplint-')
    try:
        paths = []
        for name, src in sources:
            path = os.path.join(tmp, name)
            with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(src)
            paths.append(path)
        return L.lint_files(paths, as_set=as_set)[1]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def levels(found, rule):
    return sorted(set(a.level for a in found if a.rule == rule))


SETS = [
    ('a stranger in a file on its own is a warning',
     lambda: levels(lint_files([('A.txt', STRANGER)], False),
                    'unknown-name') == ['WARN']),
    ('a stranger with --set is an error',
     lambda: levels(lint_files([('A.txt', STRANGER)], True),
                    'unknown-name') == ['ERROR']),
    ('a call to another file\'s export warns when the file is alone',
     lambda: levels(lint_files([('B.txt', CALLER)], False),
                    'unknown-name') == ['WARN']),
    ('and is quiet with --set, when that file is in view',
     lambda: levels(lint_files([('A.txt', LIBRARY), ('B.txt', CALLER)],
                               True), 'unknown-name') == []),
]


def kit_sources():
    """The PPL this repository ships for people to copy."""
    out = []
    for base in ('examples', 'templates'):
        for folder, _, files in os.walk(os.path.join(ROOT, base)):
            out += [os.path.join(folder, f) for f in sorted(files)
                    if f.endswith('.txt')]
    return out


def rules_cite_facts():
    """-> the problems with what each rule says it comes from.

    Every rule the linter can emit either names a fact that a topic page
    defines, or says in NO_FACT what it comes from instead. A rule that does
    neither is a message nobody can check.
    """
    import re
    from hpkit import docs as D
    src = io.open(os.path.join(ROOT, 'hpkit', 'lint.py'),
                  encoding='utf-8').read()
    rules = set(re.findall(r"'(?:ERROR|WARN)',\s*'([a-z-]+)'", src))
    facts = set(f.ident for f in D.load(ROOT)[1])
    problems = []
    for rule in sorted(rules):
        if rule in L.FACTS and rule in L.NO_FACT:
            problems.append('%s is in both FACTS and NO_FACT' % rule)
        elif rule in L.FACTS:
            if L.FACTS[rule] not in facts:
                problems.append('%s names %s, which no topic page defines'
                                % (rule, L.FACTS[rule]))
        elif rule in L.NO_FACT:
            if not L.NO_FACT[rule].strip():
                problems.append('%s gives no reason for having no fact' % rule)
        else:
            problems.append('%s names no fact and gives no reason' % rule)
    for rule in sorted(set(L.FACTS) | set(L.NO_FACT)):
        if rule not in rules:
            problems.append('%s is mapped, and the linter never emits it'
                            % rule)
    return problems


def main():
    ok = bad = 0

    for rule, src in BAD:
        found, _ = L.check_source('case.hpprgm', src)
        rules = set(a.rule for a in found)
        if rule in rules:
            ok += 1
            print('  ok    catches %-20s' % rule)
        else:
            bad += 1
            print('  FAIL  misses %-20s (got: %s)'
                  % (rule, ', '.join(sorted(rules)) or 'nothing'))

    print('')
    for name, src in GOOD:
        found, _ = L.check_source('good.hpprgm', src)
        errors = [a for a in found if a.level == 'ERROR']
        if not errors:
            ok += 1
            print('  ok    quiet on %s' % name)
        else:
            bad += 1
            print('  FAIL  false alarm on %s: %s'
                  % (name, '; '.join(a.rule for a in errors)))

    print('')
    for name, src in KNOWN_NAMES:
        found, _ = L.check_source('names.hpprgm', src)
        strangers = [a for a in found if a.rule == 'unknown-name']
        if not strangers:
            ok += 1
            print('  ok    no unknown-name on %s' % name)
        else:
            bad += 1
            print('  FAIL  unknown-name on %s: %s'
                  % (name, '; '.join(a.msg.split(' ')[0] for a in strangers)))

    print('')
    for name, test in SETS:
        if test():
            ok += 1
            print('  ok    %s' % name)
        else:
            bad += 1
            print('  FAIL  %s' % name)

    print('')
    flagged = []
    for path in kit_sources():
        text = io.open(path, encoding='utf-8').read()
        flagged += ['%s:%d %s' % (os.path.relpath(path, ROOT), a.line,
                                  a.msg.split(' ')[0])
                    for a in L.check_source(path, text)[0]
                    if a.rule == 'unknown-name']
    if flagged:
        bad += 1
        print('  FAIL  unknown-name in the PPL this repository ships: %s'
              % '; '.join(flagged))
    else:
        ok += 1
        print('  ok    no unknown-name in the PPL this repository ships')

    print('')
    problems = rules_cite_facts()
    if problems:
        bad += 1
        print('  FAIL  rules against facts: %s' % '; '.join(problems))
    else:
        ok += 1
        print('  ok    every rule names its fact, or says what it comes from')

    print('\nPASS: %d   FAIL: %d' % (ok, bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
