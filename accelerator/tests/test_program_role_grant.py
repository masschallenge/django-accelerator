# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from .factories import (
    ProgramRoleGrantFactory,
)


class TestProgramRoleGrant(TestCase):

    def test_str(self):
        grant = ProgramRoleGrantFactory()
        assert grant.program_role.name in str(grant)
