#!/usr/bin/env python

"""Test the copy of nose in this directory, by running that nose against itself.

You can test nose using nose in other ways, but if you don't use this script,
you might have one installation of nose testing another installation, which is
not supported.
"""

# More detail:

# In the absence of some sort of deep renaming magic, nose can't reasonably
# test a different installation of itself, given the existence of the global
# module registry sys.modules .

# If installed system-wide with setuptools, setuptools (via the site-packages
# easy-install.pth) takes you at your word and ensures that the installed nose
# comes first on sys.path .  So the only way to test a copy of nose other than
# the installed one is to install that version (e.g. by running python setup.py
# develop).

# This script provides a way of running nose on nose's own tests without
# installing the version to be tested, nor uninstalling the currently-installed
# version.

import glob
import os
import sys


if __name__ == "__main__":
    this_dir = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
    lib_dirs = [this_dir]
    test_dir = this_dir
    try:
        import pkg_resources
        env = pkg_resources.Environment(search_path=lib_dirs)
        distributions = env["nose3"]
        assert len(distributions) == 1, (
                "Incorrect usage of selftest.py; please see DEVELOPERS.txt")
        dist = distributions[0]
        dist.activate()
    except ImportError:
        pass
    # Always make sure our chosen test dir is first on the path
    sys.path.insert(0, test_dir)
    import nose.core
    nose.core.TestProgram()
    # nose.core.TestProgram(config=nose.core.Config(env={'NOSE_VERBOSE': 3}))
