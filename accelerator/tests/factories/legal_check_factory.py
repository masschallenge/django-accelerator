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
    description = Sequence(
        lambda n: 'I accept the terms specified by '
                  '<a href="http://example.com/legal-{0}" '
                  'target="_blank">legal_check_{0}</a>'.format(n))
    is_enabled_for_experts = True
    is_enabled_for_entrepreneurs = True
