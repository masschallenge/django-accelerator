from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory


from accelerator.tests.factories.program_factory import ProgramFactory

InterestCategory = swapper.load_model('accelerator', 'InterestCategory')


class InterestCategoryFactory(DjangoModelFactory):
    class Meta:
        model = InterestCategory

    name = Sequence(lambda n: "Interest Category {0}".format(n))
    program = SubFactory(ProgramFactory)
