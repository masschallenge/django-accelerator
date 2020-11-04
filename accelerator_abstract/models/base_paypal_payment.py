# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import decimal

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


# Conforming to the django-paypal convention of using
# PayPal in CamelCase and paypal in snake_case.@python_2_unicode_compatible
class BasePayPalPayment(AcceleratorModel):
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"),
        on_delete=models.CASCADE)
    cycle = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramCycle"),
        on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    transaction = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=7,
                                 decimal_places=2,
                                 default=decimal.Decimal("0.00"))
    currency_code = models.CharField(max_length=3, default='')
    refundable = models.BooleanField(default=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_paypalpayment'
        abstract = True
