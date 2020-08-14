# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig

JudgingForm = swapper.load_model(AcceleratorConfig.name, 'JudgingForm')


class JudgingFormFactory(DjangoModelFactory):
    class Meta:
        model = JudgingForm

    name = Sequence(lambda n: "Judging Form {0}".format(n))
    description = Sequence(lambda n: "Judging Form Description {0}".format(n))
