# -*- coding: utf-8 -*-

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

JudgingForm = swapper.load_model(AcceleratorConfig.name, 'JudgingForm')


class JudgingFormFactory(DjangoModelFactory):
    class Meta:
        model = JudgingForm

    name = Sequence(lambda n: "Judging Form {0}".format(n))
    description = Sequence(lambda n: "Judging Form Description {0}".format(n))
