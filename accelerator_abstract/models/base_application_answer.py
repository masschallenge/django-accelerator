# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.querysets.application_answer_queryset import (
    ApplicationAnswerQuerySet
)


@python_2_unicode_compatible
class BaseApplicationAnswer(AcceleratorModel):
    application = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "Application"))
    application_question = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, 'ApplicationQuestion'))
    answer_text = models.CharField(max_length=2000, blank=True)

    objects = ApplicationAnswerQuerySet.as_manager()

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Application Answers'
        db_table = 'accelerator_applicationanswer'
        abstract = True

    def __str__(self):
        return "Answer to question %s from %s" % (
            self.application_question.question_number,
            self.application.startup.name)
