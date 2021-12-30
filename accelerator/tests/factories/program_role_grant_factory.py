from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories.member_factory import MemberFactory
from accelerator.tests.factories.program_role_factory import ProgramRoleFactory

ProgramRoleGrant = swapper.load_model('accelerator', 'ProgramRoleGrant')


class ProgramRoleGrantFactory(DjangoModelFactory):
    class Meta:
        model = ProgramRoleGrant

    person = SubFactory(MemberFactory)
    program_role = SubFactory(ProgramRoleFactory)
