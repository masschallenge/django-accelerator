# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


# DO NOT DELETE NEXT LINE:
# It is necessary to be able to mock out PayPalWPP

@python_2_unicode_compatible
class BaseRefundCode(AcceleratorModel):
    unique_code = models.CharField(max_length=100, unique=True)
    programs = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Program'),
        help_text=("Which programs is this refund code valid for? "
                   "If no programs are given, then this code can be "
                   "applied to any program."),
        related_name="refund_codes",
        blank=True
    )
    issued_to = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Partner"),
        blank=True, null=True, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    maximum_uses = models.PositiveIntegerField(
        verbose_name='Maximum Uses',
        help_text=('Indicate the maximum number of valid redemptions for '
                   'this code. A null value is interpreted as unlimited.'),
        default=1,
        blank=True,
        null=True,
    )
    notes = models.CharField(max_length=300, blank=True)
    internal = models.BooleanField(
        default=False,
        help_text=("If set then this code is intended for internal use "
                   "(e.g, Early Bird discount) and cannot be entered "
                   "directly by users."))

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_refundcode'
        abstract = True
        verbose_name_plural = 'Refund Codes'

    def __str__(self):
        return self.unique_code
