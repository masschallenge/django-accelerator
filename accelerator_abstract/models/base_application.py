# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import logging

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

logger = logging.getLogger(__file__)

ERROR_PAYMENT_STATUS = "error"
PAID_PAYMENT_STATUS = "paid"
UNPAID_PAYMENT_STATUS = "unpaid"
PAYMENT_STATUSES = ((PAID_PAYMENT_STATUS, "Paid"),
                    (UNPAID_PAYMENT_STATUS, "Unpaid"),
                    (ERROR_PAYMENT_STATUS, "Payment Error"))

COMPLETE_APP_STATUS = "complete"
INCOMPLETE_APP_STATUS = "incomplete"
SUBMITTED_APP_STATUS = "submitted"
APPLICATION_STATUSES = ((INCOMPLETE_APP_STATUS, "Incomplete"),
                        (COMPLETE_APP_STATUS, "Complete"),
                        (SUBMITTED_APP_STATUS, "Submitted"))

DELAYED_STATUS = "delayed"
FAILED_STATUS = "failed"
INSTANT_STATUS = "instant"
NOT_ELIGIBLE_STATUS = "not_eligible"
REQUIRED_STATUS = "required"
REFUND_STATUSES = ((NOT_ELIGIBLE_STATUS, "Not Eligible For Refund"),
                   (REQUIRED_STATUS, "Refund Due"),
                   (INSTANT_STATUS, "Refund Issued"),
                   (DELAYED_STATUS, "Refund Pending"),
                   (FAILED_STATUS, "Refund Failed"))


@python_2_unicode_compatible
class BaseApplication(AcceleratorModel):
    cycle = models.ForeignKey(swapper.get_model_name('accelerator',
                                                     'ProgramCycle'),
                              blank=True,
                              null=True,
                              related_name='applications',
                              on_delete=models.CASCADE)
    startup = models.ForeignKey(
        swapper.get_model_name('accelerator', 'Startup'),
        on_delete=models.CASCADE)
    application_type = models.ForeignKey(swapper.get_model_name(
        'accelerator', 'ApplicationType'),
        on_delete=models.CASCADE)
    application_status = models.CharField(
        blank=True,
        null=True,
        max_length=64,
        choices=APPLICATION_STATUSES
    )
    submission_datetime = models.DateTimeField(blank=True, null=True)

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Applications'
        ordering = ['startup']
        db_table = '{}_application'.format(AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        return '%s for %s by %s' % (self.application_type.name,
                                    self.cycle.name,
                                    self.startup.organization.name)
