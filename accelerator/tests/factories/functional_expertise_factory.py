# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    post_generation,
)
from factory.django import DjangoModelFactory

FunctionalExpertise = swapper.load_model('accelerator',
                                         'FunctionalExpertise')


class FunctionalExpertiseFactory(DjangoModelFactory):
    class Meta:
        model = FunctionalExpertise

    name = Sequence(lambda n: "Functional Expertise {0}".format(n))

    @post_generation
    def parent(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.parent = extracted
