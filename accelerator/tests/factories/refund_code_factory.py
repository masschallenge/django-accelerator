# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
    post_generation,
)
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig
from .partner_factory import PartnerFactory

RefundCode = swapper.load_model(AcceleratorConfig.name, 'RefundCode')


class RefundCodeFactory(DjangoModelFactory):
    class Meta:
        model = RefundCode

    unique_code = Sequence(lambda n: "test_code{0}".format(n))
    issued_to = SubFactory(PartnerFactory)
    discount = 50
    maximum_uses = 1
    notes = "Notes about this refund code"
    internal = False

    @post_generation
    def programs(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for program in extracted:
                self.programs.add(program)
