from __future__ import print_function
import sys
called = []

_multiprocess_ = 1

def setup():
    print("setup called", file=sys.stderr)
    called.append('setup')


def teardown():
    print("teardown called", file=sys.stderr)
    called.append('teardown')


def test_a():
    assert len(called) == 1, "len(%s) !=1" % called


def test_b():
    assert len(called) == 1, "len(%s) !=1" % called


class TestMe:
    def setup_class(cls):
        cls._setup = True
    setup_class = classmethod(setup_class)

    def test_one(self):
        assert self._setup, "Class was not set up"
