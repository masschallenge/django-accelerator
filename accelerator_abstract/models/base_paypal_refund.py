# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
import decimal
from django.db import models


# Conforming to the django-paypal convention of using
# PayPal in CamelCase and paypal in snake_case.@python_2_unicode_compatible
class BasePayPalRefund(AcceleratorModel):
    payment = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "PayPalPayment"))
    status = models.CharField(max_length=100, blank=True)
    transaction = models.CharField(max_length=100, blank=True)
    correlation = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=7,
                                 decimal_places=2,
                                 default=decimal.Decimal("0.00"))

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_paypalrefund'.format(AcceleratorModel.Meta.app_label)
        abstract = True
