# -*- coding: utf-8 -*-
"""Rebuild tests/hp_examples.txt from HP's help dump.

    python tests/hp_examples_extract.py ct.txt > tests/hp_examples.txt

You only need this if HP publishes a newer dump; the tests themselves read
the versioned `hp_examples.txt` and need nothing but the standard library.

Getting the input, which is the one step that is not Python:

    curl -O https://www.hpcalc.org/prime/docs/commandtree.zip
    unzip commandtree.zip
    pdftotext -layout -enc UTF-8 "Command tree 13217.pdf" ct.txt

`pdftotext` comes with poppler. That is a one-off on a maintainer's machine,
not a dependency of the kit.

What it keeps: lines of the form `NAME(args) -> result` whose NAME is a
builtin the interpreter implements. It skips anything with a complex number
or a CAS object in it, because the interpreter does not cover those types at
all and 16 such cases would just be noise in the report.

Only the expression/result pairs are taken. HP's prose stays HP's.
"""
from __future__ import unicode_literals
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

ARROW = '→'
MINUS = '−'

# Complex numbers, roots, pi, CAS domains, and the symbolic lower-case
# examples: none of these is in the interpreter's scope.
OUT_OF_SCOPE = re.compile('[i√π]|DOM_|\\bx\\b')

HEADER = """\
# Examples from HP's own documentation, as test cases.
#
# Source: "Command Tree 13217", the calculator's built-in help tree extracted
# to PDF, published at https://www.hpcalc.org/prime/docs/ (commandtree.zip).
# It is the same text the [Help] key shows on the calculator.
#
# One case per line:   EXPRESSION | RESULT
#
# These are HP's stated results, not measurements taken here, and the dump is
# from firmware 13217 while this kit's reference is 2.4.15515. So a case that
# fails is a divergence to investigate, not automatically a bug in the
# interpreter -- but every one found so far was.
#
# Only the expression/result pairs are reproduced; the surrounding prose is
# HP's. Cases involving complex numbers or CAS objects are left out because
# the interpreter does not cover those types at all.
#
# Regenerate with tests/hp_examples_extract.py if HP publishes a newer dump.
"""


def extract(text, names):
    """-> sorted [(expression, result)], each seen once."""
    seen, out = set(), []
    for raw in text.split('\n'):
        line = ' '.join(raw.split())
        if line.count(ARROW) != 1:
            continue
        expression, _, result = line.partition(ARROW)
        expression, result = expression.strip(), result.strip()
        # HP appends an explanation to some examples, in lower case.
        result = re.sub(r'\s*\([a-z][^)]*\)\s*$', '', result)
        head = re.match(r'^([A-Z][A-Z_0-9]{1,14})\s*\(', expression)
        if not head or head.group(1) not in names:
            continue
        if OUT_OF_SCOPE.search(expression) or OUT_OF_SCOPE.search(result):
            continue
        # HP prints a typographic minus; the lexer only knows the ASCII one.
        expression = expression.replace(MINUS, '-')
        result = result.replace(MINUS, '-')
        if (expression, result) in seen:
            continue
        seen.add((expression, result))
        out.append((expression, result))
    return sorted(out, key=lambda p: (re.match(r'[A-Z_0-9]+', p[0]).group(0),
                                      p[0]))


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    from hpkit import interp
    text = io.open(argv[0], encoding='utf-8').read()
    cases = extract(text, set(interp.BUILTINS))
    sys.stdout.write(HEADER + '\n')
    for expression, result in cases:
        sys.stdout.write('%s | %s\n' % (expression, result))
    sys.stderr.write('%d case(s)\n' % len(cases))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
