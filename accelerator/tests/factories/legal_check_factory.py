# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

LegalCheck = swapper.load_model(AcceleratorConfig.name, 'LegalCheck')


class LegalCheckFactory(DjangoModelFactory):
    class Meta:
        model = LegalCheck

    name = Sequence(lambda n: 'legal_check_{0}'.format(n))
    title = Sequence(lambda n: 'The Website Legal {0} Check'.format(n))
    url = Sequence(lambda n: 'http://example.com/legal-{0}'.format(n))
    accepted = False
