# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories import (
    ExpertFactory,
)
from accelerator.tests.factories.expert_interest_type_factory import (
    ExpertInterestTypeFactory
)
from accelerator.tests.factories.program_family_factory import (
    ProgramFamilyFactory
)

ExpertInterest = swapper.load_model(AcceleratorConfig.name, 'ExpertInterest')


class ExpertInterestFactory(DjangoModelFactory):
    class Meta:
        model = ExpertInterest

    user = SubFactory(ExpertFactory)
    program_family = SubFactory(ProgramFamilyFactory)
    interest_type = SubFactory(ExpertInterestTypeFactory)
    topics = Sequence(lambda n: "Expert Interest Topic {}".format(n))
