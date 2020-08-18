# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.user_label_factory import UserLabelFactory
from accelerator.tests.factories.user_role_factory import UserRoleFactory

ProgramRole = swapper.load_model(AcceleratorConfig.name, 'ProgramRole')


class ProgramRoleFactory(DjangoModelFactory):
    class Meta:
        model = ProgramRole

    program = SubFactory(ProgramFactory)
    name = Sequence(lambda n: "Program Role {0}".format(n))
    user_role = SubFactory(UserRoleFactory)
    user_label = SubFactory(UserLabelFactory)
    landing_page = None
