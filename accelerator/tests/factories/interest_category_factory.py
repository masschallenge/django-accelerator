# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory


from accelerator.tests.factories.program_factory import ProgramFactory

from accelerator.models import InterestCategory


class InterestCategoryFactory(DjangoModelFactory):
    class Meta:
        model = InterestCategory

    name = Sequence(lambda n: "Interest Category {0}".format(n))
    program = SubFactory(ProgramFactory)
