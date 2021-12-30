from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    post_generation,
)
from factory.django import DjangoModelFactory

PartnerLabel = swapper.load_model('accelerator', 'PartnerLabel')


class PartnerLabelFactory(DjangoModelFactory):
    label = Sequence(lambda n: "Label {0}".format(n))

    class Meta:
        model = PartnerLabel

    @post_generation
    def partners(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.partners.add(tag)
