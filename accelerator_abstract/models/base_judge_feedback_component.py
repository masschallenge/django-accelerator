# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

JUDGE_FEEDBACK_REVIEWER = "_RESTRICTED_: Judge Feedback Reviewer"
JUDGE_FEEDBACK_SANITIZER = "_CAUTION_: Judge Feedback Sanitizer"

DEFINITELY_RECOMMEND = "Definitely Recommend"
STRONGLY_RECOMMEND = "Strongly Recommend"
RECOMMEND = "Recommend"
DONT_RECOMMEND = "Don't Recommend"
STRONGLY_DONT_RECOMMEND = "Strongly Don't Recommend"
DEFINITELY_DONT_RECOMMEND = "Definitely Don't Recommend"

@python_2_unicode_compatible
class BaseJudgeFeedbackComponent(AcceleratorModel):
    judge_feedback = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgeApplicationFeedback"))
    feedback_element = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgingFormElement"))
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
