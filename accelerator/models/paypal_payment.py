# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from accelerator_abstract.models import BasePayPalPayment
import swapper


class PayPalPayment(BasePayPalPayment):
    class Meta(BasePayPalPayment.Meta):
        swappable = swapper.swappable_setting(
            BasePayPalPayment.Meta.app_label, "PayPalPayment")
