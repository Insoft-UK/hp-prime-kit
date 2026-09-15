# -*- coding: utf-8 -*-
"""Tests for comparing the PC interpreter against the calculator.

No calculator here either. The half that runs on the Prime is a matrix, and
a matrix is a file: `numbers.write_hpmat` writes exactly what the calculator
would have left behind, so every path except the calculator's own arithmetic
is exercised from the PC.

The one that matters most is the generated wrapper. It is PPL that nobody
types, so if it is wrong it is wrong on the calculator, where the answer is
`syntax error` and a line number. Here it goes through the linter and then
through the kit's own interpreter, which is two gates before it is ever sent.

    python tests/test_compare.py
"""
from __future__ import unicode_literals
import io, os, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from hpkit import compare as C
from hpkit import interp, lint, numbers

PASS, FAIL = [0], [0]

LIB = """EXPORT ZAREA(r)
BEGIN
  RETURN 3.14159*r*r;
END;

EXPORT NAMED()
BEGIN
  RETURN "text";
END;
"""


def ok(cond, msg, detail=''):
    if cond:
        PASS[0] += 1
        print('  ok    %s' % msg)
    else:
        FAIL[0] += 1
        print('  FAIL  %s%s' % (msg, ('  ' + detail) if detail else ''))


def main():
    tmp = tempfile.mkdtemp(prefix='hpcmp_')
    saved = (os.environ.get('HPPRIME_EMU_ROOT'),
             os.environ.get('HPPRIME_KIT_STATE'))
    try:
        lib = os.path.join(tmp, 'LIB.txt')
        with io.open(lib, 'w', encoding='utf-8') as f:
            f.write(LIB)

        root = os.path.join(tmp, 'Calculators')
        calc = os.path.join(root, 'Prime')
        os.makedirs(calc)
        os.environ['HPPRIME_EMU_ROOT'] = root
        os.environ['HPPRIME_KIT_STATE'] = os.path.join(tmp, 'state')

        calls = ['ZAREA(2)', 'NAMED()', 'ZAREA(0)']

        # -------------------------------------------------- the wrapper
        text = C.harness(calls, 9)
        ok('EXPORT HPKCMP()' in text, 'the wrapper exports one function')
        ok(text.count('IFERR') == 3, 'one IFERR per call')
        ok('M9 := MAKEMAT(0,3,2);' in text,
           'the matrix is made the size of the run')

        whole, wrapper_from = C.program_source([lib], calls, 9)
        errors = C.lint_problems(whole, wrapper_from)
        ok(not errors, 'the generated program passes the linter',
           '; '.join(str(e) for e in errors))

        # ZAREA(0) is a call, not an index, and the linter cannot tell. Inside
        # the wrapper it has to be read as a call, or a legal call with a
        # zero argument could never be compared.
        raw = [f for f in lint.check_source('<t>', whole)[0]
               if f.rule == 'one-based']
        ok(raw, 'the linter does flag NAME(0) on its own', str(raw))
        ok(all(f.line >= wrapper_from for f in raw),
           'and every one of them is inside the generated wrapper')

        # Outside the wrapper the rule still bites.
        bad_body = ('EXPORT F()\n'
                    'BEGIN\n'
                    '  RETURN L1(0);\n'
                    'END;\n')
        ok(C.lint_problems(bad_body + C.harness(['F()']), 99),
           'index 0 in your own code is still an error')

        # And it is PPL the kit's own interpreter can run, which is a
        # stronger statement than "it parses".
        m = interp.Machine()
        m.load(whole)
        ok(m.call('HPKCMP') == 3.0, 'the wrapper runs, and reports 3 calls')
        got = m.globals_.get('M9')
        ok(got is not None, 'it filled the matrix in')
        ok(got.dim() == (3, 2), 'three rows, two columns', repr(got.dim()))
        ok(got.rows[0][0] == 1.0 and abs(got.rows[0][1] - 12.56636) < 1e-9,
           'a call that returns a number is marked 1, with its value',
           repr(got.rows[0]))
        # This interpreter lets a string be stored in a matrix cell, so the
        # wrapper's IFERR does not fire here. What the Prime does with the
        # same assignment is not measured -- and it does not have to be,
        # because what keeps a string out of the comparison is not the
        # wrapper but the type check in here(), below.
        ok(got.rows[1][1] == 'text',
           'the PC interpreter stores a string in a matrix cell',
           repr(got.rows[1]))

        # ------------------------------------------------- the PC side
        pc = C.here([lib], calls)
        ok(len(pc) == 3, 'one result per call')
        ok(abs(pc[0][1] - 12.56636) < 1e-9, 'ZAREA(2) is a number here')
        ok(pc[1][1] is None and 'not a number' in pc[1][2],
           'a string result is reported as not a number')

        # ----------------------------------------- the calculator side
        path = os.path.join(calc, 'M9.hpmat')
        try:
            C.there(calc, calls, 9)
            ok(False, 'a missing matrix is an error that says what to do')
        except C.CompareError as e:
            ok('close the emulator' in str(e),
               'a missing matrix is an error that says what to do', str(e))

        with open(path, 'wb') as f:
            f.write(numbers.write_hpmat([[1.0, 12.56636],
                                         [0.0, 0.0],
                                         [1.0, 0.0]]))
        there = C.there(calc, calls, 9)
        ok(there[0][0] == 12.56636, 'the number comes back out of the file')
        ok(there[1][0] is None and there[1][1],
           'a row marked 0 comes back as "no number"')

        with open(path, 'wb') as f:
            f.write(numbers.write_hpmat([[1.0, 1.0]]))
        try:
            C.there(calc, calls, 9)
            ok(False, 'a matrix of the wrong size is refused')
        except C.CompareError as e:
            ok('row(s)' in str(e),
               'a matrix left over from something else is refused', str(e))

        # ------------------------------------------------- the verdicts
        rows = C.verdicts([('F', 1.0, None)], [(1.0, None)])
        ok(rows[0][3] == 'same', 'the same number is "same"')
        rows = C.verdicts([('F', 1.0, None)], [(2.0, None)])
        ok(rows[0][3] == 'DIFFERENT', 'a different number is "DIFFERENT"')
        rows = C.verdicts([('F', 1.0, None)], [(1.0 + 1e-12, None)])
        ok(rows[0][3] == 'same', 'a rounding difference is not a divergence')
        rows = C.verdicts([('F', 1.0, None)], [(1.0 + 1e-3, None)])
        ok(rows[0][3] == 'DIFFERENT', 'but a real one is')
        rows = C.verdicts([('F', None, 'no')], [(None, 'no')])
        ok(rows[0][3] == 'both refused',
           'both refusing is agreement, not a failure')
        rows = C.verdicts([('F', 1.0, None)], [(None, 'no')])
        ok(rows[0][3] == 'ONE REFUSED',
           'one refusing and one answering is the interesting case')

        # Zero against zero must not divide by anything.
        rows = C.verdicts([('F', 0.0, None)], [(0.0, None)])
        ok(rows[0][3] == 'same', 'zero against zero is the same')

        ok(C.report(C.verdicts([('F', 1.0, None)], [(2.0, None)])) == 1,
           'report counts the disagreements')
        ok(C.report(C.verdicts([('F', 1.0, None)], [(1.0, None)])) == 0,
           'and counts none when there are none')

        # ---------------------------------------------------- the state
        try:
            C.load_state()
            ok(False, 'collecting before running says so')
        except C.CompareError as e:
            ok('nothing to collect' in str(e),
               'collecting before running says so', str(e))
        C.save_state({'files': [lib], 'calls': calls, 'mat': 9, 'tol': 1e-9,
                      'calc': 'Prime'})
        ok(C.load_state()['calls'] == calls, 'the calls survive to --collect')

        # ------------------------------------------------------ the cli
        with open(path, 'wb') as f:
            f.write(numbers.write_hpmat([[1.0, 12.56636],
                                         [0.0, 0.0],
                                         [1.0, 0.0]]))
        rc = C.cli(['--collect'])
        ok(rc == 0, '--collect exits 0: both sides agree, and both refuse '
                    'the call that does not give a number')

        # One side answering where the other refused is the case worth
        # exiting non-zero for.
        with open(path, 'wb') as f:
            f.write(numbers.write_hpmat([[1.0, 12.56636],
                                         [1.0, 7.0],
                                         [1.0, 0.0]]))
        ok(C.cli(['--collect']) == 1,
           'a call the PC refuses and the calculator answers is a failure')

        # Now a run where both sides agree on everything.
        C.save_state({'files': [lib], 'calls': ['ZAREA(2)'], 'mat': 9,
                      'tol': 1e-9, 'calc': 'Prime'})
        with open(path, 'wb') as f:
            f.write(numbers.write_hpmat([[1.0, 12.56636]]))
        ok(C.cli(['--collect']) == 0, '--collect exits 0 when they agree')

        with open(path, 'wb') as f:
            f.write(numbers.write_hpmat([[1.0, 99.0]]))
        ok(C.cli(['--collect']) == 1, 'and 1 when they do not')

        # A source the linter refuses must never reach the calculator.
        bad = os.path.join(tmp, 'BAD.txt')
        with io.open(bad, 'w', encoding='utf-8') as f:
            f.write('EXPORT F()\nBEGIN\n  IF 1 THEN RETURN 1; ENDIF;\nEND;')
        rc = C.cli([bad, '--call', 'F()', '--no-wait'])
        ok(rc == 1, 'a program the linter rejects is not sent')

        # The wrapper is nobody's program: it comes off once it has answered.
        wrapper = os.path.join(calc, C.NAME + '.hpprgm')
        open(wrapper, 'wb').write(b'x')
        ok(C.clean_up(calc), 'the wrapper is taken off the calculator')
        ok(not os.path.isfile(wrapper), 'and it is really gone')
        ok(not C.clean_up(calc), 'removing it twice is not an error')

        C.save_state({'files': [lib], 'calls': ['ZAREA(2)'], 'mat': 9,
                      'tol': 1e-9, 'calc': 'Prime'})
        with open(path, 'wb') as f:
            f.write(numbers.write_hpmat([[1.0, 12.56636]]))
        open(wrapper, 'wb').write(b'x')
        C.cli(['--collect'])
        ok(not os.path.isfile(wrapper), '--collect clears it too')
        open(wrapper, 'wb').write(b'x')
        C.cli(['--collect', '--keep'])
        ok(os.path.isfile(wrapper), 'unless you said --keep')
        os.remove(wrapper)

        ok(C.cli([]) == 2, 'no arguments prints the usage')
        ok(C.cli(['--help']) == 0, '--help prints the usage')
        ok(C.cli([lib]) == 2, 'files with no --call prints the usage')
    finally:
        for var, was in (('HPPRIME_EMU_ROOT', saved[0]),
                         ('HPPRIME_KIT_STATE', saved[1])):
            os.environ.pop(var, None)
            if was is not None:
                os.environ[var] = was
        shutil.rmtree(tmp, ignore_errors=True)

    print('\nPASS: %d   FAIL: %d' % (PASS[0], FAIL[0]))
    return 1 if FAIL[0] else 0


if __name__ == '__main__':
    sys.exit(main())
