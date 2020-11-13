# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

JudgingForm = swapper.load_model('accelerator', 'JudgingForm')


class JudgingFormFactory(DjangoModelFactory):
    class Meta:
        model = JudgingForm

    name = Sequence(lambda n: "Judging Form {0}".format(n))
    description = Sequence(lambda n: "Judging Form Description {0}".format(n))
