# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import JudgingForm


class JudgingFormFactory(DjangoModelFactory):
    class Meta:
        model = JudgingForm

    name = Sequence(lambda n: "Judging Form {0}".format(n))
    description = Sequence(lambda n: "Judging Form Description {0}".format(n))
