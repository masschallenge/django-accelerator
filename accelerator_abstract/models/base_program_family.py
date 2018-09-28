# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseProgramFamily(AcceleratorModel):
    """An association of related programs."""

    name = models.CharField(max_length=128)
    short_description = models.TextField(
        blank=True,
        help_text="You may use HTML, including links",
    )
    url_slug = models.CharField(
        max_length=30,
        default="",
    )
    email_domain = models.CharField(
        max_length=30,
        default="",
        help_text="Base domain for role-based email"
    )
    phone_number = models.CharField(
        max_length=30,
        default="",
        help_text="Phone number for this program (local form)"
    )
    physical_address = models.TextField(
        default="",
    )
    office_hour_bcc = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        help_text="An email address to bcc whenever office hours"
                  " are created, deleted, or modified in this program family"
    )
    is_open = models.BooleanField(
        default=True,
        help_text="Whether this ProgramFamily should be available to"
                  " entrepreneurs and experts"
    )
    is_open_for_startups = models.BooleanField(
        default=False,
        help_text="Whether this ProgramFamily should be available to"
                  " entrepreneurs"
    )
    is_open_for_experts = models.BooleanField(
        default=False,
        help_text="Whether this ProgramFamily should be available to"
                  " experts"
    )

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = "program families"
        db_table = '{}_programfamily'.format(AcceleratorModel.Meta.app_label)
        abstract = True
