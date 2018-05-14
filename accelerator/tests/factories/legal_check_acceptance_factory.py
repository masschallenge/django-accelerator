# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.entrepreneur_profile_factory import (
    EntrepreneurProfileFactory
)
from accelerator.tests.factories.legal_check_factory import (
    LegalCheckFactory
)

LegalCheckAcceptance = swapper.load_model(AcceleratorConfig.name,
                                          'LegalCheckAcceptance')


class LegalCheckAcceptanceFactory(DjangoModelFactory):
    class Meta:
        model = LegalCheckAcceptance

    profile = SubFactory(EntrepreneurProfileFactory)
    legal_check = SubFactory(LegalCheckFactory)
    accepted = False
