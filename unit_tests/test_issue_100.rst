This is a test of the bug reported in issue 100: test.address() fails
for a case defined in a doctest.

    >>> import unittest
    >>> import nose.case
    >>> class SimpleTest(unittest.TestCase):
    ...
    ...     def runTest(self):
    ...         pass
    >>> test = nose.case.Test(SimpleTest())
    >>> test.address()[0]
    >>> test.address()[1] in ('builtins', '__builtin__')
    True
    >>> test.address()[2]
    'SimpleTest.runTest'
