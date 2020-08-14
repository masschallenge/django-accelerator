# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig

ExpertInterestType = swapper.load_model(AcceleratorConfig.name,
                                        'ExpertInterestType')


class ExpertInterestTypeFactory(DjangoModelFactory):
    class Meta:
        model = ExpertInterestType

    name = Sequence(lambda n: "Expert Interest {}".format(n))
    short_description = Sequence(lambda n: "Description {}".format(n))
