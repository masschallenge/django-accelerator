# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models import BasePayPalRefund
from accelerator_abstract.models.accelerator_model import AcceleratorModel
import decimal
from django.db import models


class PayPalRefund(BasePayPalRefund):
    class Meta(BasePayPalRefund.Meta):
        swappable = swapper.swappable_setting(
            BasePayPalRefund.Meta.app_label, "PayPalRefund")
