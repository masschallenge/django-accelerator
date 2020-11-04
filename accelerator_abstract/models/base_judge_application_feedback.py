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

JUDGING_FEEDBACK_STATUS_COMPLETE = "COMPLETE"
JUDGING_FEEDBACK_STATUS_INCOMPLETE = "INCOMPLETE"
JUDGING_FEEDBACK_STATUS_CONFLICT = "NOT-JUDGED-CONFLICT"
JUDGING_FEEDBACK_STATUS_OTHER = "NOT-JUDGED-OTHER"
JUDGING_FEEDBACK_STATUS_ENUM = (
    (JUDGING_FEEDBACK_STATUS_COMPLETE, 'COMPLETE'),
    (JUDGING_FEEDBACK_STATUS_INCOMPLETE, 'INCOMPLETE'),
    (JUDGING_FEEDBACK_STATUS_CONFLICT, 'NOT JUDGED, CONFLICT'),
    (JUDGING_FEEDBACK_STATUS_OTHER, 'NOT JUDGED, OTHER'),)

JUDGING_STATUS_NO_CONFLICT = 1
JUDGING_STATUS_CONFLICT = 2
JUDGING_STATUS_OTHER = 3
JUDGING_STATUS_ENUM = (
    (JUDGING_STATUS_NO_CONFLICT, 'No Conflict'),
    (JUDGING_STATUS_CONFLICT, 'Not Judged - Conflict of Interest'),
    (JUDGING_STATUS_OTHER, 'Not Judged - Other (eg., no show)'),)


@python_2_unicode_compatible
class BaseJudgeApplicationFeedback(AcceleratorModel):
    application = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Application"),
        on_delete=models.CASCADE)
    form_type = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "JudgingForm"),
        on_delete=models.CASCADE)
    judge = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    panel = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Panel"),
        on_delete=models.CASCADE)
    judging_status = models.IntegerField(
        null=True,
        blank=True,
        choices=JUDGING_STATUS_ENUM)
    feedback_status = models.CharField(
        max_length=20,
        editable=False,
        choices=JUDGING_FEEDBACK_STATUS_ENUM)
    viewers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="viewed_feedback",
        db_table="accelerator_judgeapplicationfeedback_viewers")

    MANDATORY_MESSAGE = 'The question "%s" is mandatory.'
    REQUIRED_MINIMUM_MESSAGE = 'The question "%s" requires a minimum of %s %s.'
    STR_FORMAT = 'Feedback to Application %s by Judge %s'
    REQUIRED_MAXIMUM_MESSAGE = 'The question "%s" requires a maximum of %s %s.'
    REQUIRED_CHARACTER_SET_MESSAGE = ('The question "%s" must be in English'
                                      ' text')

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_judgeapplicationfeedback'
        abstract = True
        verbose_name_plural = 'Judge Application Feedback'
        unique_together = ('application', 'judge', 'panel')

    def __str__(self):
        return self.STR_FORMAT % (self.application, self.judge)
