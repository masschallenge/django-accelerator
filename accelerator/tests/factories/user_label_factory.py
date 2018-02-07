# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    post_generation,
)

from accelerator.apps import AcceleratorConfig

UserLabel = swapper.load_model(AcceleratorConfig.name, 'UserLabel')


class UserLabelFactory(DjangoModelFactory):
    label = Sequence(lambda n: "Label {0}".format(n))

    class Meta:
        model = UserLabel

    @post_generation
    def startups(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.startups.add(tag)
