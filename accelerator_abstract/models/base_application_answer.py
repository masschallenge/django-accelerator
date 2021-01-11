# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseApplicationAnswer(AcceleratorModel):
    application = models.ForeignKey(to="mc.Application"),
        on_delete=models.CASCADE)
    application_question = models.ForeignKey("mc.ApplicationQuestion"),
        on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True)

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Application Answers'
        db_table = 'accelerator_applicationanswer'
        abstract = True
        unique_together = ('application', 'application_question')

    def __str__(self):
        return "Answer to question %s from %s" % (
            self.application_question.question_number,
            self.application.startup.name)
