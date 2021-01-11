# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import MentoringSpecialties


class MentoringSpecialtiesFactory(DjangoModelFactory):
    class Meta:
        model = MentoringSpecialties

    name = Sequence(lambda n: "Mentoring Specialties {0}".format(n))
