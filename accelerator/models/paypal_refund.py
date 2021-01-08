# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BasePayPalRefund


class PayPalRefund(BasePayPalRefund):
    class Meta(BasePayPalRefund.Meta):
        swappable = False
