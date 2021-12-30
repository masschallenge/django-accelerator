from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

ExpertInterestType = swapper.load_model('accelerator', 'ExpertInterestType')


class ExpertInterestTypeFactory(DjangoModelFactory):
    class Meta:
        model = ExpertInterestType

    name = Sequence(lambda n: "Expert Interest {}".format(n))
    short_description = Sequence(lambda n: "Description {}".format(n))
