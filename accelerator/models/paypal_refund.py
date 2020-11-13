# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models import BasePayPalRefund


class PayPalRefund(BasePayPalRefund):
    class Meta(BasePayPalRefund.Meta):
        swappable = swapper.swappable_setting(
            BasePayPalRefund.Meta.app_label, "PayPalRefund")
