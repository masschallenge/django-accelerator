# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from .program_cycle_factory import ProgramCycleFactory
from .startup_factory import StartupFactory

PayPalPayment = swapper.load_model('accelerator', 'PayPalPayment')


class PayPalPaymentFactory(DjangoModelFactory):
    class Meta:
        model = PayPalPayment

    startup = SubFactory(StartupFactory)
    cycle = SubFactory(ProgramCycleFactory)
    token = Sequence(lambda n: "PayPal Token {0}".format(n))
    transaction = Sequence(lambda n: "PayPal Transaction {0}".format(n))
    amount = 99.0
    currency_code = "USD"
    refundable = True
