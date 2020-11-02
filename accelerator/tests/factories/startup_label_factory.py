# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    post_generation,
)
from factory.django import DjangoModelFactory

StartupLabel = swapper.load_model('accelerator', 'StartupLabel')


class StartupLabelFactory(DjangoModelFactory):
    label = Sequence(lambda n: "Label {0}".format(n))

    class Meta:
        model = StartupLabel

    @post_generation
    def startups(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.startups.add(tag)
