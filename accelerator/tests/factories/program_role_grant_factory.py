# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

ProgramRoleGrant = swapper.load_model(AcceleratorConfig.name,
                                      'ProgramRoleGrant')

from accelerator.tests.factories.member_factory import MemberFactory
from accelerator.tests.factories.program_role_factory import ProgramRoleFactory


class ProgramRoleGrantFactory(DjangoModelFactory):
    class Meta:
        model = ProgramRoleGrant

    person = SubFactory(MemberFactory)
    program_role = SubFactory(ProgramRoleFactory)
