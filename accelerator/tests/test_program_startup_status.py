# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from .factories import (
    ProgramStartupStatusFactory,
)


class TestProgramStartupStatus(TestCase):

    def test_str(self):
        pss = ProgramStartupStatusFactory()
        assert pss.startup_status in str(pss)
