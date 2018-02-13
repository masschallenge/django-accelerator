# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    ProgramPartnerFactory,
)


class TestProgramPartner(TestCase):

    def test_str(self):
        program_partner = ProgramPartnerFactory()
        assert program_partner.partner_type.partner_type in str(
            program_partner)
        assert program_partner.partner.name in str(program_partner)
        assert program_partner.program.name in str(program_partner)
