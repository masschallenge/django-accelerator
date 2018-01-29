# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
import re

JUDGE_FEEDBACK_REVIEWER = "_RESTRICTED_: Judge Feedback Reviewer"
JUDGE_FEEDBACK_SANITIZER = "_CAUTION_: Judge Feedback Sanitizer"

@python_2_unicode_compatible
class BaseJudgeFeedbackComponent(AcceleratorModel):
    judge_feedback = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "JudgeApplicationFeedback"))
    feedback_element = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "JudgingFormElement"))
    answer_text = models.CharField(max_length=2000, blank=True)
    original_answer_text = models.CharField(max_length=2000, blank=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_judgefeedbackcomponent'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = 'Feedback Components'
        unique_together = ('judge_feedback', 'feedback_element')

    def __str__(self):
        return "Feedback for component %s from %s" % (
            self.feedback_element.element_number,
            self.judge_feedback.judge)
