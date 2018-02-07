# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

ExpertCategory = swapper.load_model(AcceleratorConfig.name, 'ExpertCategory')


class ExpertCategoryFactory(DjangoModelFactory):
    class Meta:
        model = ExpertCategory

    name = Sequence(lambda n: 'Expert Category {0}'.format(n))
