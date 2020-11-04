# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

NEW_ENTREPRENEURS_BUCKET_TYPE = "new_entrepreneurs"
STALE_NOSTARTUP_BUCKET_TYPE = "stale_nostartup"
STALE_STARTUP_BUCKET_TYPE = "stale_startup"
UNPAID_BUCKET_TYPE = "unpaid"
UNSUBMITTED_BUCKET_TYPE = "unsubmitted"
SUBMITTED_BUCKET_TYPE = "submitted"
NEW_EXPERTS_BUCKET_TYPE = "new_experts"

# NOTE: Only add to the end of this list since the order is currently
# significant for the naming of associated ProgramRoles.  See AC-4651
# for loosening this restriction
BUCKET_TYPES = (
    (STALE_NOSTARTUP_BUCKET_TYPE, "Old Entrepreneurs"),
    (STALE_STARTUP_BUCKET_TYPE, "Old Startups"),
    (NEW_ENTREPRENEURS_BUCKET_TYPE, "New Entrepreneurs"),
    (UNPAID_BUCKET_TYPE, "Active Unpaid Startups"),
    (UNSUBMITTED_BUCKET_TYPE, "Working on Application"),
    (SUBMITTED_BUCKET_TYPE, "Has Submitted Application"),
    (NEW_EXPERTS_BUCKET_TYPE, "New Experts"),
)

EXPERTS_GROUP = "Experts"
FRESH_LEADS_GROUP = "Fresh Lead Buckets"
STALE_LEADS_GROUP = "Stale Lead Buckets"


class BaseBucketState(AcceleratorModel):
    CYCLE_BASED = "cycle"
    PROGRAM_BASED = "program"

    basis = models.CharField(
        choices=((CYCLE_BASED, "Cycle"),
                 (PROGRAM_BASED, "Program")),
        default=CYCLE_BASED,
        max_length=20
    )
    name = models.CharField(
        max_length=64,
        choices=BUCKET_TYPES,
        null=True,
        blank=True,
        default="unsubmitted",
    )
    group = models.CharField(max_length=255,
                             default="Other")
    sort_order = models.PositiveIntegerField()
    cycle = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramCycle"),
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "Program"),
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    program_role = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramRole"),
        on_delete=models.CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_bucketstate'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        ordering = ["sort_order", ]
