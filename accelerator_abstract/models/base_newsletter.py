# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

FIRST_NAME = 1
LAST_NAME = 2
EMAIL = 0

EMAIL_TEMPLATE = "newsletter/newsletter_email.html"


class BaseNewsletter(AcceleratorModel):
    name = models.CharField(max_length=127)
    subject = models.CharField(
        max_length=500,  # long to allow for template code
        blank=True,
        help_text='Best practice: keep subject lines short')
    from_addr = models.CharField(
        max_length=255,
        blank=True,
        null=True)
    recipient_roles = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'ProgramRole'),
        limit_choices_to={
            'newsletter_recipient': True,
        },
        blank=True)
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"))
    judging_round = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgingRound"),
        null=True,
        blank=True)
    cc_addrs = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Zero or more email addresses to CC; separate with commas")
    date_mailed = models.DateTimeField(blank=True, null=True, editable=False)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_newsletter'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        ordering = ('-created_at', 'name',)
