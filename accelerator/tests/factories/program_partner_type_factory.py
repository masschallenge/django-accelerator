from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories import ProgramFactory

ProgramPartnerType = swapper.load_model('accelerator', 'ProgramPartnerType')


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
