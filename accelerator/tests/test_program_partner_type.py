from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ProgramPartnerTypeFactory


class TestProgramPartnerType(TestCase):

    def test_str(self):
        program_partner_type = ProgramPartnerTypeFactory()
        assert program_partner_type.partner_type in str(program_partner_type)
        assert program_partner_type.program.name in str(program_partner_type)
