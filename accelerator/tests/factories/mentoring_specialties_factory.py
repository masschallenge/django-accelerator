# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig

MentoringSpecialties = swapper.load_model(AcceleratorConfig.name,
                                          'MentoringSpecialties')


class MentoringSpecialtiesFactory(DjangoModelFactory):
    class Meta:
        model = MentoringSpecialties

    name = Sequence(lambda n: "Mentoring Specialties {0}".format(n))
