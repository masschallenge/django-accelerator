from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories import (
    ExpertFactory,
)
from accelerator.tests.factories.expert_interest_type_factory import (
    ExpertInterestTypeFactory
)
from accelerator.tests.factories.program_family_factory import (
    ProgramFamilyFactory
)

ExpertInterest = swapper.load_model('accelerator', 'ExpertInterest')


class ExpertInterestFactory(DjangoModelFactory):
    class Meta:
        model = ExpertInterest

    user = SubFactory(ExpertFactory)
    program_family = SubFactory(ProgramFamilyFactory)
    interest_type = SubFactory(ExpertInterestTypeFactory)
    topics = Sequence(lambda n: "Expert Interest Topic {}".format(n))
