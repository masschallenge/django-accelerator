# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import logging

import swapper
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

logger = logging.getLogger(__file__)


@python_2_unicode_compatible
class BaseNewsletterReceipt(AcceleratorModel):
    newsletter = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Newsletter'),
        on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_newsletterreceipt'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        pass

    def __str__(self):
        return "%s sent to %s" % (self.newsletter, self.recipient)
