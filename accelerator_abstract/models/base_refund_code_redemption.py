# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import decimal

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.models.base_application import REFUND_STATUSES

CREDIT_CODE_NOT_AVAILABLE = ("Apologies, credit code %s "
                             "is no longer available")


@python_2_unicode_compatible
class BaseRefundCodeRedemption(AcceleratorModel):
    refund_code = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "RefundCode"),
        related_name="redemptions", on_delete=models.CASCADE)

    cycle = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramCycle"),
        on_delete=models.CASCADE)
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"),
        blank=True, null=True, on_delete=models.CASCADE)
    refund_status = models.CharField(
        max_length=32,
        choices=REFUND_STATUSES,
        blank=True,
    )
    refund_transaction_id = models.CharField(max_length=500, blank=True)

    # refund_amount is deprecated and should be removed
    refund_amount = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=decimal.Decimal("0.00"),
    )

    class Meta(AcceleratorModel.Meta):
        unique_together = ("startup", "refund_code", "cycle")
        db_table = "{}_refundcoderedemption".format(
            AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        return "{} redeemed by {}".format(self.refund_code.unique_code,
                                          self.startup)
