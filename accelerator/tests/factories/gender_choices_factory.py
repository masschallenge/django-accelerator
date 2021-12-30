from __future__ import unicode_literals

import swapper

from factory import Sequence
from factory.django import DjangoModelFactory

GenderChoices = swapper.load_model('accelerator', 'GenderChoices')


class GenderChoicesFactory(DjangoModelFactory):
    class Meta:
        model = GenderChoices
    name = Sequence(lambda n: "test_choice{0}".format(n))
