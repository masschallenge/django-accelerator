from __future__ import unicode_literals

import swapper
from factory import (
    Iterator,
    SubFactory,
)
from factory.django import DjangoModelFactory

from .program_cycle_factory import ProgramCycleFactory
from .refund_code_factory import RefundCodeFactory
from .startup_factory import StartupFactory

RefundCodeRedemption = swapper.load_model('accelerator',
                                          'RefundCodeRedemption')


class RefundCodeRedemptionFactory(DjangoModelFactory):
    class Meta:
        model = RefundCodeRedemption

    refund_code = SubFactory(RefundCodeFactory)
    startup = SubFactory(StartupFactory)
    refund_status = ""
    refund_transaction_id = ""
    refund_amount = Iterator([10, 25, 50, 100])
    cycle = SubFactory(ProgramCycleFactory)
