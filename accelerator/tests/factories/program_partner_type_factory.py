# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories import ProgramFactory

ProgramPartnerType = swapper.load_model(AcceleratorConfig.name,
                                        'ProgramPartnerType')


class ProgramPartnerTypeFactory(DjangoModelFactory):
    class Meta:
        model = ProgramPartnerType

    partner_type = Sequence(lambda n: 'Test Partner Type %d' % n)
    program = SubFactory(ProgramFactory)
    description = Sequence(
        lambda n: "Description of Program Partner Type #{0}".format(n))
    feature_in_footer = False
    sort_order = 1
    badge_image = None
    badge_display = "NONE"
