# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from accelerator_abstract.models import BasePayPalPayment


class PayPalPayment(BasePayPalPayment):
    class Meta(BasePayPalPayment.Meta):
        db_table = '{}_paypalpayment'.format(
            BasePayPalPayment.Meta.app_label, "PaypalPayment")
