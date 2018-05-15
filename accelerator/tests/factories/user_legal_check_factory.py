# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.legal_check_factory import (
    LegalCheckFactory
)
from simpleuser.tests.factories.user_factory import UserFactory

UserLegalCheck = swapper.load_model(AcceleratorConfig.name, 'UserLegalCheck')


class UserLegalCheckFactory(DjangoModelFactory):
    class Meta:
        model = UserLegalCheck

    user = SubFactory(UserFactory)
    legal_check = SubFactory(LegalCheckFactory)
    accepted = False
