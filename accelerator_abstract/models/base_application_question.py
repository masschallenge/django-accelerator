# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import swapper

from django.db import models
from accelerator_abstract.models.base_question import (
    CHOICE_LAYOUTS,
    QUESTION_TYPES,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel

CHARACTERS_UNIT_NAME = "Characters"
WORDS_UNIT_NAME = "Words"
TEXT_LIMIT_UNITS = ((CHARACTERS_UNIT_NAME.lower(), CHARACTERS_UNIT_NAME),
                    (WORDS_UNIT_NAME.lower(), WORDS_UNIT_NAME))


@python_2_unicode_compatible
class BaseApplicationQuestion(AcceleratorModel):
    application_type = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "ApplicationType"))
    program = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "Program"),
        blank=True,
        null=True)
    question_number = models.IntegerField()
    section_heading = models.CharField(max_length=40, blank=True)
    question_text = models.CharField(max_length=200, blank=True)
    help_text = models.CharField(max_length=1000, blank=True)
    # To be removed:
    question_type = models.CharField(
        max_length=64,
        choices=QUESTION_TYPES,
    )
    mandatory = models.BooleanField(default=False)
    text_box_lines = models.IntegerField(blank=True)
    text_limit = models.IntegerField(blank=True)
    text_limit_units = models.CharField(
        max_length=64,
        choices=TEXT_LIMIT_UNITS,
        blank=True,
    )
    # To be removed:
    choice_options = models.CharField(max_length=4000, blank=True)
    # To be removed:
    choice_layout = models.CharField(
        max_length=64,
        choices=CHOICE_LAYOUTS,
        blank=True,
    )
    question = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "Question"),
        blank=True,
        null=True)

    class Meta(AcceleratorModel.Meta):
        abstract = True
        db_table = '{}_applicationquestion'.format(
            AcceleratorModel.Meta.app_label)
        ordering = ["application_type", "question_number", ]
        verbose_name_plural = "Application Questions"

    STR_FORMAT = "Question %s (%s) from the %s"

    def __str__(self):
        return self.STR_FORMAT % (
            self.question_number,
            self.question_text[:10],
            self.application_type.name)

    def parsed_choices(self):
        return self.choice_options.split("|")
