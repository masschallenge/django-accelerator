#!/usr/bin/env python
# This script is derived from:
# https://github.com/pinax/pinax-notifications/blob/master/runtests.py
# which is copyright (c) 2012-2016 James Tauber and contributors and
# available under the MIT license.
# All changes that are copyrighted by MassChallenge, Inc. are also
# made available under the MIT license.

import os
import sys

import django

from django.conf import settings

from shared_settings import DEFAULT_SETTINGS


def runtests(*test_args):
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    try:
        from django.test.runner import DiscoverRunner
        runner_class = DiscoverRunner
        test_args = ["accelerator.tests"]
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner
        runner_class = DjangoTestSuiteRunner
        test_args = ["tests"]

    failures = runner_class(verbosity=1, interactive=True,
                            failfast=False).run_tests(test_args)
    sys.exit(failures)


if __name__ == "__main__":
    runtests(*sys.argv[1:])
